// Author: Andreas Leeb
// Version: 1.1p

uniform float opacity;

//@implements: sampler2D
struct SolidColor {
  sampler2D sampler;
  //@ label: "Mix", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
  float mix;
  //@ label: "Red", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255
  float red;
  //@ label: "Green", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255
  float green;
  //@ label: "Blue", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255
  float blue;
  //@ label: "Alpha", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 100
  float alpha;
};

vec4 texture(SolidColor s, vec2 tex_coords) {
  vec4 orig = texture(s.sampler, tex_coords);
  return mix(orig,vec4(s.red, s.green, s.blue, s.alpha*orig.a),s.mix);
}
