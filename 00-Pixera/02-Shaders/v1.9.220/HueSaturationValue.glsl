// Author: Andreas Leeb
// Version: 1.0

//@implements: sampler2D
struct HueSaturationValue {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Hue[deg]", editor: range, min: 0, max: 1, range_min: 0, range_max: 360, range_default: 0, group: hsvColorWheel, group_label: "HSV"
  float hue;
  //@ label: "Saturation[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float saturation;
  //@ label: "Value[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float value;
};

vec3 hsv_to_rgb(vec3 hsv) {
  return clamp(vec3(abs(3. - 6. * hsv.x) - 1.,
                2. - abs(2. - 6. * hsv.x),
                2. - abs(4. - 6. * hsv.x)), 0., 1.) * hsv.y * hsv.z + hsv.z * (1. - hsv.y);
}

vec3 rgb_to_hsv(vec3 c) {
  const vec4 cx = vec4(1., 0., 1. / 6., 2. / 6.);

  vec3 d = c.grb - c.bgr;

  vec4 c1 = d.x >= 0. ? vec4(c.rgg, 1.) : vec4(c.brb, -1.);
  vec4 c2 = c1.w * d.y >= 0. ? cx.xyyy : (c1.w * d.z >= 0. ? cx.yxyw : cx.yyxz);

  float delta = -dot(d.zyx, c2.xyz);
  float max = dot(c1.xyz, c2.xyz);

  return vec3(
    abs(delta) > 0. ?
      (dot(d.xzy, c2.xyz) / delta * (1. / 6.) + c2.w - c1.w * .25 + .25) :
      0.,
    max > 0.0 ? abs(delta) / max : 0.0,
    max);
}

vec4 texture(HueSaturationValue s, vec2 tex_coords) {
  vec4 color = texture(s.sampler, tex_coords);
  vec4 orig = color;
  vec3 hsv = rgb_to_hsv(color.rgb);
  hsv.x += s.hue;
  hsv.x = fract(hsv.x);
  hsv.y += hsv.y * (s.saturation);
  hsv.z += hsv.z * (s.value);
  return mix(orig,vec4(hsv_to_rgb(hsv), color.a),s.mix);
}
