#if defined(GPUPAD)
#version 450
vec4 texture_(sampler2D s, vec2 tc) { return texture(s, tc); }
vec4 texture_(sampler3D s, vec3 tc) { return texture(s, tc); }
#define texture texture_
#endif

//@implements: sampler2D
struct PolarCoordinates {
  sampler2D sampler;
  //@ label: "X Pos", editor: range, min: -1, max: 1, range_min: -1, range_max: 1, range_default: 0
  float xPos;
  //@ label: "Y Pos", editor: range, min: -1, max: 1, range_min: -1, range_max: 1, range_default: 0
  float yPos;
  //@ label: "X Scale", editor: range, min: 0, max: 10, range_min: 0, range_max: 10, range_default: 0.5
  float xScale;
  //@ label: "Y Scale", editor: range, min: 0, max: 10, range_min: 0, range_max: 10, range_default: 0.5
  float yScale;
  //@ label: "Rotate", editor: range, min: -1, max: 1, range_min: -1, range_max: 1, range_default: 0
  float rot;
};

vec4 texture(PolarCoordinates s, vec2 tex_coords) {
		
	vec2 scaleRec = 1. / vec2(s.xScale, s.yScale);
	mat2 scale = mat2(scaleRec.x, 0., 0., scaleRec.y);
	
	vec2 center = vec2(0.5,0.5);
	tex_coords = (scale * (tex_coords - center)) - vec2(scaleRec.x * s.xPos, scaleRec.y * s.yPos);
	
	vec2 polar = vec2(atan(tex_coords.x, tex_coords.y), length(tex_coords));
	polar.x -= 1.57079632679;
    if(polar.x < 0.0)
    {
		polar.x += 6.28318530718;
    }
    polar.x /= 6.28318530718;
    polar.x = 1.0 - polar.x;
    polar.y = 1.0 - polar.y;
    
    if(polar.x < 0.0 || polar.x > 1.0
	|| polar.y < 0.0 || polar.y > 1.0)
	{
		discard;
	}
    
    polar.x = fract(polar.x + s.rot);
    
	return texture(s.sampler, polar);
}
