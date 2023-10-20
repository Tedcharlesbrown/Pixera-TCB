//@implements: sampler2D
struct RectMaskSoft{
	sampler2D sampler;
	//@ label: "Mix[%]", editor: range, min: 0, max: 100, range_min: 0, range_max: 100, range_default: 0
	float mix;
	//@ label: "Top Left X", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
	float topLx;
	//@ label: "Top Left Y", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 100
	float topLy;
	//@ label: "Top Right X", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 100
	float topRx;
	//@ label: "Top Right Y", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 100
	float topRy;
	//@ label: "Bottom Left X", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
	float bottomLx;
	//@ label: "Bottom Left Y", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
	float bottomLy;
	//@ label: "Bottom Right X", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 100
	float bottomRx;
	//@ label: "Bottom Right Y", editor: range, min: 0, max: 1, range_min: 0, range_max: 100, range_default: 0
	float bottomRy;
	//@ label: "Smoothness", editor: range, min: 0, max: 0.5, range_min: 0, range_max: 100, range_default: 10
	float Smoothness;
	//@ label: "Invert", editor: range, min:0.0, max: 1.0, range_min:0, range_max: 1, range_default: 0
	float invert;
};

mat2 rotate2d_R(float _angle){
    return mat2(cos(_angle),-sin(_angle),
                sin(_angle),cos(_angle));
}


float drawLine2(in vec2 p1, in vec2 p2, vec2 tex_coords, float offset){
    vec2 st = tex_coords;
    
    vec2 bo1;
    vec2 bo2;
     
    vec2 topPoint = (step(p2.y, p1.y)*p1) + (step(p1.y, p2.y)*p2);
    vec2 bottomPoint = (step(p2.y, p1.y)*p2) + (step(p1.y, p2.y)*p1);
    
    if(topPoint == bottomPoint){
        topPoint = p1;
        bottomPoint = p2;
    }
    
    float winkel = asin((bottomPoint.x - topPoint.x)/(distance(topPoint, bottomPoint)));
    
    
    st -= bottomPoint;
    st = vec2(rotate2d_R( winkel)*st);
    st.y += bottomPoint.y;
    
    if(topPoint == p2){
    
        bo1.x = step(-offset, st.x);
        bo1.y = step(bottomPoint.y, st.y);
        bo2.x = step(1.0, 1.0 - st.x);
    }else{
        bo1.x = step(0.0, st.x);
        bo1.y = step(bottomPoint.y, st.y);
        bo2.x = step(1.0 - offset, 1.0 - st.x);
    }
	
    st.y -= bottomPoint.y;
    st = vec2(rotate2d_R(-winkel)*st);
    st += bottomPoint;
    
    st -= topPoint;
    st = vec2(rotate2d_R( winkel)*st);
    st.y += topPoint.y;
    
    bo2.y = step(1.0 - topPoint.y, 1.0 - st.y);
    
    st.y -= topPoint.y;
    st = vec2(rotate2d_R(- winkel)*st);
    st += topPoint;
    
    return bo1.x * bo1.y * bo2.x * bo2.y;
}

