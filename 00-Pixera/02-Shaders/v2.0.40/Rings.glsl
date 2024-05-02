// Author: ?
// Version: 1.0p
//@implements: sampler2D
struct Rings {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Time", editor: range, min: 0, max: 1000, range_min: 0, range_max: 1000, range_default: 0
  float time;
  //@ label: "Amount", editor: discrete, discrete_min: 1, discrete_max: 15, discrete_default: 5
  int amount;
  //@ label: "Width", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1920
  float width;
  //@ label: "Height", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1080
  float height;
};


vec4 texture(Rings s, vec2 tex_coords) {
  vec4 orig = texture(s.sampler, tex_coords);
  vec2 resolution = vec2(s.width, s.height);
  
  float rings = s.amount;
  
 vec2 p = (gl_FragCoord.xy * 2.0 - resolution) / min(resolution.x, resolution.y);
	vec3 destColor=vec3(0.0,0.0,0.0);
	for( float i = 0.0 ;i<rings;i++){
		 float j = float(i)+1.0;
		vec2 q=vec2(cos(s.time*j),sin(s.time*j))*0.5;
		destColor+=0.01/abs(length(p-q)-0.2);
	}
	
	return mix(orig, vec4(destColor, orig.a), s.mix);
}
