// Author: Adrian Bleul

//@implements: sampler2D
struct TriNoise2 {
	sampler2D sampler;
	//@ label: "time", editor: range, min: 0, max: 100, range_min: 0, range_max: 1, range_default: 1
	float time;
	//@ label: "amount", editor: range, min: 2, max: 200, range_min: 2, range_max: 200, range_default: 50
	float amount;
	//@ label: "Mix", editor: range, min: -20.0, max: 0.0, range_min: 1, range_max: 100, range_default: 75
	float noiseScale;
};
//Declaring some Variables because it's much faster to do it here than in the loops


vec4 Color;

float BaryA;
float BaryB;
float BaryC;
vec3 mid;

vec2 BaryP;
vec3 U;
vec3 V;
vec3 normal;

float ankathete;
float normalAngle;
float normalAngleCorrected;

//Genereric random function (deterministic)
float randomNoII(vec2 seed) {
    return fract(sin(dot(seed.xy,
                         vec2(12.9898,78.233)))*
        43758.5453123);
}

//Generic noise function (also deterministic)
float noise_NoII(in vec2 st) {
    vec2 i = floor(st);
    vec2 f = fract(st);

    float a = randomNoII(i);
    float b = randomNoII(i + vec2(1.0, 0.0));
    float c = randomNoII(i + vec2(0.0, 1.0));
    float d = randomNoII(i + vec2(1.0, 1.0));

    vec2 u = f*f*(3.0-2.0*f);

    return mix(a, b, u.x) + 
            (c - a)* u.y * (1.0 - u.x) + 
            (d - b) * u.x * u.y;
}

//2nd random function (it only needs a seed, not a vec2)
float randNoII(float seed){
	 return fract(sin(seed)*10000.0);
}
 
mat2 rotate2d_NoII(float _angle){
    return mat2(cos(_angle),-sin(_angle),
                sin(_angle),cos(_angle));
}
//Function for drawing Lines (Useful for debuging, but also cool wireframe effect)
float drawLineNoII(in vec2 p1, in vec2 p2, vec2 tex_coords){
    vec2 st = tex_coords.xy;
    
    vec2 bo1;
    vec2 bo2;
     
    vec2 topPoint = (step(p2.y, p1.y)*p1) + (step(p1.y, p2.y)*p2);
    vec2 bottomPoint = (step(p2.y, p1.y)*p2) + (step(p1.y, p2.y)*p1);
    
    if(topPoint == bottomPoint){
        topPoint = p1;
        bottomPoint = p2;
    }
    
    float winkel = asin((bottomPoint.x - topPoint.x)/(distance(topPoint, bottomPoint)));
    
    st -= bottomPoint;
    st = vec2(rotate2d_NoII( winkel)*st);
    st.y += bottomPoint.y;
    

	bo1.x = step(-0.0005, st.x);
	bo1.y = step(bottomPoint.y, st.y);
	bo2.x = step(0.9995, 1.0 - st.x);

	
    st.y -= bottomPoint.y;
    st = vec2(rotate2d_NoII(-winkel)*st);
    st += bottomPoint;
    
    st -= topPoint;
    st = vec2(rotate2d_NoII( winkel)*st);
    st.y += topPoint.y;
    
    bo2.y = step(1.0 - topPoint.y, 1.0 - st.y);
    
    st.y -= topPoint.y;
    st = vec2(rotate2d_NoII(- winkel)*st);
    st += topPoint;
    
    return bo1.x * bo1.y * bo2.x * bo2.y;
}
//Checks if point is in Triangle based on barycentric Coordinates   
float inTriNoII(vec3 baryCoords){
    mid = vec3(0.5);
    mid =  step(abs(baryCoords-mid),mid);
   	return mid.x * mid.y * mid.z;
}

