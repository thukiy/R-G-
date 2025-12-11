<|ref|>equation<|/ref|><|det|>[[117, 78, 686, 126]]<|/det|>
\[
\mathbf{A} = \mathbf{C} + \mathbf{b} = \begin{bmatrix} 2 \\ 4 \end{bmatrix} + \begin{bmatrix} -3 \\ -2.25 \end{bmatrix} = \begin{bmatrix} 2 - 3 \\ 4 - 2.25 \end{bmatrix} = \begin{bmatrix} -1 \\ 1.75 \end{bmatrix}
\]

<|ref|>text<|/ref|><|det|>[[115, 125, 150, 143]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[115, 141, 863, 194]]<|/det|>
Die Spiegelmatrix S erhalten wir durch die Überlegung, dass die Bilder der
Einheitsvektoren auch wieder senkrecht zueinander sein müssen und wenden dann
das Spaltenvektor Konstruktionsverfahren an. 

<|ref|>equation<|/ref|><|det|>[[115, 191, 866, 310]]<|/det|>
\[
S \cdot \hat{\mathbf{e}}_y = \begin{bmatrix} \sin(2\eta) \\ \cos(2\eta) \end{bmatrix} = \begin{bmatrix} 2 \sin(\eta) \cos(\eta) \\ \cos^2(\eta) - \sin^2(\eta) \end{bmatrix} = \begin{bmatrix} 2 \cdot \frac{1}{\sqrt{5}} \cdot \frac{2}{\sqrt{5}} \\ \left(\frac{2}{\sqrt{5}}\right)^2 - \left(\frac{1}{\sqrt{5}}\right)^2 \end{bmatrix} = \begin{bmatrix} \frac{4}{5} \\ \frac{4}{5} - \frac{1}{5} \end{bmatrix}
\]

<|ref|>equation<|/ref|><|det|>[[115, 317, 785, 460]]<|/det|>
\[
\begin{align*}
S \cdot \hat{\mathbf{e}}_x &= R(\pi/2) \cdot S \cdot \hat{\mathbf{e}}_y = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} \cdot \frac{1}{5} \cdot \begin{bmatrix} 4 \\ 3 \end{bmatrix} = \frac{1}{5} \cdot \begin{bmatrix} 0 \cdot 4 + (-1) \cdot 3 \\ 1 \cdot 4 + 0 \cdot 3 \end{bmatrix} \\
&= \frac{1}{5} \cdot \begin{bmatrix} -3 \\ 4 \end{bmatrix}.
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[115, 416, 750, 462]]<|/det|>
\[
S = \begin{bmatrix} S \cdot \hat{\mathbf{e}}_x & S \cdot \hat{\mathbf{e}}_y \end{bmatrix} = \begin{bmatrix} \frac{1}{5} \cdot \begin{bmatrix} -3 \\ 4 \right) & \frac{1}{5} \cdot \begin{bmatrix} 4 \\ 3 \right) \end{bmatrix} = \frac{1}{5} \cdot \begin{bmatrix} -3 & 4 \\ 4 & 3 \end{bmatrix}
\]

<|ref|>text<|/ref|><|det|>[[115, 468, 500, 488]]<|/det|>
Der Ortsvektor von A ergibt sich folglich zu 

<|ref|>equation<|/ref|><|det|>[[115, 485, 860, 583]]<|/det|>
\[
\mathbf{A} = S \cdot \mathbf{B} = \frac{1}{5} \cdot \begin{bmatrix} -3 & 1 \\ 4 & 3 \end{bmatrix} \cdot \begin{bmatrix} 2 \\ 0.25 \end{bmatrix} = \frac{1}{5} \cdot \begin{bmatrix} (-3) \cdot 2 + 4 \cdot 0.25 \\ 4 \cdot 2 + 3 \cdot 0.25 \end{bmatrix} = \frac{1}{5} \cdot \left[ \begin{array}{c} -5 \\ 8.75 \end{array} \right] \\
= \begin{bmatrix} -1 \\ 1.75 \end{bmatrix}.
\]

<|ref|>sub_title<|/ref|><|det|>[[115, 600, 494, 619]]<|/det|>
7. Orthogonale Standardmatrizen in 2D 

<|ref|>text<|/ref|><|det|>[[115, 618, 845, 656]]<|/det|>
Ermitteln Sie, welche der Standardmatrizen E, P, Z₃, Pₓ, Pᵧ, Sₓ, Sᵧ, R(π/2), R(-π/2)
und R(π/4) orthogonal sind. 

<|ref|>text<|/ref|><|det|>[[115, 672, 875, 710]]<|/det|>
Wir stellen fest, welche der Matrizen 1, P, Z₃, Pₓ, Pᵧ, Sₓ,Sᵧ, R(π/2), R(-π/2) und
R(π/4) orthogonal sind. Es gilt 

<|ref|>equation<|/ref|><|det|>[[237, 720, 755, 763]]<|/det|>
\[
\mathbb{1}^{-1} = \mathbb{1} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \quad \text{und} \quad \mathbb{1}^{T} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{ bmatrix}^{T} = \begin{bmatrix} 1 & 0 \\ 0 & 1
\end{bmatrix} = \mathbb{1},
\]

<|ref|>text<|/ref|><|det|>[[115, 770, 700, 791]]<|/det|>
somit folgt \(\mathbb{1}^{-1} = \mathbb{1}^{T}\), das heisst, die Matrix \(\mathbb{1}\) ist orthogonal. Es gilt 

<|ref|>equation<|/ref|><|det|>[[167, 799, 790, 843]]<|/det|>
\[
P^{-1} = P = \begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix} \quad \text{und} \quad P^T = \begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix}^{T} = \begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix}
\]