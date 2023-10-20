// Author: Adrian Bleul

//@implements: sampler2D
struct LavaLamp{
	sampler2D sampler;
	//@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
	float mix;
	//@ label: "time", editor: range, min: 0, max: 100, range_min: 0, range_max: 1, range_default: 0
	float time; 
	//@ label: "Foreground Red", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255
  	float fColorR;
  	//@ label: "Foreground Green", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
  	float fColorG;
  	//@ label: "Foreground Blue", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
  	float fColorB;
  	//@ label: "Midground Red", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 127
  	float mColorR;
  	//@ label: "Midground Green", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
  	float mColorG;
  	//@ label: "Midground Blue", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 127
  	float mColorB;
  	//@ label: "Background Red", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
  	float bColorR;
  	//@ label: "Background Green", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
  	float bColorG;
  	//@ label: "Background Blue", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255
  	float bColorB;
};

float iTime;

vec3 BG_COLOR;
vec3 MG_COLOR;
vec3 FG_COLOR;

float sd_box(vec3 p, float x, float y, float z);

float smin(float a, float b, float k);
float noise(vec3 p);

float map(vec3 p) {
    float d = 1000.0;
    
    d = smin(d, sd_box(p - vec3(0.0, 1.25, 0.75), 10.0, 0.5, 10.0), 0.25);
    d = smin(d, sd_box(p - vec3(0.0,-1.25, 0.75), 10.0, 0.5, 10.0), 0.25);
    
    float t = iTime * 0.5;
    d += noise(p + vec3(0.0, t, t));
    
    return d;  
}

float sd_box(vec3 p, float x, float y, float z) {
	vec3 d = abs(p) - vec3(x, y, z);
	return min(max(d.x, max(d.y, d.z)), 0.0) + length(max(d, 0.0));
}

float smin(float a, float b, float k) {
	float h = clamp(0.5 + 0.5 * (b - a) / k, 0.0, 1.0);
	return mix(b, a, h) - k * h * (1.0 - h);
}

float noise(vec3 p) {
	vec3 s = vec3(7.0, 157.0, 113.0);
	vec3 ip = floor(p);
	p -= ip;
	vec4 h = vec4(0.0, s.yz, s.y + s.z) + dot(ip, s);
	p = p * p * (3.0 - 2.0 * p);
	h = mix(fract(sin(h) * 43758.5453), fract(sin(h + s.x) * 43758.5453), p.x);
	h.xy = mix(h.xz, h.yw, p.y);
	return mix(h.x, h.y, p.z) * 2.0 - 1.0;
}

vec3 compute_normal(vec3 p) {
	vec3 eps = vec3(0.0005, 0.0, 0.0);
    vec3 n;
    n.x = map(p + eps.xyy) - map(p - eps.xyy);
    n.y = map(p + eps.yxy) - map(p - eps.yxy);
    n.z = map(p + eps.yyx) - map(p - eps.yyx);
    n = normalize(n);
    return n;
}

float compute_ao(vec3 p, vec3 n) {
	float occ = 0.0;
	float sca = 1.0;
	for(int i = 0; i < 5; i++) {
		float hr = 0.01 + 0.12 * float(i) / 4.0;
		float d = map(p + hr * n);
		occ += -(d - hr) * sca;
		sca *= 0.95;
	}
	return clamp(1.0 - 3.0 * occ, 0.0, 1.0);
}

vec4 texture(LavaLamp s, vec2 tex_coords) {
    vec4 orig = texture(s.sampler, tex_coords);    
    iTime = s.time;
    FG_COLOR = vec3(s.fColorR, s.fColorG, s.fColorB);
    MG_COLOR = vec3(s.mColorR, s.mColorG, s.mColorB);
    BG_COLOR = vec3(s.bColorR, s.bColorG, s.bColorB);
    vec3 ro = vec3(0.0, 0.0, -2.5);
    vec3 rd;
    rd.xy = tex_coords * 2.0 - vec2(1.7775, 1.0);
    rd.z = 1.0;
    rd = normalize(rd);
    
    vec3 color = BG_COLOR;
    if(s.mix != 0.0)
    {
    float t = 0.0;
    float t_max = 7.5;
    for(int i = 0; i < 256; i++) {
        float d = map(ro + t * rd);
        t += d * 0.6;
        if(d < 0.002) {
            vec3 p = ro + t * rd;
            vec3 n = compute_normal(p);
            vec3 l = normalize(vec3(0.25, 1.0, -0.5));
            float dot_nl = clamp(dot(n, l), 0.0, 1.0);
            float ao = compute_ao(p, n);
            float fog = clamp(1.0 - t / t_max, 0.0, 1.0);
            float light = mix(dot_nl, ao, 0.5);
            
            color = mix(MG_COLOR, FG_COLOR, light);
            color = mix(BG_COLOR, color, fog);
            break;
        }
        else if(t > t_max) {
            break;
        }
    }
    }
    
    return mix(orig,vec4(color, 1.0),s.mix);
}