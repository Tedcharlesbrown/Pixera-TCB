// Author: Andreas Leeb
// Version: 1.0

//@implements: sampler2D
struct ColorChannels {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
	float mix;
  //@ label: "Red", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 127, group: rgbColorPicker, group_label: "Color"
  float red;
  //@ label: "Green", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 127, group: rgbColorPicker
  float green;
  //@ label: "Blue", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 127, group: rgbColorPicker
  float blue;

   //@ label: "RedMix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float redMix;
   //@ label: "GreenMix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float greenMix;
    //@ label: "BlueMix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float blueMix;
};

vec4 texture(ColorChannels s, vec2 tex_coords) {
  vec4 orig = texture(s.sampler, tex_coords);
  vec4 color = texture(s.sampler, tex_coords);
  vec3 params = vec3(s.red, s.green, s.blue);
  vec3 mixParams = vec3(s.redMix, s.greenMix, s.blueMix);
  color.rgb = mix(color.rgb, params, mixParams);
  return mix(orig, color, s.mix);
}
