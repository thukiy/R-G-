<|ref|>text<|/ref|><|det|>[[88, 65, 775, 85]]<|/det|>
b) Während dieser 10 Jahre wurde insgesamt eine Lohnsumme ausbezahlt von 

<|ref|>equation<|/ref|><|det|>[[117, 95, 884, 214]]<|/det|>
\[
\begin{align*}
\underline{S} &= \sum_{k=0}^{9} 12 \cdot L_k = \sum_{k=0}^{9} 12 \cdot a^k \cdot L_0 = 12 \cdot L_0 \sum_{k=0}^{9} a^k = 12 \cdot L_0 \cdot G_{(0;9)}(a) = 12 \cdot L_0 \cdot \frac{a^0 - a^{9+1}}{1-a} \\
&= 12 \cdot L_0 \cdot \frac{1-a^{10}}{-i} = 12 \cdot \frac{a^{10}-1}{i} \cdot L_0 = 12 \cdot \frac{1.02^{10}-1}{0.02} \cdot 4'000 \text{ CHF} \\
&\approx 525'586.61 \text{ CHF}.
\end{align*}
\] 

<|ref|>text<|/ref|><|det|>[[844, 197, 888, 214]]<|/det|>
(49) 

<|ref|>sub_title<|/ref|><|det|>[[77, 245, 558, 263]]<|/det|>
12. Anwendung der geometrischen Summen-Formel 

<|ref|>text<|/ref|><|det|>[[77, 262, 830, 296]]<|/det|>
Es sei \(x \in \mathbb{R} \setminus \{-1, 0, 1\}\). Wir berechnen die folgenden Terme mit Hilfe der geometrischen
Summen-Formel. 

<|ref|>text<|/ref|><|det|>[[83, 301, 181, 319]]<|/det|>
a) Es gilt 

<|ref|>equation<|/ref|><|det|>[[115, 330, 800, 525]]<|/det|>
\[
\begin{align*}
\underline{G} &= 1 + \frac{\sqrt{3}}{4} + \frac{3}{16} + \frac{3\sqrt{3}}{64} = \sum_{k=0}^{3} \left(\frac{\sqrt{3}}{4}\right)^k = G_{(0;3)} \left(\frac{\sqrt{3}}{4}\right)^0 - \left(\frac{\sqrt{3}}{4}\right)^{3+1} \\
&= \frac{1 - \left(\frac{\sqrt{3}}{4}\right)^4}{\frac{4-\sqrt{3}}{4}} = \frac{4}{4-\sqrt{3}} \cdot \left(1 - \left(\frac{\sqrt{3}}{4}\right)^{2.2}\right) = \frac{1}{4-\sqrt{3}} \cdot \left(4 - \frac{3^2}{4^3}\right) \\
&= \frac{1}{4-\sqrt{3}} \cdot \left(\frac{4^4}{4^3} - \frac{3^2}{4^3}\right) = \frac{1}{4-\sqrt{3}} \cdot \frac{256-9}{64} = \frac{1}{4-\sqrt{3}} \cdot \frac{247}{64} = \frac{247}{64} \cdot \left(4 - \sqrt{3}\right) \\
&\approx 1.70.
\end{align*}
\] 

<|ref|>text<|/ref|><|det|>[[844, 506, 888, 523]]<|/det|>
(50) 

<|ref|>text<|/ref|><|det|>[[88, 543, 184, 561]]<|/det|>
b) Es gilt 

<|ref|>equation<|/ref|><|det|>[[115, 572, 888, 672]]<|/det|>
\[
\begin{align*}
\underline{H} &= \frac{x^{1'306} - x^{1'310}}{(1+x) \cdot (1-x)} = \frac{x^{1'306} - x^{1'310}}{1-x^2} = \frac{x^{2.653} - x^{2.655}}{1-x^2} = \frac{(x^2)^{653} - (x^2)^{654+1}}{1-x^2} \\
&= G_{(653;654)}(x^2) = \sum_{k=653}^{654} x^{2k} = x^{2.653} + x^{2.654} = x^{1'306} + x^{1'308}.
\end{align*}
\] 

<|ref|>text<|/ref|><|det|>[[88, 685, 184, 703]]<|/det|>
c) Es gilt 

<|ref|>equation<|/ref|><|det|>[[115, 713, 888, 919]]<|/det|>
\[
\begin{align*}
\underline{I} &= \sum_{l=2}^{8} \sum_{k=0}^{l} \frac{1}{2^k} = \sum_{l=2}^{8} \sum_{k=0}^{l} \left(\frac{1}{2}\right)^k = \sum_{l=2}^{8} G_{(0;l)} \left(\frac{1}{2}\right) = \sum_{l=2}^{8} \frac{\left(\frac{1}{2}\right)^0 - \left(\frac{1}{2}\right)^{l+1}}{1-\frac{1}{2}} \\
&= \sum_{l=2}^{8} \frac{1 - \left(\frac{1}{2}\right)^{l+1}}{\frac{1}{2}} = 2 \sum_{l=2}^{8} \left(1 - \left(\frac{1}{2}\right)^{l+1}\right) = 2 \sum_{l=2}^{8} 1 - 2 \sum_{l=2}^{8} \left(\frac{1}{2}\right)^{l+1} \\
&= 2 \cdot (8-2+1) - 2 \cdot \frac{1}{2} \sum_{l=2}^{8} \left(\frac{1}{2}\right)^l = 14 - G_{(2;8)} \left(\frac{1}{2}\right) = 14 - \frac{\left(\frac{1}{2}\right)^2 - \left(\frac{1}{2}\right)^{8+1}}{1-\frac{1}{2}} \\
&= 14 - \frac{\frac{1}{2^2} - \frac{1}{2^9}}{\frac{1}{2}} = 14 - \frac{1}{2} + \frac{1}{2^8} = 13.5 + \frac{1}{256} \approx 13.5.
\end{align*}
\]