// Author: Andreas Leeb
// Version: 1.0

//@implements: sampler2D
struct Rotation {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
  float mix;
  //@ label: "Angle", editor: range, min: 0, max: 360, range_min: 0, range_max: 360, range_default: 0
  float angle;
  //@ label: "Speed", editor: range, min: 0, max: 5000, range_min: 0, range_max: 5000, range_default: 1
  float speed;
};

mat2 ro_rotate(float angle) {
  float sine = sin(angle);
  float cosine = cos(angle);
  return mat2(cosine, -sine, sine, cosine);
}

vec4 texture(Rotation s, vec2 tex_coords) {
	vec2 coords = tex_coords;
  float rad = radians(s.angle) * s.speed;
  tex_coords = ro_rotate(rad) * tex_coords;
  if(tex_coords.x < 0. || tex_coords.y < 0. || tex_coords.x > 1. || tex_coords.y > 1.0)
    return mix(texture(s.sampler, tex_coords), vec4(0.), s.mix);
  return mix(texture(s.sampler, coords), texture(s.sampler, tex_coords), s.mix);
}
