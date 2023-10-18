// Author: Andreas Leeb
// Version: 1.1

//@implements: sampler2D
struct Reflection {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
  float mix;
  //@ label: "Strength", editor: range, min: 0.3, max: 1, range_min: 30, range_max: 100, range_default: 60
  float strength;
  //@ label: "PositionY", editor: range, min: 0, max: 0.5, range_min: 0, range_max: 50, range_default: 10
  float posY;
};

vec4 texture(Reflection s, vec2 tex_coords) {
  vec4 colorOrig = texture(s.sampler, tex_coords);
  vec2 n_coords = tex_coords / (1. - s.posY); // scale
  n_coords.y -= s.posY / (1. - s.posY); // move up
  n_coords.x -= s.posY / (1. - s.posY) * .5; // move to center
  
  if(n_coords.x < 0. || n_coords.x > 1.) return mix(colorOrig, vec4(0.), s.mix);
  
  if(tex_coords.y < s.posY) {
    vec2 coords = vec2(n_coords.x, 1. - n_coords.y); // reflection
    vec4 color = texture(s.sampler, fract(coords));
    color.a *= smoothstep(0., 1., tex_coords.y / s.posY * s.strength) * s.strength;
    return mix(colorOrig, color, s.mix);
  }
  
  return mix(colorOrig, texture(s.sampler, fract(n_coords)), s.mix);
}
