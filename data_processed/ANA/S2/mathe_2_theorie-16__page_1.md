<|ref|>text<|/ref|><|det|>[[20, 10, 401, 38]]<|/det|>
Def : uneigentliches Integral 

<|ref|>text<|/ref|><|det|>[[133, 50, 936, 78]]<|/det|>
a) \(f: \mathbb{R} \to \mathbb{R}\) habe bei \(a \in \mathbb{R}\) einen uneigentlichen Grenzwert, d.h. 

<|ref|>equation<|/ref|><|det|>[[184, 88, 390, 124]]<|/det|>
\[ \lim_{x \to a} f(x) = \pm \infty \]

<|ref|>text<|/ref|><|det|>[[184, 148, 666, 177]]<|/det|>
\(f\) sei auf \([t, b] \subset ]a, b[\) integrierbar 

<|ref|>text<|/ref|><|det|>[[184, 188, 881, 216]]<|/det|>
\(f\) heisst beänglich \([a, b]\) uneigentlich integrierbar, wenn 

<|ref|>equation<|/ref|><|det|>[[190, 223, 704, 270]]<|/det|>
\[ \int_a^b f(x) \, dx = \lim_{\substack{t \to a \\ t > a}} \int_t^b f(x) \, dx \quad \text{existiert} \]

<|ref|>text<|/ref|><|det|>[[184, 286, 887, 355]]<|/det|>
Existiert der Grenzwert nicht, dann spricht man von einem
divergenten uneigentlichen Integral 

<|ref|>text<|/ref|><|det|>[[133, 383, 876, 411]]<|/det|>
b) Sei der Integrationsbereich \([a, \infty[\) oder \(]-\infty, b]\) und 

<|ref|>text<|/ref|><|det|>[[184, 421, 920, 448]]<|/det|>
\(f\) sei auf jedem Teilintervall \([c, d]\) integrierbar, dann ist 

<|ref|>text<|/ref|><|det|>[[190, 459, 597, 488]]<|/det|>
\(f\) uneigentlich integrierbar, wenn 

<|ref|>equation<|/ref|><|det|>[[190, 495, 737, 572]]<|/det|>
\[ \begin{aligned} \int_a^b f(x) \, dx &= \lim_{b \to \infty} \int_a^b f(x) \, dx && \text{bzw.} \\ -\infty \int_a^b f(x) \, dx &= \lim_{a \to -\infty} \int_a^b f(x) \, dx && \text{konvergiert} \end{aligned} \]

<|ref|>text<|/ref|><|det|>[[20, 595, 480, 628]]<|/det|>
Bsp : 
\[ \int_0^1 \frac{1}{\sqrt{x}} \, dx = \lim_{a \to 0} \int_a^1 \frac{1}{\sqrt{x}} \, dx \] 

<|ref|>equation<|/ref|><|det|>[[176, 636, 620, 672]]<|/det|>
\[ = \lim_{a \to 0} [2\sqrt{x}]_a^1 = \lim_{a \to 0} [2\sqrt{a}] = 2 \]

<|ref|>text<|/ref|><|det|>[[125, 689, 464, 725]]<|/det|>
\[ \int_0^1 \frac{1}{x} \, dx = \lim_{a \to 0} \int_0^1 \frac{1}{x} \, dx \] 

<|ref|>equation<|/ref|><|det|>[[176, 732, 750, 778]]<|/det|>
\[ = \lim_{a \to 0} [\ln x]_0^1 = \lim_{a \to 0} [\ln 1 - \ln a] \quad \to +\infty \]

<|ref|>text<|/ref|><|det|>[[40, 812, 333, 841]]<|/det|>
\(\to\) Verallgemeinerung : 

<|ref|>equation<|/ref|><|det|>[[103, 847, 590, 880]]<|/det|>
\[ \int_0^1 \frac{1}{x^n} \, dx \quad \text{konvergiert für } 0 < n < 1 \]

<|ref|>equation<|/ref|><|det|>[[103, 885, 835, 961]]<|/det|>
\[ \int_0^1 \frac{1}{x^n} \,dx = \lim_{a \to 0} \int_0^1 \frac{ 1 }{ x^n } \, dx \\ = \lim_{a \to 0} \left[ \frac{1}{1-n} x^{-n+1} \right]_a^1 = \lim_{a \to 0} \left[ \frac{1}{1 - n} \cdot \frac{1}{a} \cdot a^{-n+1} \right] = \frac{1}{1-n} \]