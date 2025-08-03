// Author: Andreas Leeb
// Version: 1.0

//@implements: sampler2D
struct Tiling {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Factor", editor: range, min: 1, max: 50, range_min: 1, range_max: 50, range_default: 1
  float factor;
};

vec4 texture(Tiling s, vec2 tex_coords) {
	vec2 coords = tex_coords;
	tex_coords = fract(tex_coords * s.factor);
	return mix(texture(s.sampler, coords), texture(s.sampler, tex_coords), s.mix);
}
