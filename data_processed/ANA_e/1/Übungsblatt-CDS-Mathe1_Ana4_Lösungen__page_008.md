<|ref|>text<|/ref|><|det|>[[132, 66, 285, 85]]<|/det|>
iv) Wir erhalten 

<|ref|>equation<|/ref|><|det|>[[162, 92, 784, 198]]<|/det|>
\[
\begin{align*}
\sum_{k=2}^{11} \left( \frac{1}{2} \right)^k &= G_{(2;11)} \left( \frac{1}{2} \right) = \frac{\left( \frac{1}{2} \right)^2 - \left( \frac{1}{2} \right)^{11+1}}{1 - \frac{1}{2}} = \frac{\frac{1}{2^2} - \frac{1}{2^{12}}}{1/2} = 2 \cdot \left( \frac{1}{2^2} - \frac{1}{2^{12}} \right) \\
&= \frac{1}{2} - \frac{1}{2^{11}} = \frac{2^{10}}{2^{11}} - \frac{1}{2^{11}} = \frac{2^{10} - 1}{2^{11}} = \frac{1'024 - 1}{2'048} = \frac{1'023}{2'048}. \tag{39}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[92, 211, 716, 230]]<|/det|>
f) Wir betrachten geometrische Summen für die Fälle \(x = 0\) und \(x = 1\). 

<|ref|>text<|/ref|><|det|>[[118, 234, 888, 286]]<|/det|>
Fall 1: \(x = 0\). Wird in diesem Fall \(m = 0\) gewählt, dann kann die Formel aus (22) nicht angewendet werden, weil darin der nicht definierte Term \(0^0\) auftritt. Formal erhalten wir nämlich 

<|ref|>equation<|/ref|><|det|>[[360, 291, 888, 329]]<|/det|>
\[
G_{(0;n)}(0) := \underbrace{0^0}_{=?} + 0^1 + \ldots + 0^n = ? \quad (40)
\]

<|ref|>text<|/ref|><|det|>[[118, 336, 888, 372]]<|/det|>
Fall 2: \(x = 1\). In diesem Fall kann die geometrische Summen-Formel aus (35) nicht angewendet werden, weil der Nenner \((1 - x)\) nicht verschwinden darf. 

<|ref|>text<|/ref|><|det|>[[118, 375, 888, 412]]<|/det|>
Um diese Schwierigkeiten zu vermeiden, wurde bei der Definition der geometrischen Summe in (22) sinnvollerweise die Bedingung \(x \notin \{0, 1\}\) vorausgesetzt. 

<|ref|>sub_title<|/ref|><|det|>[[75, 432, 456, 450]]<|/det|>
9. Aussagen über geometrische Summen 

<|ref|>text<|/ref|><|det|>[[75, 450, 515, 470]]<|/det|>
Es seien \(x, y \in \mathbb{R} \setminus \{0, 1\}\) und \(m, n \in \mathbb{N}^+\) mit \(m < n\). 

<|ref|>table<|/ref|><|det|>[[75, 480, 888, 662]]<|/det|>
<table><tr><td>Welche der folgenden Aussagen sind wahr und welche falsch?</td><td>wahr</td><td>falsch</td></tr><tr><td>a) In jedem Fall gilt \(G_{(0;n)}(x + y) \in \mathbb{R}\).</td><td>○</td><td>●</td></tr><tr><td>b) In jedem Fall gilt \(G_{(10;30)}(x) = G_{(10;20)}(x) + G_{(20;30)}(x)\).</td><td>○</td><td>●</td></tr><tr><td>c) In jedem Fall gilt \(G_{(m;n)}(x + y) = G_{(m;n)}(x) + G_{(m;n)}(y)\).</td><td>○</td><td>●</td></tr><tr><td>d) In jedem Fall gilt \(G_{(m;n)}(y) < G_{(m;n+1)}(y)\).</td><td>○</td><td>●</td></tr><tr><td>e) In jedem Fall gilt \(G_{(m+7;n+7)}(x) = x^7 \cdot G_{(m;n)}(x)\).</td><td>●</td><td>○</td></tr><tr><td>f) In jedem Fall gilt \(G_{(m;n)}(x^2) = G_{(2m;2n)}(x)\).</td><td>○</td><td>●</td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[78, 682, 430, 699]]<|/det|>
10. Geometrische Summen berechnen 

<|ref|>text<|/ref|><|det|>[[75, 700, 543, 718]]<|/det|>
Wir berechnen die folgenden geometrischen Summen. 

<|ref|>text<|/ref|><|det|>[[75, 718, 175, 736]]<|/det|>
a) Es gilt 

<|ref|>equation<|/ref|><|det|>[[118, 748, 888, 794]]<|/det|>
\[
\frac{A}{k} = \sum_{k=0}^{12} 2^k = G_{(0;12)}(2) = \frac{2^0 - 2^{12+1}}{1-2} = \frac{1-8'192}{1-2} = \frac{-8'191}{-1} = \frac{8'191}{-1}. \quad (41)
\]

<|ref|>text<|/ref|><|det|>[[92, 803, 192, 822]]<|/det|>
b) Es gilt 

<|ref|>equation<|/ref|><|det|>[[118, 830, 742, 922]]<|/det|>
\[
\begin{align*}
B &= \sum_{k=1}^{10} 2 \cdot 3^k = 2 \sum_{k=1}^{10} 3^k = 2 G_{(1;10)}(3) = 2 \cdot \frac{3^1 - 3^{10+1}}{1-3} = 2 \cdot \frac{3 - 177'147}{1-3} \\
&= 2 \cdot \frac{-177'144}{-2} = 177'144.
\end{align*}
\]