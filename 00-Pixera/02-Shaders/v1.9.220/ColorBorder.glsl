// Author: Andreas Leeb
// Version: 1.0p

//@implements: sampler2D
struct ColorBorder {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Thickness", editor: range, min: 0.001, max: 0.5, range_min: 0, range_max: 500, range_default: 10
  float thickness;
  //@ label: "Color Red", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255, group: rgbaColorPicker, group_label:"Color"
  float colorR;
  //@ label: "Color Green", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255, group: rgbaColorPicker
  float colorG;
  //@ label: "Color Blue", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255, group: rgbaColorPicker
  float colorB;
  //@ label: "Color Alpha", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255, group: rgbaColorPicker
  float colorA;
};

vec4 texture(ColorBorder s, vec2 tex_coords) {
  vec4 orig =  texture(s.sampler, tex_coords);
  if(tex_coords.x <= s.thickness || tex_coords.x >= 1. - s.thickness ||
     tex_coords.y <= s.thickness || tex_coords.y >= 1. - s.thickness) { // border
    vec4 color = vec4(s.colorR, s.colorG, s.colorB, s.colorA);
    color.a = color.a < orig.a ? color.a : orig.a;
    return mix(orig,color,s.mix);
  } else {
  	tex_coords = (tex_coords - s.thickness) / (1. - 2. * s.thickness); // scaling
    vec4 color = texture(s.sampler, tex_coords);
    return mix(orig,color,s.mix);
  }
}
