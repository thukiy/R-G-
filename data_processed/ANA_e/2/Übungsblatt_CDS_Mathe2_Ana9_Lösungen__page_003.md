<|ref|>text<|/ref|><|det|>[[115, 84, 142, 100]]<|/det|>
e) 

<|ref|>text<|/ref|><|det|>[[115, 100, 880, 128]]<|/det|>
Differenziert wird jeweils nach der Produktregel, wobei die (partiellen) Ableitungen des Faktors \(\cosh(xy)\) mit Hilfe der Kettenregel gebildet werden: 

<|ref|>equation<|/ref|><|det|>[[159, 133, 845, 176]]<|/det|>
\[
z = \underbrace{(x^3 - y^2)}_{\text{u}} \cdot \underbrace{\cosh(xy)}_{\text{v}} = uv \quad \text{mit} \quad u = x^3 - y^2 \quad \text{und} \quad v = \cosh \frac{(xy)}{t} = \cosh t \quad \text{mit} \quad t = xy
\]

<|ref|>equation<|/ref|><|det|>[[159, 177, 845, 195]]<|/det|>
\[
u_x = 3x^2, \quad u_y = -2y \quad \text{und} \quad v_x = (\sinh t) \cdot y = y \cdot \sinh (xy), \quad v_y = (\sinh t) \cdot x = x \cdot \sinh (xy)
\]

<|ref|>equation<|/ref|><|det|>[[159, 203, 620, 221]]<|/det|>
\[
z_x = u_x v + v_x u = 3x^2 \cdot \cosh (xy) + y \cdot \sinh (xy) \cdot (x^3 - y^2) =
\]

<|ref|>equation<|/ref|><|det|>[[179, 228, 488, 246]]<|/det|>
\[
= 3x^2 \cdot \cosh (xy) + (x^3 y - y^3) \cdot \sinh (xy)
\]

<|ref|>equation<|/ref|><|det|>[[159, 255, 625, 273]]<|/det|>
\[
z_y = u_y v + v_y u = -2y \cdot \cosh (xy) + x \cdot \sinh (xy) \cdot (x^3 - y^2) = 
\]

<|ref|>equation<|/ref|><|det|>[[179, 280, 496, 298]]<|/det|>
\[
= -2y \cdot \cosh (xy) + (x^4 - xy^2) \cdot \sinh (xy)
\]

<|ref|>text<|/ref|><|det|>[[115, 297, 142, 315]]<|/det|>
f) 

<|ref|>text<|/ref|><|det|>[[120, 316, 435, 334]]<|/det|>
Wir benötigen jeweils die Kettenregel: 

<|ref|>equation<|/ref|><|det|>[[174, 344, 880, 496]]<|/det|>
\[
\begin{align*}
z &= \ln (2x + e^{3y}) = \ln u \quad \text{mit} \quad u = 2x + e^{3y} \quad \text{und} \quad \frac{\partial u}{\partial x} = 2, \quad \frac{\partial u}{\partial y} = 3 \cdot e^{3y} \\
z_x &= \frac{\partial z}{\partial x} = \frac{\partial z}{\partial u} \cdot \frac{\partial u}{\partial x} = \frac{1}{u} \cdot 2 = \frac{2}{u} = \frac{2}{2x + e^{3y}} \\
z_y &= \frac{\partial z}{\partial y} = \frac{\partial z}{\partial u} \cdot \frac{\partial u}{\delta y} = \frac{1}{u} \cdot 3 \cdot e^{3y} = \frac{3 \cdot e^{3y}}{u} = \frac{3 \cdot e^{3y}}{2x + e^{3y}}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 508, 521, 526]]<|/det|>
3. Partielle Ableitungen 1. und 2. Ordnung 

<|ref|>text<|/ref|><|det|>[[115, 525, 664, 544]]<|/det|>
Bestimmen Sie alle partiellen Ableitungen 1. und 2. Ordnung. 

<|ref|>text<|/ref|><|det|>[[115, 542, 390, 561]]<|/det|>
a) \(z = f(x, y) = x \cdot e^y - y \cdot e^x\) 

<|ref|>text<|/ref|><|det|>[[115, 559, 373, 578]]<|/det|>
b) \(z = f(x, y) = \ln(2y - x^2)\) 

<|ref|>text<|/ref|><|det|>[[115, 577, 372, 599]]<|/det|>
c) \(z = f(x, y) = \sqrt{x^2 - 2xy}\). 

<|ref|>text<|/ref|><|det|>[[115, 613, 147, 630]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[120, 631, 797, 650]]<|/det|>
Alle Ableitungen erhält man durch elementare gliedweise (partielle) Differentiation. 

<|ref|>text<|/ref|><|det|>[[120, 664, 415, 682]]<|/det|>
Partielle Ableitungen 1. Ordnung 

<|ref|>equation<|/ref|><|det|>[[179, 693, 707, 730]]<|/det|>
\[
z_x = \frac{\partial}{\partial x} [x \cdot e^y - y \cdot e^x] = 1 \cdot e^y - y \cdot e^x = e^y - y \cdot e^x
\]

<|ref|>equation<|/ref|><|det|>[[179, 739, 707, 777]]<|/det|>
\[
z_y = \frac{\partial}{\partial y} [x \cdot e^y - y \cdot e^x] = x \cdot e^y - 1 \cdot e^x = x \cdot e^y - e^x
\]