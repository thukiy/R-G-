<|ref|>equation<|/ref|><|det|>[[119, 81, 570, 186]]<|/det|>
\[
\begin{align*}
E_1: \begin{bmatrix} -1 - (-1) & 0 - 0 \\ 0 - 0 & -1 - 1 \end{bmatrix} &\Leftrightarrow \begin{bmatrix} 0 & 0 \\ 0 & [-2] \end{bmatrix} &\Leftrightarrow \begin{bmatrix} 0 & [1] \end{bmatrix} \\
E_2: \begin{bmatrix} 1 - (-1) & 0 - 0 \\ 0 - 0 & 1 - 1 \end{bmatrix} &\Leftrightarrow \begin{bmatrix} 2 & 0 \\ 0 & 0 \end{bmatrix} &\Leftrightarrow \begin{bmatrix} 1 & 0 \end{bmatrix} .
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[119, 196, 845, 214]]<|/det|>
Durch Ablesen aus den reduzierten Stufenformen erhalten wir die reellen Eigenräume 

<|ref|>equation<|/ref|><|det|>[[119, 225, 585, 315]]<|/det|>
\[
\begin{align*}
E_1(S_y) &= \left\{ \begin{bmatrix} x \\ 0 \end{bmatrix} \in \mathbb{R}^2 \right\} = \text{span} \left\{ \begin{bmatrix} 1 \\ 0 \end{bmatrix} \right\} = \text{span} \{\hat{e}_x\} \\
E_2(S_y) &= \left\{ \begin{bmatrix} 0 \\ y \end{bmatrix} \in \mathbb{R}^2 \right\} = \text{span}\left\{ \begin{bmatrix} 0 \\ 1 \end{bmatrix} \right\} = \text{span} \{\hat{e}_y\}.
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[115, 330, 504, 348]]<|/det|>
3. Eigenwerte und -vektoren bestimmen 

<|ref|>text<|/ref|><|det|>[[115, 347, 880, 382]]<|/det|>
Berechnen Sie jeweils das charakteristische Polynom, die reellen Eigenwerte und die reellen Eigenvektoren der Matrix. 

<|ref|>equation<|/ref|><|det|>[[115, 380, 761, 458]]<|/det|>
\[
\begin{align*}
a) \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix} \qquad b) \begin{pmatrix} 1 & 1 \\ 2 & 0 \end{pmatrix} \qquad c) \begin{pmatrix} 0 & 6 \\ 2 & 0 \end{pmatrix} \\
d) \begin{pmatrix} 0 & -6 \\ 2 & 0 \end{pmatrix} \qquad e) \begin{pmatrix} 2 & 2 & -1 \\ 0 & -3 & 0 \end{pmatrix} \qquad f) \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[125, 475, 633, 503]]<|/det|>
a) Da die Matrix diagonal ist, entsprechen die Eigenwerte den Einträgen in der Hauptdiagonale. 

<|ref|>equation<|/ref|><|det|>[[156, 510, 725, 650]]<|/det|>
\[
\begin{align*}
\lambda_1 &= 2, \quad \lambda_2 = 3 \implies \text{spec}(A) = \{\xi_1, \xi_2, \xi_3\} \\
\text{det} \begin{pmatrix} \lambda_1 - 2 & 0 \\ 0 & \lambda_2 - 3 \end{pmatrix} &= (\lambda_1 - 2)(\lambda_2 - 3) = 6 - 5\lambda_1 + \lambda_2^2 = P_A(\lambda) \\
\vec{E}_1 \text{ und } \lambda_1 = 2: \quad \vec{E}_1^2 = 4 \cdot \begin{pmatrix} 0 \\ 0 \end{pmatrix} \\
\vec{E}_2 \text{ und } \lambda_2 = 3: \quad \vec{E}_2^2 = 4 \cdot \begin{pmatrix} 0 \\ 1 \end{pmatrix}
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[115, 653, 562, 737]]<|/det|>
\[
\begin{align*}
5) \quad \det \begin{pmatrix} \lambda_1 - 1 & 1 \\ 2 & \lambda_2 - 2 \end{pmatrix} &= (\lambda_1 - 1)(\lambda_2 - 2) - 2 \\
&= \lambda_1 - 3\lambda_1 + \lambda_2^2 - 2 = \lambda_1^2 - 3\lambda_1 = P_A(\lambda)
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[161, 744, 446, 817]]<|/det|>
\[
\begin{align*}
P_A(\lambda) \stackrel{!}{=} 0 \\
\lambda^2 - 3\lambda = \lambda(\lambda - 3) \stackrel{!}{=} 0 \\
\lambda_1 = 0 \quad \lambda_2 = 3
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[164, 830, 325, 863]]<|/det|>
\[
\vec{E}_1 \text{ und } \lambda_1 = 0:
\]

<|ref|>equation<|/ref|><|det|>[[173, 864, 444, 914]]<|/det|>
\[
\begin{array}{c|cc}
1 & 1 & 0 \\
2 & 2 & 0 \\
\end{array}
\quad \begin{array}{c|cc}
1 & 1 & 0 \\
0 & 0 & 0 \\
\end{array}
\quad \begin{array}{c|cc}
0 & 0 & 0 \\
1 & 1 & 0 \\
\end{array}
\]

<|ref|>equation<|/ref|><|det|>[[0, 0, 0, 0]]<|/det|>
\[
\begin{align*}
\lambda_1 &= 0, \quad \lambda_2 = 0
\end{align*}
\]