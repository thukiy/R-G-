<|ref|>text<|/ref|><|det|>[[122, 83, 225, 101]]<|/det|>
Es gilt also 

<|ref|>equation<|/ref|><|det|>[[280, 113, 757, 133]]<|/det|>
\[
F(x) = \sinh(x) \cosh(x) - x + b - F(x) \quad | + F(x) \]

<|ref|>equation<|/ref|><|det|>[[260, 141, 722, 160]]<|/det|>
\[
2 \cdot F(x) = \sinh(x) \cosh(x) - x + b \quad | : 2.
\]

<|ref|>text<|/ref|><|det|>[[122, 172, 295, 189]]<|/det|>
Daraus erhalten wir 

<|ref|>equation<|/ref|><|det|>[[122, 197, 621, 235]]<|/det|>
\[
\frac{F(x)}{2} = \frac{\sinh(x) \cosh(x) - x + b}{2} = \frac{\sinh(x) \cosh(x) - x}{2} + c.
\]

<|ref|>text<|/ref|><|det|>[[113, 235, 137, 253]]<|/det|>
j) 

<|ref|>equation<|/ref|><|det|>[[115, 252, 520, 290]]<|/det|>
\[
F(x) = \int \cosh^2(x) \, dx = \int \cosh(x) \cdot \cosh(x) \, dx
\]

<|ref|>equation<|/ref|><|det|>[[161, 310, 875, 412]]<|/det|>
\[
\begin{align*}
&= \cosh(x) \cdot \sinh(x) - \int \sinh(x) \cdot \sinh(x) \, dx = \cosh(x) \sinh(x) - \int \sinh^2(x) \, dx \\
&= \cosh(x) \sinh(x) - \int (\cosh^2(x) - 1) \, dx = \cosh(x) \sinh(x) - \int \cosh^2(x) \, dx + \int 1 \, dx \\
&= \cosh(x) \sinh(x) - F(x) + x + b.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 423, 220, 441]]<|/det|>
Es gilt also 

<|ref|>equation<|/ref|><|det|>[[275, 453, 752, 499]]<|/det|>
\[
\begin{align*}
F(x) &= \cosh(x) \sinh(x) - F(x) + x + b \quad | + F(x) \\
2 \cdot F(x) &= \cosh(x) \sinh(x) + x + b
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[122, 509, 308, 526]]<|/det|>
Daraus erhalten wir 

<|ref|>equation<|/ref|><|det|>[[122, 533, 652, 572]]<|/det|>
\[
\frac{F(x)}{2} = \frac{\cosh(x) \sinh(x) + x + b}{2} = \frac{\cosh(x) \sinh(x) + x}{2} + c.
\]

<|ref|>text<|/ref|><|det|>[[115, 588, 660, 605]]<|/det|>
3. Stammfunktionen mit partieller Integration bestimmen 

<|ref|>text<|/ref|><|det|>[[115, 604, 844, 638]]<|/det|>
Berechnen Sie die folgenden bestimmten Integrale mit der Methode der partiellen
Integration. 

<|ref|>equation<|/ref|><|det|>[[115, 635, 643, 666]]<|/det|>
a) \(\int_0^3 \frac{x}{2\sqrt{x+1}} dx\) b) \(\int_1^2 x\sqrt{x-1} dx\) 

<|ref|>equation<|/ref|><|det|>[[115, 665, 241, 686]]<|/det|>
c) \(\int_1^2 x \ln x \, dx\)

<|ref|>text<|/ref|><|det|>[[115, 703, 142, 720]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[122, 716, 810, 920]]<|/det|>
\[
\begin{align*}
I &= \int_0^3 \frac{x}{2\sqrt{x+1}} \, dx = \int_0^3 x \cdot \frac{1}{2\sqrt{x+1}} \, dx = \left[ x \cdot \sqrt{x+1} \right]_0^3 - \int_0^3 \sqrt{x+1} \, dx \\
&= \left[ x \cdot \sqrt{x+1} \right]_0^3 - 2 \cdot \left[ (x+1)^{\frac{3}{2}} \right]_0^3 \\
&= 3 \cdot \sqrt{3+1} - 0 \cdot \sqrt{0+1} - \frac{2}{3} \cdot (3+1)^{\frac{3}{2}} + \frac{2}{3} \cdot (0+1)^{\frac{3}{2}} = 6 - 0 - \frac{2}{3} \cdot 8 + \frac{2}{3} \\
&= \frac{18}{3} - \frac{16}{3} + \frac{2}{3} = \frac{4}{3}.
\end{align*}
\]