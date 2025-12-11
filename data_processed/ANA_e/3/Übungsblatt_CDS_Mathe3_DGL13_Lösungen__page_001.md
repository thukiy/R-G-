<|ref|>title<|/ref|><|det|>[[115, 165, 510, 201]]<|/det|>
# Übungsblatt DGL 13 

<|ref|>text<|/ref|><|det|>[[576, 179, 880, 196]]<|/det|>
Computational and Data Science 

<|ref|>text<|/ref|><|det|>[[755, 199, 880, 215]]<|/det|>
BSc HS2024 

<|ref|>text<|/ref|><|det|>[[115, 232, 270, 260]]<|/det|>
## Lösungen 

<|ref|>text<|/ref|><|det|>[[750, 240, 880, 257]]<|/det|>
Mathematik 3 

<|ref|>text<|/ref|><|det|>[[115, 286, 210, 303]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 303, 866, 338]]<|/det|>
- Sie kennen den Begriff des Separationsansatzes und können diesen zur Lösung von PDGLs einsetzen. 

<|ref|>text<|/ref|><|det|>[[115, 337, 870, 371]]<|/det|>
- Sie kennen die Methode von d'Alembert zur Lösung von bestimmten PDGLs und können diese für die Wellengleichung anwenden. 

<|ref|>text<|/ref|><|det|>[[115, 370, 860, 404]]<|/det|>
- Sie kenne die Methode der Charakteristiken zur Lösung von PDGLs 1. Ordnung und können diese anwenden. 

<|ref|>sub_title<|/ref|><|det|>[[115, 435, 425, 453]]<|/det|>
### 1. Lösen der Laplace-Gleichung 

<|ref|>text<|/ref|><|det|>[[115, 452, 416, 470]]<|/det|>
Lösen Sie die Laplace-Gleichung 

<|ref|>equation<|/ref|><|det|>[[310, 468, 685, 490]]<|/det|>
\[ \Delta u(x, y) = u_{xx}(x, y) + u_{yy}(x, y) = 0 \]

<|ref|>text<|/ref|><|det|>[[115, 489, 358, 507]]<|/det|>
mit den Randbedingungen 

<|ref|>equation<|/ref|><|det|>[[115, 505, 841, 549]]<|/det|>
\[ \begin{aligned} u_y(x, 0) &= 0, \\ u(x, 1) &= \sin(3\pi x) \cosh(3\pi) - 2 \sin(\pi x) \text{ für } x \in [0,1] \text{ sowie } \\ u(0, y) &= u(1, y) = 0 \text{ für } y \in [0,1] \end{aligned} \]

<|ref|>text<|/ref|><|det|>[[115, 547, 440, 565]]<|/det|>
mithilfe eines Separationsansatzes. 

<|ref|>equation<|/ref|><|det|>[[120, 585, 685, 622]]<|/det|>
\[ V(x)W(y) \text{ führt auf} \quad \text{Der Separationsansatz der Form } u(x, y) = V(x)W(y) \text{ führt auf} \]

<|ref|>equation<|/ref|><|det|>[[120, 636, 685, 679]]<|/det|>
\[ V''(x)W(y) + V(x)W''(y) = 0 \quad \text{bzw.} \quad \frac{V''(x)}{V(x)} = -\frac{W''(y)}{W(y)}, \]

<|ref|>text<|/ref|><|det|>[[120, 694, 686, 750]]<|/det|>
wenn \(V(x) \neq 0\) und \(W(y) \neq 0\) sind. Es folgt, dass diese Identität nur erfüllt werden kann, wenn beide Seiten konstant sind. Damit ergeben sich die gewöhnlichen Differenzialgleichungen 

<|ref|>equation<|/ref|><|det|>[[200, 766, 606, 788]]<|/det|>
\[ V''(x) = kV(x) \quad \text{und} \quad W''(y) = -kW(y) \]

<|ref|>text<|/ref|><|det|>[[120, 805, 400, 824]]<|/det|>
mit den allgemeinen Lösungen 

<|ref|>equation<|/ref|><|det|>[[200, 840, 606, 864]]<|/det|>
\[ V(x) = a_1 \exp(\sqrt{k}x) + a_2 \exp(-\sqrt{k}x), \]

<|ref|>equation<|/ref|><|det|>[[200, 868, 606, 892]]<|/det|>
\[ W(y) = a_3 \exp(\sqrt{-k}y) + a_4 \exp(-\sqrt{-k}y). \]