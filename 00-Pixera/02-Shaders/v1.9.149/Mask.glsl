#if defined(GPUPAD)
#version 450
vec4 texture_(sampler2D s, vec2 tc) { return texture(s, tc); }
vec4 texture_(sampler3D s, vec3 tc) { return texture(s, tc); }
#define texture texture_
#endif

//@implements: sampler2D

struct Mask {
	sampler2D sampler;
	//@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
	float mix;
	//@ label: "Sampler", editor: sampler
	sampler2D samplerMask;
	//@ label: "RGB / Alpha", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
	float rgb_alpha;
	//@ label: "Invert", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
	float invert;
	//@ label: "Border Alpha", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
	float borderAlpha;
	//@ label: "Offset X", editor: range, min: -100, max: 100, range_min: -100, range_max: 100, range_default: 0
	float offsetX;
	//@ label: "Offset Y", editor: range, min: -100, max: 100, range_min: -100, range_max: 100, range_default: 0
	float offsetY;
	//@ label: "Rotate", editor: range, min: -360, max: 360, range_min: -360, range_max: 360, range_default: 0
	float rotZ;
	//@ label: "Aspect Ratio", editor: range, min: 0, max: 10, range_min: 0, range_max: 10, range_default: 1
	float ar;
	//@ label: "Scale X", editor: range, min: 0.01, max: 10, range_min: 0.01, range_max: 10, range_default: 1
	float scaleX;
	//@ label: "Scale Y", editor: range, min: 0, max: 10, range_min: 0, range_max: 10, range_default: 1
	float scaleY;
};

mat2 rotate(float angle) {
	float sine = sin(angle);
	float cosine = cos(angle);
	return mat2(cosine, -sine, sine, cosine);
}

vec4 texture(Mask s, vec2 tex_coords) {
	vec4 origColor = texture(s.sampler, tex_coords);
	
	mat2 matRot = rotate(radians(s.rotZ));
	vec2 center = vec2(0.5);
	vec2 uvMask = mat2(1.0/s.ar, 0, 0, 1.0) * matRot * mat2(s.ar, 0, 0, 1.0) * mat2(1./s.scaleX, 0, 0, 1./s.scaleY) * (tex_coords - center) + center + matRot * vec2(s.offsetX, s.offsetY);
		
	vec4 maskColor = texture(s.samplerMask, uvMask);
	float maskFac = abs(s.invert - mix((maskColor.r + maskColor.g + maskColor.b) / 3., maskColor.a, s.rgb_alpha));

	if(uvMask.x < 0. || uvMask.y < 0. || uvMask.x > 1. || uvMask.y > 1.0)
		maskFac = s.borderAlpha;

	origColor.a = clamp(s.mix * maskFac + (1. - s.mix) * origColor.a, 0., origColor.a);
	origColor.rgb *= origColor.a;
	
	return origColor;
}
