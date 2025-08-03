//@implements: sampler2D
struct Radar {
	sampler2D sampler;
	//@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
	float mix;
	//@ label: "Direction", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
	float direction; // 0 for horizontal, 1 for vertical
	//@ label: "Position[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 50
	float position;
};

vec4 texture(Radar s, vec2 tex_coords) {
	vec2 dir;
	
	// Set direction based on the direction parameter
	if (s.direction < 0.5) {
		dir = vec2(1.0, 0.0); // Horizontal
	} else {
		dir = vec2(0.0, 1.0); // Vertical
	}
	
	// Project texture coordinates to the line direction
	float lineCoord = dot(tex_coords, dir);
	
	// Adjust position to range from left/bottom to right/top
	float adjustedPosition = s.position;
	
	// Single pixel width by rounding the projected coordinate
	float alpha = step(adjustedPosition - 0.5 / 100.0, lineCoord) - step(adjustedPosition + 0.5 / 100.0, lineCoord);
	
	vec4 color = texture(s.sampler, tex_coords);
	color.rgb = mix(color.rgb, vec3(1.0), alpha * s.mix);
	return color;
}
