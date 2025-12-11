<|ref|>text<|/ref|><|det|>[[90, 66, 186, 85]]<|/det|>
e) Es gilt 

<|ref|>equation<|/ref|><|det|>[[118, 90, 888, 130]]<|/det|>
\[ \frac{e'(z)}{3} = \frac{1}{3} \cdot z^{\frac{1}{3} - 1} = \frac{1}{3} \cdot z^{\frac{1}{3} + \frac{2}{3}} = \frac{1}{3} \cdot z^{-\frac{2}{3}}. \qquad (19) \]

<|ref|>text<|/ref|><|det|>[[90, 141, 186, 160]]<|/det|>
f) Es gilt 

<|ref|>equation<|/ref|><|det|>[[118, 165, 888, 204]]<|/det|>
\[ \frac{f'(k)}{3} = 2 \cdot \frac{2}{3} \cdot k^{\frac{2}{3} - 1} = \frac{2 \cdot 2}{3} \cdot k^{\frac{2}{3} + \frac{2}{3}} = \frac{4}{3} \cdot k^{-\frac{1}{3}}. \qquad (20) \]

<|ref|>text<|/ref|><|det|>[[90, 217, 186, 235]]<|/det|>
g) Es gilt 

<|ref|>equation<|/ref|><|det|>[[118, 240, 888, 263]]<|/det|>
\[ \frac{g'(w)}{-p \cdot w^{p-1}}. \qquad (21) \]

<|ref|>text<|/ref|><|det|>[[90, 278, 186, 297]]<|/det|>
h) Es gilt 

<|ref|>equation<|/ref|><|det|>[[118, 303, 888, 325]]<|/det|>
\[ \frac{h'(v)}{u^2 \cdot v^{2-1} \cdot w^2} = \frac{2u^2vw^2}{2}. \qquad (22) \]

<|ref|>text<|/ref|><|det|>[[90, 341, 186, 360]]<|/det|>
i) Es gilt 

<|ref|>equation<|/ref|><|det|>[[118, 365, 888, 405]]<|/det|>
\[ \frac{i'(q)}{rs} = \frac{p^2 \cdot 1}{rs} = \frac{p^2}{rs}. \qquad (23) \]

<|ref|>sub_title<|/ref|><|det|>[[75, 430, 490, 448]]<|/det|>
## 5. Ableitung der kubischen Standardfunktion 

<|ref|>text<|/ref|><|det|>[[75, 448, 612, 466]]<|/det|>
Wir betrachten die *kubische Standard-Funktion* \(f : \mathbb{R} \to \mathbb{R}\) mit 

<|ref|>equation<|/ref|><|det|>[[428, 472, 888, 492]]<|/det|>
\[ f(x) := x^3. \qquad (24) \]

<|ref|>text<|/ref|><|det|>[[90, 504, 504, 523]]<|/det|>
a) Mit Hilfe der *Monom-Ableitung* erhalten wir 

<|ref|>equation<|/ref|><|det|>[[118, 528, 888, 552]]<|/det|>
\[ \frac{f'(x)}{3} = 3 \cdot x^{3-1} = 3x^2. \qquad (25) \]

<|ref|>text<|/ref|><|det|>[[90, 566, 780, 601]]<|/det|>
b) Mit Hilfe des *Differenzquotienten* und der *binomischen Formel* für dritte Potenzen erhalten wir 

<|ref|>equation<|/ref|><|det|>[[118, 606, 860, 763]]<|/det|>
\[ \begin{aligned} \frac{f'(x)}{\delta x} &= \lim_{\delta x \to 0} \frac{f(x + \delta x) - f(x)}{\delta x} = \lim_{\delta x \to 0} \frac{(x + \delta x)^3 - x^3}{\delta x} \\ &= \lim_{\delta x \to 0} \frac{x^3 + 3 \cdot x^2 \cdot \delta x + 3 \cdot x \cdot \delta x^2 + \delta x^3 - x^3}{\delta x} = \lim_{\delta x \to 0} \frac{3 \cdot x^2 \cdot \delta x + 3 \cdot x \cdot x \cdot \delta x^2 + \delta x^3}{\delta x} \\ &= \lim_{\delta x \to 0} (\frac{3 \cdot x^2 + 3 \cdot x \cdot \delta x + \delta x^2}{\delta x}) = \lim_{\delta x \to 0} (3 \cdot x^2 + 3 \cdot x \cdot \delta x + \frac{\delta x^2}{\delta x}) \\ &= 3 \cdot x^2 + 3 \cdot x \cdot 0 + 0^2 = 3 \cdot x^2 + 0 + 0 = 3x^2. \end{aligned} \qquad (26) \]

<|ref|>text<|/ref|><|det|>[[90, 775, 504, 794]]<|/det|>
c) Mit Hilfe der *Monom-Ableitung* erhalten wir 

<|ref|>equation<|/ref|><|det|>[[122, 799, 888, 895]]<|/det|>
\[ \begin{aligned} \frac{f''(x)}{\delta x} &= 2 \cdot 3 \cdot x^{2-1} = \frac{6x}{\delta x} \\ \frac{f'''(x)}{\delta x} &= \frac{6}{\delta x} \\ \frac{f''''(x)}{\delta x} &= \frac{0}{\delta x}. \end{aligned} \qquad (27) \]