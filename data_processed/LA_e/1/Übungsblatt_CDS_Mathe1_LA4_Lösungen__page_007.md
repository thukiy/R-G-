<|ref|>equation<|/ref|><|det|>[[125, 85, 688, 140]]<|/det|>
\[ \begin{bmatrix} 1 & 1 & 36 \\ 4 & 4 & 5 & 104 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & 1 & 36 \\ 0 & [1] & -40 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & 0 & 76 \\ 0 & [1] & -40 \end{bmatrix}. \]

<|ref|>text<|/ref|><|det|>[[115, 140, 280, 159]]<|/det|>
Rang und Defekt: 

<|ref|>equation<|/ref|><|det|>[[115, 157, 399, 175]]<|/det|>
\[ n_R = 2, n_D = n_V - n_R = 2 - 2 = 0. \]

<|ref|>text<|/ref|><|det|>[[115, 173, 860, 226]]<|/det|>
Pivot-Variablen: m und n und somit gibt es keine freien Parameter. Wir erhalten als Lösungsmenge: L = {(76;-40)}. Da n = -40 gibt es keine Möglichkeit das Restaurant mit Vierertischen und Fünfertischen einzurichten. 

<|ref|>text<|/ref|><|det|>[[115, 225, 150, 243]]<|/det|>
c) 

<|ref|>text<|/ref|><|det|>[[115, 240, 825, 276]]<|/det|>
Wenn das Restaurant aus I Zweier-, m Vierer- und n Fünfertischen eingerichtet werden soll, dann muss gelten: 

<|ref|>equation<|/ref|><|det|>[[115, 273, 250, 291]]<|/det|>
\[ l + m + n = 36 \]

<|ref|>equation<|/ref|><|det|>[[115, 289, 290, 307]]<|/det|>
\[ 2l + 4m + 5n = 104 \]

<|ref|>text<|/ref|><|det|>[[115, 305, 570, 324]]<|/det|>
Mit Hilfe des Gauß-Jordan Verfahrens erhalten wir 

<|ref|>equation<|/ref|><|det|>[[125, 328, 688, 375]]<|/det|>
\[ \begin{bmatrix} 1 & 1 & 36 \\ 2 & 2 & 4 & 5 & 104 \end{bmatrix} \Leftrightarrow \begin{bmatrix}
1 & 1 & 36 \\
0 & [2] & 3 & 32
\end{bmatrix} \Leftrightarrow \begin{bmatrix}
1 & 1 & 36 \\
0 & 1 & 1.5 & 16
\end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[125, 383, 344, 430]]<|/det|>
\[ \Leftrightarrow \begin{bmatrix} 1 & 0 & -0.5 \\ 0 & [1] & 1.5 \end{bmatrix} \begin{bmatrix} 20 \\ 16 \end{bmatrix}. \]

<|ref|>text<|/ref|><|det|>[[115, 433, 280, 451]]<|/det|>
Rang und Defekt: 

<|ref|>equation<|/ref|><|det|>[[115, 449, 395, 468]]<|/det|>
\[ n_R = 2, n_D = n_V - n_R = n_R = 3 - 2 = 1. \]

<|ref|>text<|/ref|><|det|>[[115, 466, 660, 485]]<|/det|>
Pivot-Variablen: I und m und somit ist n ein freier Parameter. 

<|ref|>text<|/ref|><|det|>[[115, 483, 761, 501]]<|/det|>
Durch Ablesen der 2. und 1. Zeile der reduzierten Stufenform ergibt sich 

<|ref|>equation<|/ref|><|det|>[[115, 499, 408, 518]]<|/det|>
\[ m + 1,5n = 16, \Rightarrow m = 16 - 1,5n \]

<|ref|>equation<|/ref|><|det|>[[115, 516, 380, 535]]<|/det|>
\[ l - 0,5n = 20 \Rightarrow l = 20 + 0,5n \]

<|ref|>text<|/ref|><|det|>[[115, 550, 644, 569]]<|/det|>
Wir erhalten als Lösungsmenge: L = {(20+0,5n;16-1,5n;n)}. 

<|ref|>text<|/ref|><|det|>[[115, 567, 880, 635]]<|/det|>
Wir können nun alle möglichen Varianten bestimmen, indem wir beachten, dass jeder der 3 Werte für l, m und n grösser 0 sein muss und dass die Werte für l, m und n ganzzahlig sein müssen. D. h. wir beginnen mit n = 1 und erhöhen dann den Wert von n um jeweils 1 und notieren jede sinnvolle Lösung. 

<|ref|>table<|/ref|><|det|>[[125, 638, 241, 797]]<|/det|>
<table><tr><td>l</td><td>m</td><td>n</td></tr><tr><td>21</td><td>13</td><td>2</td></tr><tr><td>22</td><td>10</td><td>4</td></tr><tr><td>23</td><td>7</td><td>6</td></tr><tr><td>24</td><td>4</td><td>8</td></tr><tr><td>25</td><td>1</td><td>10</td></tr></table>

<|ref|>text<|/ref|><|det|>[[115, 816, 475, 835]]<|/det|>
5. Diskussion von LGS in Stufenform 

<|ref|>equation<|/ref|><|det|>[[115, 832, 250, 868]]<|/det|>
a) \(\begin{bmatrix} 1 & 2 & 3 \\ 0 & 0 & 3 \end{bmatrix} \begin{bmatrix} 4 \\ 6 \end{bmatrix}\)

<|ref|>equation<|/ref|><|det|>[[115, 880, 250, 918]]<|/det|>
c) \(\begin{bmatrix} 1 & 2 & 3 \\ 0 & 3 & 1 \end{bmatrix} \begin{bmatrix} 4 \\ 6 \end{bmatrix}\)

<|ref|>equation
\begin{bmatrix} 1 & 2 & 3 \\ 0 & 0 & 3 \\ 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} 4 \\ 6 \end{bmatrix}\)

<|ref|>equation