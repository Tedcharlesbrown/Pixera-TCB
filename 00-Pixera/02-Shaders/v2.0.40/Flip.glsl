// Author: Andreas Leeb
// Version: 1.0p

//@implements: sampler2D
struct Flip {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Horizontal", editor: bool, bool_default: false
  bool xAxis;
  //@ label: "Vertical", editor: bool, bool_default: false
  bool yAxis;
};

vec4 texture(Flip s, vec2 tex_coords) {
	vec2 coords = tex_coords.xy;
  if(s.xAxis) {
  	coords.x = 1. - coords.x;
  }
  if(s.yAxis) {
  	coords.y = 1. - coords.y;
  }
  vec4 color = mix(texture(s.sampler, tex_coords),texture(s.sampler, coords), s.mix);
  return color;
}
