// Author: Benni M.
// Version: 1.0

//@implements: sampler2D
struct Cropping {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
  float mix;
  //@ label: "Left", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 0
  float left;
  //@ label: "Left Softness[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 0
  float left_softness;
  //@ label: "Top", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 0
  float top;
  //@ label: "Top Softness[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 0
  float top_softness;
  //@ label: "Right", editor: range, min: 0, max: 1, range_min: 0, range_max: 10000, range_default: 0
  float right;
  //@ label: "Right Softness[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 0
  float right_softness;
  //@ label: "Bottom", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 0
  float bottom;
  //@ label: "Bottom Softness[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 1000, range_default: 0
  float bottom_softness;
  //@ label: "Angle[deg]", editor: range, min: 0, max: 360, range_min: 0, range_max: 360, range_default: 0
  float angle;
};

vec4 texture(Cropping s, vec2 tex_coords) {
  vec4 color = texture(s.sampler, tex_coords);
  vec4 orig = color;
  float angle = radians(s.angle);
  float sine = sin(angle);
  float cosine = cos(angle);
  tex_coords -= vec2(0.5);
  mat2 rotMat = mat2(cosine, -sine, sine, cosine);
  tex_coords = rotMat * tex_coords;
  tex_coords += vec2(0.5);  
  float color_left = 1; // color.a;
  float color_bottom = 1; // color.a;
  float color_right = 1; // color.a;
  float color_top = 1; // color.a;
  if(tex_coords.x > s.left && tex_coords.x < s.left + s.left_softness)
  {
	color_left = smoothstep(s.left, s.left + s.left_softness, tex_coords.x);
  }
  if(tex_coords.y > s.bottom && tex_coords.y < s.bottom + s.bottom_softness)
  {
	color_bottom = smoothstep(s.bottom, s.bottom + s.bottom_softness, tex_coords.y);
  }
  if(tex_coords.x < 1.0 - s.right && tex_coords.x > 1.0 - (s.right + s.right_softness))
  {
	color_right = smoothstep(1.0 - s.right, 1.0 - (s.right + s.right_softness), tex_coords.x);
  }
  if(tex_coords.y < 1.0 - s.top && tex_coords.y > 1.0 - (s.top + s.top_softness))
  {
	color_top = smoothstep(1.0 - s.top, 1.0 - (s.top + s.top_softness), tex_coords.y);
  }
  
  color.a *= (color_left * color_right * color_top * color_bottom);
 
  if(tex_coords.x <= s.left){color.a = 0;}
  if(tex_coords.y <= s.bottom){color.a = 0;}  
  if(tex_coords.x >= (1.0 - s.right)){color.a = 0;}  
  if(tex_coords.y >= (1.0 - s.top)){color.a = 0;}

  return mix(orig,color,s.mix);
}
