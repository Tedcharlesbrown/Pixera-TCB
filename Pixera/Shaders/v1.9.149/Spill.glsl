// Author: Andreas Leeb
// Version: 1.0p

//@implements: sampler2D
struct Spill {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
  float mix;
  //@ label: "Red", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
  float red;
  //@ label: "Green", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 255
  float green;
  //@ label: "Blue", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
  float blue;
  //@ label: "Lightness", editor: range, min: 0, max: 2, range_min: 0, range_max: 200, range_default: 100
  float lightness;
  //@ label: "Saturation", editor: range, min: 0, max: 2, range_min: 0, range_max: 200, range_default: 100
  float saturation;
  //@ label: "HueTolerance", editor: range, min: 0, max: .3, range_min: 0, range_max: 1000, range_default: 1000
  float hueTol;
  //@ label: "LightnessTolerance", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 1000
  float lightTol;
};

vec3 sp_rgb2hsv(vec3 c) {
  vec4 K = vec4(0., -1. / 3., 2. / 3., -1.);
  vec4 p = mix(vec4(c.bg, K.wz), vec4(c.gb, K.xy), step(c.b, c.g));
  vec4 q = mix(vec4(p.xyw, c.r), vec4(c.r, p.yzx), step(p.x, c.r));

  float d = q.x - min(q.w, q.y);
  float e = 1.0e-10;
  return vec3(abs(q.z + (q.w - q.y) / (6. * d + e)), d / (q.x + e), q.x);
}

vec3 sp_hsv2rgb(vec3 c) {
  vec4 K = vec4(1., 2. / 3., 1. / 3., 3.);
  vec3 p = abs(fract(c.xxx + K.xyz) * 6. - K.www);
  return c.z * mix(K.xxx, clamp(p - K.xxx, 0., 1.), c.y);
}

vec4 texture(Spill s, vec2 tex_coords) {
  vec4 color = texture(s.sampler, tex_coords);
  vec3 sHsv = sp_rgb2hsv(vec3(s.red, s.green, s.blue));
  vec3 tHsv = sp_rgb2hsv(color.rgb);
  
  if(tHsv.x >= sHsv.x - s.hueTol && tHsv.x <= sHsv.x + s.hueTol &&
     tHsv.z >= sHsv.z - s.lightTol && tHsv.z <= sHsv.z + s.lightTol) {
    tHsv.y *= s.saturation;
    tHsv.z *= s.lightness;
    color.rgb = sp_hsv2rgb(tHsv);
  }
  
  return mix(texture(s.sampler, tex_coords), color, s.mix);
}
