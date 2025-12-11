<|ref|>sub_title<|/ref|><|det|>[[114, 81, 545, 99]]<|/det|>
## 3. Aussagen über den Binomialkoeffizienten 

<|ref|>text<|/ref|><|det|>[[114, 98, 680, 116]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[114, 113, 880, 240]]<|/det|>
<table><tr><td></td><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Jeder Binomialkoeffizient \( \binom{n}{k} \) ist eine natürliche Zahl.</td><td>X</td><td></td><td></td></tr><tr><td>b) Verdoppelt man sowohl \( n \) als auch \( k \), dann ändert sich der Wert des Binomialkoeffizienten nicht.</td><td></td><td>X</td><td></td></tr><tr><td>c) Ersetzt man \( k \) durch \( n-k \), dann ändert sich der Wert des Binomialkoeffizienten nicht.</td><tr><td></td><td>X</td><td></td><td></td></tr></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[114, 254, 460, 273]]<|/det|>
## 4. Binomialkoeffizienten berechnen 

<|ref|>equation<|/ref|><|det|>[[114, 271, 723, 390]]<|/det|>
\[
\begin{align*}
a) \binom{3}{2} \quad & b) \binom{2}{3} \quad & c) \binom{7}{5} \\
d) \binom{7}{2} \quad & e) \binom{871}{1} \quad & f) \binom{935}{934}
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[114, 353, 470, 390]]<|/det|>
\[
g) \binom{100}{4} \quad h) \binom{100}{5}
\]

<|ref|>text<|/ref|><|det|>[[122, 405, 875, 425]]<|/det|>
a) Wir zeigen mehrere Varianten, um den gesuchten Binomialkoeffizienten zu berechnen 

<|ref|>text<|/ref|><|det|>[[150, 427, 675, 446]]<|/det|>
Variante 1: Aufgrund der Struktur des PASCAL-Dreiecks gilt 

<|ref|>equation<|/ref|><|det|>[[178, 456, 368, 499]]<|/det|>
\[
\frac{\binom{3}{2}}{\binom{2}{2}} = \binom{3}{3-1} = \frac{3}{2}
\]

<|ref|>text<|/ref|><|det|>[[150, 514, 680, 533]]<|/det|>
Variante 2: Gemäss Definition der Binomialkoeffizienten gilt 

<|ref|>equation<|/ref|><|det|>[[178, 543, 506, 586]]<|/det|>
\[
\frac{\binom{3}{2}}{\binom{2}{2}} \quad = \quad \frac{3!}{2! \cdot (3-2)!} = \frac{2! \cdot 3}{2! \cdot 1!} = \frac{3}{1} = \frac{3}{2}
\]

<|ref|>text<|/ref|><|det|>[[122, 604, 428, 623]]<|/det|>
b) Binomialkoeffizienten der Form 

<|ref|>equation<|/ref|><|det|>[[154, 633, 206, 675]]<|/det|>
\[
\binom{n}{k}
\]

<|ref|>text<|/ref|><|det|>[[150, 682, 875, 715]]<|/det|>
sind nur definiert für \(n, k \in \mathbb{N}\) mit \(k \le n\). Die letzte Voraussetzung ist im vorliegenden Fall mit \(n = 2\) und \(k = 3\) nicht erfüllt. 

<|ref|>text<|/ref|><|det|>[[122, 721, 580, 740]]<|/det|>
c) Gemäss Definition der Binomialkoeffizienten gilt 

<|ref|>equation<|/ref|><|det|>[[154, 750, 605, 792]]<|/det|>
\[
\frac{\binom{7}{5}}{\binom{5}{5}} = \frac{7!}{5! \cdot (7-5)!} = \frac{5! \cdot 6 \cdot 7}{5! \cdot 2!} = \frac{6 \cdot 7}{2} = \frac{3 \cdot 7}{1} = 21.
\]

<|ref|>text<|/ref|><|det|>[[122, 813, 872, 852]]<|/det|>
d) Wir zeigen mehrere Varianten, um den gesuchten Binomialkoeffizienten zur berechnen
Variante 1: Mit Hilfe von (35) erhalten wir 

<|ref|>equation<|/ref|><|det|>[[184, 861, 457, 905]]<|/det|>
\[
\frac{\binom{7}{2}}{\binom{2}{2}} = \binom{7}{7-2} = \binom{7}{5} = 21.
\]