<|ref|>text<|/ref|><|det|>[[30, 15, 299, 45]]<|/det|>
7) a) \(2^4 = 16 \cdot e^{i\pi}\) 

<|ref|>equation<|/ref|><|det|>[[140, 48, 592, 120]]<|/det|>
\[
\begin{align*}
2 &= \sqrt[4]{16} \cdot (e^{i(\pi + 2k\pi)})^{\pi/4} \quad & k \in \mathbb{Z} \\
&= 2 \cdot e^{i(\frac{\pi}{4} + \frac{2k\pi}{4})} \\
&= 2 \cdot e^{i(\frac{\pi}{4} + \pi)} \\
&= 2 \cdot e^{i(\frac{\pi}{4} + 2k\pi)} \\
&= 2 \cdot e^{i(\frac{\pi}{4} + \pi)}
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[140, 123, 660, 175]]<|/det|>
\[
\begin{align*}
z_0 &= 2e^{i\frac{\pi}{4}} = 2(\cos\frac{\pi}{4} + i \cdot \sin\frac{\pi}{4}) = \sqrt{2} + \sqrt{2}i \\
z_1 &= 2e^{i\frac{3\pi}{4}} = 2(\cos(\frac{3\pi}{4}) + i \cdot \sin(\frac{3\pi}{4})) = -\sqrt{2} + \sqrt{2}i \\
z_2 &= 2e^{i\frac{5\pi}{4}} = 2(\cos(\frac{5\pi}{4}) + i \cdot \sin(\frac{5\pi}{4})) = -\sqrt{2} - \sqrt{2}i \\
z_3 &= 2e^{i\frac{7\pi}{4}} = 2(\cos(\frac{7\pi}{4}) + i \cdot \sin(\frac{7\pi}{4})) = \sqrt{2} - \sqrt{2}i
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[80, 321, 856, 366]]<|/det|>
b) \(A = \frac{1}{2} \begin{pmatrix} \sqrt{3} & -1 \\ 1 & \sqrt{3} \end{pmatrix}\) 
Drehmatrix: \(\begin{pmatrix} \cos\alpha & -\sin\alpha \\ \sin\alpha & \cos\alpha \end{pmatrix}\) 

<|ref|>equation<|/ref|><|det|>[[140, 375, 440, 406]]<|/det|>
\[\cos\alpha = \frac{1}{2} \sqrt{3} \quad \alpha = \frac{\pi}{6}\]

<|ref|>equation<|/ref|><|det|>[[140, 412, 440, 444]]<|/det|>
\[-\sin\alpha = -\frac{1}{2} \quad \alpha = \frac{\pi}{6}\]

<|ref|>equation<|/ref|><|det|>[[140 454, 265, 483]]<|/det|>
\[A = R(\frac{\pi}{6})\]

<|ref|>equation<|/ref|><|det|>[[140, 490, 560, 525]]<|/det|>
\[A^{45} = R(\frac{\pi}{6})^{45} = R(15 \cdot \frac{\pi}{6}) = R(\frac{\pi}{2}\pi)\]

<|ref|>equation<|/ref|><|det|>[[140, 530, 650, 580]]<|/det|>
\[= \begin{pmatrix} \cos \frac{5\pi}{2} \pi & -\sin \frac{5\pi}{2} \pi \\ \sin \frac{5\pi}{2} \pi & \cos \frac{5\pi}{2} \pi \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\]

<|ref|>text<|/ref|><|det|>[[80, 603, 631, 640]]<|/det|>
c) \(\int_{0}^{1} \int_{0}^{1} f(x, y) \, dy \, dx = \int_{0}^{1} \int_{0}^{1} f(x, y) \, dx \, dy\) 

<|ref|>equation<|/ref|><|det|>[[140, 640, 720, 765]]<|/det|>
\[
\begin{align*}
y &= \sqrt{x} \quad \Rightarrow \quad y^2 = x \\
y &= \sqrt{x} \quad \Rightarrow \quad y^2 = x \\
y = \sqrt{x} \quad \Rightarrow \quad y^2 = x
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[80, 778, 530, 810]]<|/det|>
d) \(f(x, y) = \frac{1}{2\pi^2} 2^{x-y}\) 

<|ref|>equation<|/ref|><|det|>[[140, 816, 650, 863]]<|/det|>
\[\nabla f(x, y) = \begin{pmatrix} 2^{x-y} \\ -2^{x-y} \end{pmatrix} \quad \nabla f(1; 2) = \begin{pmatrix} \frac{1}{2} \\ -\frac{1}{2} \end{pmatrix}\]

<|ref|>equation<|/ref|><|det|>[[140, 870, 686, 901]]<|/det|>
\[\nabla = (-\frac{3}{4}) \quad |\nabla| = \sqrt{9+16} = 5 \quad \hat{\nabla} = \frac{1}{5} (-\frac{3}{4})\]

<|ref|>equation<|/ref|><|det|>[[140, 907, 625, 940]]<|/det|>
\[\langle \hat{\nabla}, \nabla f(1; 2) \rangle = \frac{1}{5} \langle (-\frac{3}{4}), (\frac{12}{12}) \rangle = -\frac{3}{10}\]