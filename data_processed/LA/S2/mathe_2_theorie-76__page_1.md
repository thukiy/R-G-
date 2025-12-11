<|ref|>text<|/ref|><|det|>[[160, 30, 460, 60]]<|/det|>
für \(2 \times 2\) Matrix gilt: 

<|ref|>equation<|/ref|><|det|>[[187, 70, 808, 178]]<|/det|>
\[
\begin{align*}
A &= \begin{pmatrix} a & b \\ c & d \end{pmatrix} \quad \to \quad \text{invertierbar, wenn } ad \neq bc \\
&\quad \to A^{-1} = \frac{1}{ad - bc} \cdot \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[20, 206, 320, 235]]<|/det|>
## Lineare Abbildungen 

<|ref|>text<|/ref|><|det|>[[48, 246, 660, 272]]<|/det|>
entspricht einer stetigen Funktion in der Analysis 

<|ref|>equation<|/ref|><|det|>[[60, 283, 380, 344]]<|/det|>
\[
f : [a, b] \to [c, d]
\]

<|ref|>text<|/ref|><|det|>[[60, 364, 699, 392]]<|/det|>
Lineare Abbildung: Lineare Struktur wird erhalten 

<|ref|>text<|/ref|><|det|>[[48, 424, 230, 450]]<|/det|>
aus Analysis: 

<|ref|>text<|/ref|><|det|>[[48, 460, 682, 528]]<|/det|>
* Lineare Funktion \(f : \mathbb{R} \to \mathbb{R}\) mit \(f(x) = a \cdot x\)
  stellt Gesetze durch Ursprung mit \(m = a\) dar 

<|ref|>text<|/ref|><|det|>[[48, 538, 384, 565]]<|/det|>
* für \(x_1, x_2 \in \mathbb{R}\) gibt: 

<|ref|>equation<|/ref|><|det|>[[88, 575, 797, 640]]<|/det|>
\[
\begin{align*}
f(x_1 + x_2) &= a \cdot (x_1 + x_2) = a \cdot x_1 + a \cdot x_2 = f(x_1) \cdot f(x_2) \\
f(n \cdot x_1) &= a \cdot (n \cdot x_1) = n \cdot (a \cdot x_1) = n \cdot f(x_1)
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[88, 653, 875, 681]]<|/det|>
⇛ Eigenschaft nennt man linearität, Abbildung heisst linear 

<|ref|>text<|/ref|><|det|>[[20, 712, 370, 741]]<|/det|>
Def: Lineare Abbildung 

<|ref|>equation<|/ref|><|det|>[[135, 750, 975, 936]]<|/det|>
\[
\begin{align*}
V, W &\le \mathbb{R}^m \quad \text{seien Vektorräume} \\
\text{Eine lineare Abbildung } L : V \to W, \quad \vec{x} \to L(\vec{x}) \\
\text{heisst genau dann linear, wenn für } \forall \vec{x}, \vec{y} \in V \text{ und } n \in \mathbb{R} \text{ gilt:} \\
L(\vec{x} + \vec{y}) = L(\vec{x}) + L(\vec{y}) \\
L(n \cdot \vec{x}) = n \cdot L(\vec{x})
\end{align*}
\]