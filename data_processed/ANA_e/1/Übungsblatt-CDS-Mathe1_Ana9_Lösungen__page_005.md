<|ref|>sub_title<|/ref|><|det|>[[107, 67, 608, 86]]<|/det|>
## 7. Diverse Ableitungen berechnen mit Python/Sympy 

<|ref|>text<|/ref|><|det|>[[107, 85, 923, 121]]<|/det|>
Wir berechnen die *Ableitungen* aus Aufgabe 6 mit Python/Sympy. Dazu implementieren wir den folgenden Code, den wir für jede Teilaufgabe modifizieren. 

<|ref|>text<|/ref|><|det|>[[107, 127, 444, 335]]<|/det|>
# Python initialisieren:
import IPython.display as dp;
import sympy as sp;
# Python konfigurieren:
sp.init_printing();
x=sp.symbols('x');
# Parameter:
f=...
# Berechnungen:
fs=sp.simplify(sp.diff(f,x));
# Ausgabe:
dp.display(f);
dp.display(fs); 

<|ref|>text<|/ref|><|det|>[[121, 347, 395, 365]]<|/det|>
a) Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[150, 372, 300, 404]]<|/det|>
# Parameter:
f=sp.exp(-x); 

<|ref|>text<|/ref|><|det|>[[150, 412, 533, 430]]<|/det|>
Gemäss Ausgabe erhalten wir die *Ableitung* 

<|ref|>equation<|/ref|><|det|>[[150, 440, 280, 468]]<|/det|>
\[
\frac{f'(x) = -e^{-x}}{x}.
\]

<|ref|>text<|/ref|><|det|>[[121, 485, 395, 503]]<|/det|>
b) Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[150, 510, 315, 542]]<|/det|>
# Parameter:
f=x*sp.exp(x); 

<|ref|>text<|/ref|><|det|>[[150, 550, 533, 567]]<|/det|>
Gemäss Ausgabe erhalten wir die *Ableitung* 

<|ref|>equation<|/ref|> rightset
\[
\frac{f'(x) = (x+1) \cdot e^x}{x}.
\]

<|ref|>text<|/ref|><|det|>[[121, 622, 395, 639]]<|/det|>
c) Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[150, 647, 360, 679]]<|/det|>
# Parameter:
f=(x+2)*sp.exp(x); 

<|ref|>text<|/ref|><|det|>[[150, 687, 533, 705]]<|/det|>
Gemäss Ausgabe erhalten wir die *Ableitung* 

<|ref|>equation<|/ref|>rights
\[
\frac{f'(x) = (x+3) \cdot e^x}{x}.
\]

<|ref|>text<|/ref|><|det|>[[121, 759, 395, 777]]<|/det|>
d) Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[150, 785, 300, 817]]<|/det|>
# Parameter:
f=sp.exp(-x**2); 

<|ref|>text<|/ref|><|det|>[[150, 825, 533, 842]]<|/det|>
Gemäss Ausgabe erhalten wir die *Ableitung* 

<|ref|>equation<|/ref|>left
\[
\frac{\dot{f}(t) = -2 \cdot x \cdot e^{-x^2}}{x}.
\]

<|ref|>text<|/ref|><|det|>[[121, 897, 395, 915]]<|/det|>
e) Wir modifizieren den Code.