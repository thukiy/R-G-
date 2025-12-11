<|ref|>equation<|/ref|><|det|>[[40, 10, 714, 120]]<|/det|>
\[
\begin{align*}
\vec{a}_1^\top \vec{a}_1 &= (a_{11} \quad a_{12} \quad \ldots \quad a_{1n}) \cdot \begin{pmatrix} a_{11} \\ a_{12} \\ \vdots \\ a_{1n} \end{pmatrix} \\
&= a_{11}^2 + a_{12}^2 + \ldots + a_{1n}^2 = \langle \vec{a}_1^\top, \vec{a}_1^\top \rangle
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[40, 163, 565, 234]]<|/det|>
\[
\langle \vec{a}, \vec{a} \rangle = a_1^2 + a_2^2 + \ldots + a_n^2 = |\vec{a}|^2 \\
|\vec{a}| = \sqrt{a_1^2 + a_2^2 + \ldots + a_n^2}
\]

<|ref|>equation<|/ref|><|det|>[[40, 258, 550, 316]]<|/det|>
\[
\rightarrow \langle \vec{a}_j, \vec{a}_j \rangle = \delta_{ij} = \begin{cases} 1 & i = j \\ 0 & i \neq j \end{cases}
\]

<|ref|>text<|/ref|><|det|>[[115, 364, 761, 393]]<|/det|>
(Skalarprodukt ist 0, wenn Verloren 1 sind) 

<|ref|>text<|/ref|><|det|>[[40, 423, 933, 488]]<|/det|>
→ Spalten bzw. Deelenveloren einer orthogonalen Matrix sind paarweise
senkrecht aufeinander 

<|ref|>text<|/ref|><|det|>[[40, 500, 920, 565]]<|/det|>
→ da Skalarprodukte in Hauptdiagonale 1 sind, haben die Spalten -
bzw. Deelenveloren die Dünge 1, sie sind also normiert 

<|ref|>text<|/ref|><|det|>[[40, 578, 940, 645]]<|/det|>
→ die Spalten- bzw. Deelenveloren einer orthogonalen Matrix stellen ein
Orthogonalisystem dar 

<|ref|>text<|/ref|><|det|>[[20, 672, 785, 740]]<|/det|>
Sata : A sei quadratisch n x n Matrix und \(\vec{v}, \vec{w} \in \mathbb{R}^n\)
Dann gilt : \(\langle \vec{v}, A \cdot \vec{w} \rangle = \langle A^\top \cdot \vec{v}, \vec{w} \rangle\) 

<|ref|>text<|/ref|><|det|>[[25, 772, 916, 802]]<|/det|>
Folgeungen : Für orthogonale n x n Matrix A und \(\vec{v}, \vec{w} \in \mathbb{R}^n\) gilt : 

<|ref|>equation<|/ref|><|det|>[[80, 812, 490, 840]]<|/det|>
\[
a) \langle A \cdot \vec{v}, A \cdot \vec{w} \rangle = \langle \vec{v}, \vec{w} \rangle
\]

<|ref|>text<|/ref|><|det|>[[150, 850, 440, 876]]<|/det|>
⇢ mit obigen Sata : 

<|ref|>equation<|/ref|><|det|>[[200, 886, 750, 915]]<|/det|>
\[
\langle A \cdot \vec{v}, A \cdot \vec{w} \rangle = \langle A^\top A \cdot \vec{v}, \vec{w} \rangle = \langle \vec{v}, \vec{w} \rangle = \langle \vec{v}, \vec{v} \rangle
\]