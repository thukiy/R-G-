<|ref|>title<|/ref|><|det|>[[115, 165, 465, 201]]<|/det|>
# Übungsblatt Sto 6 

<|ref|>text<|/ref|><|det|>[[575, 179, 880, 196]]<|/det|>
Computational and Data Science 

<|ref|>text<|/ref|><|det|>[[757, 199, 880, 215]]<|/det|>
BSc HS2024 

<|ref|>text<|/ref|><|det|>[[115, 231, 270, 260]]<|/det|>
## Lösungen 

<|ref|>text<|/ref|><|det|>[[750, 240, 880, 257]]<|/det|>
Mathematik 3 

<|ref|>text<|/ref|><|det|>[[115, 286, 210, 304]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 303, 820, 338]]<|/det|>
- Sie kennen die Begriffe Additionssatz für Mittelwerte, Multiplikationssatz für Mittelwerte, Additionssatz für Varianzen und können diese anwenden. 

<|ref|>text<|/ref|><|det|>[[115, 336, 850, 370]]<|/det|>
- Sie können Mittelwerte und Varianzen von Kombinationen von Zufallsvariablen bestimmen. 

<|ref|>sub_title<|/ref|><|det|>[[115, 402, 513, 420]]<|/det|>
### 1. Erwartungswerte von Zufallsvariablen 

<|ref|>text<|/ref|><|det|>[[115, 418, 765, 454]]<|/det|>
Die Zufallsvariablen X₁, X₂, X₃ und X₄ besitzen die folgenden Mittel- bzw. Erwartungswerte: 

<|ref|>table<|/ref|><|det|>[[320, 457, 677, 513]]<|/det|>
<table><tr><td>\(X_i\)</td><td>\(X_1\)</td><td>\(X_2\)</td><td>\(X_3\)</td><td>\(X_4\)</td></tr><tr><td>\(\mu_i = E(X_i)\)</td><td>2</td><td>5</td><td>-3</td><td>1</td></tr></table>

<|ref|>text<|/ref|><|det|>[[115, 513, 720, 532]]<|/det|>
Bestimmen Sie den Erwartungswert der folgenden Zufallsvariablen: 

<|ref|>text<|/ref|><|det|>[[115, 530, 320, 547]]<|/det|>
a) \(Z_1 = X_1 + 2X_2 - 5X_4\) 

<|ref|>text<|/ref|><|det|>[[115, 546, 380, 565]]<|/det|>
b) \(Z_2 = X_1 + 8X_2 - 3(X_3 + X_4)\) 

<|ref|>text<|/ref|><|det|>[[115, 563, 360, 581]]<|/det|>
c) \(Z_3 = X_1 + X_2 + 2X_3 - X_4\) 

<|ref|>text<|/ref|><|det|>[[120, 597, 614, 615]]<|/det|>
Additions- bzw. Linearitätssatz für Mittelwerte verwenden: 

<|ref|>equation<|/ref|><|det|>[[120, 618, 646, 638]]<|/det|>
\[
\text{a) } E(Z_1) = \mu_1 + 2\mu_2 - 5\mu_4 = 2 + 2 \cdot 5 - 5 \cdot 1 = 7
\]

<|ref|>equation<|/ref|><|det|>[[120, 645, 780, 665]]<|/det|>
\[
\text{b) } E(Z_2) = \mu_1 + 8\mu_2 - 3(\mu_3 + \mu_4) = 2 + 8 \cdot 5 - 3(-3 + 1) = 48
\]

<|ref|>equation<|/ref|><|det|>[[120, 672, 713, 692]]<|/det|>
\[
\text{c) } E(Z_3) = \mu_1 + \mu_2 + 2\mu_3 - \mu_4 = 2 + 5 + 2(-3) - 1 = 0
\]

<|ref|>sub_title<|/ref|><|det|>[[115, 710, 525, 728]]<|/det|>
### 2. Erwartungswerte von Zufallsvariablen II 

<|ref|>text<|/ref|><|det|>[[115, 727, 870, 761]]<|/det|>
Die stochastisch unabhängigen Zufallsvariablen Xᵢ besitzen die Mittelwerte μᵢ = E(Xᵢ) = 2i² (i = 1, 2, 3, 4). Welchen Mittelwert besitzen dann die folgenden Produkte? 

<|ref|>equation<|/ref|><|det|>[[115, 760, 590, 778]]<|/det|>
\[
\text{a) } Z_1 = X_1 * X_2 * X_3 * X_4 \quad \text{b) } Z_2 = X_1 * (X_2 + X_3)
\]

<|ref|>equation<|/ref|><|det|>[[115, 777, 551, 795]]<|/det|>
\[
\text{c) } Z_3 = (X_1 - X_2) * (X_1 + X_2) \quad \text{d) } Z_4 = 3X_1 * X_4^2
\]