#if defined(GPUPAD)
#version 450
vec4 texture_(sampler2D s, vec2 tc) { return texture(s, tc); }
vec4 texture_(sampler3D s, vec3 tc) { return texture(s, tc); }
#define texture texture_
#endif

//@implements: sampler2D
struct DirectionalBlur {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
	float mix;
  //@ label: "Strength", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 1
  float strength;
  //@ label: "Angle[deg]", editor: range, min: 0, max: 360, range_min: 0, range_max: 360, range_default: 0
  float angle;
  //@ label: "Samples", editor: range, min: 2, max: 100, range_min: 2, range_max: 100, range_default: 10
  float ct;
};

vec4 texture(DirectionalBlur s, vec2 tex_coords) {
  vec4 orig = texture(s.sampler, tex_coords);
  vec4 color = vec4(vec3(0.), 1.);
  
  float angleRad = radians(s.angle);
  vec2 direction = vec2(sin(angleRad), cos(angleRad)) * s.strength;
  
  float div = 0.0;
  const float delta = 2.0 / float(s.ct);
  for(float i = -1.0; i <= 1.0; i += delta)
  {
      color += texture(s.sampler, tex_coords - vec2(direction.x * i, direction.y * i));
      div += 1.0;
  }
  return mix(orig, color / div, s.mix);
}
