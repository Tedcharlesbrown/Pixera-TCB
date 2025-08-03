// Author: ?
// Version: 1.0p

//@implements: sampler2D
struct AddColor {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Red", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255, group: rgbaColorPicker, group_label: "Color"
  float reds;
  //@ label: "Green", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 221, group: rgbaColorPicker
  float green;
  //@ label: "Blue", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0, group: rgbaColorPicker
  float blue;
  //@ label: "Alpha", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255, group: rgbaColorPicker
  float alpha;
};

vec4 texture(AddColor s, vec2 tex_coords) {
  vec4 orig = texture(s.sampler, tex_coords);
  vec4 color = texture(s.sampler, tex_coords) + vec4((s.reds), (s.green), (s.blue), s.alpha);
  color = mix(orig, color, s.mix);
  color.a = clamp(orig.a, 0, 1);
  return color;
}
