<|ref|>text<|/ref|><|det|>[[73, 65, 748, 86]]<|/det|>
S2 Rand stellen: An den Randstellen \(x_0 = 0\) und \(x_E = U/2\) hat \(A\) die Werte 

<|ref|>equation<|/ref|><|det|>[[127, 95, 888, 175]]<|/det|>
\[
\begin{align*}
A_0 &= A(x_0) = A(0) = 0 \cdot \left( \frac{U}{2} - 0 \right) = 0 \cdot \frac{U}{2} = 0 \tag{81} \\
A_E &= A(x_E) = A\left(\frac{U}{2}\right) = \frac{U}{2} \left(\frac{U}{2} - \frac{U}{2}\right) = \frac{U}{2} \cdot 0 = 0.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[73, 189, 858, 209]]<|/det|>
S3 Kandidatenergül eich: Wir stellen die Ergebnisse in der folgenden Tabelle zusammen. 

<|ref|>table<|/ref|><|det|>[[336, 219, 670, 316]]<|/det|>
<table><tr><td>k</td><td>xk</td><td>Ak</td><td>Typ</td></tr><tr><td>0</td><td>0</td><td>0</td><td>globales Minimum</td></tr><tr><td>1</td><td>U/4</td><td>U²/16</td><td>globales Maximum</td></tr><tr><td>E</td><td>U/2</td><td>0</td><td>globales Minimum</td></tr></table>

<|ref|>text<|/ref|><|det|>[[73, 334, 820, 354]]<|/det|>
Ein Rechteck mit Umfang \(U > 0\) hat also gerade dann die maximale Fläche, wenn gilt 

<|ref|>equation<|/ref|><|det|>[[77, 363, 888, 400]]<|/det|>
\[
\frac{a}{x} = x_1 = \frac{U}{\frac{4}{4}} \tag{83}
\]

<|ref|>equation<|/ref|><|det|>[[77, 411, 888, 450]]<|/det|>
\[
\frac{b}{2} = \frac{U}{2} - a = \frac{U}{2} - \frac{U}{4} = \frac{U}{4} = a \tag{84}
\]

<|ref|>equation<|/ref|><|det|>[[73, 460, 888, 504]]<|/det|>
\[
\frac{A}{16} = \frac{U^2}{16} \quad (85)
\]

<|ref|>text<|/ref|><|det|>[[73, 518, 740, 538]]<|/det|>
Dies beschreibt gerade das Quadrat mit Umfang \(U\) und Seitenlänge \(l = U/4\). 

<|ref|>sub_title<|/ref|><|det|>[[73, 565, 316, 583]]<|/det|>
6. Optimale Verpackungen 

<|ref|>text<|/ref|><|det|>[[73, 582, 895, 619]]<|/det|>
Wir bestimmen jeweils die optimalen geometrischen Abmessungen (Länge, Breite, Höhe, Radius,
etc..), so dass die angegebene Verpackung mit möglichst wenig Material hergestellt werden kann. 

<|ref|>text<|/ref|><|det|>[[88, 626, 890, 674]]<|/det|>
a) Wir betrachten eine quaderförmige Kiste mit Länge L, Breite B und Höhe H, die ein
Volumen fasst von 

<|ref|>equation<|/ref|><|det|>[[117, 683, 888, 703]]<|/det|>
\[
V = LBH = 9.001 = 9.00 \text{ dm}^3. \tag{86}
\]

<|ref|>text<|/ref|><|det|>[[117, 713, 721, 732]]<|/det|>
Ihre rechteckige Grundfläche sei doppelt so lang wie breit, d.h. es gilt 

<|ref|>equation<|/ref|><|det|>[[117, 741, 888, 760]]<|/det|>
\[
L = 2B. \tag{87}
\]

<|ref|>text<|/ref|><|det|>[[117, 770, 825, 789]]<|/det|>
Zunächst formulieren wir die Aufgabe als Optimierungsproblem. Dazu wählen wir 

<|ref|>equation<|/ref|><|det|>[[125, 796, 888, 815]]<|/det|>
\[
x := L \qquad (\text{unabhängige Variable}) \tag{88}
\]

<|ref|>equation<|/ref|><|det|>[[125, 820, 888, 839]]<|/det|>
\[
A := \text{Oberfläche der Kiste} \quad (\text{zu optimierende Variable}). \tag{88}
\]

<|ref|>text<|/ref|><|det|>[[117, 849, 888, 886]]<|/det|>
Wir drücken nun sämtliche Variablen des Problems durch die unabhängige Variable x aus.
Mit Hilfe von (86) und (87) erhalten wir 

<|ref|>equation<|/ref|><|det|>[[125, 898, 888, 917]]<|/det|>
\[
L(x) = x \tag{89}
\]