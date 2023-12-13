// Author: Andreas Leeb
// Version: 1.0p

//@implements: sampler2D
struct Noise {
  sampler2D sampler;
   //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Size", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 500
  float size;
  //@ label: "Time", editor: range, min: 0, max: 1000, range_min: 0, range_max: 1000, range_default: 0
  float time;
  //@ label: "Width[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1920
  float width;
  //@ label: "Height[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1200
  float height;
  //@ label: "BlackColor Red", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0, group: rgbaColorPicker, group_label: "Black Color", partInfo: 1-2
  float blackColorRed;
  //@ label: "BlackColor Green", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0, group: rgbaColorPicker
  float blackColorGreen;
  //@ label: "BlackColor Blue", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0, group: rgbaColorPicker
  float blackColorBlue;
  //@ label: "BlackColor Alpha", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255, group: rgbaColorPicker
  float blackColorAlpha;
  //@ label: "WhiteColor Red", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255, group: rgbaColorPicker, group_label: "White Color", partInfo: 2-2
  float whiteColorRed;
  //@ label: "WhiteColor Green", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255, group: rgbaColorPicker
  float whiteColorGreen;
  //@ label: "WhiteColor Blue", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255, group: rgbaColorPicker
  float whiteColorBlue;
  //@ label: "WhiteColor Alpha", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255, group: rgbaColorPicker
  float whiteColorAlpha;
};

float ns_rand(vec2 xy, float time) {
  return fract(sin(dot(xy, vec2(5.33312, 19.0207963))) * 214758.878 * sin(time + .16434));
}

vec4 texture(Noise s, vec2 tex_coords) {
  vec2 dim = vec2(s.width, s.height);
  vec4 orig = texture(s.sampler, tex_coords);
  vec4 blackColor = vec4(s.blackColorRed, s.blackColorGreen, s.blackColorBlue, s.blackColorAlpha);
  vec4 whiteColor = vec4(s.whiteColorRed, s.whiteColorGreen, s.whiteColorBlue, s.whiteColorAlpha);
  
  vec4 color = texture(s.sampler, tex_coords);
  vec2 scaledCoords = (tex_coords * dim / dim.y) * s.size;
  float rand = ns_rand(floor(scaledCoords), s.time);
  vec4 noise = mix(blackColor, whiteColor, rand);
  color = mix(color, noise, s.mix);
  color.a = color.a < orig.a ? color.a : orig.a;
  return color;
}
