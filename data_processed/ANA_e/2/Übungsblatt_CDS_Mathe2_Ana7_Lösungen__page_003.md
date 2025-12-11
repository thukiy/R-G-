<|ref|>text<|/ref|><|det|>[[115, 82, 150, 100]]<|/det|>
b) 

<|ref|>equation<|/ref|><|det|>[[125, 96, 820, 325]]<|/det|>
\[
\begin{align*}
\underline{I} &= \int_{1}^{2} \int_{1-x}^{\sqrt{x}} x^2 y \, \mathrm{d}y \, \mathrm{d}x = \int_{1}^{2} x^2 \cdot \frac{1}{2} \cdot \left[ y^2 \right] \Big|_{1-x}^{\sqrt{x}} \, \mathrm{d}x = \frac{1}{2} \int_{1}^{2} x^2 \cdot \left( x - (1-x)^2 \right) \, \mathrm{d}x \\
&= \frac{1}{2} \int_{1}^{2} x^2 \cdot (x - 1 + 2x - x^2) \, \mathrm{d}x = \frac{1}{2} \int_{1}^{2}x^2 \cdot (3x - 1 - x^2) \, \mathrm{d}x \\
&= \frac{1}{2} \int_{1} (3x^3 - x^2 - x^4) \, \mathrm{d}x = \frac{1}{2} \cdot \left[ \frac{3x^4}{4} - \frac{x^5}{3} - \frac{x^5}{5} \right] \Big|_{1}^{2} \\
&= \frac{1}{2} \cdot \left( \frac{3 \cdot 2^4}{4} - \frac{2^3}{3} - \frac{2^5}{5} - \frac{3 \cdot 1^4}{4} + \frac{1^3}{3} + \frac{1^5}{5} \right) = \frac{1}{2} \cdot \left( 12 - \frac{8}{3} - \frac{32}{5} - \frac{3}{4} + \frac{1}{3} + \frac{1}{5} \right) \\
&= \frac{1}{2} \cdot \left( 12 - \frac{7}{3} - \frac{31}{5} - \frac{3}{4} \right) = \frac{1}{2} \cdot \left( \frac{720}{60} - \frac{140}{60} - \frac{372}{60} - \frac{45}{60} \right) = \frac{1}{2} \cdot \frac{163}{60} = \frac{163}{120}.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 325, 150, 343]]<|/det|>
c) 

<|ref|>equation<|/ref|><|det|>[[125, 341, 805, 430]]<|/det|>
\[
\begin{align*}
\underline{I} &= \int_{1}^{2}\int_{0}^{x} e^{\frac{y}{x}} \, \mathrm{d}y \, \mathrm{d}x = \int_{1}^{2} \left[ x \cdot e^{\frac{y}{x}} \right]_{0}^{x} \, \mathrm{d}x = \int_{1}^{2} x \cdot \left( e^{\frac{x}{x}} - e^{\frac{0}{x}} \right) \, \mathrm{d}x = (e-1) \int_{1}^{2} x \, \mathrm{d}x \\
&= (e-1) \cdot \frac{1}{2} \cdot \left[ x^2 \right]_{1}^{2} = (e-1) \cdot \left( \frac{2^2}{2} - \frac{1^2}{2} \right) = (e-1) \cdot \left( \frac{4}{2} - \frac{1}{2} \right) = \frac{3}{2} \cdot (e-1).
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 440, 360, 459]]<|/det|>
4. Integrale über Gebiete 

<|ref|>text<|/ref|><|det|>[[115, 457, 802, 476]]<|/det|>
Berechnen Sie das folgende Integral über das jeweils angegebene Gebiet G. 

<|ref|>equation<|/ref|><|det|>[[428, 483, 565, 526]]<|/det|>
\[
I = \int_{G} 2xy^2 \, dA
\]

<|ref|>text<|/ref|><|det|>[[115, 526, 603, 545]]<|/det|>
a) Rechteck mit Eckpunkten (-1;-1), (4;-1), (4;2), (-1;2) 

<|ref|>text<|/ref|><|det|>[[115, 544, 518, 562]]<|/det|>
b) Dreieck mit Eckpunkten (0;0), (3;1), (-2;1) 

<|ref|>text<|/ref|><|det|>[[115, 577, 150, 595]]<|/det|>
a) 

<|ref|>image<|/ref|><|det|>[[115, 595, 540, 765]]<|/det|>
 

<|ref|>equation<|/ref|><|det|>[[125, 765, 872, 880]]<|/det|>
\[
\begin{align*}
\underline{I} &= \int_{G} 2xy^2 \, dA = 2 \int_{G} xy^2 \, dA = 2 \int_{-1}^{2} \int_{-1}^{4} xy^2 \, dx \, dy = 2 \int_{-1}^{4} x \, dx \cdot \int_{-1}^{2} y^2 \, dy \\
&= 2 \cdot \frac{1}{2} \cdot \left[ x^2 \right]_{-1}^{4} \cdot \frac{1}{3} \cdot \left[ y^3 \right]_{-1}^{2} = \left( 4^2 - (-1)^2 \right) \cdot \frac{1}{3} \cdot \left( 2^3 - (-1)^3 \right) = (16-1) \cdot \frac{1}{3} \cdot (8+1) \\
&= 15 \cdot \frac{1}{3} \cdot 9 = 5 \cdot 9 = \frac{45}{3}.
\end{align*}
\]