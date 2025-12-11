<|ref|>text<|/ref|><|det|>[[18, 12, 978, 120]]<|/det|>
Bsp: bestimme Konkret kifft mit Prävalenz 20 pro 100 000 Personen auf, d.h. die Wahrscheinlichkeit, dass jemand diese Konkret hat, beträgt \(P(K) = \frac{2}{10000} = 0,0002 \triangleq 0,02\%\) 

<|ref|>text<|/ref|><|det|>[[125, 127, 978, 280]]<|/det|>
Prävalenz: Normal aufnahme, wie viele Personen infiziert sind.
Es gibt einen Test, um zu bestimmen, ob Person unkrank ist.
Test zeigt mit 95% an, ob Person krank ist: \(P(T|K) = 0,95\)
Test kann jedoch auch falsch positiv anzeigen, mit 1%: 

<|ref|>equation<|/ref|><|det|>[[131, 284, 333, 312]]<|/det|>
\[P(T|K) = 0,01\]

<|ref|>text<|/ref|><|det|>[[131, 323, 943, 394]]<|/det|>
Wie gross ist Wahrscheinlichkeit, dann eine getestete Person Träger des Konkret ist? 

<|ref|>equation<|/ref|><|det|>[[131, 410, 702, 485]]<|/det|>
\[P(K|T) = \frac{P(K) \cdot P(T|K)}{P(T)} \quad (\text{Satz von Bayes})\]

<|ref|>equation<|/ref|><|det|>[[131, 499, 602, 525]]<|/det|>
\[P(T) = P(K) \cdot P(T|K) + P(K) \cdot P(T|K)\]

<|ref|>equation<|/ref|><|det|>[[131, 543, 833, 588]]<|/det|>
\[P(K|T) = \frac{0,0002 \cdot 0,95}{0,0002 \cdot 0,95 + 0,9998 \cdot 0,01} = 0,0186 \triangleq 1,86\%\]