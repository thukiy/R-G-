<|ref|>text<|/ref|><|det|>[[114, 82, 141, 100]]<|/det|>
b) 

<|ref|>equation<|/ref|><|det|>[[380, 98, 737, 118]]<|/det|>
\[D = b^2 - 4ac = 0 \quad \text{or} \quad | + 4ac \]

<|ref|>equation<|/ref|><|det|>[[241, 130, 737, 147]]<|/det|>
\[\Leftrightarrow \quad b^2 = 4ac \quad | : (4a). \]

<|ref|>text<|/ref|><|det|>[[122, 152, 295, 170]]<|/det|>
Daraus erhalten wir 

<|ref|>equation<|/ref|><|det|>[[450, 170, 533, 209]]<|/det|>
\[c = \frac{b^2}{4a}.\]

<|ref|>text<|/ref|><|det|>[[114, 215, 141, 232]]<|/det|>
c) 

<|ref|>text<|/ref|><|det|>[[114, 231, 295, 248]]<|/det|>
Ableitungen bilden: 

<|ref|>equation<|/ref|><|det|>[[120, 250, 355, 271]]<|/det|>
\[y_1'(x) = \lambda \cdot e^{\lambda x} = \lambda \cdot y_1(x)\]

<|ref|>equation<|/ref|><|det|>[[120, 278, 395, 300]]<|/det|>
\[y_1''(x) = \lambda \cdot \lambda \cdot e^{\lambda x} = \lambda^2 \cdot y_1(x).\]

<|ref|>text<|/ref|><|det|>[[144, 300, 725, 319]]<|/det|>
- Einsetzen in DGL und mit Kenntnis, dass \(\lambda\) eine Nullstelle ist: 

<|ref|>equation<|/ref|><|det|>[[181, 320, 836, 373]]<|/det|>
\[a y_1'' + b y_1' + c y_1 = a \cdot \lambda^2 \cdot y_1 + b \cdot \lambda \cdot y_1 + c \cdot y_1 = (a \cdot \lambda^2 + b \cdot \lambda + c) \cdot y_1 \\ = p(\lambda) \cdot y_1 = 0 \cdot y_1 = \underline{0}.\]

<|ref|>text<|/ref|><|det|>[[144, 373, 347, 390]]<|/det|>
- Einsetzen in DGL: 

<|ref|>equation<|/ref|><|det|>[[181, 391, 842, 504]]<|/det|>
\[ \begin{aligned} a y_1'' + b y_1' + c y_1 &= a \cdot \lambda^2 \cdot y_1 + b \cdot \lambda \cdots y_1 + c \cdot y_1 = (a \cdot \lambda^2 \cdot b \cdot \lambda + c) \cdot y_1 \\ &= \left( a \cdot \left( -\frac{b}{2a} \right)^2 + b \cdot \left( -\frac{b}{2a} \right) + \frac{b^2}{4a} \right) \cdot y_1 = \left( \frac{b^2}{4a} - \frac{b^2}{2a} + \frac{b^2}{4a} \right) \cdot y_1 \\ &= \frac{b^2}{a} \cdot \left( \frac{1}{4} - \frac{1}{2} + \frac{1}{4} \right) \cdot y_1 = \frac{b^2}{a} \cdot 0 \cdot y_1 = \underline{0}. \end{aligned} \]

<|ref|>text<|/ref|><|det|>[[114, 505, 141, 522]]<|/det|>
d) 

<|ref|>text<|/ref|><|det|>[[114, 521, 293, 539]]<|/det|>
Ableitungen bilden: 

<|ref|>equation<|/ref|><|det|>[[120, 540, 501, 562]]<|/det|>
\[y_2'(x) = 1 \cdot e^{\lambda x} + x \cdot \lambda \cdot e^{\lambda x} = (1 + \lambda x) \cdot e^{\lambda x}\]

<|ref|>equation<|/ref|><|det|>[[120, 570, 678, 592]]<|/det|>
\[y_2''(x) = (0 + \lambda \cdot 1) \cdot e^{\lambda x} + (1 + \lambda x) \cdot \lambda \cdot e^{\lambda x} = (\lambda + \lambda + \lambda^2 x) \cdot e^{\lambda x}\]

<|ref|>equation<|/ref|><|det|>[[171, 600, 340, 620]]<|/det|>
\[= (2\lambda + \lambda^2 x) \cdot e^{\lambda x}.\]

<|ref|>text<|/ref|><|det|>[[114, 619, 662, 638]]<|/det|>
Einsetzen in DGL und mit Kenntnis, dass \(\lambda\) eine Nullstelle ist: \(\lambda\) 

<|ref|>equation<|/ref|><|det|>[[120, 640, 830, 808]]<|/det|>
\[ \begin{aligned} a y_2'' + b y_2' + c y_2 &= a \cdot (2\lambda + \lambda^2 x) \cdot e^{\lambda x} + b \cdot (1 + \lambda x) \cdot e^{\lambda x} + c \cdot x \cdot e^{\lambda x} \\ &= (2a\lambda + a\lambda^2 x + b + b\lambda x + c x) \cdot e^{\lambda x} \\ &= (2a\lambda + b + (a\lambda^2 + b\lambda + c)x) \cdot e^{\lambda x} \\ &= (2a \cdot \left(-\frac{b}{2a}\right) + b + p(\lambda) \cdot x) \cdot e^{\lambda x} = (-b + b + p(\lambda) \cdot x) \cdot e^{\lambda x} \\ &= (0 + 0 \cdot x) \cdot e^{\lambda x} = 0 \cdot e^{\lambda x} = \underline{0}. \end{aligned} \]

<|ref|>text<|/ref|><|det|>[[114, (0, 141, 0]]<|/det|>
4. Allgemeine Lösung von DGL 2. Ordnung bestimmen 

<|ref|>text<|/ref|><|det|>[[114, 840, 872, 875]]<|/det|>
Bestimmen Sie die allgemeine Lösung der gegebenen DGL 2. Ordnung mit Hilfe des charakteristischen Polynoms. 

<|ref|>text<|/ref|><|det|>[[114, 874, 833, 893]]<|/det|>
a) \(y'' + 3y' - 4y = 0\) b) \(y'' + 20y' + 100y = 0\) c) \(y'' + 4y' + 20y = 0\) 

<|ref|>text<|/ref|><|det|>[[114, 892, 833, 911]]<|/det|>
d) \(2y'' + 20y' + 50y = 0\) e) \(3y'' - 6y' + 30y = 0\) f) \(2y'' + 7y' + 3y = 0\)