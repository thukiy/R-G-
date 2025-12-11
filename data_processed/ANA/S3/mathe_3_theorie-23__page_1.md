<|ref|>sub_title<|/ref|><|det|>[[27, 12, 784, 44]]<|/det|>
Euler - homogene DGL, DGL in homogenen Veränderlichen 

<|ref|>text<|/ref|><|det|>[[55, 73, 789, 100]]<|/det|>
Eine Funktion \(f: \mathbb{R}^n \to \mathbb{R}\) heisst homogen vom Grad \(p\), wenn 

<|ref|>equation<|/ref|><|det|>[[95, 108, 590, 135]]<|/det|>
\[f(\lambda x) = \lambda^p \cdot f(x) \quad \lambda \neq 0, \lambda \in \mathbb{R}\]

<|ref|>text<|/ref|><|det|>[[95, 149, 510, 175]]<|/det|>
\(f: \mathbb{R}^2 \to \mathbb{R}\) homogen vom Grad 0: 

<|ref|>equation<|/ref|><|det|>[[135, 186, 410, 212]]<|/det|>
\[f(\lambda x, \lambda y) = \lambda^p f(x, y)\]

<|ref|>text<|/ref|><|det|>[[55, 246, 802, 273]]<|/det|>
Die DGL \(y' = f(x, y)\) heisst für eine derartige Funktion homogen 

<|ref|>equation<|/ref|><|det|>[[55, 300, 655, 366]]<|/det|>
\[\text{mit } \lambda = \frac{1}{\lambda} \text{ folgt: } y' = f(\lambda x, \lambda y) = f(\frac{1}{\lambda} \cdot x, \frac{1}{\lambda} \cdot y) \\ = f(1, \frac{y}{\lambda}) = g(\frac{y}{\lambda})\]

<|ref|>text<|/ref|><|det|>[[55, 377, 755, 405]]<|/det|>
\(y' = g(\frac{y}{\lambda})\) heisst auch Normalform einer homogenen DGL 

<|ref|>text<|/ref|><|det|>[[55, 416, 775, 443]]<|/det|>
\(\to\) um die DGL zu lösen, verwenden wir eine Substitution: 

<|ref|>equation<|/ref|><|det|>[[135, 454, 330, 479]]<|/det|>
\[y(x) = x \cdot u(x)\]

<|ref|>equation<|/ref|><|det|>[[135, 490, 395, 516]]<|/det|>
\[y'(x) = u(x) + x \cdot u'(x)\]

<|ref|>equation<|/ref|><|det|>[[235, 524, 525, 556]]<|/det|>
\[= g(\frac{y}{x}) = g\left(\frac{x \cdot u(x)}{x}\right) = g(u)\]

<|ref|>text<|/ref|><|det|>[[55, 567, 305, 593]]<|/det|>
\(\to u + x \cdot u' = g(u)\) 

<|ref|>equation<|/ref|><|det|>[[95, 600, 235, 633]]<|/det|>
\[u' = \frac{g(u) - u}{x}\]

<|ref|>text<|/ref|><|det|>[[315, 612, 736, 635]]<|/det|>
DGL mit Trennung des Variablen lösen 

<|ref|>text<|/ref|><|det|>[[25, 667, 620, 694]]<|/det|>
Bsp: \(\bullet x^2 y' = a^2 x^2 + y^2 + xy\) 

<|ref|>equation<|/ref|><|det|>[[460, 670, 620, 694]]<|/det|>
\[x \neq 0, a \neq 0\]

<|ref|>equation<|/ref|><|det|>[[155, 700, 365, 732]]<|/det|>
\[y' = a^2 + \frac{y^2}{x} + \frac{y}{x}\]

<|ref|>equation<|/ref|><|det|>[[125, 740, 655, 770]]<|/det|>
\[u(x) = \frac{y}{x} \quad \text{da } x \cdot u' = a^2 + u^2 + a \quad |: x\]

<|ref|>equation<|/ref|><|det|>[[285, 775, 588, 808]]<|/det|>
\[u' = \frac{ax}{x} + \frac{ux^2}{x} = \frac{1}{x}(a^2 + u^2)\]

<|ref|>equation<|/ref|><|det|>[[115, 813, 360, 847]]<|/det|>
\[\int \frac{1}{a^2 + u^2} du = \int \frac{1}{x} dx\]

<|ref|>equation<|/ref|><|det|>[[115, 854, 583, 920]]<|/det|>
\[\frac{1}{a} \arctan \frac{u}{a} = \text{eln} x \cdot \text{eln} c \quad C \neq 0\]

<|ref|>equation<|/ref|><|det|>[[195, 925, 285, 950]]<|/det|>
\[= \text{eln} x \cdot c\]

<|ref|>equation<|/ref|><|det|>[[155, 928, 535, 959]]<|/det|>
\[\arctan \frac{u}{a} = a \cdot \text{eln} x \cdot c \quad | \text{tan}\]

<|ref|>equation<|/ref|><|det|>[[235, 965, 485, 995]]<|/det|>
\[\frac{u}{a} = \text{tan}(a \cdot \text{eln} x \cdot c)\]