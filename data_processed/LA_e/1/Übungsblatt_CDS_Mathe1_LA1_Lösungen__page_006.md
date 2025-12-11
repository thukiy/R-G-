<|ref|>text<|/ref|><|det|>[[90, 65, 350, 84]]<|/det|>
c) Wir betrachten den Term 

<|ref|>equation<|/ref|><|det|>[[117, 93, 888, 115]]<|/det|>
\[p = 2(3 + 3\tan^2(x)) \cdot \cos^2(x). \qquad (18)\]

<|ref|>text<|/ref|><|det|>[[117, 125, 363, 143]]<|/det|>
Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[117, 150, 260, 165]]<|/det|>
# Parameter: 

<|ref|>equation<|/ref|><|det|>[[117, 167, 536, 183]]<|/det|>
\[p=2*(3+3*\text{sp}.\tan(x)*2)*\text{sp}.\cos(x)*2;\]

<|ref|>text<|/ref|><|det|>[[117, 192, 306, 210]]<|/det|>
Gemäss Ausgabe gilt 

<|ref|>equation<|/ref|><|det|>[[117, 222, 178, 241]]<|/det|>
\[p = 6.\]

<|ref|>text<|/ref|><|det|>[[845, 223, 888, 241]]<|/det|>
(19) 

<|ref|>sub_title<|/ref|><|det|>[[75, 273, 456, 292]]<|/det|>
## 8. Gleichungen lösen mit Python/Sympy 

<|ref|>text<|/ref|><|det|>[[75, 291, 888, 326]]<|/det|>
Wir *vereinfachen* jeweils die Gleichung mit Python/Sympy. Dazu implementieren wir den folgenden Code, den wir für jede Teilaufgabe modifizieren. 

<|ref|>text<|/ref|><|det|>[[75, 333, 411, 526]]<|/det|>
# Python initialisieren:
import IPython.display as dp;
import sympy as sp;
# Python konfigurieren:
sp.init_printing();
x=sp.symbols('x');
# Parameter:
l=..., r=..., 
# Berechnungen:
L=sp.solve(l-r,x);
# Ausgabe:
dp.display(L); 

<|ref|>text<|/ref|><|det|>[[90, 538, 380, 556]]<|/det|>
a) Wir betrachten die *Gleichung* 

<|ref|>equation<|/ref|><|det|>[[117, 567, 234, 585]]<|/det|>
\[3x + 5 = 17.\]

<|ref|>text<|/ref|><|det|>[[845, 567, 888, 585]]<|/det|>
(20) 

<|ref|>text<|/ref|><|det|>[[117, 597, 360, 615]]<|/det|>
Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[117, 622, 260, 638]]<|/det|>
# Parameter: 

<|ref|>equation<|/ref|><|det|>[[117, 640, 283, 656]]<|/det|>
\[l=3*x+5; \quad r=17;\]

<|ref|>text<|/ref|><|det|>[[117, 665, 456, 683]]<|/det|>
Gemäss Ausgabe ist die *Lösungsmenge* 

<|ref|>equation<|/ref|><|det|>[[117, 693, 200, 713]]<|/det|>
\[\mathcal{L} = \{4\}.\]

<|ref|>text<|/ref|><|det|>[[845, 694, 888, 712]]<|/det|>
(21) 

<|ref|>text<|/ref|><|det|>[[90, 734, 380, 752]]<|/det|>
b) Wir betrachten die *Gleichung* 

<|ref|>equation<|/ref|><|det|>[[117, 763, 310, 782]]<|/det|>
\[3x^2 - 36x + 107 = 2.\]

<|ref|>text<|/ref|><|det|>[[845, 763, 888, 782]]<|/det|>
(22) 

<|ref|>text<|/ref|><|det|>[[117, 794, 360, 812]]<|/det|>
Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[117, 820, 260, 835]]<|/det|>
# Parameter: 

<|ref|>equation<|/ref|><|det|>[[117, 837, 385, 852]]<|/det|>
\[l=3*x*2-36*x+107; \quad r=2;\]

<|ref|>text<|/ref|><|det|>[[117, 862, 456, 880]]<|/det|>
Gemäss Ausgabe ist die *Lösungsmenge* 

<|ref|>equation (23) 
\[\mathcal{L} = \{5,7\}.\]