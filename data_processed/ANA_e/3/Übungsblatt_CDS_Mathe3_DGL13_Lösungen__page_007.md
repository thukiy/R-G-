<|ref|>sub_title<|/ref|><|det|>[[115, 81, 350, 100]]<|/det|>
## 2. Helmholtz-Gleichung 

<|ref|>text<|/ref|><|det|>[[115, 99, 844, 160]]<|/det|>
a) Zeigen Sie, dass die Wellengleichung \(u_{tt} = \Delta u\) mit \(x \in \mathbb{R}^2\), \(t \in \mathbb{R}\) mithilfe des Separationsansatzes \(u(x, t) = e^{ikt} U(x)\) auf die Helmholtz-Gleichung \(\Delta U + k^2 U = 0\) führt. 

<|ref|>text<|/ref|><|det|>[[115, 158, 570, 178]]<|/det|>
b) Finden Sie Lösungen zur Helmholtz-Gleichung 

<|ref|>equation<|/ref|><|det|>[[144, 176, 477, 213]]<|/det|>
\[ \Delta u + k^2 u = \frac{\partial^2 u}{\partial x_1^2} + \frac{\partial^2 u}{\partial x_2^2} + k^2 u = 0 \]

<|ref|>text<|/ref|><|det|>[[144, 211, 390, 229]]<|/det|>
mit den Randbedingungen 

<|ref|>equation<|/ref|><|det|>[[144, 227, 600, 248]]<|/det|>
\[ u(x_1, 0) = u(x_1, b) = u(0, x_2) = u(a, x_2) = 0 \]

<|ref|>text<|/ref|><|det|>[[144, 245, 872, 285]]<|/det|>
für \(0 < a, b \in \mathbb{R}\), indem Sie \(k^2 = k_{x_1}^2 + k_{x_2}^2\) setzen und einen Separationsansatz benutzen. 

<|ref|>sub_title<|/ref|><|det|>[[247, 304, 395, 323]]<|/det|>
### (a) Der Ansatz 

<|ref|>equation<|/ref|><|det|>[[324, 341, 520, 364]]<|/det|>
\[ u(x, t) = e^{ik t} U(x) \]

<|ref|>text<|/ref|><|det|>[[124, 379, 191, 399]]<|/det|>
liefert 

<|ref|>equation<|/ref|><|det|>[[176, 414, 666, 492]]<|/det|>
\[ \begin{aligned} u_{tt} &= (ik)^2 \exp(ik t) U(x) = -k^2 \exp(ik t) U(x), \\ u_{x_j x_j} &= \exp(ik t) \frac{\partial^2 U(x)}{\partial x_j^2}, \quad j = 1, 2. \end{aligned} \]

<|ref|>text<|/ref|><|det|>[[124, 504, 491, 525]]<|/det|>
Somit folgt aus \(u_{tt} = \Delta u\) die Identität 

<|ref|>equation<|/ref|><|det|>[[194, 540, 646, 563]]<|/det|>
\[ -k^2 \exp(ik t) U(x) = \exp(ik t)(U_{x_1 x_1} + U_{x_2 x_2}), \]

<|ref|>text<|/ref|><|det|>[[124, 579, 686, 601]]<|/det|>
d. h., es gilt die Helmholtz-Gleichung \(-k^2 U(x) = \Delta U(x)\).