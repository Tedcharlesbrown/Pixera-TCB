// Author: Andreas Leeb
// Version: 1.0p

//@implements: sampler2D
struct LedEffect {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
  float mix;
  //@ label: "Amount", editor: range, min: 1, max: 250, range_min: 1, range_max: 250, range_default: 50
  float amount;
  //@ label: "Softness[%]", editor: range, min: 0, max: .5, range_min: 0, range_max: 100, range_default: 20
  float softness;
  //@ label: "Gap[%]", editor: range, min: 0, max: 2, range_min: 0, range_max: 200, range_default: 25
  float gap;
  //@ label: "Gap Red", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
  float gapR;
  //@ label: "Gap Green", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
  float gapG;
  //@ label: "Gap Blue", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
  float gapB;
  //@ label: "Gap Alpha", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 100
  float gapA;
};

vec4 le_texel(LedEffect s, vec2 dim, vec2 abs_coords) {
  vec2 tex_coords = abs_coords / dim;
  return texture(s.sampler, tex_coords);
}

vec4 texture(LedEffect s, vec2 tex_coords) {
  vec2 dim = vec2(1920., 1080.);
  vec4 orig = texture(s.sampler, tex_coords);
  dim = vec2(16., 10.66666);
  vec2 abs_coords = tex_coords * dim;
  
  vec4 gapColor = vec4(s.gapR * s.gapA, s.gapG * s.gapA, s.gapB * s.gapA, s.gapA);
  
  float diameter = dim.y / s.amount;
  float radius = diameter / 2.;
  float gap = diameter * s.gap;
  diameter += gap;
  
  vec2 center = gap / 2. + floor(abs_coords / diameter) * diameter + radius; // center pixel of LED
  vec4 color = le_texel(s, dim, center);
  
  float softTol = radius * s.softness;
  float dst = distance(abs_coords, center);
  return mix(orig,mix(color, gapColor, smoothstep(radius - softTol, radius + softTol, dst)),s.mix);
}
