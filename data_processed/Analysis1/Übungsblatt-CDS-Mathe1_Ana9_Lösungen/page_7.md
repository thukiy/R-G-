d) Wir betrachten die Funktion

$$
f(x)=\frac{1}{1+\mathrm{e}^{-x}}
$$

Mit Hilfe der Reziproken-Regel erhalten wir

$$
\begin{aligned}
& \xrightarrow{f^{\prime}(x)}=-\frac{\left(1+\mathrm{e}^{-x}\right)^{\prime}}{\left(1+\mathrm{e}^{-x}\right)^{2}}=-\frac{0-\mathrm{e}^{-x}}{\left(1+\mathrm{e}^{-x}\right)^{2}}=\frac{\mathrm{e}^{-x}}{\left(1+\mathrm{e}^{-x}\right)^{2}}=\frac{\mathrm{e}^{2 x} \cdot \mathrm{e}^{-x}}{\mathrm{e}^{2 x} \cdot\left(1+\mathrm{e}^{-x}\right)^{2}} \\
& =\frac{\mathrm{e}^{2 x-x}}{\left(\mathrm{e}^{x}\right)^{2} \cdot\left(1+\mathrm{e}^{-x}\right)^{2}}=\frac{\mathrm{e}^{x}}{\left(\mathrm{e}^{x} \cdot\left(1+\mathrm{e}^{-x}\right)\right)^{2}}=\frac{\mathrm{e}^{x}}{\left(\mathrm{e}^{x}+1\right)^{2}} .
\end{aligned}
$$

e) Wir betrachten die Funktion

$$
f(x)=\ln ^{\ln (x)}(x)=(\ln (x))^{\ln (x)}
$$

Mit Hilfe der Exponential-Regel erhalten wir

$$
\begin{aligned}
& \xrightarrow{f^{\prime}(x)}=\left(\ln ^{\prime}(x) \cdot \ln (\ln (x))+\ln ^{\prime}(x) \cdot \frac{\ln (x)}{\ln (x)}\right) \cdot \ln ^{\ln (x)}(x) \\
& =\left(\frac{1}{x} \cdot \ln (\ln (x))+\frac{1}{x} \cdot 1\right) \cdot \ln ^{\ln (x)}(x)=\frac{1}{x} \cdot(\ln (\ln (x))+1) \cdot \ln ^{\ln (x)}(x) .
\end{aligned}
$$

f) Wir betrachten die Funktion

$$
f(x)=\frac{2^{-\sqrt{|x|}}}{\ln (2)}
$$

Mit Hilfe der Ketten-Regel erhalten wir

$$
\begin{aligned}
& \xrightarrow{f^{\prime}(x)}=\frac{1}{\ln (2)} \cdot(-\sqrt{|x|})^{\prime} \cdot \ln (2) \cdot 2^{-\sqrt{|x|}}=-\frac{1}{2 \cdot \sqrt{|x|}} \cdot|x|^{\prime} \cdot 2^{-\sqrt{|x|}}=-\frac{\operatorname{sgn}(x)}{2 \cdot \sqrt{|x|}} \cdot 2^{-\sqrt{|x|}} \\
& =\underbrace{-\frac{\operatorname{sgn}(x)}{\sqrt{|x|}} \cdot 2^{-\sqrt{|x|}-1}}
\end{aligned}
$$

# 9. Diverse Ableitungen berechnen mit Python/Sympy 

Wir berechnen die Ableitungen aus Aufgabe 8 mit Python/Sympy. Dazu implementieren wir den folgenden Code, den wir für jede Teilaufgabe modifizieren.

```
# Python initialisieren:
import IPython.display as dp;
import sympy as sp;
# Python konfigurieren:
sp.init_printing();
x=sp.symbols('x',real=True);
# Parameter:
f=...;
# Berechnungen:
fs=sp.simplify(sp.diff(f,x));
# Ausgabe:
dp.display(f);
dp.display(fs);
```