<|ref|>text<|/ref|><|det|>[[122, 66, 220, 85]]<|/det|>
c) Es gilt 

<|ref|>equation<|/ref|><|det|>[[147, 92, 920, 196]]<|/det|>
\[
\begin{align*}
\frac{C}{k} &= \sum_{k=0}^{9} \sqrt{3^k} = \sum_{k=0}^{9} \left( \sqrt{3} \right)^k = G_{(0;9)} \left( \sqrt{3} \right) = \frac{\left( \sqrt{3} \right)^0 - \left( \sqrt{3} \right)^{9+1}}{1 - \sqrt{3}} = \frac{1 - \left( \sqrt{3} \right)^{10}}{1 - \sqrt{3}} \\
&= \frac{1 - \left( \sqrt{3} \right)^{2.5}}{1 - \sqrt{3}} = \frac{1 - 3^5}{1 - \sqrt{3}} = \frac{1 - 243}{1 - \sqrt{3}} = \frac{242}{\sqrt{3} - 1} \approx \frac{331}{1} \tag{43}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[122, 204, 220, 222]]<|/det|>
d) Es gilt 

<|ref|>equation<|/ref|><|det|>[[147, 231, 920, 373]]<|/det|>
\[
\begin{align*}
D &= \sum_{k=0}^{8} \frac{4}{2^{k+1}} = \sum_{k=0}^{8} \frac{4}{2 \cdot 2^k} = \sum_{k=0}^{8} \frac{2}{2^k} = 2 \sum_{k=0}^{8} \frac{1}{2^k} = 2 \sum_{k=0}^{8} \left( \frac{1}{2} \right)^k = 2 G_{(0;8)} \left( \frac{1}{2} \right) \\
&= 2 \cdot \frac{\left( \frac{1}{2} \right)^0 - \left( \frac{1}{2} \right)^{8+1}}{1 - \frac{1}{2}} = 2 \cdot \frac{1 - \frac{1}{2^9}}{1} = 2 \cdot 2 \cdot \left( 1 - \frac{1}{2^9} \right) = \frac{2^{11}}{2^9} - \frac{2^2}{2^9} = \frac{2^9}{2^7} - \frac{1}{2^7} \\
&= \frac{512 - 1}{128} = \frac{511}{128} \approx 3.99. \tag{44}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[122, 380, 220, 399]]<|/det|>
e) Es gilt 

<|ref|>equation<|/ref|><|det|>[[147, 408, 866, 595]]<|/det|>
\[
\begin{align*}
E &= \sum_{k=2}^{5} \frac{10 \sqrt{3^{4k}}}{5^{k+1}} = \sum_{k=2}^{5} \frac{10 \cdot 3^{\frac{4k}{2}}}{5 \cdot 5^k} = \sum_{k=2}^{5} 2 \cdot \frac{3^{2k}}{5^k} = 2 \sum_{k=2}^{5} \frac{9^k}{5^k} = 2 \sum_{k=2}^{5} \left( \frac{9}{5} \right)^k \\
&= 2 G_{(2;5)} \left( \frac{9}{5} \right) = 2 \cdot \frac{\left( \frac{9}{5} \right)^2 - \left( \frac{9}{5} \right)^{5+1}}{1 - \frac{9}{5}} = 2 \cdot \frac{\left( \frac{9}{5} \right) - \left( \frac{9}{5} \right)^6}{-\frac{4}{5}} = \frac{5 \cdot 2}{4} \cdot \left( \left( \frac{9}{5} \right)^6 - \left( \frac{9}{5} \right)^2 \right) \\
&= \frac{5}{2} \cdot \left( \frac{9^6}{5^6} - \frac{9^2}{5^2} \right) = \frac{1}{2} \cdot \left( \frac{9^6}{5^5} - \frac{9^2}{5} \right) = \frac{1}{2} \cdot \left( \frac {9^6}{5^5} - \frac{5^4 \cdot 9^2}{5^5} \right) = \frac{531'441 - 625 \cdot 81}{2 \cdot 3'125} \\
&= \frac{480'816}{2 \cdot 3'125} = \frac{240'408}{3'125} \approx \frac{76.9}{.} \tag{45}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[122, 604, 220, 623]]<|/det|>
f) Es gilt 

<|ref|>equation<|/ref|><|det|>[[147, 632, 920, 736]]<|/det|>
\[
\begin{align*}
F &= \sum_{k=3}^{7} \left( 1 + x^{2k} \right) = \sum_{k=3}^{7} 1 + \sum_{k=3}^{7} \left( x^2 \right)^k = (7 - 3 + 1) + G_{(3;7)} \left( x^2 \right) \\
&= 5 + \frac{\left( x^2 \right)^3 - \left( x^2 \right)^{7+1}}{1 - x^2} = 5 + \frac{x^{2 \cdot 3} - x^{2 \cdot 8}}{1 - x^2} = 5 + \frac{x^6 - x^{16}}{1 - x^2}. \tag{46}
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[108, 764, 303, 782]]<|/det|>
11. Lohnerhöhungen 

<|ref|>text<|/ref|><|det|>[[108, 782, 920, 818]]<|/det|>
Ein Einstiegslohn von monatlich \(L_0 := 4'000\) CHF werde jährlich um \(i := 2\%\) = 0.02 erhöht.
Dies ergibt einen jährlichen Lohn-Faktor von 

<|ref|>equation<|/ref|><|det|>[[437, 828, 920, 847]]<|/det|>
\[
a = 1 + i = 1.02. \tag{47}
\]

<|ref|>text<|/ref|><|det|>[[122, 862, 508, 881]]<|/det|>
a) Nach 10 Jahren beträgt der Monatslohn 

<|ref|>equation<|/ref|><|det|>[[147, 890, 920, 914]]<|/det|>
\[
\frac{L_{10}}{L_0} = a^{10} \cdot L_0 = 1.02^{10} \cdot 4'000 \text{ CHF} \approx 4'875.98 \text{ CHF}. \tag{48}
\]