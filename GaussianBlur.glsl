// Author: existical (Shadertoy) Changed by Benni M. 
// Version: 1.0

//@implements: sampler2D
struct GaussianBlur {
   sampler2D sampler;
   //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 255, range_default: 0
   float mix;
   //@ label: "Directions", editor: range, min: 0.0, max: 30.0, range_min: 0.0, range_max: 30.0, range_default: 16.0
   float Directions;
   //@ label: "Quality", editor: range, min: 0.0, max: 10.0, range_min: 0.01, range_max: 10.0, range_default: 3.0
   float Quality;
   //@ label: "Size", editor: range, min: 0.0, max: 50.0, range_min: 0.0, range_max: 50.0, range_default: 8.0
   float Size;
   //@ label: "Width[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1920
   float width;
   //@ label: "Height[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1080
   float height;
};

vec4 texture(GaussianBlur s, vec2 tex_coords) {
   float Pi = 6.28318530718; // Pi*2
	
   //GAUSSIAN BLUR SETTINGS
   float Directions = s.Directions;
   float Quality = s.Quality;
   float Size = s.Size;
   vec2 iResolution = vec2(s.width, s.height);   
	
   vec2 Radius = Size / iResolution.xy;

   // Pixel colour
   vec4 Color = texture(s.sampler, tex_coords);
   vec4 orig = Color;

    // Blur calculations
    for (float d = 0.0; d < Pi; d += Pi / Directions)
    {
        for (float i = 1.0 / Quality; i <= 1.0; i += 1.0 / Quality)
        {
            Color += texture(s.sampler, tex_coords + vec2(cos(d), sin(d)) * Radius * i);
        }
    }

    // Output to screen
    Color /= Quality * s.Directions - 15.0;

    return mix(orig, Color, s.mix);
}