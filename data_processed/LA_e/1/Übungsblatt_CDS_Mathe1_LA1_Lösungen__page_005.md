<|ref|>text<|/ref|><|det|>[[150, 68, 419, 83]]<|/det|>
# Python konfigurieren: 

<|ref|>text<|/ref|><|det|>[[150, 84, 410, 100]]<|/det|>
a, b=sp.symbols('a b'); 

<|ref|>text<|/ref|><|det|>[[150, 100, 293, 115]]<|/det|>
# Parameter: 

<|ref|>text<|/ref|><|det|>[[150, 116, 512, 132]]<|/det|>
p=b**4+a**3*b-a**2*b**2-a*b**3; 

<|ref|>text<|/ref|><|det|>[[150, 142, 339, 160]]<|/det|>
Gemäss Ausgabe gilt 

<|ref|>equation<|/ref|><|det|>[[149, 170, 373, 196]]<|/det|>
\[
p = b \cdot (a - b)^2 \cdot (a + b).
\]

<|ref|>text<|/ref|><|det|>[[880, 171, 920, 189]]<|/det|>
(13) 

<|ref|>sub_title<|/ref|><|det|>[[108, 227, 508, 246]]<|/det|>
7. Terme Vereinfachen mit Python/Sympy 

<|ref|>text<|/ref|><|det|>[[108, 245, 920, 280]]<|/det|>
Wir *vereinfachen* jeweils den Term mit Python/Sympy. Dazu implementieren wir den folgenden Code, den wir für jede Teilaufgabe modifizieren. 

<|ref|>text<|/ref|><|det|>[[108, 287, 400, 303]]<|/det|>
# Python initialisieren: 

<|ref|>text<|/ref|><|det|>[[108, 303, 445, 320]]<|/det|>
import IPython.display as dp; 

<|ref|>text<|/ref|><|det|>[[108, 320, 340, 336]]<|/det|>
import sympy as sp; 

<|ref|>text<|/ref|><|det|>[[108, 336, 377, 352]]<|/det|>
# Python konfigurieren: 

<|ref|>text<|/ref|><|det|>[[108, 352, 333, 368]]<|/det|>
sp.init_printing(); 

<|ref|>text<|/ref|><|det|>[[108, 368, 320, 384]]<|/det|>
x=sp.symbols('x'); 

<|ref|>text<|/ref|><|det|>[[108, 384, 252, 400]]<|/det|>
# Parameter: 

<|ref|>text<|/ref|><|det|>[[108, 401, 189, 416]]<|/det|>
p=...; 

<|ref|>text<|/ref|><|det|>[[108, 416, 293, 432]]<|/det|>
# Berechnungen: 

<|ref|>text<|/ref|><|det|>[[108, 432, 308, 448]]<|/det|>
q=sp.simplify(p); 

<|ref|>text<|/ref|><|det|>[[108, 448, 231, 464]]<|/det|>
# Ausgabe: 

<|ref|>text<|/ref|><|det|>[[108, 464, 272, 481]]<|/det|>
dp.display(q); 

<|ref|>text<|/ref|><|det|>[[122, 493, 378, 510]]<|/det|>
a) Wir betrachten den Term 

<|ref|>equation<|/ref|><|det|>[[150, 521, 402, 542]]<|/det|>
\[
p = 5x^2 + 3x^3 - 11x^2 + 3x.
\]

<|ref|>text<|/ref|><|det|>[[880, 524, 920, 542]]<|/det|>
(14) 

<|ref|>text<|/ref|><|det|>[[150, 555, 393, 573]]<|/det|>
Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[150, 581, 296, 596]]<|/det|>
# Parameter: 

<|ref|>equation<|/ref|><|det|>[[150, 597, 475, 613]]<|/det|>
\[
p=5*x**2+3*x**3-11*x**2+3*x;
\]

<|ref|>text<|/ref|><|det|>[[150, 622, 339, 640]]<|/det|>
Gemäss Ausgabe gilt 

<|ref|>equation<|/ref|><|det|>[[150, 650, 295, 676]]<|/det|>
\[
p = 3x(x-1)^2.
\]

<|ref|>text<|/ref|><|det|>[[880, 653, 920, 671]]<|/det|>
(15) 

<|ref|>text<|/ref|><|det|>[[122, 697, 377, 714]]<|/det|>
b) Wir betrachten den Term 

<|ref|>equation<|/ref|><|det|>[[150, 725, 373, 762]]<|/det|>
\[
p = \frac{13 - 3x^4 - 3x^2 - 7}{2x^2 + 6 + x^2}.
\]

<|ref|>text<|/ref|><|det|>[[880, 735, 920, 753]]<|/det|>
(16) 

<|ref|>text<|/ref|><|det|>[[150, 772, 393, 790]]<|/det|>
Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[150, 799, 293, 814]]<|/det|>
# Parameter: 

<|ref|>equation<|/ref|><|det|>[[150, 814, 600, 831]]<|/det|>
\[
p = (13 - 3*x**4 - 3*x**2 - 7) / (2*x**2 + 6 + x**2);
\]

<|ref|>text<|/ref|><|det|>[[150, 840, 339, 858]]<|/det|>
Gemäss Ausgabe gilt 

<|ref|>equation<|/ref|><|det|>[[150, 868, 255, 894]]<|/det|>
\[
p = 1 - x^2.
\]

<|ref|>text<|/ref|><|det|>[[880, 871, 920, 889]]<|/det|>
(17)