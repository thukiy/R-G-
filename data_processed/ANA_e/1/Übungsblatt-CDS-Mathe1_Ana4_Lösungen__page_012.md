<|ref|>sub_title<|/ref|><|det|>[[77, 66, 315, 84]]<|/det|>
## 15. Geometrische Reihen 

<|ref|>text<|/ref|><|det|>[[74, 84, 692, 118]]<|/det|>
Wir berechnen, falls möglich, jeweils den Grenzwert der geometrischen Reihe. 

<|ref|>text<|/ref|><|det|>[[74, 118, 607, 137]]<|/det|>
a) Mit Hilfe der geometrischen Summen-Formel erhalten wir 

<|ref|>equation<|/ref|><|det|>[[115, 135, 800, 230]]<|/det|>
\[
\begin{align*}
\underline{A} &= \sum_{k=0}^{\infty} \frac{1}{2^k} = \lim_{n \to \infty} \sum_{k=0}^{n} \frac{1}{2^k} = \lim_{n \to \infty} G_{(0;n)} \left( \frac{1}{2} \right)^k = \lim_{n \to \infty} \frac{1 - \left( \frac{1}{2} \right)^{n+1}}{1 - \frac{1}{2}} \\
&= \lim_{n \to \infty} \frac{1 - \frac{1}{2^{n+1}}}{\frac{1}{2}} = \frac{1 - 0}{\frac{1}{2}} = \underline{2}.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[87, 239, 622, 258]]<|/det|>
b) Wir zeigen zwei Varianten, um diese Teilaufgabe zu lösen. 

<|ref|>text<|/ref|><|det|>[[110, 261, 732, 280]]<|/det|>
Variante 1: Mit Hilfe der geometrischen Summen-Formel erhalten wir 

<|ref|>equation<|/ref|><|det|>[[142, 286, 836, 383]]<|/det|>
\[
\begin{align*}
\underline{B} &= \sum_{k=1}^{\infty} \frac{1}{2^k} = \lim_{n \to \infin} \sum_{k=1}^{n} \frac{1}{2^k} = \lim_{n \to \infin \atop k=1} G_{(1;n)} \left( \frac{1}{2} \right)^k = \frac{\lim_{n \to \infin} \frac{1}{2} - \left( \frac{1}{2} \right)^{n+1}}{1-\frac{1}{2}} \\
&= \lim_{n \to \infin} \frac{\frac{1}{2} - \frac{1}{2^{n+1}}}{\frac{1}{2}} - \frac{1}{2} = \underline{1}.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[110, 390, 715, 410]]<|/det|>
Variante 2: Mit Hilfe des Resultates aus Teilaufgabe a) erhalten wir 

<|ref|>equation<|/ref|><|det|>[[142, 417, 835, 464]]<|/det|>
\[
\underline{B} = \sum_{k=1}^{\infty} \frac{1}{2^k} = \sum_{k=0}^{\infty} \frac{1}{2^k} - \frac{1}{2^0} = 2 - \frac{1}{1} = 2 - 1 = \underline{1}.
\]

<|ref|>text<|/ref|><|det|>[[87, 472, 608, 492]]<|/det|>
c) Mit Hilfe des Resultates aus Teilaufgabe b) erhalten wir 

<|ref|>equation<|/ref|><|det|>[[110, 499, 835, 547]]<|/det|>
\[
\underline{C} = \sum_{k=2}^{\infty} \frac{1}{2^k} = \sum_{k=1}^{\infty} \frac{1}{2^k} - \frac{1}{2^1} = 1 - \frac{1}{2} = \frac{1}{2}.
\]

<|ref|>text<|/ref|><|det|>[[87, 556, 621, 576]]<|/det|>
d) Mit Hilfe der geometrischen Summen-Formel erhalten wir 

<|ref|>equation<|/ref|><|det|>[1][2][3]{\frac{1}{3}} = 2 \lim_{n \to \infty} \sum_{k=0}^{n} \left( \frac{1}{3} \right)^k = 2 \lim_{n \to \infty} G_{(0;n)} \left( \left( \frac{1}{3} \right)^k \right) = 2 \lim_{n \to \infty} G_{(0;n)} \frac{1}{3} = 2 \lim_{n \to \infty} G_{(0;n)} \cdot \frac{1}{3} = 2 \lim_{n \to \infty} \frac{1}{3} = 2 \lim_{n \to \infty} 1 = 2 \lim_{n \to \infty} \frac{1}{3} \cdot \frac{1}{3} = 2 \lim_{n \to \infin} \frac{1}{3} = 2 \lim_{n \to \infin \atop k=0} \frac{1}{3} = 2 \lim_{n \to \in fin} \frac{1}{3} = 2 \lim_{n \to \in f i n} \frac{1}{3} = 2 \lim_{n \to \in \infty} \frac{1}{3} = 2 \lim_{n \to 0} \frac{1}{3} = 2 \lim_{n \to 0 \atop k=0} \frac{1}{3} = 2 \lim \frac{1}{3} = 2 \lim_{n \to \in f n} \frac{1}{3} = 2 \lim_{n \to \infty \atop k=0} \frac{1}{3} = 2 \lim 1 = 2 \lim_{n \to \infty} \frac{1}{n} = 2 \lim_{n \to \infty} \frac{1}{n} \cdot \frac{1}{n} = 2 \lim_{n \to \infty} 1 = 2 \cdot \frac{1}{n} = 2 \cdot \frac{1}{n} = 2 \cdot \frac{n}{n} = 2 \cdot \frac{1}{n} = 2 \lim_{n \to \in f n} \frac{1}{\frac{1}{n}} = 2 \lim_{n \to \in f n} \frac{1}{n} = 2 \lim_{n \to \in f \infty} \frac{1}{n} = 2 \lim_{n \to 0} \frac{1}{n} = 2 \lim_{n \to 0 \atop k=0} 1 = 2 \lim_{n \to 0 \atop k=0} \left( \frac{1}{3} \right)^k = 2 \cdot \frac{1}{n} = 2 \cdot \frac{\frac{1}{3}}{n} = 2 \cdot \frac{1}{n} = 2 \cdot 1 = 2 \cdot \frac{1}{n} = 2 \cdot 1 \cdot \frac{1}{n} = 2 \cdot 1 \cdot \left( \frac{1}{3} \right) = 2 \cdot \frac{1}{n} = 2 \cdot \frac {1}{n} = 2 \cdot \frac{1}{n} = 2. \quad (63)
\]

<|ref|>text<|/ref|><|det|>[[87, 691, 621, 711]]<|/det|>
e) Wir zeigen zwei Varianten, um diese Teilaufgabe zu lösen. 

<|ref|>text</td><td>Variante 1: Mit Hilfe der geometrischen Summen-Formel erhalten wir</td><td></td></tr></table>