// Author: Andreas Leeb
// Version: 1.0p

//@implements: sampler2D
struct Movement {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Time", editor: range, min: 0, max: 1000, range_min: 0, range_max: 1000, range_default: 0
  float time;
  //@ label: "Speed", editor: range, min: 0, max: 5, range_min: 0, range_max: 500, range_default: 100
  float speed;
  //@ label: "Vertical", editor: bool, bool_default: false
  bool vertical;
};

vec4 texture(Movement s, vec2 tex_coords) {
	vec2 coords = tex_coords;
	if(s.vertical) {
		tex_coords.y = fract(tex_coords.y - s.time * s.speed);
	} 
	else 
	{
    tex_coords.x = fract(tex_coords.x - s.time * s.speed);
  	}
  	if(tex_coords.x < 0. || tex_coords.y < 0. || tex_coords.x > 1. || tex_coords.y > 1.0)
    	return vec4(0.);
    return mix(texture(s.sampler, coords), texture(s.sampler, tex_coords), s.mix);
}
