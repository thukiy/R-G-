<|ref|>sub_title<|/ref|><|det|>[[107, 66, 640, 85]]<|/det|>
## 9. Integrale von Polynom-Funktionen mit Python/Sympy 

<|ref|>text<|/ref|><|det|>[[107, 84, 921, 120]]<|/det|>
Wir berechnen die *Integrale* aus Aufgabe 9 mit Python/Sympy. Dazu implementieren wir den folgenden Code, den wir für jede Teilaufgabe modifizieren. 

<|ref|>text<|/ref|><|det|>[[107, 126, 440, 320]]<|/det|>
# Python initialisieren:
import IPython.display as dp;
import sympy as sp;
# Python konfigurieren:
sp.init_printing();
x=sp.symbols('x');
# Parameter:
f=..., x_0=..., x_E=...;
# Berechnungen:
I=sp.integrate(f, (x, x_0, x_E));
# Ausgabe:
dp.display(I); 

<|ref|>text<|/ref|><|det|>[[121, 330, 395, 349]]<|/det|>
a) Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[150, 355, 459, 450]]<|/det|>
# Parameter:
f=2*x-1; x_0=0; x_E=3;
Gemäss Ausgabe erhalten wir das *Integral*
\[
I = 6.
\]

<|ref|>text<|/ref|><|det|>[[121, 463, 395, 481]]<|/det|>
b) Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[150, 487, 420, 522]]<|/det|>
# Parameter:
f=2*x-1; x_0=-1; x_E=1; 

<|ref|>text<|/ref|><|det|>[[150, 528, 523, 546]]<|/det|>
Gemäss Ausgabe erhalten wir das *Integral* 

<|ref|>text<|/ref|><|det|>[[150, 555, 225, 577]]<|/det|>
\[
I = -2.
\] 

<|ref|>text<|/ref|><|det|>[[121, 594, 395, 612]]<|/det|>
c) Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[150, 618, 533, 653]]<|/det|>
# Parameter:
f=6*x**2-8*x**3+1; x_0=-2; x_E=1;
Gemäss Ausgabe erhalten wir das *Integral* 

<|ref|>text<|/ref|><|det|>[[150, talk="0" style="font-size: 0.8em; font-family: monospace; line-height: 1.5em; white-space: pre;">I = 51."> 

<|ref|>text<|/ref|><|det|>[[121, 725, 395, 743]]<|/det|>
d) Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[150, 750, 544, 784]]<|/det|>
# Parameter:
f=6*x**2-8*x**3+1;
x_0=-2;
x_E=-1;
Gemäss Ausgabe erhalten wir das *Integral* 

<|ref|>text<|/ref|><|det|>[[151, 793, 225, 814]]<|/det|>
\[
I = 45.
\] 

<|ref|>text<|/ref|><|det|>[[121, 860, 395, 878]]<|/det|>
e) Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[150, 884, 280, 899]]<|/det|>
# Parameter:
f=2/3-16*x**4; x_0=1; x_E=3/2;