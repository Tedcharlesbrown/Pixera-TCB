// Author: Andreas Leeb
// Version 1.0p

//@implements: sampler2D
struct AlphaWipe {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Direction[deg]", editor: range, min: 0, max: 360, range_min: 0, range_max: 360, range_default: 0
  float direction;
  //@ label: "Position[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 50
  float position;
  //@ label: "Width[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 10
  float width;
  //@ label: "Inverse", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
  float inverse;
};

vec4 texture(AlphaWipe s, vec2 tex_coords) {
  s.direction = radians(s.direction);
  vec2 dir = vec2(cos(s.direction), sin(s.direction));
  float diag = 1. / dot(abs(dir), vec2(1.));
  dir *= diag;
  float width = (s.width) * diag;

  vec4 color = texture(s.sampler, tex_coords);
  float pos = dot(tex_coords * 2. - 1., dir) * .5 + .5;
  float alpha = (((s.position) * (1. + width)) - pos) / width;

  alpha = 1.57079633 * clamp (alpha, 0., 1.);
  alpha = abs(s.inverse - sin(alpha));
  color.a = mix(color.a, (color.a *alpha),s.mix);
  //color.rgb *= color.a;
  return color;
}
