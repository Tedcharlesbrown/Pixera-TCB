// Author: Andreas Leeb
// Version: 1.0

//@implements: sampler2D
struct BoxBlur {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Strength", editor: range, min: 1, max: 10, range_min: 1, range_max: 10, range_default: 1
  float strength;
  //@ label: "Width[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1920
  float width;
  //@ label: "Height[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1080
  float height;
};

vec4 bb_texel(BoxBlur s, vec2 dim, vec2 abs_coords) {
  vec2 tex_coords = abs_coords / dim;
  return texture(s.sampler, tex_coords);
}

vec4 texture(BoxBlur s, vec2 tex_coords) {
  vec4 orig = texture(s.sampler, tex_coords);
  vec4 color = vec4(vec3(0.), orig.a);
  vec2 dim = vec2(s.width, s.height);
  vec2 abs_coords = tex_coords * dim;
  
  int count = 0;
  int maxOffset = int(s.strength);
  // kernel size NxN, N = 2 * maxOffset + 1
  for(int x = -maxOffset; x <= maxOffset; x++) {
    for(int y = -maxOffset; y <= maxOffset; y++) {
      vec2 coords = abs_coords + vec2(x, y);
      if(coords.x >= 0. && coords.x <= dim.x && coords.y >= 0. && coords.y <= dim.y) {
  	    count++;
  	    color += bb_texel(s, dim, coords);
      }
    }
  }
  color /= count;
  return mix(texture(s.sampler, tex_coords), color, s.mix);
}
