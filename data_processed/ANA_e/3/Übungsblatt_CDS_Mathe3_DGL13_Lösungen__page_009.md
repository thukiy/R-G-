<|ref|>text<|/ref|><|det|>[[121, 82, 680, 120]]<|/det|>
Aus den Randbedingungen \(u(x_1, 0) = u(x_1, b) = 0\) folgt \(V(0) = V(b) = 0\). Wir erhalten: 

<|ref|>equation<|/ref|><|det|>[[170, 136, 635, 192]]<|/det|>
\[
\begin{align*}
V(0) &= a_3 + a_4 \Rightarrow a_3 = -a_4 \\
V(b) &= a_3 \left( \exp\left(\sqrt{-k_{x_2}^2} b\right) - \exp\left(-\sqrt{-k_{x_2}^2} b\right) \right) = 0
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[121, 207, 217, 226]]<|/det|>
Also folgt 

<|ref|>equation<|/ref|><|det|>[[121, 241, 680, 275]]<|/det|>
\[
\exp\left(\sqrt{-k_{x_2}^2} b\right) = \exp\left(-\sqrt{-k_{x_2}^2} b\right) \text{ bzw. } \exp\left(2\sqrt{-k_{x_2}^2} b\right) = 1.
\]

<|ref|>text<|/ref|><|det|>[[121, 290, 680, 352]]<|/det|>
Diese Gleichung wird erfüllt für \(2\sqrt{-k_{x_2}^2} b = 2\pi in\) bzw.
\(\sqrt{k_{x_2}^2} = \frac{\pi n}{b}\). Also ist \(k_{x_2}^2 = \frac{\pi^2 n^2}{b^2}\) für \(n \in \mathbb{N}\). 

<|ref|>text<|/ref|><|det|>[[121, 360, 680, 398]]<|/det|>
Analog erhalten wir aus \(u(0, x_2) = u(a, x_2) = 0\) die Bedingungen \(U(0) = U(a) = 0\) und damit 

<|ref|>equation<|/ref|><|det|>[[208, 414, 590, 453]]<|/det|>
\[
a_1 = -a_2 \quad \text{und} \quad k_{x_1}^2 = \frac{\pi^2 m^2}{a}, \quad m \in \mathbb{N}.
\]

<|ref|>text<|/ref|><|det|>[[121, 467, 532, 487]]<|/det|>
Damit ergeben sich die zugehörigen Lösungen 

<|ref|>equation<|/ref|><|det|>[[275, 500, 523, 570]]<|/det|>
\[
\begin{align*}
V_n(x_2) &= \tilde{c}_n \sin\left(\frac{\pi n}{b} x_2\right), \\
U_m(x_1) &= \tilde{d}_n \sin\left(\frac{\pi m}{a} x_1\right).
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[121, 583, 680, 639]]<|/det|>
Jegliche Linearkombinationen dieser Funktionen sind weitere Lösungen. Insgesamt können wir die Klasse der Lösungen beschreiben durch Entwicklungen der Form 

<|ref|>equation<|/ref|><|det|>[[195, 655, 605, 750]]<|/det|>
\[
\begin{align*}
u(x_1, x_2) &= \sum_{n, m=1}^{\infty} U_m(x_1) V_n(x_2) \\
&= \sum_{n, m} c_{nm} \sin\left(\frac{\pi m}{a} x_1\right) \sin\left(\frac{\pi n}{b} x_2\right)
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[121, 767, 159, 783]]<|/det|>
mit 

<|ref|>equation<|/ref|><|det|>[[243, 797, 555, 840]]<|/det|>
\[
k^2 = k_{x_1}^2 + k_{x_2}^2 = \pi^2 \left( \frac{m^2}{a^2} + \frac{n^2}{b^2} \right)
\]

<|ref|>text<|/ref|><|det|>[[121, 855, 530, 874]]<|/det|>
und bei entsprechender Konvergenz der Reihe.