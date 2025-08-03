// Edited by Ted Charles Brown

// #if defined(GPUPAD)
// #version 450
// vec4 texture_(sampler2D s, vec2 tc) { return texture(s, tc); }
// vec4 texture_(sampler3D s, vec3 tc) { return texture(s, tc); }
// #define texture texture_
// #endif

//@implements: sampler2D
struct UVPositionAndScale_Mix{
	sampler2D sampler;
	//@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
	float mix;
	//@ label: "X Pos", editor: range, min: -5, max: 5, range_min: -5, range_max: 5, range_default: 0
	float xPos;
	//@ label: "Y Pos", editor: range, min: -5, max: 5, range_min: -5, range_max: 5, range_default: 0
	float yPos;
	//@ label: "X Scale", editor: range, min: 0, max: 10, range_min: 0, range_max: 10, range_default: 1
	float xScale;
	//@ label: "Y Scale", editor: range, min: 0, max: 10, range_min: 0, range_max: 10, range_default: 1
	float yScale;
	//@ label: "Scale", editor: range, min: 0, max: 10, range_min: 0, range_max: 10, range_default: 1
	float xyScale;
};

vec4 texture(UVPositionAndScale_Mix s,vec2 tex_coords){
	vec4 orig = texture(s.sampler, tex_coords);
	if(s.mix == 0.){
		return orig;
	}
	
	// Adjust xScale and yScale using xyScale
	float adjustedXScale = s.xScale * s.xyScale;
	float adjustedYScale = s.yScale * s.xyScale;

	vec2 scaleRec = 1.0 / vec2(adjustedXScale, adjustedYScale);
	mat2 scale = mat2(scaleRec.x, 0., 0., scaleRec.y);

	vec2 center = vec2(0.5, 0.5);
	tex_coords = (scale * (tex_coords - center)) + center - vec2(scaleRec.x * s.xPos, scaleRec.y * s.yPos);

	if(tex_coords.x < 0. || tex_coords.x > 1. || tex_coords.y < 0. || tex_coords.y > 1.){
		discard;
	}

	return texture(s.sampler, tex_coords);
}
