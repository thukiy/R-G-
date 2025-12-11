<|ref|>sub_title<|/ref|><|det|>[[24, 15, 437, 43]]<|/det|>
## Lösungsansätze für Basislösungen 

<|ref|>equation<|/ref|><|det|>[[50, 48, 180, 80]]<|/det|>
\[y(x) = e^{\lambda x}\]

<|ref|>equation<|/ref|><|det|>[[50, 88, 333, 120]]<|/det|>
\[y'(x) = \lambda \cdot e^{\lambda x} = \lambda \cdot y(x)\]

<|ref|>equation<|/ref|><|det|>[[50, 127, 370, 159]]<|/det|>
\[y''(x) = \lambda^2 \cdot e^{\lambda x} = \lambda^2 \cdot y(x)\]

<|ref|>sub_title<|/ref|><|det|>[[24, 191, 260, 214]]<|/det|>
## Einstellen in DGL: 

<|ref|>equation<|/ref|><|det|>[[50, 222, 479, 252]]<|/det|>
\[\alpha \cdot \lambda^2 \cdot e^{\lambda x} + b \cdot \lambda e^{\lambda x} + c \cdot e^{\lambda x} = 0\]

<|ref|>equation<|/ref|><|det|>[[50, 264, 800, 290]]<|/det|>
\[\alpha \cdot \lambda^2 + b \cdot \lambda + c = 0 \quad \text{charakteristische Gleichung oder}\]

<|ref|>equation<|/ref|><|det|>[[50, 333, 270, 366]]<|/det|>
\[\lambda_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}\]

<|ref|>text<|/ref|><|det|>[[24, 380, 828, 408]]<|/det|>
→ die Lösungen sind von der Diskriminante \(D = b^2 - 4ac\) abhängig 

<|ref|>sub_title<|/ref|><|det|>[[24, 435, 220, 460]]<|/det|>
### 1. Falle: \(D > 0\) 

<|ref|>equation<|/ref|><|det|>[[160, 465, 540, 500]]<|/det|>
\[\exists \text{ 2 Lösungen } \lambda_{1,2} = \frac{-b \pm \sqrt{D}}{2a}\]

<|ref|>equation<|/ref|><|det|>[[160, 510, 490, 576]]<|/det|>
\[\begin{align*}
y(x) &= C_1 y_1(x) + C_2 y_2(x) \\
&= C_1 \cdot e^{\lambda_1 x} + C_2 \cdot e^{\lambda_2 x}
\end{align*}\]

<|ref|>sub_title<|/ref|><|det|>[[24, 606, 220, 631]]<|/det|>
### 2. Falle: \(D = 0\) 

<|ref|>equation<|/ref|><|det|>[[160, 636, 400, 671]]<|/det|>
\[\exists \text{ 1 Lösung } \lambda = -\frac{b}{2a}\]

<|ref|>equation<|/ref|><|det|>[[160, 678, 375, 707]]<|/det|>
\[y_1(x) = C \cdot e^{-\frac{b}{2a} \cdot x}\]

<|ref|>text<|/ref|><|det|>[[154, 721, 690, 747]]<|/det|>
→ 2. Lösung mittels Variation der Konstanten 

<|ref|>equation<|/ref|><|det|>[[154, 757, 390, 784]]<|/det|>
\[\rightarrow C(x) = C_1 + C_2 \cdot x\]

<|ref|>equation<|/ref|><|det|>[[210, 789, 504, 822]]<|/det|>
\[y(x) = (C_1 + C_2 \cdot x) \cdot e^{-\frac{b}{2a} \cdot x}\]

<|ref|>sub_title<|/ref|><|det|>[[24, 853, 220, 878]]<|/det|>
### 3. Falle: \(D < 0\) 

<|ref|>equation<|/ref|><|det|>[[160, 884, 490, 970]]<|/det|>
\[\lambda_{1,2} = \frac{-b \pm \sqrt{D}}{2a} = \frac{-b}{2a} \pm i \frac{\sqrt{D}}{2a}\]

<|ref|>equation<|/ref|><|det|>[[340, 950, 427, 970]]<|/det|>
\[= S \pm i \omega\]