// Author: Adrian Bleul
uniform vec4 color3;
//@implements: sampler2D
struct Glitch{
	sampler2D sampler;
	//@ label: "Mix", editor: range, min: 0.0, max: 1.0, range_min: 0, range_max: 1.0, range_default: 0.0
	float mix;
	//@ label: "time", editor: range, min: 0, max: 50, range_min: 0, range_max: 1, range_default: 0
	float time;
	//@ label: "Wave", editor: range, min: 0.0, max: 2.0, range_min: 0.0, range_max: 2.0, range_default: 0.3
	float gF;
	//@ label: "Noise", editor: range, min: 0.0, max: 2.0, range_min: 0.0, range_max: 2.0, range_default: 1.0
	float gN;
};

vec3 mod289(vec3 x) {
  return x - floor(x * (1.0 / 289.0)) * 289.0;
}

vec2 mod289(vec2 x) {
  return x - floor(x * (1.0 / 289.0)) * 289.0;
}

vec3 permute(vec3 x) {
  return mod289(((x*34.0)+1.0)*x);
}

float snoise(vec2 v)
  {
  const vec4 C = vec4(0.211324865405187,  // (3.0-sqrt(3.0))/6.0
                      0.366025403784439,  // 0.5*(sqrt(3.0)-1.0)
                     -0.577350269189626,  // -1.0 + 2.0 * C.x
                      0.024390243902439); // 1.0 / 41.0
// First corner
  vec2 i  = floor(v + dot(v, C.yy) );
  vec2 x0 = v -   i + dot(i, C.xx);

// Other corners
  vec2 i1;
  //i1.x = step( x0.y, x0.x ); // x0.x > x0.y ? 1.0 : 0.0
  //i1.y = 1.0 - i1.x;
  i1 = (x0.x > x0.y) ? vec2(1.0, 0.0) : vec2(0.0, 1.0);
  // x0 = x0 - 0.0 + 0.0 * C.xx ;
  // x1 = x0 - i1 + 1.0 * C.xx ;
  // x2 = x0 - 1.0 + 2.0 * C.xx ;
  vec4 x12 = x0.xyxy + C.xxzz;
  x12.xy -= i1;

// Permutations
  i = mod289(i); // Avoid truncation effects in permutation
  vec3 p = permute( permute( i.y + vec3(0.0, i1.y, 1.0 ))
		+ i.x + vec3(0.0, i1.x, 1.0 ));

  vec3 m = max(0.5 - vec3(dot(x0,x0), dot(x12.xy,x12.xy), dot(x12.zw,x12.zw)), 0.0);
  m = m*m ;
  m = m*m ;

// Gradients: 41 points uniformly over a line, mapped onto a diamond.
// The ring size 17*17 = 289 is close to a multiple of 41 (41*7 = 287)

  vec3 x = 2.0 * fract(p * C.www) - 1.0;
  vec3 h = abs(x) - 0.5;
  vec3 ox = floor(x + 0.5);
  vec3 a0 = x - ox;

// Normalise gradients implicitly by scaling m
// Approximation of: m *= inversesqrt( a0*a0 + h*h );
  m *= 1.79284291400159 - 0.85373472095314 * ( a0*a0 + h*h );

// Compute final noise value at P
  vec3 g;
  g.x  = a0.x  * x0.x  + h.x  * x0.y;
  g.yz = a0.yz * x12.xz + h.yz * x12.yw;
  return 130.0 * dot(m, g);
}

float rand(vec2 co)
{
   return fract(sin(dot(co.xy,vec2(12.9898,78.233))) * 43758.5453);
}

vec4 texture(Glitch s, vec2 tex_coords)
{
	float iTime = s.time;
	
    // Create large, incidental noise waves
    float noise = max(0.0, snoise(vec2(iTime, tex_coords.y * 0.3)) - 0.3) * (1.0 / 0.7) * s.gN;
	    
    // Offset by smaller, constant noise waves
    noise = noise + (snoise(vec2(iTime*10.0, tex_coords.y * 2.4)) - 0.5) * s.gF;
    
    // Apply the noise as x displacement for every line
    float xpos = tex_coords.x - noise * noise * 0.25;
	vec4 colorOrig = texture(s.sampler, vec2(tex_coords.x, tex_coords.y));
    vec4 color = texture(s.sampler, vec2(xpos, tex_coords.y));
	
    // Mix in some random interference for lines
    color.rgb = mix(color.rgb, vec3(rand(vec2(tex_coords.y * iTime))), noise * 0.3).rgb;
    
    // Apply a line pattern every 4 pixels
    if (floor(mod(tex_coords.y * 0.25, 2.0)) == 0.0)
    {
        color.rgb *= 1.0 - (0.15 * noise);
    }
	color.g = mix(color.r, texture(s.sampler, vec2(xpos + noise * 0.05, tex_coords.y)).g, 1.0);
    color.b = mix(color.r, texture(s.sampler, vec2(xpos - noise * 0.05, tex_coords.y)).b, 1.0);
	return mix(colorOrig,color,s.mix);
}