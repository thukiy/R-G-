<|ref|>text<|/ref|><|det|>[[103, 15, 544, 42]]<|/det|>
- N Elemente bestehen aus 2 Sorten : 

<|ref|>text<|/ref|><|det|>[[160, 54, 790, 120]]<|/det|>
M und (N-M), wobei M Elemente die gewünschte Eigenschaft besitzen 

<|ref|>equation<|/ref|><|det|>[[160, 123, 551, 220]]<|/det|>
\[ f(x) = \frac{\binom{M}{x} \cdot \binom{N-M}{n-x}}{\binom{N}{n}} = \frac{\text{gunstige mögliche}}{\text{faile}} \]

<|ref|>text<|/ref|><|det|>[[103, 226, 960, 255]]<|/det|>
→ hypergeometrisch durch binomial anfahren, wenn gilt: \(n < 0,05N\) 

<|ref|>sub_title<|/ref|><|det|>[[50, 280, 350, 311]]<|/det|>
## Poisson-Verteilung 

<|ref|>text<|/ref|><|det|>[[103, 321, 808, 390]]<|/det|>
→ Grenzfall der Binomialverteilung, für Modellierung seltener Ereignisse 

<|ref|>text<|/ref|><|det|>[[103, 400, 470, 426]]<|/det|>
→ wird meist genau, wenn 

<|ref|>equation<|/ref|><|det|>[[163, 433, 535, 504]]<|/det|>
\[ \begin{aligned} p &\le 0,01 \\ f(x) &= \frac{\mu^x}{x!} \cdot e^{-\mu} \end{aligned} \quad \begin{aligned} n \cdot p &\le 5 \\ \mu &= n \cdot p \end{aligned} \]