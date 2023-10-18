//@implements: sampler2D
struct GainGradientCorner {
  sampler2D sampler;
  //@ label: "Position X", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
  float positionX;
  //@ label: "Position Y", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
  float positionY;
  //@ label: "Width X", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 1
  float widthX;
  //@ label: "Width Y", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 1
  float widthY;
  //@ label: "Strength[%]", editor: range, min: 0, max: 10, range_min: 0, range_max: 10, range_default: 1
  float strength;
};

vec4 texture(GainGradientCorner s, vec2 tex_coords) {
  vec4 color = texture(s.sampler, tex_coords);
   
  vec2 uv = vec2(0,0);
  if(tex_coords.x >= (s.positionX - s.widthX) && tex_coords.x <= (s.positionX + s.widthX)
  	&& tex_coords.y >= (s.positionY - s.widthY) && tex_coords.y <= (s.positionY + s.widthY))
  {
  	uv.x = 1.0 - abs(tex_coords.x - s.positionX) / s.widthX;
  	uv.y = 1.0 - abs(tex_coords.y - s.positionY) / s.widthY;
  }
  
  color.xyz += uv.x*uv.x*uv.y*uv.y * s.strength;
  
  return color;
}
