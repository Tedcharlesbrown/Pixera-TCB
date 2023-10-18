#if defined(GPUPAD)
#version 450
vec4 texture_(sampler2D s, vec2 tc) { return texture(s, tc); }
vec4 texture_(sampler3D s, vec3 tc) { return texture(s, tc); }
#define texture texture_
// int u_render_target_id;
#endif

//@implements: sampler2D
struct DrivingPlates {
	sampler2D sampler;
	//@ label: "Sampler2", editor: sampler
	sampler2D sampler2;
	//@ label: "Sampler3", editor: sampler
	sampler2D sampler3;
	//@ label: "Sampler4", editor: sampler
	sampler2D sampler4;
	//@ label: "Sampler5", editor: sampler
	sampler2D sampler5;
	//@ label: "Sampler6", editor: sampler
	sampler2D sampler6;
	//@ label: "Sampler7", editor: sampler
	sampler2D sampler7;
	//@ label: "Sampler8", editor: sampler
	sampler2D sampler8;
	//@ label: "Sampler9", editor: sampler
	sampler2D sampler9;
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
	//@ label: "FOV", editor: range, min: 0.01, max: 180, range_min: 0.01, range_max: 180, range_default: 60
	float fov;
	//@ label: "AspectRatio", editor: range, min: 0.01, max: 100, range_min: 0.01, range_max: 100, range_default: 1
	float ar;
	//@ label: "Horizontal Feather", editor: range, min: 0.0, max: 1.0, range_min: 0.0, range_max: 1, range_default: 0
	float horFeather;
	//@ label: "FOV Ceiling", editor: range, min: 0.01, max: 180, range_min: 0.01, range_max: 180, range_default: 60
	float fovCeiling;
	//@ label: "AspectRatio Ceiling", editor: range, min: 0.01, max: 100, range_min: 0.01, range_max: 100, range_default: 1
	float arCeiling;
	//@ label: "Sampler", editor: sampler
	sampler2D samplerScreenPxlPos;
};

float radians(float degrees)
{
	return degrees * 0.01745329251994329576923690768489;
}

mat4x4 getTranslationMatrix(vec3 eyePt)
{
	mat4x4 mat;
	mat[0][0] = 1.0;
	mat[1][1] = 1.0;
	mat[2][2] = 1.0;
	mat[3][0] = eyePt.x;
	mat[3][1] = eyePt.y;
	mat[3][2] = eyePt.z;
	mat[3][3] = 1.0;
	
	return mat;
}

mat4x4 getRotationMatrix4x4(vec3 rotEuler)
{
	float c1 = cos(-rotEuler.x);
    float c2 = cos(-rotEuler.y);
    float c3 = cos(-rotEuler.z);
    float s1 = sin(-rotEuler.x);
    float s2 = sin(-rotEuler.y);
    float s3 = sin(-rotEuler.z);
        
    mat4x4 Result;
    Result[0][0] = c2 * c3;
    Result[0][1] =-c1 * s3 + s1 * s2 * c3;
    Result[0][2] = s1 * s3 + c1 * s2 * c3;
    Result[0][3] = 0;
    Result[1][0] = c2 * s3;
    Result[1][1] = c1 * c3 + s1 * s2 * s3;
    Result[1][2] =-s1 * c3 + c1 * s2 * s3;
    Result[1][3] = 0;
    Result[2][0] =-s2;
    Result[2][1] = s1 * c2;
    Result[2][2] = c1 * c2;
    Result[2][3] = 0;
    Result[3][0] = 0;
    Result[3][1] = 0;
    Result[3][2] = 0;
    Result[3][3] = 1;
    return Result;
}

mat4x4 getYRotationMatrix4x4(float y)
{
	float c2 = cos(-y);
    float s2 = sin(-y);
        
    mat4x4 Result;
    Result[0][0] = c2;
    Result[0][1] = 0;
    Result[0][2] = s2;
    Result[0][3] = 0;
    Result[1][0] = 0;
    Result[1][1] = 1;
    Result[1][2] = 0;
    Result[1][3] = 0;
    Result[2][0] = -s2;
    Result[2][1] = 0;
    Result[2][2] = c2;
    Result[2][3] = 0;
    Result[3][0] = 0;
    Result[3][1] = 0;
    Result[3][2] = 0;
    Result[3][3] = 1;
    return Result;
}

mat4x4 getPerspective(float fov,float ar,float zNear,float zFar)
{
	float tanHalfFovx = tan(fov / 2.0);

	mat4x4 Result = mat4x4(1);

	Result[0][0] = 1.0 / (tanHalfFovx);
	Result[1][1] = 1.0 / (tanHalfFovx / ar);
	Result[2][3] = - 1.0;

	Result[2][2] = zFar / (zNear - zFar);
	Result[3][2] = -(zFar * zNear) / (zFar - zNear);
	Result[3][3] = 1;
	return Result;
}

const float Pi4 = 0.7853981633974483096;

