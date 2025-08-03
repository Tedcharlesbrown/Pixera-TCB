// Author: Andreas Leeb
// Version: 1.0

//@implements: sampler2D
struct Swirl {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "PositionX", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 500
  float x;
  //@ label: "PositionY", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 500
  float y;
  //@ label: "Radius", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 500
  float radius;
  //@ label: "Twist", editor: range, min: -10, max: 10, range_min: -15, range_max: 15, range_default: 3
  float twist;
  //@ label: "Time", editor: range, min: 0, max: 1, range_min: 0, range_max: 10000, range_default: 0
  float time;
};

vec4 texture(Swirl s, vec2 tex_coords) {  
  vec2 center = vec2(s.x, s.y);
  float dist = distance(tex_coords, center);
  vec4 orig = texture(s.sampler, tex_coords);
  
  if(dist < s.radius) {
    float pct = (s.radius - dist) / s.radius;
    float angle = pct * pct * s.twist * sin(radians(s.time * 10000. + 90.));
    
    float sine = sin(angle);
    float cosine = cos(angle);
    mat2 rotMat = mat2(cosine, -sine, sine, cosine);
    tex_coords = rotMat * (tex_coords - center) + center;
  }
  
  return mix(orig,texture(s.sampler, tex_coords),s.mix);
}
