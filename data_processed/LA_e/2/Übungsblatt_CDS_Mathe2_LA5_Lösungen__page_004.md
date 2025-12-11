<|ref|>text<|/ref|><|det|>[[115, 83, 144, 100]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[115, 98, 546, 115]]<|/det|>
Das lineare Gleichungssystem lautet als Matrizenprodukt 

<|ref|>equation<|/ref|><|det|>[[172, 123, 525, 200]]<|/det|>
\[ \begin{pmatrix} 1 & 3 & 2 \\ -2 & -4 & -3 \\ 3 & 8 & 5 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 1 \\ -3 \\ 2 \end{pmatrix}. \]

<|ref|>text<|/ref|><|det|>[[115, 210, 612, 227]]<|/det|>
Die Berechnung der Inversen \(A^{-1}\) mittels Gauß-Elimination ergibt 

<|ref|>equation<|/ref|><|det|>[[172, 236, 410, 290]]<|/det|>
\[ A^{-1} = \begin{pmatrix} -4 & -1 & 1 \\ -1 & 1 & 1 \\ 4 & -1 & -2 \end{pmatrix}. \]

<|ref|>text<|/ref|><|det|>[[115, 299, 543, 316]]<|/det|>
Damit lautet die Lösung des linearen Gleichungssystems 

<|ref|>equation<|/ref|><|det|>[[172, 325, 630, 377]]<|/det|>
\[ \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} \begin{pmatrix} -4 & -1 & 1 \\ -1 & 1 & -1 \\ 4 & -1 & -2 \end{pmatrix} \begin{pmatrix} 1 \\ -3 \\ 2 \end{pmatrix} = \begin{pmatrix} 1 \\ -2 \\ 3 \end{pmatrix}. \]

<|ref|>text<|/ref|><|det|>[[115, 377, 147, 395]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[115, 395, 870, 450]]<|/det|>
Die rechten Seiten \(\vec{b}_i\) sind die Einheitsvektoren und die Vektoren \(\vec{x}_k\) sind demnach Lösungen der linearen Gleichungssysteme \(A \cdot \vec{x}_k = \vec{e}_k\). Die rechte Seite im LGS, das zu lösen ist, kann mit den Einheitsvektoren in der Form 

<|ref|>equation<|/ref|><|det|>[[115, 448, 586, 507]]<|/det|>
\[ \begin{pmatrix} 2 \\ 3 \\ -5 \end{pmatrix} = 2 \cdot \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} + 3 \cdot \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} - 5 \cdot \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} = 2 \cdot \vec{e}_1 + 3 \cdot \vec{e}_2 - 5 \cdot \vec{e}_3 \]

<|ref|>text<|/ref|><|det|>[[115, 507, 338, 524]]<|/det|>
dargestellt werden. D. h. 

<|ref|>equation<|/ref|><|det|>[[115, 522, 383, 580]]<|/det|>
\[ \vec{x} = 2 \cdot \vec{x}_1 + 3 \cdot \vec{x}_2 - 5 \cdot \vec{x}_3 = \begin{pmatrix} 4 \\ 1 \\ -6 \end{pmatrix} \]

<|ref|>text<|/ref|><|det|>[[115, 581, 312, 599]]<|/det|>
ist die Lösung, da gilt 

<|ref|>equation<|/ref|><|det|>[[115, 598, 460, 660]]<|/det|>
\[ \begin{align*} A \cdot \vec{x} &= A \cdot (2 \cdot \vec{x}_1 + 3 \cdot \vec{x}_2 -5 \cdot \vec{x}_3) \\ &= 2 \cdot (A \cdot \vec{x}_1) + 3 \cdot (A \cdot \vec{x}_2) - 5 \cdot (A \cdot \vec{x}_3) \\ &= 2 \cdot \vec{e}_1 + 3 \cdot \vec{e}_2-5 \cdot \vec{e}_3 = \vec{b} \end{align*} \]

<|ref|>text<|/ref|><|det|>[[115, 661, 212, 678]]<|/det|>
Alternativ: 

<|ref|>text<|/ref|><|det|>[[115, 677, 680, 696]]<|/det|>
Kombiniert man die 3 Spaltenvektoren \(\vec{x}_1, \vec{x}_2, \vec{x}_3\) zu einer Matrix 

<|ref|>equation<|/ref|><|det|>[[325, 694, 576, 752]]<|/det|>
\[ X = (\vec{x}_1 | \vec{x}_2 | \vec{x}_3) = \begin{pmatrix} 1 & -6 & -4 \\ 0 & 2 & 1 \\ -1 & 7 & 5 \end{pmatrix} \]

<|ref|>text<|/ref|><|det|>[[115, 763, 189, 779]]<|/det|>
dann ist 

<|ref|>equation<|/ref|><|det|>[[269, 777, 628, 797]]<|/det|>
\[ A \cdot X = (A \cdot \vec{x}_1 | A \cdot \vec{x}_2 | A \cdot \vec{x}_3) = (\vec{e}_1 | \vec{e}_2 | \vec{e}_3) = E \]

<|ref|>text<|/ref|><|det|>[[115, 802, 723, 820]]<|/det|>
und somit \(X = A^{-1}\) die Inverse zu \(A\). Aus der Lösungsformel für LGS folgt dann 

<|ref|>equation<|/ref|><|det|>[[273, 830, 625, 888]]<|/det|>
\[ \vec{x} = A^{-1} \cdot \vec{b} = \begin{pmatrix} 1 & -6 & -4 \\ 0 & 2 \\ -1 & 7 & 5 \end{pmatrix} \cdot \begin{pmatrix} 2 \\ 3 \\ -5 \end{pmatrix} = \begin{pmatrix} 4 \\ 1 \\ -6 \end{pmatrix} \]