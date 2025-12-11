<|ref|>text<|/ref|><|det|>[[115, 81, 671, 101]]<|/det|>
Formal mathematische Beschreibung der Verteilungsfunktion: 

<|ref|>equation<|/ref|><|det|>[[125, 98, 691, 288]]<|/det|>
\[
F_X(x) = P(X \le x) = \begin{cases} 0 & x < 1 \\ \frac{1}{6} & 1 \le x < 2 \\ \frac{1}{6} + \frac{5}{36} & 2 \le x < 3 \\ \frac{1}{6} + \frac{5}{36} + \frac{25}{216} & 3 \le x < 4 \\ 1 & x \ge 4 \end{cases}
\]

<|ref|>sub_title<|/ref|><|det|>[[115, 308, 274, 326]]<|/det|>
5. Sportschütze 

<|ref|>text<|/ref|><|det|>[[115, 324, 777, 343]]<|/det|>
Ein Bogenschütze trifft die Zielscheibe mit der Wahrscheinlichkeit \(p = 0,8\). 

<|ref|>text<|/ref|><|det|>[[115, 341, 880, 377]]<|/det|>
a) Bestimmen Sie die Wahrscheinlichkeitsverteilung der diskreten Zufallsvariablen \(X = \text{Anzahl der abgegebenen Schüsse bis zum } 1\). Treffer. 

<|ref|>text<|/ref|><|det|>[[115, 374, 880, 410]]<|/det|>
b) Wie gross ist die Wahrscheinlichkeit dafür, die Scheibe bei insgesamt 3 abgegebenen Schüssen zu treffen? 

<|ref|>text<|/ref|><|det|>[[125, 427, 864, 462]]<|/det|>
a) Der Schütze trifft *erstmals* beim \(x\)-ten Schuss (vorher \(x-1\) Fehlschüsse, jeweils mit der Wahrscheinlichkeit \(1-p=0,2\)). Der *Multiplikationssatz* liefert dann: 

<|ref|>equation<|/ref|><|det|>[[159, 472, 822, 517]]<|/det|>
\[
p(x) = f(x) = (0,2 \cdot 0,2 \cdot \ldots \cdot 0,2) \cdot 0,8 = 0,8 \cdot 0,2^{x-1} \quad (x = 1, 2, 3, \ldots)
\]

<|ref|>text<|/ref|><|det|>[[125, 528, 520, 546]]<|/det|>
b) Der Schütze trifft *spätestens* beim 3. Schuss: 

<|ref|>equation<|/ref|><|det|>[[159, 554, 657, 574]]<|/det|>
\[
P = f(1) + f(2) + f(3) = 0,8(1 + 0,2 + 0,2^2) = 0,992
\]