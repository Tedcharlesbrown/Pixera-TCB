// Author: Andreas Leeb
// Version: 1.0p

//@implements: sampler2D
struct BoxBlurSep {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Strength", editor: range, min: 1, max: 50, range_min: 1, range_max: 50, range_default: 1
  float strength;
  //@ label: "Horizontal", editor: bool, bool_default: true
  bool horizontal;
  //@ label: "Width[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1920
  float width;
  //@ label: "Height[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1200
  float height;
};

vec4 bbs_texel(BoxBlurSep s, vec2 dim, vec2 abs_coords) {
  vec2 tex_coords = abs_coords / dim;
  return texture(s.sampler, tex_coords);
}

vec4 texture(BoxBlurSep s, vec2 tex_coords) {
  vec4 color = vec4(vec3(0.), 1.);
  vec2 dim = vec2(s.width, s.height);
  vec2 abs_coords = tex_coords * dim;
  
  if(s.mix/100. == 0.0)
  {
  	return texture(s.sampler, tex_coords);
  }
  
  int horizontal = 0;
  if(s.horizontal)
  {
    horizontal = 1;
  }
  
  float vertical = 1 - horizontal;
  int maxOffset = int(s.strength);
  int count = 0;
  for(int x = -maxOffset; x <= maxOffset; x++) {
    vec2 coords = abs_coords + vec2(x * horizontal, x * vertical);
    if(coords.x >= 0. && coords.x <= dim.x && coords.y >= 0. && coords.y <= dim.y) { // for nice borders
  	  color += bbs_texel(s, dim, coords);
  	  count++;
    }
  }
  
  color /= count;
  color = mix(texture(s.sampler, tex_coords),color, s.mix);
  return color;
}
