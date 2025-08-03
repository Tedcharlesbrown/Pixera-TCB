// Author: Dr. Stephan Lindebaum
// Version: 1.1

//@implements: sampler2D

struct MaskRGB {
	sampler2D sampler;
	//@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
	float mix;
	//@ label: "Sampler", editor: sampler
	sampler2D samplerMask;
};

vec4 texture(MaskRGB s, vec2 tex_coords) {
	vec4 origColor = texture(s.sampler, tex_coords);
	vec4 maskColor = texture(s.samplerMask, tex_coords);
	maskColor.a = origColor.a;
	float maskFac = (maskColor.r + maskColor.g + maskColor.b) / 3.;
	origColor.a = clamp(s.mix * maskFac + (1. - s.mix) * origColor.a, 0., origColor.a);
	origColor.rgb *= origColor.a;
	return origColor;
}