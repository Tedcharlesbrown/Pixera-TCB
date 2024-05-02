#if defined(GPUPAD)
#version 450
vec4 texture_(sampler2D s, vec2 tc) { return texture(s, tc); }
vec4 texture_(sampler3D s, vec3 tc) { return texture(s, tc); }
#define texture texture_
// int u_render_target_id;
#endif

//@implements: sampler2D
struct EquirectangularRangedBidirectional {
	sampler2D sampler;
	//@ label: "Position X", editor: range, min: -100, max: 100, range_min: -100, range_max: 100, range_default: 0, ui_name:"Eye", ui_role:"xPos"
	float posX;
	//@ label: "Position Y", editor: range, min: -100, max: 100, range_min: -100, range_max: 100, range_default: 0, ui_name:"Eye", ui_role:"yPos"
	float posY;
	//@ label: "Position Z", editor: range, min: -100, max: 100, range_min: -100, range_max: 100, range_default: 10, ui_name:"Eye", ui_role:"zPos"
	float posZ;
	//@ label: "Rotation X", editor: range, min: -360, max: 360, range_min: -360, range_max: 360, range_default: 0, ui_name:"Eye", ui_role:"xRot"
	float rotX;
	//@ label: "Rotation Y", editor: range, min: -360, max: 360, range_min: -360, range_max: 360, range_default: 0, ui_name:"Eye", ui_role:"yRot"
	float rotY;
	//@ label: "Rotation Z", editor: range, min: -360, max: 360, range_min: -360, range_max: 360, range_default: 0, ui_name:"Eye", ui_role:"zRot"
	float rotZ;
	//@ label: "Hor Range Start", editor: range, min: 0, max: 360, range_min: 0, range_max: 360, range_default: 0
	float horRangeStart;
	//@ label: "Hor Range End", editor: range, min: 0, max: 360, range_min: 0, range_max: 360, range_default: 360
	float horRangeEnd;
	//@ label: "Ver Range Start", editor: range, min: 0, max: 180, range_min: 0, range_max: 180, range_default: 0
	float verRangeStart;
	//@ label: "Ver Range End", editor: range, min: 0, max: 180, range_min: 0, range_max: 180, range_default: 180
	float verRangeEnd;
	//@ label: "Sampler", editor: sampler
	sampler2D samplerScreenPxlPos;
};

float radians(float degrees)
{
	return degrees * 0.01745329251994329576923690768489;
}

mat3x3 getRotationMatrix3x3(vec3 rotEuler)
{
	float c1 = cos(-rotEuler.x);
    float c2 = cos(-rotEuler.y);
    float c3 = cos(-rotEuler.z);
    float s1 = sin(-rotEuler.x);
    float s2 = sin(-rotEuler.y);
    float s3 = sin(-rotEuler.z);
        
    mat3x3 Result;
    Result[0][0] = c2 * c3;
    Result[0][1] =-c1 * s3 + s1 * s2 * c3;
    Result[0][2] = s1 * s3 + c1 * s2 * c3;
    Result[1][0] = c2 * s3;
    Result[1][1] = c1 * c3 + s1 * s2 * s3;
    Result[1][2] =-s1 * c3 + c1 * s2 * s3;
    Result[2][0] =-s2;
    Result[2][1] = s1 * c2;
    Result[2][2] = c1 * c2;
    return Result;
}

#define PI 3.1415926535897932384626433832795
#define halfPI 1.5707963267948966192313216916398
vec4 texture(EquirectangularRangedBidirectional s,vec2 tex_coords) {
	
	ivec2 texSize = textureSize(s.samplerScreenPxlPos, 0);
	float ct = float(texSize.y / texSize.x);
	
	float index = u_render_target_id;
	if(ct == 1) {
		index = 0;
	}
	
	float texCoordScale = (texSize.x - 2.0)/ texSize.x;
	float vertRange = 1.0 / ct;
	float scaleShift = index * vertRange + 0.5 / ct;
	
	vec2 shiftedTexCoords;
	shiftedTexCoords.x = (tex_coords.x - 0.5) * texCoordScale + 0.5;
	shiftedTexCoords.y = ((index * vertRange + (1.0 - tex_coords.y) * vertRange) - scaleShift) * texCoordScale + scaleShift;
	
	vec3 pxlWorldPos = texture(s.samplerScreenPxlPos, shiftedTexCoords).xyz;
	vec3 normal = getRotationMatrix3x3(vec3(radians(s.rotX), radians(s.rotY), radians(s.rotZ))) * normalize(pxlWorldPos - vec3(s.posX, s.posY, s.posZ));
	
	// Calculate radial coordinates.
	float lon = atan(normal.z, normal.x);
    
    vec4 range = vec4(-PI + s.horRangeStart/180.0 * PI, -PI + s.horRangeEnd/180.0 * PI,
    s.verRangeStart/180.0 * PI, s.verRangeEnd/180.0 * PI);
    
    if(lon < range.x || lon > range.y)
    {
        discard;
    }
    float lat = acos(normal.y); // [-1,1] -> [0,PI]
    if(lat < range.z || lat > range.w)
    {
        discard;
    }
    vec2 sphereCoords = vec2(lon, lat) * (1.0 / PI);
    vec2 radialCoords = vec2((-s.horRangeStart/360.0 + (sphereCoords.x * 0.5 + 0.5)) * (360.0 / (s.horRangeEnd - s.horRangeStart)),
    1.0 - ((sphereCoords.y - s.verRangeStart/180.0) * (180.0 / (s.verRangeEnd - s.verRangeStart))));
    
	vec4 color = texture(s.sampler, radialCoords);
	return color;
}

ivec2 textureSize(EquirectangularRangedBidirectional s, int level) {
  return ivec2(1);
}
