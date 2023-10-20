# Effect Overview

## [AbstractCubes](AbstractCubes.glsl)
<img src="AbstractCubes.png" alt="AbstractCubes" width="500"/>

- Creates a field of cubes moving to time / generated noise

> Replaces content

**Variables:**

`time`
`Spacing`
`Size`
`Wave`
`Noise`
`Red`
`Green`
`Blue`
## [AbstractPlane](AbstractPlane.glsl)
<img src="AbstractPlane.png" alt="AbstractPlane" width="500"/>

- Generates a moving field according to time

> Replaces content

**Variables:**

`time`
`Foreground Red`
`Foreground Green`
`Foreground Blue`
`Background Red`
`Background Green`
`Background Blue`
## [AddColor](AddColor.glsl)
<img src="AddColor.png" alt="AddColor" width="500"/>

- Adds color layers over the current content

> 

**Variables:**

`Mix[%]`
`Red`
`Green`
`Blue`
`Alpha`
## [AlphaWipe](AlphaWipe.glsl)
<img src="AlphaWipe.png" alt="AlphaWipe" width="500"/>

- Smoothly transitions content with a directional wipe

> 

**Variables:**

`Mix[%]`
`Direction[deg]`
`Position[%]`
`Width[%]`
`Inverse`
## [BlackWhiteColor](BlackWhiteColor.glsl)
<img src="BlackWhiteColor.png" alt="BlackWhiteColor" width="500"/>

- Maps colors to a black and white spectrum

> 

**Variables:**

`Mix[%]`
`Exclude from red`
`to red`
`Exclude from green`
`to green`
`Exclude from blue`
`to blue`
## [BoxBlur](BoxBlur.glsl)
<img src="BoxBlur.png" alt="BoxBlur" width="500"/>

- Applies a box blur effect over content

> Mix% currently not in use (v1.9.149)

**Variables:**

`Mix[%]`
`Strength`
`Width[px]`
`Height[px]`
## [BoxBlurSep](BoxBlurSep.glsl)
<img src="BoxBlurSep.png" alt="BoxBlurSep" width="500"/>

- Applies a directional box blur effect

> 

**Variables:**

`Mix[%]`
`Strength`
`Horizontal`
`Width[px]`
`Height[px]`
## [BrightnessContrast](BrightnessContrast.glsl)
<img src="BrightnessContrast.png" alt="BrightnessContrast" width="500"/>

- Adjusts brightness and contrast of the content

> 

**Variables:**

`Mix[%]`
`Brightness[%]`
`Contrast[%]`
`Offset[%]`
## [Checkerboard](Checkerboard.glsl)
<img src="Checkerboard.png" alt="Checkerboard" width="500"/>

- Creates a checkerboard pattern

> 

**Variables:**

`Rows`
`Mix[%]`
`Width[px]`
`Height[px]`
`BlackColor Red`
`BlackColor Green`
`BlackColor Blue`
`BlackColor Alpha`
`WhiteColor Red`
`WhiteColor Green`
`WhiteColor Blue`
`WhiteColor Alpha`
`NonSquareAllowed`
## [ChromaKey](ChromaKey.glsl)
<img src="ChromaKey.png" alt="ChromaKey" width="500"/>

- Keys out a specific color range

> 

**Variables:**

`Mix[%]`
`Red`
`Green`
`Blue`
`HueTolerance`
`LightnessTolerance`
## [ClampColors](ClampColors.glsl)
<img src="ClampColors.png" alt="ClampColors" width="500"/>

- Clamps color values within specified ranges

> 

**Variables:**

`Mix`
`RedMin`
`RedMax`
`GreenMin`
`GreenMax`
`BlueMin`
`BlueMax`
## [ColorBorder](ColorBorder.glsl)
<img src="ColorBorder.png" alt="ColorBorder" width="500"/>

- Adds a colored border around content

> 

**Variables:**

`Mix[%]`
`Thickness`
`Color Red`
`Color Green`
`Color Blue`
`Color Alpha`
## [ColorChange](ColorChange.glsl)
<img src="ColorChange.png" alt="ColorChange" width="500"/>

