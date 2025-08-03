
//@implements: sampler2D
struct MovementFreerun {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Speed Hor", editor: range, min: -10, max: 10, range_min: -100, range_max: 100, range_default: 0
  float speedH;
   //@ label: "Speed Ver", editor: range, min: -10, max: 10, range_min: -100, range_max: 100, range_default: 0
  float speedV;
};

vec4 texture(MovementFreerun s, vec2 tex_coords) {
  float time = u_sync_time;
	vec2 coords = tex_coords;
	tex_coords.x = fract(tex_coords.x - time * s.speedH);
	tex_coords.y = fract(tex_coords.y - time * s.speedV);
	
	if(tex_coords.x < 0. || tex_coords.y < 0. || tex_coords.x > 1. || tex_coords.y > 1.0)
	  return vec4(0.);
  return mix(texture(s.sampler, coords), texture(s.sampler, tex_coords), s.mix);
}
