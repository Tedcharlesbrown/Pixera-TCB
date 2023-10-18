// Author: Andreas Leeb
// Version: 1.0

//@implements: sampler2D
struct Pixelate {
  sampler2D sampler;
  //@ label: "Width[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1920
  float width;
  //@ label: "Height[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1200
  float height;
  //@ label: "Pixels", editor: range, min: 1, max: 1000, range_min: 1, range_max: 1000, range_default: 100
  float amount;
};

vec4 texture(Pixelate s, vec2 tex_coords) {
  vec2 dim = vec2(s.width, s.height);
  vec2 abs_coords = tex_coords * dim;
  
  float height = dim.y / s.amount;
  abs_coords = floor(abs_coords / height) * height;
  return texture(s.sampler, abs_coords / dim);
}
