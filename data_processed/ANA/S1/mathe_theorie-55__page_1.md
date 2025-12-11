<|ref|>text<|/ref|><|det|>[[234, 10, 838, 42]]<|/det|>
f(x) ist an x = 0 stetig und differenzierbar 

<|ref|>image<|/ref|><|det|>[[275, 52, 675, 280]]<|/det|>
 

<|ref|>sub_title<|/ref|><|det|>[[18, 302, 216, 334]]<|/det|>
Kettenregel : 

<|ref|>text<|/ref|><|det|>[[50, 342, 519, 371]]<|/det|>
g, h seien auf R differenzierbar 

<|ref|>equation<|/ref|><|det|>[[50, 379, 240, 408]]<|/det|>
\[f(x) = g(h(x))\]

<|ref|>text<|/ref|><|det|>[[50, 415, 520, 450]]<|/det|>
Es gilt: \(f'(x) = g'(h(x)) \cdot h'(x)\) 

<|ref|>text<|/ref|><|det|>[[50, 519, 965, 590]]<|/det|>
→ kann als wichtigste Ableitungsregel betrachtet werden, da viele Funktionen in wissenschaftlich und Technik zusammengesetzt sind 

<|ref|>equation<|/ref|><|det|>[[50, 611, 944, 671]]<|/det|>
\[f'(x) = \lim_{dx \to 0} \frac{dy}{dx} = \lim_{dx \to 0} \left( \frac{dy}{dx} \cdot \frac{dh}{dx} \right) = \lim_{dx \to 0} \left( \frac{dy}{dx \cdot \frac{dh}{dx}} \right) = g'(h) \cdot h'(x)\]

<|ref|>text<|/ref|><|det|>[[24, 694, 825, 725]]<|/det|>
Bsp: 
- \(f(x) = (3x - 4)^8\) 
- \(g(h) = h^8\) 
- \(g'(h) = 8h^7\) 

<|ref|>equation<|/ref|><|det|>[[500, 722, 797, 750]]<|/det|>
\[h(x) = 3x - 4 \quad h'(x) = 3\]

<|ref|>equation<|/ref|><|det|>[[184, 768, 475, 825]]<|/det|>
\[f'(x) = g'(h(x)) \cdot h'(x) = 8 \cdot (3x - 4)^7 \cdot 3\]

<|ref|>equation<|/ref|><|det|>[[500, 810, 675, 838]]<|/det|>
\[= 24(3x - 4)^7\]

<|ref|>equation<|/ref|><|det|>[[134, 864, 730, 935]]<|/det|>
\[f'(x) = \sqrt{h(x)} \quad g(h) = \sqrt{h} = h^{\frac{1}{2}}\]

<|ref|>equation<|/ref|><|det|>[[500, 904, 647, 939]]<|/det|>
\[g'(h) = \frac{1}{2\sqrt{h}}\]

<|ref|>equation<|/ref|><|det|>[[164, 940, 707, 978]]<|/det|>
\[f'(x) = \frac{1}{2\sqrt{x}} \cdot h'(x) \quad \text{Warzelegel}\]