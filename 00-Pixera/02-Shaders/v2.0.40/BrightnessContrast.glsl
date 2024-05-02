// Author: ?
// Version: 1.0

//@implements: sampler2D
struct BrightnessContrast {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Brightness[%]", editor: range, min: 0, max: 300, range_min: 0, range_max: 300, range_default: 100
  float brightness;
  //@ label: "Contrast[%]", editor: range, min: 0, max: 300, range_min: 0, range_max: 300, range_default: 100
  float contrast;
  //@ label: "Offset[%]", editor: range, min: -100, max: 100, range_min: -100, range_max: 100, range_default: 0
  float offset;
};

vec4 texture(BrightnessContrast s, vec2 tex_coords) {
  vec4 color = texture(s.sampler, tex_coords);
  return mix(color, vec4((color.rgb * (s.brightness/100.) - .5)
    * (s.contrast/100.) + .5 + (s.offset/100.), color.a), s.mix);
}
