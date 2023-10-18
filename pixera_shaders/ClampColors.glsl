// Author: Andreas Leeb
// Version: 1.0

//@implements: sampler2D
struct ClampColors {
  sampler2D sampler;
  //@ label: "Mix", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
  float mix;
  //@ label: "RedMin", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
  float redMin;
  //@ label: "RedMax", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255
  float redMax;
  //@ label: "GreenMin", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
  float greenMin;
  //@ label: "GreenMax", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255
  float greenMax;
  //@ label: "BlueMin", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
  float blueMin;
  //@ label: "BlueMax", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255
  float blueMax;
};

vec4 texture(ClampColors s, vec2 tex_coords) {
  vec4 color = texture(s.sampler, tex_coords);
  vec4 orig = color;
  vec3 min = vec3(s.redMin, s.greenMin, s.blueMin);
  vec3 max = vec3(s.redMax, s.greenMax, s.blueMax);
  color.rgb = clamp(color.rgb, min, max);
  return mix(orig, color, s.mix);
}
