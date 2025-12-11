<|ref|>equation<|/ref|><|det|>[[123, 87, 352, 110]]<|/det|>
\[
= 2y - 2xz + 2z^2
\]

<|ref|>sub_title<|/ref|><|det|>[[114, 125, 404, 143]]<|/det|>
2. Rotation von Vektorfeldern 

<|ref|>text<|/ref|><|det|>[[114, 142, 617, 161]]<|/det|>
Bestimmen Sie die Rotation der folgenden Vektorfelder. 

<|ref|>equation<|/ref|><|det|>[[114, 160, 675, 213]]<|/det|>
\[
\text{a) } \vec{F}(x, y) = \frac{1}{\sqrt{x^2 + y^2}} \begin{pmatrix} y \\ -x \end{pmatrix} \qquad \text{b) } \vec{F}(x, y, z) = \begin{pmatrix} xy - z^2 \\ 2xyz \\ x^2z - y^2z \end{pmatrix}
\]

<|ref|>equation<|/ref|><|det|>[[114, 213, 488, 245]]<|/det|>
\[
\text{c) } \vec{F}(x, y, z) = \frac{1}{\sqrt{x^2 + y^2 + z^2}} (x\hat{e}_x + y\hat{e}_y + z\hat{e}_z)
\]

<|ref|>text<|/ref|><|det|>[[114, 258, 142, 275]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[114, 277, 600, 303]]<|/det|>
\[
F_x = y(x^2 + y^2)^{-1/2}; \quad F_y = -x(x^2 + y^2)^{-1/2}
\]

<|ref|>equation<|/ref|><|det|>[[114, 315, 876, 521]]<|/det|>
\[
\begin{align*}
(\text{rot } \vec{F})_z &= \frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y} = \frac{\partial}{\partial x} \left[ -x(x^2 + y^2)^{-1/2} \right] - \frac{\partial}{\partial y} \left[ y(x^2 + y^2)^{-1/2} \right] = \\
&= -(x^2 + y^2)^{-1/2} + x^2(x^2 + y^2)^{-3/2} - (x^2 + y^2)^{-1/2} + y^2(x^2 + y^2)^{-3/2} = \\
&= -2(x^2 + y^2)^{-1/2} + (x^2 + y^2)(x^2 + y^2)^{-3/2} = \\
&= -2(x^2+y^2)^{-1/2} + (x^2+y^2)^{-1/2} = -(x^2+y^2)^{-1/2} = -\frac{1}{\sqrt{x^2+y^2}}
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[114, 520, 770, 556]]<|/det|>
\[
\text{Somit: } \text{rot } \vec{F} = -\frac{1}{\sqrt{x^2 + y^2}} \vec{e}_z = -\frac{1}{r} \vec{e}_z \qquad (\text{mit } r = \sqrt{x^2 + y^2})
\]

<|ref|>text<|/ref|><|det|>[[114, 558, 142, 575]]<|/det|>
b) 

<|ref|>equation<|/ref|><|det|>[[114, 577, 620, 603]]<|/det|>
\[
F_x = xy - z^2; \quad F_y = 2xyz; \quad F_z = x^2z - y^2z
\]

<|ref|>equation<|/ref|><|det|>[[114, 576, 820, 705]]<|/det|>
\[
\begin{align*}
(\text{rot } \vec{F})_x &= \frac{\partial F_z}{\partial y} - \frac{\partial F_y}{\partial z} = -2yz - 2xy \\
(\text{rot } \vec{F})_y &= \frac{\partial F_x}{\partial z} - \frac{\partial F_z}{\partial x} = -2zx - 2xz \\
(\text{rot } \vec{F})_z &= \frac{\partial F_y}{\overbrace{\partial x}} - \frac{\partial F_x}{\partial y} = 2yz - x
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[114, 705, 876, 900]]<|/det|>
\[
\begin{align*}
F_x &= x(x^2 + y^2 + z^2)^{-1/2}; \quad F_y = y(x^2 + y^2 + z^2)^{-1/2}; \quad F_z = z(x^2 + y^2 + z^2)^{-1/2} \\
(\text{rot } \vec{F})_x &= \frac{\partial F_z}{\overbrace{\partial y}} - \frac{\partial F_y}{\overbrace{\partial z}} = \frac{\partial}{\partial y} \left( z(x^2 + y^2 + z^2)^{-1/2} \right) - \frac{\partial}{\partial z} \left( y(x^2 + y^2 + z^2)^{-1/2} \right) = \\
&= z \left( -\frac{1}{2} \right) (x^2 + y^2 + z^2)^{-3/2} \cdot 2y - y \left( -\frac{1}{2} \right) (x^2 + y^{2} + z^2)^{-3/2} \cdot 2z = \\
&= -yz(x^2 + y^2 + z^2)^{-3/2} + yz(x^2 + y^2 + z^2)^{-3/2} = 0
\end{align*}
\]