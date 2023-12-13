//@implements: sampler2D
struct Blank {
  sampler2D sampler;
  //@ label: "Dummy", editor: range, min: 0.0, max: 1.0, range_min: 0, range_max: 1, range_default: 0
  float Dummy;
};

vec4 texture(Blank s, vec2 tex_coords) {
  return texture(s.sampler, tex_coords);
}
