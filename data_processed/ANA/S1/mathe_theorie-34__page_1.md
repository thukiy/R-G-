<|ref|>text<|/ref|><|det|>[[70, 12, 345, 42]]<|/det|>
Divergentkriterium : 

<|ref|>text<|/ref|><|det|>[[109, 48, 872, 123]]<|/det|>
Konvergiert \(\sum_{k=1}^{\infty} a_k\), dann folgt, dass \(\lim_{k \to \infty} a_k = 0\) gilt.
jedoch folgt aus \(\lim_{k \to \infty} a_k = 0\) nicht, dass \(\sum_{k=1}^{\infty} a_k\) konvergiert. 

<|ref|>text<|/ref|><|det|>[[24, 142, 433, 183]]<|/det|>
Bsp : 
\[\sum_{k=1}^{\infty} \frac{1}{k}\]
ist divergent 

<|ref|>text<|/ref|><|det|>[[217, 183, 485, 223]]<|/det|>
es gilt : \(\lim_{k \to \infty} \frac{1}{k} = 0\) 

<|ref|>equation<|/ref|><|det|>[[137, 235, 770, 395]]<|/det|>
\[
\begin{align*}
\sum_{k=1}^{\infty} \frac{1}{k} &= 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8} + \dots + \frac{1}{2^m} \\
&\ge 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{4} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \dots + \frac{1}{2^{m-1}} \\
&= 2 \cdot \frac{1}{2^2} = \frac{1}{2} = 4 \cdot \frac{1}{2^3} = \frac{1}{2} \\
&= 1 + m \cdot \frac{1}{2} \xrightarrow{m \to \infty} \infty
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[24, 419, 157, 452]]<|/det|>
Sympy 

<|ref|>text<|/ref|><|det|>[[55, 458, 864, 491]]<|/det|>
Summenberechnung : \(S = \text{sp. summation } (k \ast 2, (k, 1, 5))\); 

<|ref|>equation<|/ref|><|det|>[[390, 488, 576, 536]]<|/det|>
\[
S = \sum_{k=1}^{S} k^2
\]

<|ref|>text<|/ref|><|det|>[[45, 556, 735, 590]]<|/det|>
Grenzwertberechnung : \(a = \text{sp. limit\_seq } (1/k, k)\); 

<|ref|>equation<|/ref|><|det|>[[390, 590, 540, 636]]<|/det|>
\[
\lim_{k \to \infty} \frac{1}{k}
\]

<|ref|>text<|/ref|><|det|>[[24, 670, 460, 702]]<|/det|>
Geometrische Summenformel 

<|ref|>equation<|/ref|><|det|>[[80, 707, 808, 781]]<|/det|>
\[
G_{(m;n)}(x) := \sum_{k=m}^{n} x^k \\
\to (1-x) \cdot G_{(m;n)}(x) = x^m - x^{m+1} \qquad x \notin \{0; 1\}
\]