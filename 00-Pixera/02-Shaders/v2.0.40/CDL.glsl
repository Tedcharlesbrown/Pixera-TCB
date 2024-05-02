// Author: 
// Version: 1.0p

//@implements: sampler2D
struct CDL {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;

  //@ label: "Red Slope", editor: range, min: -1, max: 1, range_min: -1, range_max: 1, range_default: 0, group: rgbColorChangeWheel, group_label: "Slope", partInfo: 1-3
  float redLift;
  //@ label: "Green Slope", editor: range, min: -1, max: 1, range_min: -1, range_max: 1, range_default: 0
  float greenLift;
  //@ label: "Blue Slope", editor: range, min: -1, max: 1, range_min: -1, range_max: 1, range_default: 0
  float blueLift;

  //@ label: "Red Offest", editor: range, min: -1, max: 1, range_min: -1, range_max: 1, range_default: 0, group: rgbColorChangeWheel, group_label: "Offest", partInfo: 2-3
  float redGamma;
  //@ label: "Green Offest", editor: range, min: -1, max: 1, range_min: -1, range_max: 1, range_default: 0
  float greenGamma;
  //@ label: "Blue Offest", editor: range, min: -1, max: 1, range_min: -1, range_max: 1, range_default: 0
  float blueGamma;
  
  //@ label: "Red Power", editor: range, min: 0.01, max: 16, range_min: 0.01, range_max: 16, range_default: 1, group: rgbColorChangeWheel, group_label: "Power", partInfo: 3-3
  float redGain;
  //@ label: "Green Power", editor: range, min: 0.01, max: 16, range_min: 0.01, range_max: 16, range_default: 1
  float greenGain;
  //@ label: "Blue Power", editor: range, min: 0.01, max: 16, range_min: 0.01, range_max: 16, range_default: 1
  float blueGain;
};

vec4 texture(CDL s, vec2 tex_coords) {
  vec4 orig = texture(s.sampler, tex_coords);
  vec3 inputrgb = texture(s.sampler, tex_coords).rgb;
  
  vec3 lift = vec3(s.redLift, s.greenLift, s.blueLift);
  
  s.redGamma = s.redGamma * -1;
  s.greenGamma = s.greenGamma * -1;
  s.blueGamma = s.blueGamma * -1;
  
  vec3 gamma = vec3(
  s.redGamma < 0. ? s.redGamma + 1. : (3.*s.redGamma)+1.,
  s.greenGamma < 0. ? s.greenGamma + 1. : (3.*s.greenGamma)+1.,
  s.blueGamma < 0. ? s.blueGamma + 1. : (3.*s.blueGamma)+1.
  );

  vec3 gain = vec3(s.redGain, s.greenGain, s.blueGain);
  
  vec3 lggtemp = pow((gain * inputrgb) + lift, gamma);
  vec4 lgg = vec4(lggtemp, orig.a);
  
  vec4 result = orig;
  if(s.mix != 0.)
  {
    result = mix(orig, lgg, s.mix);
    result.a = orig.a;
  }

  return result;
}
