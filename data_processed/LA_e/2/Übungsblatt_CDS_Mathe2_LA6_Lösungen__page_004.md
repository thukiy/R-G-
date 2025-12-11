<|ref|>equation<|/ref|><|det|>[[114, 81, 810, 255]]<|/det|>
\[
\begin{align*}
R_{-\alpha} \cdot R_{\alpha} &= \begin{bmatrix} \cos(\alpha) & \sin(\alpha) \\ -\sin(\alpha) & \cos(\alpha) \end{bmatrix} \cdot \begin{bmatrix} \cos(\alpha) & -\sin(\alpha) \\ \sin(\alpha) & \cos(\alpha) \end{bmatrix} \\
&= \begin{bmatrix} \cos(\alpha) \cos(\alpha) + \sin(\alpha) \sin(\alpha) & \cos(\alpha)(-\sin(\alpha)) + \sin(\alpha) \cos(\alpha) \\ (-\sin(\alpha)) \cos(\alpha) + \cos(\alpha) \sin(\alpha) & (-\sin(\alpha))(-\sin(\alpha)) + \cos(\alpha) \cos(\alpha) \end{bmatrix} \\
&= \begin{bmatrix} \cos^2(\alpha) + \sin^2(\alpha) & -\cos(\alpha) \sin(\alpha) + \sin(\alpha) \cos(\alpha) \\ -\sin(\alpha) \cos(\alpha) + \cos(\alpha) \sin(\alpha) & \sin^2(\alpha) + \cos^2(\alpha) \end{bmatrix} \\
&= \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \underline{\mathbb{1}},
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 255, 145, 273]]<|/det|>
d) 

<|ref|>text<|/ref|><|det|>[[114, 271, 870, 344]]<|/det|>
Die Hintereinanderausführung der Matrizen \(R_{\alpha}\) und \(R_{\beta}\) sollte aus geometrischer Sicht bedeuten, dass zuerst eine Drehung um \(\alpha\) und anschliessend eine Drehung um \(\beta\) (bzw. umgekehrt) ausgeführt wird \(\rightarrow\) insgesamt also um den Winkel \(\alpha+\beta\). Dies bedeutet, dass gelten sollte: \(R_{\alpha} \cdot R_{\beta} = R_{\beta} \cdot R_{\alpha} = R_{\alpha+\beta}\). 

<|ref|>equation<|/ref|><|det|>[[114, 345, 800, 686]]<|/det|>
\[
\begin{align*}
R_{\alpha} \cdot R_{\beta} &= \begin{bmatrix} \cos(\alpha) & -\sin(\alpha) \\ \sin(\beta) & \cos(\beta) \end{bmatrix} \cdot \begin{bmatrix} \cos(\beta) & -\sin(\beta) \\ \sin(\beta) & \cos(\beta) \end{bmatrix} \\
&= \begin{bmatrix} \cos(\alpha) \cos(\beta) + (-\sin(\alpha)) \sin(\beta) & \cos(\alpha)(-\sin(\beta)) + (-\sin(\alpha)) \cos(\beta) \\ \sin(\alpha) \cos(\beta) + \cos(\alpha) \sin(\beta) & \sin(\alpha)(-\sin(\beta)) + \cos(\alpha) \cos(\beta) \end{bmatrix} \\
&= \begin{bmatrix} \cos(\alpha)\cos(\beta) - \sin(\alpha)\sin(\beta) & -\cos(\alpha)\sin(\beta) - \sin(\alpha)\cos(\beta) \\ \sin(\alpha)\cos(\beta) + \cos(\alpha)\sin(\beta) & \cos(\alpha)\cos(\beta) - \sin(\alpha)\sin(\beta) \end{bmatrix} \\
&= \begin{bmatrix} \cos(\alpha + \beta) & -\sin(\alpha + \beta) \\ \sin(\alpha + \beta) & \cos(\alpha + \beta) \end{bmatrix} = R_{\alpha+\beta} \\
R_{\beta} \cdot R_{\alpha} &= \begin{bmatrix} \cos(\beta) & -\sin(\beta) \\ \sin(\alpha) & \cos(\beta) \end{bmatrix} \cdot \begin{bmatrix} \cos( \alpha) & -\sin( \alpha) \\ \sin( \alpha) & \cos( \alpha) \end{bmatrix} \\
&= \begin{bmatrix} \cos(\beta) \cos(\alpha) + (-\sin(\beta)) \sin(\alpha) & \cos(\beta)(-\sin(\alpha)) + (-\sin(\beta)) \cos(\alpha) \\ \sin(\beta) \cos(\alpha) + \cos(\beta) \sin(\alpha) & \sin(\beta)(-\sin(\alpha)) + \cos(\beta) \cos(\alpha) \end{bmatrix} \\
&= \begin{bmatrix} \cos(\beta) \cos( \alpha) - \sin(\beta) \sin(\alpha) & -\cos(\beta) \sin(\alpha) - \sin(\beta) \cos(\alpha) \\ \sin(\beta) \cos(\alpha) + \cos( \beta) \sin(\alpha) & \cos(\beta) \cos(\alpha) - \sin(\beta) \sin(\alpha) \end{bmatrix} \\
&= \begin{bmatrix} \cos(\beta + \alpha) & -\sin(\beta + \alpha) \\ \sin(\beta + \alpha) & \cos(\beta + \alpha) \end{bmatrix} = R_{\beta+\alpha} = R_{\alpha+\beta} = R_{\alpha} \cdot R_{\beta}.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 685, 145, 703]]<|/det|>
e) 

<|ref|>equation<|/ref|><|det|>[[114, 702, 796, 840]]<|/det|>
\[
\begin{align*}
R_0 &= \begin{bmatrix} \cos(0) & -\sin(0) \\ \sin(0) & \cos(0) \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} =
\underline{\mathbb{1}}, \\
R_{\pm\pi/6} &= \begin{bmatrix} \cos(\pm\pi/6) & -\sin(\pm\pi/6) \\ \sin(\pm\pi/6) & \cos(\pm\pi/6) \end{bmatrix} = \begin{bmatrix} \cos(\pi/6) & \mp\sin(\pi/6) \\ \pm\sin(\pi/6) & \cos(\pi/6) \end{bmatrix} = \begin{bmatrix} \frac{\sqrt{3}}{2} & \mp\frac{1}{2} \\ \pm\frac{1}{2} & \frac{\sqrt{3}}{2} \end{bmatrix} \\
&= \frac{1}{2} \cdot \begin{bmatrix} \sqrt{3} & \mp 1 \\ \pm 1 & \sqrt{3} \end{bmatrix}.
\end{align*}
\]