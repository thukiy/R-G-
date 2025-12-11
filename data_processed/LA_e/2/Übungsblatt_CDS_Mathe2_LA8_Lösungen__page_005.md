<|ref|>text<|/ref|><|det|>[[115, 81, 410, 100]]<|/det|>
Bestimmung der Eigenvektoren: 

<|ref|>equation<|/ref|><|det|>[[119, 100, 500, 202]]<|/det|>
\[
\begin{align*}
E_1: \begin{bmatrix} 0 & -1 & 0 & -0 \\ 0 & -0 & 0 & -0 \end{bmatrix} &\Leftrightarrow & \begin{bmatrix} [1] & 0 \\ 0 & 0 \end{bmatrix} \\
E_2: \begin{bmatrix} 1 & -1 & 0 & -0 \\ 0 & -1 & 0 & -1 \end{bmatrix} &\Leftrightarrow & \begin{bmatrix} 0 & 0 \\ 0 & [1] \end{bmatrix} \\
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[119, 212, 844, 230]]<|/det|>
Durch Ablesen aus den reduzierten Stufenformen erhalten wir die reellen Eigenräume 

<|ref|>equation<|/ref|><|det|>[[119, 240, 588, 280]]<|/det|>
\[
E_1(P_x) = \left\{ \begin{bmatrix} 0 \\ y \end{bmatrix} \in \mathbb{R}^2 \right\} = \text{span} \left\{ \begin{bmatrix} 0 \\ 1 \end{bmatrix} \right\} = \text{span} \{\hat{e}_y\}
\]

<|ref|>equation<|/ref|><|det|>[[119, 288, 590, 328]]<|/det|>
\[
E_2(P_x) = \left\{ \begin{bmatrix} x \\ 0 \end{bmatrix} \in \mathbb{R}^2 \right\} = \text{span}\left\{ \begin{bmatrix} 1 \\ 0 \end{bmatrix} \right\} = \text{span}\{\hat{e}_x\}.
\]

<|ref|>text<|/ref|><|det|>[[115, 343, 795, 380]]<|/det|>
Spur, Determinante und charakteristisches Polynom von P_y ergeben sich zu
tr(P_y) = 0 + 1 = 1 

<|ref|>equation<|/ref|><|det|>[[119, 386, 405, 404]]<|/det|>
\[
\det(P_y) = 0 \cdot 0 - 0 \cdot 1 = 0 - 0 = 0
\]

<|ref|>equation<|/ref|><|det|>[[122, 410, 639, 435]]<|/det|>
\[
\frac{p_{P_y}(\lambda)}{\lambda} = \lambda^2 - \text{tr}(P_y) \cdot \lambda + \det(P_y) = \lambda^2 - 1 \cdot \lambda + 0 = \frac{\lambda^2 - \lambda}{\lambda}
\]

<|ref|>text<|/ref|><|det|>[[119, 437, 444, 455]]<|/det|>
Die charakteristische Gleichung lautet 

<|ref|>equation<|/ref|><|det|>[[350, 467, 636, 486]]<|/det|>
\[
0 = p_{P_y}(\lambda) = \lambda^2 - \lambda = \lambda \cdot (\lambda - 1)
\]

<|ref|>text<|/ref|><|det|>[[119, 486, 430, 504]]<|/det|>
und hat die beiden reellen Lösungen 

<|ref|>equation<|/ref|><|det|>[[397, 518, 590, 536]]<|/det|>
\[
\lambda_1 = 0 \quad \text{und} \quad \lambda_2 = 1.
\]

<|ref|>text<|/ref|><|det|>[[115, 547, 610, 566]]<|/det|>
Dies sind gerade die reellen Eigenwerte von P_y, es ist also 

<|ref|>equation<|/ref|><|det|>[[411, 578, 576, 600]]<|/det|>
\[
\text{spec}(P_y) = \{0, 1\}.
\]

<|ref|>text<|/ref|><|det|>[[115, 602, 410, 621]]<|/det|>
Bestimmung der Eigenvektoren: 

<|ref|>equation<|/ref|><|det|>[[119,

<|ref|>equation<|/ref|><|det|>[[119, 625, 495, 666]]<|/det|>
\[
E_1: \begin{bmatrix} 0 & -1 & 0 & -0 & 0 \\ 0 & -0 & 0 & -1 & 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 0 & 0 \\ 0 & [1] \end{bmatrix}
\]

<|ref|>equation<|/ref|><|det|>[[119, 680, 500, 722]]<|/det|>
\[
E_2: \begin{bmatrix} 1 & -1 & 0 & -0 & 0 \\ 0 & -1 & 0 & -1 & 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix}[1] & 0 \\ 0 & 0 \end{bmatrix}
\]

<|ref|>text<|/ref|><|det|>[[115, 737, 840, 755]]<|/det|>
Durch Ablesen aus den reduzierten Stufenformen erhalten wir die Reellen Eigenräume 

<|ref|>equation<|/ref|><|det|>[[119, 767, 580, 807]]<|/det|>
\[
E_1(P_y) = \left\{ \begin{bmatrix} x \\ 0 \end{bmatrix} \in R^2 \right\} = \text{span} \left\{ \begin{bmatrix} 1 \\ 0 \end{bmatrix} \right\} = span\{\hat{e}_x\}
\]

<|ref|>equation<|/ref|><|det|>[[119, 816, 580, 856]]<|/det|>
\[
E_2(P_y) = \left\{ \begin{bmatrix} 0 \\ y \end{bmatrix} \in R^2 \right\} = \text{span} \begin{cases} \begin{bmatrix} 0 \\ 1 \end{bmatrix} \end{cases} = \text{span}\{\hat{e}_y\}.
\]

<|ref|>text<|/ref|><|det|>[[115, 872, 795, 890]]<|/det|>
Spur, Determinante und charakteristisches Polynom von S_x ergeben sich zu