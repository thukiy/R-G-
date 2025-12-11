<|ref|>title<|/ref|><|det|>[[115, 165, 465, 201]]<|/det|>
# Übungsblatt Sto 7 

<|ref|>text<|/ref|><|det|>[[575, 179, 880, 216]]<|/det|>
Computational and Data Science
BSc HS2023 

<|ref|>text<|/ref|><|det|>[[115, 232, 270, 261]]<|/det|>
## Lösungen 

<|ref|>text<|/ref|><|det|>[[752, 240, 880, 258]]<|/det|>
Mathematik 1 

<|ref|>text<|/ref|><|det|>[[115, 287, 210, 304]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 303, 725, 338]]<|/det|>
- Sie kennen die Begriffe Erwartungswert, Mittelwert, Varianz und Standardabweichung und können diese anwenden und erklären. 

<|ref|>text<|/ref|><|det|>[[115, 337, 718, 371]]<|/det|>
- Sie können den Erwartungswert, Mittelwert, die Varianz und die Standardabweichung für diskrete Zufallsvariablen bestimmen. 

<|ref|>sub_title<|/ref|><|det|>[[115, 402, 545, 420]]<|/det|>
### 1. Erwartungswert diskreter Zufallsvariablen 

<|ref|>text<|/ref|><|det|>[[115, 418, 763, 437]]<|/det|>
Welchen Erwartungswert besitzen die folgenden diskreten Verteilungen: 

<|ref|>text<|/ref|><|det|>[[115, 436, 144, 453]]<|/det|>
a) 

<|ref|>table<|/ref|><|det|>[[115, 451, 880, 490]]<|/det|>
<table><tr><td>xi</td><td>-1</td><td>0</td><td>1</td><td>2</td><td>3</td></tr><tr><td>f(xi)</td><td>0,1</td><td>0,3</td><td>0,4</td><td>0,15</td><td>0,05</td></tr></table>

<|ref|>text<|/ref|><|det|>[[115, 503, 144, 520]]<|/det|>
b) 

<|ref|>table<|/ref|><|det|>[[115, 518, 880, 557]]<|/det|>
<table><tr><td>xi</td><td>-2</td><td>-1</td><td>0</td><td>1</td><td>4</td><td>5</td><td>10</td></tr><tr><td>f(xi)</td><td>1/12</td><td>2/12</td><td>2/12</td><td>3/12</td><td>2/12</td><td>1/12</td><td>1/12</td></tr></table>

<|ref|>text<|/ref|><|det|>[[115, 572, 144, 589]]<|/det|>
c) 

<|ref|>table<|/ref|><|det|>[[115, 587, 755, 624]]<|/det|>
<table><tr><td>xi</td><td>-2</td><td>-1</td><td>1</td><td>2</td></tr><tr><td>f(xi)</td><td>1/8</td><td>3/8</td><td>1/4</td><td>1/4</td></tr></table>

<|ref|>text<|/ref|><|det|>[[115, 622, 822, 657]]<|/det|>
d) Bestimmen Sie für c) ausserdem den Erwartungswert der von X abhängigen Funktionen \(Z_1 = g_1(X) = 5X + 2\), \(Z_2 = g_2(X) = X^2\). 

<|ref|>equation<|/ref|><|det|>[[120, 674, 580, 693]]<|/det|>
\[
a) \quad E(X) = -0,1 + 0 + 0,4 + 0,3 + 0,15 = 0,75
\]

<|ref|>equation<|/ref|><|det|>[[120, 697, 690, 735]]<|/det|>
\[
b) \quad E(X) = -\frac{2}{12} - \frac{2}{12} + 0 + \frac{3}{12} + \frac{8}{12} + \frac{5}{12} + \frac{10}{12} = \frac{22}{12} = \frac{11}{6}
\]

<|ref|>text<|/ref|><|det|>[[115, 738, 144, 755]]<|/det|>
c) 

<|ref|>equation<|/ref|><|det|>[[125, 757, 456, 794]]<|/det|>
\[
E(X) = -\frac{2}{8} - \frac{3}{8} + \frac{1}{4} + \frac{2}{4} = \frac{1}{8}
\]

<|ref|>text<|/ref|><|det|>[[115, 796, 144, 813]]<|/det|>
d) 

<|ref|>equation<|/ref|><|det|>[[125, 812, 728, 849]]<|/det|>
\[
\text{Linearitätssatz: } E(Z_1) = E(5X + 2) = 5 \cdot E(X) + 2 = 5 \cdot \frac{1}{8} + 2 = \frac{21}{8}
\]

<|ref|>equation<|/ref|><|det|>[[125, 853, 636, 889]]<|/det|>
\[
E(Z_2) = E(X^2) = \sum x_i^2 \cdot f(x_i) = \frac{4}{8} + \frac{3}{8} + \frac{1}{4} + \frac{4}{4} = \frac{17}{8}
\]