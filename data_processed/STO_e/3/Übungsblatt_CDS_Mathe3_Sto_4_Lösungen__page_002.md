<|ref|>equation<|/ref|><|det|>[[125, 78, 875, 210]]<|/det|>
\[
\begin{align*}
\text{a) Normierung: } a \cdot \int_0^2 (2x^2 - x^3) \, dx &= a \left[ \frac{2}{3} x^3 - \frac{1}{4} x^4 \right]_0^2 = \frac{4}{3} a = 1 \quad \Rightarrow \quad a = 3/4 \\
\text{b) } F(x) &= \frac{3}{4} \cdot \int_0^x (2u^2 - u^3) \, du = \frac{3}{4} \left[ \frac{2}{3} u^3 - \frac{1}{4} u^4 \right]_0^x = \frac{1}{16} (8x^3 - 3x^4) \\
\text{(0 $\le$ $x$ $\le$ 2)}
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[125, 225, 397, 245]]<|/det|>
c) \(P(X \le 1) = F(1) = 5/16\)

<|ref|>sub_title<|/ref|><|det|>[[115, 260, 460, 279]]<|/det|>
3. Parameter einer Dichtefunktion II 

<|ref|>text<|/ref|><|det|>[[115, 277, 825, 312]]<|/det|>
Gegeben sei die Verteilungsfunktion \(F(x) = a \cdot \tan^{-1}(x) + b\), \(-\infty < x < \infty\) einer
stetigen Zufallsvariable. 

<|ref|>text<|/ref|><|det|>[[115, 310, 533, 328]]<|/det|>
Bestimmen Sie die beiden Parameter a und b. 

<|ref|>text<|/ref|><|det|>[[115, 327, 584, 346]]<|/det|>
Wie lautet die Dichtefunktion f(x) dieser Verteilung? 

<|ref|>text<|/ref|><|det|>[[115, 362, 877, 400]]<|/det|>
a) Aus den Grenzwerten \(\lim_{x \to -\infty} F(x) = 0\) und \(\lim_{x \to \infty} F(x) = 1\) lassen sich die unbekannten
Parameter \(a\) und \(b\) wie folgt bestimmen: 

<|ref|>equation<|/ref|><|det|>[[155, 410, 735, 530]]<|/det|>
\[
\begin{align*}
\text{(I) } \lim_{x \to -\infty} (a \cdot \arctan x + b) &= a \left( -\frac{\pi}{2} \right) + b = 0 \\
\text{(II) } \lim_{x \to \infty} (a \cdot \arctan x + b) &= a \left( \frac{\pi}{2} \right) + b = 1 \\
2b = 1 \quad \Rightarrow \quad b = \frac{1}{2} \quad ; \quad \text{(II)} \quad \Rightarrow \quad a \left( \frac{\pi}{2} \right) + \frac{1}{2} = 1 \quad \Rightarrow \quad a = \frac{1}{\pi}
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[115, 530, 699, 568]]<|/det|>
\[
\text{b) } F(x) = \frac{1}{\pi} \cdot \arctan x + \frac{1}{2} \quad \Rightarrow \quad f(x) = F'(x) = \frac{1}{\pi} \cdot \frac{1}{1+x^2}
\]

<|ref|>sub_title<|/ref|><|det|>[[115, 582, 355, 600]]<|/det|>
4. Exponentialverteilung 

<|ref|>text<|/ref|><|det|>[[115, 598, 789, 634]]<|/det|>
Die Lebensdauer T eines bestimmten elektronischen Bauteils genüge einer
Exponentialverteilung mit der Dichtefunktion 

<|ref|>equation<|/ref|><|det|>[[115, 639, 590, 696]]<|/det|>
\[
f(x) = \begin{cases} \lambda \cdot e^{-\lambda t} & \text{für} \\ 0 & \text{für} \end{cases} \quad t \ge 0 \quad \lambda > 0.
\]

<|ref|>text<|/ref|><|det|>[[115, 700, 875, 740]]<|/det|>
Wie gross ist die Wahrscheinlichkeit dafür, dass ein Bauelement mindestens bis zum
Zeitpunkt \(t = \frac{2}{\lambda}\) funktionstüchtig bleibt? 

<|ref|>equation<|/ref|><|det|>[[122, 757, 675, 806]]<|/det|>
\[
P(0 \le T \le 2\lambda^{-1}) = \lambda \cdot \int_0^{2\lambda^{-1}} e^{-\lambda t} dt = \left[ -e^{-\lambda t} \right]_0^{2\lambda^{-1}} = 1 - e^{-2} = 0,8647
\]

<|ref|>sub_title<|/ref|><|det|>[[115, 820, 500, 839]]<|/det|>
5. Masszahlen einer stetigen Verteilung 

<|ref|>text<|/ref|><|det|>[[115, 837, 789, 874]]<|/det|>
a) Wie gross ist der Erwartungswert der stetigen Zufallsvariablen X mit der
Dichtefunktion \(f(x) = 0,5 \cdot (1 + x)\) für \(-1 \le x \le 1\) und 0 sonst. 

<|ref|>text<|/ref|><|det|>[[115, 871, 872, 923]]<|/det|>
b) Welchen Mittelwert und welche Varianz besitzt eine stetig verteilte Zufallsvariable
X mit der Dichtefunktion \(f(x) = ax^2 \cdot (1 - x)\), \(0 \le x \le 1\), \(a \in \mathbb{R}\) (für alle übrigen x
verschwindet f(x))?