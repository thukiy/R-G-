# 7. Grenzwerte berechnen mit Python/Sympy 

Wir berechnen die Grenzwerte aus Aufgabe 6 mit Python/Sympy. Dazu implementieren wir den folgenden Code, den wir für jede Teilaufgabe modifizieren.

```
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
```

a) Wir modifizieren den Code.
\# Parameter:
$\mathrm{a} \_\mathrm{n}=3 /(\mathrm{n}+2)$
Gemäss Ausgabe konvergiert die Folge gegen den Grenzwert $\underline{a}=\underline{0}$.
b) Wir modifizieren den Code.
\# Parameter:
$\mathrm{a} \_\mathrm{n}=(\mathrm{n}+2) / 3$
Gemäss Ausgabe divergiert die Folge.
c) Wir modifizieren den Code.
\# Parameter:
$\mathrm{a} \_\mathrm{n}=(\mathrm{n}+2) /(3 * \mathrm{n})$;
Gemäss Ausgabe konvergiert die Folge gegen den Grenzwert $\underline{a}=\underline{\underline{1}}$.
d) Wir modifizieren den Code.
\# Parameter:
$\mathrm{a} \_\mathrm{n}=3 * \mathrm{n} /(\mathrm{n}+2)$
Gemäss Ausgabe konvergiert die Folge gegen den Grenzwert $\underline{a}=\underline{3}$.
e) Wir modifizieren den Code.
\# Parameter:
$\mathrm{a} \_\mathrm{n}=3 * \mathrm{n} /(6 * \mathrm{n}+2)$
Gemäss Ausgabe konvergiert die Folge gegen den Grenzwert $\underline{a}=\underline{\underline{1}}$.
f) Wir modifizieren den Code.
\# Parameter:
$\mathrm{a} \_\mathrm{n}=(4-\mathrm{n} * * 2) /(2+\mathrm{n}) * * 2$;