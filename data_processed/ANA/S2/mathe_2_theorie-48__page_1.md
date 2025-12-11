<|ref|>text<|/ref|><|det|>[[130, 12, 978, 80]]<|/det|>
→ ist nicht immer möglich oder es liegen mehrere Nebenbedingungen vor
dagrangesche Multiplikationsregel 

<|ref|>text<|/ref|><|det|>[[24, 108, 944, 179]]<|/det|>
Sah: Externa von \(f: D \subseteq \mathbb{R}^n \to \mathbb{R}\) unter Nebenbedingungen \(g(x_1, \ldots, x_n) = 0\)
egeben sich mit Hells dagrangeschen Multiplikator \(I\): 

<|ref|>equation<|/ref|><|det|>[[110, 186, 544, 250]]<|/det|>
\[ \nabla f(x_0) + n \nabla g(x_0) = 0 \quad n \in \mathbb{R} \]
mit \(x_0 =\) Extensstelle 

<|ref|>text<|/ref|><|det|>[[42, 283, 616, 312]]<|/det|>
→ für \(\Delta g(x_0) = 0\) keine Aussage möglich 

<|ref|>text<|/ref|><|det|>[[42, 325, 508, 351]]<|/det|>
→ die weit von \(n\) ist nicht relevant 

<|ref|>text<|/ref|><|det|>[[24, 383, 440, 412]]<|/det|>
Bsp: \(f(x, y) = -x^2 - \frac{1}{2}y^2 + 5\) 

<|ref|>equation<|/ref|><|det|>[[135, 420, 655, 450]]<|/det|>
\[ \text{Nebenbedingungen: } g(x, y) = x + y - 2 = 0 \]

<|ref|>equation<|/ref|><|det|>[[135, 455, 585, 488]]<|/det|>
\[ \nabla f(x, y) = (-2x) \quad \nabla g(x, y) = (1) \]

<|ref|>equation<|/ref|><|det|>[[135, 496, 455, 528]]<|/det|>
\[ \nabla f(x, y) + n \cdot \nabla g(x, y) = 0 \]

<|ref|>equation<|/ref|><|det|>[[155, 533, 410, 565]]<|/det|>
\[ (-2x) + n \cdot (1) = 0 \]

<|ref|>equation<|/ref|><|det|>[[135, 595, 710, 626]]<|/det|>
\[ -2x + n = 0 \quad (1) \quad -2x + n = 0 \]

<|ref|>equation<|/ref|><|det|>[[135, 633, 710, 664]]<|/det|>
\[ -y + n = 0 \quad (2) \quad -y + n = 0 \]

<|ref|>equation<|/ref|><|det|>[[145, 672, 712, 703]]<|/det|>
\[ x + y - 2 = 0 \quad (3) \quad x + y = 2 \]

<|ref|>equation<|/ref|><|det|>[[135, 730, 794, 796]]<|/det|>
\[ \text{LGS: } \begin{vmatrix} -2 & 0 & 1 \\ 0 & -1 & 1 \\ 1 & 1 & 0 \end{vmatrix} \quad \begin{vmatrix} 0 \\ 0 \\ 2 \end{vmatrix} \quad \ldots \quad x = \frac{2}{3}, \quad y = \frac{3}{4}, \quad n = \frac{4}{3} \]

<|ref|>equation<|/ref|><|det|>[[135, 825, 652, 920]]<|/det|>
\[ H(x_0) = \begin{pmatrix} -2 & -1 \\ 0 & 1 \end{pmatrix} \quad \text{det}(H) = 2 > 0 \quad \frac{\Delta^2 f}{\Delta x^2} = -2 < 0 \quad \Rightarrow \text{relatives Maximum}\]