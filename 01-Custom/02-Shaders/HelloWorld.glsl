//@implements: sampler2D
struct HelloWorld {
   sampler2D sampler;  // The input image/video
   //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
   float mix;
};

vec4 texture(HelloWorld s, vec2 tex_coords) {
   vec4 origColor = texture(s.sampler, tex_coords); // Sample the original color from the texture
   vec4 green = vec4(0.0, 1.0, 0.0, origColor.a);  // green color with alpha from original texture

   return mix(origColor, green, s.mix);
}
