<|ref|>text<|/ref|><|det|>[[114, 81, 144, 99]]<|/det|>
h) 

<|ref|>equation<|/ref|><|det|>[[127, 102, 675, 330]]<|/det|>
\[
\begin{align*}
\det(A) &= \begin{vmatrix}
1 & 0 & 0 & 1 & 0 \\
1 & 0 & 0 & -1 & 0 \\
0 & 1 & 1 & 0 & 0 \\
0 & -1 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & \sqrt{2}
\end{vmatrix} = \begin{vmatrix}
1 & 1 & 0 & 0 & 0 \\
1 & 1 & -1 & 0 & 0 \\
0 & 0 & 1 & 1 & 0 \\
0 & 0 & -1 & 1 & 0 \\
0 & 0 & 0 & 0 & \sqrt{2} \\
\end{vmatrix} \cdot (-1)^2 \\
&= \begin{vmatrix}
1 & 1 & 0 & 0 & 0 \\
0 & [-2] & 0 & 0 & 0 \\
0 & 0 & [1] & 1 & 0 \\
0 & 0 & -1 & 1 & 1 \\
0 & 0 & 0 & 0 & \sqrt{2}
\end{vmathmatrix} \cdot 1 = \begin{vmatrix}
1 & 1 & 0 & 0 & 0 & 0 \\
0 & [-2] & 0 & \sqrt{2} & 0 & 0 \\
0 & 0 & [1] & 1 & \sqrt{2} & 0 \\
0 & 0 & 0 & 0 & [2] & 0 \\
0 & 0 & 0 & 0 & [\sqrt{2}] & 0
\end{vmatrix} \\
&= 1 \cdot (-2) \cdot 1 \cdot 2 \cdot \sqrt{2} = \frac{4 \sqrt{2}}{2}.
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[114, 347, 679, 365]]<|/det|>
4. Spur und Determinante mit Python/Numpy bestimmmen 

<|ref|>text<|/ref|><|det|>[[114, 364, 816, 399]]<|/det|>
Berechnen Sie jeweils Spur und Determinante der Matrizen aus Aufgabe 3 mit Python/Numpy. 

<|ref|>text<|/ref|><|det|>[[114, 415, 142, 431]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[114, 430, 312, 446]]<|/det|>
# Initialisieren 

<|ref|>text<|/ref|><|det|>[[114, 446, 348, 463]]<|/det|>
import numpy as np; 

<|ref|>text<|/ref|><|det|>[[114, 462, 252, 478]]<|/det|>
# Parameter 

<|ref|>text<|/ref|><|det|>[[114, 477, 430, 494]]<|/det|>
A=np.array([[2,3],[4,5]]); 

<|ref|>text<|/ref|><|det|>[[114, 494, 290, 510]]<|/det|>
# Berechnungen 

<|ref|>text<|/ref|><|det|>[[114, 510, 320, 526]]<|/det|>
spur=np.trace(A); 

<|ref|>text<|/ref|><|det|>[[114, 526, 480, 543]]<|/det|>
determinante=np.linalg.det(A); 

<|ref|>text<|/ref|><|det|>[[114, 543, 234, 559]]<|/det|>
# Ausgabe 

<|ref|>text<|/ref|><|det|>[[114, 559, 370, 575]]<|/det|>
print('Spur =', spur); 

<|ref|>text<|/ref|><|det|>[[114, 575, 670, 592]]<|/det|>
print('Determinante =', round(determinante, 3)); 

<|ref|>text<|/ref|><|det|>[[114, 592, 250, 609]]<|/det|>
b) - h) analog 

<|ref|>sub_title<|/ref|><|det|>[[114, 624, 456, 641]]<|/det|>
5. Aussagen über die Determinante 

<|ref|>text<|/ref|><|det|>[[114, 640, 678, 658]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[114, 656, 877, 846]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Die Determinante ist nur für quadratische Matrizen definiert.</td><td>X</td><td></td></tr><tr><td>b) Ob eine quadratische Matrix regulär oder singulär ist, lässt sich nicht nur anhand der Determinante beurteilen.</td><td></td><td>X</td></tr><tr><td>c) Für eine quadratische nxn Matrix A und eine orthogonale nxn Matrix Q gilt: det(QA) = det(A).</td><td>X</td><td></td></tr><tr><td>d) Für quadratische nxn Matrizen A und B gilt: det(A+B) = det(A) + det(B).</td><td></td><td>X</td></tr><tr><td>e) Gilt A = A⁻¹, dann folgt: det(A) ∈ {-1;1}.</td><td>X</td><td></td></tr><tr><td>f) A sei eine schiefsymmetrische nxn Matrix. Für ungerade n gilt: det(A) = 0.</td><td>X</td><td></td></tr></table>