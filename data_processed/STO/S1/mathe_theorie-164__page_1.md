<|ref|>text<|/ref|><|det|>[[12, 28, 951, 60]]<|/det|>
Bsp: 3maliger Münzwurf: 2 mal dabei und im 3. wurf wappen 

<|ref|>text<|/ref|><|det|>[[129, 66, 520, 99]]<|/det|>
Ereignis A: 1. wurf dabei 

<|ref|>text<|/ref|><|det|>[[248, 105, 515, 137]]<|/det|>
B: 2. wurf dabei 

<|ref|>text<|/ref|><|det|>[[248, 145, 559, 177]]<|/det|>
C: 3. wurf wappen 

<|ref|>text<|/ref|><|det|>[[128, 186, 546, 217]]<|/det|>
→ Ereignisse sind unabhängig 

<|ref|>equation<|/ref|><|det|>[[176, 224, 644, 295]]<|/det|>
\[
\begin{align*}
P(A \cap B \cap C) &= P(A) \cdot P(B) \cdot P(C) \\
&= \frac{1}{2} \cdot \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{8}
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[19, 319, 562, 352]]<|/det|>
Ereignisbauen / Baumdiagramm 

<|ref|>text<|/ref|><|det|>[[45, 360, 690, 391]]<|/det|>
nötlich bei mehrstufigen Aufbereitungsverfahren 

<|ref|>image<|/ref|><|det|>[[160, 390, 444, 572]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[45, 594, 852, 625]]<|/det|>
Wahrscheinlichkeiten werden entlang eines Pfades multipliziert 

<|ref|>sub_title<|/ref|><|det|>[[12, 671, 393, 703]]<|/det|>
Totale Wahrscheinlichkeit 

<|ref|>text<|/ref|><|det|>[[41, 714, 950, 745]]<|/det|>
Gegeben: Ereignisse \(A_1, \ldots, A_n\), \(n \in \mathbb{N}\), die paarweise disjunkt sind. 

<|ref|>text<|/ref|><|det|>[[41, 752, 595, 784]]<|/det|>
Ausserdem gibt: \(A_1 \cup A_2 \cup \ldots A_n = \Omega\) 

<|ref|>text<|/ref|><|det|>[[41, 792, 900, 825]]<|/det|>
Die totale Wahrscheinlichkeit für ein beliebiges Ereignis \(B\) ist 

<|ref|>equation<|/ref|><|det|>[[88, 830, 404, 870]]<|/det|>
\[
P(B) = \sum_i P(A_i) \cdot P(B|A_i)
\]