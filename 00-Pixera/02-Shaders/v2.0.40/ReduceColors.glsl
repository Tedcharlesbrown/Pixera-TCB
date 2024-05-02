// Author: Andreas Leeb
// Version: 1.0

//@implements: sampler2D
struct ReduceColors {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "RedValues", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 16, group: rgbColorPicker, group_label: "Values"
  float redValues;
  //@ label: "GreenValues", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 16, group: rgbColorPicker
  float greenValues;
  //@ label: "BlueValues", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 16, group: rgbColorPicker
  float blueValues;
};

vec4 texture(ReduceColors s, vec2 tex_coords) {
  vec4 color = texture(s.sampler, tex_coords);
  vec3 values = vec3(s.redValues, s.greenValues, s.blueValues);
  values = clamp(values, 0, 1);
  color.rgb = round(color.rgb * values) / values;
  return mix(texture(s.sampler, tex_coords), color, s.mix);
}
