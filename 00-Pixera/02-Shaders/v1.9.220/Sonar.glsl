// Author: ?
// Version: 1.0p
#define PI 3.14159265359
//@implements: sampler2D
struct Sonar {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Time", editor: range, min: 0, max: 1000, range_min: 0, range_max: 1000, range_default: 0
  float time;
  //@ label: "Width", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1920
  float width;
  //@ label: "Height", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1080
  float height;
  //@ label: "Red", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255, group: rgbColorPicker, group_label: "Color"
  float red;
  //@ label: "Green", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 221, group: rgbColorPicker
  float green;
  //@ label: "Blue", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0, group: rgbColorPicker
  float blue;
};

float d2y(float d){return 1./(0.2+d);}
float radius = 0.42;

float fct(vec2 p, float r, float time){
	float a = 3.*mod(-atan(p.y, -p.x)+time, 2.*PI);
	
	
	float scan = 0.*1.;
	return (d2y(a)+scan)*(1.0-smoothstep(0.3,radius,r));
}

	
float circle(vec2 p, float r){
	float d=distance(r, radius);
	return d2y(100.*d);
}

float grid(vec2 p, float y){
	float a = 7.;
	float res = 30.;
	float e = 0.9;
	vec2 pi = fract(p*res);
	pi = step(e, pi);
	return a * y * pi.x * pi.y;
}

vec4 texture(Sonar s, vec2 tex_coords) {
  vec4 orig = texture(s.sampler, tex_coords);
  vec2 resolution = vec2(s.width, s.height);
  vec3 color = vec3(s.red,s.green,s.blue);
  
  vec2 position = (( gl_FragCoord.xy )-0.5*resolution)/ resolution.y ;
	vec2 uv = position;
	position/=cos(.125*length(position));
	float y  = 0.;
	
	float dc = length(position);
	
	y+=fct(position, dc, s.time);
	y+=circle(position, dc);
	y+=grid(position, y);
	float d = smoothstep(0.01,0.003,length(vec2(uv.x-0.2,uv.y-0.1)));
	y += d * max(sin(s.time+3.72)*5.0,0.0);
	d = smoothstep(0.01,0.003,length(vec2(uv.x+0.1,uv.y-0.2)));
	y += d * max(sin(s.time+5.3)*5.0,0.0);
	y=pow(y,1.75);
	vec4 outCol = vec4(sqrt(y)*color, orig.a);
	return mix(orig, outCol, s.mix);
}
