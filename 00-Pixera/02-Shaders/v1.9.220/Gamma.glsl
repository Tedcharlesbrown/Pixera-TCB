// Author: Andreas Leeb
// Version: 1.1

//@implements: sampler2D
struct Gamma {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Gamma[%]", editor: range, min: 0, max: 3, range_min: 0, range_max: 300, range_default: 100
  float gamma;
};

vec4 texture(Gamma s, vec2 tex_coords) {
  vec4 color = texture(s.sampler, tex_coords);
  float gammaR = max(1. / s.gamma, 0.00001);
  
  vec4 colorGamma;
  colorGamma.r = pow(max(color.r,0.0), gammaR);
  colorGamma.g = pow(max(color.g,0.0), gammaR);
  colorGamma.b = pow(max(color.b,0.0), gammaR);
  colorGamma.a = color.a;
  
  return mix(color, colorGamma, s.mix);
}
