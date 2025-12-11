<|ref|>sub_title<|/ref|><|det|>[[75, 65, 380, 83]]<|/det|>
## 7. Ableitung der Wurzelfunktion 

<|ref|>text<|/ref|><|det|>[[75, 83, 536, 101]]<|/det|>
Wir betrachten die Wurzel-Funktion \(f: \mathbb{R}^+ \to \mathbb{R}\) mit 

<|ref|>equation<|/ref|><|det|>[[423, 113, 888, 135]]<|/det|>
\[f(x) := \sqrt{x}. \qquad (41)\]

<|ref|>text<|/ref|><|det|>[[88, 151, 761, 170]]<|/det|>
a) Wir berechnen die Ableitung \(f'(x)\) mit Hilfe der Monom-Ableitung. Es gilt 

<|ref|>equation<|/ref|><|det|>[[117, 180, 888, 225]]<|/det|>
\[\frac{f'(x)}{x} = (\sqrt{x})' = (x^{\frac{1}{2}})' = \frac{1}{2} \cdot x^{\frac{1}{2} - 1} = \frac{1}{2} \cdot x^{-\frac{1}{2}} = \frac{1}{2} \cdot \frac{1}{\sqrt{x}} = \frac{1}{2\sqrt{x}}. \qquad (42)\]

<|ref|>text<|/ref|><|det|>[[88, 243, 888, 295]]<|/det|>
b) Wir berechnen die Ableitung \(f'(x)\) mit Hilfe des Differenzquotienten, wobei wir den Bruch mit \((\sqrt{x+\delta x} + \sqrt{x})\) erweitern und dann im Zähler ausmultiplizieren. Es gilt 

<|ref|>equation<|/ref|><|det|>[[117, 305, 888, 493]]<|/det|>
\[\begin{align*} \frac{f'(x)}{\delta x} &= \lim_{\delta x \to 0} \frac{f(x+\delta x) - f(x)}{\delta x} = \lim_{\delta x \to 0} \frac{\sqrt{x+\delta x} - \sqrt{x}}{\delta x} \\ &= \lim_{\delta x \to 0} \frac{(\sqrt{x+\delta x} - \sqrt{x}) \cdot (\sqrt{x+\delta x} + \sqrt{x})}{\delta x \cdot (\sqrt{x+\delta x} + \sqrt{x})} = \lim_{\delta x \to 0} \frac{(\sqrt{x+\delta x})^2 - (\sqrt{x})^2}{\delta x \cdot (\sqrt{x+\delta x} + \sqrt{x})} \\ &= \lim_{\delta x \to 0} \frac{x+\delta x - x}{\delta x \cdot (\sqrt{x+\delta x} + \sqrt{x})} = 1 \lim_{\delta x \to 0} \frac{\delta x}{\delta x \cdot (\sqrt{x+\delta x} + \sqrt{x})} \quad = \lim_{\delta x \to 0} \frac{1}{\sqrt{x+\delta x} + \sqrt{x}} \\ &= \frac{1}{\sqrt{x+0} + \sqrt{x}} = \frac{1}{\sqrt{x} + \sqrt{x}} = \frac{1}{2\sqrt{x}}. \end{align*} \qquad (43)\]

<|ref|>text<|/ref|><|det|>[[88, 511, 827, 530]]<|/det|>
c) Wir berechnen die zweite Ableitung von \(f\) mit Hilfe der Monom-Ableitung. Es gilt 

<|ref|>equation<|/ref|><|det|>[[117, hoto 220, 888, 625]]<|/det|>
\[\begin{align*} \frac{f''(x)}{x} &= (f'(x))' = \left(\frac{1}{2} \cdot x^{-\frac{1}{2}}\right)' = \frac{1}{2} \cdot \left(-\frac{1}{2}\right) \cdot x^{-\frac{1}{2}-1} = -\frac{1}{4} \cdot x^{-\frac{3}{2}} = -\frac{1}{4} \cdot \frac{1}{\sqrt{x^3}} \\ &= -\frac{1}{4\sqrt{x^3}}. \end{align*} \qquad (44)\]