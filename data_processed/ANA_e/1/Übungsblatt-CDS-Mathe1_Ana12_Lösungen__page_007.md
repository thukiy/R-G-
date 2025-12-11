<|ref|>text<|/ref|><|det|>[[108, 66, 454, 84]]<|/det|>
5. Maximierung einer Rechteck-Fläche 

<|ref|>text<|/ref|><|det|>[[108, 83, 925, 137]]<|/det|>
Wir betrachten ein Rechteck mit Umfang \(U > 0\) und suchen die Seiten \(a\) und \(b\) derart, dass die Fläche des Rechtecks maximal wird. Zunächst formulieren wir die Aufgabe als Optimierungsproblem. Dazu wählen wir 

<|ref|>equation<|/ref|><|det|>[[118, 147, 923, 190]]<|/det|>
\[
\begin{align*}
x &:= a \tag{unabhängige Variable} \\
A &:= \text{Fläche des Rechtecks} \quad (\text{zu optimierende Variable}). \tag{69}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[108, 200, 641, 219]]<|/det|>
Aus der Elementargeometrie kennen wir die Zusammenhänge 

<|ref|>equation<|/ref|><|det|>[[114, 229, 923, 270]]<|/det|>
\[
\begin{align*} U &= 2 \cdot (a + b) \tag{70} \\ A &= ab. \end{align*}
\]

<|ref|>text<|/ref|><|det|>[[108, 283, 925, 319]]<|/det|>
Mit Hilfe dieser Informationen können wir die Variablen \(a\), \(b\) und \(A\) durch die unabhängige Variable \(x\) und die gegebene Konstante \(U\) ausdrücken. Wir erhalten 

<|ref|>equation<|/ref|><|det|>[[108, 331, 923, 435]]<|/det|>
\[
\begin{align*} a(x) &= x \tag{71} \\ b(x) &= \frac{U}{2} - a = \frac{U}{2} - x \tag{72} \\ A(x) &= ab = x \cdot \left(\frac{U}{2} - x\right) = \frac{U}{2} x - x^2. \tag{73} \end{align*}
\]

<|ref|>text<|/ref|><|det|>[[108, 446, 680, 464]]<|/det|>
Die Seiten eines Rechtecks sind immer positiv, d.h. es muss gelten 

<|ref|>equation<|/ref|><|det|>[[403, 473, 923, 508]]<|/det|>
\[
a, b \ge 0 \Leftrightarrow 0 \le x \le \frac{U}{2}. \quad (74)
\]

<|ref|>text<|/ref|><|det|>[[108, 517, 900, 536]]<|/det|>
Wir suchen somit das globale Maximum der Funktion \(A(x)\) auf dem geschlossenen Intervall 

<|ref|>equation<|/ref|><|det|>[[403, 547, 923, 569]]<|/det|>
\[
I := [x_0, x_E] = [0, U/2]. \quad (75)
\]

<|ref|>text<|/ref|><|det|>[[108, 580, 570, 598]]<|/det|>
Dabei gehen wir gemäss den folgenden Schritten vor. 

<|ref|>text<|/ref|><|det|>[[108, 602, 688, 621]]<|/det|>
S1 Kritische Stellen: Für die erste Ableitung von A erhalten wir 

<|ref|>equation<|/ref|><|det|>[[150, 631, 923, 666]]<|/det|>
\[
A'(x) = \frac{U}{2} \cdot 1 - 2x^{2-1} = \frac{U}{2} - 2x. \quad (76)
\]

<|ref|>text<|/ref|><|det|>[[150, 675, 660, 693]]<|/det|>
Da \(A'\) linear ist, hat \(A\) höchstens eine kritische Stelle. Aus 

<|ref|>equation<|/ref|><|det|>[[422, 704, 923, 779]]<|/det|>
\[
\begin{align*} 0 &= A'(x) = \frac{U}{2} - 2x \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \mid + 2x \tag{77} \\ 2x &= \frac{U}{2} \quad \quad \quad \quad \quad \quad \quad \quad \quad \qquad \mid : 2 \tag{78} \end{align*}
\]

<|ref|>text<|/ref|><|det|>[[150, 787, 262, 803]]<|/det|>
erhalten wir 

<|ref|>equation<|/ref|><|det|>[[491, 812, 923, 846]]<|/det|>
\[
x_1 = \frac{U}{4}. \quad (79)
\]

<|ref|>text<|/ref|><|det|>[[150, 855, 392, 872]]<|/det|>
Ferner finden wir den Wert 

<|ref|>equation<|/ref|><|det|>[[150, 880, 923, 919]]<|/det|>
\[
A_1 = A(x_1) = A\left(\frac{U}{4}\right) = \frac{U}{4}\left(\frac{U}{2} - \frac{U}{4}\right) = \frac{U}{4} \cdot \frac{U}{4} = \frac{U^2}{16}. \quad (80)
\]