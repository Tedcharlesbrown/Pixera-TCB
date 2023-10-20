// Author: Adrian Bleul

//@implements: sampler2D
struct RaymarchClouds{
	sampler2D sampler;
	//@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
  	float mix;
	//@ label: "time", editor: range, min: 0, max: 100, range_min: 0, range_max: 1, range_default: 0
	float time;
	//@ label: "Focus", editor: range, min: 1, max: 6, range_min: 0, range_max: 100, range_default: 100
	float slider4;
	//@ label: "Treshold", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 80
	float treshold;
	//@ label: "Foreground Red", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255
	float fColorR;
	//@ label: "Foreground Green", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
	float fColorG;
	//@ label: "Foreground Blue", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
	float fColorB;
	//@ label: "Background Red", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
	float bColorR;
	//@ label: "Background Green", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
	float bColorG;
	//@ label: "Background Blue", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255
	float bColorB;
	
};


#define SPIRAL_NOISE_ITER 10
//#define SHANE_ORGANIC

vec2 iResolution = vec2(0.16, 0.9);
vec2 iMouse = vec2(100.0, 100.0);

float hash( const in vec3 p ) {
    return fract(sin(dot(p,vec3(127.1,311.7,758.5453123)))*43758.5453123);
}

float pn(in vec3 x) {
    vec3 p = floor(x), f = fract(x);
	f *= f*(3.-f-f);
	vec2 uv = (p.xy+vec2(37,17)*p.z) + f.xy;
	vec2 rg = vec2(1.0);
	return 2.4*mix(rg.x, rg.y, f.z)-1.;
}

//-------------------------------------------------------------------------------------
// otaviogood's noise from https://www.shadertoy.com/view/ld2SzK
//--------------------------------------------------------------
// This spiral noise works by successively adding and rotating sin waves while increasing frequency.
// It should work the same on all computers since it's not based on a hash function like some other noises.
// It can be much faster than other noise functions if you're ok with some repetition.
const float nudge = 20.;	// size of perpendicular vector
float normalizer = 1.0 / sqrt(1.0 + nudge*nudge);	// pythagorean theorem on that perpendicular to maintain scale
float SpiralNoiseC(vec3 p, vec4 id) {
    float iter = 2., n = 2.-id.x; // noise amount
    for (int i = 0; i < SPIRAL_NOISE_ITER; i++) {
        // add sin and cos scaled inverse with the frequency
        n += -abs(sin(p.y*iter) + cos(p.x*iter)) / iter;	// abs for a ridged look
        // rotate by adding perpendicular and scaling down
        p.xy += vec2(p.y, -p.x) * nudge;
        p.xy *= normalizer;
        // rotate on other axis
        p.xz += vec2(p.z, -p.x) * nudge;
        p.xz *= normalizer;  
        // increase the frequency
        iter *= id.y + .733733;
    }
    return n;
}


float map(vec3 p, vec4 id) {
	float k = 2.*id.w +.1; //  p/=k;
    return k*(.5 + SpiralNoiseC(p.zxy*.4132+333., id)*3. + pn(p*8.5)*.12);
}

//-------------------------------------------------------------------------------------
// Based on [iq: https://www.shadertoy.com/view/MsS3Wc]
//-------------------------------------------------------------------------------------
vec3 hsv2rgb(float x, float y, float z) {	
	return z+z*y*(clamp(abs(mod(x*6.+vec3(0,4,2),6.)-3.)-1.,0.,1.)-1.);
}

