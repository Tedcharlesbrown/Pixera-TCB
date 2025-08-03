// Author: Andreas Leeb
// Version: 1.0p

//@implements: sampler2D
struct TriGradient {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Position1[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 33
  float position1;
  //@ label: "Position2[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 67
  float position2;
  //@ label: "Width[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 16
  float width;
  //@ label: "Strength[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 20
  float strength;
  //@ label: "Angle[deg]", editor: range, min: 0, max: 90, range_min: 0, range_max: 90, range_default: 0
  float angle;
  //@ label: "Color 1 Red", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255, group: rgbColorPicker, group_label: "Left", partInfo: 1-3
  float red1;
  //@ label: "Color 1 Green", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0, group: rgbColorPicker
  float green1;
  //@ label: "Color 1 Blue", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0, group: rgbColorPicker
  float blue1;
  //@ label: "Color 2 Red", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0, group: rgbColorPicker, group_label: "Middle", partInfo: 2-3
  float red2;
  //@ label: "Color 2 Green", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255, group: rgbColorPicker
  float green2;
  //@ label: "Color 2 Blue", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0, group: rgbColorPicker
  float blue2;
  //@ label: "Color 3 Red", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0, group: rgbColorPicker, group_label: "Right", partInfo: 3-3
  float red3;
  //@ label: "Color 3 Green", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0, group: rgbColorPicker
  float green3;
  //@ label: "Color 3 Blue", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255, group: rgbColorPicker
  float blue3;

};

mat2 tg_rotate(float angle) {
  float sine = sin(angle);
  float cosine = cos(angle);
  return mat2(cosine, -sine, sine, cosine);
}

vec4 texture(TriGradient s, vec2 tex_coords) {
  vec4 color = texture(s.sampler, tex_coords);
  vec4 orig = color;
  vec4 color1 = vec4(s.red1, s.green1, s.blue1, 1.);
  vec4 color2 = vec4(s.red2, s.green2, s.blue2, 1.);
  vec4 color3 = vec4(s.red3, s.green3, s.blue3, 1.);
  
  float rad = radians(s.angle);
  tex_coords = tg_rotate(rad) * tex_coords;
  float w = s.width / 2.;
  
  vec4 gradColor;
  if(tex_coords.x < s.position1 - w) gradColor = color1;
  else if(tex_coords.x < s.position1 + w) gradColor = mix(color1, color2, smoothstep(-w, w, tex_coords.x - s.position1));
  else if(tex_coords.x >= s.position1 + w && tex_coords.x < s.position2 - w) gradColor = color2;
  else if(tex_coords.x < s.position2 + w) gradColor = mix(color2, color3, smoothstep(-w, w, tex_coords.x - s.position2));
  else gradColor = color3;
  
  vec4 result = mix(orig,mix(color, gradColor, s.strength),s.mix);  
  result.a = orig.a;
  return result;
}
