<|ref|>text<|/ref|><|det|>[[25, 21, 512, 45]]<|/det|>
Bsp : DGL : \(y' + y \tan x = \sin x \cdot \cos x\) 

<|ref|>text<|/ref|><|det|>[[125, 58, 305, 81]]<|/det|>
AB : \(y(0) = 1\) 

<|ref|>text<|/ref|><|det|>[[108, 112, 325, 138]]<|/det|>
1. Homogene DGL 

<|ref|>equation<|/ref|><|det|>[[156, 150, 350, 177]]<|/det|>
\(y' + y \tan x = 0\)

<|ref|>equation<|/ref|><|det|>[[156, 188, 333, 215]]<|/det|>
\(y' = -y \tan x\)

<|ref|>equation<|/ref|><|det|>[[156, 223, 415, 255]]<|/det|>
\(\int \frac{1}{y} dy = -\int \tan x dx\)

<|ref|>equation<|/ref|><|det|>[[156, 264, 450, 291]]<|/det|>
\(\int \ln|y| = -\int \ln|\cos x| + C\)

<|ref|>equation<|/ref|><|det|>[[196, 298, 661, 333]]<|/det|>
\(y = \pm \cos x \cdot e^c \quad \pm e^c = : K\)

<|ref|>equation<|/ref|><|det|>[[196, 342, 666, 368]]<|/det|>
\(y = K \cdot \cos x \quad K \in \mathbb{R} \setminus \{0\}\)

<|ref|>text<|/ref|><|det|>[[160, 399, 580, 427]]<|/det|>
stärische Lösung : \(y \cdot \tan x = 0\) 

<|ref|>equation<|/ref|><|det|>[[425, 437, 500, 462]]<|/det|>
\(y = 0\)

<|ref|>text<|/ref|><|det|>[[130, 475, 595, 501]]<|/det|>
→ alle Lösung der homogenen DGL : 

<|ref|>equation<|/ref|><|det|>[[216, 511, 530, 536]]<|/det|>
\(y_n = K \cdot \cos x \quad K \in \mathbb{R}\)

<|ref|>text<|/ref|><|det|>[[108, 568, 730, 595]]<|/det|>
2. Partikuläre Lösung der inhomogenen DGL 

<|ref|>equation<|/ref|><|det|>[[160, 606, 787, 632]]<|/det|>
\(y_p = K(x) \cdot \cos x \quad \text{Variation der Konstanten}\)

<|ref|>text<|/ref|><|det|>[[160, 640, 852, 682]]<|/det|>
→ in inhomogene DGL einstellen \(y' = \frac{\sin x \cdot \cos x - y \cdot \tan x}{y_p}\) 

<|ref|>equation<|/ref|><|det|>[[160, 680, 857, 707]]<|/det|>
\(K'(x) \cdot \cos x - K(x) \cdot \sin x = \sin x \cdot \cos x - K(x) \cdot \cos x \cdot \frac{\sin x}{\cos x}\)

<|ref|>equation<|/ref|><|det|>[[160, 715, 650, 742]]<|/det|>
\(K'(x) \cdot \cos x = \sin x \cdot \cos x \quad \text{; } \cos x\)

<|ref|>equation<|/ref|><|det|>[[160, 755, 333, 781]]<|/det|>
\(K'(x) = \sin x\)

<|ref|>equation<|/ref|><|det|>[[160, 794, 380, 821]]<|/det|>
\(\int dK = \int \sin x \, dx\)

<|ref|>equation<|/ref|><|det|>[[160, 833, 614, 860]]<|/det|>
\(K(x) = -\cos x + B \quad B \in \mathbb{R}\)

<|ref|>text<|/ref|><|det|>[[130, 872, 512, 899]]<|/det|>
→ \(y_p(x) = (-\cos x + B) \cdot \cos x\) 

<|ref|>text<|/ref|><|det|>[[130, 910, 615, 937]]<|/det|>
→ alle Lösung der inhomogenen DGL : 

<|ref|>equation<|/ref|><|det|>[[216, 949, 740, 975]]<|/det|>
\(y_{\text{alleg}} = y_n + y_p = K \cdot \cos x + B \cdot \cos x - \cos^2 x\)