<|ref|>sub_title<|/ref|><|det|>[[115, 166, 488, 202]]<|/det|>
# Übungsblatt DGL 3 

<|ref|>text<|/ref|><|det|>[[576, 179, 880, 196]]<|/det|>
Computational and Data Science 

<|ref|>text<|/ref|><|det|>[[757, 199, 880, 216]]<|/det|>
BSc HS2024 

<|ref|>sub_title<|/ref|><|det|>[[115, 232, 270, 261]]<|/det|>
## Lösungen 

<|ref|>text<|/ref|><|det|>[[752, 240, 880, 258]]<|/det|>
Mathematik 3 

<|ref|>text<|/ref|><|det|>[[115, 286, 210, 303]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 303, 875, 354]]<|/det|>
- Sie kennen die Methode der Trennung der Variablen und können diese sowohl zur Lösung von separierbaren DGL anwenden als zur Lösung von AWP, die eine separierbare DGL enthalten. 

<|ref|>sub_title<|/ref|><|det|>[[115, 386, 463, 404]]<|/det|>
### 1. Aussagen über separierbare DGL 

<|ref|>text<|/ref|><|det|>[[115, 410, 680, 428]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[115, 426, 880, 629]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Jede analytisch isolierbare autonome DGL 1. Ordnung ist separierbar.</td><td>X</td><td></td></tr><tr><td>b) Jede elementar integrierbare DGL ist separierbar.</td><td>X</td><td></td></tr><tr><td>c) Jede separierbare DGL hat genau eine Lösung.</td><td></td><td>X</td></tr><tr><td>d) Die Methode der Trennung der Variablen beruht auf der Substitutionsregel, die in der Integralrechnung ihre Anwendung findet.</td><td>X</td><td></td></tr><tr><td>e) Die Methode der Trennung der Variablen kann nur auf lineare DGL angewandt werden.</td><td></td><td>X</td></tr><tr><td>f) Um ein AWP mit separierbarer DGL zu lösen, muss zuerst die allgemeine Lösung der DGL bestimmt werden.</td><td></td><td>X</td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[115, 645, 315, 662]]<|/det|>
### 2. Separierbare DGL 

<|ref|>text<|/ref|><|det|>[[115, 661, 220, 679]]<|/det|>
a) \(y' = 2y\) 

<|ref|>text<|/ref|><|det|>[[115, 677, 220, 696]]<|/det|>
d) \(y' = x^2y^3\) 

<|ref|>text<|/ref|><|det|>[[115, 695, 260, 714]]<|/det|>
g) \(x^2 y' = y(x-y)\) 

<|ref|>text<|/ref|><|det|>[[375, 660, 470, 679]]<|/det|>
b) \(y' = xy\) 

<|ref|>text<|/ref|><|det|>[[375, 677, 500, 696]]<|/det|>
e) \(y' = 1 + y^2\) 

<|ref|>text<|/ref|><|det|>[[375, 694, 536, 714]]<|/det|>
h) \(xyy' = 4x^2 + y^2\) 

<|ref|>text<|/ref|><|det|>[[632, 660, 720, 679]]<|/det|>
c) \(y' = y^2\) 

<|ref|>text<|/ref|><|det|>[[632, 677, 777, 696]]<|/det|>
f) \(y' = 3x^2y + x^2\) 

<|ref|>text<|/ref|><|det|>[[115, 728, 145, 745]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[115, 744, 386, 762]]<|/det|>
Statische Lösungen: \(y_s(x) = 0\). 

<|ref|>text<|/ref|><|det|>[[115, 761, 857, 779]]<|/det|>
Nicht statische Lösungen mit der Methode der Trennung der Variablen bestimmen: 

<|ref|>equation<|/ref|><|det|>[[328, 784, 400, 803]]<|/det|>
\[y' = 2 \cdot y\]

<|ref|>equation<|/ref|><|det|>[[597, 783, 640, 803]]<|/det|>
\[: y\]

<|ref|>equation<|/ref|><|det|>[[115, 812, 390, 850]]<|/det|>
\[\Leftrightarrow \quad \frac{1}{y} \cdot y' = 2\]

<|ref|>equation<|/ref|><|det|>[[597, 808, 688, 847]]<|/det|>
\[\int \ldots dx\]

<|ref|>equation<|/ref|><|det|>[[115, 855, 520, 890]]<|/det|>
\[\Leftrightarrow \quad \int \frac{1}{y} \cdot y' dx = \int \frac{1}{y} dy = \int 2 dx = 2 \int 1 dx\]