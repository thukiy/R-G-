<|ref|>equation<|/ref|><|det|>[[119, 81, 857, 207]]<|/det|>
\[
\begin{align*}
\frac{y(x)}{x} &= \left( y_0 + C(x) \cdot e^{M(x_0)} \right) \cdot e^{M(x) - M(x_0)} = \left( -\frac{7}{9} + \left( \frac{16}{9} - \frac{3x + 16}{9} \cdot e^{-3x} \right) \cdot e^{3x_0} \right) \cdot e^{3x_0} \\
&= \left( -\frac{7}{9} + \frac{16}{9} - \frac{3x + 16}{9} - e^{-3x} \right) \cdot e^{3x} = \frac{9}{9} \cdot e^{3x} - \frac{3x + 16}{9} \cdot e^{-3x + 3x} \\
&= e^{3x} - \frac{x}{3} - \frac{16}{9}.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 221, 150, 238]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[115, 235, 875, 280]]<|/det|>
Analytisch isolierte Form der DGL: \(y' = \frac{1}{x}y + 2x^2 + x \text{ mit } m(x) = 1/x \text{ und } q(x) = 2x^2+x\).
Für die Stammfunktion von \(m(x)\) und die Konstante \(C(x)\) ergibt sich 

<|ref|>equation<|/ref|><|det|>[[115, 277, 740, 377]]<|/det|>
\[
\begin{align*}
M(x) &= \int m(x) dx = \int \frac{1}{x} dx = \ln|x| \\
C(x) &= \int_{x_0}^{x} q(s) \cdot e^{-M(s)} \, ds = \int_{2}^{x} (2s^2 + s) \cdot e^{-\ln(|s|)} \, ds = \int_{2}^{x} (2s^2 + s) - \frac{1}{s} \, ds \\
&= \int_{2}^{x} (2s + 1) \, ds = \left[ s^2 + s \right]_{2}^{x} = x^2 + x - 4 - 2 = x^2 + x - 6.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 379, 617, 399]]<|/det|>
Somit ergibt sich für die Lösung des AWP für \(x \ge x_0 = 2\): 

<|ref|>equation<|/ref|><|det|>[[123, 404, 783, 470]]<|/det|>
\[
\begin{align*}
y(x) &= \left( y_0 + C(x) \cdot e^{M(x_0)}\right) \cdot e^{M(x) - M(x_0)} = \left( 12 + \left( x^2 + x - 6 \right) \cdot e^{\ln(|2|)} \right) \cdot e^{\ln(|x|) - \ln(|2|)} \\
&= \left( 12 + \left( x^2 + x - 6 \right)\cdot 2 \right) \cdot \frac{x}{2} = 6x + x^3 + x^2 - 6x = \frac{x^3 + x^2}{2}.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 472, 145, 488]]<|/det|>
c) 

<|ref|>text<|/ref|><|det|>[[115, 486, 203, 503]]<|/det|>
AWP a): 

<|ref|>text<|/ref|><|det|>[[115, 502, 470, 717]]<|/det|>
# Python initialisieren
import IPython.display as dp;
import sympy as sp;
# Python konfigurieren
sp.init_printing();
x=sp.symbols('x');
y=sp.Function('y');
# Parameter
l=y(x).diff(x); r=3*y(x)+x+5;
# Berechnungen
L=sp.dsolve(l-r, y(x), ics={y(0):-7/9});
# Ausgabe
dp.display(L); 

<|ref|>text<|/ref|><|det|>[[115, 729, 555, 748]]<|/det|>
AWP b) analog nur mit veränderter DGL und AB.