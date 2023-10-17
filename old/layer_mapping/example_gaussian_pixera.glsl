//@implement: sampler2D
struct GaussianBlur {
    sampler2D sampler;
    float mix;
    float Directions;
    float Quality;
    float Size;
    float width;
    float height;
};

vec4 texture(GaussianBlur s, vec2 tex_coords) {
    float _Pi = 3.14;
    
    float Directions = s.Directions;
    float Quality = s.Quality;
    float Size = s.Size;
    vec2 iResolution = vec2(s.width, s.height);

    vec2 Radius = Size / iResolution.xy;

    vec4 Color = texture(s.sampler,tex_coords);
    vec4 orig = Color;

    for (float d = 0.0; d < _Pi; d += _Pi / Directions)
    {
        for (float i = 1.0 / Quality; i <= 1.0; i += 1.0 / Quality)
        {
            Color += texture(s.sampler, tex_coords + vec2(cos(d), sin(d)) * Radius * i);
        }
    }

    Color /= Quality * s.Directions - 15.0;

    return mix(orig, Color, s.mix);
}