<|ref|>equation<|/ref|><|det|>[[150, 12, 950, 150]]<|/det|>
\[
\begin{align*}
\int 2x \cdot \sin x \, dx &= 2x, \quad v'(x) = 2, \quad u'(x) = \sin x, \quad u(x) = -\cos x \\
&= 2x \cdot (-\cos x) - \int 2 \cdot (-\cos x) \, dx \\
&= -2x \cdot \cos x + \int 2 \cdot \cos x \, dx \\
&= -2x \cdot \cos x + 2 \cdot \sin x + c
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[142, 186, 720, 255]]<|/det|>
\[
\begin{align*}
\int x^2 \cdot \cos x \, dx &= x^2 \cdot \sin x - (-2x \cos x + 2 \sin x + c) \\
&= x^2 \cdot \sin x + 2x \cos x - 2 \sin x + c_1
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[120, 281, 920, 530]]<|/det|>
\[
\begin{align*}
\int \sin^2 x \, dx &= \int \sin x \cdot \sin x \, dx \quad \forall (x) = \sin x, \quad v'(x) = \cos x \\
&= \sin x \cdot (-\cos x) - \int \cos x \cdot (-\cos x) \, dx \\
&= -\sin x \cdot \cos x - \int \cos^2 x \, dx \\
&= -\sin x \cdot \cos x - \int 1 \, dx - \int \sin^2 x \, dx \\
&= -\sin x \cdot \cos x - \int 2 \cdot \sin x \cdot \cos x + \int 1 \, dx \\
&= -\sin x \cdot \cos x + x + c \\
\int \sin^2 x \, dx &= -\sin x \cdot \cos x + c_1
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[175, 556, 636, 590]]<|/det|>
\[
\int \sin^2 x \, dx = \frac{1}{2}x - \frac{1}{2} \sin x \cdot \cos x + c_1
\]

<|ref|>equation<|/ref|><|det|>[[120, 615, 600, 648]]<|/det|>
\[
\int \sqrt{a^2 - x^2} \, dx \quad a^2 - x^2 \geq 0
\]

<|ref|>equation<|/ref|><|det|>[[160, 656, 310, 680]]<|/det|>
\[
x = a \cdot \sin z
\]

<|ref|>equation<|/ref|><|det|>[[160, 688, 636, 722]]<|/det|>
\[
\frac{dx}{dz} = a \cdot \cos z \quad \iff \quad dx = a \cdot \cos z \, dz
\]

<|ref|>equation<|/ref|><|det|>[[160, 730, 490, 755]]<|/det|>
\[
\int \sqrt{a^2 - (a \cdot \sin z)^2} \, a \cdot \cos z \, dz
\]

<|ref|>equation<|/ref|><|det|>[[160, 765, 880, 810]]<|/det|>
\[
= \int \sqrt{a^2 - a^2 \cdot \sin^2 z} \, a \cdot \cos z \, dz = \int a \cdot \sqrt{1 - \sin^2 z} \, a \cdot \cos z \, dz
\]

<|ref|>equation<|/ref|><|det|>[[160, -1, 999, 100]]<|/det|>
\[
= a^2 \cdot \int 1 \, dz - a^2 \cdot \int \sin^2 dz = a^2 z - a^2 \left( \frac{1}{2} z - \frac{1}{2} \sin z \cos z \right) + c
\]

<|ref|>equation<|/ref|><|det|>[[160, 856, 999, 890]]<|/det|>
\[
= a^2 \cdot z - \frac{1}{2} a^2 z + \frac{1}{2} a^2 \sin (z) \cos (z) + c
\]

<|ref|>equation<|/ref|><|det|>[[160, 899, 999, 933]]<|/det|>
\[
= \frac{1}{2} a^2 z + \frac{1}{2} \cdot \frac{1}{2} a^2 \sin z \cos z + c = \frac{1}{2} a^2 z + \frac{1}{2} z \cdot \frac{1}{2} a^2 \sin z \cdot \sqrt{1 - \sin^2 z} + c
\]