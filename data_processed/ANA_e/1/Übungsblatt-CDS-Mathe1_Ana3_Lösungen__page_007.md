<|ref|>sub_title<|/ref|><|det|>[[107, 66, 530, 85]]<|/det|>
## 7. Grenzwerte berechnen mit Python/Sympy 

<|ref|>text<|/ref|><|det|>[[107, 84, 920, 120]]<|/det|>
Wir berechnen die *Grenzwerte* aus Aufgabe 6 mit Python/Sympy. Dazu implementieren wir den folgenden Code, den wir für jede Teilaufgabe modifizieren. 

<|ref|>text<|/ref|><|det|>[[107, 127, 444, 336]]<|/det|>
# Python initialisieren:
import IPython.display as dp;
import sympy as sp;
# Python konfigurieren:
sp.init_printing();
a,n=sp.symbols('a,n');
# Parameter:
a_n=...;
# Berechnungen:
a=sp.limit_seq(a_n,n);
# Ausgabe:
dp.display(a_n);
dp.display(a); 

<|ref|>text<|/ref|><|det|>[[121, 348, 395, 366]]<|/det|>
a) Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[150, 373, 293, 405]]<|/det|>
# Parameter:
a_n=3/(n+2); 

<|ref|>text<|/ref|><|det|>[[150, 414, 730, 433]]<|/det|>
Gemäss Ausgabe *konvergiert* die *Folge* gegen den *Grenzwert* \(a=0\). 

<|ref|>text<|/ref|><|det|>[[121, 445, 395, 463]]<|/det|>
b) Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[150, 471, 293, 503]]<|/det|>
# Parameter:
a_n=(n+2)/3; 

<|ref|>text<|/ref|><|det|>[[150, 512, 476, 530]]<|/det|>
Gemäss Ausgabe *divergiert* die *Folge*. 

<|ref|>text<|/ref|><|det|>[[121, 545, 395, 563]]<|/det|>
c) Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[150, 571, 338, 602]]<|/det|>
# Parameter:
a_n=(n+2)/(3*n); 

<|ref|>text<|/ref|><|det|>[[150, 610, 730, 633]]<|/det|>
Gemäss Ausgabe *konvergiert* die *Folge* gegen die *Grenzwert* \(a=\frac{1}{3}\). 

<|ref|>text<|/ref|><|det|>[[121, 647, 395, 665]]<|/det|>
d) Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[150, 673, 293, 704]]<|/det|>
# Parameter:
a_n=3*n/(n+2); 

<|ref|>text<|/ref|><|det|>[[150, 713, 730, 732]]<|/det|>
Gemäss Ausgabe *konvergiert* die *Folge* gegen der *Grenzwert* \(a=3\). 

<|ref|>text<|/ref|><|det|>[[121, 745, 395, 763]]<|/det|>
e) Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[150, 771, 293, 802]]<|/det|>
# Parameter:
a_n=3*n/(6*n+2); 

<|ref|>text<|/ref|><|det|>[[150, 811, 730, 833]]<|/det|>
Gemäss Ausgabe *konvergiert* die *Folge* gegen dem *Grenzwert* \(a=\frac{1}{2}\). 

<|ref|>text<|/ref|><|det|>[[121, 847, 395, 865]]<|/det|>
f) Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[150, 873, 293, 885]]<|/det|>
# Parameter:
a_n=(4-n**2)/(2+n)**2;