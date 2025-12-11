<|ref|>text<|/ref|><|det|>[[90, 66, 238, 85]]<|/det|>
c) Wir erhalten 

<|ref|>equation<|/ref|><|det|>[[117, 95, 888, 145]]<|/det|>
\[ \sum_{k=-2}^{2} k^3 = (-2)^3 + (-1)^3 + 0^3 + 1^3 + 2^3 = -8 - 1 + 0 + 1 + 8 = 0. \quad (4) \]

<|ref|>text<|/ref|><|det|>[[90, 165, 238, 183]]<|/det|>
d) Wir erhalten 

<|ref|>equation<|/ref|><|det|>[[117, 193, 888, 243]]<|/det|>
\[ \sum_{k=2}^{4} \frac{1}{k} = \frac{1}{2} + \frac{1}{3} + \frac{1}{4} = \frac{6}{12} + \frac{4}{12} + \frac{3}{12} = \frac{6+4+3}{12} = \frac{13}{12}. \quad (5) \]

<|ref|>text<|/ref|><|det|>[[90, 263, 238, 281]]<|/det|>
e) Wir erhalten 

<|ref|>equation<|/ref|><|det|>[[117, 290, 888, 340]]<|/det|>
\[ \sum_{k=0}^{4} 2^k = 2^0 + 2^1 + 2^2 + 2^3 + 2^4 = 1 + 2 + 4 + 8 + 16 = \frac{31}{16}. \quad (6) \]

<|ref|>text<|/ref|><|det|>[[90, 360, 238, 377]]<|/det|>
f) Wir erhalten 

<|ref|>equation<|/ref|><|det|>[[117, 387, 888, 501]]<|/det|>
\[ \begin{align*} \sum_{k=4}^{9} (-1)^k k &= (-1)^4 \cdot 4 + (-1)^5 \cdot 5 + (-1)^6 \cdot 6 + (-1)^7 \cdot 7 + (-1)^8 \cdot 8 + (-1)^9 \cdot 9 \\ &= 1 \cdot 4 + (-1) \cdot 5 + 1 \cdot 6 + (-1) \cdot 7 + 1 \cdot 8 + (-1) \cdot 9 \\ &= 4 - 5 + 6 - 7 + 8 - 9 = -\underline{3}. \end{align*} \quad (7) \]

<|ref|>sub_title<|/ref|><|det|>[[75, 530, 470, 548]]<|/det|>
## 3. Summen berechnen mit Python/Sympy 

<|ref|>text<|/ref|><|det|>[[75, 548, 888, 583]]<|/det|>
Wir berechnen die *Summen* aus Aufgabe 2 mit Python/Sympy. Dazu implementieren wir den folgendne Code, den wir für jede Teilaufgabe modifizieren: 

<|ref|>text<|/ref|><|det|>[[75, 590, 468, 750]]<|/det|>
```python
# Python initialisieren:
import IPython.display as dp;
import sympy as sp;
# Python konfigurieren:
sp.init_printing();
k,S=sp.symbols('k,S');
# Berechnungen:
S=sp.summation(...,(...,...,...));
# Ausgabe:
dp.display(S);
```

<|ref|>text<|/ref|><|det|>[[90, 761, 360, 779]]<|/det|>
a) Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[117, 787, 420, 838]]<|/det|>
# Berechnungen:
S=sp.summation(k,(k,4,10));
Gemäss Ausgabe ist S=49. 

<|ref|>text<|/ref|><|det|>[[90, 856, 360, 874]]<|/det|>
b) Wir modifizieren den Code. 

<|ref|>text<|/ref|><|det|>[[117, 883, 454, 914]]<|/det|>
# Berechnungen:
S=sp.summation(2*k,(k,4,10));