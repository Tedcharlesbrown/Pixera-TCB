// Author: Andreas Leeb
// Version: 1.0

//@implements: sampler2D
struct DropShadowRect {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
  float mix;
  //@ label: "Width[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1920
  float width;
  //@ label: "Height[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1080
  float height;
  //@ label: "ShadowWidth[%]", editor: range, min: 0, max: 0.5, range_min: 0, range_max: 50, range_default: 5
  float shadowWidth;
  //@ label: "Strength[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 40
  float strength;
  //@ label: "Angle[deg]", editor: range, min: 0, max: 360, range_min: 0, range_max: 360, range_default: 225
  float angle;
};

bool isOutsideBorder(vec2 tex_coords, float width) {
  return tex_coords.x <= width || tex_coords.x > 1. - width ||
         tex_coords.y <= width || tex_coords.y > 1. - width;
}

// like built-in distance but corrected corresponding to aspect ratio
float distance2(vec2 a, vec2 b, float aspectRatio) {
  if(aspectRatio >= 1.)
    return sqrt(pow((a.x - b.x) * aspectRatio, 2.) + pow((a.y - b.y), 2.));
  return sqrt(pow((a.x - b.x), 2.) + pow((a.y - b.y) / aspectRatio, 2.));
}

// calculates the nearest point that lies on the border
vec2 nearestBorderPoint(vec2 tex_coords, float width) {
  if(tex_coords.x <= width && tex_coords.y > 1. - width) { // left top
    return vec2(width, 1. - width);
  }
  if(tex_coords.x <= width && tex_coords.y > width) { // left center
  	return vec2(width, tex_coords.y);
  }
  if(tex_coords.x <= width) { // left bottom
  	return vec2(width, width);
  }
  if(tex_coords.y <= width && tex_coords.x <= 1. - width) { // bottom center
  	return vec2(tex_coords.x, width);
  }
  if(tex_coords.y <= width) { // right bottom
  	return vec2(1. - width, width);
  }
  if(tex_coords.y <= 1. - width) { // right center
  	return vec2(1. - width, tex_coords.y);
  }
  if(tex_coords.x > 1. - width) { // right top
  	return vec2(1. - width, 1. - width);
  }
  return vec2(tex_coords.x, 1. - width); // top center
}

const float PI = 3.14159265358979;

float angleFactor(vec2 tex_coords, float width, float angle, float aspectRatio) {
  // angles greater than 90 degrees are calculated as if they were below 90 degrees and rotated
  // (e.g. 135 deg => calculate with 45 degrees and rotate everything by 90 degrees)
  float rads = radians(angle);
  if(rads > PI/2.) {
  	float rotAngle = floor(rads * 2./PI) * PI/2.;
  	rads -= rotAngle;
  	mat2 rot = mat2(cos(rotAngle), -sin(rotAngle), sin(rotAngle), cos(rotAngle));
  	tex_coords = rot * (tex_coords - .5) + .5;
  }
  if(tex_coords.y > 1. - width || tex_coords.x > 1. - width) return 0.;
  // linear functions:
  float k = tan(rads) * aspectRatio; // slope
  float d1 = width * (1. - k); // y-intercept for top
  float d2 = 1. - width - k * width; // y-intercept for bottom/left
  float d3 = width - k * (1. - width); // y-intercept for right
  float low = k * tex_coords.x + d1; // top y boundary
  float high = k * tex_coords.x + d2; // bottom y boundary
  float left = (tex_coords.y - d1) / k; // left x boundary
  float right = (tex_coords.y - d3) / k; // right x boundary
  float highDiff = abs(tex_coords.y - high);
  float lowDiff = abs(tex_coords.y - low);
  float leftDiff = abs(tex_coords.x - left);
  float rightDiff = abs(tex_coords.x - right);
  float oneSideShadow = (int(angle) % 90 == 0) ? 1. : 0.;
  float leftUpper = step(low, tex_coords.y) * step(tex_coords.y, high) // between low and high
                    - smoothstep(.025, 0., highDiff) * .4
                    - smoothstep(.025, 0., lowDiff) * .4 * oneSideShadow;
  float rightLower = step(left, tex_coords.x) * step(tex_coords.x, right) // between left and right
                     - smoothstep(.025, 0., rightDiff) * .4
                     - smoothstep(.025, 0., leftDiff) * .4 * oneSideShadow;
  return leftUpper + rightLower * step(leftUpper, 0.);
}

vec4 texture(DropShadowRect s, vec2 tex_coords) {
  vec3 shadowColor = vec3(0);
  float aspectRatio = s.width / s.height;
  float diff = s.shadowWidth - s.shadowWidth * ((aspectRatio < 1.) ? aspectRatio : (1. / aspectRatio));
  if(aspectRatio >= 1. && (tex_coords.x <= diff || tex_coords.x > 1. - diff)
     || aspectRatio < 1. && (tex_coords.y <= diff || tex_coords.y > 1. - diff))
    return mix(texture(s.sampler, tex_coords), vec4(shadowColor, 0), s.mix);
  if(isOutsideBorder(tex_coords, s.shadowWidth)) {
  	float dst = distance2(tex_coords, nearestBorderPoint(tex_coords, s.shadowWidth), aspectRatio);
  	float factor = angleFactor(tex_coords, s.shadowWidth, s.angle, aspectRatio);
  	float alpha = (1. - dst / s.shadowWidth) * s.strength * factor; // alpha value inversely proportional to distance from border
  	return mix(texture(s.sampler, tex_coords), vec4(shadowColor, alpha), s.mix);
  }
  tex_coords = (tex_coords - s.shadowWidth) / (1. - 2. * s.shadowWidth); // scaling
  return texture(s.sampler, tex_coords);
}

