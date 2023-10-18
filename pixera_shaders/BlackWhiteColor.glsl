// Author: Andreas Leeb
// Version: 1.0

//@implements: sampler2D
struct BlackWhiteColor {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0.0, max: 1.0, range_min: 0, range_max: 1, range_default: 0
  float mix;
  //@ label: "Exclude from red", editor: range, min: 0.0, max: 1.0, range_min: 0, range_max: 65535, range_default: 0
  float redFrom;
  //@ label: "to red", editor: range, min: 0.0, max: 1.0, range_min: 0.0, range_max: 65535, range_default: 0
  float redTo;
  //@ label: "Exclude from green", editor: range, min: 0.0, max: 1.0, range_min: 0, range_max: 65535, range_default: 0
  float greenFrom;
  //@ label: "to green", editor: range, min: 0.0, max: 1.0, range_min: 0, range_max: 65535, range_default: 0
  float greenTo;
  //@ label: "Exclude from blue", editor: range, min: 0.0, max: 1.0, range_min: 0, range_max: 65535, range_default: 0
  float blueFrom;
  //@ label: "to blue", editor: range, min: 0.0, max: 1.0, range_min: 0, range_max: 65535, range_default: 0
  float blueTo;
};

vec4 texture(BlackWhiteColor s, vec2 tex_coords) {
  vec4 color = texture(s.sampler, tex_coords);
  if(color.r >= s.redFrom && color.r <= s.redTo &&
     color.g >= s.greenFrom && color.g <= s.greenTo &&
     color.b >= s.blueFrom && color.b <= s.blueTo) {
    return mix(color, texture(s.sampler, tex_coords), s.mix);
  }
  return mix(texture(s.sampler, tex_coords), vec4(vec3((color.r + color.g + color.b) / 3.), color.a), s.mix);
}
