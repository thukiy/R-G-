<|ref|>title<|/ref|><|det|>[[115, 166, 485, 201]]<|/det|>
# Übungsblatt DGL 5 

<|ref|>text<|/ref|><|det|>[[575, 179, 880, 196]]<|/det|>
Computational and Data Science 

<|ref|>text<|/ref|><|det|>[[755, 199, 880, 215]]<|/det|>
BSc HS2024 

<|ref|>text<|/ref|><|det|>[[115, 232, 270, 260]]<|/det|>
## Lösungen 

<|ref|>text<|/ref|><|det|>[[750, 240, 880, 257]]<|/det|>
Mathematik 3 

<|ref|>text<|/ref|><|det|>[[115, 287, 210, 304]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 303, 840, 339]]<|/det|>
- Sie kennen die Begriffe linear homogene DGL 2. Ordnung, charakteristisches Polynom, Basislösung und Wronski Determinante sowie deren Bedeutung. 

<|ref|>text<|/ref|><|det|>[[115, 337, 781, 370]]<|/det|>
- Sie können DGL 2. Ordnung bzgl. linear, linear homogen und autonom klassifizieren. 

<|ref|>text<|/ref|><|det|>[[115, 369, 861, 420]]<|/det|>
- Sie können die allgemeine Lösung einer linear homogenen DGL 2. Ordnung mit Hilfe des charakteristischen Polynoms bestimmen und können auch die Basislösungen bestimmen. 

<|ref|>sub_title<|/ref|><|det|>[[115, 450, 615, 469]]<|/det|>
### 1. Aussagen über linear homogene DGL 2. Ordnung 

<|ref|>text<|/ref|><|det|>[[115, 476, 680, 494]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[115, 492, 880, 680]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Linear homogene DGL 2. Ordnung sind zur (theoretischen) Bestimmung von Schwingungen relevant.</td><td>X</td><td></td></tr><tr><td>b) Das charakteristische Polynom einer linear homogenen DGL 2. Ordnung ist eine quadratische Funktion.</td><td>X</td><td></td></tr><tr><td>c) Jede Lösung einer linear homogenen DGL 2. Ordnung kann als Linearkombination von 2 Basislösungen geschrieben werden.</td><td>X</td><td></td></tr><tr><td>d) Ein eindeutig lösbares AWP mit einer linear homogenen DGL 2. Ordnung benötigt genau 2 ABs.</td><td>X</td><td></td></tr><tr><td>e) Ein eindeutig lösbares RWP mit einer linear homogenen DGL 2. Ordnung benötigt genau 2 RBs.</td><td>X</td><td></td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[115, 694, 300, 711]]<|/det|>
### 2. DGL 2. Ordnung 

<|ref|>text<|/ref|><|det|>[[115, 710, 803, 728]]<|/det|>
Seien \(a, b, c \in \mathbb{R}\) mit \(a \neq 0\). Gegeben sei die folgende linear homogene DGL 2. 

<|ref|>text<|/ref|><|det|>[[115, 727, 636, 746]]<|/det|>
Ordnung mit konstanten Koeffizienten \(ay' + by' + cy = 0\). 

<|ref|>text<|/ref|><|det|>[[115, 745, 728, 763]]<|/det|>
a) \(y_1(x)\) sei eine Lösung der DGL und es sei \(C \in \mathbb{R}\). Zeigen Sie, dass 

<|ref|>equation<|/ref|><|det|>[[144, 761, 608, 780]]<|/det|>
\[y(x) := C \cdot y_1(x) \text{ ebenfalls eine Lösung der DGL ist.}\]

<|ref|>text<|/ref|><|det|>[[115, 778, 789, 796]]<|/det|>
b) \(y_1(x)\) und \(y_2(x)\) seien Lösungen der DGL. Zeigen Sie, dass die Summe 

<|ref|>equation<|/ref|><|det|>[[144, 794, 647, 813]]<|/det|>
\[y(x) = y_1(x) + y_2(x) \text{ ebenfalls eine Lösung der DGL ist.}\]

<|ref|>text<|/ref|><|det|>[[0, 0, 0, 0]]<|/det|>
c) \(y_1(x)\) und \(y_2(x)\) seien Lösungen der DG und es sei \(C_1, C_2 \in \mathbb{R}\). Zeigen Sie, dass 

<|ref|>equation<|/ref|><|det|>[[144, clef 0, 848, 0]]<|/det|>
\[y(x) := C_1 \cdot y_1(x) + C_2 \cdot y_2(x) \text{ ebenfalls eine Lösung der DGL ist.}\]