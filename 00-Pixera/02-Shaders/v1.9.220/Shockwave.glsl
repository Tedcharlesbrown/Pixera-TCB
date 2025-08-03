// Author: Andreas Leeb
// Version: 1.0

//@implements: sampler2D
struct Shockwave {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Time", editor: range, min: 0, max: 1000, range_min: 0, range_max: 1000, range_default: 0
  float time;
  //@ label: "TimeMultiplier", editor: range, min: 1, max: 50, range_min: 1, range_max: 50, range_default: 20
  float timeMult;
};

const vec3 shockParams = vec3(10., .8, .1);
const vec2 center = vec2(.5, .5);

vec4 texture(Shockwave s, vec2 tex_coords) {
  s.time = fract((s.time) * s.timeMult);
  s.time -= shockParams.z;
  
  vec2 coords = tex_coords;
  
  float dst = distance(tex_coords, center);
  if(dst <= (s.time + shockParams.z) &&
     dst >= (s.time - shockParams.z)) {
     float diff = dst - s.time;
     float powDiff = pow(abs(diff * shockParams.x), shockParams.y);
     float diff2 = diff * powDiff;
     vec2 diffUV = normalize(tex_coords - center);
     tex_coords += diffUV * diff2;
  }
  
  return mix(texture(s.sampler, coords), texture(s.sampler, tex_coords), s.mix);
}
