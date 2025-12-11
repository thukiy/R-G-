<|ref|>title<|/ref|><|det|>[[115, 165, 465, 201]]<|/det|>
# Übungsblatt Sto 9 

<|ref|>text<|/ref|><|det|>[[575, 179, 880, 216]]<|/det|>
Computational and Data Science
BSc HS2023 

<|ref|>text<|/ref|><|det|>[[115, 233, 270, 261]]<|/det|>
## Lösungen 

<|ref|>text<|/ref|><|det|>[[752, 240, 880, 258]]<|/det|>
Mathematik 1 

<|ref|>text<|/ref|><|det|>[[115, 287, 210, 304]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 303, 880, 390]]<|/det|>
- Sie kennen die speziellen diskreten Wahrscheinlichkeitsverteilungen hypergeometrische und Poisson-Verteilung und ihre Eigenschaften.
- Sie können für konkrete Beispiele bestimmen, welche Wahrscheinlichkeitsverteilung vorliegt und können diese dann auch auf konkrete Situationen anwenden. 

<|ref|>sub_title<|/ref|><|det|>[[115, 418, 252, 435]]<|/det|>
### 1. Zahlenlotto 

<|ref|>text<|/ref|><|det|>[[115, 435, 857, 485]]<|/det|>
Wie gross ist die Wahrscheinlichkeit, beim Zahlenlotto (es werden 6 aus 49 Kugeln gezogen) 3 Richtige zu haben? Bestimmen Sie auch den Erwartungswert und die Varianz. 

<|ref|>text<|/ref|><|det|>[[115, 500, 780, 571]]<|/det|>
Hier wird ohne Zurücklegen gezogen, weil eine einmal ausgewählte Kugel nicht ein weiteres Mal unter den "Richtigen" erscheinen darf. Insgesamt liegen \(N = 49\) Kugeln in der Urne, von denen \(M = 6\) "Richtige" sind. Die Wahrscheinlichkeit für \(X = 3\) "Richtige" beträgt 

<|ref|>equation<|/ref|><|det|>[[196, 577, 694, 660]]<|/det|>
\[f(3) = \frac{\binom{M}{x} \binom{N-M}{n-x}}{\binom{N}{n}} = \frac{\binom{6}{3} \binom{49-6}{6-3}}{\binom{49}{6}} = \frac{20 \cdot 12.341}{13.983.816} = 0,018.\]

<|ref|>text<|/ref|><|det|>[[115, 670, 780, 738]]<|/det|>
Hierbei gibt es 20 verschiedene Möglichkeiten, 3 aus insgesamt 6 "Richtigen" zu ziehen, 12.341 verschiedene Möglichkeiten, 3 aus insgesamt 43 "Falschen" auszuwählen und 13.983.816 verschiedene Möglichkeiten, 6 aus insgesamt 49 Kugeln zu ziehen. 

<|ref|>text<|/ref|><|det|>[[115, 745, 780, 780]]<|/det|>
Wie groß sind arithmetisches Mittel und Varianz bei den Richtigen im Lottospiel? Pro Tippreihe hat man also im Durchschnitt 0,735 Richtige, 

<|ref|>equation<|/ref|><|det|>[[212, 787, 536, 821]]<|/det|>
\[\mu = E(X) = n \cdot \frac{M}{N} = 6 \cdot \frac{6}{49} = \frac{36}{49} = 0,735.\]

<|ref|>text<|/ref|><|det|>[[115, 825, 286, 842]]<|/det|>
Die Varianz beträgt: 

<|ref|>equation<|/ref|><|det|>[[212, 848, 740, 886]]<|/det|>
\[\sigma^2 = n \cdot \frac{M}{N} \cdot \left(1 - \frac{M}{N}\right) \left(\frac{N-n}{N-1}\right) = 6 \cdot \frac{6}{49} \cdot \left(1 - \frac{6}{49}\right) \cdot \left(\frac{49-6}{49-1}\right) = 0,578.\]