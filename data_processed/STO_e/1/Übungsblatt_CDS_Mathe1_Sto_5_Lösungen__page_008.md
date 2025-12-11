<|ref|>text<|/ref|><|det|>[[119, 85, 533, 103]]<|/det|>
Wahrscheinlichkeit für einwandfreien Flansch F2: 

<|ref|>equation<|/ref|><|det|>[[162, 115, 500, 137]]<|/det|>
\[P(A_2) = 1 - P(\overline{A_2}) = 1 - 0,015 = 0,985\]

<|ref|>text<|/ref|><|det|>[[119, 149, 558, 168]]<|/det|>
Wahrscheinlichkeit für einwandfreien Dichtungsring: 

<|ref|>equation<|/ref|><|det|>[[162, 180, 477, 201]]<|/det|>
\[P(A_3) = 1 - P(\overline{A_3}) = 1 - 0,02 = 0,98\]

<|ref|>text<|/ref|><|det|>[[119, 213, 725, 231]]<|/det|>
Wahrscheinlichkeit einer einwandfreien Flanschverbindung beträgt somit: 

<|ref|>equation<|/ref|><|det|>[[162, 244, 546, 263]]<|/det|>
\[P(A) = 0,99 \cdot 0,985 \cdot 0,98 = 0,95565 \approx 95,6\%\]

<|ref|>text<|/ref|><|det|>[[119, 276, 822, 312]]<|/det|>
Wir können also insgesamt \(N = 0,95565 \cdot 500 = 477\) einwandfreie Flanschverbindungen erwarten. 

<|ref|>sub_title<|/ref|><|det|>[[114, 330, 293, 347]]<|/det|>
## 9. Kondensatoren 

<|ref|>text<|/ref|><|det|>[[114, 346, 827, 381]]<|/det|>
Eine Warenlieferung besteht aus 250 Kondensatoren, die auf 3 Maschinen vom gleichen Typ hergestellt wurden. Dabei gilt: 

<|ref|>table<|/ref|><|det|>[[114, 378, 618, 434]]<|/det|>
<table><tr><td>Maschine</td><td>A</td><td>B</td><td>C</td></tr><tr><td>Produzierte Stückzahl</td><td>80</td><td>50</td><td>120</td></tr><tr><td>Davon Ausschuss</td><td>2</td><td>1</td><td>3</td></tr></table>

<|ref|>text<|/ref|><|det|>[[114, 448, 496, 466]]<|/det|>
Wie gross ist die Wahrscheinlichkeit, dass 

<|ref|>text<|/ref|><|det|>[[114, 465, 642, 483]]<|/det|>
a) ein der Lieferung entnommener Kondensator defekt ist, 

<|ref|>text<|/ref|><|det|>[[114, 481, 850, 515]]<|/det|>
b) ein zufällig entnommener defekter Kondensator auf der Maschine C hergestellt wurde? 

<|ref|>text<|/ref|><|det|>[[114, 513, 567, 533]]<|/det|>
Die Verwendung eines Ereignisbaums ist hilfreich. 

<|ref|>text<|/ref|><|det|>[[122, 548, 822, 566]]<|/det|>
Anteile der 3 Maschinen \(A\), \(B\) und \(C\) an der Gesamtproduktion (250 Kondensatoren): 

<|ref|>equation<|/ref|><|det|>[[122, 569, 520, 588]]<|/det|>
\[A: 80 \text{ von } 250 \quad \Rightarrow \quad P(A) = 80/250 = 0,32\]

<|ref|>equation<|/ref|><|det|>[[122, 590, 515, 609]]<|/det|>
\[B: 50 \text{ von } 250 \quad \Rightarrow \quad P(B) = 50/250 = 0,2\]

<|ref|>equation<|/ref|><|det|>[[122, 611, 533, 630]]<|/det|>
\[C: 120 \text{ von } 250 \quad \Rightarrow \quad P(C) = 120/250 = 0,48\]

<|ref|>text<|/ref|><|det|>[[122, 632, 860, 651]]<|/det|>
Wahrscheinlichkeiten für die Produktion eines defekten Kondensators (d) auf den Maschinen: 

<|ref|>equation<|/ref|><|det|>[[122, 653, 820, 673]]<|/det|>
\[P_A(d) = 2/80 = 0,025; \quad P_B(d) = 1/50 = 0,02; \quad P_C(d) = 3/120 = 0,025\]

<|ref|>text<|/ref|><|det|>[[122, 675, 595, 694]]<|/det|>
Aus dem unvollständigen Ereignisbaum in Bild A-24 folgt: 

<|ref|>equation<|/ref|><|det|>[[122, 702, 568, 742]]<|/det|>
\[a) P = 0,32 \cdot 0,025 + 0,2 \cdot 0,02 + 0,48 \cdot 0,025 = 0,024\]

<|ref|>equation<|/ref|><|det|>[[122, 755, 364, 791]]<|/det|>
\[b) P = \frac{0,48 \cdot 0,025}{0,024} = 0,5\]