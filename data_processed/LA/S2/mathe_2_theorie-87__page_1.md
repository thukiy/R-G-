<|ref|>sub_title<|/ref|><|det|>[[25, 12, 203, 40]]<|/det|>
## Rechenregeln : 

<|ref|>text<|/ref|><|det|>[[45, 50, 285, 78]]<|/det|>
- det(A) = det(Aᵀ) 

<|ref|>text<|/ref|><|det|>[[45, 90, 338, 117]]<|/det|>
- det(λ·A) = λⁿ det(A) 

<|ref|>text<|/ref|><|det|>[[45, 129, 755, 156]]<|/det|>
- det(A·B) = det(A)·det(B) = det(B)·det(A) = det(B·A) 

<|ref|>text<|/ref|><|det|>[[45, 165, 280, 197]]<|/det|>
- det(A⁻¹) = \(\frac{1}{\text{det}(A)}\) 

<|ref|>text<|/ref|><|det|>[[45, 206, 916, 234]]<|/det|>
- es gibt keine Summenformel : det(A+B) ≠ det(A) + det(B) oftmals 

<|ref|>sub_title<|/ref|><|det|>[[25, 266, 504, 293]]<|/det|>
## Modifikationsregeln für Determinanten : 

<|ref|>text<|/ref|><|det|>[[55, 305, 380, 331]]<|/det|>
A sei n×n Matrix, λ ∈ ℝ 

<|ref|>text<|/ref|><|det|>[[55, 344, 512, 370]]<|/det|>
a) deßentausch : det(A) → - det(A) 

<|ref|>text<|/ref|><|det|>[[55, 383, 550, 409]]<|/det|>
b) Spaltenausch : det(A) → - det(A) 

<|ref|>text<|/ref|><|det|>[[55, 421, 808, 448]]<|/det|>
c) Multiplikation einer Zeile mit λ : det(A) → λ·det(A) 

<|ref|>text<|/ref|><|det|>[[55, 459, 808, 486]]<|/det|>
d) " " " Spalte mit λ : det(A) → λ·det(A) 

<|ref|>text<|/ref|><|det|>[[550, 500, 969, 565]]<|/det|>
e) Subtrahiert man eines Vielfaches einer Zeile von einer anderen, so ändert sich die Welt von det(A) nicht. 

<|ref|>equation<|/ref|><|det|>[[25, 592, 930, 895]]<|/det|>
\[
\begin{align*}
\text{Bsp} : & \quad A = \begin{pmatrix} 1 & 2 & -3 \\ 2 & -4 & 1 \\ 2 & 2 & 8 \end{pmatrix} \\
& \quad \text{det}(A) = \begin{vmatrix} 1 & 2 & -3 \\ 2 & -4 & 1 \\ \hline 2 & 2 & 8 \end{vmatrix} = 2 \cdot \begin{vmatrix} 1 & 2 & -3 \\ 2 & -4 \end{vmatrix} = 2 \cdot \begin{vmatrix} 1 & 1 & 4 \end{vmatrix} = 2 \cdot \begin{vmatrix} 1 & -2 & 1 \end{vmatrix} = 2 \cdot (-1) \\
& \quad = 2 \cdot \begin{vmatrix} 1 & 2 & -3 \\ \hline 0 & -8 & 7 \\ 0 & -1 & 7 \end{vmatrix} = 2 \cdot (-1) \cdot \begin{vmatrix} 1 & 2 & -3 \\ \hline 1 & -1 & 7 \\ 0 & -8 & 7 \end{vmatrix} = 2 \cdot (-1) \cdot 1 \cdot (-1) \cdot (-49) = -98
\end{align*}
\]