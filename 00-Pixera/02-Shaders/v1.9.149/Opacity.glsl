// Author: Andreas Leeb
// Version: 1.0

//@implements: sampler2D
struct Opacity {
  sampler2D sampler;
  //@ label: "Alpha[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 100
  float alpha;
};

vec4 texture(Opacity s, vec2 tex_coords) {
  vec4 color = texture(s.sampler, tex_coords);
  color.a = s.alpha;
  color.rgb *= color.a;
  return color;
}
