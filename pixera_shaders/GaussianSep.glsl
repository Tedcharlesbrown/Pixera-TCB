// Author: Andreas Leeb
// Version: 1.0p

//@implements: sampler2D
struct GaussianSep {
  sampler2D sampler;
  //@ label: "Mix[%]", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
  float mix;
  //@ label: "Strength", editor: range, min: 1, max: 14, range_min: 1, range_max: 14, range_default: 1
  float strength;
  //@ label: "Horizontal", editor: range, min: 0, max: 1, range_min: 0, range_max: 1, range_default: 0
  float horizontal;
  //@ label: "Width[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1920
  float width;
  //@ label: "Height[px]", editor: range, min: 0, max: 10000, range_min: 0, range_max: 10000, range_default: 1080
  float height;
};

vec4 gs_texel(GaussianSep s, vec2 dim, vec2 abs_coords) {
  vec2 tex_coords = abs_coords * dim;
  return textureLod(s.sampler, tex_coords, 2.0);
  //return texture(s.sampler, tex_coords);
}

const float weight1[] = float[](      .25,         .5,         .0,        .0,      .0,       .0,      .0,      .0,      .0,      .0, .0);
const float weight2[] = float[](    .0625,        .25,       .375,        .0,      .0,       .0,      .0,      .0,      .0,      .0, .0);
const float weight3[] = float[](  .015625,     .09375,    .234375,     .3125,      .0,       .0,      .0,      .0,      .0,      .0, .0);
const float weight4[] = float[](  .003906,     .03125,    .109375,    .21875, .273438,       .0,      .0,      .0,      .0,      .0, .0);
const float weight5[] = float[](  .000977,    .009766,    .043945,   .117188, .205078,  .246094,      .0,      .0,      .0,      .0, .0);
const float weight6[] = float[](  .000244,    .002930,    .016113,   .053711, .120850,  .193359, .225586,      .0,      .0,      .0, .0);
const float weight7[] = float[](  .000061,    .000854,    .005554,   .022217, .061096,  .122192, .183289, .209473,      .0,      .0, .0);
const float weight8[] = float[](  .000015,    .000244,    .001831,   .008545, .027771,  .066650, .122192, .174561, .196381,      .0, .0);
const float weight9[] = float[](3.8147e-6, 6.86646e-5, 5.83649e-4, .00311279, .011673, .0326843, .070816, .121399, .166924, .185471, .0);
const float weight10[]= float[](9.5367431640625e-7, 1.9073486328125e-5, .000181198120117, .001087188720703, .004620552062988, .014785766601563, .036964416503906, .073928833007813, .120134353637695, .160179138183594, .176197052001953);
const float weight11[]= float[](5.245211241346e-6, 5.5074718034133e-5, .000367164786894, .001744032737748, .006278517855891, .017789133925025, .040660877542914, .076239145392964, .118594226166833, .154172494016883, .168188175291145);
const float weight14[]= float[](7.62774119504408e-5, .000366131577362, .001403504379888, .004411013765363, .011578911134077, .025730913631282, .048888735899436, .079999749653622, .113332978675965, .139486742985803, .149450081770503);
const float weight47[]= float[](0., 0., 0., 0., .046264675846733, .058677149854393, .071250824823192, .082849796306037, .092264545886268, .09841551561202, .100554983342716);
const float weight86[]= float[](0., 0., 0., 0., .058851256886942, .066943304708896, .074381449676552, .08073108562455, .085594404035667, .088651347036941, .089694304060905);

vec4 texture(GaussianSep s, vec2 tex_coords) {
  vec4 color = vec4(vec3(0.), 1.);
  vec2 dim = vec2(s.width, s.height);
  vec2 dimInverse = vec2(1.0) / dim;
  vec2 abs_coords = tex_coords * dim;
  
  float vertical = 1. - floor(s.horizontal);
  int maxOffset = int(s.strength);
  float[11] weight;
  switch(maxOffset) {
    case  1: weight =  weight1; break;
    case  2: weight =  weight2; break;
    case  3: weight =  weight3; break;
    case  4: weight =  weight4; break;
    case  5: weight =  weight5; break;
    case  6: weight =  weight6; break;
    case  7: weight =  weight7; break;
    case  8: weight =  weight8; break;
    case  9: weight =  weight9; break;
    case 10: weight = weight10; break;
    case 11: weight = weight11; break;
    case 12: weight = weight14; break;
    case 13: weight = weight47; break;
    case 14: weight = weight86; break;
  }
  
  maxOffset = clamp(maxOffset, 0, 10);
  
  for(int x = -maxOffset; x <= maxOffset; x++) {
    float w = weight[-abs(x) + maxOffset];
    if(w > 0.) {
      vec2 coords = abs_coords + vec2(x * s.horizontal, x * vertical);
      color += gs_texel(s, dimInverse, coords) * w;
    }
  }
  
  return mix(texture(s.sampler, tex_coords), color, s.mix);
}
