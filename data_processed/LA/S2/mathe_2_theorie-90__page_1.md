<|ref|>text<|/ref|><|det|>[[99, 12, 707, 42]]<|/det|>
→ Henge de Eigenwerte heisst Spektrum von A : 

<|ref|>equation<|/ref|><|det|>[[147, 48, 450, 82]]<|/det|>
\[
\text{spec}(A) = \{ \lambda_1, \ldots, \lambda_n \}
\]

<|ref|>text<|/ref|><|det|>[[99, 90, 950, 120]]<|/det|>
→ \(\vec{E}_1\) & \(\vec{E}_2\) seien Eigenvektoren zum selben Eigenvektor \(\lambda\), \(a, b \in \mathbb{R}\) : 

<|ref|>equation<|/ref|><|det|>[[150, 127, 627, 234]]<|/det|>
\[
\begin{align*}
A(a \cdot \vec{E}_1 + b \cdot \vec{E}_2) &= a \cdot A \cdot \vec{E}_1 + b \cdot A \cdot \vec{E}_2 \\
&= a \cdot \lambda \cdot \vec{E}_1 + b \cdot \lambda \cdot \vec{E}_2 \\
&= \lambda (a \cdot \vec{E}_1 + b \cdot \vec{E}_2)
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[150, 245, 873, 272]]<|/det|>
↪ Vielfaches eines Eigenvektors und dünnströmbinatlon von 

<|ref|>text<|/ref|><|det|>[[187, 285, 911, 312]]<|/det|>
eigenvektoren zum selben Eigenwert sind wieder Eigenvektor 

<|ref|>text<|/ref|><|det|>[[99, 344, 644, 371]]<|/det|>
→ bei Drehungen : Eigenvektor // Drehachse 

<|ref|>text<|/ref|><|det|>[[99, 384, 940, 411]]<|/det|>
→ bei Spiegelungen : Vektoren in Spiegelflyperebene sind Eigenvektoren 

<|ref|>text<|/ref|><|det|>[[20, 442, 561, 469]]<|/det|>
Bestimmung von Eigenweiten und -vektoren 

<|ref|>equation<|/ref|><|det|>[[50, 476, 490, 505]]<|/det|>
\[
A \cdot \vec{E} = \lambda \cdot \vec{E} \iff (A - \lambda \cdot \mathbb{1}) \cdot \vec{E} = 0
\]

<|ref|>equation<|/ref|><|det|>[[35, 518, 299, 545]]<|/det|>
\[
\rightarrow \det(A - \lambda \cdot \mathbb{1}) = 0
\]

<|ref|>text<|/ref|><|det|>[[20, 577, 440, 604]]<|/det|>
Def: Gegeben sei \(n \times n\) Matrix \(A\) 

<|ref|>equation<|/ref|><|det|>[[110, 616, 950, 644]]<|/det|>
\[
p_A(\lambda) = \det(A - \lambda \cdot \mathbb{1}) \quad \text{heisst charakteristisches Polynom } n\text{-ten Grades}
\]

<|ref|>equation<|/ref|><|det|>[[110, 655, 672, 682]]<|/det|>
\[
p_A(\lambda) = 0 \quad \text{heisst charakteristische Gleichung}
\]

<|ref|>text<|/ref|><|det|>[[99, 694, 920, 721]]<|/det|>
→ Nulleben den charakteristischen Polynoms sind Eigenwerte von A 

<|ref|>equation<|/ref|><|det|>[[99, 732, 515, 760]]<|/det|>
\[
p_0(\lambda) = \det(0 - \lambda \cdot \mathbb{1}) = (-\lambda)^n
\]

<|ref|>equation<|/ref|><|det|>[[150, 771, 755, 799]]<|/det|>
\[
p_n(\lambda) = \det(1 - \lambda \cdot \mathbb{1}) = (1 - \lambda)^n \cdot \det(\mathbb{1}) = (1 - \lambda)^n
\]

<|ref|>text<|/ref|><|det|>[[20, 830, 270, 858]]<|/det|>
Bsp: \(A = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}\) 

<|ref|>equation<|/ref|><|det|>[[150, 867, 630, 896]]<|/det|>
\[
p_A(\lambda) = \det(A - \lambda \cdot 1) = \det\begin{pmatrix} 1-\lambda & -1 \\ 1 & 1-\lambda \end{pmatrix}
\]

<|ref|>equation<|/ref|><|det|>[[224, 907, 777, 933]]<|/det|>
\[
= (1-\lambda)(-1-\lambda) - 3 = -1-\lambda + \lambda + \lambda^2 - 3 = \lambda^2 - 4
\]

<|ref|>equation<|/ref|><|det|>[[150, 944, 920, 973]]<|/det|>
\[
p_A(\lambda) \stackrel{!}{=} 0 \quad \lambda^2 - 4 = 0 \iff \lambda^2 = 4 \quad \rightarrow \lambda_1 = +2 \quad \lambda_2 = -2
\]