// Author: Andreas Leeb
// Version: 1.0
// EDITED: Adrian

//@implements: sampler2D
struct DropShadow {
  sampler2D sampler;
  sampler2D s2;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Width[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1920
  float width;
  //@ label: "Height[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1080
  float height;
  //@ label: "Strength", editor: range, min: 0, max: 30, range_min: 0, range_max: 30, range_default: 15
  float strength;
  //@ label: "Performance", editor: range, min: 0, max: 35, range_min: 0, range_max: 35, range_default: 10
  float performance;
  //@ label: "Optimize", editor: range, min: 1, max: 5, range_min: 1, range_max: 5, range_default: 2
  float optimize;
  //@ label: "Angle[deg]", editor: range, min: 0, max: 360, range_min: 0, range_max: 360, range_default: 225
  float angle;
};

vec4 texel(DropShadow s, vec2 dim, vec2 abs_coords) {
  vec2 tex_coords = abs_coords * dim;
  return texture(s.sampler, tex_coords);
}

vec4 texture(DropShadow s, vec2 tex_coords) {
  const float alphaThreshold = .9;
  vec2 dim = vec2(s.width, s.height);
  //EDIT: Added inversion of dims here, so that it doesn't have to be calculated in the loop.
  vec2 dimInverse = vec2(1.0) / dim;
  vec4 tex = texture(s.sampler, tex_coords);
  if(tex.a >= alphaThreshold) return tex;
  vec2 abs_coords = tex_coords * dim;
  vec3 shadowColor = vec3(0);
  tex = vec4(shadowColor, 0);
    
  s.strength = clamp(s.strength, 0., 200.);
  int k = int(s.strength); // length/height[px] of the area to scan
  int optimize = int(clamp(s.optimize, 1., 100.)); // quantisizes the scan interval (e.g. double the alpha weight of neighbor while skipping every second neighbor pixel
  float factor = 2. / (k * k * 20.) * optimize * (1. + s.performance * .03);
  float ignore = floor(s.strength * .02 * s.performance); // ignore the pixel itself and some close neighbors, for performance reasons
  float rads = radians(s.angle);
  vec2 rotation = vec2(cos(rads), sin(rads));
    
  for(int i = 0; i <= k; i += 2) {
    if(i <= ignore) continue;
    for(int j = 0; j <= k; j += optimize) {
      if(j <= ignore) continue;
      vec2 offset = vec2(i, j) * rotation;
      vec2 n_coords = abs_coords + offset;
      vec4 neighbor = texel(s, dimInverse, n_coords);
      // EDIT: if condition replaced with step function.
      // if current pixel is transparent and "neighbor" opaque
      // increase current pixel's opacity, proportional to distance from opaque neighbor
      tex.a += step(alphaThreshold, neighbor.a) * (distance(abs_coords, n_coords) * factor);
    }
  }

  tex = mix(texture(s.sampler, tex_coords), tex, s.mix);
  return tex;
}
