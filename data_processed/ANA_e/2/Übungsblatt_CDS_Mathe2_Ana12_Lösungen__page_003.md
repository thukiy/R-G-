<|ref|>text<|/ref|><|det|>[[119, 90, 780, 115]]<|/det|>
Analog: \((\text{rot } \vec{F})_y = (\text{rot } \vec{F})_z = 0\) (alle Ableitungen mit der Kettenregel) 

<|ref|>text<|/ref|><|det|>[[119, 123, 480, 147]]<|/det|>
Somit: \(\text{rot } \vec{F} = \vec{0} \Rightarrow \vec{F}\) ist wirbelfrei. 

<|ref|>sub_title<|/ref|><|det|>[[114, 159, 380, 178]]<|/det|>
## 3. Potentialfeld bestimmen 

<|ref|>text<|/ref|><|det|>[[114, 180, 835, 235]]<|/det|>
Zeigen Sie, dass das räumliche Vektorfeld \(\vec{F}(x, y, z) = \begin{pmatrix} 2xz + y^2 \\ 2xy \\ x^2 \end{pmatrix}\) wirbelfrei und somit als Gradient eines skalaren Feldes \(\phi(x, y, z)\) darstellbar ist. Bestimmen Sie dieses Potentialfeld. 

<|ref|>equation<|/ref|><|det|>[[114, 288, 511, 308]]<|/det|>
\[F_x = 2xz + y^2; \quad F_y = 2xy; \quad F_z = x^2\]

<|ref|>equation<|/ref|><|det|>[[114, 316, 730, 430]]<|/det|>
\[ \begin{aligned} (\text{rot } \vec{F})_x &= \frac{\partial F_z}{\partial y} - \frac{\partial F_y}{\partial z} = 0 - 0 = 0 \\ (\text{rot } \vec{F})_y &= \frac{\partial F_x}{\partial z} - \frac{\partial F_z}{\partial x} = 2x - 2x = 0 \\ (\text{rot } \vec{F})_z &= \frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y} = 2y - 2y = 0 \end{aligned} \quad \Rightarrow \quad \text{rot } \vec{F} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} = \vec{0} \]

<|ref|>text<|/ref|><|det|>[[114, 439, 875, 476]]<|/det|>
\(\vec{F}\) ist somit wirbelfrei. Die Vektorkomponenten von \(\vec{F}\) sind demnach die partiellen Ableitungen 1. Ordnung eines (noch unbekannten) Skalarfeldes \(\phi = \phi(x; y; z)\): 

<|ref|>equation<|/ref|><|det|>[[114, 486, 688, 560]]<|/det|>
\[ \frac{\partial \phi}{\partial x} = F_x = 2xz + y^2; \quad \frac{\partial \phi}{\partial y} = F_y = 2xy; \quad \frac{\partial \phi}{\partial z} = F_z = x^2 \]

<|ref|>equation<|/ref|><|det|>[[114, 528, 620, 562]]<|/det|>
\[ \phi = \int \frac{\partial \phi}{\partial x} dx = \int (2xz + y^2) dx = x^2z + xy^2 + K(y; z) \]

<|ref|>text<|/ref|><|det|>[[114, 565, 875, 600]]<|/det|>
Die Integrationskonstante \(K\) kann noch von \(y\) und \(z\) abhängen: \(K = K(y; z)\). Sie wird aus den bekannten partiellen Ableitungen von \(\phi\) nach \(y\) bzw. \(z\) wie folgt bestimmt: 

<|ref|>equation<|/ref|><|det|>[[114, 604, 775, 641]]<|/det|>
\[ \frac{\partial \phi}{\partial y} = \frac{\partial}{\partial y} (x^2z + xy^2 + K(y; z)) = 2xy + \frac{\partial K}{\partial y} = 2xy \Rightarrow \frac{\partial K}{\partial y} = 0 \Rightarrow K \text{ ist unabhängig von } y, \text{ kann aber noch von } z \text{ abhängen: } K = K_1(z) \]

<|ref|>text<|/ref|><|det|>[[114, 666, 500, 684]]<|/det|>
Zwischenergebnis: \(\phi = x^2z + xy^2 + K_1(z)\) 

<|ref|>equation<|/ref|><|det|>[[114, 694, 785, 732]]<|/det|>
\[ \frac{\partial \phi}{\partial z} = \frac{\partial}{\partial z} (x^2z + xy^2 + K_1(z)) = x^2 + K_1'(z) = x^2 \Rightarrow K_1'(z) = 0 \Rightarrow K_1(z) = \text{const.} = C \]

<|ref|>equation<|/ref|><|det|>[[114, 741, 350, 760]]<|/det|>
\[ K_1(z) = \text{const.} = C \]

<|ref|>equation<|/ref|>math<|/ref|><|det|>[[114, 772, 640, 794]]<|/det|>
\[ \text{Lösung: } \phi = \phi(x; y; z) = x^2z + xy^2 + C \quad (\text{mit } C \in \mathbb{R}) \]