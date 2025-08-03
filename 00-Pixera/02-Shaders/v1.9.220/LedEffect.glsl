// Author: Andreas Leeb
// Version: 1.0p

//@implements: sampler2D
struct LedEffect {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Amount", editor: range, min: 1, max: 250, range_min: 1, range_max: 250, range_default: 50
  float amount;
  //@ label: "Softness[%]", editor: range, min: 0, max: .5, range_min: 0, range_max: 100, range_default: 20
  float softness;
  //@ label: "Gap[%]", editor: range, min: 0, max: 2, range_min: 0, range_max: 200, range_default: 25
  float gap;
  //@ label: "Gap Red", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0, group: rgbaColorPicker, group_label: "Gap Color"
  float gapR;
  //@ label: "Gap Green", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0, group: rgbaColorPicker
  float gapG;
  //@ label: "Gap Blue", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0, group: rgbaColorPicker
  float gapB;
  //@ label: "Gap Alpha", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255, group: rgbaColorPicker
  float gapA;
  
  //@ label: "Square", editor: bool, bool_default: false
  bool square;
  //@ label: "Width[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1920
  float width;
  //@ label: "Height[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1080
  float height;
};

vec4 le_texel(LedEffect s, vec2 dim, vec2 abs_coords) {
  vec2 tex_coords = abs_coords / dim;
  return texture(s.sampler, tex_coords);
}

vec4 texture(LedEffect s, vec2 tex_coords) {
  vec2 dim = vec2(s.width, s.height);
  vec4 orig = texture(s.sampler, tex_coords);
  vec2 abs_coords = tex_coords * dim;
  
  vec4 gapColor = vec4(s.gapR, s.gapG, s.gapB, s.gapA);
  
  float diameter = dim.y / s.amount;
  float radius = diameter / 2.;
  float gap = diameter * s.gap;
  diameter += gap;
  
  vec2 center = gap / 2. + floor(abs_coords / diameter) * diameter + radius; // center pixel of LED
  vec4 color = le_texel(s, dim, center);
  
  float softTol = radius * s.softness;
  
  float dst;
  if (s.square) {
    // Use Manhattan distance for square effect
    dst = max(abs(abs_coords.x - center.x), abs(abs_coords.y - center.y));
  } else {
    // Euclidean distance for circle effect
    dst = distance(abs_coords, center);
  }
  
  vec4 result = mix(orig,mix(color, gapColor, smoothstep(radius - softTol, radius + softTol, dst)),s.mix);
  result.a = orig.a;
  return result;
}
