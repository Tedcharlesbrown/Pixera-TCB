// Author: Andreas Leeb
// Version: 1.0

//@implements: sampler2D
struct ColorChange {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
  float mix;
  //@ label: "Time", editor: range, min: 0, max: 100, range_min: 0, range_max: 100, range_default: 0
  float time;
  //@ label: "Speed", editor: range, min: .1, max: 10, range_min: 1, range_max: 100, range_default: 10
  float speed;
};

vec3 cc_rgb2hsv(vec3 c) {
  vec4 K = vec4(0., -1. / 3., 2. / 3., -1.);
  vec4 p = mix(vec4(c.bg, K.wz), vec4(c.gb, K.xy), step(c.b, c.g));
  vec4 q = mix(vec4(p.xyw, c.r), vec4(c.r, p.yzx), step(p.x, c.r));

  float d = q.x - min(q.w, q.y);
  float e = 1.0e-10;
  return vec3(abs(q.z + (q.w - q.y) / (6. * d + e)), d / (q.x + e), q.x);
}

vec3 cc_hsv2rgb(vec3 c) {
  vec4 K = vec4(1., 2. / 3., 1. / 3., 3.);
  vec3 p = abs(fract(c.xxx + K.xyz) * 6. - K.www);
  return c.z * mix(K.xxx, clamp(p - K.xxx, 0., 1.), c.y);
}

vec4 texture(ColorChange s, vec2 tex_coords) {
  vec4 color = texture(s.sampler, tex_coords);
  vec3 hsv = cc_rgb2hsv(color.rgb);
  hsv.x = (sin(s.time * s.speed) + 1.) / 2.;
  color.rgb = cc_hsv2rgb(hsv);
  color = mix(texture(s.sampler, tex_coords), color, s.mix);
  return color;
}
