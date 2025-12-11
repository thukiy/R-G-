<|ref|>sub_title<|/ref|><|det|>[[114, 80, 770, 100]]<|/det|>
3. Lösen einer PDGL 1. Ordnung mit dem Charakteristikenverfahren 

<|ref|>text<|/ref|><|det|>[[114, 98, 460, 117]]<|/det|>
Gegeben ist das Anfangswertproblem 

<|ref|>equation<|/ref|><|det|>[[114, 115, 512, 138]]<|/det|>
\[xu_x + yu_y + (x^2 + y^2)u = 0, \quad x, y > 0,\]

<|ref|>equation<|/ref|><|det|>[[114, 138, 399, 161]]<|/det|>
\[u(x, -x^2) = e^{-x^2/2}, \quad x > 0.\]

<|ref|>text<|/ref|><|det|>[[114, 160, 758, 181]]<|/det|>
Finden Sie die Lösung \(u = u(x, y)\) mit dem Charakteristikenverfahren. 

<|ref|>text<|/ref|><|det|>[[114, 179, 490, 198]]<|/det|>
a) Gegeben ist das Anfangswertproblem 

<|ref|>equation<|/ref|><|det|>[[145, 196, 537, 217]]<|/det|>
\[tu_t + u_x = 2u, \quad u(x, 1) = x(u, t > 0).\]

<|ref|>text<|/ref|><|det|>[[145, 215, 822, 234]]<|/det|>
Benutzen Sie das Charakteristikenverfahren zur Bestimmung der Lösung \(u\). 

<|ref|>text<|/ref|><|det|>[[114, 248, 141, 265]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[114, 265, 686, 305]]<|/det|>
Das System der charakteristischen Differenzial-
gleichungen ist mit \(w(s) := u(k_1(s), k_2(s))\): 

<|ref|>equation<|/ref|><|det|>[[246, 316, 387, 337]]<|/det|>
\[k_1'(s) = k_1(s),\]

<|ref|>equation<|/ref|><|det|>[[246, 339, 387, 360]]<|/det|>
\[k_2'(s) = k_2(s),\]

<|ref|>equation<|/ref|><|det|>[[246, 362, 558, 386]]<|/det|>
\[w'(s) = -(k_1(s)^2 + k_2(s)^2)w(s).\]

<|ref|>text<|/ref|><|det|>[[119, 396, 543, 416]]<|/det|>
Es folgt \(k_1(s) = c_1 e^s\), \(k_2(s) = c_2 e^s\) und somit 

<|ref|>equation<|/ref|><|det|>[[268, 426, 537, 450]]<|/det|>
\[w'(s) = -(c_1^2 + c_2^2)e^{2s}w(s).\]

<|ref|>text<|/ref|><|det|>[[119, 460, 333, 480]]<|/det|>
Dies liefert die Lösung 

<|ref|>equation<|/ref|><|det|>[[216, 490, 589, 533]]<|/det|>
\[w(s) = c_3 \exp\left(-\frac{1}{2}(k_1(s)^2 + k_2(s)^2)\right).\]

<|ref|>text<|/ref|><|det|>[[119, 543, 580, 563]]<|/det|>
Als nächstes wird die Anfangskurve parametrisiert: 

<|ref|>equation<|/ref|><|det|>[[189, 572, 616, 615]]<|/det|>
\[(x_0(t), y_0(t), u_0(t)) = \left(t, -t^2, \exp\left(-\frac{1}{2}t^2\right)\right).\]

<|ref|>text<|/ref|><|det|>[[119, 625, 686, 645]]<|/det|>
Für \(s = 0\) soll \((k(s), w(s))\) auf dieser Anfangskurve liegen. 

<|ref|>text<|/ref|><|det|>[[119, 642, 602, 667]]<|/det|>
Damit folgt \(c_1 = t\), \(c_2 = -t^2\) und \(c_3 = \exp\left(\frac{1}{2}t^4\right)\) und 

<|ref|>equation<|/ref|><|det|>[[249, 677, 555, 699]]<|/det|>
\[x(s, t) = t e^s, \quad y(s, t) = -t^2 e^s.\]

<|ref|>text<|/ref|><|det|>[[119, 698, 228, 717]]<|/det|>
Dies liefert 

<|ref|>equation<|/ref|><|det|>[[359, 723, 446, 757]]<|/det|>
\[t = -\frac{y}{x}.\]

<|ref|>text<|/ref|><|det|>[[119, 755, 441, 774]]<|/det|>
Setzt man jetzt alles ein, erhält man 

<|ref|>equation<|/ref|><|det|>[[192, 784, 612, 829]]<|/det|>
\[u(x, y) = \exp\left(\frac{1}{2}\frac{y^4}{x^4}\right)\exp\left(-\frac{1}{2}(x^2 + y^2)\right).\]

<|ref|>text<|/ref|><|det|>[[114, 831, 144, 848]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[114, 846, 565, 865]]<|/det|>
https://www.youtube.com/watch?v=Gy_nl5BHkYg