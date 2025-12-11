<|ref|>title<|/ref|><|det|>[[115, 183, 476, 218]]<|/det|>
Übungsblatt LA 12 

<|ref|>text<|/ref|><|det|>[[577, 196, 880, 232]]<|/det|>
Computational and Data Science
BSc HS2023 

<|ref|>text<|/ref|><|det|>[[115, 250, 270, 278]]<|/det|>
Lösungen 

<|ref|>text<|/ref|><|det|>[[750, 258, 878, 275]]<|/det|>
Mathematik 1 

<|ref|>text<|/ref|><|det|>[[115, 304, 210, 321]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 320, 861, 354]]<|/det|>
- Sie kennen die Beschreibung einer Ebene in Parameter-, Normalen- und Hesse Normalform. 

<|ref|>text<|/ref|><|det|>[[115, 353, 761, 371]]<|/det|>
- Sie können den Abstand eines Punktes von einer Ebene bestimmen. 

<|ref|>text<|/ref|><|det|>[[115, 370, 771, 388]]<|/det|>
- Sie können die Lage von Geraden und Ebene zueinander bestimmen. 

<|ref|>sub_title<|/ref|><|det|>[[115, 419, 422, 437]]<|/det|>
1. Aussagen über Ebenen in 3D 

<|ref|>text<|/ref|><|det|>[[115, 436, 680, 454]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[115, 452, 880, 639]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Um eine Ebene in 3D in Parameterform darzustellen, benötigt man genau zwei reelle Parameter.</td><td>X</td><td></td></tr><tr><td>b) Durch Angabe des Einheitsnormalenvektors ist eine Ebene in 3D eindeutig bestimmt.</td><td></td><td>X</td></tr><tr><td>c) Die Gleichung x + y = 1 beschreibt eine Ebene in 3D.</td><td>X</td><td></td></tr><tr><td>d) Die Gleichung x² + y -z + 5 = 0 beschreibt eine Ebene in 3D.</td><td></td><td>X</td></tr><tr><td>e) Der Abstand eines Punktes von einer Ebene in 3D lässt sich mit Hilfe der Hesse Normalform berechnen.</td><td>X</td><td></td></tr><tr><td>f) Der konstante Term in der Hesse Normalform für eine Ebene in 3D entspricht der Länge des Normalenvektors.</td><td></td><td>X</td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[115, 655, 220, 671]]<|/det|>
2. Ebenen 

<|ref|>text<|/ref|><|det|>[[115, 670, 861, 705]]<|/det|>
a) Bestimmen Sie die Gleichung der Ebene durch die 3 Punkte P₁ = (3;1;0), P₂ = (-4;1;1) und P₃ = (5;9;3). 

<|ref|>text<|/ref|><|det|>[[115, 703, 795, 721]]<|/det|>
b) Bestimmen Sie für die Ebene E: -4x + y - 2z - 3 = 0 eine Parameterform. 

<|ref|>text<|/ref|><|det|>[[115, 720, 830, 771]]<|/det|>
c) Bestimmen Sie eine Parameterform, eine Normalengleichung und die Hesse Normalform für die Ebene, die durch die Punkte (2;1;3), (1;0;2) und (-3;4;-1) verläuft. 

<|ref|>text<|/ref|><|det|>[[115, 788, 145, 804]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[115, 801, 546, 820]]<|/det|>
\[ \vec{r}(P) = \vec{r}(\lambda; \mu) = \vec{r}_1 + \lambda (\vec{r}_2 - \vec{r}_1) + \mu (\vec{r}_3 - \vec{r}_1) = \]

<|ref|>equation<|/ref|><|det|>[[162, 828, 686, 886]]<|/det|>
\[ = \begin{pmatrix} 3 \\ 1 \\ 0 \end{pmatrix} + \lambda \begin{pmatrix} -4 - 3 \\ 1 - 1 \\ 1 - 0 \end{pmatrix} + \mu \begin{pmatrix} 5 - 3 \\ 9 - 1 \\ 3 - 0 \end{pmatrix} = \begin{pmatrix} 3 - 7\lambda + 2\mu \\ 1 \\ \lambda + 3\mu \end{pmatrix} \]