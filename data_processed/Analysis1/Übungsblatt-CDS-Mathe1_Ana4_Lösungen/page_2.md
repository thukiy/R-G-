c) Wir erhalten

$$
\underline{\sum_{k=-2}^{2} k^{3}}=(-2)^{3}+(-1)^{3}+0^{3}+1^{3}+2^{3}=-8-1+0+1+8=\underline{0}
$$

d) Wir erhalten

$$
\underline{\sum_{k=2}^{4} \frac{1}{k}}=\frac{1}{2}+\frac{1}{3}+\frac{1}{4}=\frac{6}{12}+\frac{4}{12}+\frac{3}{12}=\frac{6+4+3}{12}=\frac{13}{\underline{12}}
$$

e) Wir erhalten

$$
\sum_{\substack{k=0}}^{4} 2^{k}=2^{0}+2^{1}+2^{2}+2^{3}+2^{4}=1+2+4+8+16=\underline{31}
$$

f) Wir erhalten

$$
\begin{aligned}
\sum_{k=4}^{9}(-1)^{k} k & =(-1)^{4} \cdot 4+(-1)^{5} \cdot 5+(-1)^{6} \cdot 6+(-1)^{7} \cdot 7+(-1)^{8} \cdot 8+(-1)^{9} \cdot 9 \\
& =1 \cdot 4+(-1) \cdot 5+1 \cdot 6+(-1) \cdot 7+1 \cdot 8+(-1) \cdot 9 \\
& =4-5+6-7+8-9=\underline{-3}
\end{aligned}
$$

# 3. Summen berechnen mit Python/Sympy 

Wir berechnen die Summen aus Aufgabe 2 mit Python/Sympy. Dazu implementieren wir den folgendne Code, den wir für jede Teilaufgabe modifizieren:

```
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

a) Wir modifizieren den Code.

```
# Berechnungen:
S=sp.summation(k,(k,4,10));
```

Gemäss Ausgabe ist $\underline{S=49}$.
b) Wir modifizieren den Code.

```
# Berechnungen:
S=sp.summation(2*k,(k,4,10));
```