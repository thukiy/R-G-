<|ref|>text<|/ref|><|det|>[[114, 81, 878, 150]]<|/det|>
Für die zu berechnenden Mengen verwenden wir entsprechend den
Gerätebezeichnungen A, B und C. Für die Montagezeit ergibt sich: 45*60 min = 2700
min, für die Prüfzeit: 10*60 min = 600 min und für die Stellplätze: 240. Daraus
erhalten wir die folgenden Gleichungen und somit das LGS: 

<|ref|>equation<|/ref|><|det|>[[257, 163, 636, 220]]<|/det|>
\[
\begin{align*}
(1) \quad & A + 2B + 2C = 240 \quad \text{Stellplätze} \\
(2) \quad & 4A + 2B + 6C = 600 \quad \text{Prüfzeit} \\
(3) \quad & 20A + 10B + 20C = 2700 \quad \text{Montagezeit}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 226, 417, 243]]<|/det|>
Das Gauß-Rechenschema hierzu lautet: 

<|ref|>equation<|/ref|><|det|>[[241, 252, 647, 444]]<|/det|>
\[
\begin{array}{cccc}
(1) & 1 & 2 & 2 \\
(2) & 4 & 2 & 6 \\
(3) & 20 & 10 & 20 \\
(1) & 1 & 2 & 2 \\
(2) & 0 & -6 & -2 \\
(3) & 0 & -30 & -20 \\
(1) & 1 & 2 & 2 \\
(2) & -6 & -2 & -2 \\
(3) & 0 & 0 & -10 \\
\end{array}
\quad \begin{array}{c}
240 \\
600 \\
2700 \\
240 \\
-360 \\
-2100 \\
240 \\
-360 \\
-300 \\
\end{array}
\quad \begin{array}{c}
-4 \cdot (1) \\
-20 \cdot (1) \\
\end{array}
\]

<|ref|>text<|/ref|><|det|>[[117, 448, 510, 466]]<|/det|>
und es liefert die Lösung \(C = 30\), \(B = 50\), \(A = 80\). 

<|ref|>sub_title<|/ref|><|det|>[[114, 481, 504, 499]]<|/det|>
3. Lösen von LGS mit Hilfe von Matrizen 

<|ref|>text<|/ref|><|det|>[[114, 498, 551, 516]]<|/det|>
a) Schreiben Sie das lineare Gleichungssystem 

<|ref|>equation<|/ref|><|det|>[[402, 515, 620, 533]]<|/det|>
\[
x_1 + 3x_2 + 2x_3 = 1
\]

<|ref|>equation<|/ref|><|det|>[[402, 532, 620, 550]]<|/det|>
\[
-2x_1 - 4x_2 - 3x_3 = -3
\]

<|ref|>equation<|/ref|><|det|>[[402, 548, 585, 566]]<|/det|>
\[
3x_1 + 8x_2 + 5x_3 = 2
\]

<|ref|>text<|/ref|><|det|>[[144, 565, 840, 583]]<|/det|>
als Matrixprodukt und berechnen Sie die Lösung mit Hilfe der inversen Matrix. 

<|ref|>text<|/ref|><|det|>[[114, 583, 864, 618]]<|/det|>
b) Für ein LGS in Matrixform \(A \cdot \vec{x} = \vec{b}\) sind zu den folgenden rechten Seiten bereits Lösungen bekannt: 

<|ref|>equation<|/ref|><|det|>[[144, 616, 666, 666]]<|/det|>
\[
\vec{b} = \vec{e}_1: \vec{x}_1 = \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}, \quad \vec{b} = \vec{e}_2: \vec{x}_2 = \begin{pmatrix} -6 \\ 2 \\ 7 \end{pmatrix}, \quad \vec{b} = \vec{e}_3: \vec{x}_3 = \begin{pmatrix} -4 \\ 1 \\ -5 \end{pmatrix}.
\]

<|ref|>text<|/ref|><|det|>[[144, 663, 680, 681]]<|/det|>
Bestimmen Sie mit diesen 3 Vektoren die Lösung zum LGS 

<|ref|>equation<|/ref|><|det|>[[144, 679, 272, 725]]<|/det|>
\[
A \cdot \vec{x} = \begin{pmatrix} 2 \\ 3 \\ -5 \end{pmatrix}.
\]

<|ref|>text<|/ref|><|det|>[[114, 725, 340, 743]]<|/det|>
c) Zu lösen ist das LGS 

<|ref|>equation<|/ref|><|det|>[[144, 742, 280, 792]]<|/det|>
\[
\begin{align*}
x_1 - 2x_3 &= 3 \\
-2x_2 + x_3 &= 3 \\
-2x_1 + x_2 &= 3.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[144, 791, 760, 826]]<|/det|>
Geben Sie das LGS in Matrixform an. Berechnen Sie die Inverse der
Koeffizientenmatrix und bestimmen Sie damit die Lösung des LGS.