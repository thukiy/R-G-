<|ref|>text<|/ref|><|det|>[[115, 81, 861, 116]]<|/det|>
c) Eine stetige Zufallsvariable X genüge einer sogenannten Gamma-Verteilung mit der Dichtefunktion 

<|ref|>equation<|/ref|><|det|>[[143, 113, 590, 170]]<|/det|>
\[f(x) = \begin{cases} \lambda^2 \cdot x \cdot e^{-\lambda x} & x > 0 \\ 0 & x \le 0 \end{cases} \quad \text{für} \quad \lambda > 0.\]

<|ref|>text<|/ref|><|det|>[[145, 174, 792, 193]]<|/det|>
Berechnen Sie den Mittelwert, die Varianz und die Standardabweichung. 

<|ref|>text<|/ref|><|det|>[[115, 208, 144, 225]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[120, 230, 710, 270]]<|/det|>
\[E(X) = 0,5 \cdot \int_{-1}^{1} x(1 + x)dx = 0,5 \cdot \int_{-1}^{1} (x + x^2)dx = 0,5 \left[ \frac{1}{2}x^2 + \frac{1}{3}x^3 \right]_{-1}^{1} = \frac{1}{3}\]

<|ref|>text<|/ref|><|det|>[[115, 272, 144, 289]]<|/det|>
b) 

<|ref|>equation<|/ref|><|det|>[[120, 290, 740, 457]]<|/det|>
\[
\begin{align*}
\text{Normierung: } a \cdot \int_{-1}^{1} (x^2 - x^3)dx &= a \left[ \frac{1}{3}x^3 - \frac{1}{4}x^4 \right]_{-1}^{1} = \frac{1}{12}a = 1 \quad \Rightarrow \quad a = 12 \\
\mu &= 12 \cdot \int_{-1}^{1} x(x^2 - x^3)dx = 12 \cdot \int_{-1}^{1} (x^3 - x^4)dx = 12 \left[ \frac{1}{4}x^4 - \frac{1}{5}x^5 \right]_{-1}^{1} = 12 \cdot \frac{1}{20} = \frac{3}{5} \\
E(X^2) &= 12 \cdot \int_{-1}^{1} x^2(x^2 - x^3)dx = 12 \cdot \int_{-1}^{1}(x^4 - x^5)dx = 12 \left[ \frac{1}{5}x^5 - \frac{1}{6}x^6 \right]_{-1}^{1} = \\
&= 12 \cdot \frac{1}{30} = \frac{2}{5} ; \quad \sigma^2 = E(X^2) - \mu^2 = \frac{2}{5} - \frac{9}{25} = \frac{1}{25} ; \quad \sigma = \frac{1}{5}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 459, 144, 476]]<|/det|>
c) 

<|ref|>equation<|/ref|><|det|>[[120, 475, 702, 628]]<|/det|>
\[
\begin{align*}
\mu &= \lambda^2 \cdot \int_{0}^{\infty} x^2 \cdot e^{-\lambda x}dx = \lambda^2 \left[ \frac{\lambda^2 x^2 + 2\lambda x + 2}{-\lambda^3} \cdot e^{-\lambda x} \right]_{0}^{\infty} = \lambda^2 \left( 0 + \frac{2}{\lambda^3} \right) = \frac{2}{\lambda} \\
E(X^2) &= \lambda^2 \cdot \int_{0}^{\infty} x^3 \cdot e^{-\lambda x}dx = \lambda^2 \left[ \frac{x^3 \cdot e^{-\lambda x}}{-\lambda} \right]_{0}^{\infty} + \lambda^2 \cdot \frac{3}{\lambda} \int_{0}^{\infty} x^2 \cdot e^{-\lambda x}dx = \\
&= \lambda^2 (0 + 0) + 3\lambda \left[ \frac{\lambda^2 x^2 + 2\lambda x + 3}{-\lambda^3} \cdot e^{-\lambda x} \right]_{0}^{\infin} = 3\lambda \left( 0 + \frac{2}{\lambda^3} \right) = 6 \\
\sigma^2 &= E(X^2) - \mu^2 = \frac{6}{\lambda^2} - \frac{4}{\lambda^2} = \frac{2}{\lambda^2} ; \quad \sigma = \frac{\sqrt{2}}{\lambda}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 643, 230, 660]]<|/det|>
6. Bahnhof 

<|ref|>text<|/ref|><|det|>[[115, 660, 840, 711]]<|/det|>
An einem Bahnhof fahrt die Schnellbahn exakt alle 20 Minuten ab. Wie gross ist die Wahrscheinlichkeit dafür, dass ein zufällig eintreffender Fahrgast mehr als 15 Minuten warten muss? Gehen Sie von einer Gleichverteilung aus. 

<|ref|>text<|/ref|><|det|>[[115, 725, 420, 743]]<|/det|>
Die Wartezeit ist gleichverteilt mit 

<|ref|>equation<|/ref|><|det|>[[120, 746, 347, 790]]<|/det|>
\[
f(x) = \begin{cases} \frac{1}{\sqrt{20}} & \text{für } 0 \le x \le 20 \\ 0 & \text{sonst} \end{cases}
\]

<|ref|>text<|/ref|><|det|>[[115, 792, 455, 810]]<|/det|>
Für die Wahrscheinlichkeit ergibt sich