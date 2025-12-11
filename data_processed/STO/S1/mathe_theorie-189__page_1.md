<|ref|>text<|/ref|><|det|>[[25, 30, 692, 63]]<|/det|>
- stetige Zufallsvariable mit linearer Dichtefunktion 

<|ref|>equation<|/ref|><|det|>[[95, 70, 544, 100]]<|/det|>
\[f(x) = 0,02x \quad (0 \le x \le 10)\]

<|ref|>text<|/ref|><|det|>[[95, 109, 310, 137]]<|/det|>
bestimme \(F(x)\) : 

<|ref|>equation<|/ref|><|det|>[[125, 143, 850, 220]]<|/det|>
\[F(x) = -\infty \int 0,02 u \, du = 0,02 \int u \, du = 0,02 \cdot [\frac{1}{2} u^2] \Big|_0^\infty = 0,02 \cdot [\frac{1}{2} x^2 - \frac{1}{2} \cdot 0] = 0,01 x^2\]

<|ref|>equation<|/ref|><|det|>[[125, 225, 525, 293]]<|/det|>
\[F(x) = \begin{cases} 0 & x < 0 \\ 0,01x^2 & 0 \le x \le 10 \\ 1 & x > 10 \end{cases}\]

<|ref|>image<|/ref|><|det|>[[88, 303, 930, 490]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[25, 519, 819, 586]]<|/det|>
- die Benssquarer eines elektronischen Bauteils sei exponentialverteilt mit Dichtefunktion 

<|ref|>equation<|/ref|><|det|>[[95, 593, 661, 661]]<|/det|>
\[f(t) = \begin{cases} c & t < 0 \\ c \cdot e^{-0,1t} & t \ge 0 \end{cases} \quad c > 0\]

<|ref|>text<|/ref|><|det|>[[95, 696, 639, 725]]<|/det|>
zuerst c bestimmen : es muss gelten 

<|ref|>equation<|/ref|><|det|>[[440, 728, 655, 768]]<|/det|>
\[-\infty \int f(t) \, dt = 1\]

<|ref|>equation<|/ref|><|det|>[[95, 785, 740, 970]]<|/det|>
\[\begin{align*}
-\infty \int f(t) \, dt &= -\infty \int c \cdot e^{-0,1t} \, dt = c \cdot \int e^{-0,1t} \, dt \\
&= c \cdot \int (e^{-0,1})^t \, dt = c \cdot \left[ \frac{1}{e^{-0,1} \cdot 1} \cdot (e^{-0,1})^t \right] \Big|_0^\infty \\
&= c \cdot \left[ -\frac{1}{0,1 \cdot e^{-0,1}} \cdot e^{-0,1t} \right] \Big|_0^\infty = c \cdot \left[ -\frac{1}{0,1} \cdot e^{-0,1t} \right] \Big|_0^\infty \\
&= c \cdot \left[ 0 - (-10) \right] = 10c \overset{!}{=} 1 \\
&= c = \frac{1}{10}
\end{align*}\]