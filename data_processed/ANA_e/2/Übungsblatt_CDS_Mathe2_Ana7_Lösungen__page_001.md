<|ref|>title<|/ref|><|det|>[[115, 183, 476, 217]]<|/det|>
Übungsblatt 7 Ana 

<|ref|>text<|/ref|><|det|>[[577, 197, 880, 231]]<|/det|>
Computational and Data Science
FS2024 

<|ref|>text<|/ref|><|det|>[[115, 250, 270, 278]]<|/det|>
Lösungen 

<|ref|>text<|/ref|><|det|>[[749, 257, 880, 275]]<|/det|>
Mathematik 2 

<|ref|>text<|/ref|><|det|>[[115, 304, 210, 321]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 320, 870, 354]]<|/det|>
- Sie kennen die Begriffe Mehrfachintegral, Integrationsgebiet und ihre wichtigsten Eigenschaften. 

<|ref|>text<|/ref|><|det|>[[115, 353, 787, 387]]<|/det|>
- Sie können für die Vereinfachung von Zweifach- und Dreifachintegralen kartesische Koordinaten in Polar- bzw. Zylinderkoordinaten umwandeln. 

<|ref|>text<|/ref|><|det|>[[115, 386, 855, 419]]<|/det|>
- Sie können Mehrfachintegrale auf einfachen Gebieten in 2D und 3D berechnen und die Integrationsreihenfolge vertauschen. 

<|ref|>text<|/ref|><|det|>[[115, 418, 808, 451]]<|/det|>
- Sie können Masse, Volumen und Schwerpunkt mittels Mehrfachintegralen bestimmen. 

<|ref|>sub_title<|/ref|><|det|>[[115, 485, 463, 502]]<|/det|>
1. Aussagen über Zweifachintegrale 

<|ref|>text<|/ref|><|det|>[[115, 501, 680, 518]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[115, 516, 880, 703]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Ein Zweifachintegral beschreibt das Volumen zwischen dem Graphen einer Funktion \(f: \mathbb{R}^2 \to \mathbb{R}\) und einem Gebiet in der xy-Ebene.</td><td>X</td><td></td></tr><tr><td>b) Die Fläche eines Gebiets in 2D lässt sich mit Hilfe eines Zweifachintegrals berechnen.</td><td>X</td><td></td></tr><tr><td>c) Für \(f(x, y) \ge 0\) gilt: \(\int_G f(x, y) dA \ge 0\) für jedes Gebiet G in der xy-Ebene.</td><td>X</td><td></td></tr><tr><td>d) Für \(f(x, y) \le 0\) gilt: \(\int_{x_0}^{x_E} \int_{y_0}^{y_E} f(x, y) dy dx \le 0\) für alle \(x_0, x_E, y_0, y_E \in \mathbb{R}\).</td><td></td><td>X</td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[115, 718, 384, 735]]<|/det|>
2. Integrale über Rechtecke 

<|ref|>text<|/ref|><|det|>[[115, 735, 468, 752]]<|/det|>
Berechnen Sie die folgenden Integrale. 

<|ref|>equation<|/ref|><|det|>[[115, 751, 860, 805]]<|/det|>
\[
\begin{align*}
a) \int_0^1 \int_0^2 xy \, dx \, dy & \qquad b) \int_0^2 \int_0^1 x^2 \, dx \, dy & \qquad c) \int_0^{\ln 3} \int_0^{\ln 2} e^{2x+y} \, dx \, dy \\
d) \int_0^1 \int_1^e \frac{x^2}{y} \, dy \, dx & \qquad e) \int_1^4 \int_{-1}^2 (2x + 6x^2y) \, dx \, dy & \qquad f) \int_{-1}^2 \int_1^4 (2x + 6x^2y) \, dy \, dx
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[115, 821, 857, 910]]<|/det|>
\[
\begin{align*}
a) \int_0^1 \int_1^2 xy \, dx \, dy &= \int_0^2 x \, dx \cdot \int_0^1 y \, dy = \frac{1}{2} \cdot \left[ x^2 \right]_0^1 \cdot \frac{1}{2} \cdot \left[ y^2 \right]_0^1 = \frac{1}{4} \cdot (2^2 - 0) \cdot (1^2 - 0) \\
&= \frac{1}{4} \cdot 4 \cdot 1 = \frac{1}{2}.
\end{align*}
\]