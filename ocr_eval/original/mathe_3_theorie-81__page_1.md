<|ref|>sub_title<|/ref|><|det|>[[27, 19, 360, 63]]<|/det|>
# Kombinatorik 

<|ref|>text<|/ref|><|det|>[[60, 75, 792, 101]]<|/det|>
beschäftigt sich mit Anordnen und Auswählen von Elementen 

<|ref|>text<|/ref|><|det|>[[50, 112, 250, 137]]<|/det|>
→ Unenmodell 

<|ref|>sub_title<|/ref|><|det|>[[25, 171, 368, 196]]<|/det|>
## Anordnen : 
## Pemuklutionen 

<|ref|>text<|/ref|><|det|>[[40, 208, 520, 234]]<|/det|>
- es liegen n unlescheidbare Elemente 

<|ref|>equation<|/ref|><|det|>[[70, 247, 639, 273]]<|/det|>
\[P(n) = n! \quad \text{Anzahl Anordnungsmöglichkeiten}\]

<|ref|>text<|/ref|><|det|>[[40, 286, 930, 312]]<|/det|>
- n Elemente, wobei jeweilige Elemente mehrfach vorhanden sein können 

<|ref|>equation<|/ref|><|det|>[[70, 324, 870, 350]]<|/det|>
\[n = n_1 + n_2 + \dots + n_k, \quad \text{wobei die } n_k \text{ unlescheidbar sind } (k \le n)\]

<|ref|>equation<|/ref|><|det|>[[70, 355, 450, 390]]<|/det|>
\[P(n; n_1 \dots n_k) = \frac{n!}{n_1! \cdot n_2! \cdot \dots \cdot n_k!}\]

<|ref|>text<|/ref|><|det|>[[70, 402, 890, 464]]<|/det|>
→ die Anordnungen, die aufgrund des Nicht-Unlescheidbarkeit von
gleichen Elementen entstehen, werden nicht mitgezählt 

<|ref|>sub_title<|/ref|><|det|>[[30, 496, 395, 520]]<|/det|>
## Kombinationen (Auswählen) 

<|ref|>text<|/ref|><|det|>[[20, 534, 860, 596]]<|/det|>
→ wie viele Möglichkeiten gibt es, aus n Elementen genau k Elemente
auszuwählen ? 

<|ref|>text<|/ref|><|det|>[[20, 610, 928, 671]]<|/det|>
→ es wird unleschieden, ob Elemente nur einmal oder mehrmals gezogen
werden können 

<|ref|>text<|/ref|><|det|>[[70, 686, 728, 711]]<|/det|>
(ohne/ mit Wiederholung) bau. ohne/ mit Zurücklegen 

<|ref|>text<|/ref|><|det|>[[20, 724, 692, 750]]<|/det|>
→ Reihenfolge des Elemente wird nicht berücksichtigt 

<|ref|>text<|/ref|><|det|>[[55, 763, 808, 789]]<|/det|>
a) ohne Zurücklegen, n Elemente, k werden ausgewählt : 

<|ref|>equation<|/ref|><|det|>[[140, 794, 555, 828]]<|/det|>
\[C(n, k) = \binom{n}{k} = \frac{n!}{k!(n-k)!} \quad k \le n\]

<|ref|>text<|/ref|><|det|>[[55, 839, 535, 864]]<|/det|>
b) mit Zurücklegen : (k > n möglich) 

<|ref|>equation<|/ref|><|det|>[[140, 869, 600, 902]]<|/det|>
\[C_W(n, k) = \binom{n+k-1}{k} = \frac{(n+k-1)!}{k!(n+k-1-k)!} = \frac{(n+k-1)!}{k!(n-k)!}\]