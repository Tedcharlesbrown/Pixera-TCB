#version 450
// Author: Andreas Leeb
// Version: 1.0

precision highp float;

//@implements: sampler2D
struct Relief {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Direction", editor: enum, enum_default: 0, values: "Left, Down, Right, Up"
  int direction;
  //@ label: "Width[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1920
  float width;
  //@ label: "Height[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1200
  float height;
};

vec4 rl_texel(Relief s, vec2 dim, vec2 abs_coords) {
  vec2 tex_coords = abs_coords / dim;
  return texture(s.sampler, tex_coords);
}



const mat3 weight1 = mat3(-2., -1.,  0.,
                          -1.,  1.,  1.,
                           0.,  1.,  2.);
const mat3 weight2 = mat3( 0.,  1.,  2.,
                          -1.,  1.,  1.,
                          -2., -1.,  0.);
const mat3 weight3 = mat3( 2.,  1.,  0.,
                           1.,  1., -1.,
                           0., -1., -2.);
const mat3 weight4 = mat3( 0., -1., -2.,
                           1.,  1., -1.,
                           2.,  1.,  0.);
                          
const mat3 weights[] = mat3[](weight1, weight2, weight3, weight4);
const float weightSum = 8.;

const vec2 offset[] = vec2[](vec2(-1.,  1.), vec2(0.,  1.), vec2(1.,  1.),
                             vec2(-1.,  0.), vec2(0.,  0.), vec2(1.,  0.),
                             vec2(-1., -1.), vec2(0., -1.), vec2(1., -1.));

vec4 texture(Relief s, vec2 tex_coords) {
  //vec2 dim = textureSize(s.sampler, 0);      // for GPUpad
  vec2 dim = vec2(s.width, s.height);        // for Wings
  vec4 color = vec4(0.);
  
  int direction = int(s.direction);
  vec2 abs_coords = tex_coords * dim;
  for(int i = 0; i < offset.length(); i++) {
    vec2 coords = abs_coords + offset[i];
    if(any(lessThan(coords, vec2(0.))) || any(greaterThan(coords, dim)))
      coords = abs_coords;
      
    vec4 texel = rl_texel(s, dim, coords);
    color.rgb += texel.rgb * weights[direction][i/3][i%3];
    color.a = texel.a;
  }
  
  return mix(texture(s.sampler, tex_coords), color, s.mix);
}
