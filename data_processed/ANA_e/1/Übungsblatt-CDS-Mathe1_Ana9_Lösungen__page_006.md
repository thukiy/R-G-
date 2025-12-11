<|ref|>text<|/ref|><|det|>[[120, 68, 270, 82]]<|/det|>
# Parameter: 

<|ref|>equation<|/ref|><|det|>[[120, 84, 275, 100]]<|/det|>
\(f = (x+1)*2*x;\)

<|ref|>text<|/ref|><|det|>[[120, 109, 503, 127]]<|/det|>
Gemäss Ausgabe erhalten wir die Ableitung 

<|ref|>equation<|/ref|><|det|>[[120, 138, 402, 163]]<|/det|>
\[f'(s) = 2^x \cdot ((x+1) \cdot \ln(2) + 1).\]

<|ref|>text<|/ref|><|det|>[[91, 184, 365, 202]]<|/det|>
f) Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[120, 210, 270, 224]]<|/det|>
# Parameter: 

<|ref|>equation<|/ref|><|det|>[[120, 226, 344, 241]]<|/det|>
\(f = (x+1)*3*x*(-x*2);\)

<|ref|>text<|/ref|><|det|>[[120, 251, 503, 269]]<|/det|>
Gemäss Ausgabe erhalten wir die Ableitung 

<|ref|>equation<|/ref|><|det|>[[1200, 281, 465, 302]]<|/det|>
\[f'(x) = 3^{-x^2} \cdot (-x \cdot (x+1) \cdot \ln(9) + 1).\]

<|ref|>sub_title<|/ref|><|det|>[[75, 336, 295, 353]]<|/det|>
## 8. Diverse Ableitungen 

<|ref|>text<|/ref|><|det|>[[75, 354, 625, 372]]<|/det|>
Wir berechnen jeweils die Ableitung der angegebenen Funktion. 

<|ref|>text<|/ref|><|det|>[[90, 377, 375, 395]]<|/det|>
a) Wir betrachten die Funktion 

<|ref|>equation<|/ref|><|det|>[[120, 406, 270, 426]]<|/det|>
\[f(x) = 5^{x^3 - \sqrt{x} + 7}.\]

<|ref|>text<|/ref|><|det|>[[120, 440, 465, 458]]<|/det|>
Mit Hilfe der Ketten-Regel erhalten wir 

<|ref|>equation<|/ref|><|det|>[[120, 470, 777, 510]]<|/det|>
\[\frac{f'(x)}{x} = (x^3 - \sqrt{x} + 7)' \cdot \ln(5) \cdot 5^{x^3 - \sqrt{x} + 7} = \left(3x^2 - \frac{1}{2\sqrt{x}}\right) \cdot \ln(5) \cdot 5^{x^3 - \sqrt{x}+7}.\]

<|ref|>text<|/ref|><|det|>[[90, 532, 375, 549]]<|/det|>
b) Wir betrachten die Funktion 

<|ref|>equation<|/ref|><|det|>[[120, 561, 312, 582]]<|/det|>
\[f(x) = \log_2(9x^2 - 4).\]

<|ref|>text<|/ref|><|det|>[[120, 593, 465, 611]]<|/det|>
Mit Hilfe der Ketten-Regel erhalten wir 

<|ref|>equation<|/ref|><|det|>[[1200, 622, 720, 710]]<|/det|>
\[\begin{align*} \frac{f'(x)}{x} &= (9x^2 - 4)' \cdot \log_2'(9x^2 - 4) = (9 \cdot 2x^{2-1} - 0) \cdot \frac{1}{\ln(2) \cdot (9x^2 - 4)} \\ &= \frac{18x}{\ln(2) \cdot (9x^2 - 4)}. \end{align*}\]

<|ref|>text<|/ref|><|det|>[[90, 729, 375, 747]]<|/det|>
c) Wir betrachten die Funktion 

<|ref|>equation<|/ref|><|det|>[[120, 758, 848, 824]]<|/det|>
\[\begin{align*} f(x) &= \sqrt[4]{\ln(x^{256})} = \sqrt[4]{\ln(|x|^{256})} = \sqrt[4]{256 \cdot \ln(|x|)} = \sqrt[4]{256} \cdot \sqrt[4]{\ln(|x|)} = 4 \cdot \sqrt[4]{\ln(|x|)} \\ &= 4 \cdot (\ln(|x|))^{\frac{1}{4}}. \end{align*}\]

<|ref|>text<|/ref|><|det|>[[120, 834, 465, 852]]<|/det|>
Mit Hilfe der Ketten-Regel erhalten wir 

<|ref|>equation<|/ref|><|det|>[[1208, 863, 744, 912]]<|/det|>
\[\frac{f'(x)}{x} = 4 \cdot \frac{1}{4} \cdot (\ln(|x|))^{\frac{1}{4}-1} \cdot (\ln(|x|))' = (\ln(|x|))^{-\frac{3}{4}} \cdot \frac{1}{x} = \frac{1}{x \cdot \sqrt[4]{\ln^3(|x|)}}.\]