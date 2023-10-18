// Author: Andreas Leeb
// Version: 1.0p

//@implements: sampler2D
struct Solarize {
  sampler2D sampler;
  //@ label: "Mix", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
  float mix;
  //@ label: "Threshold", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 128
  float threshold;
  //@ label: "Below", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
  float below;
};

vec4 texture(Solarize s, vec2 tex_coords) {
  vec4 color = texture(s.sampler, tex_coords);
  vec4 orig = color;
  if(s.below > 0) {
    if(color.r <= s.threshold) {
  	  color.r = 1. - color.r;
    }
    if(color.g <= s.threshold) {
  	  color.g = 1. - color.g;
    }
    if(color.b <= s.threshold) {
      color.b = 1. - color.b;
    }
  } else {
  	if(color.r >= s.threshold) {
  	  color.r = 1. - color.r;
    }
    if(color.g >= s.threshold) {
  	  color.g = 1. - color.g;
    }
    if(color.b >= s.threshold) {
      color.b = 1. - color.b;
    }
  }
  return mix(orig,color,s.mix);
}
