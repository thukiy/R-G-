S2 Rand stellen: An den Randstellen $x_{0}=0$ und $x_{\mathrm{E}}=U / 2$ hat $A$ die Werte

$$
\begin{aligned}
& A_{0}=A\left(x_{0}\right)=A(0)=0 \cdot\left(\frac{U}{2}-0\right)=0 \cdot \frac{U}{2}=0 \\
& A_{\mathrm{E}}=A\left(x_{\mathrm{E}}\right)=A\left(\frac{U}{2}\right)=\frac{U}{2}\left(\frac{U}{2}-\frac{U}{2}\right)=\frac{U}{2} \cdot 0=0
\end{aligned}
$$

S3 Kandidatenvergl eich: Wir stellen die Ergebnisse in der folgenden Tabelle zusammen.

| $k$ | $x_{k}$ | $A_{k}$ | Typ |
| :--: | :--: | :--: | :-- |
| 0 | 0 | 0 | globales Minimum |
| 1 | $U / 4$ | $U^{2} / 16$ | globales Maximum |
| E | $U / 2$ | 0 | globales Minimum |

Ein Rechteck mit Umfang $U>0$ hat also gerade dann die maximale Fläche, wenn gilt
$\underline{a}=x_{1}=\underline{\underline{4}}$
$\underline{b}=\frac{U}{2}-a=\frac{U}{2}-\frac{U}{4}=\underline{\underline{4}}=a$
$\underline{A}=\underline{\frac{U^{2}}{16}}$

Dies beschreibt gerade das Quadrat mit Umfang $U$ und Seitenlänge $l=U / 4$.

# 6. Optimale Verpackungen 

Wir bestimmen jeweils die optimalen geometrischen Abmessungen (Länge, Breite, Höhe, Radius, etc..), so dass die angegebene Verpackung mit möglichst wenig Material hergestellt werden kann.
a) Wir betrachten eine quaderförmige Kiste mit Länge $L$, Breite $B$ und Höhe $H$, die ein Volumen fasst von
$V=L B H=9.001=9.00 \mathrm{dm}^{3}$.
Ihre rechteckige Grundfläche sei doppelt so lang wie breit, d.h. es gilt
$L=2 B$.
Zunächst formulieren wir die Aufgabe als Optimierungsproblem. Dazu wählen wir

$$
\begin{array}{ll}
x:=L & \text { (unabhängige Variable) } \\
A: \equiv \text { Oberfläche der Kiste } & \text { (zu optimierende Variable). }
\end{array}
$$

Wir drücken nun sämtliche Variablen des Problems durch die unabhängige Variable $x$ aus. Mit Hilfe von (86) und (87) erhalten wir

$$
L(x)=x
$$