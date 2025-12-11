<|ref|>equation<|/ref|><|det|>[[303, 81, 737, 152]]<|/det|>
\[
\begin{align*}
3y &= 9 \Rightarrow y = \frac{9}{3} = 3 \\
2x + 5y &= 8 \Rightarrow x = \frac{8 - 5y}{2} = \frac{8 - 5 \cdot 3}{2} = \frac{-7}{2} = -3.5.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[117, 160, 308, 178]]<|/det|>
Die Lösungsmenge ist 

<|ref|>equation<|/ref|><|det|>[[415, 191, 577, 213]]<|/det|>
\[
\mathbb{L} = \{(-3.5; 3)\}.
\]

<|ref|>sub_title<|/ref|><|det|>[[114, 233, 371, 250]]<|/det|>
3. Aussagen über ein LGS 

<|ref|>text<|/ref|><|det|>[[114, 250, 408, 268]]<|/det|>
Gegeben sei das folgende LGS: 

<|ref|>equation<|/ref|><|det|>[[114, 268, 198, 285]]<|/det|>
\(x + y = 0\)

<|ref|>equation<|/ref|><|det|>[[114, 285, 198, 302]]<|/det|>
\(x - y = 0\).

<|ref|>text<|/ref|><|det|>[[114, 308, 680, 326]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[114, 324, 880, 444]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Es gilt \(n_G = n_V\).</td><td>X</td><td></td></tr><tr><td>b) Um das LGS in die Stufenform zu bringen, braucht es 2 Gauß-Schritte.</td><td></td><td>X</td></tr><tr><td>c) Der Rang des LGS beträgt 2.</td><td>X</td><td></td></tr><tr><td>d) Das LGS hat unendlich viele Lösungen.</td><td></td><td>X</td></tr><tr><td>e) Die Variable y ist eine Pivot-Variable.</td><td>X</td><td></td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[114, 460, 250, 477]]<|/det|>
4. Restaurant 

<|ref|>text<|/ref|><|det|>[[114, 476, 825, 494]]<|/det|>
In einem Restaurant sollen an 36 Tischen 104 Sitzplätze zur Verfügung stehen. 

<|ref|>text<|/ref|><|det|>[[114, 493, 686, 511]]<|/det|>
a) Mit wie vielen Zweier- und Vierertischen wäre dies möglich? 

<|ref|>text<|/ref|><|det|>[[114, 510, 795, 544]]<|/det|>
b) Wäre es auch möglich, das Restaurant nur mit Vierer- und Fünfertischen einzurichten? 

<|ref|>text<|/ref|><|det|>[[114, 543, 850, 577]]<|/det|>
c) Wie viele und welche Varianten gibt es, das Restaurant mit Zweier-, Vierer und Fünfertischen einzurichten? 

<|ref|>text<|/ref|><|det|>[[114, 593, 141, 609]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[114, 608, 848, 642]]<|/det|>
Wenn das Restaurant aus m Zweier- und n Vierertischen eingerichtet werden soll, dann muss gelten: 

<|ref|>equation<|/ref|><|det|>[[114, 640, 214, 657]]<|/det|>
\(m + n = 36\)

<|ref|>equation<|/ref|><|det|>[[114, 656, 250, 673]]<|/det|>
\(2m + 4n = 104\)

<|ref|>text<|/ref|><|det|>[[114, 673, 570, 691]]<|/det|>
Mit Hilfe des Gauß-Jordan Verfahrens erhalten wir 

<|ref|>equation<|/ref|><|det|>[[124, 696, 690, 743]]<|/det|>
\[
\begin{bmatrix}
1 & 1 & 36 \\
2 & 4 & 104
\end{bmatrix}
\Leftrightarrow
\begin{bmatrix}
1 & 1 & 36 \\
1 & 2 & 52
\end{bmatrix}
\Leftrightarrow
\begin{bmatrix}
1 & 1 & 36 \\
0 & [1] & 16
\end{bmatrix}
\Leftrightarrow
\begin{bmatrix}
1 & 0 & 20 \\
0 & [1] & 16
\end{bmatrix}.
\]

<|ref|>text<|/ref|><|det|>[[114, 748, 280, 765]]<|/det|>
Rang und Defekt: 

<|ref|>equation<|/ref|><|det|>[[114, 764, 395, 782]]<|/det|>
\(n_R = 2, n_D = n_V - n_R = 2 - 2 = 0\).

<|ref|>text<|/ref|><|det|>[[114, 780, 870, 831]]<|/det|>
Pivot-Variablen: m und n und somit gibt es keine freien Parameter. Wir erhalten als Lösungsmenge: L = {(20;16)}. Somit lässt sich das Restaurant mit 20 Zweier- und 16 Vierertischen einrichten. 

<|ref|>text<|/ref|><|det|>[[114, 830, 144, 847]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[114, 846, 844, 880]]<|/det|>
Wenn das Restaurant aus m Vierer- und n Fünfertischen eingerichtet werden soll, dann muss gelten: 

<|ref|>equation<|/ref|><|det|>[[1142, 880, 214, 896]]<|/det|>
\(m + n = 36\)

<|ref|>equation<|/ref|><|det|>[[114, 896, 250, 913]]<|/det|>
\(4m + 5n = 104\)

<|ref|>text<|/ref|><|det|>[[114, 912, 570, 930]]<|/det|>
Mit Hilfe des Gauß-Jordan Verfahrens erhalten wir