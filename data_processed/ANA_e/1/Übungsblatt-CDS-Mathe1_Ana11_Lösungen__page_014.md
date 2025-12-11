<|ref|>sub_title<|/ref|><|det|>[[75, 65, 460, 84]]<|/det|>
## 6. Aufleitungen von Polynom-Funktionen 

<|ref|>text<|/ref|><|det|>[[75, 83, 789, 102]]<|/det|>
Wir berechnen die folgenden *unbestimmten Integrale* durch elementares *Aufleiten*. 

<|ref|>text<|/ref|><|det|>[[90, 106, 240, 125]]<|/det|>
a) Wir erhalten 

<|ref|>equation<|/ref|><|det|>[[118, 137, 888, 173]]<|/det|>
\[
F(x) = \int (2x + 1) \, dx = 2 \cdot \frac{1}{2} x^2 + 1 \cdot x + c = \frac{x^2 + x + c}{2}. \quad (26)
\]

<|ref|>text<|/ref|><|det|>[[90, 181, 240, 199]]<|/det|>
b) Wir erhalten 

<|ref|>equation<|/ref|><|det|>[[118, 210, 888, 247]]<|/det|>
\[
F(x) = \int (4x - 8) \, dx = 4 \cdot \frac{1}{2} x^2 - 8x + c = 2x^2 - 8x + c. \quad (27)
\]

<|ref|>text<|/ref|><|det|>[[90, 250, 240, 268]]<|/det|>
c) Wir erhalten 

<|ref|>equation<|/ref|><|det|>[[118, 280, 888, 317]]<|/det|>
\[
F(x) = \int (12x^2 + 17) \, dx = 12 \cdot \frac{1}{3} x^3 + 17x + c = 4x^3 + 17x + c. \quad (28)
\]

<|ref|>text<|/ref|><|det|>[[90, 330, 240, 348]]<|/det|>
d) Wir erhalten 

<|ref|>equation<|/ref|><|det|>[[118, 360, 888, 396]]<|/det|>
\[
F(x) = \int (3x^2 - 6x) \, dx = 3 \cdot \frac{1}{3} x^3 - 6 \cdot \frac{1}{2} x^2 + c = \frac{x^3 - 3x^2 + c}{2}. \quad (29)
\]

<|ref|>text<|/ref|><|det|>[[90, 411, 240, 429]]<|/det|>
e) Wir erhalten 

<|ref|>equation<|/ref|><|det|>[[118, 441, 888, 477]]<|/det|>
\[
F(x) = \int (6x^2 - 4x + 3) \, dx = 6 \cdot \frac{1}{3} x^3 - 4 \cdot \frac{1}{2} x^2 + 3x + c = \frac{2x^3 - 2x^2 + 3x + c}{2}. \quad (30)
\]

<|ref|>text<|/ref|><|det|>[[90, 492, 240, 510]]<|/det|>
f) Wir erhalten 

<|ref|>equation<|/ref|><|det|>[[118, 522, 888, 558]]<|/det|>
\[
F(x) = \int (8x - 1 + 9x^2) \, dx = 8 \cdot \frac{1}{2} x^2 - 1 \cdot x + 9 \cdot \frac{1}{3} \cdot x^3 + c = \frac{4x^2 - x + 3x^3 + c}{2}. \quad (31)
\]

<|ref|>sub_title<|/ref|><|det|>[[75, 602, 642, 620]]<|/det|>
## 7. Aufleitungen von Polynom-Funktionen mit Python/Sympy 

<|ref|>text<|/ref|><|det|>[[75, 619, 888, 654]]<|/det|>
Wir berechnen die *unbestimmten Integrale* aus Aufgabe 7 mit Python/Sympy. Dazu implementieren wir den folgenden Code, den wir für jede Teilaufgabe modifizieren. 

<|ref|>text<|/ref|><|det|>[[75, 661, 411, 875]]<|/det|>
# Python initialisieren:
import IPython.display as dp;
import sympy as sp;
# Python konfigurieren:
sp.init_printing();
x=sp.symbols('x');
# Parameter:
f=...;
# Berechnungen:
F=sp.expand(sp.integrate(f,x));
# Ausgabe:
dp.display(f);
dp.display(F); 

<|ref|>text<|/ref|><|det|>[[90, 885, 364, 903]]<|/det|>
a) Wir modifizieren den Code.