a) Wenn die Türe quadratisch sein soll, dann muss gelten

$$
\begin{aligned}
b & =h=c-\frac{a}{4} \cdot b^{2} & & -c+\frac{a}{4} \cdot b^{2} \\
\Leftrightarrow \quad \frac{a}{4} \cdot b^{2}+b-c & =0 & & |\mathrm{MF} .
\end{aligned}
$$

Mit Hilfe der Mitternachtsformel zur Lösung von quadratischen Gleichungen erhalten wir

$$
\begin{aligned}
b_{1,2} & =\frac{-1 \pm \sqrt{1-4 \cdot \frac{a}{4} \cdot(-c)}}{2 \cdot \frac{a}{4}}=\frac{-1 \pm \sqrt{1+a c}}{\frac{a}{2}}=\frac{2}{a} \cdot(-1 \pm \sqrt{1+a c}) \\
& \approx \frac{2}{\frac{4.00}{9.00 \mathrm{~m}}} \cdot\left(-1 \pm \sqrt{1+\frac{4.00}{9.00 \mathrm{~m}} \cdot 4.00 \mathrm{~m}}\right)=\frac{2 \cdot 9.00 \mathrm{~m}}{4.00} \cdot\left(-1 \pm \sqrt{\frac{9.00+16.0}{9.00}}\right) \\
& =4.50 \mathrm{~m} \cdot\left(-1 \pm \sqrt{\frac{25.0}{9.00}}\right)=4.50 \mathrm{~m} \cdot\left(-1 \pm \frac{5.00}{3.00}\right)
\end{aligned}
$$

Die beiden Lösungen sind demnach

$$
\begin{aligned}
& b_{1}=4.50 \mathrm{~m} \cdot\left(-1-\frac{5.00}{3.00}\right)=4.50 \mathrm{~m} \cdot\left(-\frac{8.00}{3.00}\right)=-12.0 \mathrm{~m} \\
& b_{2}=4.50 \mathrm{~m} \cdot\left(-1+\frac{5.00}{3.00}\right)=4.50 \mathrm{~m} \cdot\left(\frac{2.00}{3.00}\right)=3.00 \mathrm{~m}
\end{aligned}
$$

Weil Breite und Höhe der Türe beide positiv sein müssen, finden wir

$$
\underline{h}=b \approx 3.00 \mathrm{~m}
$$

b) Die Türe soll die maximal mögliche Fläche haben. Zunächst formulieren wir die Aufgabe als Optimierungsproblem. Dazu wählen wir

$$
z:=b \quad \text { (unabhängige Variable) }
$$

$A: \equiv$ Fläche der Türe (zu optimierende Variable).
Wir drücken nun die Variablen $b, h$ und $A$ durch die unabhängige Variable $z$ aus. Mit Hilfe von (77) erhalten wir

$$
\begin{aligned}
& b(z)=z \\
& h(z)=c-\frac{a}{4} \cdot b^{2}(z)=c-\frac{a}{4} \cdot z^{2} \\
& A(z)=b(z) \cdot h(z)=z \cdot h(z)=z \cdot\left(c-\frac{a}{4} \cdot z^{2}\right)=c \cdot z-\frac{a}{4} \cdot z^{3}
\end{aligned}
$$

Weil die Türe innerhalb des Torbogens gebaut werden soll, muss gelten

$$
0 \leq z \leq 6.00 \mathrm{~m}
$$

Wir suchen somit das globale Maximum der Funktion $A(z)$ auf dem geschlossenen Interval 1

$$
I:=\left[z_{0}, z_{\mathrm{E}}\right]=[0,6.00 \mathrm{~m}]
$$

Dabei gehen wir gemäss den folgenden drei Schritten vor.