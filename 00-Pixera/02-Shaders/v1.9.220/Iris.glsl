// Author: Andreas Leeb
// Version: 1.0p

//@implements: sampler2D
struct Iris {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "xRadius", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 400
  float xRadius;
  //@ label: "yRadius", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 400
  float yRadius;
  //@ label: "Smoothness", editor: range, min: 0, max: 1, range_min: 0, range_max: 5000, range_default: 50
  float smoothness;
  //@ label: "xPosition", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 500
  float x;
  //@ label: "yPosition", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 500
  float y;
  //@ label: "Angle[deg]", editor: range, min: 0, max: 360, range_min: 0, range_max: 360, range_default: 0
  float angle;
  //@ label: "Color Red", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0, group: rgbaColorPicker, group_label: "Color"
  float colorR;
  //@ label: "Color Green", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0, group: rgbaColorPicker
  float colorG;
  //@ label: "Color Blue", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0, group: rgbaColorPicker
  float colorB;
  //@ label: "Color Alpha", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255, group: rgbaColorPicker
  float colorA;
  //@ label: "Invert", editor: bool, bool_default: false
  bool invert;
  //@ label: "Width[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1920
  float width;
  //@ label: "Height[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1080
  float height;
};

vec4 texture(Iris s, vec2 tex_coords) {
  vec4 color = texture(s.sampler, tex_coords);
  vec4 orig = color;
  vec4 irisColor = vec4(s.colorR, s.colorG, s.colorB, s.colorA);
  irisColor.a *= s.colorA;
  
  float rad = radians(s.angle);
  mat2 rot = mat2(cos(rad), -sin(rad), sin(rad), cos(rad));
  tex_coords = rot * (tex_coords - vec2(s.x, s.y)) + vec2(s.x, s.y);
  
  float imageAspectRatio = s.width / s.height;
  float irisAspectRatio = s.yRadius * imageAspectRatio / s.xRadius;
  vec2 new_coords = tex_coords * vec2(irisAspectRatio, 1.);
  vec2 center = vec2(s.x * irisAspectRatio, s.y);
  color = mix(color, irisColor, abs(int(s.invert) - smoothstep(s.yRadius, s.yRadius + s.smoothness,
                                                        distance(center, new_coords))));
  vec4 result = mix(orig,color,s.mix);
  result.a = orig.a;
  return result;
}
