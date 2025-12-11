<|ref|>equation<|/ref|><|det|>[[160, 88, 700, 188]]<|/det|>
\[
\begin{align*}
\text{Var}(X) &= E(X^2) - [E(X)]^2 = \frac{1}{2} - \left(\frac{1}{2}\right)^2 = \frac{1}{2} - \frac{1}{4} = \frac{1}{4} \\
E(Y) &= \int_{0}^{\infty} y \cdot e^{-y} \, dy = \left[(-y - 1) \cdot e^{-y}\right]_{0}^{\infty} = 0 + 1 = 1 \\
\text{Integral } 313 \text{ mit } a = -1
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[163, 220, 787, 303]]<|/det|>
\[
\begin{align*}
E(Y^2) &= \int_{0}^{\infty} y^2 \cdot e^{-y} \, dy = \left[ \frac{y^2 + 2y + 2}{-1} \cdot e^{-y} \right]_{0}^{\infty} = 0 + 2 = 2 \\
\text{Integral } 314 \text{ mit } a = -1
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[164, 319, 590, 343]]<|/det|>
\[
\text{Var}(Y) = E(Y^2) - [E(Y)]^2 = 2 - 1^2 = 1
\]

<|ref|>equation<|/ref|><|det|>[[122, 347, 828, 510]]<|/det|>
\[
\begin{align*}
d) \quad P(0 \le X \le 2; 0 \le Y \le 3) &= 2 \cdot \int_{x=0}^{2} \int_{y=0}^{3} e^{-2x-y} \, dy \, dx = \\
&= 2 \cdot \int_{0}^{2} e^{-2x} \, dx \cdot \int_{0}^{3} e^{-y} \, dy = 2 \left[-\frac{1}{2} \cdot e^{-2x}\right]_{0}^{2} \cdot \left[-\frac{1}{2} \cdot e^{-y}\right]_{0}^{3} = \\
&= \left[ e^{-2x} \right]_{0}^{2} \cdot \left[ e^{-y} \right]_{0}^{3} = (e^{-4} - 1) (e^{-3} - 1) = 0,9328
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[130, 520, 470, 544]]<|/det|>
22 Integrale mit \(e^{ax}\) (a ≠ 0) 

<|ref|>equation<|/ref|><|det|>[[130, 560, 330, 590]]<|/det|>
\[
(312) \int e^{ax} \, dx = \frac{1}{a} \cdot e^{ax}
\]

<|ref|>equation<|/ref|><|det|>[[130, 595, 380, 627]]<|/det|>
\[
(313) \int x \cdot e^{ax} \, dx = \left(\frac{ax - 1}{a^2}\right) \cdot e^{ax}
\]

<|ref|>equation<|/ref|><|det|>[[130, 633, 444, 666]]<|/det|>
\[
(314) \int x^2 \cdot e^{ax} \, dx = \left(\frac{a^2 x^2 - 2ax + 2}{a^3}\right) \cdot e^{ax}
\]

<|ref|>sub_title<|/ref|><|det|>[[114, 690, 192, 707]]<|/det|>
7. Cafe 

<|ref|>text<|/ref|><|det|>[[114, 706, 866, 792]]<|/det|>
Bei einem Cafebesitzer entfallen 60 % der Bestellungen auf Kaffee und Kuchen
sowie 40 % auf Eis. An seinen Öffnungstagen herrscht zu 30 % Sonnenschein und
zu 70 % Bewölkung oder Regen. Wie gross sind die gemeinsamen
Wahrscheinlichkeiten, wenn die beiden Zufallsvariablen "Bestellungen" und "Wetter"
unabhängig voneinander sind? 

<|ref|>text<|/ref|><|det|>[[114, 805, 820, 858]]<|/det|>
Gegeben sind die Randverteilungen der beiden Zufallsvariablen X und Y. Ihr
Produkt muss bei Unabhängigkeit mit den gemeinsamen Wahrscheinlichkeiten
\(p_{ik}\) identisch sein. Wir bestimmen die \(p_{ik}\) mittels einer Verteilungstabelle: