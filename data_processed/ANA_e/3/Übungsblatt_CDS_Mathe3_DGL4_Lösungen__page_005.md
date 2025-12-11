<|ref|>sub_title<|/ref|><|det|>[[114, 81, 490, 100]]<|/det|>
## 4. Linear inhomogene DGL mit Python 

<|ref|>text<|/ref|><|det|>[[114, 99, 748, 135]]<|/det|>
Bestimmen Sie die allgemeinen Lösungen der DGL aus Aufgabe 3 mit Python/Sympy. 

<|ref|>text<|/ref|><|det|>[[114, 149, 145, 165]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[114, 164, 400, 180]]<|/det|>
# Python initialisieren 

<|ref|>text<|/ref|><|det|>[[114, 180, 469, 197]]<|/det|>
import IPython.display as dp; 

<|ref|>text<|/ref|><|det|>[[114, 196, 350, 212]]<|/det|>
import sympy as sp; 

<|ref|>text<|/ref|><|det|>[[114, 212, 390, 228]]<|/det|>
# Python konfigurieren 

<|ref|>text<|/ref|><|det|>[[114, 228, 345, 245]]<|/det|>
sp.init_printing(); 

<|ref|>text<|/ref|><|det|>[[114, 244, 340, 261]]<|/det|>
x=sp.symbols('x'); 

<|ref|>text<|/ref|><|det|>[[114, 261, 348, 278]]<|/det|>
y=sp.Function('y'); 

<|ref|>text<|/ref|><|det|>[[114, 277, 256, 293]]<|/det|>
# Parameter 

<|ref|>text<|/ref|><|det|>[[114, 293, 857, 310]]<|/det|>
l=y(x).diff(x); r=2*y(x)+1; # linke und rechte Seite der DGL 

<|ref|>text<|/ref|><|det|>[[114, 309, 293, 325]]<|/det|>
# Berechnungen 

<|ref|>text<|/ref|><|det|>[[114, 325, 384, 342]]<|/det|>
L=sp.dsolve(l-r,y(x)); 

<|ref|>text<|/ref|><|det|>[[114, 342, 234, 358]]<|/det|>
# Ausgabe 

<|ref|>text<|/ref|><|det|>[[114, 358, 288, 374]]<|/det|>
dp.display(L); 

<|ref|>text<|/ref|><|det|>[[114, 390, 877, 425]]<|/det|>
Für b) - f) ist der Code analog zu a), nur die Funktionen für die linke und rechte Seite entsprechend ändern. 

<|ref|>sub_title<|/ref|><|det|>[[114, 440, 466, 458]]<|/det|>
## 5. AWP mit linear inhomogener DGL 

<|ref|>text<|/ref|><|det|>[[114, 457, 410, 475]]<|/det|>
Lösen Sie die gegebenen AWP. 

<|ref|>text<|/ref|><|det|>[[114, 473, 690, 499]]<|/det|>
a) DGL: \(y' - 3y - x = 5\) b) DGL: \(y' - \frac{1}{x}y = 2x^2 + x\) 

<|ref|>text<|/ref|><|det|>[[134, 497, 280, 523]]<|/det|>
AB: \(y(0) = -\frac{7}{9}\) 

<|ref|>text<|/ref|><|det|>[[472, 497, 610, 523]]<|/det|>
AB: \(y(2) = 12\) 

<|ref|>text<|/ref|><|det|>[[114, 521, 512, 540]]<|/det|>
c) Lösen Sie Aufgabe a) mit Python/Sympy. 

<|ref|>text<|/ref|><|det|>[[114, 555, 145, 571]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[114, 570, 820, 608]]<|/det|>
Analytisch isolierte Form der DGL: \(y' = 3y + x + 5\) mit \(m(x) = 3\) und \(q(x) = x+5\). Für die Stammfunktion von \(m(x)\) und die Konstante \(C(x)\) ergibt sich 

<|ref|>equation<|/ref|><|det|>[[114, 605, 410, 625]]<|/det|>
\[M(x) = \int m(x)dx = \int 3x dx = 3x\]

<|ref|>equation<|/ref|><|det|>[[124, 628, 841, 792]]<|/det|>
\[ 
\begin{aligned}
C(x) &= \int_{x_0}^{x} q(s) \cdot e^{-M(s)} \, ds = \int_{0}^{x} (s+5) \cdot e^{-3s} \, ds = \left[ (s+5) \cdot \frac{e^{-3s}}{-3} \right]_{0}^{x} - \int_{0}^{x} 1 \cdot \frac{e^{-3s}}{-3} \, ds \\
&= (x+5) \cdot \frac{e^{-3x}}{-3} - (0+5) \cdot \frac{e^{-3\cdot 0}}{-3} + \frac{1}{3} \int_{0}^{x} e^{-3s} \, ds = -\frac{x+5}{3} \cdot e^{-3x} + \frac{5}{3} + \frac{1}{3} \cdot \left[ \frac{e^{-3s}}{-3} \right]_{0}^{x} \\
&= -\frac{x+5}{3} \cdot e^{-3x} + \frac{1}{3} \cdot e^{-3x} + \frac{1}{9} \cdot e^{-3\cdot 0} = -\frac{3x+15+1}{9} \cdot e^{-3x} + \frac{15+1}{9} \\
&= \frac{16}{9} - \frac{3x+16}{9} \cdot e^{-3x}.
\end{aligned}
\]

<|ref|>text<|/ref|><|det|>[[114, 806, 585, 825]]<|/det|>
Somit ergibt sich für die Lösung des AWP für \(x \ge x_0\):