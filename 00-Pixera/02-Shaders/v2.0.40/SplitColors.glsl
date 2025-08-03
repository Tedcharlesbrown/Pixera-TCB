// Author: Andreas Leeb
// Version: 1.0

//@implements: sampler2D
struct SplitColors {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Strength", editor: range, min: 0, max: 0.05, range_min: 0, range_max: 1000, range_default: 100
  float strength;
  //@ label: "Angle[deg]", editor: range, min: 0, max: 360, range_min: 0, range_max: 360, range_default: 0
  float angle;
};

vec4 texture(SplitColors s, vec2 tex_coords) {
  vec4 color = texture(s.sampler, tex_coords);
  
  float angle = radians(s.angle);
  float sine = sin(angle);
  float cosine = cos(angle);
  mat2 rotMat = mat2(cosine, -sine, sine, cosine);
  
  vec2 left = rotMat * vec2(-s.strength, 0.);
  vec4 leftColor = texture(s.sampler, tex_coords + left);
  color.r = mix(color.r, leftColor.r, s.mix);
  
  vec2 right = rotMat * vec2(s.strength, 0.);
  vec4 rightColor = texture(s.sampler, tex_coords + right);
  color.b = mix(color.b, rightColor.b, s.mix);
  
  return color;
}