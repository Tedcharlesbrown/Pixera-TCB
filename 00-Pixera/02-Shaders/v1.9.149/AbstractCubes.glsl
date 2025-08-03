// Author: Adrian Bleul

//@implements: sampler2D
struct AbstractCubes{
	sampler2D sampler;
	//@ label: "time", editor: range, min: 0, max: 50, range_min: 0, range_max: 1, range_default: 0
	float time;
	//@ label: "Spacing", editor: range, min: 0.1, max: 50.0, range_min: 0, range_max: 100, range_default: 10
	float spacing;
	//@ label: "Size", editor: range, min: 0.01, max: 0.5, range_min: 0.01, range_max: 0.5, range_default: 0.02
	float size;
	//@ label: "Wave", editor: range, min: 0.0, max: 5.0, range_min: 0, range_max: 500, range_default: 250
	float gF;
	//@ label: "Noise", editor: range, min: 0.0, max: 2.0, range_min: 0, range_max: 100, range_default: 100
	float gN;
	//@ label: "Red", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, raange_default: 200
  	float fColorR;
  	//@ label: "Green", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, raange_default: 200
  	float fColorG;
  	//@ label: "Blue", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, raange_default: 255
  	float fColorB;
	
};

float iTime;
float globalHeight;
float globalSize;
float gS;
float gFade;
float gNoise;
vec3 gCol;
float globalDis;

vec3 stepSpace(vec3 p, float s)
{
	return p-mod(p-s/2.0, s);
}

float box(vec3 p)
{
	float si = globalSize;
	vec3 boxBounds = vec3(si);
	//vec3 fp = stepSpace(p);
	//float offset = sin(fp.x*0.3+iTime*4.0)+cos(fp.z*0.3+iTime*2.0);
	
	//p.y += offset;
	vec3 di = abs(p) - boxBounds;
	//return length(p) - boxBounds.x;
  	//return min(max(distance.x,max(distance.y,distance.z)),0.0) + length(max(distance,0.0));
  	return min(max(di.x,max(di.y,di.z)),0.0) + length(max(di,0.0));
}

float random2d(vec2 st)
{
	//return 0;
	return fract(sin(dot(st.xy, vec2(12.999, 79.74367))) * (45879.878396440));
}

float noise2d(vec2 st)
{
	vec2 i = floor(st);
	vec2 f = fract(st);
	
	float a = random2d(i);
	float b = random2d(i + vec2(1.0, 0.0));
	float c = random2d(i + vec2(0.0, 1.0));
	float d = random2d(i + vec2(1.0, 1.0));
	
	vec2 u = f*f*(3.0-2.0*f);
	
	return mix(a, b,u.x) + (c - a) * u.y * (1.0 - u.x) +
			(d - b) * u.x * u.y ;
}

vec2 sim2d(vec2 p, float s)
{
	vec2 ret = p;
	ret = p + s/2.0;
	ret = fract(ret/s)*s-s/2.0;
	return ret;
}

