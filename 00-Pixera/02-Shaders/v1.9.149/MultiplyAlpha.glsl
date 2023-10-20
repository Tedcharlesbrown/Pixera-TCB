// Author: ?
// Version: 1.0

//@implements: sampler2D
struct MultiplyAlpha {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
  float mix;
  //@ label: "Alpha[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 100
  float alpha;
};

vec4 texture(MultiplyAlpha s, vec2 tex_coords) {
  vec4 color = texture(s.sampler, tex_coords);
  color.a = clamp(color.a * s.alpha, 0, 1);
  return mix(texture(s.sampler, tex_coords),color, s.mix);
}
