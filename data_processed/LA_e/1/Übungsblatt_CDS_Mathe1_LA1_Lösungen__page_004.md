<|ref|>text<|/ref|><|det|>[[117, 65, 889, 102]]<|/det|>
Zusätzlich fällt auf, dass die Terme in jedem auftretenden *Polynom* in absteigender Reihenfolge nach *Potenzen* sortiert werden. 

<|ref|>sub_title<|/ref|><|det|>[[90, 110, 338, 129]]<|/det|>
### c) Keine Lösung verfügbar. 

<|ref|>sub_title<|/ref|><|det|>[[75, 150, 472, 169]]<|/det|>
## 6. Terme Faktorisieren mit Python/Sympy 

<|ref|>text<|/ref|><|det|>[[75, 167, 889, 203]]<|/det|>
Wir *faktorisieren* jeweils den Term mit Python/Sympy. Dazu implementieren wir den folgenden Code, den wir für jede Teilaufgabe modifizieren. 

<|ref|>text<|/ref|><|det|>[[75, 208, 415, 401]]<|/det|>
# Python initialisieren:
import IPython.display as dp;
import sympy as sp;
# Python konfigurieren:
sp.init_printing();
...=sp.symbols('...');
# Parameter:
p=...;
# Berechnungen:
q=sp.factor(p);
# Ausgabe:
dp.display(q); 

<|ref|>sub_title<|/ref|><|det|>[[90, 411, 350, 429]]<|/det|>
### a) Wir betrachten den Term 

<|ref|>equation<|/ref|><|det|>[[117, 437, 888, 456]]<|/det|>
\[p = x^3 - 4x. \qquad (8)\]

<|ref|>text<|/ref|><|det|>[[117, 465, 361, 483]]<|/det|>
Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[117, 490, 387, 555]]<|/det|>
# Python konfigurieren:
x=sp.symbols('x');
# Parameter:
p=x**3-4*x; 

<|ref|>text<|/ref|><|det|>[[117, 562, 305, 580]]<|/det|>
Gemäss Ausgabe gilt 

<|ref|>equation<|/ref|><|det|>[[117, 588, 888, 610]]<|/det|>
\[p = (x + 2) \cdot x \cdot (x - 2). \qquad (9)\]

<|ref|>sub_title<|/ref|><|det|>[[90, 626, 350, 644]]<|/det|>
### b) Wir betrachten den Term 

<|ref|>equation<|/ref|><|det|>[[117, 652, 888, 671]]<|/det|>
\[p = 2xy - 3x^3y - 2y^3 + 3x^2y^3. \qquad (10)\]

<|ref|>text<|/ref|><|det|>[[117, 680, 360, 697]]<|/det|>
Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[117, 704, 387, 720]]<|/det|>
# Python konfigurieren:
x,y=sp.symbols('x y');
# Parameter:
p=2*x*y-3*x**3*y-2*y**3+3*x**2*y**3; 

<|ref|>text<|/ref|><|det|>[[117, 722, 255, 737]]<|/det|>
# Parameter:
p=2*x*y-3*x**3*y-2*y**3 + 3*x**2*y**3; 

<|ref|>text<|/ref|><|det|>[[117, 778, 305, 795]]<|/det|>
Gemäss Ausgabe gilt 

<|ref|>equation<|/ref|><|det|>[[117, 802, 888, 825]]<|/det|>
\[p = y \cdot (3x^2 - 2) \cdot (y^2 - x). \qquad (11)\]

<|ref|>sub_title<|/ref|><|det|>[[90, 842, 350, 860]]<|/det|>
### c) Wir betrachten den Term 

<|ref|>equation<|/ref|><|det|>[[117, 868, 888, 888]]<|/det|>
\[p = b^4 + a^3b - a^2b^2 - ab^3. \qquad (12)\]

<|ref|>text<|/ref|><|det|>[[117, 897, 360, 915]]<|/det|>
Wir modifizieren den Code.