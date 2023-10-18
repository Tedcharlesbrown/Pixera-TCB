// Author: Andreas Leeb
// Version: 1.0p

//@implements: sampler2D
struct Checkerboard {
  sampler2D sampler;
  //@ label: "Rows", editor: range, min: 1, max: 1000, range_min: 1, range_max: 1000, range_default: 8
  float rows;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 50
  float mix;
  //@ label: "Width[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1920
  float width;
  //@ label: "Height[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1080
  float height;
  //@ label: "BlackColor Red", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
  float blackColorRed;
  //@ label: "BlackColor Green", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
  float blackColorGreen;
  //@ label: "BlackColor Blue", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
  float blackColorBlue;
  //@ label: "BlackColor Alpha", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 100
  float blackColorAlpha;
  //@ label: "WhiteColor Red", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255
  float whiteColorRed;
  //@ label: "WhiteColor Green", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255
  float whiteColorGreen;
  //@ label: "WhiteColor Blue", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255
  float whiteColorBlue;
  //@ label: "WhiteColor Alpha", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 100
  float whiteColorAlpha;
  //@ label: "NonSquareAllowed", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
  float nonSqA;
};

vec4 texture(Checkerboard s, vec2 tex_coords) {
  vec2 dim = vec2(s.width, s.height);
  
  vec4 color = texture(s.sampler, tex_coords);
  vec4 blackColor = vec4(s.blackColorRed, s.blackColorGreen, s.blackColorBlue, s.blackColorAlpha);
  vec4 whiteColor = vec4(s.whiteColorRed, s.whiteColorGreen, s.whiteColorBlue, s.whiteColorAlpha);
  vec4 orig = color;
  
  if(s.nonSqA == 0.) tex_coords *= dim / dim.y;
  
  float size = 1. / s.rows;
  bool x = int(floor(tex_coords.x / size)) % 2 == 0;
  bool y = int(floor(tex_coords.y / size)) % 2 == 1;
  color = mix(blackColor, whiteColor, x && !y || !x && y);
  color = mix(orig, color, s.mix);
  return color;
}
