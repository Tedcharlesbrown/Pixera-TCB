// Author: Andreas Leeb
// Version: 1.0p

//@implements: sampler2D
struct Negative {
  sampler2D sampler;
  //@ label: "Mix", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
  float mix;
};

vec4 texture(Negative s, vec2 tex_coords) {
  vec4 color = texture(s.sampler, tex_coords);
  vec4 color_neg = vec4(vec3(1. - color.rgb),1.);
  return mix(color,color_neg,s.mix);
}
