<|ref|>text<|/ref|><|det|>[[117, 80, 315, 99]]<|/det|>
Matrizenschreibweise: 

<|ref|>equation<|/ref|><|det|>[[186, 107, 476, 190]]<|/det|>
\[
\begin{pmatrix}
6 & -a & 3 & 0 \\
a & -1 & a & 0 \\
7 & 2 & 4 & 0
\end{pmatrix}
\begin{pmatrix}
(-1)
\end{pmatrix}
\]

<|ref|>equation<|/ref|><|det|>[[186, 181, 476, 245]]<|/det|>
\[
\begin{pmatrix}
6 & -a & 3 & 0 \\
-a & 1 & -a & 0 \\
7 & 2 & 4 & 0
\end{pmatrix}
\longleftrightarrow
\begin{pmatrix}
+ \\
(a)
\end{pmatrix}
(-2)
\]

<|ref|>equation<|/ref|><|det|>[[186, 246, 470, 310]]<|/det|>
\[
\begin{pmatrix}
6 - a^2 & 0 & 3 - a^2 & 0 \\
-a & 1 & -a & 0 \\
7 + 2a & 0 & 4 + 2a & 0
\end{pmatrix}
\longleftrightarrow
\begin{pmatrix}
(-1)
\end{pmatrix}
\]

<|ref|>equation<|/ref|><|det|>[[186, 312, 480, 377]]<|/det|>
\[
\begin{pmatrix}
6 - a^2 & 0 & 3 & -a^2 & 0 \\
-a & 1 & -a & 0 \\
1 + 2a + a^2 & 0 & 1 + 2a + a^2 & 0
\end{pmatrix}
\longleftrightarrow
\begin{pmatrix}
0 \\
0 \\
0 \\
\frac{1}{(1+a)^2}
\end{pmatrix}
\]

<|ref|>equation<|/ref|><|det|>[[186, 380, 485, 446]]<|/det|>
\[
\begin{pmatrix}
6 - a^2 & 0 & 3-a^2 & 0 \\
-a & 1 & -a & 0 \\
(1+a)^2 & 0 & (1+a)^2 & 0
\end{pmatrix}
\longleftrightarrow
\begin{pmatrix}
0 \\
0
\end{pmatrix}
\]

<|ref|>text<|/ref|><|det|>[[117, 453, 794, 473]]<|/det|>
Für \(a = -1\) gibt es offensichtlich eine nicht triviale Lösung. Ab jetzt sei \(a \neq -1\): 

<|ref|>equation<|/ref|><|det|>[[186, 483, 595, 567]]<|/det|>
\[
\begin{pmatrix}
6 - a^2 & 0 & 3- a^2 & 0 \\
-a & 1 & -a & 0 \\
1 & 0 & 1 & 0
\end{pmatrix}
\longleftrightarrow
\begin{pmatrix}
0 \\
0 \\
1 \\
0
\end{pmatrix}
\longleftrightarrow
\begin{pmatrix}
(a) & (-(6-a^2)) \\
0 & 0
\end{pmatrix}
\]

<|ref|>equation<|/ref|><|det|>[[186, 559, 595, 622]]<|/det|>
\[
\begin{pmatrix}
1 & 0 & 1 & 0 \\
-a & 1 & -a & 0 \\
6 - a^2 & 0 & 3 - a^2 & 0
\end{pmatrix}
\longleftrightarrow
\begin{pmatrix}
0 & 0 \\
0 & 0
\end{pmatrix}
\longleftrightarrow
\begin{pmatrix}
(a) & (-(6 - a^2))
\end{pmatrix}
\]

<|ref|>equation<|/ref|><|det|>[[186, 622, 312, 688]]<|/det|>
\[
\begin{pmatrix}
1 & 0 & 1 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & -3 & 0
\end{pmatrix}
\longleftrightarrow
\begin{pmatrix}
0 & 0 & 0 \\
0 & 0 & 0
\end{pmatrix}
\longleftrightarrow
\begin{pmatrix}
(a) & (6 - a^2)
\end{pmatrix}
\]

<|ref|>text<|/ref|><|det|>[[117, 700, 852, 737]]<|/det|>
Dieses LGS ist nur noch trivial lösbar, d. h. die 3 Vektoren sind dann linear unabhängig.
Also bilden die 3 Vektoren für \(a \neq -1\) eine Basis des \(\mathbb{R}^3\). 

<|ref|>sub_title<|/ref|><|det|>[[117, 752, 429, 771]]<|/det|>
5. Aussagen über Bild und Kern 

<|ref|>text<|/ref|><|det|>[[117, 770, 390, 788]]<|/det|>
Gegeben sei eine mxn Matrix. 

<|ref|>text<|/ref|><|det|>[[117, 786, 680, 805]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[117, 803, 877, 929]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Es gilt: \(\ker(A) \neq \emptyset\).</td><td>X</td><td></td></tr><tr><td>b) Für \(m = 2\) und \(n = 3\) gilt: \(\ker(A) \neq \{0\}\).</td><td>X</td><td></td></tr><tr><td>c) Für \(m = 3\) und \(n = 2\) gilt: \(\ker(A) \neq \{0\}\).</td><td>X</td><td>X</td></tr><tr><td>d) Für \(n = m\) und \(A\) regulär gilt: \(\ker(A) \neq \{0\}\).</td><td>X</td><td>X</td><td></td></tr><tr><td>e) Für \(n = m\) und \(A\) singulär gilt: \(\ker(A) \neq \{0\}\).</td><td>X</td><td>X<td></td></td></tr><tr><td>f) Für \(m = 3\) und \(n = 4\) gilt: \(\dim(\ker(A)) + \dim(\text{img}(A)) = 7\).</td><td>X</td><td></td></tr></table>