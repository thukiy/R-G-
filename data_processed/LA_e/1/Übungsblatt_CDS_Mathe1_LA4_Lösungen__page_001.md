<|ref|>title<|/ref|><|det|>[[115, 166, 456, 201]]<|/det|>
# Übungsblatt LA 4 

<|ref|>text<|/ref|><|det|>[[572, 179, 880, 216]]<|/det|>
Computational and Data Science
BSc HS2023 

<|ref|>text<|/ref|><|det|>[[115, 232, 270, 260]]<|/det|>
## Lösungen 

<|ref|>text<|/ref|><|det|>[[752, 240, 880, 258]]<|/det|>
Mathematik 1 

<|ref|>text<|/ref|><|det|>[[115, 287, 210, 305]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 303, 846, 354]]<|/det|>
- Sie kennen die Begriffe Stufenform, reduzierte Stufenform, Dimensionszahl, Rang, Defekt, Pivot-Variable, freier Parameter und Verträglichkeit sowie deren wichtigsten Eigenschaften. 

<|ref|>text<|/ref|><|det|>[[115, 352, 837, 402]]<|/det|>
- Sie können Rang, Defekt, Pivot-Variablen und freie Parameter für jedes LGS anhand einer Stufenform bestimmen und die Verträglichkeit auf jeder Zeile prüfen. 

<|ref|>text<|/ref|><|det|>[[115, 401, 863, 451]]<|/det|>
- Sie können anhand der Dimensionszahlen Rang und Defekt sowie den Verträglichkeiten auf jeder Zeile einer Stufenform die Lösungsmenge eines LGS beurteilen. 

<|ref|>text<|/ref|><|det|>[[115, 450, 803, 485]]<|/det|>
- Sie können die Lösungsmenge eines beliebigen LGS bzw. eines LGS mit Paramtern mit Hilfe des Gauß- und Gauß-Jordan-Verfahrens bestimmen. 

<|ref|>sub_title<|/ref|><|det|>[[115, 516, 545, 535]]<|/det|>
### 1. Aussagen über lineare Gleichungssystem 

<|ref|>text<|/ref|><|det|>[[115, 533, 680, 550]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[115, 548, 880, 671]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Jedes LGS hat genau eine Stufenform.</td><td></td><td>X</td></tr><tr><td>b) Jedes LGS hat genau eine reduzierte Stufenform.</td><td>X</td><td></td></tr><tr><td>c) Ist ein LGS eindeutig lösbar, dann gilt: \(n_R = n_V\).</td><td>X</td><td></td></tr><tr><td>d) Gilt für ein LGS \(n_R = n_V\), dann ist es eindeutig lösbar.</td><td></td><td>X</td></tr><tr><td>e) Die Lösungsmenge besteht niemals aus genau 2 Elementen.</td><td>X</td><td></td></tr><tr><td>f) Für den Defekt eines LGS gilt: \(n_D \le n_G\).</td><td></td><td>X</td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[115, 686, 277, 703]]<|/det|>
### 2. Stufenformen 

<|ref|>text<|/ref|><|det|>[[115, 702, 870, 737]]<|/det|>
Bestimmen Sie jeweils die Pivot-Elemente, Pivot-Variablen, freien Parameter, Rang, Defekt und Lösungsmenge. 

<|ref|>equation<|/ref|><|det|>[[115, 750, 197, 784]]<|/det|>
a) \(\begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}\)

<|ref|>equation<|/ref|><|det|>[[488, 750, 597, 784]]<|/det|>
b) \(\begin{bmatrix} 2 & 0 \\ 0 & 0 \end{bmatrix}\)

<|ref|>equation<|/ref|><|det|>[[115, 797, 217, 831]]<|/det|>
c) \(\begin{bmatrix} 0 & 2 \\ 0 & 0 \end{bmatrix}\)

<|ref|>equation<|/ref|><|det|>[[488, 797, 597, 831]]<|/det|>
d) \(\begin{bmatrix} 2 & 5 \\ 0 & 0 \end{bmatrix}\)

<|ref|>equation<|/ref|><|det|>[[115, 843, 217, 877]]<|/det|>
e) \(\begin{bmatrix} 0 & 6 \\ 0 & 0 \end{bmatrix}\)

<|ref|>equation<|/ref|><|det|>[[488, 843, 597, 877]]<|/det|>
f) \(\begin{bmatrix} 2 & 0 \\ 0 & 0 \end{bmatrix} \)

<|ref|>equation<|/ref|><|det|>[[115, 889, 217, 923]]<|/det|>
g) \(\begin{bmatrix} 0 & 2 \\ 0 & 0 \end{bmatrix} \)

<|ref|>equation<|/ref|><|det|>[[488, 889, 597, 923]]<|/det|>
h) \(\begin{bmatrix} 2 & 2 \\ 0 & 0 \end{bmatrix} \)
</table>