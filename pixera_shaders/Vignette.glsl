// Author: Andreas Leeb
// Version: 1.0

//@implements: sampler2D
struct Vignette {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
  float mix;
  //@ label: "Width[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 50
  float width;
};

#define BLACK vec3(0.)
#define HALF_SQRT_2 0.7071067812

vec4 texture(Vignette s, vec2 tex_coords) {
  vec4 color = texture(s.sampler, tex_coords);
  vec2 center = vec2(.5);
  
  float radius = HALF_SQRT_2 - s.width;
  float dst = distance(tex_coords, center);
  
  float weight = 1. - smoothstep(0., 1., (HALF_SQRT_2 - dst) / (HALF_SQRT_2 - radius));
  color.rgb = mix(color.rgb, BLACK, vec3(weight) * step(radius, dst));
  return mix(texture(s.sampler, tex_coords), color, s.mix);
}
