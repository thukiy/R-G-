<|ref|>equation<|/ref|><|det|>[[253, 84, 560, 110]]<|/det|>
\[
\text{Substitution: } t = \sqrt{2} x, \text{ dt } = \sqrt{2} \text{ dx}
\]

<|ref|>equation<|/ref|><|det|>[[245, 110, 710, 210]]<|/det|>
\[
\begin{align*}
&= 2 \int_{0}^{a/\sqrt{2}} \sqrt{1 + x^2} \, \mathrm{d}x = 2 \cdot \frac{1}{2} \left[ x \sqrt{1 + x^2} + \arcsinh x \right]_{0}^{a/\sqrt{2}} \\
&= \frac{a}{\sqrt{2}} \sqrt{1 + (a/\sqrt{2})^2} + \arcsinh(a/\sqrt{2}).
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 213, 144, 231]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[115, 229, 500, 247]]<|/det|>
Wir berechnen zuerst die Ableitung der Kurve. 

<|ref|>equation<|/ref|><|det|>[[245, 258, 715, 319]]<|/det|>
\[
\dot{y}(t) = \begin{pmatrix} -\cos(t) - t(-\sin(t)) + \cos(t) \\ -\sin(t) + \sin(t) + t\cos(t) \end{pmatrix} = \begin{pmatrix} t\sin(t) \\ t\cos(t) \end{pmatrix}
\]

<|ref|>text<|/ref|><|det|>[[115, 319, 345, 338]]<|/det|>
Der Betrag ergibt sich zu 

<|ref|>equation<|/ref|><|det|>[[120, 341, 824, 383]]<|/det|>
\[
\|\dot{y}(t)\| = \sqrt{t^2 \sin^2(t) + t^2 \cos^2(t) + \frac{t^2}{4}} = \sqrt{t^2 (\sin^2(t) + \cos^2(t)) + \frac{1}{4}} = t\sqrt{1 + \frac{1}{4}} = t\sqrt{\frac{5}{2}}
\]

<|ref|>text<|/ref|><|det|>[[115, 384, 692, 403]]<|/det|>
Dieses Ergebnis wiederum eingesetzt in die Bogenlängenfunktion ergibt 

<|ref|>equation<|/ref|><|det|>[[232, 414, 714, 463]]<|/det|>
\[
L(t) = \int_{0}^{t} \|\dot{y}(\tau)\| \mathrm{d}\tau = \int_{0}^{t} \tau \frac{\sqrt{5}}{2} \mathrm{d}\tau = \left[ \tau^2 \frac{\sqrt{5}}{4} \right]_{0}^{t} = t^2 \frac{\sqrt{5}}{4}
\]

<|ref|>sub_title<|/ref|><|det|>[[115, 480, 264, 498]]<|/det|>
7. Vektorfelder 

<|ref|>text<|/ref|><|det|>[[115, 496, 572, 516]]<|/det|>
Skizzieren Sie jeweils die gegebenen Vektorfelder. 

<|ref|>equation<|/ref|><|det|>[[115, 512, 583, 550]]<|/det|>
\[
\text{a) } \ddot{v}(x, y) = \begin{pmatrix} 0,5 \\ 0,25 \end{pmatrix} \quad \text{b) } \ddot{v}(x, y) = \frac{1}{\sqrt{x^2 + y^2}} \begin{pmatrix} x \\ y \end{pmatrix}
\]

<|ref|>equation<|/ref|><|det|>[[115, 545, 585, 576]]<|/det|>
\[
\text{c) } \ddot{v}(x, y) = \frac{1}{\sqrt{x^3 + y^3}} \begin{pmatrix} y \\ -x \end{pmatrix} \quad \text{d) } \ddot{v}(x, y) = \frac{1}{\sqrt{x^4 + y^4}} \begin{pmatrix} y \\ x \end{pmatrix}
\]

<|ref|>text<|/ref|><|det|>[[115, 574, 650, 593]]<|/det|>
e) Plotten Sie das Vektorfeld aus a) – d) mit Python/Numpy. 

<|ref|>text<|/ref|><|det|>[[115, 608, 144, 625]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[115, 622, 833, 658]]<|/det|>
Dies ist ein homogenes Vektorfeld das sich die Länge und Richtung des Vektors
nicht ändern und somit unabhängig von x und y sind. 

<|ref|>equation<|/ref|><|det|>[[135, 660, 404, 682]]<|/det|>
\[
v(x; y) = \sqrt{0.5^2 + 0.25^2} \approx 0.6
\]

<|ref|>equation<|/ref|><|det|>[[125, 689, 333, 725]]<|/det|>
\[
m(x; y) = \frac{0.25}{0.5} = 0.5.
\]

<|ref|>image<|/ref|><|det|>[[120, 722, 644, 926]]<|/det|>