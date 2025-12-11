<|ref|>sub_title<|/ref|><|det|>[[115, 183, 455, 219]]<|/det|>
Übungsblatt LA 7 

<|ref|>text<|/ref|><|det|>[[576, 195, 880, 231]]<|/det|>
Computational and Data Science
FS2024 

<|ref|>text<|/ref|><|det|>[[750, 248, 880, 265]]<|/det|>
Mathematik 2 

<|ref|>text<|/ref|><|det|>[[115, 293, 210, 310]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 309, 880, 344]]<|/det|>
- Sie kennen die Begriffe Spur, Determinante, Leibnizsche Formel, Regel von Sarrus, Gramsche Matrix und deren wichtigste Eigenschaften. 

<|ref|>text<|/ref|><|det|>[[115, 342, 880, 376]]<|/det|>
- Sie kennen die Formel zur Berechnung von Massen (Länge, Fläche, Volumen ...) und können sie anwenden. 

<|ref|>text<|/ref|><|det|>[[115, 375, 860, 408]]<|/det|>
- Sie können die Eigenschaften einer Matrix anhand ihrer Spur und Determinante beurteilen. 

<|ref|>text<|/ref|><|det|>[[115, 407, 848, 425]]<|/det|>
- Sie können die Determinante quadratischer Matrizen in 2D und 3D berechnen. 

<|ref|>text<|/ref|><|det|>[[115, 424, 781, 458]]<|/det|>
- Sie können die Determinanten einer quadratischen Matrix mit Hilfe des Gaußschen Verfahrens berechnen. 

<|ref|>sub_title<|/ref|><|det|>[[115, 490, 377, 507]]<|/det|>
1. Aussagen über die Spur 

<|ref|>text<|/ref|><|det|>[[115, 506, 680, 524]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[115, 522, 880, 661]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Die Spur ist für jede Matrix definiert.</td><td></td><td>X</td></tr><tr><td>b) Ob eine Matrix regulär oder singulär ist, lässt sich nicht alleine anhand der Spur beurteilen.</td><td>X</td><td></td></tr><tr><td>c) Für alle orthogonalen Matrizen gilt: tr(A<sup>T</sup>·A) = n.</td><td>X</td><td></td></tr><tr><td>d) Für alle quadratischen nxn Matrizen gilt: tr(A·B-B·A) = 0.</td><td>X</td><td></td></tr><tr><td>e) Für alle quadratischen nxn Matrizen gilt: tr(A·B) = tr(A)·tr(B).</td><td></td><td>X</td></tr><tr><td>f) Die Matrix A ist schiefsymmetrisch, wenn gilt: tr(A) = 0.</td><td></td><td>X</td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[115, 676, 635, 694]]<|/det|>
2. Spur und Determinante der Standardmatrizen in 2D 

<|ref|>text<|/ref|><|det|>[[115, 693, 880, 727]]<|/det|>
Bestimmen Sie für die Standardmatrizen E, I, P, Z, P, P, P, S und S jeweils die Spur und die Determinante. 

<|ref|>text<|/ref|><|det|>[[115, 742, 866, 778]]<|/det|>
Die Matrizen E, I, P beschreiben Drehungen, die Matrizen sind somit orthogonal. Es gilt folglich: det(E) = det(I) = det(P) = 1. 

<|ref|>text<|/ref|><|det|>[[115, 776, 863, 811]]<|/det|>
Die Matrizen P, P, P beschreiben Projektionen. Sind sind deshalb singulär und somit gilt: det(P) = det(P) = 0. 

<|ref|>text<|/ref|><|det|>[[115, 809, 783, 844]]<|/det|>
Die Matrizen S und S beschreiben Spiegelungen. Da Spiegelungen nicht orientierungstreu sind, gilt: det(S) = det(S) = -1. 

<|ref|>text<|/ref|><|det|>[[115, 842, 875, 878]]<|/det|>
Die Matrix Z beschreibt eine Streckung um den Faktor λ. Dabei vergrössern sich die Flächen um den Faktor λ² und es folgt: det(Z) = λ².