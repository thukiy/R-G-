<|ref|>text<|/ref|><|det|>[[20, 13, 365, 42]]<|/det|>
Bsp: 
• \(f(x,y) = 1 + x^2 + y^2\) 

<|ref|>equation<|/ref|><|det|>[[140, 54, 430, 80]]<|/det|>
Tangentialebene in (1; 2)

<|ref|>equation<|/ref|><|det|>[[140, 90, 399, 115]]<|/det|>
\(f(1; 2) = 1 + 1 + 4 = 6\)

<|ref|>equation<|/ref|><|det|>[[140, 123, 430, 155]]<|/det|>
\(\frac{\partial f}{\partial x} = 2x\)

<|ref|>equation<|/ref|><|det|>[[140, 160, 430, 194]]<|/det|>
\(\frac{\partial f}{\partial y} = 2y\)

<|ref|>equation<|/ref|><|det|>[[140, 202, 533, 228]]<|/det|>
\[\rightarrow 2 = 6 + 2 \cdot (x-1) + 4(y-2)\]

<|ref|>equation<|/ref|><|det|>[[140, 240, 690, 266]]<|/det|>
\[= 6 + 2x - 2 + 4y - 8 = 2x + 4y - 4\]

<|ref|>text<|/ref|><|det|>[[20, 300, 440, 333]]<|/det|>
Def: \(f: \mathbb{R}^n \to \mathbb{R}\), \(\vec{x} = \left( \begin{array}{c} x_1 \\ \vdots \\ x_n \end{array} \right) \in \mathbb{R}^n\) 

<|ref|>equation<|/ref|><|det|>[[100, 344, 861, 370]]<|/det|>
\(f(\vec{x})\) ist in \(\vec{x}_0\) nach \(x_0\) partiell differenzierbar, wenn der Grenzwert

<|ref|>equation<|/ref|><|det|>[[100, 380, 732, 420]]<|/det|>
\[\lim_{h \to 0} \frac{f(x_0, x_0, \ldots, x_0 + h, \ldots, x_0) - f(\vec{x}_0)}{h} = \frac{\partial f(\vec{x}_0)}{\partial x_0} \quad \text{existiert}\]

<|ref|>text<|/ref|><|det|>[[20, 442, 891, 468]]<|/det|>
Bildung der Ableitung \(x_0\): alle anderen Variablen als Konstanten behandeln 

<|ref|>text<|/ref|><|det|>[[20, 500, 530, 528]]<|/det|>
Rechenregeln: \(f, g: \mathbb{R}^n \to \mathbb{R}\), \(a, b \in \mathbb{R}\) 

<|ref|>equation<|/ref|><|det|>[[44, 536, 614, 568]]<|/det|>
\[\cdot \frac{\partial}{\partial x_0} (a \cdot f(\vec{x}) + b \cdot g(\vec{x})) = a \cdot \frac{\partial}{\partial x_0} f(\vec{x}) + b \cdot \frac{\partial}{\partial x_0} g(\vec{x})\]

<|ref|>equation<|/ref|><|det|>[[44, 576, 600, 608]]<|/det|>
\[\cdot \frac{\partial}{\partial x_0} (f(\vec{x}) \cdot g(\vec{x})) = \frac{\partial}{\partial x_0} f(\vec{x}) \cdot g(\vec{x}) + f(\vec{x}) \cdot \frac{\partial}{\partial x_0} g(\vec{x})\]

<|ref|>text<|/ref|><|det|>[[20, 639, 565, 665]]<|/det|>
Def: Sei \(f: D \subseteq \mathbb{R}^n \to \mathbb{R}\) partiell differenzierbar. 

<|ref|>text<|/ref|><|det|>[[106, 680, 350, 702]]<|/det|>
Dann heisst der Velor 

<|ref|>equation<|/ref|><|det|>[[110, 714, 562, 825]]<|/det|>
\[\text{grad } f(\vec{x}) = \nabla f(\vec{x}) \quad \nabla : \text{ Nabla}\]

<|ref|>equation<|/ref|><|det|>[[110, 760, 764, 857]]<|/det|>
\[= \begin{pmatrix} \frac{\partial f}{\partial x_1} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{pmatrix} \quad \text{Gradient der Funktion } f(\vec{x})\]

<|ref|>text<|/ref|><|det|>[[146, 830, 763, 858]]<|/det|>
grad \(f: D \to \mathbb{R}^n\) ist eine velorformige Funktion. 

<|ref|>text<|/ref|><|det|>[[20, 884, 545, 936]]<|/det|>
Bsp: \(\nabla (x^2 + x \cdot \sin y) = \begin{pmatrix} 2x + \sin y \\ x \cdot \cos y \end{pmatrix}\)