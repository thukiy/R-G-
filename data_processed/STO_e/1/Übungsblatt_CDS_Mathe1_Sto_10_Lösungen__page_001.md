<|ref|>title<|/ref|><|det|>[[115, 165, 489, 201]]<|/det|>
# Übungsblatt Sto 10 

<|ref|>text<|/ref|><|det|>[[576, 179, 880, 216]]<|/det|>
Computational and Data Science
BSc HS2023 

<|ref|>text<|/ref|><|det|>[[115, 232, 270, 261]]<|/det|>
## Lösungen 

<|ref|>text<|/ref|><|det|>[[752, 240, 880, 258]]<|/det|>
Mathematik 1 

<|ref|>text<|/ref|><|det|>[[115, 287, 210, 305]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 303, 880, 355]]<|/det|>
- Sie kennen die Begriffe stetige Zufallsvariable, Verteilungsfunktion, Dichtefunktion, Wahrscheinlichkeitsverteilung und deren wichtigste Eigenschaften und können diese erklären. 

<|ref|>text<|/ref|><|det|>[[115, 353, 744, 388]]<|/det|>
- Sie kennen den Unterschied zwischen einer diskreten und stetigen Zufallsvariablen und können ihn auf konkrete Beispiele anwenden. 

<|ref|>text<|/ref|><|det|>[[115, 387, 822, 421]]<|/det|>
- Sie können anhand einer gegebenen Dichtefunktion die Verteilungsfunktion bestimmen und umgekehrt. 

<|ref|>text<|/ref|><|det|>[[115, 419, 720, 454]]<|/det|>
- Sie können den Erwartungswert, Mittelwert, die Varianz und die Standardabweichung für eine stetige Zufallsvariable bestimmen. 

<|ref|>sub_title<|/ref|><|det|>[[115, 485, 592, 503]]<|/det|>
### 1. Verteilungsfunktionen stetiger Zufallsvariablen 

<|ref|>text<|/ref|><|det|>[[115, 501, 880, 536]]<|/det|>
X sei eine stetige Zufallsvariable mit der Dichtefunktion f(x). Bestimmen Sie die jeweilige Verteilungsfunktion F(x): 

<|ref|>equation<|/ref|><|det|>[[115, 533, 420, 565]]<|/det|>
\[ \text{a) } f(x) = \frac{1}{2}x \quad (0 \le x \le 2), \]

<|ref|>equation<|/ref|><|det|>[[115, 563, 440, 586]]<|/det|>
\[ \text{b) } f(x) = \lambda \cdot e^{-\lambda x} \quad (x \ge 0; \lambda > 0), \]

<|ref|>equation<|/ref|><|det|>[[115, 583, 385, 615]]<|/det|>
\[ \text{c) } f(x) = \frac{1}{x^2} \quad (x \ge 1). \]

<|ref|>text<|/ref|><|det|>[[125, 628, 842, 647]]<|/det|>
Außerhalb der angegebenen Intervalle verschwindet die Verteilungsfunktion (F(x) = 0). 

<|ref|>equation<|/ref|><|det|>[[125, 650, 666, 703]]<|/det|>
\[ \text{a) } F(x) = \frac{1}{2} \cdot \int_{0}^{x} u \, du = \frac{1}{4} \left[ u^2 \right]_{0}^{x} = \frac{1}{4} x^2 \quad (0 \le x \le 2) \]

<|ref|>equation<|/ref|><|det|>[[125, 707, 824, 760]]<|/det|>
\[ \text{b) } F(x) = \lambda \cdot \int_{0}^{x} e^{-\lambda u} \, du = \lambda \left[ \frac{e^{-\lambda u}}{-\lambda} \right]_{0}^{x} = \left[ -e^{-\lambda u} \right]_{0}^{x} = 1 - e^{-\lambda x} \quad (x \ge 0) \]

<|ref|>equation<|/ref|><|det|>[[125, 794, 608, 847]]<|/det|>
\[ \text{c) } F(x) = \int_{1}^{x} \frac{1}{u^2} \, du = \left[ -\frac{1}{u} \right]_{1}^{x} = 1 - \frac{1}{x} \quad (x \ge 1) \]

<|ref|>sub_title<|/ref|><|det|>[[115, 863, 536, 880]]<|/det|>
### 2. Parameter bei Dichtefunktion bestimmen 

<|ref|>text<|/ref|><|det|>[[115, 879, 880, 914]]<|/det|>
Bestimmen Sie den jeweiligen Parameter in der Dichtefunktion f(x) der stetigen Zufallsvariablen X: