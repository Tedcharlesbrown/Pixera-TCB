// Author: ?
// Version: 1.0p

//@implements: sampler2D
struct MultiplyColor {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Red", editor: range, min: 0, max: 2, range_min: 0, range_max: 2, range_default: 1
  float red;
  //@ label: "Green", editor: range, min: 0, max: 2, range_min: 0, range_max: 2, range_default: 1
  float green;
  //@ label: "Blue", editor: range, min: 0, max: 2, range_min: 0, range_max: 2, range_default: 1
  float blue;
  //@ label: "Alpha", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 1
  float alpha;
};

vec4 texture(MultiplyColor s, vec2 tex_coords) {
  vec4 orig = texture(s.sampler, tex_coords);
  vec4 color = texture(s.sampler, tex_coords) * vec4(s.red, s.green, s.blue, s.alpha);
  color.a = clamp(color.a, 0, 1);
  return mix(orig,color,s.mix);
}
