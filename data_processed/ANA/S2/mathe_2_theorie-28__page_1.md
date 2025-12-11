<|ref|>sub_title<|/ref|><|det|>[[20, 13, 440, 40]]<|/det|>
## Berechnung eines zweifachintegrales : 

<|ref|>text<|/ref|><|det|>[[50, 53, 820, 80]]<|/det|>
Rückführung auf 2 Einzelintegrale, die nacheinander ausgeführt werden 

<|ref|>image<|/ref|><|det|>[[120, 90, 930, 300]]<|/det|>
 

<|ref|>equation<|/ref|><|det|>[[50, 280, 520, 375]]<|/det|>
\[ V = \int_{G} \int_{a}^{b} f(x, y) \, dA = \int_{x=a}^{b} \left( \int_{y=f(x)}^{f(x)} f(x, y) \, dy \right) \, dx \]

<|ref|>text<|/ref|><|det|>[[50, 404, 855, 430]]<|/det|>
→ hier : inneres Integral y als Variable, x wird als Konstante betrachtet 

<|ref|>text<|/ref|><|det|>[[50, 444, 465, 468]]<|/det|>
→ Integration von innen nach aussen 

<|ref|>text<|/ref|><|det|>[[50, 483, 770, 508]]<|/det|>
→ Reihenfolge ist festgelegt, kein betriebiges Verlassen möglich! 

<|ref|>sub_title<|/ref|><|det|>[[20, 540, 680, 566]]<|/det|>
## Satz von Fubini (Fächenintegrale über Rechteckgebiet) : 

<|ref|>text<|/ref|><|det|>[[50, 579, 960, 641]]<|/det|>
wenn \(G = [a, b] \times [c, d]\) im Rechteck und \(f : G \to \mathbb{R}\) eine integrierbare Funktion ist, dann gilt : 

<|ref|>equation<|/ref|><|det|>[[80, 643, 671, 696]]<|/det|>
\[ \int_{G} f \, dA = \int_{a}^{b} \int_{c}^{d} f(x, y) \, dy \, dx = \int_{c}^{d} \int_{a}^{b} f(x, y) \, dx \, dy \]

<|ref|>text<|/ref|><|det|>[[20, 714, 561, 740]]<|/det|>
Bsp : \(G = [0; 1] \times [1; 2]\), \(f(x, y) = x^y\) 

<|ref|>equation<|/ref|><|det|>[[128, 744, 777, 821]]<|/det|>
\[ \begin{aligned} V &= \int_{1}^{2} \int_{0}^{1} x^y \, dx \, dy = \int_{1}^{2} \left[ \frac{1}{y+1} \cdot x^{y+1} \right]_{0}^{1} \, dy = \int_{1}^{2} \frac{1}{y+1} \, dy \\ &= [\ln(y+1)]_{1}^{2} = \ln 3 - \ln 2 \end{aligned} \]

<|ref|>sub_title<|/ref|><|det|>[[20, 850, 160, 876]]<|/det|>
## Sonderfall : 

<|ref|>equation<|/ref|><|det|>[[50, 888, 680, 955]]<|/det|>
\[ \begin{aligned} f(x, y) &= q(x) \cdot h(y) & a \le x \le b, & c \le y \le d \\ a \int_{c}^{d} q(x) \cdot h(y) \, dy \, dx &= a \int_{c}^{d} q(x) \, dx \cdot h(y) \, dy \end{aligned} \]