// Author: Andreas Leeb
// Version: 1.0

//@implements: sampler2D
struct Dissolve {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Strength[%]", editor: range, min: 0, max: .1, range_min: 0, range_max: 100, range_default: 10
  float strength;
};

float ds_rand(vec2 co){
    return fract(sin(dot(co.xy, vec2(12.9898, 78.233))) * 43758.5453);
}

vec4 texture(Dissolve s, vec2 tex_coords) {
  vec4 orig = texture(s.sampler, tex_coords);
  vec4 color = vec4(0.);
  tex_coords += ds_rand(vec2(tex_coords)) * s.strength;
  color += texture(s.sampler, tex_coords);
  return mix(orig,color,s.mix);
}
