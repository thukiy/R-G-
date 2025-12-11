<|ref|>equation<|/ref|><|det|>[[117, 81, 533, 263]]<|/det|>
\[
\begin{align*}
x^2 - 4 &= x + 2 \quad \Rightarrow \quad x_1 = -2; \quad x_2 = 3 \\
A &= \int_{-2}^{3} [(x + 2) - (x^2 - 4)] \, dx = \\
&= \int_{-2}^{3} (-x^2 + x + 6) \, dx = \\
&= \left[ -\frac{1}{3} x^3 + \frac{1}{2} x^2 + 6x \right]_{-2}^{3} = 125/6
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 262, 668, 282]]<|/det|>
Nun lassen sich x- und y-Wert des Schwerpunkts bestimmen: 

<|ref|>equation<|/ref|><|det|>[[114, 283, 888, 558]]<|/det|>
\[
\begin{align*}
x_s &= \frac{1}{A} \cdot \int_{-2}^{3} x [(x + 2) - (x^2 - 4)] \, dx = \\
    &= \frac{1}{A} \cdot \int_{-2}^{3} (-x^3 + x^2 + 6x) \, dx = \\
    &= \frac{6}{125} \left[ -\frac{1}{4} x^4 + \frac{1}{3} x^3 + 3x^2 \right]_{-2}^{3} = 0.5 \\
y_s &= \frac{1}{2A} \cdot \int_{-2}^{3} [(x + 2)^2 - (x^2 - 4)^2] \, dx = \frac{1}{2A} \cdot \int_{-2}^{3} (-x^4 + 9x^2 + 4x - 12) \, dx = \\
    &= \frac{3}{125} \left[ -\frac{1}{5} x^5 + 3x^3 + 2x^2 - 12x \right]_{-2}^{3} = 0
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[120, 564, 684, 585]]<|/det|>
Der Flächenschwerpunkt liegt also auf der x-Achse: \(S = (0,5; 0)\) 

<|ref|>sub_title<|/ref|><|det|>[[114, 600, 432, 619]]<|/det|>
5. Schwerpunkt Rotationskörper 

<|ref|>text<|/ref|><|det|>[[114, 618, 825, 654]]<|/det|>
Bestimmen Sie den Schwerpunkt des Rotationskörpers, der durch Drehung der Funktion \(f(x) = \ln x, 1 \le x \le e\) um die x-Achse entsteht. 

<|ref|>text<|/ref|><|det|>[[114, 668, 830, 705]]<|/det|>
Zuerst Berechnung des Volumens des Rotationskörpers (Integral durch 2malige
partielle Integration lösen – Integrand ist \(1 \cdot (\ln x)^2\)): 

<|ref|>equation<|/ref|><|det|>[[120, 702, 816, 755]]<|/det|>
\[
V_x = \pi \cdot \int_{1}^{e} (\ln x)^2 \, dx = \pi \left[ x \left( (\ln x)^2 - 2 \cdot \ln x + 2 \right) \right]_{1}^{e} = \pi (e - 2) = 2,257
\]

<|ref|>text<|/ref|><|det|>[[114, 755, 856, 791]]<|/det|>
Der Schwerpunkt liegt auf der x-Achse, d. h. \(y_s = 0\). Integral durch 2malige partielle
Integration lösen. 

<|ref|>equation<|/ref|><|det|>[[120, 790, 907, 843]]<|/det|>
\[
x_s = \frac{\pi}{V_x} \cdot \int_{1}^{e} x (\ln x)^2 \, dx = \frac{1}{e-2} \left[ \frac{1}{2} x^2 \left( (\ln x)^2 - \ln x + \frac{1}{2} \right) \right]_{1}^{e} = \frac{e^2 - 1}{4(e-2)} = 2,224
\]