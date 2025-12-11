<|ref|>text<|/ref|><|det|>[[20, 15, 824, 44]]<|/det|>
→ Bestimmung der Parameter \(a, b, \ldots\) durch Minimum von \(S\): 

<|ref|>text<|/ref|><|det|>[[65, 54, 339, 80]]<|/det|>
Ableihen und 0 setzen 

<|ref|>equation<|/ref|><|det|>[[105, 85, 365, 118]]<|/det|>
\[ \frac{\partial S}{\partial a} = 0, \quad \frac{\partial S}{\partial b} = 0 \quad \ldots \]

<|ref|>text<|/ref|><|det|>[[145, 130, 412, 155]]<|/det|>
⇝ lösen eines LGS 

<|ref|>text<|/ref|><|det|>[[25, 186, 639, 214]]<|/det|>
Bestimmung der Ausgleichsgeraden (f(x) = ax + b) : 

<|ref|>equation<|/ref|><|det|>[[80, 225, 460, 252]]<|/det|>
\[ v_i = y_i - f(x_i) = y_i - ax_i - b \]

<|ref|>text<|/ref|><|det|>[[25, 283, 595, 310]]<|/det|>
Summe \(S\) der Abweichungen ergibt sich zu 

<|ref|>equation<|/ref|><|det|>[[80, 316, 525, 354]]<|/det|>
\[ S(a, b) = \sum_{i=1}^{n} v_i^2 = \sum_{i=1}^{n} (y_i - ax_i - b)^2 \]

<|ref|>text<|/ref|><|det|>[[25, 378, 220, 406]]<|/det|>
Minimumsum: 

<|ref|>equation<|/ref|><|det|>[[80, 410, 490, 454]]<|/det|>
\[ \frac{\partial S}{\partial a} = \sum_{i=1}^{n} 2(y_i - ax_i - b) \cdot (-x_i) \]

<|ref|>equation<|/ref|><|det|>[[120, 450, 500, 490]]<|/det|>
\[ = 2 \sum_{i=1}^{n} (ax_i^2 + bx_i - x_i y_i) \quad \stackrel{!}{=} 0 \]

<|ref|>equation<|/ref|><|det|>[[80, 505, 430, 549]]<|/det|>
\[ \frac{\partial S}{\partial b} = \sum_{i=1}^{n} 2(y_i - ax_i -b) \cdot (-1) \]

<|ref|>equation<|/ref|><|det|>[[120, 545, 420, 585]]<|/det|>
\[ = 2 \sum_{i=1}^{n} (b + ax_i - y_i) \quad \stackrel{!}{=} 0 \]

<|ref|>text<|/ref|><|det|>[[25, 608, 375, 636]]<|/det|>
Steigung \(a\) ergibt sich zu 

<|ref|>equation<|/ref|><|det|>[[80, 640, 590, 689]]<|/det|>
\[ a = \frac{\sum_{i=1}^{n} x_i y_i - n \bar{x} \bar{y}}{\sum_{i=1}^{n} x_i^2 - n \bar{x}^2} \quad \bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i \]

<|ref|>equation<|/ref|><|det|>[[80, 720, 230, 747]]<|/det|>
\[ b = \bar{y} - a \bar{x} \]

<|ref|>image<|/ref|><|det|>[[190, 789, 592, 990]]<|/det|>