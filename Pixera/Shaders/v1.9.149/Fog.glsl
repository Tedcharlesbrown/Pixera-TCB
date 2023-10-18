// Author: Andreas Leeb
// Version: 1.0p

//@implements: sampler2D
struct Fog {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
  float mix;
  //@ label: "Time", editor: range, min: 0, max: 100, range_min: 0, range_max: 1, range_default: 1
  float time;
  //@ label: "TimeMultiplier", editor: range, min: 1, max: 100, range_min: 1, range_max: 100, range_default: 10
  float timeMult;
  //@ label: "Angle[deg]", editor: range, min: 0, max: 360, range_min: 0, range_max: 360, range_default: 0
  float angle;
  //@ label: "FogStrength[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 50
  float strength;
  //@ label: "Red", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, raange_default: 255
  float colorR;
  //@ label: "Green", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, raange_default: 255
  float colorG;
  //@ label: "Blue", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, raange_default: 255
  float colorB;
};

float fo_rand(vec2 xy) {
  return fract(sin(dot(xy, vec2(5.33312, 19.0207963))) * 214758.878);
}

float fo_noise(vec2 st) {
  vec2 i = floor(st);
  vec2 f = fract(st);

  float a = fo_rand(i);
  float b = fo_rand(i + vec2(1., 0.));
  float c = fo_rand(i + vec2(0., 1.));
  float d = fo_rand(i + vec2(1., 1.));

  vec2 u = f * f * (3. - 2. * f);
  return mix(a, b, u.x) + (c - a) * u.y * (1. - u.x) + (d - b) * u.x * u.y;
}

const mat2 rot = mat2(.87758, .479426, -.479426, .87758); 

float fo_fbm(vec2 st) {
  float v = 0.;
  float a = .5;
  vec2 shift = vec2(100.);
  for (int i = 0; i < 5; ++i) {
    v += a * fo_noise(st);
    st = rot * st * 2. + shift;
    a *= .5;
  }
  return v;
}

vec4 texture(Fog s, vec2 tex_coords) {
  vec4 ret = texture(s.sampler, tex_coords);
  s.time *= s.timeMult;
	
  vec4 color = vec4(s.colorR, s.colorG, s.colorB, 1.);

  float rads = radians(s.angle);
  float sine = sin(rads);
  float cosine = cos(rads);
  mat2 rotMat = mat2(cosine, -sine, sine, cosine);
  tex_coords = rotMat * tex_coords;

  vec2 q;
  q.x = fo_fbm(tex_coords);
  q.y = fo_fbm(tex_coords + 1.);

  vec2 r;
  r.x = fo_fbm(tex_coords + q + vec2(1.7, 9.2) + .15 * s.time);
  r.y = fo_fbm(tex_coords + q + vec2(8.3, 2.8) + .126 * s.time);

  float f = fo_fbm(tex_coords + r);

  return mix(texture(s.sampler, tex_coords),mix(ret, color, (f*f*f + .6*f*f + .5*f) * s.strength), s.mix);
}
