<|ref|>text<|/ref|><|det|>[[25, 16, 880, 45]]<|/det|>
Bsp: skleige Gleichverteilung / Rechtseitverteilung / Uniformverteilung 

<|ref|>text<|/ref|><|det|>[[120, 54, 680, 80]]<|/det|>
→ jede Realisation ist gleich wahrscheinlich 

<|ref|>equation<|/ref|><|det|>[[101, 88, 480, 156]]<|/det|>
\[f(x) = \begin{cases} \frac{1}{b-a} & a \le x \le b \\ 0 & \text{sonst} \end{cases}\]

<|ref|>image<|/ref|><|det|>[[101, 170, 520, 315]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[30, 344, 280, 368]]<|/det|>
Verteilungsfunktion : 

<|ref|>equation<|/ref|><|det|>[[60, 370, 590, 444]]<|/det|>
\[F(x) = -\infty \int_{-\infty}^{x} \frac{1}{b-a} \, dx = \int_{-\infty}^{x} \frac{1}{b-a} \, dx = \frac{1}{b-a} [x]_{-\infty}^{x} = \frac{1}{b-a} (x-a) = \frac{x-a}{b-a}\]

<|ref|>equation<|/ref|><|det|>[[50, 448, 408, 555]]<|/det|>
\[F(x) = \begin{cases} 0 & x < a \\ \frac{x-a}{b-a} & a \le x \le b \\ 1 & x > b \end{cases}\]

<|ref|>image<|/ref|><|det|>[[101, 580, 485, 744]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[50, 778, 610, 803]]<|/det|>
Mittelwert : \(\mu = -\infty \int x \cdot f(x) \, dx = a \int x \cdot \frac{1}{b-a} \, dx\) 

<|ref|>equation<|/ref|><|det|>[[240, 808, 670, 844]]<|/det|>
\[= \frac{1}{b-a} \left[ \frac{1}{a} x^2 \right]_{-\infty}^{b} = \frac{b^2 - a^2}{2(b-a)} = \frac{1}{2} (b-a)\]

<|ref|>text<|/ref|><|det|>[[50, 875, 380, 900]]<|/det|>
Varianz : \(\sigma^2 = E(x^2) - \mu^2\) 

<|ref|>equation<|/ref|><|det|>[[190, 904, 707, 976]]<|/det|>
\[E(x^2) = -\infty \int x^2 \frac{1}{b-a} \, dx = a \int x^2 \frac{1}{b-a} \cdot x^2 \, dx\] \[= \frac{1}{b-a} \cdot \left[ \frac{1}{3} x^3 \right]_{-\infty}^{b} = \frac{b^3 - a^3}{3(b-a)} = \frac{1}{3} (a^2 + ab + b^2)\]