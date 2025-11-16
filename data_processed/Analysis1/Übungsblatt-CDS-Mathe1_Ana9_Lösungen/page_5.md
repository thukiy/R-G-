# 7. Diverse Ableitungen berechnen mit Python/Sympy 

Wir berechnen die Ableitungen aus Aufgabe 6 mit Python/Sympy. Dazu implementieren wir den folgenden Code, den wir für jede Teilaufgabe modifizieren.

```
# Python initialisieren:
import IPython.display as dp;
import sympy as sp;
# Python konfigurieren:
sp.init_printing();
x=sp.symbols('x');
# Parameter:
f=...;
# Berechnungen:
fs=sp.simplify(sp.diff(f,x));
# Ausgabe:
dp.display(f);
dp.display(fs);
```

a) Wir modifizieren den Code.

```
# Parameter:
f=sp.exp(-x);
```

Gemäss Ausgabe erhalten wir die Ableitung

$$
f^{\prime}(x)=-\mathrm{e}^{-x}
$$

b) Wir modifizieren den Code.

```
# Parameter:
f=x*sp.exp(x);
```

Gemäss Ausgabe erhalten wir die Ableitung

$$
\underline{f^{\prime}(x)}=(x+1) \cdot \mathrm{e}^{x}
$$

c) Wir modifizieren den Code.

```
# Parameter:
f=(x+2)*sp.exp(x);
```

Gemäss Ausgabe erhalten wir die Ableitung

$$
\underline{f^{\prime}(x)}=(x+3) \cdot \mathrm{e}^{x}
$$

d) Wir modifizieren den Code.

```
# Parameter:
f=sp.exp(-x**2);
```

Gemäss Ausgabe erhalten wir die Ableitung

$$
\underline{\dot{f}(t)}=-2 \cdot x \cdot \mathrm{e}^{-x^{2}}
$$

e) Wir modifizieren den Code.