<|ref|>title<|/ref|><|det|>[[115, 166, 465, 201]]<|/det|>
# Übungsblatt Sto 5 

<|ref|>text<|/ref|><|det|>[[575, 179, 880, 216]]<|/det|>
Computational and Data Science
BSc HS2023 

<|ref|>text<|/ref|><|det|>[[115, 233, 270, 261]]<|/det|>
## Lösungen 

<|ref|>text<|/ref|><|det|>[[752, 240, 880, 258]]<|/det|>
Mathematik 1 

<|ref|>text<|/ref|><|det|>[[115, 287, 210, 305]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 303, 855, 370]]<|/det|>
- Sie kennen die Begriffe Additionssatz, Multiplikationssatz, bedingte Wahrscheinlichkeit, totale Wahrscheinlichkeit, abhängige/unabhängige Ereignisse, Ereignisbaum, Satz von Bayes und deren wichtigste Eigenschaften und können diese erklären. 

<|ref|>text<|/ref|><|det|>[[115, 369, 874, 404]]<|/det|>
- Sie können Additionssatz, Multiplikationssatz, bedingte Wahrscheinlichkeit, totale
Wahrscheinlichkeit und Satz von Bayes auf konkrete Situationen anwenden. 

<|ref|>text<|/ref|><|det|>[[115, 402, 825, 420]]<|/det|>
- Sie können Wahrscheinlichkeiten mit Hilfe eines Ereignisbaums bestimmen. 

<|ref|>sub_title<|/ref|><|det|>[[115, 451, 317, 469]]<|/det|>
### 1. Qualitätskontrolle 

<|ref|>text<|/ref|><|det|>[[115, 468, 878, 551]]<|/det|>
Bei einer Qualitätskontrolle haben von 60 kontrollierten Stücken 15 den Defekt A und 12 den Defekt B. 38 Stück bieten keinen Anlass zur Beanstandung. Bestimmen Sie die Wahrscheinlichkeit dafür, dass ein Stück, das den Defekt A aufweist, auch den Defekt B hat. Zeichnen Sie auch einen Ereignisbaum für alle Fälle, die eintreten können. 

<|ref|>text<|/ref|><|det|>[[120, 565, 875, 625]]<|/det|>
Insgesamt sind \(22(=60-38)\) Stück defekt. Haben 15 Teile den Defekt A und 12 Stück den Defekt B, so müssen \((15+12)-22=5\) Teile gleichzeitig den Defekt A und den Defekt B haben. Folgende Wahrscheinlichkeiten sind gegeben: 

<|ref|>equation<|/ref|><|det|>[[120, 639, 870, 686]]<|/det|>
\[P(A) = \frac{|A|}{|\Omega|} = \frac{15}{60} = 0,25, \quad P(B) = \frac{|B|}{|\Omega|} = \frac{12}{60} = 0,20, \quad P(A \cap B) = \frac{|A \cap B|}{|\Omega|} = \frac{5}{60} = 0,083.\]

<|ref|>text<|/ref|><|det|>[[120, 699, 875, 777]]<|/det|>
Wir wissen, dass das Ereignis A = "Teil hat den Defekt A" bereits eingetreten ist. Gesucht ist die Wahrscheinlichkeit dafür, dass zusätzlich noch B = "Teil hat den Defekt B" eintritt. Hierbei handelt es sich um die Wahrscheinlichkeit von B unter der Bedingung von A.