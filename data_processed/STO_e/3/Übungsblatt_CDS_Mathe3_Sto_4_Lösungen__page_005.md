<|ref|>text<|/ref|><|det|>[[114, 82, 145, 100]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[125, 99, 712, 117]]<|/det|>
\[
\phi(a) = 0,3210 < 0,5 \quad \Rightarrow \quad a < 0 \quad (\text{Wir setzen } a = -k \text{ mit } k > 0) \quad \Rightarrow
\]

<|ref|>equation<|/ref|><|det|>[[125, 118, 642, 137]]<|/det|>
\[
\phi(a) = \phi(-k) = 1 - \phi(k) = 0,3210 \quad \Rightarrow \quad \phi(k) = 0,6790 \quad \Rightarrow
\]

<|ref|>equation<|/ref|><|det|>[[125, 138, 419, 156]]<|/det|>
\[
k = 0,465 \quad \Rightarrow \quad a = -k = -0,465
\]

<|ref|>text<|/ref|><|det|>[[114, 155, 145, 173]]<|/det|>
b) 

<|ref|>equation<|/ref|><|det|>[[125, 171, 699, 212]]<|/det|>
\[
\phi(b) - \phi(-0,22) = \phi(b) - 1 + \phi(0,22) = \phi(b) - 1 + 0,5871 = \\
= \phi(b) - 0,4129 = 0,413 \quad \Rightarrow \quad \phi(b) = 0,8259 \quad \Rightarrow \quad b = 0,938
\]

<|ref|>text<|/ref|><|det|>[[114, 212, 145, 230]]<|/det|>
c) 

<|ref|>equation<|/ref|><|det|>[[117, 229, 697, 305]]<|/det|>
\[
\begin{align*}
P(U \ge a) &= 1 - P(U \le a) = 1 - \phi(a) = 0,8002 \quad \Rightarrow \\
\phi(a) &= 0,1998 < 0,5 \quad \Rightarrow \quad a < 0 \quad (\text{Wir setzen } a = -k \text{ mit } k > 0) \quad \\
\phi(a) &= \phi(-k) = 1 - \phi(k) = 0,1998 \quad \Rightarrow \quad \phi(k) = 0,8002 \quad \Rightarrow \\
k &= 0,842 \quad \Rightarrow \quad a = -k = -0,842
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[114, 318, 418, 336]]<|/det|>
9. Standardnormalverteilung III 

<|ref|>text<|/ref|><|det|>[[114, 335, 848, 373]]<|/det|>
Die Zufallsvariable X sei normalverteilt mit Mittelwert μ = 40 und Varianz σ² = 100.
Bestimmen Sie die folgenden Werte: 

<|ref|>equation<|/ref|><|det|>[[114, 370, 750, 390]]<|/det|>
\[
\text{a) } P(X \le 55) \qquad \text{b) } P(X \le 28) \qquad \text{c) } P(28 \le X \le 55)
\]

<|ref|>text<|/ref|><|det|>[[114, 386, 550, 405]]<|/det|>
d) Bestimmen Sie das 95% und das 5% Quantil. 

<|ref|>text<|/ref|><|det|>[[114, 420, 145, 438]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[117, 437, 543, 465]]<|/det|>
\[
P(X \le 55) = P\left(\frac{X-40}{10} \le \frac{55-40}{10}\right) = \Phi(1.5) = 0,9332
\]

<|ref|>text<|/ref|><|det|>[[114, 461, 145, 479]]<|/det|>
b) 

<|ref|>equation<|/ref|><|det|>[[117, 479, 512, 524]]<|/det|>
\[
\begin{align*}
P(X \le 28) &= P\left(\frac{X-40}{10} \le \frac{28-40}{10}\right) = \Phi(-1.2) \\
&= 1 - \Phi(1.2) = 1 - 0,8849 = 0,1151
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 523, 145, 541]]<|/det|>
c) 

<|ref|>equation<|/ref|><|det|>[[114, 540, 660, 580]]<|/det|>
\[
\begin{align*}
P(28 < X \le 55) &= P(X \le 55) - P(X \le 28) \\
&= \Phi(1.5) - \Phi(-1.2) = 0,9332 - 0,1151 = 0,8181
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 579, 145, 597]]<|/det|>
d) 

<|ref|>text<|/ref|><|det|>[[117, 595, 840, 673]]<|/det|>
Der Wert 0,95 befindet sich in der Tabelle zwischen 1,64 und 1,65, sodass
das 95%-Quantil der Standardnormalverteilung mit 1,645 angegeben werden
kann. Der Wert für das 5%-Quantil der Standardnormalverteilung ist wegen
Φ(-z) = 1 - Φ(z) = 0,05 ⇔ Φ(z) = 0,95 bei z = -1,645. 

<|ref|>text<|/ref|><|det|>[[114, 668, 840, 750]]<|/det|>
Da die transformierte Zufallsvariable Z = X - 40/10 standardnormalverteilt ist, muss
x - 40/10 = 1,645 nach x aufgelöst werden, um das 95%-Quantil von X zu bestimmen. Das 95%-Quantil ist somit x = 10 · 1,645 + 40 = 56,45. Analog ergibt sich das 5%-Quantil von X aus x = 10 · (-1,645) + 40 = 23,55. 

<|ref|>text<|/ref|><|det|>[[117, 747, 664, 767]]<|/det|>
Dieses Ergebnis kann folgendermaßen interpretiert werden: 

<|ref|>text<|/ref|><|det|>[[117, 766, 845, 845]]<|/det|>
Bei einer N(40, 100)-normalverteilten Zufallsvariablen X ist das Ergebnis mit einer Wahrscheinlichkeit von 5% höchstens 23,55 und mit der Wahrscheinlichkeit von 95% höchstens 56,45. Das bedeutet auch, dass das Ergebnis mit 90%-iger Wahrscheinlichkeit im Intervall [23,55; 56,45] um den Erwartungswert 40 liegt.