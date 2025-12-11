<|ref|>text<|/ref|><|det|>[[115, 81, 308, 99]]<|/det|>
Mit Gauß-Verfahren: 

<|ref|>equation<|/ref|><|det|>[[179, 103, 640, 169]]<|/det|>
\[
\begin{pmatrix}
r & 1 & 1 \\
1 & r & 1 \\
1 & 1 & r
\end{pmatrix}
\rightarrow
\begin{pmatrix}
0 & 1-r^2 & 1-r \\
1 & r & 1 \\
0 & 1-r & r-1
\end{pmatrix}
\begin{pmatrix}
1-r \\
1 \\
0
\end{pmatrix}
\]

<|ref|>text<|/ref|><|det|>[[125, 183, 699, 239]]<|/det|>
1. Fall: \(r = 1\). In diesem Fall kann man die Lösungsmenge direkt ablesen: \(L = \{(1-s-t, s, t) | s, t \in \mathbb{R}\}\) (das sind unendlich viele Lösungen). 

<|ref|>text<|/ref|><|det|>[[125, 247, 699, 305]]<|/det|>
2. Fall: \(r \neq 1\). Wir führen einen weiteren Eliminationsschritt durch. Hierbei multiplizieren wir die erste und die dritte Zeile mit \(\frac{1}{1-r}\) und erhalten: 

<|ref|>equation<|/ref|><|det|>[[191, 321, 630, 387]]<|/det|>
\[
\begin{pmatrix}
0 & 1+r & 1 \\
1 & r & 1 \\
0 & 1 & -1
\end{pmatrix}
\rightarrow
\begin{pmatrix}
1 & r & 1 \\
0 & 1 & -1 \\
0 & 0 & 2+r
\end{pmatrix}
\begin{pmatrix}
1 \\
0 \\
1
\end{pmatrix}
\]

<|ref|>text<|/ref|><|det|>[[125, 401, 457, 420]]<|/det|>
Im Fall \(r = -2\) gilt offenbar \(L = \emptyset\). 

<|ref|>text<|/ref|><|det|>[[125, 429, 697, 470]]<|/det|>
Und im Fall \(r \neq -2\) gibt es offenbar genau eine Lösung. Es ist
\(L = \{(\frac{1}{2+r}, \frac{1}{2+r}, \frac{1}{2+r})\}\) die Lösungsmenge. 

<|ref|>sub_title<|/ref|><|det|>[[115, 488, 592, 506]]<|/det|>
10. Lineare Gleichungssysteme mit Python lösen 

<|ref|>text<|/ref|><|det|>[[115, 505, 747, 540]]<|/det|>
a) Lösen Sie die linearen Gleichungssystem aus Aufgabe 3 und 5 mit Python/Numpy. 

<|ref|>text<|/ref|><|det|>[[115, 538, 747, 574]]<|/det|>
b) Lösen Sie die linearen Gleichungssystem aus Aufgabe 3 und 5 mit
Python/Sympy. 

<|ref|>text<|/ref|><|det|>[[115, 587, 525, 605]]<|/det|>
a) Lösung für Aufgabe 3a) (b) und c) analog). 

<|ref|>text<|/ref|><|det|>[[115, 604, 225, 621]]<|/det|>
Mit Numpy: 

<|ref|>text<|/ref|><|det|>[[115, 620, 400, 636]]<|/det|>
# Python initialisieren 

<|ref|>text<|/ref|><|det|>[[115, 636, 352, 653]]<|/det|>
import numpy as np; 

<|ref|>text<|/ref|><|det|>[[115, 653, 260, 668]]<|/det|>
# Parameter 

<|ref|>text<|/ref|><|det|>[[115, 668, 852, 720]]<|/det|>
A=np.array([[2,-1],[-1,2]]); → Variablen auf die linke Seite bringen und sortieren, dann erste Zeile in eckige Klammern, anschliessend zweite Zeile in eckige Klammern 

<|ref|>text<|/ref|><|det|>[[115, 719, 520, 737]]<|/det|>
b=np.array([1,7]); → rechte Seite 

<|ref|>text<|/ref|><|det|>[[115, 736, 206, 752]]<|/det|>
pr_L=3; 

<|ref|>text<|/ref|><|det|>[[115, 752, 293, 768]]<|/det|>
# Berechnungen 

<|ref|>text<|/ref|><|det|>[[115, 768, 830, 785]]<|/det|>
L=np.linalg.solve(A,b); → lineares Gleichungssystem wird gelöst 

<|ref|>text<|/ref|><|det|>[[115, 784, 238, 801]]<|/det|>
# Ausgabe 

<|ref|>text<|/ref|><|det|>[[115, 801, 700, 819]]<|/det|>
print(f"L={np.array2string(L,precision=pr_L)}"); 

<|ref|>text<|/ref|><|det|>[[115, 834, 500, 852]]<|/det|>
Lösung für Aufgabe 5a) (b) und c) analog). 

<|ref|>text<|/ref|><|det|>[[115, 851, 400, 867]]<|/det|>
# Python initialisieren 

<|ref|>text<|/ref|><|det|>[[115, 867, 352, 883]]<|/det|>
import numpy as np; 

<|ref|>text<|/ref|><|det|>[[115, 883, 260, 899]]<|/det|>
# Parameter 

<|ref|>text<|/ref|><|det|>[[115, 899, 625, 916]]<|/det|>
A=np.array([[2,-3,1],[-1,3,-2],[3,-1,5]]);