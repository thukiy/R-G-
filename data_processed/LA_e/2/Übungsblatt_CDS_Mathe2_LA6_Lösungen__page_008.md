<|ref|>equation<|/ref|><|det|>[[117, 80, 839, 345]]<|/det|>
\[
\begin{align*}
R(2\pi/3) &= \begin{bmatrix} \cos(2\pi/3) & -\sin(2\pi/3) \\ \sin(2\pi/3) & \cos(2\pi/3) \end{bmatrix} = \begin{bmatrix} -\frac{1}{2} & -\frac{\sqrt{3}}{2} \\ \frac{\sqrt{3}}{2} & -\frac{1}{2} \end{bmatrix} = \frac{1}{2} \begin{bmatrix} -1 & -\sqrt{3} \\ \sqrt{3} & -1 \end{bmatrix} \\
\mathbf{v} &= R(2\pi/3) \cdot \mathbf{u} = \frac{1}{2} \cdot \begin{bmatrix} -1 & -\sqrt{3} \\ \sqrt{3} & 1 \end{bmatrix} \cdot \begin{bmatrix} 0 \\ 3 \end{bmatrix} = \frac{1}{2} \cdot \begin{bmatrix} (-1) \cdot 0 + (-\sqrt{3}) \cdot 3 \\ \sqrt{3} \cdot 0 + (-1) \cdot 3 \end{bmatrix} \\
&= \frac{3}{2} \cdot \begin{bmatrix} -\sqrt{3} \\ -1 \end{bmatrix}
\end{align*}
\quad
\begin{align*}
\mathbf{w} &= S_y \cdot \mathbf{v} = \frac{3}{2} \cdot \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix} \cdot \begin{bmatrix} -\sqrt{3} \\ -1 \end{bmatrix} = \frac{3}{2} \cdot \begin{bmatrix} (-1) \cdot (-\sqrt{3}) + 0 \cdot (-1) \\ 0 \cdot (-\sqrt{3}) + 1 \cdot (-1) \end{bmatrix} \\
&= \frac{3}{2} \cdot \begin{bmatrix} \sqrt{3} \\ -1 \end{bmatrix}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 347, 583, 365]]<|/det|>
Für die beiden anderen Eckpunkte ergibt sich somit 

<|ref|>equation<|/ref|><|det|>[[115, 364, 603, 476]]<|/det|>
\[
\begin{align*}
\mathbf{B} &= \mathbf{M} + \mathbf{v} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} + \frac{3}{2} \cdot \begin{bmatrix} -\sqrt{3} \\ 1 \end{bmatrix} = \frac{3}{2} \cdot \begin{bmatrix} -\sqrt{3} \\ \sqrt{3} \end{bmatrix} \\
\mathbf{C} &= \mathbf{M} + \mathbf{w} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} + \frac{2}{3} \cdot \begin{bmatrix} \sqrt{3} \\ 1 \end{bmatrix} = \frac{3}{2} \\
\mathbf{A} &= \begin{bmatrix} \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{bmatrix}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 490, 500, 507]]<|/det|>
5. Aussagen über eine Drehmatrix in 2D 

<|ref|>text<|/ref|><|det|>[[115, 506, 375, 523]]<|/det|>
Gegeben sei die Drehmatrix 

<|ref|>equation<|/ref|><|det|>[[414, 522, 583, 605]]<|/det|>
\[
A = \begin{pmatrix} \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}\\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \end{pmatrix}
\]

<|ref|>text<|/ref|><|det|>[[115, 613, 680, 630]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[115, 628, 880, 768]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) A ist schiefsymmetrisch.</td><td></td><td>X</td></tr><tr><td>b) Es gilt: \(A^{100} = \mathbb{E}\).</td><td></td><td>X</td></tr><tr><td>c) Es gilt: \(A^6 = R(-\frac{\pi}{2})\).</td><td>X</td><td></td></tr><tr><td>d) Es gibt ein \(n \in \mathbb{N}\) so dass gilt: \(A^n = P\).</td><td>X</td><td></td></tr><tr><td>e) Die inverse Matrix \(A^{-1}\) von \(A\) ist \(A^T\).</td><td>X</td><td></td></tr><tr><td>f) Es gilt: \(A = \frac{1}{\sqrt{2}} \cdot \mathbb{E} + \frac{1}{\sqrt{2}} \cdot R(\frac{\pi}{2})\).</td><td>X</td><td></td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[115, 782, 456, 799]]<|/det|>
6. Gleichschenkliges Dreieck in 2D 

<|ref|>text<|/ref|><|det|>[[115, 798, 856, 850]]<|/det|>
Gegeben sei ein gleichschenkliges Dreieck mit den Eckpunkten B = (2;1/4) und
C = (2;4), das die Gerade G, die durch den Ursprung und den Punkt C verläuft, als
Symmetrieachse hat. 

<|ref|>text<|/ref|><|det|>[[115, 849, 757, 867]]<|/det|>
a) Bestimmen Sie die Ecke A des Dreiecks durch Drehung der Seite a. 

<|ref|>text<|/ref|><|det|>[[115, 866, 851, 899]]<|/det|>
b) Bestimmen Sie die Ecke A durch Spiegelung an der Symmetrieachse, also der
Geraden G.