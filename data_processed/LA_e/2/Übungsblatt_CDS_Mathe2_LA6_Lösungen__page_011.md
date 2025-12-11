<|ref|>text<|/ref|><|det|>[[118, 85, 714, 106]]<|/det|>
somit folgt \(P^{-1} = P^T\), das heisst, die Matrix \(P\) ist orthogonal. Es gilt 

<|ref|>equation<|/ref|><|det|>[[135, 115, 827, 157]]<|/det|>
\[Z_3^{-1} = Z_{1/3} = \frac{1}{3} \cdot \mathbb{1} = \begin{bmatrix} \frac{1}{3} & 0 \\ 0 & \frac{1}{3} \end{bmatrix} \quad \text{und} \quad Z_3^T = \begin{bmatrix} 3 & 0 \\ 0 & 3 \end{bmatrix}^T = \begin{bmatrix} 3 & 0 \\ 0 & 3 \end{ bmatrix} = 3 \cdot \mathbb{1} = Z_3,\]

<|ref|>text<|/ref|><|det|>[[118, 164, 880, 252]]<|/det|>
somit folgt \(Z_3^{-1} \neq Z_3^T\), das heisst, die Matrix \(Z_3\) ist nicht orthogonal. Die Matrizen \(P_x\) und \(P_y\) beschreiben die Projektionen senkrecht auf die \(x\)-Achse bzw. auf die \(y\)-Achse und demnach lineare Abbildungen, welche weder injektiv noch surjektiv sind. Folglich existieren für \(P_x\) bzw. \(P_y\) keine inversen Matrizen, womit Orthogonalität für \(P_x\) und \(P_y\) zum Vornherein ausgeschlossen werden kann. Es gilt 

<|ref|>equation<|/ref|><|det|>[[204, 260, 790, 304]]<|/det|>
\[S_x^{-1} = S_x = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} \quad \text{und} \quad S_x^T = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}^T = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{ bmatrix} = S_x,\]

<|ref|>text<|/ref|><|det|>[[118, 313, 715, 333]]<|/det|>
somit folgt \(S_x^{-1} = S_x^T\), das heisst, die Matrix \(S_x\) ist orthogonal. Es gilt 

<|ref|>equation<|/ref|><|det|>[[204, 342, 790, 385]]<|/det|>
\[S_y^{-1} = S_y = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix} \quad \text{und} \quad S_y^T = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}^T = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{ bmatrix} = S_y,\]

<|ref|>text<|/ref|><|det|>[[118, 392, 715, 413]]<|/det|>
somit folgt \(S_y^{-1} = S_y^T\), das heisst, die Matrix \(S_y\) ist orthogonal. Es gilt 

<|ref|>equation<|/ref|><|det|>[[118, 421, 555, 592]]<|/det|>
\[R^{-1}(\pi/2) = R(-\pi/2) = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix} \\ R^T(\pi/2) = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}^T = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}^T = R(-\pi/2),\]

<|ref|>text<|/ref|><|det|>[[118, 599, 850, 620]]<|/det|>
somit folgt \(R^{-1}(\pi/2) = R^T(\pi/2)\), das heisst, die Matrix \(R(\pi/2)\) ist orthogonal. Es gilt 

<|ref|>equation<|/ref|><|det|>[[118, 628, 553, 670]]<|/det|>
\[R^{-1}(-\pi/2) = R(\pi/2) = \begin{bmatrix} 0 & -1 \\ 1 & -1 \end{bmatrix}\]

<|ref|>equation<|/ref|><|det|>[[118, 677, 553, 730]]<|/det|>
\[R^T(-\pi/2) = \begin{bmatrix} 0 & 1 \\ -1 & -1 \end{bmatrix}^T = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} = R(\pi/2),\]

<|ref|>text<|/ref|><|det|>[[118, 737, 875, 775]]<|/det|>
somit folgt \(R^{-1}(-\pi/2) = R^T(-\pi/2)\), das heisst, die Matrix \(R(-\pi/2)\) ist orthogonal. Es gilt 

<|ref|>equation<|/ref|><|det|>[[118, 783, 520, 790]]<|/det|>
\[R^{-1}(\pi/4) = R(-\pi/4) = \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{bmatrix}\]

<|ref|>equation<|/ref|><|det|>[[118, 799, 512, 792]]<|/det|>
\[R^T(\pi/4) = \begin{bmatrix} \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \quad \end{bmatrix}^T = \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{2} \\ -\frac{1}{\sqrt{2}} & \frac{1}{2} \end{bmatrix},\]

<|ref|>text<|/ref|><|det|>[[118, 797, 875, 850]]<|/det|>
somit folgt \(R^{-1}(\pi/4) = R^T(\pi/4)\), das heisst, die Matrix \(R(\pi/4)\) ist orthogonal. Von allen Matrizen, welche wir in dieser Teilaufgabe untersucht haben, sind also diejenigen in der Menge 

<|ref|>equation<|/ref|><|det|>[[327, 856, 666, 877]]<|/det|>
\[\{\mathbb{1}, P, S_x, S_y, R(\pi/2), R(-\pi/2), R(\pi/4)\}\]

<|ref|>text<|/ref|><|det|>[[118, 890, 830, 908]]<|/det|>
orthogonal. Bemerkenswerterweise sind das genau die Spiegelungen und Drehungen!