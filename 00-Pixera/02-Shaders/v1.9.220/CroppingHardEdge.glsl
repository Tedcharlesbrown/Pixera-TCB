#if defined(GPUPAD)
#version 450
vec4 texture_(sampler2D s, vec2 tc) { return texture(s, tc); }
vec4 texture_(sampler3D s, vec3 tc) { return texture(s, tc); }
#define texture texture_
#endif

//@implements: sampler2D
struct CroppingHardEdge {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
	float mix;
  //@ label: "Left", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float left;
  //@ label: "Top", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float top;
  //@ label: "Right", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float right;
  //@ label: "Bottom", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float bottom;
  //@ label: "Angle[deg]", editor: range, min: 0, max: 360, range_min: 0, range_max: 360, range_default: 0
  float angle;
};

vec4 texture(CroppingHardEdge s, vec2 tex_coords) {
  vec4 orig = texture(s.sampler, tex_coords);
  vec4 color = texture(s.sampler, tex_coords);
  float angle = radians(s.angle);
  float sine = sin(angle);
  float cosine = cos(angle);
  tex_coords -= vec2(0.5);
  mat2 rotMat = mat2(cosine, -sine, sine, cosine);
  tex_coords = rotMat * tex_coords;
  tex_coords += vec2(0.5);  
  
  if(tex_coords.x <= s.left){color.a = 0.;}
  if(tex_coords.y <= s.bottom){color.a = 0.;}  
  if(tex_coords.x >= (1.0 - s.right)){color.a = 0.;}  
  if(tex_coords.y >= (1.0 - s.top)){color.a = 0.;}

  return mix(orig, color, s.mix);
}
