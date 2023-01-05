#if defined(GPUPAD)
#version 450
vec4 texture_(sampler2D s,vec2 tc){return texture(s,tc);}
vec4 texture_(sampler3D s,vec3 tc){return texture(s,tc);}
#define texture texture_
// int u_render_target_id;
#endif

//@implements: sampler2D
struct Perspective{
	sampler2D sampler;
	//@ label: "Position X", editor: range, min: -100, max: 100, range_min: -100, range_max: 100, range_default: 0
	float posX;
	//@ label: "Position Y", editor: range, min: -100, max: 100, range_min: -100, range_max: 100, range_default: 0
	float posY;
	//@ label: "Position Z", editor: range, min: -100, max: 100, range_min: -100, range_max: 100, range_default: 10
	float posZ;
	//@ label: "Rotation X", editor: range, min: -360, max: 360, range_min: -360, range_max: 360, range_default: 0
	float rotX;
	//@ label: "Rotation Y", editor: range, min: -360, max: 360, range_min: -360, range_max: 360, range_default: 0
	float rotY;
	//@ label: "Rotation Z", editor: range, min: -360, max: 360, range_min: -360, range_max: 360, range_default: 0
	float rotZ;
	//@ label: "FOV", editor: range, min: 0.01, max: 180, range_min: 0.01, range_max: 180, range_default: 60
	float fov;
	//@ label: "AspectRatio", editor: range, min: 0.01, max: 100, range_min: 0.01, range_max: 100, range_default: 1
	float ar;
	//@ label: "Sampler", editor: sampler
	sampler2D samplerScreenPxlPos;
};

float get_radians(float degrees)
{
	return degrees*.01745329251994329576923690768489;
}

mat4x4 getTranslationMatrix(vec3 eyePt)
{
	mat4x4 mat;
	mat[0][0]=1.;
	mat[1][1]=1.;
	mat[2][2]=1.;
	mat[3][0]=eyePt.x;
	mat[3][1]=eyePt.y;
	mat[3][2]=eyePt.z;
	mat[3][3]=1.;
	
	return mat;
}

mat3x3 getRotationMatrix3x3(vec3 rotEuler)
{
	float c1=cos(-rotEuler.x);
	float c2=cos(-rotEuler.y);
	float c3=cos(-rotEuler.z);
	float s1=sin(-rotEuler.x);
	float s2=sin(-rotEuler.y);
	float s3=sin(-rotEuler.z);
	
	mat3x3 Result;
	Result[0][0]=c2*c3;
	Result[0][1]=-c1*s3+s1*s2*c3;
	Result[0][2]=s1*s3+c1*s2*c3;
	Result[1][0]=c2*s3;
	Result[1][1]=c1*c3+s1*s2*s3;
	Result[1][2]=-s1*c3+c1*s2*s3;
	Result[2][0]=-s2;
	Result[2][1]=s1*c2;
	Result[2][2]=c1*c2;
	return Result;
}

mat4x4 getRotationMatrix4x4(vec3 rotEuler)
{
	float c1=cos(-rotEuler.x);
	float c2=cos(-rotEuler.y);
	float c3=cos(-rotEuler.z);
	float s1=sin(-rotEuler.x);
	float s2=sin(-rotEuler.y);
	float s3=sin(-rotEuler.z);
	
	mat4x4 Result;
	Result[0][0]=c2*c3;
	Result[0][1]=-c1*s3+s1*s2*c3;
	Result[0][2]=s1*s3+c1*s2*c3;
	Result[0][3]=0;
	Result[1][0]=c2*s3;
	Result[1][1]=c1*c3+s1*s2*s3;
	Result[1][2]=-s1*c3+c1*s2*s3;
	Result[1][3]=0;
	Result[2][0]=-s2;
	Result[2][1]=s1*c2;
	Result[2][2]=c1*c2;
	Result[2][3]=0;
	Result[3][0]=0;
	Result[3][1]=0;
	Result[3][2]=0;
	Result[3][3]=0;
	return Result;
}

mat4x4 getViewMatrix(vec3 eyePt,vec3 rotEuler)
{
	return transpose(getRotationMatrix4x4(rotEuler))*getTranslationMatrix(vec3(-eyePt.x,-eyePt.y,-eyePt.z));
}

mat4x4 getPerspective(float fov,float ar,float zNear,float zFar)
{
	float tanHalfFovx=tan(fov/2.);
	
	mat4x4 Result;
	
	Result[0][0]=1./(tanHalfFovx);
	Result[1][1]=1./(tanHalfFovx/ar);
	Result[2][3]=-1.;
	
	Result[2][2]=zFar/(zNear-zFar);
	Result[3][2]=-(zFar*zNear)/(zFar-zNear);
	
	return Result;
}

vec4 texture(Perspective s,vec2 tex_coords){
	
	ivec2 texSize=textureSize(s.samplerScreenPxlPos,0);
	float ct=float(texSize.y/texSize.x);
	
	float index=u_render_target_id;
	if(ct==1){
		index=0;
	}
	
	vec2 shiftedTexCoords=tex_coords;
	float vertRange=1./ct;
	shiftedTexCoords.y=index*vertRange+(1.-tex_coords.y)*vertRange;
	
	vec4 pxlWorldPos=texture(s.samplerScreenPxlPos,shiftedTexCoords);
	pxlWorldPos.w=1.;
	
	mat4x4 matViewProj=getPerspective(get_radians(s.fov),s.ar,.1,1000.)*getViewMatrix(vec3(s.posX,s.posY,s.posZ),vec3(get_radians(s.rotX),get_radians(s.rotY),get_radians(s.rotZ)));
	
	vec4 ptProjected=matViewProj*pxlWorldPos;
	ptProjected/=ptProjected.w;
	if(ptProjected.x>1.){discard;}
	if(ptProjected.x<-1.){discard;}
	if(ptProjected.y>1.){discard;}
	if(ptProjected.y<-1.){discard;}
	
	vec2 projUV=vec2((ptProjected.x+1.)/2.,(ptProjected.y+1.)/2.);
	
	vec4 color=texture(s.sampler,projUV);
	
	return color;
}

ivec2 textureSize(Perspective s,int level){
	return ivec2(1);
}