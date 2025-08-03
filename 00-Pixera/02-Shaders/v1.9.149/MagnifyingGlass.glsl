// Author: Andreas Leeb
// Version: 1.0

//@implements: sampler2D
struct MagnifyingGlass {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
  float mix;
  //@ label: "Radius", editor: range, min: 0, max: 1.415, range_min: 0, range_max: 1415, range_default: 250
  float radius;
  //@ label: "xPosition", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 500
  float x;
  //@ label: "yPosition", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 500
  float y;
  //@ label: "Scale[%]", editor: range, min: .1, max: 10., range_min: 10, range_max: 1000, range_default: 200
  float scale;
};

vec4 texture(MagnifyingGlass s, vec2 tex_coords) {
  vec4 orig = texture(s.sampler, tex_coords);
  vec2 center = vec2(s.x, s.y);
  float dst = distance(tex_coords, center);
  
  float scaleRec = 1. / s.scale;
  mat2 scale = mat2(scaleRec, 0., 0., scaleRec);
  if(dst <= s.radius)
    tex_coords = fract(scale * (tex_coords - center) + center);
  
  return mix(orig,texture(s.sampler, tex_coords),s.mix);
}
