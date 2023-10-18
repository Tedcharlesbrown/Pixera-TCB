// Author: Andreas Leeb
// Edited by Ted Charles Brown - added aspect ratio
// Version: 1.1

//@implements: sampler2D
struct Vignette_AspectRatio {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
  float mix;
  //@ label: "Strength[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 50
  float Strength;
  //@ label: "Width[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1920
  float width;
  //@ label: "Height[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1080
  float height;
};

#define BLACK vec3(0.)
#define HALF_SQRT_2 0.7071067812

vec4 texture(Vignette_AspectRatio s, vec2 tex_coords) {
  vec4 color = texture(s.sampler, tex_coords);
  vec2 center = vec2(.5);

  vec2 aspectAdjusted = vec2(s.width / s.height, 1.0);
  vec2 distFromCenter = (tex_coords - center) * aspectAdjusted;
  
  float radius = HALF_SQRT_2 - s.Strength;
  float dst = length(distFromCenter);
  
  float weight = 1. - smoothstep(0., 1., (HALF_SQRT_2 - dst) / (HALF_SQRT_2 - radius));
  color.rgb = mix(color.rgb, BLACK, vec3(weight) * step(radius, dst));
  return mix(texture(s.sampler, tex_coords), color, s.mix);
}
