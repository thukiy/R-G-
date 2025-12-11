<|ref|>text<|/ref|><|det|>[[114, 82, 142, 100]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[114, 99, 816, 214]]<|/det|>
\[
P(X = 4) = \frac{\binom{4}{4} \cdot \binom{32 - 4}{10 - 4}}{ \binom{32}{10} } = \frac{1 \cdot \binom{28}{6}}{ \binom{32}{10} } = \frac{\frac{28!}{6!(28-6)!}}{\frac{32!}{10!(32-10)!}} = \frac{\frac{28!}{6!} \cdot \frac{28!}{32!}}{\frac{32!}{10!}} = \frac{\frac{28!}{6!} \cdot \frac{28}{32!} \cdot \frac{10!}{32!}}{\frac{32!}{10!}} = \frac{\frac{1}{6!} \cdot \frac{28!}{32!} \cdot \frac{10!}{32!}}{\frac{32! \cdot 10!}{10!}} = \frac{\frac{28!}{6!} \cdot 28! \cdot 10!}{32! \cdot 10!} = \frac{\frac{28!}{6!} \cdot 28! \cdot \frac{10!}{32!}}{\frac{32! \cdot 10}{10!}} = \frac{\frac{28!}{6!} \cdot 8 \cdot 9 \cdot 10}{\frac{28!}{6!} \cdot 29 \cdot 30 \cdot 31 \cdot 32} = \frac{7 \cdot 8 \cdot 9 \cdot 10}{29 \cdot 30 \cdot 31 \cdot 32} = 0,0058
\]

<|ref|>text<|/ref|><|det|>[[114, 225, 644, 240]]<|/det|>
Umformungen: 10! = (6!) · 7 · 8 · 9 · 10; 32! = (28!) · 29 · 30 · 31 · 32 

<|ref|>text<|/ref|><|det|>[[114, 245, 852, 273]]<|/det|>
Fazit: Die Chance, dass ein Spieler alle 4 „Asse“ erhält, ist also sehr gering (die Wahrscheinlichkeit beträgt rund 0,6%). 

<|ref|>text<|/ref|><|det|>[[114, 273, 142, 291]]<|/det|>
b) 

<|ref|>equation<|/ref|><|det|>[[114, 290, 735, 411]]<|/det|>
\[
P(X = 0) = \frac{\binom{4}{0} \cdot \binom{32 - 4}{10 - 0}}{ \binom{32}{10} } = \frac{1 \cdot \binom{2}{8}}{ \binom{10}{10} } = \frac{\frac{28!}{10!} \cdot \frac{28!}{32!}}{\frac{32!}{10!(32-10)!}} = \frac{\frac{1}{10!} \cdot \frac{28!}{32!}}{\frac{32! \cdot 10}{10!}} = \left( \frac{28!}{10!} \right) \cdot \left( \frac{28!}{32!} \right) = \frac{28!}{32!} \cdot \frac{28!}{32!} = \frac{28!}{32!} \cdot \frac{28!}{32} = \frac{28!}{32!} \cdot \frac{28!}{31!} = \frac{28!}{32!} \cdot \frac{28! \cdot 22!}{32!} = \frac{28!}{32!} \cdot \frac{\frac{28!}{32!} \cdot 22!}{32!} = \frac{28!}{32!} 0,2034
\]

<|ref|>text<|/ref|><|det|>[[114, 420, 680, 437]]<|/det|>
Umformungen: 22! = (18!) · 19 · 20 · 21 · 22; 32! = (28!) · 29 · 30 · 31 · 3 

<|ref|>text<|/ref|><|det|>[[114, 440, 675, 456]]<|/det|>
Fazit: Die Wahrscheinlichkeit, dass ein Spieler kein „Ass“ erhält, beträgt rund 20,3%. 

<|ref|>sub_title<|/ref|><|det|>[[114, 473, 257, 490]]<|/det|>
10. α-Teilchen 

<|ref|>text<|/ref|><|det|>[[114, 490, 864, 542]]<|/det|>
Bei der Emission von α-Teilchen einer bestimmten radioaktiven Substanz werden in einer Stunde genau 1620 α-Teilchen registriert. Welche Wahrscheinlichkeit besteht, dass in einem 10-Sekunden-Intervall 

<|ref|>text<|/ref|><|det|>[[114, 541, 227, 559]]<|/det|>
a) genau 2 

<|ref|>text<|/ref|><|det|>[[114, 558, 504, 575]]<|/det|>
b) Mehr als 2 α-Teilchen emittiert werden? 

<|ref|>text<|/ref|><|det|>[[114, 590, 686, 604]]<|/det|>
Zufallsvariable: X = Anzahl der in einem 10-Sekunden-Intervall emittierten α-Teilchen 

<|ref|>text<|/ref|><|det|>[[114, 610, 875, 637]]<|/det|>
X genügt einer Poisson-Verteilung mit dem noch unbekannten Parameter (Mittelwert) μ, den wir wie folgt bestimmen (1 h = 3600 s; h: Stunden; s: Sekunden): 

<|ref|>equation<|/ref|><|det|>[[114, 641, 543, 670]]<|/det|>
\[
Mittlere Anzahl emittierter α-Teilchen pro Sekunde: \frac{1620}{3600} = 0,45
\]

<|ref|>text<|/ref|><|det|>[[114, 675, 875, 704]]<|/det|>
Im 10-Sekunden-Intervall werden somit im Mittel μ = 10 · 0,45 = 4,5 α-Teilchen emittiert. Die Wahrscheinlichkeitsfunktion der diskreten Zufallsvariable X lautet damit wie folgt: 

<|ref|>equation<|/ref|><|det|>[[159, 710, 625, 739]]<|/det|>
\[
f(x) = P(X = x) = \frac{\mu^x}{x!} \cdot e^{-\mu} = \frac{4,5^x}{x!} \cdot e^{-4,5} \quad (x = 0, 1, 2, \dots)
\]

<|ref|>text<|/ref|><|det|>[[114, 741, 142, 758]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[114, 757, 472, 787]]<|/det|>
\[
P(X = 2) = \frac{4,5^2}{2!} \cdot e^{-4,5} = 0,1125 \cong 11,25\%
\]

<|ref|>text<|/ref|><|det|>[[114, 790, 142, 807]]<|/det|>
b) 

<|ref|>equation<|/ref|><|det|>[[114, 806, 688, 825]]<|/det|>
\[
P(X > 2) = 1 - P(X \le 2) = 1 - P(X = 0) - P(X = 1) - P(X = 2) =
\]

<|ref|>equation<|/ref|><|det|>[[196, 830, 872, 867]]<|/det|>
\[
= 1 - \frac{4,5^0}{0!} \cdot e^{-4,5} - \frac{4,5^1}{1!} \cdot e^{-4,5} - \frac{4,5^2}{2!} \cdot e^{-4,5}
\]

<|ref|>equation<|/ref|><|det|>[[196, 872, 775, 890]]<|/det|>
\[
= 1 - (1 + 4,5 + 10,125) \cdot e^{-4,5} = 1 - 15,625 \cdot e^{-4,5} = 0,8264 \cong 82,64\%
\]