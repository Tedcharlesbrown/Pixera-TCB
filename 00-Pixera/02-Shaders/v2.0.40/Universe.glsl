// Author: ?
// Version: 1.0p

//@implements: sampler2D
struct Universe {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Time", editor: range, min: 0, max: 1000, range_min: 0, range_max: 1000, range_default: 0
  float time;
  //@ label: "Width", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1920
  float width;
  //@ label: "Height", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1080
  float height;
};

const int iters = 200;

int fractal(vec2 p, float time) {
  
	float tt = time*0.003;
	float tt2 = time*0.07;
	float cr = cos(tt+10.0*sin(tt2*0.09));
	float ci = 0.75+sin(tt+cos(tt2*0.035))*0.15;
	
	for (int i = 0; i < iters; i++) {
		
		if (length(p) > 1.5) {
			return i;
		}
		p = vec2(p.x * p.x - p.y * p.y + cr, 2.0 * p.x * p.y + ci);
		
	}
	
	return 0;	
}

vec3 color(int i) {
	float f = float(i)/float(iters) * 2.0;
	return vec3((sin(f*10.0)), (sin(f*24.0)), abs(sin(f*42.0)));
}

vec4 texture(Universe s, vec2 tex_coords) {
  vec4 orig = texture(s.sampler, tex_coords);
  vec2 resolution = vec2(s.width, s.height);
  
  vec2 position = 3.*(-0.5 + gl_FragCoord.xy / resolution.xy );// + mouse / 1.0;
	position.x *= resolution.x/resolution.y;
	vec4 color = vec4(color(fractal(position, s.time)), orig.a);
	color = mix(orig, color, s.mix);
	
	return color;
}