float drawLine1(in vec2 p1, in vec2 p2, vec2 tex_coords, float smoothness){
    vec2 st = tex_coords;
    float smoothValue = smoothness;
    
    float correction = smoothValue * 10. * 0.0;
    
  
    
    vec2 bo1;
    vec2 bo2;
     
    vec2 topPoint = (step(p2.y, p1.y)*p1) + (step(p1.y, p2.y)*p2);
    vec2 bottomPoint = (step(p2.y, p1.y)*p2) + (step(p1.y, p2.y)*p1);
    
    if(topPoint == bottomPoint){
        topPoint = p1;
        bottomPoint = p2;
    }
    
    float winkel = asin((bottomPoint.x - topPoint.x)/(distance(topPoint, bottomPoint)));
    
    st -= bottomPoint;
    st = vec2(rotate2d_R( winkel)*st);
    st.y += bottomPoint.y;
    
    if(topPoint == p2){
       bo1.x = step(-0.0005, st.x);
    	bo1.x = smoothstep(-smoothValue, correction, st.x);
    	bo1.y = step(bottomPoint.y, st.y);
		bo2.x = step(0.9995, 1.0 - st.x);
    }else{
        bo1.x = step(-0.0005, st.x);
    	bo1.y = step(bottomPoint.y, st.y);
		bo2.x = step(0.9995, 1.0 - st.x);
        bo2.x = smoothstep(smoothValue, -correction, st.x);
    }
    
    st.y -= bottomPoint.y;
    st = vec2(rotate2d_R(-winkel)*st);
    st += bottomPoint;
    
    st -= topPoint;
    st = vec2(rotate2d_R( winkel)*st);
    st.y += topPoint.y;
    
    bo2.y = step(1.0 - topPoint.y, 1.0 - st.y);
    
    st.y -= topPoint.y;
    st = vec2(rotate2d_R(- winkel)*st);
    st += topPoint;
    
    return bo1.x * bo1.y * bo2.x * bo2.y;
}

vec4 texture(RectMaskSoft s, vec2 tex_coords) {
    vec2 st = tex_coords;
    vec4 color = texture(s.sampler, st);
    float smoothness = s.Smoothness;
    
	vec2 p1 = vec2(s.topLx,s.topLy);
    vec2 p2 = vec2(s.topRx,s.topRy);
    vec2 p3 = vec2(s.bottomRx,s.bottomRy);
    vec2 p4 = vec2(s.bottomLx,s.bottomLy);
    
    vec2 a = p1;
    
    vec2 b = p2;
    
    vec2 c = p3;
    
    vec2 d = p4;
   
    vec2 p = st;
    
    float correction = smoothness * 10. * 0.0;
    
    float radsmooth1 = smoothstep(smoothness, -correction, distance(st,p1));
    float radsmooth2 = smoothstep(smoothness, -correction, distance(st,p2));
    float radsmooth3 = smoothstep(smoothness, -correction, distance(st,p3));
    float radsmooth4 = smoothstep(smoothness, -correction, distance(st,p4));
    
    float rad = radsmooth1 + radsmooth2 + radsmooth3 + radsmooth4;
    
    float test = step(((a.y-b.y)*(p.x-a.x) + (b.x-a.x)*(p.y-a.y)), 0.);
    float test2 = step(((b.y-c.y)*(p.x-b.x) + (c.x-b.x)*(p.y-b.y)), 0.);
    float test3 = step(((c.y-d.y)*(p.x-c.x) + (d.x-c.x)*(p.y-c.y)), 0.);
    float test4 = step(((d.y-a.y)*(p.x-d.x) + (a.x-d.x)*(p.y-d.y)), 0.);
    
    float quad = test * test2 * test3 * test4;
    float box2 = drawLine2(p1, p2, tex_coords, smoothness) + drawLine2(p2, p3, tex_coords, smoothness) + drawLine2(p3, p4, tex_coords, smoothness) + drawLine2(p4, p1, tex_coords, smoothness);
    float box = drawLine1(p1, p2, tex_coords, smoothness) + drawLine1(p2, p3, tex_coords, smoothness) + drawLine1(p3, p4, tex_coords, smoothness) + drawLine1(p4, p1, tex_coords, smoothness);
    
    vec3 boxColor = vec3((1.0, 1.0, 1.0)*box);
    vec3 boxColor2 = vec3((1.0, 1.0, 1.0)*box2);
    
    float nuQuad = 1.0 - quad;
    
    vec3 col = 1.0 - vec3(boxColor2 + quad);
    vec4 Color;
    float nuCol = 1.0 - (box2 + quad);
    float cola = clamp(float(rad * nuCol) + box + quad, 0.0, 1.0);
    float colaInvert = 1.0 - cola;
    float alphaFak = mix((step(s.invert, 0.0) * cola) + (colaInvert * step(1.0, s.invert)), 1.0,(100.0 - s.mix)*0.01);
    return vec4(color.rgb, alphaFak * color.a);
}