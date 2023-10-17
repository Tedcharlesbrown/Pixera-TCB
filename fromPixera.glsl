// Author: Cody Luketic
// Color temperature (sRGB) stuff
// Copyright (C) 2014 by Benjamin 'BeRo' Rosseaux
// Because the german law knows no public domain
in the usual sense,
// this code is licensed under the CC0 license
//
http://creativecommons.org/publicdomain/zero/1.0/
const float LuminancePreservationFactor = 1.0;
const float PI2 = 6.2831853071;
// Valid from 1000 to 40000 K (and additionally 0
for pure full white)
vec3 colorTemperatureToRGB(const in float
temperature){
// Values from:
http://blenderartists.org/forum/showthread.php?
270332-OSLGoodness&p=2268693&viewfull=1#post2268693
mat3 m = (temperature <= 6500.0) ?
mat3(vec3(0.0, -2902.1955373783176,
-8257.7997278925690),
 vec3(0.0, 1669.5803561666639,
2575.2827530017594),
 vec3(1.0, 1.3302673723350029,
1.8993753891711275)) :
 mat3(vec3(1745.0425298314172,
1216.6168361476490, -8257.7997278925690),
 vec3(-2666.3474220535695,
-2173.1012343082230, 2575.2827530017594),
 vec3(0.55995389139931482,0.70381203140554553, 1.8993753891711275));
return mix(clamp(vec3(m[0] /
(vec3(clamp(temperature, 1000.0, 40000.0)) +
m[1]) + m[2]), vec3(0.0), vec3(1.0)), vec3(1.0),
smoothstep(1000.0, 0.0, temperature));
}
//@implements: sampler2D
struct ColorTemperature {
sampler2D sampler;
//@ label: "Mix[%]", editor: range, min: 0, max:
1, range_min: 0, range_max: 1, range_default: 0.5
float mix;
//@ label: "Kelvin Preset", editor: enum,
enum_default: 0, values: "No_Preset,
Candle_1800K, Sunrise_Sunset_2500K,
Tungsten_3000K, Morning_3500K, Moonlight_4000K,
Midday_5500K, Cloudy_6500K, Shade_7000K,
Clear_Sky_10000K"
 int idKelvinPreset;
//@ label: "Kelvin", editor: range, min: 1000,
max: 10000, range_min: 1000, range_max: 10000,
range_default: 1000
float kelvin;
//@ label: "Brightness[%]", editor: range, min:
0, max: 1, range_min: 0, range_max: 1,
range_default: 1
float luminancePreservationFactor;
};
vec4 texture(ColorTemperature s, vec2 tex_coords)
{
vec3 inColor = texture(s.sampler,
tex_coords).xyz;
vec3 outColor = mix(inColor, inColor *
colorTemperatureToRGB(s.kelvin), s.mix);
switch(s.idKelvinPreset) {
case 0:
 break;
case 1:
 outColor = mix(inColor, inColor *
colorTemperatureToRGB(1800.0), s.mix);
 break;
 case 2:
 outColor = mix(inColor, inColor *
colorTemperatureToRGB(2500.0), s.mix);
 break;
case 3:
 outColor = mix(inColor, inColor *
colorTemperatureToRGB(3000.0), s.mix);
 break;
case 4:
 outColor = mix(inColor, inColor *
colorTemperatureToRGB(3500.0), s.mix);
 break;
case 5:
 outColor = mix(inColor, inColor *
colorTemperatureToRGB(4000.0), s.mix);
 break;
case 6:
 outColor = mix(inColor, inColor *
colorTemperatureToRGB(5500.0), s.mix);
 break;
case 7:
 outColor = mix(inColor, inColor *
colorTemperatureToRGB(6500.0), s.mix);
 break;
case 8:
 outColor = mix(inColor, inColor *
colorTemperatureToRGB(7000.0), s.mix);
 break;
case 9:
 outColor = mix(inColor, inColor *
colorTemperatureToRGB(10000.0), s.mix);
 break;
default:
 outColor = vec3(1.0);
 break;
}
outColor *= mix(1.0, dot(inColor, vec3(0.2126,
0.7152, 0.0722)) / max(dot(outColor, vec3(0.2126,
0.7152, 0.0722)), 1e-5),
s.luminancePreservationFactor);
return vec4(outColor, 1.0);
}