float mapH(vec3 pos)
{
	vec3 newPos = pos;
	
	vec3 fp = stepSpace(pos, gS);
	newPos.xz= sim2d(newPos.xz, gS);
	//newPos.x -= 0.2;
	//newPos.z -= 0.2;
	
	
	// new Noise:
	
	float offset = sin(fp.x*0.3+iTime*1.0)*cos(fp.z*0.3+iTime*4.0)*sin(fp.z*0.5+iTime*4.0)*-cos(fp.x*0.7+iTime*1.0);
	float nuOffset = (offset*gFade)-(((noise2d(fp.zx)*1.0))*gNoise*1.0);
	newPos.y += nuOffset;
	
	
	// old Noise:
	/*
	float offset = sin(fp.x*0.3+iTime*1.0)+cos(fp.z*0.3+iTime*1.0);
	newPos.y += ((offset * 0.8)*gFade)-((noise2d(fp.xz)+(noise2d(fp.zx)*0.3))*gNoise*0.0);
	
	//newPos.y += offset*1;
	/*
	if(pos.x < 7.0 && pos.x > 5.0 && pos.z < 0.52 && pos.z > -0.52 )
	{
		newPos.y -= 1.8;
	}
	*/
	//newPos.y -= noise2d(pos.xz);
	return box(newPos);
}
/*
float dof(vec3 rO, vec3 rD, float tmin)
{
	float d = 0.0;
	vec3 p = vec3(0.0);
	float tmax = 10.0;
	float t = tmin - 5.0;
	//t = 0.0;
	for(t ; t < tmax;)
	{
		p = rO + rD * t;
		d = mapH(p);
		if(d < 0.001 || t > tmax)
		{
			return t;
		}
		t += d * 0.1;
	} 
	return t;
}
*/
float trace(vec3 rO, in vec3 rD)
{
	float t = 0.0;
	float d = 0.0;
	vec3 p = vec3(0.0);
	vec2 mm = vec2(0.0);
	for(int i = 0; i < 128; i++)
	{
		p = rO + rD * t; 
		d = mapH(p);
		if(d < 0.001 || t > 10)
		{ 
			return t;
		}
		t += d * globalDis;
	}
	return t;
}

mat3 setLookAt( in vec3 ro, in vec3 ta, float cr )
{
	vec3  cw = normalize(ta-ro);
	vec3  cp = vec3(sin(cr), cos(cr),0.0);
	vec3  cu = normalize( cross(cw,cp) );
	vec3  cv = normalize( cross(cu,cw) );
    return mat3( cu, cv, cw );
}

vec3 normal(in vec3 p)
{
  //tetrahedron normal
  const float n_er=0.01;
  float v1=mapH(vec3(p.x+n_er,p.y-n_er,p.z-n_er));
  float v2=mapH(vec3(p.x-n_er,p.y-n_er,p.z+n_er));
  float v3=mapH(vec3(p.x-n_er,p.y+n_er,p.z-n_er));
  float v4=mapH(vec3(p.x+n_er,p.y+n_er,p.z+n_er));
  return normalize(vec3(v4+v1-v3-v2,v3+v4-v1-v2,v2+v4-v3-v1));
}

vec3 render(in vec3 rO, in vec3 rD)
{
	vec3 outColor = vec3(0.0);
	float distance = trace(rO, rD);
	outColor = vec3(1.0 - (distance * 0.1));
	//outColor = vec3(1.0 - (dof(rO, rD, distance) * 0.1));
	return outColor;
}

vec4 texture(AbstractCubes s, vec2 tex_coords)
{
	vec2 uv = tex_coords.xy * 2.0;
	uv -= 1.0;
	uv.x *= (1920.0 / 1080.0);
	iTime = s.time;
	//iTime = 1.0;
	
	globalDis = 0.5;
	gCol = vec3(s.fColorR, s.fColorG, s.fColorB);
	
	gFade = s.gF;
	gNoise = s.gN;
	
	//globalHeight = s.height*sin(iTime);
	globalSize = s.size ;
	gS = globalSize * 2.0 * s.spacing;
	//gS = (globalSize * 2.0) + s.spacing;
	//globalSize = 0.01 * abs(sin(iTime*10));
	
	// camera	
    vec3 ro = vec3( iTime + 0.0, 2.5, 0.0 );
    vec3 ta = vec3( iTime + 5.0, 2.0, 0.0 );
    float roll = 0.0;
		        
    // camera tx
    mat3 ca = setLookAt( ro, ta, roll );
    //fisheye
    
    float r2 = uv.x*uv.x*0.32 + uv.y*uv.y;
    uv *= (7.0-sqrt(37.5-11.5*r2))/(r2+1.0);
    
    
    vec3 rd = normalize( ca * vec3(uv.xy,1.5) );
    
    vec3 coll = vec3(1.0, 0.0, 0.0);
    
    //vec3 col = render( ro, rd );
	
	return vec4(render( ro, rd )*gCol, 1.0);
}