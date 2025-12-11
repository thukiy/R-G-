<|ref|>text<|/ref|><|det|>[[122, 65, 625, 85]]<|/det|>
c) Für die erste und zweite Ableitung von \(G\) erhalten wir 

<|ref|>equation<|/ref|><|det|>[[160, 91, 920, 135]]<|/det|>
\[
\begin{align*}
G'(x) &= 4x^{4-1} - 3 \cdot 2x^{2-1} + 0 = 4x^3 - 6x \tag{129} \\
G''(x) &= 4 \cdot 3x^{3-1} - 6 = 12x^2 - 6.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[150, 142, 920, 161]]<|/det|>
Da \(G'(x)\) ein kubisches Polynom ist, hat \(G\) höchstens drei kritische Stellen. Die Gleichung 

<|ref|>equation<|/ref|><|det|>[[368, 167, 920, 188]]<|/det|>
\[
0 = G'(x) = 4x^3 - 6x = 2x \cdot (2x^2 - 3) \quad (130)
\]

<|ref|>text<|/ref|><|det|>[[150, 197, 404, 215]]<|/det|>
hat offensichtlich die Lösung 

<|ref|>equation<|/ref|><|det|>[[500, 223, 920, 241]]<|/det|>
\[
x_1 = 0. \tag{131}
\]

<|ref|>text<|/ref|><|det|>[[150, 250, 348, 268]]<|/det|>
Zudem finden wir aus 

<|ref|>equation<|/ref|><|det|>[[454, 275, 920, 295]]<|/det|>
\[
2x^2 - 3 = 0 \quad | + 3 \quad (132)
\]

<|ref|>equation<|/ref|><|det|>[[293, 304, 920, 322]]<|/det|>
\[
\Leftrightarrow \qquad 2x^2 = 3 \quad | : 2 \quad (133)
\]

<|ref|>equation<|/ref|><|det|>[[293, 331, 920, 366]]<|/det|>
\[
\Leftrightarrow \qquad x^2 = \frac{3}{2} \quad | \pm \sqrt{\cdots} \quad (134)
\]

<|ref|>text<|/ref|><|det|>[[150, 370, 428, 388]]<|/det|>
zwei weitere Lösungen, nämlich 

<|ref|>equation<|/ref|><|det|>[[473, 394, 920, 433]]<|/det|>
\[
x_{2,3} = \pm \sqrt{\frac{3}{2}}. \quad (135)
\]

<|ref|>text<|/ref|><|det|>[[150, 440, 430, 457]]<|/det|>
Ferner berechnen wir die Werte 

<|ref|>equation<|/ref|><|det|>[[160, 462, 580, 481]]<|/det|>
\[
G(x_1) = G(0) = 0^4 - 3 \cdot 0^2 + 4 = 0 + 0 + 4 = 4
\]

<|ref|>equation<|/ref|><|det|>[[160, 486, 580, 504]]<|/det|>
\[
G''(x_1) = G''(0) = 12 \cdot 0^2 - 6 = 0 - 6 = -6 < 0.
\]

<|ref|>equation<|/ref|><|det|>[[160, 510, 763, 593]]<|/det|>
\[
\begin{align*}
G(x_2) &= G\left(+\sqrt{\frac{3}{2}}\right) = \left(+\sqrt{\frac{3}{2}}\right)^4 - 3\left(+\sqrt{\frac{3}{2}}\right)^2 + 4 = \frac{9}{4} - 3 \cdot \frac{3}{2} + 4 \\
&= \frac{9}{4} - \frac{18}{4} + \frac{16}{4} = \frac{7}{4}
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[160, 597, 920, 640]]<|/det|>
\[
G''(x_2) = G''\left(+\sqrt{\frac{3}{2}}\right) = 12\left(+\sqrt{\frac{3}{2}}\right)^2 - 6 = 12 \cdot \frac{3}{2} - 6 = 18 - 6 = 12 > 0 \quad (136)
\]

<|ref|>equation<|/ref|><|det|>[[160, 646, 763, 737]]<|/det|>
\[
\begin{align*}
G(x_3) &= G\left(+\sqrt{\frac{3}{2}}\right) = \left(+ \sqrt{\frac{3}{2}}\right)^4 - 3\left(+ \sqrt{\frac{3}{2}}\right)^2 + 4 = \frac{9}4 - 3 \cdot \frac{3}{2} + 4 \\
&= \frac 94 - \frac 184 + \frac 164 = \frac 74
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[160, 740, 810, 784]]<|/det|>
\[
G''(x_3) = G''\left(+\sqrt{\frac{3}{2}}\right) = \frac{12}{2}\left(+\sqrt{\frac{3}{2}}\right)^2 - 6 = \frac{12}{2} \cdot \frac{3}{2} - 6 = 18 - 6 = \frac{12}{2} > 0.
\]

<|ref|>text<|/ref|><|det|>[[150, 792, 696, 811]]<|/det|>
Wir stellen die Ergebnisse in der folgenden Tabelle zusammen. 

<|ref|>table<|/ref|><|det|>[[277, 818, 792, 919]]<|/det|>
<table><tr><td>k</td><td>xk</td><td>G(xk)</td><td>G'(xk)</td><td>G''(xk)</td><td>Typ</td></tr><tr><td>1</td><td>0</td><td>4</td><td>0</td><td>-6 &lt; 0</td><td>lokales Maximum</td></tr><tr><td>2</td><td>-√3/2</td><td>7/4</td><td>0</td><td>+12 &gt; 0</td><td>lokales Minimum</td></tr><tr><td>3</td><td>+√3/2</td><td>7/4</td><td>0</td><td>+12 &gt;0</td><td>lokales Minimum</td></tr></table>