- Modifies content color dynamically with time

> 

**Variables:**

`Mix[%]`
`Time`
`Speed`
## [ColorChannels](ColorChannels.glsl)
<img src="ColorChannels.png" alt="ColorChannels" width="500"/>

- Manipulates individual color channels

> 

**Variables:**

`Red`
`RedMix[%]`
`Green`
`GreenMix[%]`
`Blue`
`BlueMix[%]`
## [ColorStripes](ColorStripes.glsl)
<img src="ColorStripes.png" alt="ColorStripes" width="500"/>

- Generates colored stripes over content

> 

**Variables:**

`Mix[%]`
`Amount`
`Seed`
`Vertical`
## [Cropping](Cropping.glsl)
<img src="Cropping.png" alt="Cropping" width="500"/>

- Crops the content with adjustable edges and angle

> 

**Variables:**

`Mix[%]`
`Left`
`Left Softness[%]`
`Top`
`Top Softness[%]`
`Right`
`Right Softness[%]`
`Bottom`
`Bottom Softness[%]`
`Angle[deg]`
## [CroppingHardEdge](CroppingHardEdge.glsl)
<img src="CroppingHardEdge.png" alt="CroppingHardEdge" width="500"/>

- Crops the content with hard edges and angle

> 

**Variables:**

`Left`
`Top`
`Right`
`Bottom`
`Angle[deg]`
## [DirectionalBlur](DirectionalBlur.glsl)
<img src="DirectionalBlur.png" alt="DirectionalBlur" width="500"/>

- Blurs content in a specified direction

> 

**Variables:**

`Strength`
`Angle`
`Samples`
## [Dissolve](Dissolve.glsl)
<img src="Dissolve.png" alt="Dissolve" width="500"/>

- Dissolves the content based on strength

> 

**Variables:**

`Mix[%]`
`Strength[%]`
## [DropShadow](DropShadow.glsl)
<img src="DropShadow.png" alt="DropShadow" width="500"/>

- Applies a shadow to content

> 

**Variables:**

`Mix[%]`
`Width[px]`
`Height[px]`
`Strength`
`Performance`
`Optimize`
`Angle[deg]`
## [DropShadowRect](DropShadowRect.glsl)
<img src="DropShadowRect.png" alt="DropShadowRect" width="500"/>

- Applies a rectangular drop shadow to scaled content

> 

**Variables:**

`Mix[%]`
`Width[px]`
`Height[px]`
`ShadowWidth[%]`
`Strength[%]`
`Angle[deg]`
## [Edges](Edges.glsl)
<img src="Edges.png" alt="Edges" width="500"/>

- Detects and emphasizes edges in content

> 

**Variables:**

`Mix[%]`
`Mode`
`Width[px]`
`Height[px]`
`Edge Width[px]`
## [Flip](Flip.glsl)
<img src="Flip.png" alt="Flip" width="500"/>

- Flips the content either horizontally or vertically

> 

**Variables:**

`Mix[%]`
`Horizontal`
`Vertical`
## [FlipColors](FlipColors.glsl)
<img src="FlipColors.png" alt="FlipColors" width="500"/>

- Flips between color channels

> 

**Variables:**

`Mix[%]`
`FlipRedGreen`
`FlipRedBlue`
`FlipGreenBlue`
## [Fog](Fog.glsl)
<img src="Fog.png" alt="Fog" width="500"/>

- Creates a fog effect influenced by time

> 

**Variables:**

`Mix[%]`
`Time`
`TimeMultiplier`
`Angle[deg]`
`FogStrength[%]`
`Red`
`Green`
`Blue`
## [GainGradientCorner](GainGradientCorner.glsl)
<img src="_noeffect.png" alt="Placeholder Image" width="500"/>

- Applies a corner gradient gain

> 

**Variables:**

`Position X`
`Position Y`
`Width X`
`Width Y`
`Strength[%]`
## [Gamma](Gamma.glsl)
<img src="Gamma.png" alt="Gamma" width="500"/>

- Adjusts the gamma of content

> 

**Variables:**

