<|ref|>equation<|/ref|><|det|>[[125, 80, 565, 130]]<|/det|>
\[ \underline{\nabla} f = \begin{bmatrix} f_{,1} \\ f_{,2} \end{bmatrix} = \begin{bmatrix} 2x^{2-1} \cdot y^2 + 0 \\ x^2 \cdot 2y^{2-1} + 0 \end{bmatrix} = \begin{bmatrix} 2xy^2 \\ 2x^2y \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[117, 143, 740, 193]]<|/det|>
\[ \underline{\nabla}^2 f = \begin{bmatrix} f_{,1,1} & f_{,1,2} \\ f_{,2,1} & f_{,2,2} \end{bmatrix} = \begin{bmatrix} 2 \cdot 1 \cdot y^2 & 2x \cdot 2y^{2-1} \\ 2 \cdot 2x^{2-1}y & 2x^2 \cdot 1 \end{bmatrix} = \begin{bmatrix} 2y^2 & 4xy \\ 4xy & 2x^2 \end{bmatrix} \]

<|ref|>text<|/ref|><|det|>[[115, 199, 150, 215]]<|/det|>
d) 

<|ref|>text<|/ref|><|det|>[[115, 214, 515, 232]]<|/det|>
Gradient und Hesse-Matrix ergeben sich zu 

<|ref|>equation<|/ref|><|det|>[[125, 233, 737, 280]]<|/det|>
\[ \underline{\nabla} f = \begin{bmatrix} f_{,1}\\ f_{,2} \end{bmatrix} = \ln(2) \cdot 2^{3x-5y} \begin{bmatrix} 3 \cdot 1 - 0 \\ 0 - 5 \cdot 1 \end{bmatrix} = \ln(2) \cdot 2^{3x-5} \begin{bmatrix} 3 \\ -5 \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[117, 295, 850, 389]]<|/det|>
\[ \underline{\nabla}^2 f = \begin{bmatrix} f_{,2,1} & f_{,1,2} \\ f_{,2,2} & f_{,2,2} \end{bmatrix} = \ln(2) \cdot \ln(2) \cdot 2^{3x-5y} \begin{bmatrix}\phantom{-}3 \cdot (3 \cdot 1 - 0) & 3 \cdot (0 - 5 \cdot 1) \\ -5 \cdot (3 \cdot 1 - 0) & -5 \cdot (0 - 5 \cdot 1) \end{bmatrix} = \ln^2(2) \cdot 2^{3x-5y} \begin{bmatrix} 9 & -15 \\ -15 & 25 \end{bmatrix} \]

<|ref|>text<|/ref|><|det|>[[115, 395, 150, 412]]<|/det|>
e) 

<|ref|>text<|/ref|><|det|>[[115, 411, 512, 429]]<|/det|>
Gradient und Hesse-Matrix ergeben sich zu 

<|ref|>equation<|/ref|><|det|> [[125, 429, 555, 476]]<|/det|>
\[ \underline{\nabla} V = \begin{bmatrix} V_{,1} \\ V_{,2} \end{bmatrix} = \begin{bmatrix} \pi \cdot 2r^{2-1} \cdot h \\ \pi r^2 \cdot 1 \end{bmatrix} = \begin{bmatrix} 2\pi rh \\ \pi r^2 \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[117, 492, 710, 540]]<|/det|>
\[ \underline{\nabla}^2 V = \begin{bmatrix} V_{,1,1} & V_{,1,2} \\ V_{,2,1} & V_{,2,2} \end{bmatrix} = \begin{bmatrix} 2\pi \cdot 1 \cdot h & 2\pi r \cdot 1 \\ \pi \cdot 2r^{2-1} & 0 \end{bmatrix} = \begin{bmatrix} 2\pi h & 2\pi r \\ 2\pi r & 0 \end{bmatrix} \]

<|ref|>text<|/ref|><|det|>[[115, 545, 150, 562]]<|/det|>
f) 

<|ref|>text<|/ref|><|det|>[[115, 561, 512, 579]]<|/det|>
Gradient und Hesse-Matrix ergeben sich zu 

<|ref|>equation<|/ref|><|det|>[125, 578, 790, 625]]<|/det|>
\[ \underline{\nabla} \psi = \begin{bmatrix} \psi_{,0} \\ \psi_{,1} \end{bmatrix} = A \cos(\omega t - kx) \begin{bmatrix} \omega \cdot 1 - 0 \\ 0 - k \cdot 1 \end{bmatrix} = A \cos(\omega t - kx) \begin{bmatrix} -k \\ -k \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[117, 640, 845, 687]]<|/det|>
\[ \underline{\nabla}^2 \psi = \begin{bmatrix} \psi_{,1,0} & \psi_{,0,1} \\ \psi_{,1,0} & \psi_{,1,1} \end{bmatrix} = -A \sin(\omega t - kx) \begin{bmatrix} \omega \cdot (\omega \cdot 1 - 0) & \omega \cdot (0 - k \cdot 1) \\ -k \cdot (\omega \cdot 1 - 0) & -k \cdot (0 - k \cdot 1) \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[167, 691, 500, 740]]<|/det|>
\[ = -A \sin(\omega t - kx) \begin{bmatrix} \omega^2 & -\omega k \\ -\omega k & k^2 \end{bmatrix} \]

<|ref|>text<|/ref|><|det|>[[115, 757, 142, 772]]<|/det|>
2. 

<|ref|>text<|/ref|><|det|>[[115, 771, 715, 791]]<|/det|>
Bestimmen Sie zu \(f: \mathbb{R}^2 \to \mathbb{R}\) mit \(f(x, y) = x^3 - x^2 \cdot \ln(y^2 + 1) - 3x\) 

<|ref|>text<|/ref|><|det|>[[115, 789, 465, 807]]<|/det|>
a) den Funktionswert am Punkt (-1;0), 

<|ref|>text<|/ref|><|det|>[[115, 806, 295, 823]]<|/det|>
b) den Gradienten 

<|ref|>text<|/ref|><|det|>[[115, 822, 305, 840]]<|/det|>
c) die Hesse-Matrix 

<|ref|>text<|/ref|><|det|>[[115, 839, 426, 857]]<|/det|>
d) alle Nullstellen des Gradienten 

<|ref|>text<|/ref|><|det|>[[115, 856, 600, 874]]<|/det|>
e) die Gleichung der Tangentialebene im Punkt (3;1).