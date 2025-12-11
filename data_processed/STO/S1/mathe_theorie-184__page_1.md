<|ref|>text<|/ref|><|det|>[[27, 12, 360, 40]]<|/det|>
→ Verteilungsfunktion : 

<|ref|>equation<|/ref|><|det|>[[100, 42, 640, 85]]<|/det|>
\[F(x) = P(X \le x) = \sum_{k \le x} \binom{n}{k} p^k \cdot (1-p)^{n-k}\]

<|ref|>text<|/ref|><|det|>[[110, 89, 700, 118]]<|/det|>
n und p sind die Parameter der Verteilung. 

<|ref|>equation<|/ref|><|det|>[[110, 125, 480, 156]]<|/det|>
\[Hilbert \mu = E(x) = n \cdot p\]

<|ref|>equation<|/ref|><|det|>[[110, 165, 450, 197]]<|/det|>
\[Varianz \sigma^2 = n \cdot p \cdot (1-p)\]

<|ref|>equation<|/ref|><|det|>[[110, 203, 637, 235]]<|/det|>
\[Standardabweichung \sigma = \sqrt{n \cdot p \cdot (1-p)}\]

<|ref|>text<|/ref|><|det|>[[22, 262, 920, 345]]<|/det|>
Veranschaulichung: ziehen einer Kugel aus une mit s und w
Kugeln. Wahrscheinlichkeit für w : p
für s : 1-p 

<|ref|>text<|/ref|><|det|>[[80, 383, 616, 412]]<|/det|>
bei n-maligem ziehen mit zurücklegen : 

<|ref|>text<|/ref|><|det|>[[110, 420, 951, 490]]<|/det|>
- Wahrscheinlichkeit für bestimmte Anordnung von x weissen und (n-x) schwarzen Kugeln : \(p^x \cdot (1-p)^{n-x}\) 

<|ref|>text<|/ref|><|det|>[[110, 497, 920, 567]]<|/det|>
- Es gibt Permutationen, die genau gleich viele w und s Kugeln aufweisen oder andere Anordnung haben 

<|ref|>equation<|/ref|><|det|>[[170, 572, 950, 640]]<|/det|>
\[ \rightarrow \binom{n}{x} = \binom{n-x}{n-x} \quad \text{Höchstreichen für Anordnung.} \]

<|ref|>equation<|/ref|><|det|>[[100, 630, 950, 664]]<|/det|>
\[ \rightarrow \binom{n}{x} \cdot p^x \cdot (1-p)^{n-x} \text{ ist also die Wahrscheinlichkeitsfunktion} \]

<|ref|>text<|/ref|><|det|>[[80, 654, 650, 721]]<|/det|>
→ für f(x) wird auch b(x; n, p) verwandt,
für Binomialverteilung B(n, p) 

<|ref|>text<|/ref|><|det|>[[80, 730, 552, 759]]<|/det|>
→ f(x) ist meist nicht symmetrisch 

<|ref|>equation<|/ref|><|det|>[[80, 763, 454, 801]]<|/det|>
\[ \rightarrow f(x+1) = \frac{(n-x) \cdot p}{(x+1) \cdot (1-p)} \cdot f(x) \]