`Mix[%]`
`Gamma[%]`
## [GaussianBlur](GaussianBlur.glsl)
<img src="GaussianBlur.png" alt="GaussianBlur" width="500"/>

- Applies a Gaussian blur effect

> 

**Variables:**

`Mix[%]`
`Directions`
`Quality`
`Size`
`Width[px]`
`Height[px]`
## [GaussianSep](GaussianSep.glsl)
<img src="GaussianSep.png" alt="GaussianSep" width="500"/>

- Applies a directional Gaussian blur

> 

**Variables:**

`Mix[%]`
`Strength`
`Horizontal`
`Width[px]`
`Height[px]`
## [Glitch](Glitch.glsl)
<img src="Glitch.png" alt="Glitch" width="500"/>

- Introduces a glitch effect based on time

> 

**Variables:**

`Mix`
`time`
`Wave`
`Noise`
## [Gradient](Gradient.glsl)
<img src="Gradient.png" alt="Gradient" width="500"/>

- Generates a gradient between two colors and alpha

> 

**Variables:**

`Left color Red`
`Left color Green`
`Left color Blue`
`Left color Alpha`
`Right color Red`
`Right color Green`
`Right color Blue`
`Right color Alpha`
`Position`
`Width`
`Strength[%]`
`Angle`
## [HueSaturationValue](HueSaturationValue.glsl)
<img src="HueSaturationValue.png" alt="HueSaturationValue" width="500"/>

- Adjusts hue / saturation / and value of content

> 

**Variables:**

`Mix[%]`
`Hue[deg]`
`Saturation[%]`
`Value[%]`
## [Iris](Iris.glsl)
<img src="Iris.png" alt="Iris" width="500"/>

- Creates an iris effect with customizable color

> 

**Variables:**

`Mix[%]`
`xRadius`
`yRadius`
`Smoothness`
`xPosition`
`yPosition`
`Angle[deg]`
`Color Red`
`Color Green`
`Color Blue`
`Color Alpha`
`Invert`
`Width[px]`
`Height[px]`
## [Kaleidoscope](Kaleidoscope.glsl)
<img src="Kaleidoscope.png" alt="Kaleidoscope" width="500"/>

- Generates a dynamic kaleidoscope effect

> 

**Variables:**

`Mix[%]`
`time`
`Rotation speed`
`Amount`
## [Keystoning](Keystoning.glsl)
<img src="Keystoning.png" alt="Keystoning" width="500"/>

- Adjusts content's perspective through corner manipulation

> 

**Variables:**

`LeftUpperX`
`LeftUpperY`
`RightUpperX`
`RightUpperY`
`LeftLowerX`
`LeftLowerY`
`RightLowerX`
`RightLowerY`
## [LavaLamp](LavaLamp.glsl)
<img src="LavaLamp.png" alt="LavaLamp" width="500"/>

- Simulates a lava lamp effect with multiple colors

> Mixes with content

**Variables:**

`Mix[%]`
`time`
`Foreground Red`
`Foreground Green`
`Foreground Blue`
`Midground Red`
`Midground Green`
`Midground Blue`
`Background Red`
`Background Green`
`Background Blue`
## [LedEffect](LedEffect.glsl)
<img src="LedEffect.png" alt="LedEffect" width="500"/>

- Applies an LED screen effect

> Uses hardcoded 1920x1080 aspect ratio

**Variables:**

`Mix[%]`
`Amount`
`Softness[%]`
`Gap[%]`
`Gap Red`
`Gap Green`
`Gap Blue`
`Gap Alpha`
## [LumaKey](LumaKey.glsl)
<img src="LumaKey.png" alt="LumaKey" width="500"/>

- Keys out based on luminance values

> 

**Variables:**

`Mix[%]`
`MinLuma`
`MaxLuma`
`Softness`
## [MagnifyingGlass](MagnifyingGlass.glsl)
<img src="MagnifyingGlass.png" alt="MagnifyingGlass" width="500"/>

- Zooms in on a section of content

> Fixed aspect ratio of "lens"

**Variables:**

