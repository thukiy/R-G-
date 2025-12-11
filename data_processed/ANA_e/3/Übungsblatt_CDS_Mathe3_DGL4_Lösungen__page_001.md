<|ref|>title<|/ref|><|det|>[[115, 166, 485, 202]]<|/det|>
# Übungsblatt DGL 4 

<|ref|>text<|/ref|><|det|>[[575, 179, 880, 196]]<|/det|>
Computational and Data Science 

<|ref|>text<|/ref|><|det|>[[755, 199, 880, 215]]<|/det|>
BSc HS2024 

<|ref|>sub_title<|/ref|><|det|>[[115, 232, 270, 260]]<|/det|>
## Lösungen 

<|ref|>text<|/ref|><|det|>[[750, 240, 880, 257]]<|/det|>
Mathematik 3 

<|ref|>text<|/ref|><|det|>[[115, 287, 210, 304]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 303, 848, 338]]<|/det|>
- Sie kennen die Begriffe linear homogen, linear inhomogen, Inhomogenität und Variation der Konstanten sowie deren wichtigste Eigenschaften. 

<|ref|>text<|/ref|><|det|>[[115, 336, 855, 386]]<|/det|>
- Sie können die allgemeine Lösung von linear homogenen DGL 1. Ordnung und AWP mit linear homogenen DGL 1. Ordnung bestimmen und können diese anwenden. 

<|ref|>text<|/ref|><|det|>[[115, 385, 843, 435]]<|/det|>
- Sie können die allgemeine Lösung einer linear inhomogenen DGL 1. Ordnung sowie die Lösung eines AWP mit linear inhomogener DGL 1. Ordnung mit der Methode der Variation der Konstanten bestimmen. 

<|ref|>sub_title<|/ref|><|det|>[[115, 466, 520, 485]]<|/det|>
### 1. Aussagen über lineare DGL 1. Ordnung 

<|ref|>text<|/ref|><|det|>[[115, 492, 790, 513]]<|/det|>
Gegeben ist die allgemeine lineare DGL 1. Ordnung: \(y' = m(x) \cdot y + q(x)\). 

<|ref|>text<|/ref|><|det|>[[115, 526, 680, 545]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[115, 543, 880, 699]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Die DGL ist genau dann separierbar, wenn gilt: \(q(x) = 0\).</td><td></td><td>X</td></tr><tr><td>b) Ist \(y_1\) eine Lösung, dann gilt dies auch für die Funktion \(y_2 = -5y_1\).</td><td></td><td>X</td></tr><tr><td>c) Sind \(y_1\) und \(y_2\) Lösungen, dann gilt dies auch für die Funktion \(y_3 = y_2 - y_1\).</td><td></td><td>X</td></tr><tr><td>d) Die Methode der Variation der Konstanten basiert auf der Produktregel der Differentialrechnung.</td><td>X</td><td></td></tr><tr><td>e) Um die Methode der Variation der Konstanten auf obige DGL anwenden zu können, braucht es eine Stammfunktion von \(q(x)\).</td><td></td><td>X</td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[115, 713, 410, 731]]<|/det|>
### 2. Homogene DGL 1. Ordnung 

<|ref|>text<|/ref|><|det|>[[115, 730, 325, 747]]<|/det|>
Gegeben sei das AWP 

<|ref|>text<|/ref|><|det|>[[115, 747, 293, 765]]<|/det|>
DGL: \(y' = m(x) \cdot y\), 

<|ref|>text<|/ref|><|det|>[[115, 764, 260, 782]]<|/det|>
AB: \(y(x_0) = y_0\). 

<|ref|>text<|/ref|><|det|>[[115, 781, 760, 799]]<|/det|>
a) Zeigen Sie, dass die allgemeine Lösung der DGL gegeben ist durch: 

<|ref|>equation<|/ref|><|det|>[[144, 797, 848, 817]]<|/det|>
\[y(x) = C \cdot e^{M(x)} \text{ mit } C \in \mathbb{R} \text{ und } M(x) \text{ sei eine beliebige Stammfunktion von } m(x).\]

<|ref|>text<|/ref|><|det|>[[115, 815, 666, 833]]<|/det|>
b) Zeigen Sie, dass die Lösung des AWP gegeben ist durch: 

<|ref|>equation<|/ref|><|det|>[[144, 831, 850, 868]]<|/det|>
\[y(x) = y_0 \cdot e^{M(x) - M(x_0)} \text{ mit } C \in \mathbb{R} \text{ und } M_0(x) \text{ sei eine beliebige Stammfunktion von } m_0(x).\]

<|ref|>text<|/ref|><|det|>[[115, 866, 710, 886]]<|/det|>
c) Bestimmen Sie die allgemeine Lösung der DGL \(y' = \cos(x) \cdot y\).