// Author: Adrian Bleul

//@implements: sampler2D
struct Kaleidoscope{
	sampler2D sampler;
	//@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
	float mix;
	//@ label: "time", editor: range, min: 0, max: 100, range_min: 0, range_max: 1, range_default: 0
	float time;
	//@ label: "Rotation speed", editor: range, min: 0, max: 0.2, range_min: 0, range_max: 100, range_default: 50
	float rotSpeed; 
	//@ label: "Amount", editor: range, min: 4, max: 100, range_min: 4, range_max: 100, range_default: 12
	float amount;
};
//angle is calculated in Radians so PI has to be defined first
float PI = 3.14159265359;

//This function checks if the Pixel on wich the algorithm runs is in Triangle
float inTri_K(vec2 a, vec2 b, vec2 c, vec2 p){
	float test = step(((a.y-b.y)*(p.x-a.x) + (b.x-a.x)*(p.y-a.y)), 0.);
    float test2 = step(((b.y-c.y)*(p.x-b.x) + (c.x-b.x)*(p.y-b.y)), 0.);
    float test3 = step(((c.y-a.y)*(p.x-c.x) + (a.x-c.x)*(p.y-c.y)), 0.);
   	
   	return test * test2 * test3;
}
//rotation matrix 
mat2 rotate2d_K(float _angle){
	
    return mat2(cos(_angle),-sin(_angle),
                sin(_angle),cos(_angle));
}

//mathematical function to calculate the dimensions of the Triangles and return them as a bw mask
float drawTri(float angle, int amount, vec2 tex_coords, float aspect, Kaleidoscope s){
	vec2 st = tex_coords;
	
	float triAngle = 360. / (amount*2);
	
	float leng = distance(vec2(0.0, 0.0), vec2(1.0 * aspect , 1.0));
	
	float sideOffset = tan(radians(triAngle)) * leng;
	
	sideOffset += 0.00001;
	
	vec2 p1 = vec2(0.5, 0.5);
	vec2 p2 = vec2(0.5 + sideOffset, 0.5 -leng);
	vec2 p3 = vec2(0.5 - sideOffset, 0.5 -leng);
	
	st.x *= aspect;
	
	st -= vec2(p1.x*aspect, p1.y);
	st = vec2(rotate2d_K(PI * angle)*st);
	st += vec2(p1.x, p1.y);
	
	return inTri_K(p1, p2, p3, st);

}

//rotate the texture and return the resulting color
vec3 rotateTexture(float angle, vec2 tex_coords, Kaleidoscope s, float aspect){
	vec2 st = tex_coords;
	
	
	vec2 center = vec2(0.5, 0.5);
	
	float texXoffset = 0.0;
    float texYoffset = 0.0;
	
	st.y += texYoffset;
	st.x += texXoffset;
	
	st.x *= aspect;
	
	center.x = (center.x+texXoffset)*aspect;
	center.y = center.y+texYoffset; 
	
	st -= center;
	st = vec2(rotate2d_K(angle*PI)*st);
	//st *= ((sin(s.time*1000.)*0.1)+0.9);
	st += center;
	
	st.x /= aspect;
	
	st = fract(st);
	
	return texture(s.sampler, st).rgb;
}	
	
//main
vec4 texture(Kaleidoscope s, vec2 tex_coords){
	vec4 orig = texture(s.sampler, tex_coords);
	vec2 st = tex_coords;
	
	float aspect = 1920.0/1080.0;
	
	int amount = int(s.amount);
	
	float angle = 2. / amount;
	vec4 col;
	
	float tri;
	
	float anim = s.time;
	anim *= amount-1;
	
	float animrot = 1.0;
	//loop for creating the kaleidoscope Effekt
	for(int i = 0; i < amount; i++){
		//Calculate Angle for fade-in
		float Anim = clamp(anim/float(i), 0.0, 1.0);
		//Anim = s.togglefadein == 0.0 ? 1.0 : Anim;
		Anim = 1.0;
		tri = drawTri(angle*i*Anim, amount, tex_coords, aspect, s);
		
		if(tri == 0.0){
			col = vec4(0.0);
			continue;
		}
		if(animrot == 1.0){
			//animate the video by constanly rotating it around the center of the effect
			float animAngle = s.time*s.rotSpeed*(((i%2)*-1.0)+(((i+1)%2)*1.0));
			col = vec4(vec3(rotateTexture(angle*i*Anim+animAngle, tex_coords, s, aspect)*tri), 1.0);
		}else{
		col = vec4(vec3(rotateTexture(angle*i*Anim, tex_coords, s, aspect)*tri), 1.0);
		}
		
		if(1.0 != Anim){
			col.rgb *= clamp(mod(anim, float(i - 1)),0.0, 1.0);
		}
		if (col != vec4(vec3(0.0),1.0)){
			break;
		}
		
	}
	
	return mix(texture(s.sampler, tex_coords), vec4(col.rgb, orig.a), s.mix) ;
}