`Mix[%]`
`Radius`
`xPosition`
`yPosition`
`Scale[%]`
## [Mask](Mask.glsl)
<img src="Mask.png" alt="Mask" width="500"/>

- Applies a mask over content with transformations

> Sampler requires external content reference

**Variables:**

`Mix[%]`
`Sampler`
`RGB / Alpha`
`Invert`
`Border Alpha`
`Offset X`
`Offset Y`
`Rotate`
`Aspect Ratio`
`Scale X`
`Scale Y`
## [MaskRGB](MaskRGB.glsl)
<img src="MaskRGB.png" alt="MaskRGB" width="500"/>

- Masks content based on RGB values

> Sampler requires external content reference

**Variables:**

`Mix[%]`
`Sampler`
## [Mirror](Mirror.glsl)
<img src="Mirror.png" alt="Mirror" width="500"/>

- Mirrors content from a specified point

> 

**Variables:**

`Mix[%]`
`MirrorPosition[%]`
`Offset`
## [Movement](Movement.glsl)
<img src="Movement.png" alt="Movement" width="500"/>

- Moves content based on time

> 

**Variables:**

`Mix[%]`
`Time`
`Speed`
`Vertical`
## [MultiplyAlpha](MultiplyAlpha.glsl)
<img src="MultiplyAlpha.png" alt="MultiplyAlpha" width="500"/>

- Multiplies content's alpha transparency

> 

**Variables:**

`Mix[%]`
`Alpha[%]`
## [MultiplyColor](MultiplyColor.glsl)
<img src="MultiplyColor.png" alt="MultiplyColor" width="500"/>

- Multiplies content with a specified color

> 

**Variables:**

`Mix[%]`
`Red`
`Green`
`Blue`
`Alpha`
## [Negative](Negative.glsl)
<img src="Negative.png" alt="Negative" width="500"/>

- Inverts the colors of content

> 

**Variables:**

`Mix`
## [Noise](Noise.glsl)
<img src="Noise.png" alt="Noise" width="500"/>

- Generates a noise pattern over content

> 

**Variables:**

`Size`
`Strength[%]`
`Time`
`Width[px]`
`Height[px]`
`BlackColor Red`
`BlackColor Green`
`BlackColor Blue`
`BlackColor Alpha`
`WhiteColor Red`
`WhiteColor Green`
`WhiteColor Blue`
`WhiteColor Alpha`
## [Opacity](Opacity.glsl)
<img src="Opacity.png" alt="Opacity" width="500"/>

- Adjusts the overall opacity of content

> 

**Variables:**

`Alpha[%]`
## [Pixelate](Pixelate.glsl)
<img src="Pixelate.png" alt="Pixelate" width="500"/>

- Pixelates the content with adjustable size

> 

**Variables:**

`Width[px]`
`Height[px]`
`Pixels`
## [PolarCoordinates](PolarCoordinates.glsl)
<img src="PolarCoordinates.png" alt="PolarCoordinates" width="500"/>

- Transforms content to polar coordinates

> 

**Variables:**

`X Pos`
`Y Pos`
`X Scale`
`Y Scale`
`Rotate`
## [RaymarchClouds](RaymarchClouds.glsl)
<img src="RaymarchClouds.png" alt="RaymarchClouds" width="500"/>

- Renders 3D clouds using raymarching

> 

**Variables:**

`Mix[%]`
`time`
`Focus`
`Treshold`
`Foreground Red`
`Foreground Green`
`Foreground Blue`
`Background Red`
`Background Green`
`Background Blue`
## [RectMaskSoft](RectMaskSoft.glsl)
<img src="RectMaskSoft.png" alt="RectMaskSoft" width="500"/>

-  Soft-edged rectangular mask with customizable corner positions

> 

**Variables:**

`Mix[%]`
`Top Left X`
`Top Left Y`
`Top Right X`
`Top Right Y`
`Bottom Left X`
`Bottom Left Y`
`Bottom Right X`
`Bottom Right Y`
`Smoothness`
`Invert`
## [ReduceColors](ReduceColors.glsl)
<img src="ReduceColors.png" alt="ReduceColors" width="500"/>

