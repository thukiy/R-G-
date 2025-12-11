<|ref|>text<|/ref|><|det|>[[115, 81, 714, 100]]<|/det|>
Weil \(\mathbb{R}\) ein Zahlen-Körper ist, gilt für alle \(\mathbf{v}, \mathbf{w} \in \mathbb{R}^3\) und alle \(a, b \in \mathbb{R}\), dass 

<|ref|>equation<|/ref|><|det|>[[211, 107, 732, 169]]<|/det|>
\[a \cdot \mathbf{v} + b \cdot \mathbf{w} = a \cdot \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix} + b \cdot \begin{bmatrix} w_1 \\ w_2 \\ w_3 \end{bmatrix} = \begin{bmatrix} a \cdot v_1 + b \cdot w_1 \\ a \cdot v_2 + b \cdot w_2 \\ a \cdot v_3 + b \cdot w_3 \end{bmatrix} \in \mathbb{R}^3.\]

<|ref|>text<|/ref|><|det|>[[115, 170, 370, 188]]<|/det|>
Es liegt ein Vektorraum vor. 

<|ref|>sub_title<|/ref|><|det|>[[115, 202, 567, 221]]<|/det|>
## 3. Linear abhängig/unabhängig und erzeugend 

<|ref|>text<|/ref|><|det|>[[115, 220, 860, 255]]<|/det|>
Bestimmen Sie, ob die jeweiligen Vektoren linear unabhängig bzw. erzeugend sind. Bilden die gegebenen Vektoren eine Basis des jeweiligen \(\mathbb{R}^n\)? 

<|ref|>equation<|/ref|><|det|>[[115, 256, 870, 360]]<|/det|>
\[ \begin{align*} a) \left\{ \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \begin{pmatrix} 1 \\ -1 \end{pmatrix} \right\} \qquad & b) \left\{ \begin{pmatrix} 2 \\ -6 \end{pmatrix}, \begin{pmatrix} -1 \\ 3 \end{pmatrix} \right\} \qquad & c) \left\{ \begin{pmatrix} -1 \\ 0 \end{pmatrix}, \begin{pmatrix} 3 \\ 2 \end{pmatrix}, \begin{pmatrix} 1 \\ 1 \end{pmatrix} \right\} \qquad & d) \left\{ \begin{pmatrix} 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ -1 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \end{pmatrix} \right\} \qquad & e) \left\{ \begin{pmatrix} 1 \\ 2 \end{pmatrix}, \begin{pmatrix} 5 \\ 6 \end{pmatrix}, \begin{pmatrix} 2 \\ 4 \end{pmatrix} \right\} \qquad & f) \left\{ \begin{pmatrix} 0 \\ 1 \end{pmatrix}, \begin{smallmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \end{pmatrix} \end{pmatrix} \end{align*} \]

<|ref|>text<|/ref|><|det|>[[115, 376, 150, 392]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[115, 390, 360, 407]]<|/det|>
Wir betrachten die Teilmenge 

<|ref|>equation<|/ref|><|det|>[[290, 415, 655, 453]]<|/det|>
\[ M = \{ \mathbf{v}_1, \mathbf{v}_2 \} = \left\{ \begin{bmatrix} 1 \\ 1 \end{bmatrix}, \begin{bmatrix} -1 \\ -1 \end{bmatrix} \right\} \subset V = \mathbb{R}^2 \]

<|ref|>text<|/ref|><|det|>[[115, 462, 570, 480]]<|/det|>
aus \(m = 2\) Vektoren. Wir schreiben das homogene LGLS 

<|ref|>equation<|/ref|><|det|>[[285, 488, 658, 527]]<|/det|>
\[ 0 = x_1 \cdot \mathbf{v}_1 + x_2 \cdot \mathbf{v}_2 = x_1 \cdot \begin{bmatrix} 1 \\ 1 \end{bmatrix} + x_2 \cdot \begin{bmatrix} 1 \\ -1 \end{bmatrix} \]

<|ref|>text<|/ref|><|det|>[[115, 535, 827, 569]]<|/det|>
in einem Gauss-Schema und bringen dieses mit Hilfe des Gauss-Verfahrens auf Stufenform. Es gilt 

<|ref|>equation<|/ref|><|det|>[[122, 577, 590, 625]]<|/det|>
\[ \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & 1 \\ 0 & -2 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & 1 \\ 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}. \]

<|ref|>text<|/ref|><|det|>[[115, 632, 429, 649]]<|/det|>
Das LGLS hat offensichtlich den Rang 

<|ref|>equation<|/ref|><|det|>[[400, 661, 544, 677]]<|/det|>
\[ n_R = 2 = m = n. \]

<|ref|>text<|/ref|><|det|>[[115, 688, 820, 725]]<|/det|>
Demnach ist \(M\) linear unabhängig sowie erzeugend und bildet folglich eine Basis von \(V\). b) 

<|ref|>text<|/ref|><|det|>[[115, 725, 360, 742]]<|/det|>
Wir betrachten die Teilmenge 

<|ref|>equation<|/ref|><|det|>[[280, 750, 661, 789]]<|/det|>
\[ M = \{ \mathbf{v}_1, \mathbf{v}_2 \}= \left\{ \begin{bmatrix} 2 \\ -6 \end{bmatrix}, \begin{bmatrix} -1 \\ 3 \end{bmatrix} \right\} \subset V = \mathbb{R}^2 \]

<|ref|>equation<|/ref|><|det|>[[115, 799, 570, 816]]<|/det|>
\[ \text{aus } m = 2 \text{ Vektoren. Wir schreiben das homogene LGLS} \]

<|ref|>equation<|/ref|><|det|>[[278, 824, 664, 863]]<|/det|>
\[ 0 = x_1 \cdot \mathbf{v}_1 + x_{2} \cdot \mathbf{v}_{2} = x_{1} \cdot \begin{bmatrix} 2 \\ -6 \end{bmatrix} + x_{2} \cdot \begin{bmatrix} -1 \\ 3 \end{bmatrix} \]