<|ref|>text<|/ref|><|det|>[[115, 81, 580, 100]]<|/det|>
Charakteristisches Polynom hat 2 reelle Nullstellen: 

<|ref|>equation<|/ref|><|det|>[[122, 100, 766, 175]]<|/det|>
\[
\begin{align*}
\lambda_{1,2} &= \frac{-b \pm \sqrt{D}}{2 \cdot a} = \frac{-7 \pm \sqrt{25}}{2 \cdot 2} = \frac{-7 \pm 5}{4} \\
\lambda_1 &= \frac{-7 - 5}{4} = \frac{-12}{4} = -3 \quad \text{und} \quad \lambda_2 = \frac{-7 + 5}{4} = \frac{-2}{4} = -\frac{1}{2} = -0.5
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 175, 511, 194]]<|/det|>
Es ergeben sich die reellen Basislösungen: 

<|ref|>equation<|/ref|><|det|>[[122, 194, 653, 218]]<|/det|>
\[
y_1(x) = e^{\lambda_1 x} = e^{-3x} \quad \text{und} \quad y_2(x) = e^{\lambda_2 x} = e^{-0.5x}.
\]

<|ref|>text<|/ref|><|det|>[[115, 218, 299, 236]]<|/det|>
Allgemeine Lösung: 

<|ref|>equation<|/ref|><|det|>[[122, 236, 660, 265]]<|/det|>
\[
\frac{y(x)}{y(1)} = C_1 \cdot y_1(x) + C_2 \cdot y_2(x) = \frac{C_1}{1} e^{-3x} + \frac{C_2}{2} e^{-0.5x}.
\]

<|ref|>sub_title<|/ref|><|det|>[[115, 285, 465, 303]]<|/det|>
5. AWP mit linear inhomogener DGL 

<|ref|>text<|/ref|><|det|>[[115, 302, 415, 320]]<|/det|>
Gegeben sei das folgende AWP: 

<|ref|>equation<|/ref|><|det|>[[115, 319, 327, 339]]<|/det|>
\[
DGL: y' - 2y' + y = 0
\]

<|ref|>equation<|/ref|><|det|>[[115, 337, 239, 355]]<|/det|>
\[
AB: y(1) = 3
\]

<|ref|>equation<|/ref|><|det|>[[155, 355, 250, 374]]<|/det|>
\[
y'(1) = 0.
\]

<|ref|>text<|/ref|><|det|>[[115, 387, 680, 405]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[115, 404, 880, 526]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Die Lösung des AWP ist reell.</td><td>X</td><td></td></tr><tr><td>b) Die Lösung des AWP oszilliert.</td><td></td><td>X</td></tr><tr><td>c) Die Lösung des AWP hat eine Nullstelle bei x = 1.</td><td></td><td>X</td></tr><tr><td>d) Für die Lösung des AWP gilt: \(y''(1) < 0\).</td><td>X</td><td></td></tr><tr><td>e) Für die Lösung des AWP gilt: \(y(x) \to \infty\) für \(x \to \infty\).</td><td></td><td>X</td></tr><tr><td>f) Die Lösung des AWP ist nach oben beschränkt.</td><td>X</td><td></td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[115, 541, 567, 559]]<|/det|>
6. AWP mit linear homogenen DGL 2. Ordnung 

<|ref|>text<|/ref|><|det|>[[115, 558, 840, 608]]<|/det|>
Bestimmen Sie die Lösung des gegebenen AWP mit Hilfe des charakteristischen
Polynoms und beurteilen Sie das Verhalten für grosse Werte der unabhängigen
Variablen. 

<|ref|>equation<|/ref|><|det|>[[115, 607, 707, 626]]<|/det|>
a) DGL: \(y' + 4y' + 5y = 0\) b) DGL: \(y'' + 20y' + 64y = 0\)

<|ref|>equation<|/ref|><|det|>[[139, 625, 590, 644]]<|/det|>
\[
AB: y(0) = \pi \quad \text{AB: } y(0) = 0
\]

<|ref|>equation<|/ref|><|det|>[[170, 643, 592, 662]]<|/det|>
\[
y'(0) = 0. \quad y'(0) = 2.
\]

<|ref|>equation<|/ref|><|det|>[[115, 660, 686, 680]]<|/det|>
c) DGL: \(4y' - 4y' + y = 0\) d) DGL: \(4y'' - 4y' + y = 0\)

<|ref|>equation<|/ref|><|det|>[[139, 678, 596, 697]]<|/det|>
\[
AB: y(0) = 5 \quad \text{AB: } y(2) = 5
\]

<|ref|>equation<|/ref|><|det|>[[170, 696, 610, 715]]<|/det|>
\[
y'(0) = -1. \quad y'(2) = -1.
\]

<|ref|>text<|/ref|><|det|>[[115, 729, 147, 745]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[115, 744, 548, 763]]<|/det|>
Charakteristisches Polynom: \(p(\lambda) = \lambda^2 + 4\lambda + 5\) 

<|ref|>text<|/ref|><|det|>[[115, 762, 345, 779]]<|/det|>
Diskriminante: \(D = -4 < 0\) 

<|ref|>text<|/ref|><|det|>[[115, 778, 790, 813]]<|/det|>
Da die ABs beide reell sind, muss auch die Lösung des AWP reell sein. Wir
bestimmen die gedämpfte Kreisfrequenz und die Dämpfungskonstante 

<|ref|>equation<|/ref|><|det|>[[122, 812, 460, 853]]<|/det|>
\[
\omega_d = \frac{\sqrt{|D|}}{2 \cdot a} = \frac{\sqrt{| -4|}}{2 \cdot 1} = \frac{\sqrt{4}}{2} = \frac{2}{2} = 1
\]

<|ref|>equation<|/ref|><|det|>[[130, 860, 325, 896]]<|/det|>
\[
\delta = \frac{b}{2 \cdot a} = \frac{4}{2 \cdot 1} = 2.
\]

<|ref|>equation<|/ref|><|det|>[[115, 896, 250, 914]]<|/det|>
\[
A = C = y_0 = \pi
\]