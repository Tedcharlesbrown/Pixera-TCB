// Author: Andreas Leeb
// Version: 1.1

//@implements: sampler2D
struct Keystoning {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
	float mix;
  //@ label: "LeftUpperX", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 100
  float lux;
  //@ label: "LeftUpperY", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 1000
  float luy;
  //@ label: "RightUpperX", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 900
  float rux;
  //@ label: "RightUpperY", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 1000
  float ruy;
  //@ label: "LeftLowerX", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 0
  float llx;
  //@ label: "LeftLowerY", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 0
  float lly;
  //@ label: "RightLowerX", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 1000
  float rlx;
  //@ label: "RightLowerY", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 0
  float rly;
};

vec4 texture(Keystoning s, vec2 tex_coords) {
   vec4 orig = texture(s.sampler, tex_coords);
  // Derivation: https://www.particleincell.com/2012/quad-interpolation/
  
  float a1 = s.llx, a2 = s.rlx - s.llx, a3 = s.lux - s.llx, a4 = -s.lux + s.rux - s.rlx + s.llx;
  float b1 = s.lly, b2 = s.rly - s.lly, b3 = s.luy - s.lly, b4 = -s.luy + s.ruy - s.rly + s.lly;
  
  float aa = a4*b3 - a3*b4;
  float bb = a4*b1 - a1*b4 + a2*b3 - a3*b2 + tex_coords.x*b4 - tex_coords.y*a4;
  float cc = a2*b1 - a1*b2 + tex_coords.x*b2 - tex_coords.y*a2;
  
  const float minNonZero = .0005;
  aa = (abs(aa) < minNonZero) ? minNonZero : aa;
  // if both dividend and divisor == 0, it should still work, thus replaced 0 with very small non-0
  float m = (-bb + sqrt(bb*bb - 4.*aa*cc)) / (2.*aa);
  float n = (tex_coords.x - a1 - a3*m) / (a2 + a4*m);
  
  if(m >= 0. && n >= 0. && m <= 1. && n <= 1.)
    return mix(orig, texture(s.sampler, vec2(n, m)), s.mix);
  
  return mix(orig, vec4(vec3(0.), 0.), s.mix);
}
