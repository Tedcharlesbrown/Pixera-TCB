// Author: Andreas Leeb
// Version: 1.0

//@implements: sampler2D
struct Sepia {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
};

vec4 texture(Sepia s, vec2 tex_coords) {
  vec4 color = texture(s.sampler, tex_coords);
  vec4 sepia = color;
  sepia.rgb = vec3((color.r + color.g + color.b) / 3.);
  sepia.rgb *= vec3(1.08, .9, .72);
  return mix(color, sepia, s.mix);
}
