// Author: Andreas Leeb
// Version: 1.1

//@implements: sampler2D
struct Sharpening {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
  float mix;
  //@ label: "Width[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1920
  float width;
  //@ label: "Height[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1080
  float height;
  //@ label: "Strength", editor: range, min: 0, max: 10, range_min: 0, range_max: 10, range_default: 3
  float strength;
};

vec4 texel(vec2 abs_coords, Sharpening s) {
  vec2 dim = vec2(s.width, s.height);
  return texture(s.sampler, abs_coords / dim);
}

vec4 texture(Sharpening s, vec2 tex_coords) {
	vec2 dim = vec2(s.width, s.height);
	vec2 abs_coords = tex_coords * dim;
	float x = s.strength;
	float a = -x * .2;
	float b = -x * .05;
	mat3 filterr = mat3(b, a, b, a, x + 1., a, b, a, b);
	vec4 col = vec4(0.);
	for(int i = 0; i < 3; i++) {
		for(int j = 0; j < 3; j++) {
		  vec2 offset = vec2(i - 1, j - 1);
		  col += filterr[i][j] * texel(abs_coords + offset, s);
		}
	}
	return mix(texture(s.sampler, tex_coords), col, s.mix);
}