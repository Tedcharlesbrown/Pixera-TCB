// Author: Andreas Leeb
// Version: 1.0

//@implements: sampler2D
struct LumaKey {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
  float mix;
  //@ label: "MinLuma", editor: range, min: 0, max: 1, range_min: 0, range_max: 10000, range_default: 0
  float minL;
  //@ label: "MaxLuma", editor: range, min: 0, max: 1, range_min: 0, range_max: 10000, range_default: 500
  float maxL;
  //@ label: "Softness", editor: range, min: 0, max: .01, range_min: 0, range_max: 100, range_default: 30
  float softness;
};

vec4 texture(LumaKey s, vec2 tex_coords) {
  vec4 color = texture(s.sampler, tex_coords);
  
  float lum = .299 * color.r + .587 * color.g + .114 * color.b;
  
  if(s.minL == s.maxL) return color;
  
  if(lum >= s.minL - s.softness && lum <= s.maxL + s.softness) {
    color.a = 1. - smoothstep(s.minL - s.softness, s.minL, lum) + smoothstep(s.maxL, s.maxL + s.softness, lum);
  }
  
  color.rgb *= color.a;
  return mix(texture(s.sampler, tex_coords), color, s.mix);
}
