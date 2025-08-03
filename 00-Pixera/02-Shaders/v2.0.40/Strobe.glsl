
//@implements: sampler2D
struct Strobe {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
  float mix;
  //@ label: "Speed", editor: range, min: 0, max: 40, range_min: 0, range_max: 100, range_default: 1
  float speed;
  //@ label: "Slope", editor: range, min: 1, max: 20, range_min: 1, range_max: 20, range_default: 1
  float slope;
  //@ label: "Red", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0, group: rgbaColorPicker, group_label: "Color"
  float red;
  //@ label: "Green", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0, group: rgbaColorPicker
  float green;
  //@ label: "Blue", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0, group: rgbaColorPicker
  float blue;
  //@ label: "Alpha", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0, group: rgbaColorPicker
  float alpha;
};

vec4 texture(Strobe s, vec2 tex_coords) {
  
  vec4 color = texture(s.sampler, tex_coords);
  float time = u_sync_time;
	
	float mixVal = sin(time * s.speed) / 2.0 * s.slope;
	
	mixVal = clamp(mixVal, -0.5, 0.5) + 0.5;
	
	vec4 strobeColor = vec4(s.red,s.green,s.blue,s.alpha); 
  return mix(color, strobeColor, s.mix * mixVal);
}
