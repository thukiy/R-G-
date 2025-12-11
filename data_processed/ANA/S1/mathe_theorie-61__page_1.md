<|ref|>text<|/ref|><|det|>[[20, 11, 425, 38]]<|/det|>
Additionstheorem nutzen : 

<|ref|>equation<|/ref|><|det|>[[50, 50, 666, 77]]<|/det|>
\[ \sin(\alpha + \beta) = \sin\alpha \cos\beta + \sin\beta \cos\alpha \quad (1) \]

<|ref|>equation<|/ref|><|det|>[[50, 88, 664, 115]]<|/det|>
\[ \sin(\alpha - \beta) = \sin\alpha \cos\beta - \sin\beta \cos\alpha \quad (2) \]

<|ref|>equation<|/ref|><|det|>[[50, 147, 787, 175]]<|/det|>
\[ (1) - (2) : \sin(\alpha + \beta) - \sin(\alpha - \beta) = 2 \sin\beta \cos\alpha \]

<|ref|>text<|/ref|><|det|>[[20, 197, 540, 235]]<|/det|>
Ersetzen : \(\alpha = \frac{\alpha + \beta}{2}\), \(\beta = \frac{\alpha - \beta}{2}\) 

<|ref|>equation<|/ref|><|det|>[[30, 255, 636, 290]]<|/det|>
\[ \rightarrow \sin\alpha - \sin\beta = \alpha \cdot \sin\frac{\alpha - \beta}{2} \cdot \cos\frac{\alpha + \beta}{2} \]

<|ref|>equation<|/ref|><|det|>[[30, 303, 490, 328]]<|/det|>
\[ \rightarrow \alpha = x + \Delta x \quad \text{und} \quad \beta = x : \]

<|ref|>text<|/ref|><|det|>[[130, 342, 347, 367]]<|/det|>
Differenzquotient 

<|ref|>equation<|/ref|><|det|>[[150, 375, 725, 416]]<|/det|>
\[ \frac{\sin(x + \Delta x) - \sin x}{\Delta x} = 2 \cdot \frac{\sin\frac{\Delta x}{2} \cdot \cos\frac{\Delta x + \Delta x}{2}}{\Delta x} \]

<|ref|>equation<|/ref|><|det|>[[150, 451, 620, 496]]<|/det|>
\[ f'(x) = \lim_{\Delta x \to 0} 2 \cdot \sin\frac{\Delta x}{2} \cdot \cos\frac{\Delta x + \Delta \Delta x}{2} \]

<|ref|>equation<|/ref|><|det|>[[220, 505, 808, 590]]<|/det|>
\[ \begin{aligned} f'(x) &= \lim_{\Delta x \to 0} 2 \cdot \sin\frac{\Delta \Delta x}{2} \cdot \cos(\frac{\Delta x + \Delta x}{2}) = \cos x \\ &= \lim_{\Delta x \to 0} \frac{\Delta \cdot \sin\frac{\Delta x}{2}}{\frac{\Delta x}{2}} \cdot \cos(\frac{\Delta x + \Delta x}{2}) = \cos \frac{\Delta x}{2} \cdot \cos(\frac{\Delta x + \Delta x}{x}) \end{aligned} \]

<|ref|>text<|/ref|><|det|>[[20, 614, 595, 644]]<|/det|>
weitere trigonometrische Funktionen : 

<|ref|>equation<|/ref|><|det|>[[50, 654, 280, 680]]<|/det|>
\[ \cdot f(x) = \cos x \]

<|ref|>equation<|/ref|><|det|>[[88, 691, 310, 721]]<|/det|>
\[ f'(x) = -\sin x \]

<|ref|>equation<|/ref|><|det|>[[50, 752, 290, 778]]<|/det|>
\[ \cdot f(x) = \tan x \]

<|ref|>equation<|/ref|><|det|>[[88, 787, 490, 822]]<|/det|>
\[ f'(x) = 1 + \tan^2 x = \frac{1}{\cos^2 x} \]

<|ref|>equation<|/ref|><|det|>[[50, 844, 290, 875]]<|/det|>
\[ \cdot f(x) = \cot x \]

<|ref|>equation<|/ref|><|det|>[[88, 884, 496, 919]]<|/det|>
\[ f'(x) = -1 - \cot^2 x = -\frac{1}{\sin^2 x} \]