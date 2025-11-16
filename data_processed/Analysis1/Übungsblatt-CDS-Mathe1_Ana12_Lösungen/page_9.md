$$
\begin{aligned}
B(x) & =\frac{L(x)}{2}=\frac{x}{2} \\
H(x) & =\frac{V}{L(x) B(x)}=\frac{V}{x \cdot \frac{x}{2}}=\frac{2 V}{x^{2}} \\
A(x) & =2 L(x) \cdot B(x)+2 L(x) \cdot H(x)+2 B(x) \cdot H(x) \\
& =2 \cdot x \cdot \frac{x}{2}+2 \cdot x \cdot \frac{2 V}{x^{2}}+2 \cdot \frac{x}{2} \cdot \frac{2 V}{x^{2}}=x^{2}+\frac{4 V}{x}+\frac{2 V}{x}=x^{2}+\frac{6 V}{x}
\end{aligned}
$$

Die Kanten eines Quaders sind immer positiv, d.h. $L \geq 0$. Weil in (91) und (92) die unabhängige Variable $x$ im Nenner steht, muss sogar gelten

$$
x=L>0
$$

Wir suchen somit das globale Minimum der Funktion $A(x)$ auf dem offenen Intervall

$$
I:=] 0, \infty[
$$

Dabei gehen wir gemäss den folgenden Schritten vor.
S1 Kritische Stellen: Die Ableitung von $A(x)$ ist

$$
A^{\prime}(x)=2 x^{2-1}+(-1) \cdot \frac{6 V}{x^{1+1}}=2 x-\frac{6 V}{x^{2}}
$$

Wir bestimmen die kritischen Stellen von $A(x)$. Für diese muss gelten

$$
\begin{array}{rlr} 
& 0=A^{\prime}(x)=2 x-\frac{6 V}{x^{2}} & \left\lvert\,+\frac{6 V}{x^{2}}\right. & \\
\Leftrightarrow & \frac{6 V}{x^{2}}=2 x & \left\lvert\, \frac{x^{2}}{2}\right. & \\
\Leftrightarrow & \frac{6 V}{x^{2}} \cdot \frac{x^{2}}{2}=3 V=x^{3} & \mid \sqrt[3]{\cdots} . & (98)
\end{array}
$$

Daraus erhalten wir genau eine kritische Stelle von $A(x)$, nämlich

$$
x_{1}=\sqrt[3]{3 V}
$$

Ferner berechnen wir gemäss (89) bis (92) die Werte

$$
\begin{aligned}
& L_{1}=L\left(x_{1}\right)=x_{1}=\sqrt[3]{3 V} \approx \sqrt[3]{3 \cdot 9.00 \mathrm{dm}^{3}}=\sqrt[3]{27 \mathrm{dm}^{3}}=3.00 \mathrm{dm}=30.0 \mathrm{~cm} \\
& B_{1}=B\left(x_{1}\right)=\frac{x_{1}}{2}=\frac{L}{2} \approx \frac{1}{2} \cdot 3.00 \mathrm{dm}=1.50 \mathrm{dm}=15.0 \mathrm{~cm} \\
& H_{1}=H\left(x_{1}\right)=\frac{2 V}{x_{1}^{2}}=\frac{2 V}{L^{2}} \approx 2 \cdot \frac{9.00 \mathrm{dm}^{3}}{(3.00 \mathrm{dm})^{2}}=2.00 \mathrm{dm}=20.0 \mathrm{~cm} \\
& A_{1}=A\left(x_{1}\right)=x_{1}^{2}+\frac{6 V}{x_{1}} \approx(3.00 \mathrm{dm})^{2}+\frac{6 \cdot 9.00 \mathrm{dm}^{3}}{3.00 \mathrm{dm}}=27.0 \mathrm{dm}^{2}
\end{aligned}
$$

S2 Rand stellen: Das offene Intervall $I$ hat keine Randstellen, es gilt jedoch

$$
A(x)=x^{2}+\frac{6 V}{x} \xrightarrow{x \rightarrow 0} \infty \quad \text { und } \quad A(x)=x^{2}+\frac{6 V}{x} \xrightarrow{x \rightarrow \infty} \infty
$$

Die Oberfläche der Kiste ist demnach gegen beide Grenzen des Intervalls I nach oben unbeschränkt.