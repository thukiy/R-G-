<|ref|>title<|/ref|><|det|>[[115, 183, 500, 216]]<|/det|>
# Übungsblatt 10 Ana 

<|ref|>text<|/ref|><|det|>[[576, 196, 879, 231]]<|/det|>
Computational and Data Science
FS2024 

<|ref|>text<|/ref|><|det|>[[115, 250, 270, 277]]<|/det|>
## Lösungen 

<|ref|>text<|/ref|><|det|>[[750, 258, 880, 275]]<|/det|>
Mathematik 2 

<|ref|>text<|/ref|><|det|>[[115, 303, 210, 320]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 320, 808, 370]]<|/det|>
- Sie kennen die Begriffe Hesse-Matrix, Richtungsableitung, lokale/globale Extrema, Sattelpunkt, Extrema unter Nebenbedingungen, Lagrange´scher Multiplikator und deren wichtigste Eigenschaften. 

<|ref|>text<|/ref|><|det|>[[115, 369, 680, 387]]<|/det|>
- Sie können die Hesse-Matrix von Skalarfeldern bestimmen. 

<|ref|>text<|/ref|><|det|>[[115, 386, 567, 404]]<|/det|>
- Sie können die Richtungsableitung berechnen. 

<|ref|>text<|/ref|><|det|>[[115, 403, 660, 420]]<|/det|>
- Sie können lokale Extrema und Sattelpunkte bestimmen. 

<|ref|>text<|/ref|><|det|>[[115, 419, 805, 437]]<|/det|>
- Sie können Extrema einer Funktion unter Nebenbedingungen bestimmen. 

<|ref|>sub_title<|/ref|><|det|>[[115, 467, 585, 485]]<|/det|>
### 1. Ableitungen von Funktionen in zwei Variablen 

<|ref|>text<|/ref|><|det|>[[115, 485, 800, 518]]<|/det|>
Berechnen Sie jeweils den Gradienten und die Hesse-Matrix der gegebenen Funktion. 

<|ref|>equation<|/ref|><|det|>[[115, 517, 870, 556]]<|/det|>
\[ 
\begin{align*} 
a) \ f(x, y) &= 3x + 5y \quad & b) \ f(x, y) &= x^2 + 2xy - 3y^2 \quad & c) \ f(x, y) &= x^2y^2 + 1 \quad \\
d) \ f(x, y) &= 2^{3x-5y} \quad & e) \ V(r, h) &= \pi r^2h \quad & f) \ \psi(t, x) &= A \sin(\omega t - kx) 
\end{align*} 
\]

<|ref|>text<|/ref|><|det|>[[115, 569, 145, 585]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[115, 585, 510, 602]]<|/det|>
Gradient und Hesse-Matrix ergeben sich zu 

<|ref|>equation<|/ref|><|det|>[[125, 606, 485, 653]]<|/det|>
\[ \nabla f = \begin{bmatrix} f_{,1} \\ f_{,2} \end{bmatrix} = \begin{bmatrix} 3 \cdot 1 + 0 \\ 0 + 5 \cdot 1 \end{bmatrix} = \begin{bmatrix} 3 \\ 5 \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[115, 668, 435, 714]]<|/det|>
\[ \nabla^2 f = \begin{bmatrix} f_{,1,1} & f_{,1,2} \\ f_{,2,1} & f_{,2,2} \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} \]

<|ref|>text<|/ref|><|det|>[[115, 720, 145, 737]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[115, 736, 510, 753]]<|/det|>
Gradient und Hesse-Matrix ergeben sich zu 

<|ref|>equation<|/ref|><|det|>[0.5, 0.5] 

<|ref|>equation<|/ref|><|det|>[[125, 755, 660, 801]]<|/det|>
\[ \nabla f = \begin{bmatrix} f_{,1} & f_{,1,2} \\ f_{,2} & f_{,2,2} \end{bmatrix} = \begin{bmatrix} 2x^{2-1} + 2 \cdot 1 \cdot y - 0 \\ 0 + 2x \cdot 1 - 3 \cdot 2y^{2-1} \end{bmatrix} = \begin{bmatrix} 2x + 2y \\ 2x - 6y \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[115, 817, 686, 863]]<|/det|>
\[ \nabla^2 f = \begin{bmatrix} f_{,1,2} & f_{,1,2} \\ f_{,2,2} & f_{,2,2} \end{bmatrix} = \begin{bmatrix}\begin{array}{cc} 2 \cdot 1 + 0 & 0 + 2 \cdot 1 \\ 2 \cdot 1 - 0 & 0 - 6 \cdot 1 \end{array}\end{bmatrix} = \begin{bmatrix} 2 & 2 \\ 2 & -6 \end{bmatrix} \]

<|ref|>text<|/ref|><|det|>[[115, 869, 145, 885]]<|/det|>
c) 

<|ref|>text<|/ref|><|det|>[[115, 885, 510, 902]]<|/det|>
Gradient und Hesse-Matrix ergeben sich zu