//-------------------------------------------------------------------------------------
// Based on "Type 2 Supernova" by Duke (https://www.shadertoy.com/view/lsyXDK) 
//-------------------------------------------------------------------------------------
vec4 renderSuperstructure(vec3 ro, vec3 rd, const vec4 id, RaymarchClouds s, vec2 tex_coords) {
	
	
	
    const float max_dist=25.;
	float ld, td=0., w, d, t, noi, lDist, a,         
    	  rRef = 2.*id.x,
          h = .05+.25*id.z;
   
    vec3 pos, lightColor;   
    vec4 sum = vec4(0);
   	
    t = .3*hash(vec3(hash(rd))+s.time); 

    for (int i=0; i<200; i++)  {
		// Loop break conditions.
	    if(td>.9 ||  sum.a > .99 || t>max_dist) break;
        
        // Color attenuation according to distance
        a = smoothstep(max_dist,0.,t);
        
        // Evaluate distance function
        d = abs(map(pos = ro + t*rd, id))+.07;
        
        // Light calculations
        
        vec2 uv = tex_coords;
        float _angle = 0.5;
        uv *= mat2(cos(_angle),-sin(_angle),
                sin(_angle),cos(_angle));
         
        vec3 bCol = vec3(s.bColorR, s.bColorG, s.bColorB);
        vec3 fCol = vec3(s.fColorR, s.fColorG, s.fColorB);
         
         
        lDist = max(length(mod(pos+2.5,5.)-2.5), .001); // TODO add random offset
        noi = pn(0.03*pos);
        lightColor = mix(hsv2rgb(noi,.5,.6), 
                         hsv2rgb(noi+.3,.5,.6), -
                         smoothstep(rRef*.5,rRef*2.,lDist));
        lightColor = mix(vec3(0.0, 0.0, 1.0), vec3(1.0, 0.0, 0.0), smoothstep(0.0, 1.0, lDist * 0.3));
        lightColor = mix(bCol, fCol, lDist * s.treshold);
        //lightColor = texture(s.sampler, tex_coords).rgb;
        sum.rgb += a*lightColor/exp(lDist*lDist*lDist*.08)/10.;
		
        if (d<h) {
			td += (1.-td)*(h-d)+.005;  // accumulate density
            sum.rgb += sum.a * sum.rgb * .25 / lDist;  // emission	
			sum += (1.-sum.a)*.05*td*a;  // uniform scale density + alpha blend in contribution 
        } 
		
        td += .015;
        t += max(d * .08 * max(min(lDist,d),2.), .01);  // trying to optimize step size
    }
    
    // simple scattering
    sum *= 1. / exp(ld*.2)*.3;
   	sum = clamp(sum, 0., 1.);   
    sum.xyz *= sum.xyz*(3.-sum.xyz-sum.xyz);
	return sum;
}

#define R(p, a) p=cos(a)*p+sin(a)*vec2(p.y, -p.x)

vec4 texture(RaymarchClouds s, vec2 tex_coords)
{ 
	if(s.mix == 0.0)
	{
		return texture(s.sampler, tex_coords);
	}
    //vec4 sliderVal, cSlider = processSliders(fragCoord, sliderVal);
    vec2 m = iMouse.xy/iResolution.xy;
    vec3 ro = vec3(15.+s.time, cos(.1*s.time), 15.+s.time);
	vec3 rd = normalize(vec3((tex_coords.xy-0.5*iResolution.xy)/iResolution.y, 1.));
   
    R(rd.zx, 1.*m.x);
    R(rd.yx, 1.5*m.y);
    R(rd.xz, s.time*.1);
	
	vec4 sliderVal = vec4(1.0, 1.0, 1.0, s.slider4);
	
    // Super Structure
   
	vec4 col = renderSuperstructure(ro, rd, sliderVal, s, tex_coords);
	
	vec4 cSlider = vec4(1.0, 1.0, 1.0, s.slider4);	
	float bCorrection = clamp(s.slider4 - 1.0, 1.0, 9.0);
    //Apply slider overlay
    //return vec4(mix(col.xyz + 0.5*vec3(.1,.2,.3),cSlider.rgb,cSlider.a), 1.);
    return mix(texture(s.sampler, tex_coords), vec4(col.rgb*bCorrection, 1.0), s.mix);
}
