# 6. Aufleitungen von Polynom-Funktionen 

Wir berechnen die folgenden unbestimmten Integrale durch elementares Aufleiten.
a) Wir erhalten

$$
\underline{F(x)}=\int(2 x+1) \mathrm{d} x=2 \cdot \frac{1}{2} x^{2}+1 \cdot x+c=\underline{x^{2}+x+c}
$$

b) Wir erhalten

$$
\underline{F(x)}=\int(4 x-8) \mathrm{d} x=4 \cdot \frac{1}{2} x^{2}-8 x+c=\underline{2 x^{2}-8 x+c}
$$

c) Wir erhalten

$$
\underline{F(x)}=\int\left(12 x^{2}+17\right) \mathrm{d} x=12 \cdot \frac{1}{3} x^{3}+17 x+c=\underline{4 x^{3}+17 x+c}
$$

d) Wir erhalten

$$
\underline{F(x)}=\int\left(3 x^{2}-6 x\right) \mathrm{d} x=3 \cdot \frac{1}{3} x^{3}-6 \cdot \frac{1}{2} x^{2}+c=\underline{x^{3}-3 x^{2}+c}
$$

e) Wir erhalten

$$
\underline{F(x)}=\int\left(6 x^{2}-4 x+3\right) \mathrm{d} x=6 \cdot \frac{1}{3} x^{3}-4 \cdot \frac{1}{2} x^{2}+3 x+c=\underline{2 x^{3}-2 x^{2}+3 x+c}
$$

f) Wir erhalten

$$
\underline{F(x)}=\int\left(8 x-1+9 x^{2}\right) \mathrm{d} x=8 \cdot \frac{1}{2} x^{2}-1 \cdot x+9 \cdot \frac{1}{3} \cdot x^{3}+c=\underline{4 x^{2}-x+3 x^{3}+c}
$$

## 7. Aufleitungen von Polynom-Funktionen mit Python/Sympy

Wir berechnen die unbestimmten Integrale aus Aufgabe 7 mit Python/Sympy. Dazu implementieren wir den folgenden Code, den wir für jede Teilaufgabe modifizieren.

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
F=sp.expand(sp.integrate(f,x));
# Ausgabe:
dp.display(f);
dp.display(F);
```

a) Wir modifizieren den Code.