<|ref|>text<|/ref|><|det|>[[115, 81, 455, 101]]<|/det|>
Es ergibt sich als allgemeine Lösung: 

<|ref|>equation<|/ref|><|det|>[[119, 107, 618, 132]]<|/det|>
\[ \frac{y(x)}{x} = (C + C(x)) \cdot e^{M(x)} = (C - x e^{-x} - e^{-x}) \cdot e^x = \frac{C e^x - x - 1}{x}. \]

<|ref|>text<|/ref|><|det|>[[115, 131, 144, 149]]<|/det|>
d) 

<|ref|>text<|/ref|><|det|>[[115, 147, 743, 169]]<|/det|>
Linear inhomogene DGL mit \(m(x) = 2x\) und \(q(x) = e^{x^2}\). Es ergibt sich 

<|ref|>equation<|/ref|><|det|>[[119, 170, 387, 202]]<|/det|>
\[ M(x) = \int m(x) \, dx = \int 2x \, dx = x^2 \]

<|ref|>equation<|/ref|><|det|>[[119, 205, 655, 238]]<|/det|>
\[ C(x) = \int q(x) \cdot e^{-M(x)} \, dx = \int e^{x^2} \cdot e^{-x^2} \, dx = \int e^{x^2 - x^2} \, dx = \int 1 \, dx = x. \]

<|ref|>text<|/ref|><|det|>[[115, 238, 456, 257]]<|/det|>
Es ergibt sich als allgemeine Lösung: 

<|ref|>equation<|/ref|><|det|>[[119,

\[ \frac{y(x)}{x} = (C + C(x)) \cdot e^{m(x)} = \frac{(C + x) e^{x^2}}{x}. \]

<|ref|>text<|/ref|><|det|>[[115, 304, 144, 322]]<|/det|>
e) 

<|ref|>text<|/ref|><|det|>[[115, 318, 700, 344]]<|/det|>
Die DGL ergibt sich zu \(y' = \frac{y}{x} + x^2\). D. h. \(m(x) = 1/x\) und \(q(x) = x^2\). 

<|ref|>equation<|/ref|><|det|>[[119, 345, 709, 453]]<|/det|>
\[ \begin{align*} M(x) &= \int m(x) \, dx = \int \frac{1}{x} \, dx = \ln(|x|) \\ C(x) &= \int q(x) \cdot e^{-M(x)} \, dx = \int x^2 \cdot e^{-\ln(|x|)} \, dx = \int x^2 \cdot \frac{1}{|x|} \, dx = \int |x| \, dx \\ &= \operatorname{sgn}(x) \int x \, dx = \operatorname{sgn}(x) \cdot \frac{1}{2} x^2 = \frac{\operatorname{sgn}(x)}{2} x^2. \end{align*} \]

<|ref|>text<|/ref|><|det|>[[115, 451, 576, 472]]<|/det|>
Es ergibt sich als allgemeine Lösung für \(x \in \mathbb{R} \setminus \{0\}\): 

<|ref|>equation<|/ref|><|det|>[[115, 475, 707, 547]]<|/det|>
\[ \begin{align*} \frac{y(x)}{x} &= (C + C(x)) \cdot e^{M(x)} = (C + \frac{\operatorname{sgn}(x)}{2} x^2) \cdot e^{\ln(|x|)} = (C + \frac{\operatorname{sgn}(x)}{2} x^2)|x| \\ &= C|x| + \frac{\operatorname{sgn}(x)}{2} x^2 \cdot |x| = C|x| + \frac{1}{2} x^2 \cdot x = C|x| + \frac{1}{2} x^3. \end{align*} \]

<|ref|>text<|/ref|><|det|>[[115, 552, 144, 570]]<|/det|>
f) 

<|ref|>text<|/ref|><|det|>[[115, 566, 765, 595]]<|/det|>
Die DGL ergibt sich zu \(y' = \frac{y}{x}+x+\frac{4}{x}\). D. h. \(m(x) = 1/x\) und \(q(x) = \frac{x+4}{x}\). 

<|ref|>equation<|/ref|><|det|>[[119, 597, 785, 750]]<|/det|>
\[ \begin{align*} M(x) &= \int m(x) \, dx &= \int \frac{1}{x} \, dx = \ln(|x|) \\ \nonumber C(x) &= \int q(x) \cdot e^{-M(x)} \, dx &= \int \left(x + \frac{4}{x}\right) \cdot e^{-\ln(|x|)} \, dx = \int \left(x + \frac{4}{x}\right) \cdot \frac{1}{|x|} \, dx \\ &= \int \left(\frac{x}{|x|} + \frac{4}{x \cdot |x|}\right) \, dx = \int \left(\operatorname{sgn}(x) + \frac{4 \operatorname{sgn}(x)}{x^2}\right) \, dx = \int \operatorname{sgn}(x) \left(1 + \frac{4}{x^2}\right) \, dx \\ &= \operatorname{sgn}(x) \left(x - \frac{4}{x}\right) = |x| - \frac{4}{|x|}. \end{align*} \]

<|ref|>text<|/ref|><|det|>[[115, 750, 576, 770]]<|/det|>
Es ergibt sich als allgemeine Lösung für \(x \in \mathbb{R}\setminus\{0\}\): 

<|ref|>equation<|/ref|><|det|>[[119, 771, 694, 831]]<|/det|>
\[ \begin{align*} \frac{y(x)}{x} &= (C + \frac{C(x)}{x}) \cdot e^{M(x)} = (C + |x| - \frac{4}{|x|}) \cdot e^{\ln(|x|)} = (C + |x| - \frac{4}{|x|}) |x| \\ &= C|x| + |x|^2 - 4 = C|x| + x^2 - 4. \end{align*} \]