<|ref|>title<|/ref|><|det|>[[115, 165, 510, 201]]<|/det|>
# Übungsblatt DGL 12 

<|ref|>text<|/ref|><|det|>[[576, 179, 880, 196]]<|/det|>
Computational and Data Science 

<|ref|>text<|/ref|><|det|>[[755, 199, 880, 215]]<|/det|>
BSc HS2024 

<|ref|>text<|/ref|><|det|>[[115, 232, 270, 260]]<|/det|>
## Lösungen 

<|ref|>text<|/ref|><|det|>[[750, 240, 880, 257]]<|/det|>
Mathematik 3 

<|ref|>text<|/ref|><|det|>[[115, 287, 210, 304]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 303, 822, 339]]<|/det|>
- Sie kennen die Definitionen von Operatoren der Vektoranalysis (Nabla- und Laplace-Operator, Divergenz, Rotation) und können diese anwenden. 

<|ref|>text<|/ref|><|det|>[[115, 337, 857, 371]]<|/det|>
- Sie kennen die Begriffe Ordnung, Linearität, Homogenität und Typ in Bezug auf eine PDGL und können diese für konkrete PDGLs anwenden. 

<|ref|>text<|/ref|><|det|>[[115, 370, 840, 404]]<|/det|>
- Sie können bestimmen, ob eine vorgegebene Funktion eine mögliche Lösung einer gegebenen PDGL darstellt. 

<|ref|>text<|/ref|><|det|>[[115, 403, 864, 453]]<|/det|>
- Sie kennen die Methode der Modellierung, um einen physikalischen/technischen Sachverhalt in ein mathematisches Problem zu übersetzen, was oftmals auf das Lösen partieller Differentialgleichungen hinausläuft. 

<|ref|>sub_title<|/ref|><|det|>[[115, 484, 380, 501]]<|/det|>
### 1. Rechnen mit Operatoren 

<|ref|>text<|/ref|><|det|>[[115, 501, 312, 518]]<|/det|>
Verifizieren Sie, dass 

<|ref|>text<|/ref|><|det|>[[115, 517, 515, 555]]<|/det|>
a) \((\vec{u}, \nabla_x) \vec{u}\) durch \((\sum_{i=1}^{3} u_i \frac{\partial u_j}{\partial x_i})_{j=1\dots 3}\) und 

<|ref|>text<|/ref|><|det|>[[115, 555, 375, 660]]<|/det|>
b) \(\Delta_x \vec{u}\) durch
\[\begin{cases}
\sum_{i=1}^{3} \frac{\partial^2 u_1}{\partial x_i^2} \\
\sum_{i=1}^{3} \frac{\partial^2 u_2}{\partial x_i^2} \\
\sum_{i=1}^{3} \frac{\parti^2 u_3}{\partial x_i^2}
\end{cases}\]

<|ref|>text<|/ref|><|det|>[[115, 660, 583, 682]]<|/det|>
dargestellt werden können, wobei gilt: \(\vec{u}: \mathbb{R}^3 \to \mathbb{R}^3\). 

<|ref|>text<|/ref|><|det|>[[115, 679, 810, 702]]<|/det|>
Hinweis für b): da \(\vec{u}\) ein Vektorfeld ist, gilt: \(\text{rot}(\text{rot} \vec{u}) = \text{grad}(\text{div} \vec{u}) - \Delta \vec{u}\).