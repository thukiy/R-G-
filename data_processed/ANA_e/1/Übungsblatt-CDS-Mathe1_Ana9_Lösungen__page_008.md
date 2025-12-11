<|ref|>text<|/ref|><|det|>[[88, 65, 364, 84]]<|/det|>
a) Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[118, 91, 260, 106]]<|/det|>
# Parameter: 

<|ref|>equation<|/ref|><|det|>[[118, 106, 410, 124]]<|/det|>
\[f=5\ast\ast(x\ast\ast3-sp.sqrt(x)+7);\]

<|ref|>text<|/ref|><|det|>[[118, 132, 501, 151]]<|/det|>
Gemäss Ausgabe erhalten wir die Ableitung 

<|ref|>equation<|/ref|><|det|>[[118, 160, 463, 205]]<|/det|>
\[f'(x) = \frac{5^{-\sqrt{x}+x^3+7} \cdot (6 \cdot x^{\frac{5}{2}} - 1) \cdot \ln(5)}{2 \cdot \sqrt{x}}.\]

<|ref|>text<|/ref|><|det|>[[88, 215, 364, 233]]<|/det|>
b) Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[118, 240, 260, 255]]<|/det|>
# Parameter: 

<|ref|>equation<|/ref|><|det|>[[118, 255, 364, 273]]<|/det|>
\[f=sp.log(9\ast\ast\ast2-4,2);\]

<|ref|>text<|/ref|><|det|>[[118, 281, 501, 299]]<|/det|>
Gemäss Ausgabe erhalten wir die Ableitung 

<|ref|>equation<|/ref|><|det|>[[1188, 310, 360, 353]]<|/det|>
\[f'(x) = \frac{18 \cdot x}{(9 \cdot x^2 - 4) \cdot \ln(2)}.\]

<|ref|>text<|/ref|><|det|>[[88, 361, 364, 379]]<|/det|>
c) Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[118, 386, 260, 401]]<|/det|>
# Parameter: 

<|ref|>equation<|/ref|><|det|>[[118, 401, 421, 419]]<|/det|>
\[f=(sp.log(x\ast\ast256))\ast\ast(1/4);\]

<|ref|>text<|/ref|><|det|>[[118, 426, 501, 445]]<|/det|>
Gemäss Ausgabe erhalten wir die Ableitung 

<|ref|>equation<|/ref|><|det|>[[1180, 456, 330, 499]]<|/det|>
\[f'(x) = \frac{64.0}{x \cdot \ln^{0.75}(x^{256})}.\]

<|ref|>text<|/ref|><|det|>[[88, 508, 364, 526]]<|/det|>
d) Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[118, 533, 260, 548]]<|/det|>
# Parameter: 

<|ref|>equation<|/ref|><|det|>[[118, 548, 343, 566]]<|/det|>
\[f=1/(1+sp.exp(-x));\]

<|ref|>text<|/ref|><|det|>[[118, 574, 501, 592]]<|/det|>
Gemäss Ausgabe erhalten wir die Ableitung 

<|ref|>equation<|/ref|><|det|>[[1189, 603, 310, 646]]<|/det|>
\[f'(x) = \frac{1}{4 \cdot \cosh^2\left(\frac{x}{2}\right)}.\]

<|ref|>text<|/ref|><|det|>[[88, 655, 364, 673]]<|/det|>
e) Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[118, 680, 260, 696]]<|/det|>
# Parameter: 

<|ref|>equation<|/ref|><|det|>[[118, 696, 410, 714]]<|/det|>
\[f=(sp.log(x))\ast\ast sp.log(x);\]

<|ref|>text<|/ref|><|det|>[[118, 722, 501, 740]]<|/det|>
Gemäss Ausgabe erhalten wir die Ableitung 

<|ref|>equation<|/ref|><|det|>[[1185, 750, 430, 802]]<|/det|>
\[f'(x) = \frac{\left(\ln(\ln(x)) + 1\right) \cdot \ln^{\ln(x)}(x)}{x}.\]

<|ref|>text<|/ref|><|det|>[[88, 810, 364, 829]]<|/det|>
f) Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[118, 836, 260, 851]]<|/det|>
# Parameter: 

<|ref|>equation<|/ref|><|det|>[[1188, 852, 548, 870]]<|/det|>
\[f=2\ast\ast(-sp.sqrt(sp.Abs(x)))/sp.log(2);\]

<|ref|>equation<|/ref|><|det|>[[1180, 880, 400, 942]]<|/det|>
\[f'(x) = \begin{cases} 0 & |x = 0 \\ -\frac{2^{-\sqrt{|x|-1}} \cdot x}{|x^{\frac{3}{2}}|} & \text{sonst.} \end{cases}\]