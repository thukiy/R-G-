<|ref|>sub_title<|/ref|><|det|>[[30, 8, 530, 66]]<|/det|>
# Differentialrechnung 

<|ref|>sub_title<|/ref|><|det|>[[25, 85, 222, 118]]<|/det|>
## Produktregel 

<|ref|>equation<|/ref|><|det|>[[55, 125, 290, 156]]<|/det|>
\[f(x) = g(x) \cdot h(x)\]

<|ref|>text<|/ref|><|det|>[[90, 164, 380, 194]]<|/det|>
wie sieht \(f'(x)\) aus? 

<|ref|>equation<|/ref|><|det|>[[90, 202, 375, 233]]<|/det|>
\[\rightarrow f'(x) = g'(x) \cdot h'(x)\]

<|ref|>text<|/ref|><|det|>[[150, 245, 375, 273]]<|/det|>
z.B. \(f(x) = x^2\) 

<|ref|>equation<|/ref|><|det|>[[240, 281, 375, 312]]<|/det|>
\[f'(x) = 2x\]

<|ref|>equation<|/ref|><|det|>[[240, 321, 480, 360]]<|/det|>
mit \(f(x) = \frac{x \cdot x}{g(x) \cdot h(x)}\)

<|ref|>text<|/ref|><|det|>[[240, 380, 730, 411]]<|/det|>
wäre \(f'(x) = g'(x) \cdot h'(x) = 1 \cdot 1 = 1\) 

<|ref|>equation<|/ref|><|det|>[[45, 437, 744, 470]]<|/det|>
Produktregel: \(g, h : \mathbb{R} \to \mathbb{R}, \quad f(x) = g(x) \cdot h(x)\)

<|ref|>text<|/ref|><|det|>[[280, 477, 800, 508]]<|/det|>
\(g \& h\) sind differenzierbar. Dann gibt: 

<|ref|>equation<|/ref|><|det|>[[280, 515, 722, 546]]<|/det|>
\[f'(x) = g'(x) \cdot h(x) + g(x) \cdot h'(x)\]

<|ref|>sub_title<|/ref|><|det|>[[25, 575, 420, 606]]<|/det|>
## Beispiel: 
\[f(x) = x^2 = x \cdot x\] 

<|ref|>equation<|/ref|><|det|>[[160, 614, 934, 660]]<|/det|>
\[f'(x) = x \cdot 1 + 1 \cdot x = 2x \rightarrow \text{stimmt mit Monom - regel überein}\]

<|ref|>sub_title<|/ref|><|det|>[[25, 693, 395, 723]]<|/det|>
## Beispiele: Differenzquotient: 

<|ref|>equation<|/ref|><|det|>[[50, 728, 896, 950]]<|/det|>
\[f'(x) = \lim_{\Delta x \to 0} \frac{f(x+\Delta x) - f(x)}{\Delta x} = \lim_{\Delta x \to 0} \frac{g(x+\Delta x) \cdot h(x+\Delta x) - g(x) \cdot h(x)}{\Delta x}\]

\[= \lim_{\Delta x \to 0} \frac{g(x+\Delta x) \times h(x+\Delta x) + g(x) \times h(x+\Delta x) - g(x) \times h(x+\Delta x) - g(x) \times h(x)}{\Delta x}\]

\[= \lim_{\Delta x \to 0} \left( \frac{h(x+\Delta x) \times [g(x+\Delta x) - g(x)]}{\Delta x} + \frac{g(x) \times [h(x+\Delta x) - h(x)]}{\Delta x} \right)\]

\[= \lim_{\Delta x \to 0} \frac{h(x+\Delta x) \times [g(x+\Delta x) - g](x)}{\Delta x} + \lim_{\Delta x \to 0} \frac{g(x) \times [h(x+\Delta x) - h(x)]}{\D