-  Reduces the number of distinct colors in the image for a posterized effect

> 

**Variables:**

`Mix[%]`
`RedValues`
`GreenValues`
`BlueValues`
## [Reflection](Reflection.glsl)
<img src="Reflection.png" alt="Reflection" width="500"/>

-  Creates a reflection effect based on position and strength

> 

**Variables:**

`Mix[%]`
`Strength`
`PositionY`
## [Relief](Relief.glsl)
<img src="Relief.png" alt="Relief" width="500"/>

-  Generates a relief effect using the specified width / height / and direction

> 

**Variables:**

`Mix[%]`
`Direction`
`Width[px]`
`Height[px]`
## [RotateCenter](RotateCenter.glsl)
<img src="RotateCenter.png" alt="RotateCenter" width="500"/>

-  Rotates the content around the center at a specified angle and speed

> 

**Variables:**

`Mix[%]`
`Angle`
`Speed`
## [Rotation](Rotation.glsl)
<img src="Rotation.png" alt="Rotation" width="500"/>

-  Rotates the content at a specified angle and speed

> 

**Variables:**

`Mix[%]`
`Angle`
`Speed`
## [Sepia](Sepia.glsl)
<img src="Sepia.png" alt="Sepia" width="500"/>

-  Applies a sepia tone to the image

> 

**Variables:**

`Mix[%]`
## [Sharpening](Sharpening.glsl)
<img src="Sharpening.png" alt="Sharpening" width="500"/>

-  Sharpens the image based on defined width / height / and strength

> 

**Variables:**

`Mix[%]`
`Width[px]`
`Height[px]`
`Strength`
## [Shockwave](Shockwave.glsl)
<img src="Shockwave.png" alt="Shockwave" width="500"/>

-  Creates a shockwave effect that animates over time"

> 

**Variables:**

`Mix[%]`
`Time`
`TimeMultiplier`
## [Solarize](Solarize.glsl)
<img src="Solarize.png" alt="Solarize" width="500"/>

-  Solarizes the image based on a threshold value

> 

**Variables:**

`Mix`
`Threshold`
`Below`
## [SolidColor](SolidColor.glsl)
<img src="SolidColor.png" alt="SolidColor" width="500"/>

-  Renders a solid color overlay with customizable RGB values

> 

**Variables:**

`Mix`
`Red`
`Green`
`Blue`
`Alpha`
## [Spill](Spill.glsl)
<img src="Spill.png" alt="Spill" width="500"/>

-  Manipulates color spill in the image with control over lightness and saturation

> 

**Variables:**

`Mix[%]`
`Red`
`Green`
`Blue`
`Lightness`
`Saturation`
`HueTolerance`
`LightnessTolerance`
## [SplitColors](SplitColors.glsl)
<img src="SplitColors.png" alt="SplitColors" width="500"/>

-  Splits RGB based on strength and angle

> 

**Variables:**

`Strength`
`Angle[deg]`
`Mix[%]`
## [Swirl](Swirl.glsl)
<img src="Swirl.png" alt="Swirl" width="500"/>

-  Applies a swirling effect to the image based on specified parameters

> 

**Variables:**

`Mix`
`PositionX`
`PositionY`
`Radius`
`Twist`
`Time`
## [Tiling](Tiling.glsl)
<img src="Tiling.png" alt="Tiling" width="500"/>

-  Repeats the image content in a tiled pattern

> 

**Variables:**

`Mix[%]`
`Factor`
## [TriGradient](TriGradient.glsl)
<img src="TriGradient.png" alt="TriGradient" width="500"/>

-  Generates a three-color gradient with customizable positions and colors

> 

**Variables:**

`Mix`
`Position1[%]`
`Position2[%]`
`Width[%]`
`Strength[%]`
`Angle[deg]`
`Color 1 Red`
`Color 1 Green`
`Color 1 Blue`
`Color 1 Alpha`
`Color 2 Red`
`Color 2 Green`
`Color 2 Blue`
`Color 2 Alpha`
`Color 3 Red`
`Color 3 Green`
`Color 3 Blue`
`Color 3 Alpha`
## [TriNoise2](TriNoise2.glsl)
<img src="TriNoise2.png" alt="TriNoise2" width="500"/>