//Calculating the barycentric Coordinates and lightmass of each Triangle.
//The function needs two sets of data for textureinterpolation: the transformed verticies of an triangle and its origin coordinates
vec4 baryCoordsNoII(vec3 A, vec3 B, vec3 C, vec2 a, vec2 b, vec2 c, vec2 tex_coords, TriNoise2 s){
    
    vec2 P = tex_coords;
    
    float denom = 1.0 / (((B.y - C.y) * (A.x - C.x)) + ((C.x - B.x) * (A.y - C.y)));
       	
    BaryA = (((B.y - C.y) * (P.x - C.x)) + ((C.x - B.x) * (P.y - C.y)))*denom;
        	
    
    BaryB = (((C.y - A.y) * (P.x - C.x)) + ((A.x - C.x) * (P.y - C.y)))*denom;
        	
    
    BaryC = 1.0 - BaryA - BaryB;
    
    if(inTriNoII(vec3(BaryA, BaryB, BaryC)) != .0){
        BaryP;
        /*
        if(s.softShadow > 0.0){
    		U = B - A;
	    	V = C - A;
	    	normal.x = (U.y * V.z) - (U.z * V.y);
	    	normal.y = (U.z * V.x) - (U.x * V.z);
	    	normal.z = (U.x * V.y) - (U.y * V.x);
			ankathete = (sqrt((normal.x * normal.x) + (normal.y * normal.y)));
			normalAngle = ankathete*(inversesqrt((ankathete * ankathete) + (normal.z * normal.z)));
			normalAngleCorrected = cos(90.0 - acos(normalAngle)) ;
		}else{
			normalAngleCorrected = 1.0;
		}
		*/
		normalAngleCorrected = 1.0;
		BaryP = P ;
		Color = vec4(texture(s.sampler, BaryP).rgb*normalAngleCorrected,1.0);
		 return Color;
		}else{
			return vec4(0.0);
		}
}
//Main function
vec4 texture(TriNoise2 s, vec2 tex_coords){
	
	int countTris = int(s.amount);
	float maxOffset = 1.0;
	//While developing this the visual style was targeted at 16:9 screens, so are the proportions, that's why I added
	//the factor from 9:16 on the given aspectratio, so it will always look the same.
	float aspectFaktor = 1.0 / 0.5625;
	float aspectRatio = (1080/1920.0);
	int countTrisY = int(countTris * (aspectRatio * aspectFaktor)); 
	int offOne = int(step(0.6, maxOffset));
	
	//The maxOffset is calculated so later the algorithm can calculate how far it has to look for matching triangle.
	maxOffset *= 0.4/countTris;
	
	
	
	int CountTrisRow = ((countTris * 2)+1);
	float CTR = 1. / CountTrisRow;
	
	float speedTime = s.time;;
	
	vec2 st = tex_coords;
    vec4 color = vec4(0.0);
    
    float Ffaktor;
    
    vec4 overload;
    
    vec3 A;
    vec3 B;
    vec3 C;
    
    vec2 a;
    vec2 b;
    vec2 c;
    
    float AxOff;
	float AyOff;
	
	float BxOff;
	float ByOff;
	
	float CxOff;
	float CyOff;
	
	float Arand;
	float Brand;
	float Crand;
	
	float countArand;
	float countBrand;
	float countCrand;
	
	float Aoffset;
	float Boffset;
	float Coffset;
    
    float iX = floor(st.x * float(CountTrisRow));
    float iY = floor((1.0 - st.y) * float(countTrisY));
	
    int rowCount = int(iY) + 1;
    
    int index = int(iX) + (int(iY) * CountTrisRow);
    
    
    
    index -= int(step(0.5, float(index))) * (2 + offOne) ;
    int oldIndex = index;
    int countA;
    int countB;
    int countC;
   
    float rowFak = float(countTris) + 1.5;
    
    float rowA;
    float rowB;
    float rowC;    
    float Div = 1.0 / countTris;
    float offset = Div * 0.5;
    float DivY = 1.0 / countTrisY;
    
    
    
    int faktor;
    int amount;
    int rowInCount;
    float dis = distance(st, vec2(0.5, 0.5));
    int backIndex = index - CountTrisRow;
    amount = index + 4 + offOne;
    
    
    //Welcome to the Loops. Each Loop does basically the same:
    //looking up if the point we are looking at is in one of the calculated triangles.
    //The first loop checks for the tris in the column where the calculation says the point should be at
    for(index; index < amount; index++){
    	
    	faktor = int(index * CTR);
    	countA = int(index * 0.5);
    	countB = ((((index - 1)%2)*((countTris + 1)+countA)) + ((index % 2)*(countA +1)));
    	countC = ((countTris + 2) + countA);
    	
    	Ffaktor = float(faktor);
    	
    	countA += faktor;
    	countB += faktor;
    	countC += faktor;
    	
    	rowA = Ffaktor;
    	rowB = Ffaktor + float(((index + 1) % 2));
    	rowC = Ffaktor + 1;
		
    	A.x = ((countA - int(rowA * rowFak))*Div)-((int(rowA) % 2)*offset);
    	A.y = 1.0 - (rowA * DivY);
    	
    	B.x = ((countB - int(rowB * rowFak))*Div)-((int(rowB) % 2)*offset);
    	B.y = 1.0 - (rowB * DivY);
    	
    	C.x = ((countC - int(rowC * rowFak))*Div)-((int(rowC) % 2)*offset);
    	C.y = 1.0 - (rowC * DivY);
    	
    	AxOff = step(0.001, A.x) * step(A.x, 0.999);
    	AyOff = step(0.001, A.y) * step(A.y, 0.999);
    	
    	BxOff = step(0.001, B.x) * step(B.x, 0.999);
    	ByOff = step(0.001, B.y) * step(B.y, 0.999);
    	
    	CxOff = step(0.001, C.x) * step(C.x, 0.999);
    	CyOff = step(0.001, C.y) * step(C.y, 0.999);
    	
    	Arand = randomNoII(A.xy);
    	Brand = randomNoII(B.xy);
    	Crand = randomNoII(C.xy);
    	
    	countArand = randomNoII(vec2(countA, countA));
    	countBrand = randomNoII(vec2(countB, countB));
    	countCrand = randomNoII(vec2(countC, countC));
    	
    	Aoffset = Arand *  maxOffset * AxOff;
    	Boffset = Brand *  maxOffset * BxOff;
    	Coffset = Crand *  maxOffset * CxOff;
    	
    	A.x += Aoffset;
        A.y += Aoffset;
        
        B.x += Boffset;
        B.y += Boffset;
        
        C.x += Coffset;
        C.y += Coffset;
    	
    	a = A.xy;
    	b = B.xy;
    	c = C.xy;
    	
    	
    	
        A.x += Aoffset * sin(speedTime * countArand);
        A.y += Aoffset * cos(speedTime * countArand);
        A.z = Aoffset;
        
        B.x += Boffset * sin(speedTime * countBrand);
        B.y += Boffset * cos(speedTime * countBrand);
        B.z = Boffset;
        
        C.x += Coffset * sin(speedTime * countCrand);
        C.y += Coffset * cos(speedTime * countCrand);
        C.z = Coffset;
		
        overload = baryCoordsNoII(A, B, C, a, b, c, tex_coords, s);
		if(overload.a == 0.0 ){
			continue;
		}else{
			color = overload;
			break;
    	}
    //If the first loop fails, we check a row above
    
	}if(color.a == 0.0){
		index = oldIndex + CountTrisRow;
		amount = index + 4 +  offOne;
		
		for(index; index < amount; index++){
    	
    		faktor = int(index * CTR);
	    	countA = int(index * 0.5);
	    	countB = ((((index - 1)%2)*((countTris + 1)+countA)) + ((index % 2)*(countA +1)));
	    	countC = ((countTris + 2) + countA);
	    	
	    	Ffaktor = float(faktor);
	    	
	    	countA += faktor;
	    	countB += faktor;
	    	countC += faktor;
	    	
	    	rowA = Ffaktor;
	    	rowB = Ffaktor + float(((index + 1) % 2)*1);
	    	rowC = Ffaktor + 1;
			
	    	A.x = ((countA - int(rowA * rowFak))*Div)-((int(rowA) % 2)*offset);
	    	A.y = 1.0 - (rowA * DivY);
	    	
	    	B.x = ((countB - int(rowB * rowFak))*Div)-((int(rowB) % 2)*offset);
	    	B.y = 1.0 - (rowB * DivY);
	    	
	    	C.x = ((countC - int(rowC * rowFak))*Div)-((int(rowC) % 2)*offset);
	    	C.y = 1.0 - (rowC * DivY);
	    	
	    	AxOff = step(0.0001, A.x) * step(A.x, 0.999);
	    	AyOff = step(0.0001, A.y) * step(A.y, 0.999);
	    	
	    	BxOff = step(0.0001, B.x) * step(B.x, 0.999);
	    	ByOff = step(0.0001, B.y) * step(B.y, 0.999);
	    	
	    	CxOff = step(0.0001, C.x) * step(C.x, 0.999);
	    	CyOff = step(0.0001, C.y) * step(C.y, 0.999);
	    	
	    	Arand = randomNoII(A.xy);
	    	Brand = randomNoII(B.xy);
	    	Crand = randomNoII(C.xy);
	    	
	    	countArand = randomNoII(vec2(countA, countA));
    		countBrand = randomNoII(vec2(countB, countB));
    		countCrand = randomNoII(vec2(countC, countC));
	    	
	    	Aoffset = Arand *  maxOffset * AxOff;
	    	Boffset = Brand *  maxOffset * BxOff;
	    	Coffset = Crand *  maxOffset * CxOff;
	    	
	    	A.x += Aoffset;
	        A.y += Aoffset ;
	        
	        B.x += Boffset;
	        B.y += Boffset ;
	        
	        C.x += Coffset;
	        C.y += Coffset ;
	    	
	    	a = A.xy;
	    	b = B.xy;
	    	c = C.xy;
	    	
	        A.x += Aoffset * sin(speedTime * countArand);
	        A.y += Aoffset * cos(speedTime * countArand);
	        A.z = Aoffset;
	        
	        B.x += Boffset * sin(speedTime * countBrand);
	        B.y += Boffset * cos(speedTime * countBrand);
	        B.z = Boffset;
	        
	        C.x += Coffset * sin(speedTime * countCrand);
	        C.y += Coffset * cos(speedTime * countCrand);
	        C.z = Coffset;
			
	        overload = baryCoordsNoII(A, B, C, a, b, c, tex_coords, s);
			if(overload.a == 0.0 ){
				continue;
			}else{
				color = overload;
				break;
	    	}
		}
	//If that loop fails too, the last one should "find" the right Triangle
	}if(color.a == 0.0){
		index = oldIndex - CountTrisRow;
		amount = index + 4 + offOne;
		
		for(index; index < amount; index++){
    	
    		faktor = int(index * CTR);
	    	countA = int(index * 0.5);
	    	countB = ((((index - 1)%2)*((countTris + 1)+countA)) + ((index % 2)*(countA +1)));
	    	countC = ((countTris + 2) + countA);
	    	
	    	Ffaktor = float(faktor);
	    	
	    	countA += faktor;
	    	countB += faktor;
	    	countC += faktor;
	    	
	    	rowA = Ffaktor;
	    	rowB = Ffaktor + float(((index + 1) % 2)*1);
	    	rowC = Ffaktor + 1;
			
	    	A.x = ((countA - int(rowA * rowFak))*Div)-((int(rowA) % 2)*offset);
	    	A.y = 1.0 - (rowA * DivY);
	    	
	    	B.x = ((countB - int(rowB * rowFak))*Div)-((int(rowB) % 2)*offset);
	    	B.y = 1.0 - (rowB * DivY);
	    	
	    	C.x = ((countC - int(rowC * rowFak))*Div)-((int(rowC) % 2)*offset);
	    	C.y = 1.0 - (rowC * DivY);
	    	
	    	AxOff = step(0.0001, A.x) * step(A.x, 0.999);
	    	AyOff = step(0.0001, A.y) * step(A.y, 0.999);
	    	
	    	BxOff = step(0.0001, B.x) * step(B.x, 0.999);
	    	ByOff = step(0.0001, B.y) * step(B.y, 0.999);
	    	
	    	CxOff = step(0.0001, C.x) * step(C.x, 0.999);
	    	CyOff = step(0.0001, C.y) * step(C.y, 0.999);
	    	
	    	Arand = randomNoII(A.xy);
	    	Brand = randomNoII(B.xy);
	    	Crand = randomNoII(C.xy);
	    	
	    	countArand = randomNoII(vec2(countA, countA));
    		countBrand = randomNoII(vec2(countB, countB));
    		countCrand = randomNoII(vec2(countC, countC));
	    	
	    	Aoffset = Arand *  maxOffset * AxOff;
	    	Boffset = Brand *  maxOffset * BxOff;
	    	Coffset = Crand *  maxOffset * CxOff;
	    	
	    	A.x += Aoffset;
	        A.y += Aoffset;
	        
	        B.x += Boffset;
	        B.y += Boffset;
	        
	        C.x += Coffset;
	        C.y += Coffset;
	    	
	    	a = A.xy;
	    	b = B.xy;
	    	c = C.xy;
	    	
	        A.x += Aoffset * sin(speedTime * countArand);
	        A.y += Aoffset * cos(speedTime * countArand);
	        A.z = Aoffset;
	        
	        B.x += Boffset * sin(speedTime * countBrand);
	        B.y += Boffset * cos(speedTime * countBrand);
	        B.z = Boffset;
	        
	        C.x += Coffset * sin(speedTime * countCrand);
	        C.y += Coffset * cos(speedTime * countCrand);
	        C.z = Coffset;
	        
	        overload = baryCoordsNoII(A, B, C, a, b, c, tex_coords, s);
			if(overload.a == 0.0 ){
				continue;
			}else{
				color = overload;
				break;
	    	}
		}
	}
	//Now to the extensions. I build the shader modular, so you can add effects based on the Triangles.
	//The values of the loop that returned a matching triangle are saved, so you can use them in the future.
	
	//Wipe Extension: Does an Alpha Wipe over the whole Screen (from left or right), each Triangle gets its own alpha value.
	/*
	if(s.wipeField < 0.0){
		s.wipePos = 1.0 - s.wipePos;
	}
	s.wipePos *= 1.0 + (abs(s.wipeField)*0.5);
	s.wipePos -= abs(s.wipeField) * 0.5 * step(0.0, s.wipeField);
	
	A.x -= Aoffset * sin(speedTime * countArand);
	A.y -= Aoffset * cos(speedTime * countArand);
	        
	B.x -= Boffset * sin(speedTime * countBrand);
	B.y -= Boffset * cos(speedTime * countBrand);
	        
	C.x -= Coffset * sin(speedTime * countCrand);
	C.y -= Coffset * cos(speedTime * countCrand);

	float diss = s.wipePos ;
	float entfernungA = smoothstep(0.0 + diss, s.wipeField + diss, A.x);
	float entfernungB = smoothstep(0.0 + diss, s.wipeField + diss, B.x);
	float entfernungC = smoothstep(0.0 + diss, s.wipeField + diss, C.x);
	color.a *= entfernungA + entfernungB + entfernungC ;
	
	A.x += Aoffset * sin(speedTime * countArand);
	A.y += Aoffset * cos(speedTime * countArand);
	        
	B.x += Boffset * sin(speedTime * countBrand);
	B.y += Boffset * cos(speedTime * countBrand);
	        
	C.x += Coffset * sin(speedTime * countCrand);
	C.y += Coffset * cos(speedTime * countCrand);
	
	//color.rgb += vec3(clamp(drawLine(A.xy, B.xy, tex_coords) + drawLine(A.xy, C.xy, tex_coords) + drawLine(B.xy, C.xy, tex_coords),0.0, 1.0)*s.lineStrength);
	*/
	//Wireframe Extension: The Wireframe Extension was once build for debugging the shader, 
	//so if you need to debug the positions of the triangles you can use that.
	/*
	s.toggleWireframe = 1.0;
	if(s.toggleWireframe == 1.0){
		
		color.rgb *= (clamp(drawLine(A.xy, B.xy, tex_coords) + drawLine(A.xy, C.xy, tex_coords) + drawLine(B.xy, C.xy, tex_coords),0.0, 1.0)*s.lineStrength);
	}
	*/
	//New Light Extension: A extension that produces a soft lighting effect, either static on the grid, or dynamically following the Triangles.
	//In addition to the basic lambert equation it produces a fantastic look.
	/*
	if(s.softShadow != 0.0){
		
		if(s.softShadow == 2.0){
		A.x -= Aoffset * sin(speedTime * countArand);
		A.y -= Aoffset * cos(speedTime * countArand);
		        
		B.x -= Boffset * sin(speedTime * countBrand);
		B.y -= Boffset * cos(speedTime * countBrand);
		        
		C.x -= Coffset * sin(speedTime * countCrand);
		C.y -= Coffset * cos(speedTime * countCrand);
	}
		float gradientOffset = 2. / countTris;
		float baseIntens = -gradientOffset;
		float Light = smoothstep(gradientOffset, baseIntens, distance(A.xy, st)) + smoothstep(gradientOffset, baseIntens, distance(B.xy, st)) +smoothstep(gradientOffset, baseIntens, distance(C.xy, st));
		
		color.rgb *= Light;
	}
	*/
	//Special Dissolve: This effect consists of two modi; One with very small values for the noise seed, generates a fluid like motion.
	//The other one with really high values generates an cool random dissolve effect.
	
	
	
	float noiseSeed = 100.;
	vec2 NoisePos = (A.xy + B.xy + C.xy);
	
	
	float Noise = noise_NoII(NoisePos*noiseSeed);
	
	
	vec3 oldCol = color.rgb;
	float radiusX = 6.0/(abs(s.noiseScale)+1.0);
	float radiusY = 6.0/(abs(s.noiseScale)+1.0);
	float noiseRadius = radiusY;
	float basebias = 0.0;
	
	aspectRatio = (1920.0/1080)*(radiusY / radiusX);
	vec2 center = vec2(0.5);
	center *= vec2(aspectRatio, 1.0);
	
	//gradient1 is used for the effect itself, it creates a soft boundariy.
	//gradient2 is protecting the content (for example a Logo) from the effect, 
	//so you can setup how far the effect should go and what should be protected.
	
	float distanceA = distance(center, A.xy * vec2(aspectRatio, 1.0));
	float distanceB = distance(center, B.xy * vec2(aspectRatio, 1.0));
	float distanceC = distance(center, C.xy * vec2(aspectRatio, 1.0));
	
	float gradient1 = smoothstep(noiseRadius, basebias, distanceA) + smoothstep(noiseRadius, basebias, distanceB) +smoothstep(noiseRadius, basebias, distanceC);
	float gradient2 = smoothstep(radiusY, 0.0, distanceA) + smoothstep(radiusY, 0.0, distanceB) +smoothstep(radiusY, 0.0, distanceC);
	
	Noise *= (s.noiseScale + 0.5);
	
	Noise *= gradient1;
	color.rgb *= clamp((Noise + gradient2), 0.0, 1.0);
	oldCol = vec3(1.0, 1.0, 1.);
	//color.rgb += (clamp((drawLine(A.xy, B.xy, tex_coords)*0.0) + (drawLine(A.xy, C.xy, tex_coords)*0.0) + (drawLine(B.xy, C.xy, tex_coords)*1.0),0.0, 1.0)*1.0)*s.lineStrength;
	//Main Out:
    return color ;
}