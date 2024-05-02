// Author: Andreas Leeb
// Version: 1.0p

//@implements: sampler2D
struct FlipColors {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "FlipRedGreen", editor: bool, bool_default: false
  bool flipRedGreen;
  //@ label: "FlipRedBlue", editor: bool, bool_default: false
  bool flipRedBlue;
  //@ label: "FlipGreenBlue", editor: bool, bool_default: false
  bool flipGreenBlue;
};

vec4 texture(FlipColors s, vec2 tex_coords) {
  vec4 color = texture(s.sampler, tex_coords);
  if(s.flipRedGreen) color.rg = color.gr;
  if(s.flipRedBlue) color.rb = color.br;
  if(s.flipGreenBlue) color.gb = color.bg;
  color = mix(texture(s.sampler, tex_coords),color, s.mix);
  return color;
}