float getBlendFactor(float feather,float coord)
{
	if(coord < feather)
	{
		return smoothstep(0, feather, coord);
	}
	else if(coord > (1.0 - feather))
	{
		return 1.0 - smoothstep(1.0 - feather, 1.0, coord);
	}
	return 1.0;
}

vec4 texture(DrivingPlates s,vec2 tex_coords) {
	
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
	
	vec4 pxlWorldPos = texture(s.samplerScreenPxlPos, shiftedTexCoords);
	pxlWorldPos.w = 1.0;
	
	vec4 color = vec4(0);
	vec3 eyePt = vec3(s.posX, s.posY, s.posZ);
	
	mat4x4 matTranslate = getTranslationMatrix(vec3(-s.posX, -s.posY, -s.posZ));
	mat4x4 matRotate = getRotationMatrix4x4(vec3(radians(s.rotX), radians(s.rotY), radians(s.rotZ)));
	mat4x4 matView = transpose(matRotate) * matTranslate;
	mat4x4 matProj = getPerspective(radians(s.fov), s.ar, 0.1, 1000.0);
	
	vec3 viewVec = vec3(matRotate * vec4(0.0,0.0,-1.0,0.0));
	if(dot(viewVec, vec3(pxlWorldPos.xyz)) - dot(eyePt, viewVec) > 0.0)
	{
		mat4x4 matViewProj = matProj * matView;
		vec4 ptProjected = matViewProj * pxlWorldPos;
		ptProjected /= ptProjected.w;
		if(ptProjected.x <= 1.0 && ptProjected.x >= -1.0 && ptProjected.y <= 1.0 && ptProjected.y >= -1.0)
		{
			vec2 projUV = vec2((ptProjected.x + 1.0)/2.0, (ptProjected.y + 1.0)/2.0);
			float blend = getBlendFactor(s.horFeather, projUV.x);
			color = (1-blend) * color +  blend * texture(s.sampler, projUV);
		}
	}
	
	mat4x4 matRotateComp = matRotate * getYRotationMatrix4x4(-Pi4);
	viewVec = vec3(matRotateComp * vec4(0.0,0.0,-1.0,0.0));
	if(dot(viewVec, vec3(pxlWorldPos.xyz)) - dot(eyePt, viewVec) > 0.0)
	{
		matView = transpose(matRotateComp) * matTranslate;
		mat4x4 matViewProj = matProj * matView;
		vec4 ptProjected = matViewProj * pxlWorldPos;
		ptProjected /= ptProjected.w;
		if(ptProjected.x <= 1.0 && ptProjected.x >= -1.0 && ptProjected.y <= 1.0 && ptProjected.y >= -1.0)
		{
			vec2 projUV = vec2((ptProjected.x + 1.0)/2.0, (ptProjected.y + 1.0)/2.0);
			float blend = getBlendFactor(s.horFeather, projUV.x);
			color = (1-blend) * color +  blend * texture(s.sampler2, projUV);
		}
	}
	
	matRotateComp = matRotate * getYRotationMatrix4x4(-2*Pi4);
	viewVec = vec3(matRotateComp * vec4(0.0,0.0,-1.0,0.0));
	if(dot(viewVec, vec3(pxlWorldPos.xyz)) - dot(eyePt, viewVec) > 0.0)
	{
		matView = transpose(matRotateComp) * matTranslate;
		mat4x4 matViewProj = matProj * matView;
		vec4 ptProjected = matViewProj * pxlWorldPos;
		ptProjected /= ptProjected.w;
		if(ptProjected.x <= 1.0 && ptProjected.x >= -1.0 && ptProjected.y <= 1.0 && ptProjected.y >= -1.0)
		{
			vec2 projUV = vec2((ptProjected.x + 1.0)/2.0, (ptProjected.y + 1.0)/2.0);
			float blend = getBlendFactor(s.horFeather, projUV.x);
			color = (1-blend) * color +  blend * texture(s.sampler3, projUV);
		}
	}
	
	matRotateComp = matRotate * getYRotationMatrix4x4(-3*Pi4);
	viewVec = vec3(matRotateComp * vec4(0.0,0.0,-1.0,0.0));
	if(dot(viewVec, vec3(pxlWorldPos.xyz)) - dot(eyePt, viewVec) > 0.0)
	{
		matView = transpose(matRotateComp) * matTranslate;
		mat4x4 matViewProj = matProj * matView;
		vec4 ptProjected = matViewProj * pxlWorldPos;
		ptProjected /= ptProjected.w;
		if(ptProjected.x <= 1.0 && ptProjected.x >= -1.0 && ptProjected.y <= 1.0 && ptProjected.y >= -1.0)
		{
			vec2 projUV = vec2((ptProjected.x + 1.0)/2.0, (ptProjected.y + 1.0)/2.0);
			float blend = getBlendFactor(s.horFeather, projUV.x);
			color = (1-blend) * color +  blend * texture(s.sampler4, projUV);
		}
	}
	
	matRotateComp = matRotate * getYRotationMatrix4x4(-4*Pi4);
	viewVec = vec3(matRotateComp * vec4(0.0,0.0,-1.0,0.0));
	if(dot(viewVec, vec3(pxlWorldPos.xyz)) - dot(eyePt, viewVec) > 0.0)
	{
		matView = transpose(matRotateComp) * matTranslate;
		mat4x4 matViewProj = matProj * matView;
		vec4 ptProjected = matViewProj * pxlWorldPos;
		ptProjected /= ptProjected.w;
		if(ptProjected.x <= 1.0 && ptProjected.x >= -1.0 && ptProjected.y <= 1.0 && ptProjected.y >= -1.0)
		{
			vec2 projUV = vec2((ptProjected.x + 1.0)/2.0, (ptProjected.y + 1.0)/2.0);
			float blend = getBlendFactor(s.horFeather, projUV.x);
			color = (1-blend) * color +  blend * texture(s.sampler5, projUV);
		}
	}
	
	matRotateComp = matRotate * getYRotationMatrix4x4(-5*Pi4);
	viewVec = vec3(matRotateComp * vec4(0.0,0.0,-1.0,0.0));
	if(dot(viewVec, vec3(pxlWorldPos.xyz)) - dot(eyePt, viewVec) > 0.0)
	{
		matView = transpose(matRotateComp) * matTranslate;
		mat4x4 matViewProj = matProj * matView;
		vec4 ptProjected = matViewProj * pxlWorldPos;
		ptProjected /= ptProjected.w;
		if(ptProjected.x <= 1.0 && ptProjected.x >= -1.0 && ptProjected.y <= 1.0 && ptProjected.y >= -1.0)
		{
			vec2 projUV = vec2((ptProjected.x + 1.0)/2.0, (ptProjected.y + 1.0)/2.0);
			float blend = getBlendFactor(s.horFeather, projUV.x);
			color = (1-blend) * color +  blend * texture(s.sampler6, projUV);
		}
	}
	
	matRotateComp = matRotate * getYRotationMatrix4x4(-6*Pi4);
	viewVec = vec3(matRotateComp * vec4(0.0,0.0,-1.0,0.0));
	if(dot(viewVec, vec3(pxlWorldPos.xyz)) - dot(eyePt, viewVec) > 0.0)
	{
		matView = transpose(matRotateComp) * matTranslate;
		mat4x4 matViewProj = matProj * matView;
		vec4 ptProjected = matViewProj * pxlWorldPos;
		ptProjected /= ptProjected.w;
		if(ptProjected.x <= 1.0 && ptProjected.x >= -1.0 && ptProjected.y <= 1.0 && ptProjected.y >= -1.0)
		{
			vec2 projUV = vec2((ptProjected.x + 1.0)/2.0, (ptProjected.y + 1.0)/2.0);
			float blend = getBlendFactor(s.horFeather, projUV.x);
			color = (1-blend) * color +  blend * texture(s.sampler7, projUV);
		}
	}
	
	matRotateComp = matRotate * getYRotationMatrix4x4(-7*Pi4);
	viewVec = vec3(matRotateComp * vec4(0.0,0.0,-1.0,0.0));
	if(dot(viewVec, vec3(pxlWorldPos.xyz)) - dot(eyePt, viewVec) > 0.0)
	{
		matView = transpose(matRotateComp) * matTranslate;
		mat4x4 matViewProj = matProj * matView;
		vec4 ptProjected = matViewProj * pxlWorldPos;
		ptProjected /= ptProjected.w;
		if(ptProjected.x <= 1.0 && ptProjected.x >= -1.0 && ptProjected.y <= 1.0 && ptProjected.y >= -1.0)
		{
			vec2 projUV = vec2((ptProjected.x + 1.0)/2.0, (ptProjected.y + 1.0)/2.0);
			float blend = getBlendFactor(s.horFeather, projUV.x);
			color = (1-blend) * color +  blend * texture(s.sampler8, projUV);
		}
	}
	
	matRotateComp = matRotate * getRotationMatrix4x4(vec3(1.570796326, 0.0, 0.0));
	viewVec = vec3(matRotateComp * vec4(0.0,0.0,-1.0,0.0));
	if(dot(viewVec, vec3(pxlWorldPos.xyz)) - dot(eyePt, viewVec) > 0.0)
	{
		matView = transpose(matRotateComp) * matTranslate;
		mat4x4 matViewProj = getPerspective(radians(s.fovCeiling), s.arCeiling, 0.1, 1000.0) * matView;
		vec4 ptProjected = matViewProj * pxlWorldPos;
		ptProjected /= ptProjected.w;
		if(ptProjected.x <= 1.0 && ptProjected.x >= -1.0 && ptProjected.y <= 1.0 && ptProjected.y >= -1.0)
		{
			vec2 projUV = vec2((ptProjected.x + 1.0)/2.0, (ptProjected.y + 1.0)/2.0);
			float blend = getBlendFactor(s.horFeather, projUV.x) * getBlendFactor(s.horFeather, projUV.y);
			color = (1-blend) * color +  blend * texture(s.sampler9, projUV);
		}
	}
	
	return color;
}

ivec2 textureSize(DrivingPlates s, int level) {
  return ivec2(1);
}
