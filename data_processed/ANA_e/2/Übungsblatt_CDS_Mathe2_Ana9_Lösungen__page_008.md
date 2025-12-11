<|ref|>text<|/ref|><|det|>[[115, 84, 142, 100]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[115, 101, 291, 118]]<|/det|>
Partielle Ableitungen: 

<|ref|>equation<|/ref|><|det|>[[176, 128, 468, 234]]<|/det|>
\[
\begin{align*}
\frac{\partial F}{\partial x} &= 4x^3 + 2\cos(y) \\
\frac{\partial F}{\partial y} &= -2x\sin(y) - \sqrt{2}\cos(y)\cos(z) \\
\frac{\partial F}{\partial z} &= \sqrt{2}\sin(y)\sin(z)
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 243, 183, 260]]<|/det|>
Damit: 

<|ref|>equation<|/ref|><|det|>[[176, 270, 820, 290]]<|/det|>
\[
dF = (4x^3 + 2\cos(y))dx + (-2x\sin(y) - \sqrt{2}\cos(y)\cos(z))dy + \sqrt{2}\sin(y)\sin(z)dz
\]

<|ref|>text<|/ref|><|det|>[[115, 291, 305, 308]]<|/det|>
Auf der Funktion f gilt: 

<|ref|>equation<|/ref|><|det|>[[176, 319, 816, 358]]<|/det|>
\[
\begin{align*}
dF &= (4x^3 + 2\cos(y))dx + (-2x\sin(y) -\sqrt{2}\cos(y)\cos(z))dy + \sqrt{2}\sin(y) \sin(z)dz \\
&= 0
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 369, 541, 389]]<|/det|>
Damit gilt an der betrachteten Stelle \((x,y,z) = (1, \frac{\pi}{2}, \frac{\pi}{4})\): 

<|ref|>equation<|/ref|><|det|>[[176, 398, 810, 580]]<|/det|>
\[
\begin{align*}
dF \left(1, \frac{\pi}{2}, \frac{\pi}{4}\right) &= \left(4 + 2\cos\left(\frac{\pi}{2}\right)\right)dx + \left(-2\sin\left(\frac{\pi}{2}\right) - \sqrt{2}\cos\left(\frac{\pi}{2}\right)\cos\left(\frac{\pi}{4}\right)\right)dy \\
&\qquad + \sqrt{2}\sin\left(\frac{\pi}{2}\right)\sin\left(\frac{\pi}{4}\right)dz \\
&= (4 + 2 \cdot 0)dx + \left(-2 \cdot 1 - \sqrt{2} \cdot 0 \cdot \frac{\sqrt{2}}{2}\right)dy \\
&\qquad + \sqrt{2} \cdot 1 \cdot \frac{\sqrt{2}}{2}dz \\
&= 4dx - 2dy + dz \\
&= 0
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 592, 186, 608]]<|/det|>
Daraus: 

<|ref|>equation<|/ref|><|det|>[[176, 620, 327, 638]]<|/det|>
\[
dz = -4dx + 2dy
\]

<|ref|>text<|/ref|><|det|>[[115, 650, 671, 670]]<|/det|>
Für Änderungen \(dx = dy = 0,1\) ergibt sich demzufolge als Änderung in \(z\) 

<|ref|>equation<|/ref|><|det|>[[176, 680, 541, 698]]<|/det|>
\[
dz = -4 \cdot 0,1 + 2 \cdot 0,1 = -0,4 + 0,2 = -0,2.
\]

<|ref|>text<|/ref|><|det|>[[115, 697, 142, 714]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[115, 712, 650, 728]]<|/det|>
Wir bringen die Funktion zunächst in eine für das Differenzieren günstigere Form: 

<|ref|>equation<|/ref|><|det|>[[166, 735, 785, 763]]<|/det|>
\[
u = \ln \sqrt{(2x^2 + 2y^2 + 2z^2)^3} = \ln (2x^2 + 2y^2 + 2z^2)^{3/2} = \frac{3}{2} \cdot \ln (2x^2 + 2y^2 + 2z^2)
\]

<|ref|>text<|/ref|><|det|>[[115, 770, 330, 786]]<|/det|>
Rechenregel: \(\ln a^n = n \cdot \ln a\) 

<|ref|>text<|/ref|><|det|>[[115, 790, 880, 818]]<|/det|>
Es genügt, die partielle Ableitung \(u_x\) zu bilden, denn die Funktion ist symmetrisch in den drei unabhängigen Variablen \(x\), \(y\) und \(z\). Die Ableitung \(u_x\) erhalten wir wie folgt mit Hilfe der Kettenregel: 

<|ref|>equation<|/ref|><|det|>[[162, 825, 790, 866]]<|/det|>
\[
u = \frac{3}{2} \cdot \ln \left(2x^2 + 2y^2 + 2z^2\right) = \frac{3}{2} \cdot \ln t \quad \text{mit} \quad t = 2x^2 + 2y^2 + 2z^2 \quad \text{und} \quad \frac{\partial t}{\partial x} = 4x
\]

<|ref|>equation<|/ref|><|det|>[[162, 874, 875, 907]]<|/det|>
\[
u_x = \frac{\partial u}{\partial x} = \frac{\partial u}{\partial t} \cdot \frac{\partial t}{\partial x} = \frac{3}{2} \cdot \frac{1}{t} \cdot 4x = \frac{3}{2} \cdot \frac{4x}{2x^2 + 2y^2 + 2z^2} = \frac{3 \cdot 4x}{2 \cdot 2(x^2 + y^2 + z^2)} = \frac{3x}{x^2 + y^2 + z^2}
\]