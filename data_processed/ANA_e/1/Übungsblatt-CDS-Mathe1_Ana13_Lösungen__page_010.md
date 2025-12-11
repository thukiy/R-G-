<|ref|>text<|/ref|><|det|>[[90, 65, 890, 102]]<|/det|>
c) Die Fläche innerhalb des Torbogens oberhalb der Türe soll \(C \approx 1.00 \text{ m}^2\) betragen. In diesem Fall muss gelten 

<|ref|>equation<|/ref|><|det|>[[117, 111, 888, 250]]<|/det|>
\[
\begin{align*}
C &= \int_{-b/2}^{b/2} f(x) \, \mathrm{d}x - A = 2 \int_0^{b/2} f(x) \, \mathrm{d}x - b \cdot h = 2 \int_0^{b/2} (c - a \cdot x^2) \, \mathrm{d}x - b \cdot h \\
&= 2 \cdot \left( c \cdot x - \frac{a}{3} \cdot x^3 \right) \Big|_0^{b/2} - b \cdot h = 2 \cdot c \cdot \frac{b}{2} - 2 \cdot \frac{a}{3} \cdot \left( \frac{b}{2} \right)^3 - b \cdot \left( c - \frac{a}{4} \cdot b^2 \right) \\
&= c \cdot b - 2 \cdot \frac{a}{3} \cdot \frac{b^3}{8} - b \cdot c + \frac{a}{4} \cdot b^3 = \left( -\frac{1}{12} + \frac{1}{4} \right) \cdot a \cdot b^3 = \frac{2}{12} \cdot a \cdot b^3 = \frac{a}{6} \cdot b^3. \tag{111}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[117, 258, 490, 278]]<|/det|>
Die Breite b erfüllt demnach die Gleichung 

<|ref|>equation<|/ref|><|det|>[[440, 288, 888, 323]]<|/det|>
\[
C = \frac{a}{6} \cdot b^3 \qquad \left| \frac{6}{a} \right. \tag{112}
\]

<|ref|>equation<|/ref|><|det|>[[262, 333, 888, 368]]<|/det|>
\[
\Leftrightarrow \qquad \frac{6C}{a} = b^3 \qquad \left| \sqrt[3]{\cdots} \right. \tag{113}
\]

<|ref|>text<|/ref|><|det|>[[117, 376, 298, 394]]<|/det|>
Daraus erhalten wir 

<|ref|>equation<|/ref|><|det|>[[117, 403, 888, 520]]<|/det|>
\[
\begin{align*}
b &= \sqrt[3]{\frac{6C}{a}} \approx \sqrt[3]{\frac{6 \cdot 1.00 \text{ m}^2}{\frac{4.00}{9.00 \text{ m}}}} = \sqrt[3]{\frac{6 \cdot 9.00 \text{ m}^3}{4.00}} = \sqrt[3]{13.5 \text{ m}^3} \approx 2.38 \text{ m} \tag{114} \\
\underline{h} &= c - \frac{a}{4} \cdot b^2 \approx 4.00 \text{ m} - \frac{4.00}{4} \cdot \left( \sqrt[3]{13.5 \text{ m}^3} \right)^2 = 4.00 \text{ m} - \frac{1}{9.00 \text{ m}} \cdot (13.5 \text{ m}^3)^{2/3} \\
&\approx 3.37 \text{ m}. \tag{115}
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[74, 550, 515, 568]]<|/det|>
5. Aussagen über das Verhalten einer Funktion 

<|ref|>text<|/ref|><|det|>[[74, 568, 330, 586]]<|/det|>
Wir betrachten die Funktion 

<|ref|>equation<|/ref|><|det|>[[356, 595, 888, 636]]<|/det|>
\[
\begin{align*}
f : \mathbb{R} &\to \mathbb{R} \\
x &\mapsto f(x) := \mathrm{e}^x \cdot (x - 1).
\end{align*}
\tag{116}
\]

<|ref|>table<|/ref|><|det|>[[74, 648, 888, 820]]<|/det|>
<table><tr><td>Welche der folgenden Aussagen sind wahr und welche falsch?</td><td>wahr</td><td>falsch</td></tr><tr><td>b) Die Funktion f hat genau eine Wendestelle.</td><td>●</td><td>○</td></tr><tr><td>c) Die Funktion f ist injektiv.</td><td>○</td><td>●</td></tr><tr><td>d) Die Funktion f' hat bei x = -1 ein lokales Minimum.</td><td>●</td><td>○</td></tr><tr><td>e) Die Funktion g(x) := eˣ+1 · (x - 1) fällt nirgends steiler ab als mit einem Winkel von 45°.</td><td>●</td><td>○</td></tr><tr><td>f) Für alle x ∈ ℝ gilt f(x) ≥ -1.</td><td>●</td><td>○</td></tr></table>