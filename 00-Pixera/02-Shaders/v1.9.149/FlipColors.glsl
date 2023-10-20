// Author: Andreas Leeb
// Version: 1.0p

//@implements: sampler2D
struct FlipColors {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
  float mix;
  //@ label: "FlipRedGreen", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
  float flipRedGreen;
  //@ label: "FlipRedBlue", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
  float flipRedBlue;
  //@ label: "FlipGreenBlue", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
  float flipGreenBlue;
};

vec4 texture(FlipColors s, vec2 tex_coords) {
  vec4 color = texture(s.sampler, tex_coords);
  if(s.flipRedGreen > 0.) color.rg = color.gr;
  if(s.flipRedBlue > 0.) color.rb = color.br;
  if(s.flipGreenBlue > 0.) color.gb = color.bg;
  color = mix(texture(s.sampler, tex_coords),color, s.mix);
  return color;
}
