# 5. Maximierung einer Rechteck-Fläche 

Wir betrachten ein Rechteck mit Umfang $U>0$ und suchen die Seiten $a$ und $b$ derart, dass die Fläche des Rechtecks maximal wird. Zunächst formulieren wir die Aufgabe als Optimierungsproblem. Dazu wählen wir

$$
\begin{array}{ll}
x:=a & \text { (unabhängige Variable) } \\
A: \equiv \text { Fläche des Rechtecks } & \text { (zu optimierende Variable). }
\end{array}
$$

Aus der Elementargeometrie kennen wir die Zusammenhänge

$$
\begin{aligned}
& U=2 \cdot(a+b) \\
& A=a b .
\end{aligned}
$$

Mit Hilfe dieser Informationen können wir die Variablen $a, b$ und $A$ durch die unabhängige Variable $x$ und die gegebene Konstante $U$ ausdrücken. Wir erhalten

$$
\begin{aligned}
& a(x)=x \\
& b(x)=\frac{U}{2}-a=\frac{U}{2}-x \\
& A(x)=a b=x \cdot\left(\frac{U}{2}-x\right)=\frac{U}{2} x-x^{2}
\end{aligned}
$$

Die Seiten eines Rechtecks sind immer positiv, d.h. es muss gelten

$$
a, b \geq 0 \Leftrightarrow 0 \leq x \leq \frac{U}{2}
$$

Wir suchen somit das globale Maximum der Funktion $A(x)$ auf dem geschlossenen Intervall

$$
I:=\left[x_{0}, x_{\mathrm{E}}\right]=[0, U / 2]
$$

Dabei gehen wir gemäss den folgenden Schritten vor.
S1 Kritische Stellen: Für die erste Ableitung von $A$ erhalten wir

$$
A^{\prime}(x)=\frac{U}{2} \cdot 1-2 x^{2-1}=\frac{U}{2}-2 x
$$

Da $A^{\prime}$ linear ist, hat $A$ höchstens eine kritische Stelle. Aus

$$
\begin{aligned}
0 & =A^{\prime}(x)=\frac{U}{2}-2 x & & +2 x \\
2 x & =\frac{U}{2} & & 2
\end{aligned}
$$

erhalten wir

$$
x_{1}=\frac{U}{4}
$$

Ferner finden wir den Wert

$$
A_{1}=A\left(x_{1}\right)=A\left(\frac{U}{4}\right)=\frac{U}{4}\left(\frac{U}{2}-\frac{U}{4}\right)=\frac{U}{4} \cdot \frac{U}{4}=\frac{U^{2}}{16}
$$