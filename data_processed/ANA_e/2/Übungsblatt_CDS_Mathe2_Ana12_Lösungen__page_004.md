<|ref|>sub_title<|/ref|><|det|>[[114, 81, 430, 100]]<|/det|>
## 4. Aussagen über ein Vektorfeld 

<|ref|>text<|/ref|><|det|>[[114, 99, 372, 116]]<|/det|>
Gegeben sei das Vektorfeld 

<|ref|>equation<|/ref|><|det|>[[114, 114, 211, 164]]<|/det|>
\[ \vec{v} = \begin{pmatrix} 1 \\ 1 \\ xy \end{pmatrix}. \]

<|ref|>text<|/ref|><|det|>[[114, 164, 681, 182]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[114, 180, 880, 271]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) \(\vec{v}\) ist konservativ.</td><td></td><td>X</td></tr><tr><td>b) \(\vec{v}\) ist quellenfrei.</td><td>X</td><td></td></tr><tr><td>c) \(\vec{v}\) ist wirbelfrei.</td><td></td><td>X</td></tr><tr><td>d) Es gibt ein Skalarfeld \(\phi\), so dass \(\vec{v} = \nabla\phi\).</td><td></td><td>X</td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[114, 284, 315, 301]]<|/det|>
## 5. Laplace-Operator 

<|ref|>text<|/ref|><|det|>[[114, 300, 844, 336]]<|/det|>
Welche Funktion erhält man, wenn man den Laplace-Operator auf das Skalarfeld \(\phi(x, y, z) = (x^2 + y^2 + z^2)^2\) anwendet? 

<|ref|>equation<|/ref|><|det|>[[120, 352, 833, 392]]<|/det|>
\[ \frac{\partial \phi}{\partial x} = 4x(x^2 + y^2 + z^2); \quad \frac{\partial^2 \phi}{\partial x^2} = 4(3x^2 + y^2 + z^2) \quad (\text{Produkt- und Kettenregel}) \]

<|ref|>equation<|/ref|><|det|>[[120, 395, 668, 433]]<|/det|>
\[ \text{Analog: } \frac{\partial^2 \phi}{\partial y^2} = 4(x^2 + 3y^2 + z^2); \quad \frac{\partial^2 \phi}{\partial z^2} = 4(x^2 + y^2 + 3z^2) \]

<|ref|>equation<|/ref|><|det|>[[120, 443, 880, 520]]<|/det|>
\[ \begin{aligned} \Delta \phi &= \frac{\partial^2 \phi}{\partial x^2} + \frac{\partial^2 \phi}{\partial y^2} + \frac{\partial^2 \phi}{\partial z^2} \\ &= 4(3x^2 + y^2 + z^2) + 4(x^2 + 3y^2 + z^2) + 4(x^2 + y^2 + 3z^2) \\ &= 4(5x^2 + 5y^2 + 5z^2) = 20(x^2 + y^2 + z^2) = 20r^2 \end{aligned} \]