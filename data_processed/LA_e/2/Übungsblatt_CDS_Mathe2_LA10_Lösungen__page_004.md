<|ref|>equation<|/ref|><|det|>[[117, 88, 359, 106]]<|/det|>
\[0 \cdot x + 1 \cdot y = 0 \Rightarrow y = 0\]

<|ref|>equation<|/ref|><|det|>[[117, 111, 359, 130]]<|/det|>
\[1 \cdot x + 0 \cdot y = 0 \Rightarrow x = 0\]

<|ref|>equation<|/ref|><|det|>[[117, 138, 238, 160]]<|/det|>
\[\ker(A) = \{0\}\]

<|ref|>text<|/ref|><|det|>[[115, 162, 386, 181]]<|/det|>
Für das Bild von A ergibt sich 

<|ref|>equation<|/ref|><|det|>[[115, 180, 421, 246]]<|/det|>
\[\operatorname{img}(A) = \operatorname{span} \begin{Bmatrix} 1 \\ -2 \\ 0 \end{Bmatrix}, \begin{Bmatrix} 0 \\ 0 \\ 1 \end{Bmatrix}\]

<|ref|>sub_title<|/ref|><|det|>[[115, 269, 450, 287]]<|/det|>
## 3. Aussagen über 2 Matrizen in 3D 

<|ref|>text<|/ref|><|det|>[[115, 285, 440, 303]]<|/det|>
Gegeben seien die beiden Matrizen 

<|ref|>equation<|/ref|><|det|>[[303, 300, 690, 353]]<|/det|>
\[A = \begin{pmatrix} 0 & 2 & -1 \\ -2 & 0 & -1 \\ 1 & 1 & 0 \end{pmatrix} \text{ und } B = \frac{1}{\sqrt{2}} \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix}.\]

<|ref|>text<|/ref|><|det|>[[115, 348, 680, 366]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[115, 363, 880, 490]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Es gilt: \(\operatorname{img}(A) = \mathbb{R}^3\).</td><td></td><td>X</td></tr><tr><td>b) Es gilt: \(\ker(A^{12}) \neq \{0\}\).</td><td>X</td><td></td></tr><tr><td>c) Es gilt: B ist orthogonal.</td><td></td><td>X</td></tr><tr><td>d) Es gilt: \(\operatorname{tr}(2A + \sqrt{2}B) = 0\).</td><td>X</td><td></td></tr><tr><td>e) Die Spaltenvektoren von B sind linear unabhängig.</td><td>X</td><td></td></tr><tr><td>f) Es gilt: \(\ker(B^3) = \ker(B)\).</td><td>X</td><td></td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[115, 504, 254, 522]]<|/det|>
## 4. Eigenwerte 

<|ref|>text<|/ref|><|det|>[[115, 520, 852, 556]]<|/det|>
A sei eine nxn Matrix. Was lässt sich über die reellen Eigenwerte von A aussagen, falls gilt: 

<|ref|>equation<|/ref|><|det|>[[115, 554, 230, 573]]<|/det|>
a) \(A = -A^T\)

<|ref|>equation<|/ref|><|det|>[[115, 571, 234, 591]]<|/det|>
b) \(A^{-1} = A^T\)

<|ref|>equation<|/ref|><|det|>[[115, 589, 425, 609]]<|/det|>
c) \(A = B^T B\), B sei eine mxn Matrix.

<|ref|>text<|/ref|><|det|>[[115, 625, 144, 641]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[115, 641, 368, 660]]<|/det|>
Es gelten die Umformungen 

<|ref|>equation<|/ref|><|det|>[[275, 679, 707, 721]]<|/det|>
\[\begin{aligned}
\lambda(\mathbf{v}, \mathbf{v}) &= \langle \lambda \mathbf{v}, \mathbf{v} \rangle = \langle A\mathbf{v}, \mathbf{v} \rangle = \langle \mathbf{v}, A^T \mathbf{v} \rangle = \langle \mathbf{v}, -A\mathbf{v} \rangle \\
&= \langle \mathbf{v}, -\lambda \mathbf{v} \rangle = -\lambda \langle \mathbf{v}, -\lambda \mathbf{v} \rangle.
\end{aligned}\]

<|ref|>text<|/ref|><|det|>[[115, 739, 523, 759]]<|/det|>
Diese Gleichungskette ist nur für \(\lambda = 0\) richtig. 

<|ref|>text<|/ref|><|det|>[[115, 758, 147, 776]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[115, 775, 865, 814]]<|/det|>
Hier liegt eine orthogonale Matrix vor mit den bekannten Eigenschaften \(A^{-1} = A^T\) und damit \(A^T A = E\). Daraus ermitteln wir 

<|ref|>equation<|/ref|><|det|>[[260, 833, 715, 856]]<|/det|>
\[\lambda^2(\mathbf{v}, \mathbf{v}) = \langle \lambda \mathbf{v}, \lambda \mathbf{v} \rangle = \langle A\mathbf{v}, A\mathbf{v} \rangle = \langle A^T A\mathbf{v}, \mathbf{v} \rangle = \langle \mathbf{v}, \mathbf{v} \rangle.\]

<|ref|>text<|/ref|><|det|>[[115, 856, 576, 876]]<|/det|>
Diese Gleichungskette ist für \(\lambda = 0\) und \(\lambda = 1\) gültig.