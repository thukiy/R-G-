<|ref|>text<|/ref|><|det|>[[114, 81, 135, 99]]<|/det|>
i) 

<|ref|>equation<|/ref|><|det|>[[120, 100, 780, 275]]<|/det|>
\[
\begin{align*}
I &= \int_{-\infty}^{\infty} \frac{1}{1+x^2} \, dx = \lim_{r \to \infty} \int_{-r}^{0} \frac{1}{1+x^2} \, dx + \lim_{s \to \infty} \int_{0}^{s} \frac{1}{1+x^2} \, dx \\
&= \lim_{r \to \infty} \left[ \arctan(x) \right]_{-r}^{0} + \lim_{s \to \infty} \left[ \arctan(x) \right]_{0}^{s} \\
&= \lim_{r \to \infty} \left( \arctan(0) - \arctan(-r) \right) + \lim_{s \to \infty} \left( \arctan(s) - \arctan(0) \right) \\
&= \lim_{r \to \infty} \left( 0 + \arctan(r) \right) + \lim_{s \to \infty} \left( \arct(0) - 0 \right) = 0 + \frac{\pi}{2} + \frac{\pi}{2} - 0 = \frac{\pi}{2}.
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[114, 288, 549, 307]]<|/det|>
3. Uneigentliche Integrale mit Python/Sympy 

<|ref|>text<|/ref|><|det|>[[114, 305, 812, 324]]<|/det|>
Berechnen Sie die uneigentlichen Integrale aus Aufgabe 2 mit Python/Sympy. 

<|ref|>text<|/ref|><|det|>[[114, 339, 145, 356]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[114, 355, 415, 371]]<|/det|>
# Python initialisieren: 

<|ref|>text<|/ref|><|det|>[[114, 370, 469, 388]]<|/det|>
import IPython.display as dp; 

<|ref|>text<|/ref|><|det|>[[114, 386, 347, 403]]<|/det|>
import sympy as sp; 

<|ref|>text<|/ref|><|det|>[[114, 403, 245, 419]]<|/det|>
# Symbole: 

<|ref|>text<|/ref|><|det|>[[114, 418, 333, 435]]<|/det|>
x=sp.symbols('x'); 

<|ref|>text<|/ref|><|det|>[[114, 434, 348, 451]]<|/det|>
sp.init_printing(); 

<|ref|>text<|/ref|><|det|>[[114, 450, 270, 467]]<|/det|>
# Parameter: 

<|ref|>text<|/ref|><|det|>[[114, 465, 277, 483]]<|/det|>
f=sp.E**(−x); 

<|ref|>text<|/ref|><|det|>[[114, 482, 300, 499]]<|/det|>
# Berechnungen: 

<|ref|>text<|/ref|><|det|>[[114, 498, 485, 515]]<|/det|>
F=sp.integrate(f, (x, 0, sp.oo)); 

<|ref|>text<|/ref|><|det|>[[114, 514, 245, 531]]<|/det|>
# Ausgabe: 

<|ref|>text<|/ref|><|det|>[[114, 530, 285, 547]]<|/det|>
dp.display(f); 

<|ref|>text<|/ref|><|det|>[[114, 546, 285, 563]]<|/det|>
dp.display(F); 

<|ref|>text<|/ref|><|det|>[[114, 579, 240, 599]]<|/det|>
b) – i) analog 

<|ref|>sub_title<|/ref|><|det|>[[114, 612, 395, 631]]<|/det|>
4. Aussagen über 2 Integrale 

<|ref|>text<|/ref|><|det|>[[114, 630, 444, 648]]<|/det|>
Gegeben seien die beiden Integrale 

<|ref|>equation<|/ref|><|det|>[[114, 646, 380, 675]]<|/det|>
\[
I = \int_{a}^{\infty} \frac{1}{x^2} \, dx \text{ und } J = \int_{a}^{\infty} \frac{1}{x} \, dx.
\]

<|ref|>text<|/ref|><|det|>[[114, 671, 680, 689]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[114, 686, 880, 812]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Die Integrale I und J sind uneigentliche Integrale.</td><td>X</td><td></td></tr><tr><td>b) Für a = 1 gilt I = 1.</td><td>X</td><td></td></tr><tr><td>c) Für a &gt; 0 ist I konvergent.</td><td></td><td>X</td></tr><tr><td>d) Für a ≤ 0 sind I und J beide divergent.</td><td>X</td><td></td></tr><tr><td>e) Für jedes a &gt; 0 gilt: I &gt; J.</td><td></td><td>X</td></tr><tr><td>f) Es gibt ein a &gt; 1, so dass gilt: I = 10.</td><td></td><td>X</td></tr></table>