// Author: Andreas Leeb
// Version: 1.0

//@implements: sampler2D
struct Mirror {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
  float mix;
  //@ label: "MirrorPosition[%]", editor: range, min: 0.5, max: 1, range_min: 50, range_max: 100, range_default: 50
  float position;
  //@ label: "Offset", editor: range, min: 0.0, max: 0.5, range_min: 0, range_max: 50, range_default: 0
  float offset;
};

vec4 texture(Mirror s, vec2 tex_coords) {
	vec2 coords = tex_coords;
	tex_coords.x += s.offset;
	s.position += s.offset;
  if(tex_coords.x >= s.position) {
  	tex_coords.x = float(s.position - mod(tex_coords, s.position));
  }
  return mix(texture(s.sampler, coords), texture(s.sampler, tex_coords), s.mix);
}
