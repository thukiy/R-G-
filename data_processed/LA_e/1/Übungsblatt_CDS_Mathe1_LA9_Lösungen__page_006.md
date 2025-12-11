<|ref|>text<|/ref|><|det|>[[114, 81, 275, 100]]<|/det|>
Mit k) ergibt sich: 

<|ref|>equation<|/ref|><|det|>[[117, 100, 735, 252]]<|/det|>
\[
\begin{align*}
|v \times w| &= \sqrt{(v \times w, v \times w)} = \sqrt{\langle v, v \rangle \cdot \langle w, w \rangle - \langle v, w \rangle \cdot \langle w, v \rangle} \\
&= \sqrt{|v|^2 \cdot |w|^2 - \langle v, w \rangle^2} = \sqrt{|v|^2 \cdot |w|^2 - \left( |v| \cdot |w| \cdot \cos(\alpha) \right)^2} \\
&= \sqrt{|v|^2 \cdot |w|^2 - |v|^2 \cdot |w|^2 \cdot \cos^2(\alpha)} = \sqrt{|v|^2 \cdot |w|^2 \cdot \left( 1 - \cos^2(\alpha) \right)} \\
&= \sqrt{|v|^2 \cdot |w|^2 \cdot \sin^2(\alpha)} = |v| \cdot |w| \cdot |\sin(\alpha)| = \frac{|v| \cdot |w| \cdot \sin(\angle(v, w))}{2}.
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[114, 266, 333, 284]]<|/det|>
7. Terme mit Vektoren 

<|ref|>text<|/ref|><|det|>[[114, 284, 870, 323]]<|/det|>
Gegeben seien die Vektoren \(\vec{a}, \vec{b}, \vec{c} \in \mathbb{R}^3\). Vereinfachen Sie die folgenden Terme
jeweils soweit wie möglich unter Zuhilfenahme der Rechenregeln für Vektoren in 3D. 

<|ref|>text<|/ref|><|det|>[[114, 321, 330, 343]]<|/det|>
a) \((\vec{a} - 2\vec{b}) \times (3\vec{a} - \vec{b})\). 

<|ref|>text<|/ref|><|det|>[[114, 340, 360, 364]]<|/det|>
b) \((\vec{a} \times (\vec{b} - 2\vec{a}), 4\vec{b} - 2\vec{a})\). 

<|ref|>text<|/ref|><|det|>[[114, 361, 295, 384]]<|/det|>
c) \((\vec{a} \times (\vec{a} \times \vec{b}), \vec{b})\). 

<|ref|>text<|/ref|><|det|>[[114, 381, 355, 404]]<|/det|>
d) \((\hat{a} \times \vec{b}, \hat{a} \times \vec{c})\) für \(\vec{a} \perp \vec{b}\). 

<|ref|>text<|/ref|><|det|>[[114, 417, 147, 435]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[117, 435, 805, 492]]<|/det|>
\[
\begin{align*}
(a - 2b) \times (3a - b) &= a \times 3a - 2b \times 3a - a \times b + 2b \times b = 0 - 6b \times a - a \times b + 0 \\
&= 6a \times b - a \times b = 5a \times b.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 492, 147, 509]]<|/det|>
b) 

<|ref|>equation<|/ref|><|det|>[[117, 508, 739, 567]]<|/det|>
\[
\begin{align*}
\langle a \times (b - 2a), 4b - 2a \rangle &= \langle a \times b - 2 \cdot a \times a, 4b - 2a \rangle = \langle a \times b, 4b - 2a \rangle \\
&= \langle a \times b, 4b \rangle - \langle a \times b, 2a \rangle = 0 - 0 = \underline{0}.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 565, 147, 582]]<|/det|>
c) 

<|ref|>text<|/ref|><|det|>[[114, 580, 250, 598]]<|/det|>
1. Möglichkeit: 

<|ref|>equation<|/ref|><|det|>[[117, 597, 700, 654]]<|/det|>
\[
\begin{align*}
\langle a \times (a \times b), b \rangle &= \langle b \times a, a \times b \rangle = \langle -a \times b, a \times b \rangle = -\langle a \times b, a \times b \rangle \\
&= -|a \times b|^2.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 654, 250, 672]]<|/det|>
2. Möglichkeit: 

<|ref|>equation<|/ref|><|det|>[[117, 671, 755, 760]]<|/det|>
\[
\begin{align*}
\langle a \times (a \times b), b\rangle &= \langle \langle a, b \rangle \cdot a - \langle a, a \rangle \cdot b, b \rangle = \langle \langle a, b \rangle \cdot a, b \rangle - \langle \langle a, a \rangle \cdot b, b \rangle \\
&= \langle a, b \rangle \cdot \langle a, b \rangle - \langle a, a \rangle \cdot \langle b, b \rangle = -\left( |a|^2 \cdot |b|^2 - \langle a, b \rangle^2 \right) \\
&= -|a \times b|^2.
\end{align*}
\]

<|ref|>text<|/ref|> numerators<|/ref|><|det|>[[114, 760, 147, 778]]<|/det|>
d) 

<|ref|>equation<|/ref|><|det|>[[117, 778, 688, 835]]<|/det|>
\[
\begin{align*}
\langle \hat{a} \times b, \hat{a} \times c \rangle &= \langle \hat{a}, \hat{a} \rangle \cdot \langle b, c \rangle - \langle \hat{a}, c \rangle \cdot \langle b, \hat{a} \rangle = 1 \cdot \langle b, c \rangle - \langle \hat{a}, c \rangle 0 \\
&= \langle b, c \rangle.
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[114, 851, 273, 868]]<|/det|>
8. Dreieck in 3D 

<|ref|>text<|/ref|><|det|>[[114, 867, 860, 887]]<|/det|>
Gegeben sei ein Dreieck mit den Eckpunkten A = (1;-2;0), B = (2;1;4), C = (0;-2;-2). 

<|ref|>text<|/ref|><|det|>[[114, 885, 486, 903]]<|/det|>
a) Berechnen Sie die Länge der Seite a. 

<|ref|>text<|/ref|><|det|>[[114, 902, 510, 920]]<|/det|>
b) Berechnen Sie die Fläche des Dreiecks.