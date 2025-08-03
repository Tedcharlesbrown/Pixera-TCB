// Author: Andreas Leeb
// Version: 1.0p

//@implements: sampler2D
struct ChromaKey {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Hue", editor: range, min: 0, max: 1, range_min: 0, range_max: 360, range_default: 120, group: hsvColorWheel, group_label: "Color"
  float hue;
  //@ label: "Saturation", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 100, group: hsvColorWheel
  float saturation;
  //@ label: "Value", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 100, group: hsvColorWheel
  float value;
  //@ label: "HueTolerance", editor: range, min: 0, max: .3, range_min: 0, range_max: 1000, range_default: 1000
  float hueTol;
  //@ label: "LightnessTolerance", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 1000
  float lightTol;
};

vec3 ck_rgb2hsv(vec3 c) {
  vec4 K = vec4(0., -1. / 3., 2. / 3., -1.);
  vec4 p = mix(vec4(c.bg, K.wz), vec4(c.gb, K.xy), step(c.b, c.g));
  vec4 q = mix(vec4(p.xyw, c.r), vec4(c.r, p.yzx), step(p.x, c.r));

  float d = q.x - min(q.w, q.y);
  float e = 1.0e-10;
  return vec3(abs(q.z + (q.w - q.y) / (6. * d + e)), d / (q.x + e), q.x);
}

vec4 texture(ChromaKey s, vec2 tex_coords) {
  vec4 color = texture(s.sampler, tex_coords);
  vec4 orig = color;
  vec3 sHsv = vec3(s.hue, s.saturation, s.value);
  vec3 tHsv = ck_rgb2hsv(color.rgb);
  
  if(tHsv.x >= sHsv.x - s.hueTol && tHsv.x <= sHsv.x + s.hueTol &&
     tHsv.z >= sHsv.z - s.lightTol && tHsv.z <= sHsv.z + s.lightTol)
    color.a = 0.;
  
  color.rgb *= color.a;
  return mix(orig, color, s.mix);
}
