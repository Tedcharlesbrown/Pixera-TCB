// Author: Andreas Leeb
// Version: 1.0p

//@implements: sampler2D
struct Gradient {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float strength;
  //@ label: "Left color Red", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255, group: rgbaColorPicker, group_label: "Left", partInfo: 1-2
  float leftRed;
  //@ label: "Left color Green", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0, group: rgbaColorPicker
  float leftGreen;
  //@ label: "Left color Blue", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0, group: rgbaColorPicker
  float leftBlue;
  //@ label: "Left color Alpha", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255, group: rgbaColorPicker
  float leftAlpha;
  //@ label: "Right color Red", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0, group: rgbaColorPicker, group_label: "Right", partInfo: 2-2
  float rightRed;
  //@ label: "Right color Green", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0, group: rgbaColorPicker
  float rightGreen;
  //@ label: "Right color Blue", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255, group: rgbaColorPicker
  float rightBlue;
  //@ label: "Right color Alpha", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255, group: rgbaColorPicker
  float rightAlpha;
  //@ label: "Position", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 50
  float position;
  //@ label: "Width", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 50
  float width;
  //@ label: "Angle[deg]", editor: range, min: 0, max: 360, range_min: 0, range_max: 360, range_default: 0
  float angle;
};

mat2 gr_rotate(float angle) {
  float sine = sin(angle);
  float cosine = cos(angle);
  return mat2(cosine, -sine, sine, cosine);
}

vec4 texture(Gradient s, vec2 tex_coords) {
  vec4 color = texture(s.sampler, tex_coords);
  vec4 leftColor = vec4(s.leftRed, s.leftGreen, s.leftBlue, s.leftAlpha);
  vec4 rightColor = vec4(s.rightRed, s.rightGreen, s.rightBlue, s.rightAlpha);
  
  tex_coords = tex_coords - .5;
  float rad = radians(s.angle);
  tex_coords = gr_rotate(rad) * tex_coords;
  s.position -= .5;
  
  float w = s.width / 2.;
  vec4 gradientColor = mix(leftColor, rightColor, smoothstep(s.position - w, s.position + w, tex_coords.x));
  color = mix(color, vec4(vec3(gradientColor.rgb),gradientColor.a * color.a), s.strength);
  return color;
}
