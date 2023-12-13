// Author: Andreas Leeb
// Version: 1.0

//@implements: sampler2D
struct Edges {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Mode", editor: enum, enum_default: 0, values: "Black and White, White and Black, Minimal Black Edges, Minimal White Edges, Inverted Black Edges, Disturbace I, Gray, Gray White Edges, Black White Edges, Disturbace II"
  int mode;
  //@ label: "Width[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1920
  float width;
  //@ label: "Height[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1080
  float height;
  //@ label: "Edge Width[px]", editor: range, min: 1, max: 10, range_min: 1, range_max: 10, range_default: 1
  float edgeWidth;
};

vec2[9] ed_boxes(float offset) {
	return vec2[](vec2(-offset,  offset), vec2(0.,  offset), vec2(offset,  offset),
                  vec2(-offset,      0.), vec2(0.,      0.), vec2(offset,      0.),
                  vec2(-offset, -offset), vec2(0., -offset), vec2(offset, -offset));
}

const mat3 sx = mat3(1., 0., -1.,
                     2., 0., -2.,
                     1., 0., -1.);


const mat3 sy = mat3( 1.,  2.,  1.,
                      0.,  0.,  0.,
                     -1., -2., -1.);

vec4 ed_texel(Edges s, vec2 dim, vec2 abs_coords) {
  vec2 tex_coords = abs_coords / dim;
  return texture(s.sampler, tex_coords);
}

float ed_avg(vec3 pixel) {
  return (pixel.r + pixel.g + pixel.b) / 3.;
}

vec4 texture(Edges s, vec2 tex_coords) {
  vec4 tex = texture(s.sampler, tex_coords);
  vec4 orig = tex;
  vec3 tex_color = tex.rgb;
  float a = tex.a;
  
  vec2 dim = vec2(s.width, s.height);
  vec2 abs_coords = tex_coords * dim;
  vec2[9] vecs = ed_boxes(s.edgeWidth);
  
  mat3 I;
  for(int i = 0; i < 3; i++) {
  	for(int j = 0; j < 3; j++) {
  	  vec4 color = ed_texel(s, dim, abs_coords + vecs[i * 3 + j]);
  	  I[i][j] = ed_avg(color.rgb);
  	}
  }
  
  float gx = dot(sx[0], I[0]) + dot(sx[1], I[1]) + dot(sx[2], I[2]);
  float gy = dot(sy[0], I[0]) + dot(sy[1], I[1]) + dot(sy[2], I[2]);
  float g = sqrt(gx * gx + gy * gy);
  
  int mode = int(s.mode);
  switch(mode) {
  	case 0:
  	  return mix(orig,vec4(vec3(g), a),s.mix);
  	case 1:
  	  return mix(orig,vec4(vec3(1. - g), a),s.mix);
  	case 2:
  	  return mix(orig,vec4(tex_color - vec3(g), a),s.mix);
  	case 3:
  	  return mix(orig,vec4(tex_color + vec3(g), a),s.mix);
  	case 4:
  	  return mix(orig,vec4(tex_color * vec3(g), a),s.mix);
  	case 5:
  	  return mix(orig,vec4(tex_color / vec3(g), a),s.mix);
  	case 6:
  	  return mix(orig,vec4(ed_avg(tex_color) - vec3(g), a),s.mix);
  	case 7:
  	  return mix(orig,vec4(ed_avg(tex_color) + vec3(g), a),s.mix);
  	case 8:
  	  return mix(orig,vec4(ed_avg(tex_color) * vec3(g), a),s.mix);
  	case 9:
  	  return mix(orig,vec4(ed_avg(tex_color) / vec3(g), a),s.mix);
  }
}
