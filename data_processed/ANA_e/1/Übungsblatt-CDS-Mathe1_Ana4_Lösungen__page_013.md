<|ref|>text<|/ref|><|det|>[[123, 66, 655, 85]]<|/det|>
f) Mit Hilfe der geometrischen Summen-Formel erhalten wir 

<|ref|>equation<|/ref|><|det|>[[149, 95, 920, 192]]<|/det|>
\[
\begin{align*}
\frac{F}{3^k} &= \sum_{k=0}^\infty \frac{2^k}{3^k} = \lim_{n \to \infty} \sum_{k=0}^n \frac{2^k}{3^k} = \lim_{n \to \infty} (\frac{2}{3})^k = \lim_{n \to \infty} G_{(0;n)} (\frac{2}{3}) = \lim_{n \to \infty} \frac{1 - (\frac{2}{3})^{n+1}}{1 - \frac{2}{3}} \\
&= \frac{1 - 0}{\frac{1}{3}} = \frac{3}{2}.
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[110, 213, 345, 230]]<|/det|>
16. Geometrische Reihen 

<|ref|>text<|/ref|><|det|>[[110, 230, 728, 265]]<|/det|>
Wir berechnen, falls möglich, jeweils den Grenzwert der geometrischen
Reihe. 

<|ref|>text<|/ref|><|det|>[[110, 265, 640, 284]]<|/det|>
a) Mit Hilfe der geometrischen Summen-Formel erhalten wir 

<|ref|>equation<|/ref|><|det|>[eq:sum_geometrisch_reihe] 
\[
\frac{G}{3^k} = \sum_{k=1}^\infty \left( \frac{3}{2} \right)^k = \lim_{n \to \infty} \sum_{k=1}^n \left( \frac{3}{2} \right)^k = \lim_{n\to\infty} G_{(1;n)} \left( \frac{3}{2} \right) = \lim_{n\to\infty} \frac{\frac{3}{2} - (\frac{3}{2})^{n+1}}{1 - \frac{3}{2}}.
\]

<|ref|>equation<|/ref|><|det|>[[149, 290, 920, 330]]<|/det|>
\[
\frac{G}{3^k} = \sum_{k=1}^\infty \frac{3^k}{2^k} = \lim_{n \to \infty} \sum_{k=1}^n \frac{3^k}{2^k} = \lim_{n \to \infty} G_{(1;n)} \left( \frac{3}{2} \right)^k = \lim_{n = \infty} \frac{\frac{3}{2} - (\frac{3}{2})^{n + 1}}{1 - \frac{3}{2}}.
\]

<|ref|>text<|/ref|><|det|>[[149, 340, 920, 358]]<|/det|>
Die geometrische Reihe ist offensichtlich divergent, denn \(3/2 > 1\) und für \(n \to \infty\) gilt somit 

<|ref|>equation<|/ref|><|det|>[[152, 368, 920, 410]]<|/det|>
\[
\left( \frac{3}{2} \right)^{n+1} \to \infty. \qquad (68)
\]

<|ref|>text<|/ref|><|det|>[[120, 423, 655, 442]]<|/det|>
b) Mit Hilfe der geometrischen Summen-Formel erhalten wir 

<|ref|>equation<|/ref|><|det|> [[149, 451, 920, 496]]<|/det|>
\[
\frac{H}{3^k} = \sum_{k=0}^\infty (-1)^k = \lim_{n \to \infty} \sum_{k=0}^n (-1)^k = \lim_{n \to \infty} G_{(0;n)} (-1) = \lim_{n \to \infty} \frac{1 - (-1)^{n+1}}{1 - (-1)}. \quad (69)
\]

<|ref|>text<|/ref|><|det|>[[149, 510, 920, 546]]<|/det|>
Die geometrische Reihe ist offensichtlich divergent, weil die Folge \((-1)^{n+1}\) für \(n \to \infty\) divergiert, indem sie zwischen den Werten \(-1\) und \(1\) hin und her springt. 

<|ref|>text<|/ref|><|det|>[[120, 554, 655, 572]]<|/det|>
c) Mit Hilfe der geometrischen Summen-Formel erhalten wir 

<|ref|>equation<|/ref|><|det|>((eq:sum_geometrisch_reihe)) 
\[
\frac{I}{3^k} = \sum_{k=1}^\infty \frac{(-1)^k}{3^k} = \lim_{n \to \infty} \sum_{k=1}^\infty \frac{(-1)^k}{3^k}
\]

<|ref|>equation<|/ref|><|det|>[[149, 580, 920, 682]]<|/det|>
\[
\begin{align*}
I &= \sum_{k=1}^\infty \frac{(-1)^k}{3^k}\\
&= \lim_{n \to \infty} \sum_{k=1}^n \frac{\left(-1\right)^k}{3^k}\\
&= \lim_{n \to \infty} G_{(1;n)} \left( \left( \frac{-1}{3} \right)^k \right)\\
&= \lim_{n \to \infty} \frac{\frac{1}{3} - \left( \frac{-1}{3} \right)^{n+1}}{1 - \left( \frac{-1}{3} \right)} = \frac{\frac{1}{3} - 0}{\frac{1}{3} + \frac{1}{3}} = \frac{\frac{1}{3}}{\frac{4}{3}} = \frac{1}{3} \cdot \frac{3}{4} = \frac{1}{4}.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[120, 700, 655, 718]]<|/det|>
d) Mit Hilfe der geometrischen Summen-Formel erhalten wir 

<|ref|>equation<|/ref|><|det|>["eq:sum_geometrisch_reihe"] 
\[
\frac{J}{3^k} = \sum_{k=0}^\infty \frac{1}{3^{3k}} = \lim_{n \to \infty} \sum_{k=0}^n \left( \frac{1}{3^{3k}} \right) = \lim_{n \to \infty} \sum_{k=0}^n \sum_{k=0}^n \left( \frac{1}{27} \right)^k = \lim_{n \to \infty} G_{(0;n)} \left( \frac{1}{27} \right)
\]

<|ref|>equation<|/ref|><|det|>[[149, 726, 920, 825]]<|/det|>
\[
\begin{align*}
J &= \sum_{k=0}^\infty \frac{1}{3^{3k}} \\
&= \lim_{n \to \infty} \sum_{k=0}^n \frac{\frac{1}{3^{3k}}}{\frac{1}{27}} \\
&= \lim_{n \to \infty} \frac{\frac{1}{3^{3k}}}{\frac{1}{27}} = \lim_{n \to \infty} \frac{\frac{1}{3^{3n+1}}}{\frac{1}{27}} = \frac{1 - 0}{\frac{26}{27}} = \frac{27}{26} \approx 1.039. \tag{71}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[120, 842, 655, 860]]<|/det|>
e) Mit Hilfe der geometrischen Summen-Formel erhalten wir 

<|ref|>equation<|/ref|><|det|>[][] 
\[
\frac{K}{3^k} = \sum_{k=1}^\infty \sqrt{\frac{3}{2^k}} = \lim_{n \to \infty} \sum_{k=1}^n \sqrt{\frac{3}{2^k}} = \lim_{n \to \infty}\sum_{k=1}^n \frac{\sqrt{3}}{\sqrt{2^k}} = \lim_{n \to \infty} \sqrt{3} \sum_{k=1}^n \frac{1}{\left(\sqrt{2}\right)^k}
\]