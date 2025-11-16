# 4. Umkehrfunktion einer linearen Funktion 

Wir betrachten $m \in \mathbb{R} \backslash\{0\}, q \in \mathbb{R}$ und die lineare Funktion

$$
\begin{aligned}
f: \mathbb{R} & \rightarrow \mathbb{R} \\
x & \mapsto f(x):=m \cdot x+q
\end{aligned}
$$

a) Um die Umkehrfunktion von $f$ zu berechnen, bestimmen wir die Lösung der Gleichung

$$
\begin{array}{rlrl}
y & =f(x)=m \cdot x+q & & -q \\
\Leftrightarrow & y-q & =m \cdot x & & : m \\
\Leftrightarrow & \frac{y-q}{m} & =x
\end{array}
$$

Daraus erhalten wir

$$
f^{-1}(y)=\frac{y-q}{m}=\frac{1}{m} \cdot y-\frac{q}{m}
$$

b) Wir zeigen mehrere Varianten, um zu begründen, warum die Umkehrfunktion von $f$ nur für $m \neq 0$ existiert.
Variante 1: Für $m=0$ würde gelten

$$
f(x)=m \cdot x+q=0 \cdot x+q=0+q=q \equiv \text { konst. }
$$

Das bedeutet, für jedes $x \in \mathbb{R}$ hätte der Funktionswert $f(x)$ den gleichen Wert $q$. Die Funktion $f$ wäre demnach nicht injektiv, somit nicht bijektiv und folglich nicht umkehrbar.
Variante 2: Für $m=0$ wäre der Graph von $f$ eine horizontale Gerade im $x$ - $y$-Diagramm. Somit wäre $f$ offensichtlich nicht bijektiv und folglich nicht umkehrbar.
Variante 3: Um die Umkehrfunktion von $f$ zu berechnen, haben wir in (15) durch $m$ dividiert. Diese Division wäre für $m=0$ nicht möglich, was die Existenz der Umkehrfunktion in diesem Fall ausschliesst.
c) Für den $x$-Achsabschnitt $p$ von $f$ gilt
$f(p)=0$.
Daraus und durch Einsetzen von (17) folgt
$\underline{p}=f^{-1}(0)=\frac{0-q}{m}=\frac{-q}{m}=\underline{\underline{-m}}$.
d) Wir betrachten die lineare Funktion
$f(x)=3 \cdot x+5$
mit den Grund-Form-Parametern $m=3$ und $q=5$. Gemäss (17) und (20) sind die Umkehrfunktion und der $x$-Achsabschnitt

$$
\begin{aligned}
\underline{f^{-1}(y)} & =\frac{y-q}{m}=\underline{\underline{y-5}}=\frac{1}{3} \cdot y-\frac{5}{3} \\
\underline{p} & =-\frac{q}{m}=\underline{\underline{-\frac{5}{3}}}
\end{aligned}
$$