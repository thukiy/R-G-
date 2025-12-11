<|ref|>title<|/ref|><|det|>[[115, 183, 455, 217]]<|/det|>
Übungsblatt LA 9 

<|ref|>text<|/ref|><|det|>[[575, 196, 880, 231]]<|/det|>
Computational and Data Science
FS2024 

<|ref|>text<|/ref|><|det|>[[115, 250, 270, 277]]<|/det|>
Lösungen 

<|ref|>text<|/ref|><|det|>[[750, 258, 880, 275]]<|/det|>
Mathematik 2 

<|ref|>text<|/ref|><|det|>[[115, 303, 210, 320]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 320, 860, 371]]<|/det|>
- Sie kennen die Begriffe Axiom, Skalarkörper, Vektorraum, Linearkombination, lineare Hülle, linear abhängig, linear unabhängig, erzeugend, Basis, Dimension, Bild, Kern und deren wichtigste Eigenschaften. 

<|ref|>text<|/ref|><|det|>[[115, 369, 863, 404]]<|/det|>
- Sie können beurteilen, ob die Vektoren einer Teilmenge von \(\mathbb{R}^n\) linear abhängig, linear unabhängig oder erzeugend sind und ob sie eine Basis bilden. 

<|ref|>text<|/ref|><|det|>[[115, 403, 707, 420]]<|/det|>
- Sie können Bild und Kern einer linearen Abbildung berechnen. 

<|ref|>sub_title<|/ref|><|det|>[[115, 452, 418, 469]]<|/det|>
1. Aussagen über Vektorräume 

<|ref|>text<|/ref|><|det|>[[115, 468, 680, 485]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[115, 483, 880, 655]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Der Vektorraum ist die fundamentale Struktur der linearen Algebra.</td><td>X</td><td></td></tr><tr><td>b) Jeder Vektorraum basiert auf einem Skalarkörper.</td><td>X</td><td></td></tr><tr><td>c) In jedem Vektorraum ist eine Addition zwischen den Vektoren definiert.</td><td>X</td><td></td></tr><tr><td>d) In jedem Vektorraum ist eine Multiplikation zwischen den Vektoren definiert.</td><td></td><td>X</td></tr><tr><td>e) In jedem Vektorraum ist eine Multiplikation zwischen den Vektoren und den reellen Zahlen definiert.</td><td></td><td>X</td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[115, 670, 356, 687]]<|/det|>
2. Vektorraumstrukturen 

<|ref|>text<|/ref|><|det|>[[115, 686, 796, 721]]<|/det|>
Welche der folgenden Strukturen bilden bezüglich der üblichen Addition und Multiplikation einen Vektorraum? Begründen Sie Ihre Antwort. 

<|ref|>text<|/ref|><|det|>[[115, 720, 254, 737]]<|/det|>
a) \((\mathbb{Z}; \mathbb{Q}; +; \cdot)\) 

<|ref|>text<|/ref|><|det|>[[115, 736, 250, 754]]<|/det|>
d) \((\mathbb{Q}^2; \mathbb{R}; +; \cdot)\) 

<|ref|>text<|/ref|><|det|>[[408, 720, 520, 737]]<|/det|>
b) \((\mathbb{Z}; \mathbb{R}; +; \cdot)\) 

<|ref|>text<|/ref|><|det|>[[408, 736, 536, 754]]<|/det|>
e) \((\mathbb{R}^3; \mathbb{Q}; +; \cdot)\) 

<|ref|>text<|/ref|><|det|>[[680, 720, 810, 737]]<|/det|>
c) \((\mathbb{Q}^2; \mathbb{Q}; +; \cdot)\) 

<|ref|>text<|/ref|><|det|>[[680, 736, 805, 754]]<|/det|>
f) \((\mathbb{R}^3; \mathbb{R}; +; \cdot)\) 

<|ref|>text<|/ref|><|det|>[[115, 770, 140, 786]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[115, 786, 370, 803]]<|/det|>
Wir betrachten das *Quadrupel* 

<|ref|>equation<|/ref|><|det|>[[415, 812, 533, 831]]<|/det|>
\[(\mathbb{Z}; \mathbb{Q}; +; \cdot).\]

<|ref|>text<|/ref|><|det|>[[115, 839, 530, 856]]<|/det|>
Wählen wir \(a := 1/2 \in \mathbb{Q}\) und \(v := 1 \in \mathbb{Z}\), dann gilt 

<|ref|>equation<|/ref|><|det|>[[384, 864, 561, 896]]<|/det|>
\[a \cdot v = \frac{1}{2} \cdot 1 = \frac{1}{2} \notin \mathbb{Z}.\]

<|ref|>text<|/ref|><|det|>[[115, 896, 461, 913]]<|/det|>
Es wird also kein Vektorraum gebildet.