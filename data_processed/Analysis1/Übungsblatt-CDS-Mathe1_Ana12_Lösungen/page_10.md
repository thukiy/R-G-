S3 Kandidatenvergl eich: Wir stellen die Ergebnisse in der folgenden Tabelle zusammen.

| $k$ | $x_{k}$ | $L_{k}$ | $B_{k}$ | $H_{k}$ | $A_{k}$ | Typ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | 30.0 cm | 30.0 cm | 15.0 cm | 20.0 cm | $27.0 \mathrm{dm}^{2}$ | globales Minimum |

Die Oberfläche der Kiste ist also genau dann minimal, wenn gilt

$$
\underline{L \approx 30.0 \mathrm{~cm}, \quad B \approx 15.0 \mathrm{~cm} \quad \text { und } \quad H \approx 20.0 \mathrm{~cm}}
$$

b) Wir betrachten eine zylinderförmige Konservendose mit Radius $R$ und Höhe $H$. Aus der Elementargeometrie wissen wir, dass Oberfläche und Volumen eines Kreiszylinders berechnet werden können durch

$$
A=2 \pi R^{2}+2 \pi R H \quad \text { bzw. } \quad V=\pi R^{2} H
$$

Wenn die gesuchte Konservendose genau einen Liter fassen soll, dann muss demnach gelten
$V=\pi R^{2} H=1.001=1.00 \mathrm{dm}^{3}$.
Zunächst formulieren wir die Aufgabe als Optimierungsproblem. Dazu wählen wir

$$
\begin{array}{ll}
x:=R & \text { (unabhängige Variable) } \\
A:=2 \pi R^{2}+2 \pi R H \equiv \text { Oberfläche der Dose } & \text { (zu optimierende Variable). }
\end{array}
$$

Wir drücken nun sämtliche Variablen des Problems durch die unabhängige Variable $x$ aus. Mit Hilfe von (108) erhalten wir

$$
\begin{aligned}
& R(x)=x \\
& H(x)=\frac{V}{\pi R^{2}(x)}=\frac{V}{\pi x^{2}} \\
& A(x)=2 \pi R^{2}(x)+2 \pi R(x) H(x)=2 \pi x^{2}+2 \pi x \frac{V}{\pi x^{2}}=2 \pi x^{2}+\frac{2 V}{x}
\end{aligned}
$$

Der Radius eines Kreiszylinders ist immer positiv, d.h. $R \geq 0$. Weil in (111) und (112) die unabhängige Variable $x$ im Nenner steht, muss sogar gelten

$$
x=R>0
$$

Wir suchen somit das globale Minimum der Funktion $A(x)$ auf dem offenen Intervall

$$
I:=] 0, \infty[
$$

Dabei gehen wir gemäss den folgenden Schritten vor.
S1 Kritische Stellen: Die Ableitung von $A(x)$ ist

$$
A^{\prime}(x)=2 \pi \cdot 2 x^{2-1}+(-1) \cdot \frac{2 V}{x^{1+1}}=4 \pi x-\frac{2 V}{x^{2}}
$$

Wir bestimmen die kritischen Stellen von $A(x)$. Für diese muss gelten

$$
0=A^{\prime}(x)=4 \pi x-\frac{2 V}{x^{2}} \quad+\frac{2 V}{x^{2}}
$$