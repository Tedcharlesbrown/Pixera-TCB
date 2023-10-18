// Author: Andreas Leeb
// Version: 1.0p

//@implements: sampler2D
struct ColorStripes {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
  float mix;
  //@ label: "Amount", editor: range, min: 1, max: 100, range_min: 1, range_max: 100, range_default: 15
  float amount;
  //@ label: "Seed", editor: range, min: .00001, max: 1, range_min: 1, range_max: 10000, range_default: 1000
  float seed;
  //@ label: "Vertical", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
  float vertical;
};

vec3 cs_rgb2hsv(vec3 c) {
  vec4 K = vec4(0., -1. / 3., 2. / 3., -1.);
  vec4 p = mix(vec4(c.bg, K.wz), vec4(c.gb, K.xy), step(c.b, c.g));
  vec4 q = mix(vec4(p.xyw, c.r), vec4(c.r, p.yzx), step(p.x, c.r));

  float d = q.x - min(q.w, q.y);
  float e = 1.0e-10;
  return vec3(abs(q.z + (q.w - q.y) / (6. * d + e)), d / (q.x + e), q.x);
}

vec3 cs_hsv2rgb(vec3 c) {
  vec4 K = vec4(1., 2. / 3., 1. / 3., 3.);
  vec3 p = abs(fract(c.xxx + K.xyz) * 6. - K.www);
  return c.z * mix(K.xxx, clamp(p - K.xxx, 0., 1.), c.y);
}

vec4 texture(ColorStripes s, vec2 tex_coords) {
  vec4 color = texture(s.sampler, tex_coords);
  vec4 orig = color;
  if(s.vertical > 0.) tex_coords.xy = tex_coords.yx;
  
  float stripe = floor(tex_coords.y * s.amount);
  vec3 hsv = cs_rgb2hsv(color.rgb);
  hsv.x = fract(sin(stripe) * 1000. * s.seed);
  color.rgb = cs_hsv2rgb(hsv);
  
  return mix(orig, color, s.mix);
}
