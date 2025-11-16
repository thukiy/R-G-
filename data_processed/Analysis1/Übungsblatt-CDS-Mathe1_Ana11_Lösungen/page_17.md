# 9. Integrale von Polynom-Funktionen mit Python/Sympy 

Wir berechnen die Integrale aus Aufgabe 9 mit Python/Sympy. Dazu implementieren wir den folgenden Code, den wir für jede Teilaufgabe modifizieren.

```
# Python initialisieren:
import IPython.display as dp;
import sympy as sp;
# Python konfigurieren:
sp.init_printing();
x=sp.symbols('x');
# Parameter:
f=...; x_0=...; x_E=...;
# Berechnungen:
I=sp.integrate(f,(x,x_0,x_E));
# Ausgabe:
dp.display(I);
```

a) Wir modifizieren den Code.

```
# Parameter:
f=2*x-1; x_0=0; x_E=3;
```

Gemäss Ausgabe erhalten wir das Integral

$$
\underline{I=6}
$$

b) Wir modifizieren den Code.

```
# Parameter:
f=2*x-1; x_0=-1; x_E=1;
```

Gemäss Ausgabe erhalten wir das Integral

$$
\underline{I=-2}
$$

c) Wir modifizieren den Code.

```
# Parameter:
f=6*x**2-8*x**3+1; x_0=-2; x_E=1;
```

Gemäss Ausgabe erhalten wir das Integral

$$
\underline{I=51}
$$

d) Wir modifizieren den Code.

```
# Parameter:
f=6*x**2-8*x**3+1; x_0=-2; x_E=-1;
```

Gemäss Ausgabe erhalten wir das Integral

$$
\underline{I=45}
$$

e) Wir modifizieren den Code.

```
# Parameter:
f=2/3-16*x**4; x_0=1; x_E=3/2;
```