-  Applies a triangular noise effect

> 

**Variables:**

`time`
`amount`
`Mix`
## [UVPositionAndScale](UVPositionAndScale.glsl)
<img src="_noeffect.png" alt="Placeholder Image" width="500"/>

-  Adjusts the UV coordinates of the image for positioning and scaling

> 

**Variables:**

`X Pos`
`Y Pos`
`X Scale`
`Y Scale`
## [UVPositionAndScale_Unclamped](UVPositionAndScale_Unclamped.glsl)
<img src="_noeffect.png" alt="Placeholder Image" width="500"/>

-  Unclamped version of UV positioning and scaling

> 

**Variables:**

`X Pos`
`Y Pos`
`X Scale`
`Y Scale`
## [Vignette](Vignette.glsl)
<img src="Vignette.png" alt="Vignette" width="500"/>

-  Applies a vignette effect to the image corners

> Fixed aspect ratio

**Variables:**

`Mix[%]`
`Width[%]`
## [Wipe](Wipe.glsl)
<img src="Wipe.png" alt="Wipe" width="500"/>

-  Wipes the image from a certain direction

> 

**Variables:**

`Mix[%]`
`X`
`Y`
## [Zoom](Zoom.glsl)
<img src="Zoom.png" alt="Zoom" width="500"/>

-  Zooms into the image from a specified position

> 

**Variables:**

`Mix[%]`
`xPosition`
`yPosition`
`Scale[%]`
## [DrivingPlates](DrivingPlates.glsl)
<img src="_noeffect.png" alt="Placeholder Image" width="500"/>

**Variables:**

`Sampler2`
`Sampler3`
`Sampler4`
`Sampler5`
`Sampler6`
`Sampler7`
`Sampler8`
`Sampler9`
`Position X`
`Position Y`
`Position Z`
`Rotation X`
`Rotation Y`
`Rotation Z`
`FOV`
`AspectRatio`
`Horizontal Feather`
`FOV Ceiling`
`AspectRatio Ceiling`
`Sampler`
## [Equirectangular](Equirectangular.glsl)
<img src="_noeffect.png" alt="Placeholder Image" width="500"/>

**Variables:**

`Position X`
`Position Y`
`Position Z`
`Rotation X`
`Rotation Y`
`Rotation Z`
`Sampler`
## [EquirectangularRanged](EquirectangularRanged.glsl)
<img src="_noeffect.png" alt="Placeholder Image" width="500"/>

**Variables:**

`Position X`
`Position Y`
`Position Z`
`Rotation X`
`Rotation Y`
`Rotation Z`
`Range Start`
`Range End`
`Sampler`
## [EquirectangularRangedBidirectional](EquirectangularRangedBidirectional.glsl)
<img src="_noeffect.png" alt="Placeholder Image" width="500"/>

**Variables:**

`Position X`
`Position Y`
`Position Z`
`Rotation X`
`Rotation Y`
`Rotation Z`
`Hor Range Start`
`Hor Range End`
`Ver Range Start`
`Ver Range End`
`Sampler`
## [Equirectangular_RotYXZ](Equirectangular_RotYXZ.glsl)
<img src="_noeffect.png" alt="Placeholder Image" width="500"/>

**Variables:**

`Position X`
`Position Y`
`Position Z`
`Rotation X`
`Rotation Y`
`Rotation Z`
`Sampler`
## [Perspective](Perspective.glsl)
<img src="_noeffect.png" alt="Placeholder Image" width="500"/>

**Variables:**

`Position X`
`Position Y`
`Position Z`
`Rotation X`
`Rotation Y`
`Rotation Z`
`FOV`
`AspectRatio`
`Sampler`
## [Planar](Planar.glsl)
<img src="_noeffect.png" alt="Placeholder Image" width="500"/>

**Variables:**

`Position X`
`Position Y`
`Position Z`
`Rotation X`
`Rotation Y`
`Rotation Z`
`Size`
`AspectRatio`
`Sampler`
