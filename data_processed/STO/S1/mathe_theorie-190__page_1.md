<|ref|>equation<|/ref|><|det|>[[115, 6, 415, 40]]<|/det|>
\[\Rightarrow f(t) = \frac{1}{10} \cdot e^{-0,1t}\]

<|ref|>equation<|/ref|><|det|>[[115, 45, 789, 85]]<|/det|>
\[F(t) = -\frac{t}{10} \int 0,1 \cdot e^{-0,1u} \, du = 0,1 \cdot \frac{t}{10} \int e^{-0,1u} \, du\]

<|ref|>equation<|/ref|><|det|>[[175, 85, 800, 120]]<|/det|>
\[= 0,1 \cdot [(-10) \cdot e^{-0,1u}] \frac{t}{10} = 0,1 \cdot [-10e^{-0,1t} - (-10)]\]

<|ref|>equation<|/ref|><|det|>[[175, 122, 945, 158]]<|/det|>
\[= 0,1 \cdot (-10) \cdot e^{-0,1t} + 1 = -e^{-0,1t} + 1 \quad \text{für } t \ge 0\]

<|ref|>image<|/ref|><|det|>[[115, 179, 860, 347]]<|/det|>

<|ref|>text<|/ref|><|det|>[[150, 364, 820, 390]]<|/det|>
\(\rightarrow\) Anteil der Bauteile, deren Lebensdauer \(\ge 10\) ist 

<|ref|>equation<|/ref|><|det|>[[201, 401, 690, 427]]<|/det|>
\[P(t \ge 10) = F(\infty) - F(10) = 1 - F(10)\]

<|ref|>equation<|/ref|><|det|>[[330, 437, 783, 468]]<|/det|>
\[= 1 - 1 + e^{-1} = e^{-1} = \frac{1}{e} \approx 0,368\]

<|ref|>text<|/ref|><|det|>[[150, 480, 928, 507]]<|/det|>
\(\rightarrow\) ca. 36,8% der Bauelemente funktioniert noch nach \(t = 10\) 

<|ref|>text<|/ref|><|det|>[[45, 533, 911, 570]]<|/det|>
**Mittelwert** einer steigern dunkelfarvariable : \(\mu = E(x) = -\infty \int x \cdot f(x) \, dx\) 

<|ref|>text<|/ref|><|det|>[[45, 590, 585, 628]]<|/det|>
**Varianz** \(\text{Var}(X) = -\infty \int (x - \mu)^2 f(x) \, dx\)