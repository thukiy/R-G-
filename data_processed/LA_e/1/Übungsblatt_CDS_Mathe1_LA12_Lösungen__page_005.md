<|ref|>text<|/ref|><|det|>[[114, 82, 145, 100]]<|/det|>
b) 

<|ref|>equation<|/ref|><|det|>[[128, 100, 816, 280]]<|/det|>
\[
\begin{align*}
\vec{n} \cdot \vec{a} &= \begin{pmatrix} 3 \\ -1 \\ -1 \end{pmatrix} \cdot \begin{pmatrix} 2 \\ 5 \\ 1 \end{pmatrix} = 6 - 5 - 1 = 0 \quad \Rightarrow \quad g \text{ und } E \text{ sind parallel} \\
\vec{n} \cdot (\vec{r}_1 - \vec{r}_0) &= \begin{pmatrix} 3 \\ -1 \\ -1 \end{pmatrix} \cdot\begin{pmatrix} 5 - 1 \\ 3 - 1 \\ 6 - 1 \end{pmatrix} = \begin{pmatrix} 3 \\ -1 \\ -1 \end{pmatrix} \cdot \left(\begin{pmatrix} 4 \\ 2 \\ 5 \end{pmatrix}\right) = 12 - 2 - 5 = 5 \\
\text{Abstand: } d &= \frac{|\vec{n} \cdot (\vec{r}_1 - \vec{r}_0)|}{|\vec{n}|} = \frac{5}{\sqrt{11}} = 1,51
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 300, 308, 319]]<|/det|>
5. Parallele Ebenen 

<|ref|>text<|/ref|><|det|>[[114, 316, 875, 401]]<|/det|>
Eine Ebene \(E_1\) verläuft durch den Punkt \(P_1 = (1; 2; 3)\), ihr Normalenvektor ist \(\vec{n} = \begin{pmatrix} 2 \\ 1 \\ a \end{pmatrix}\).

Bestimmen Sie den noch unbekannten Parameter a so, dass der Abstand des Punktes \(Q = (0; 2; 5)\) von dieser Ebene \(d = 2\) beträgt. Wie lautet die Gleichung der Parallelebene \(E_2\) durch den Punkt \(A = (5; 1; -2)\)? 

<|ref|>equation<|/ref|><|det|>[[114, 430, 875, 655]]<|/det|>
\[
\begin{align*}
\text{Abstandformel: } d &= \frac{|\vec{n} \cdot (\vec{r}_Q - \vec{r}_1)|}{|\vec{n}|} \Rightarrow d |\vec{n}| = |\vec{n} \cdot (\vec{r}_Q - \vec{r}_1)| \\
\vec{n} \cdot (\vec{r}_Q - \vec{r}_1) &= \begin{pmatrix} 2 \\ 1 \\ a \end{pmatrix} \cdot \begin{pmatrix} -1 \\ 0 \\ 2 \end{pmatrix} = -2 + 0 + 2a = 2(a - 1); \quad |\vec{n}| = \sqrt{5 + a^2} \\
d |\vec{n}| = |\vec{n} \cdot (\vec{r}_Q - r_1)| \Rightarrow 2\sqrt{5 + a^2} = |2(a - 1)| \Rightarrow \\
\sqrt{5 + a^2} = |a - 1| \quad \text{quadrieren} \Rightarrow 5 + a^2 = (a - 1)^2 = a^2 - 2a + 1 \Rightarrow \\
2a = -4 \Rightarrow a = -2
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 666, 771, 685]]<|/det|>
Die Gleichung der Parallelebene \(E_2\) durch den Punkt \(A = ( 5; 1; -2 )\) lautet: 

<|ref|>equation<|/ref|><|det|>[[114, 695, 857, 810]]<|/det|>
\[
\begin{align*}
\vec{n} \cdot (\vec{r} - \vec{r}_A) &= \begin{pmatrix} 2 \\ 1 \\ -2 \end{pmatrix} \cdot \begin{pmatrix} x - 5 \\ y - 1 \\ z + 2 \end{pmatrix} = 2(x - 5) + 1(y - 1) - 2(z + 2) = 0 \Rightarrow \\
2x + y - 2z = 15
\end{align*}
\]