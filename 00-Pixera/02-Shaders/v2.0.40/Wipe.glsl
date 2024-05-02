// Author: Benni M.
// Version: 1.0

//@implements: sampler2D
struct Wipe {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "X", editor: range, min: -1, max: 1, range_min: -1, range_max: 1, range_default: 0
  float x;
  //@ label: "Y", editor: range, min: -1, max: 1, range_min: -1, range_max: 1, range_default: 0
  float y;
};

vec4 texture(Wipe s, vec2 tex_coords) {

	vec2 coords = vec2(tex_coords.x + s.x, tex_coords.y + s.y);
	vec4 colorOrig = texture(s.sampler, tex_coords);
	vec4 color = texture(s.sampler, coords);
  	if(coords.x < 0. || coords.y < 0. || coords.x > 1. || coords.y > 1.0)
    	color = vec4(0.);
    return mix(colorOrig, color, s.mix);
}
