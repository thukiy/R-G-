<|ref|>equation<|/ref|><|det|>[[119, 84, 290, 103]]<|/det|>
\[C_1 = y_0 = 5\]

<|ref|>equation<|/ref|><|det|>[[119, 110, 536, 147]]<|/det|>
\[C_2 = v_0 - \lambda \cdot y_0 = -1 - \frac{1}{2} \cdot 5 = -1 - 2.5 = -3.5\]

<|ref|>equation<|/ref|><|det|>[[119, 144, 743, 174]]<|/det|>
\[\frac{y(x)}{x} = C_1 \cdot y_1(x) + C_2 \cdot y_2(x) = 5 \cdot e^{0.5 \cdot (x-0)} - 3.5 \cdot (x-0) \cdot e^{0.5 \cdot (x-0)}\]

<|ref|>equation<|/ref|><|det|>[[163, 182, 337, 210]]<|/det|>
\[= (5 - 3.5x) e^{0.5x}.\]

<|ref|>equation<|/ref|><|det|>[[117, 226, 246, 250]]<|/det|>
\[\lim_{x \to \infty} y(x) \to \infty\]

<|ref|>text<|/ref|><|det|>[[115, 265, 144, 282]]<|/det|>
d) 

<|ref|>text<|/ref|><|det|>[[115, 281, 853, 333]]<|/det|>
Unterschied zu c) ist die Wahl der Referenzstelle, also die Anfangsbedingung – es gilt hier x₀ = 2. Die Lösung des AWP lässt sich durch Verschiebung um Δx = 2 entlang der positiven x-Achse gewinnen. 

<|ref|>equation<|/ref|><|det|>[[119, 333, 696, 360]]<|/det|>
\[\frac{y(x)}{x} = (5 - 3.5 \cdot (x - 2)) e^{0.5 \cdot (x-2)} = (5 - 3.5 \cdot x + 3.5 \cdot 2)) e^{0.5x-0.5 \cdot 2}\]

<|ref|>equation<|/ref|><|det|>[[163, 368, 345, 388]]<|/det|>
\[= (12 - 3.5x) e^{0.5x-1}.\]

<|ref|>equation<|/ref|><|det|>[[117, 393, 260, 419]]<|/det|>
\[\lim_{x \to \infty} y(x) \to -\infty\]

<|ref|>title<|/ref|><|det|>[[115, 431, 540, 450]]<|/det|>
7. DGL 2. Ordnung mit Python/Sympy lösen 

<|ref|>text<|/ref|><|det|>[[115, 448, 880, 483]]<|/det|>
a) Benutzen Sie Python/Sympy, um die Lösungen der DGL 2. Ordnung von Aufgabe 4 zu bestimmen. 

<|ref|>text<|/ref|><|det|>[[115, 481, 881, 515]]<|/det|>
b) Benutzen Sie Python/Sympy, um die Lösungen der AWP mit DGL 2. Ordnung von Aufgabe 6 zu bestimmen. 

<|ref|>text<|/ref|><|det|>[[115, 532, 144, 548]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[115, 546, 230, 564]]<|/det|>
Aufgabe 4a: 

<|ref|>text<|/ref|><|det|>[[115, 563, 450, 780]]<|/det|>
# Python initialisieren
import IPython.display as dp;
import sympy as sp;
# Python konfigurieren
# sp.init_printing();
x=sp.symbols('x');
y=sp.Function('y');
# Parameter
a=1; b=3; c=-4;
# Berechnungen
l=a*y(x).diff(x,2)+b*y(x).diff(x)+c*y(x); r=0;
L=sp.dsolve(l-r,y(x));
# Ausgabe
dp.display(L); 

<|ref|>text<|/ref|><|det|>[[145, 807, 822, 841]]<|/det|>
➔ Aufgaben 4b – f analog, nur die Parameter a, b und c müssen verändert eingegeben werden