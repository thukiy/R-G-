<|ref|>text<|/ref|><|det|>[[115, 81, 300, 100]]<|/det|>
Allgemeine Lösung: 

<|ref|>equation<|/ref|><|det|>[[119, 99, 868, 162]]<|/det|>
\[
\begin{align*}
y(x) &= C_1 \cdot y_1(x) + C_2 \cdot y_2(x) = C_1 \cdot \mathrm{e}^{-2x-4ix} + C_2 \cdot \mathrm{e}^{-2x+4ix} \\
&= \frac{\mathrm{e}^{-2x}(C_1 \mathrm{e}^{-4ix} + C_2 \mathrm{e}^{+4ix})}{\mathrm{e}^{-2x}} = \frac{\mathrm{e}^{-2x}(C \cos(4x) + S \sin(4x))}{\mathrm{e}^{-2x}} = A \frac{\mathrm{e}^{-2x} \sin(4x + \varphi_0)}{\mathrm{e}^{-2x}}.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 180, 147, 198]]<|/det|>
d) 

<|ref|>text<|/ref|><|det|>[[115, 196, 644, 214]]<|/det|>
Das charakteristische Polynom ist die quadratische Funktion 

<|ref|>equation<|/ref|><|det|>[[115, 220, 312, 240]]<|/det|>
\[
p(\lambda) = \lambda^2 + 10\lambda + 25
\]

<|ref|>text<|/ref|><|det|>[[115, 247, 288, 265]]<|/det|>
mit Diskriminante 

<|ref|>equation<|/ref|><|det|>[[115, 271, 562, 290]]<|/det|>
\[
D = b^2 - 4 \cdot a \cdot c = 10^2 - 4 \cdot 1 \cdot 25 = 100 - 100 = 0.
\]

<|ref|>text<|/ref|><|det|>[[115, 289, 608, 307]]<|/det|>
Charakteristisches Polynom hat folglich eine Nullstelle: 

<|ref|>equation<|/ref|><|det|>[[119, 305, 411, 340]]<|/det|>
\[
\lambda = \lambda_s = -\frac{b}{2 \cdot a} = -\frac{10}{2 \cdot 1} = -5.
\]

<|ref|>text<|/ref|><|det|>[[115, 338, 505, 356]]<|/det|>
Es ergeben sich die reellen Basislösungen: 

<|ref|>equation<|/ref|><|det|>[[119, 355, 642, 377]]<|/det|>
\[
y_1(x) = \mathrm{e}^{\lambda x} = \mathrm{e}^{-5x} \quad \text{und} \quad y_2(x) = x \cdot \mathrm{e}^{\lambda x} = x \cdot \mathrm{e}^{-5x}.
\]

<|ref|>text<|/ref|><|det|>[[115, 376, 300, 395]]<|/det|>
Allgemeine Lösung: 

<|ref|>equation<|/ref|><|det|>[[119, 394, 848, 425]]<|/det|>
\[
\frac{y(x)}{D} = C_1 \cdot y_1(x) + C_2 \cdot y_2 (x) = C_1 \cdot \mathrm{e}^{-5x} + C_2 \cdot x \cdot \mathrm{e}^{-5x} = \left( C_1 + C_2 x \right) \mathrm{e}^{-5x}.
\]

<|ref|>text<|/ref|><|det|>[[115, 440, 147, 458]]<|/det|>
e) 

<|ref|>text<|/ref|><|det|>[[115, 456, 673, 475]]<|/det|>
Das charakteristische Polynom ist die quadratische Funktion 

<|ref|>equation<|/ref|><|det|> [[115, 481, 310, 502]]<|/det|>
\[
p(\lambda) = \lambda^2 - 2\lambda + 10
\]

<|ref|>text<|/ref|><|det|>[[115, 510, 293, 528]]<|/det|>
mit Diskriminante 

<|ref|>equation<|/ref|><|det|>[[115, 534, 645, 554]]<|/det|>
\[
D = b^2 - 4 \cdot a \cdot c \cdot (-2)^2 - 4 \cdot 1 \cdot 10 = 4 - 40 = -36 < 0.
\]

<|ref|>text<|/ref|><|det|>[[115, 552, 616, 571]]<|/det|>
Charakteristisches Polynom hat 2 komplexe Nullstellen: 

<|ref|>equation<|/ref|><|det|>[[119, 570, 530, 640]]<|/det|>
\[
\begin{align*}
\lambda_{1,2} &= \frac{-b \pm \sqrt{D}}{2 \cdot a} = \frac{+2 \pm \sqrt{-36}}{2 \cdot 1} = \frac{2 \pm 6i}{2} \\
\lambda_1 &= \frac{2 - 6i}{2} = 1 - 3i \quad \text{und} \quad \lambda_2 = \frac{2 + 6i}{2} = 1 + 3i
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 640, 543, 658]]<|/det|>
Es ergeben sich die komplexen Basislösungen: 

<|ref|>equation<|/ref|><|det|>[[119, 657, 688, 686]]<|/det|>
\[
y_1(x) = \mathrm{e}^{\lambda_1 x} = \mathrm{e}^{x-3ix} \quad \text{und} \quad y_2(x) = \mathrm{e}^{\lambda_2 x} = \mathrm{e}^{x+3ix}.
\]

<|ref|>text<|/ref|><|det|>[[115, 688, 300, 706]]<|/det|>
Allgemeine Lösung: 

<|ref|>equation<|/ref|><|det|>[[119, 704, 630, 728]]<|/det|>
\[
\frac{y(x)}{D} = C_1 \cdot y_2(x) + C_2 \cdot y_2(x) = C_1 \cdot e^{x-3ix} + C_2 \cdot e^{x+3ix}
\]

<|ref|>equation<|/ref|><|det|>[[162, 741, 863, 772]]<|/det|>
\[
= \mathrm{e}^{x} \left( C_1 \mathrm{e}^{-3ix} + C_2 \mathrm{e}^{+3ix} \right) = \mathrm{e}^{x} \left( C \cos(3x) + S \sin(3x) \right) = A \mathrm{e}^{x} \sin(3x + \varphi_0).
\]

<|ref|>text<|/ref|><|det|>[[115, 792, 147, 809]]<|/det|>
f) 

<|ref|>text<|/ref|><|det|>[[115, 808, 644, 826]]<|/det|>
Das charakteristische Polynom ist die quadratische Funktion 

<|ref|>equation<|/ref|><|det|>[115, 837, 301, 857]]<|/det|>
\[
p(\lambda) = 2\lambda^2 + 7\lambda + 3
\]

<|ref|>text<|/ref|><|det|>[[115, 867, 285, 885]]<|/det|>
mit Diskriminante 

<|ref|>equation<|/ref|><|det|>[[115, 894, 570, 914]]<|/det|>
\[
D = b^2 - 4 \cdot a \cdot c + 7^2 - 4 \cdot 2 \cdot 3 = 49 - 24 = 25 > 0.
\]