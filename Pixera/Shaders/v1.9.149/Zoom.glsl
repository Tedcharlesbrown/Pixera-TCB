// Author: Andreas Leeb
// Version: 1.0

//@implements: sampler2D
struct Zoom {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
  float mix;
  //@ label: "xPosition", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 500
  float x;
  //@ label: "yPosition", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 500
  float y;
  //@ label: "Scale[%]", editor: range, min: .1, max: 10., range_min: 10, range_max: 1000, range_default: 200
  float scale;
};

vec4 texture(Zoom s, vec2 tex_coords) {
	vec2 coords = tex_coords;
  	vec2 center = vec2(s.x, s.y);
	float scaleRec = 1. / s.scale;
	mat2 scale = mat2(scaleRec, 0., 0., scaleRec);
	tex_coords = fract(scale * (tex_coords - center) + center);
	return mix(texture(s.sampler, coords), texture(s.sampler, tex_coords), s.mix);
}
