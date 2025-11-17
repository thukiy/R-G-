# --- PAGE page_1 ---

# -`sleq`j_rr ?1_12 Computational and Data Science BSc HS 2023 

## Lösungen

Mathematik 1

1. Aussagen über lokale Extremalstellen

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :--: | :--: |
| a) Null ist ein lokales Minimum der quadratischen Standardfunktion. | $\bullet$ | $\bigcirc$ |
| b) Null ist ein lokales Minimum der kubischen Standardfunktion. | $\bigcirc$ | $\bullet$ |
| c) Die Funktion $2^{x}$ hat keine lokalen Extremstellen. | $\bullet$ | $\bigcirc$ |
| d) Der höchstmögliche Funktionswert einer Funktion liegt immer an einem <br> lokalen Maximum der Funktion. | $\bigcirc$ | $\bullet$ |
| e) Ein Polynom vom Grade 1'000 kann bis zu 1'000 lokale Extremstellen <br> haben. | $\bigcirc$ | $\bullet$ |
| f) Falls gilt $f^{\prime}(-3)=0$, dann hat $f$ an der Stelle $x=-3$ ein lokales Mini- <br> mum oder ein lokales Maximum. | $\bigcirc$ | $\bullet$ |

2. Analysis einer quadratischen Funktion

Es seien $a, b, c \in \mathbb{R}$ mit $a \neq 0$. Wir bestimmen die lokalen Extremstellen der allgemeinen, quadratischen Funktion

$$
f(x):=a x^{2}+b x+c
$$

Für die erste und zweite Ableitung von $f$ erhalten wir

$$
\begin{aligned}
& f^{\prime}(x)=a \cdot 2 x+b+0=2 a x+b \\
& f^{\prime \prime}(x)=2 a+0=2 a
\end{aligned}
$$

Da $f^{\prime}$ linear ist, kann $f$ höchstens eine kritische Stelle haben. Aus

$$
\begin{aligned}
0 & =f^{\prime}(x)=2 a x+b & \mid-b \\
\Leftrightarrow \quad-b & =2 a x & \mid:(2 a)
\end{aligned}
$$

folgt, dass $f$ genau eine kritische Stelle hat bei

$$
x_{\mathrm{S}}=-\frac{b}{2 a}
$$

# --- PAGE page_2 ---

Durch Einsetzen finden wir die Werte

$$
\begin{aligned}
f\left(x_{\mathrm{S}}\right) & =a x_{\mathrm{S}}^{2}+b x_{\mathrm{S}}+c=a\left(-\frac{b}{2 a}\right)^{2}+b\left(-\frac{b}{2 a}\right)+c=a \cdot \frac{b^{2}}{4 a^{2}}-\frac{b^{2}}{2 a}+c=\frac{b^{2}}{4 a}-\frac{b^{2}}{2 a}+c \\
& =-\frac{b^{2}}{4 a}+c=y_{\mathrm{S}} \\
f^{\prime}\left(x_{\mathrm{S}}\right) & =2 a x_{\mathrm{S}}+b=2 a \cdot\left(-\frac{b}{2 a}\right)+b=-\frac{2 a b}{2 a}+b=-b+b=0 \\
f^{\prime \prime}\left(x_{\mathrm{S}}\right) & =2 a
\end{aligned}
$$

Wir betrachten die Fälle $a<0$ und $a>0$ getrennt.
Fall 1: $a<0$. In diesem Fall gilt

$$
f^{\prime \prime}\left(x_{\mathrm{S}}\right)=2 a<0
$$

Demnach hat $f$ an der Stelle $x_{\mathrm{S}}$ ein lokales Maximum.
Fall 2: $a>0$. In diesem Fall gilt

$$
f^{\prime \prime}\left(x_{\mathrm{S}}\right)=2 a>0
$$

Demnach hat $f$ an der Stelle $x_{\mathrm{S}}$ ein lokales Minimum.
Diese Ergebnisse stimmen offenbar überein mit der klassischen Theorie der quadratischen Funktionen, gemäss welcher $f$ am Scheitelpunkt $\left.\xi_{\mathrm{S}} ; y_{\mathrm{S}}\right)$ im Falle $a>0$ ein lokales Minimum und im Falle $a<0$ ein lokales Maximum hat.

# 3. Bestimmung von lokalen Extremstellen 

Wir bestimmen jeweils alle lokalen Extrema und Sattelpunkte der angegebenen Funktion.
a) Wir betrachten die Funktion

$$
a(x)=3 x^{2}+12 x-7
$$

Für die erste und zweite Ableitung von $a$ erhalten wir

$$
\begin{aligned}
& a^{\prime}(x)=3 \cdot 2 x^{2-1}+12-0=6 x+12 \\
& a^{\prime \prime}(x)=6+0=6
\end{aligned}
$$

Da $a^{\prime}$ eine lineare Funktion ist, hat $a$ höchstens eine kritische Stelle. Aus

$$
\begin{aligned}
0 & =a^{\prime}(x)=6 x+12 & \mid-12 \\
\Leftrightarrow & -12=6 x & \mid: 6
\end{aligned}
$$

erhalten wir die kritische Stelle

$$
x_{1}=\frac{-12}{6}=-2
$$

Durch Einsetzen finden wir die Werte

$$
a\left(x_{1}\right)=a(-2)=3 \cdot(-2)^{2}+12 \cdot(-2)-7=12-24-7=-19
$$

# --- PAGE page_3 ---

$a^{\prime \prime}\left(x_{1}\right)=a^{\prime \prime}(-2)=6>0$.
Wir stellen die Ergebnisse in der folgenden Tabelle zusammen.

| $k$ | $x_{k}$ | $a\left(x_{k}\right)$ | $a^{\prime}\left(x_{k}\right)$ | $a^{\prime \prime}\left(x_{k}\right)$ | Typ |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | -2 | -19 | 0 | $6>0$ | lokales Minimum |

b) Wir betrachten die Funktion
$b(x)=2 x^{3}+3 x^{2}-12 x$.
Für die erste und zweite Ableitung von $b$ erhalten wir

$$
\begin{aligned}
b^{\prime}(x) & =2 \cdot 3 x^{3-1}+3 \cdot 2 x^{2-1}-12=6 x^{2}+6 x-12 \\
b^{\prime \prime}(x) & =6 \cdot 2 x^{2-1}+6-0=12 x+6
\end{aligned}
$$

Da $b^{\prime}(x)$ eine quadratische Funktion ist, hat $b$ höchstens zwei kritische Stellen. Aus

$$
\begin{array}{ll} 
& 0=b^{\prime}(x)=6 x^{2}+6 x-12 \quad \mid: 6 \\
\Leftrightarrow & 0=x^{2}+x-2 & \mid \mathrm{MF}
\end{array}
$$

erhalten wir
$x_{1,2}=\frac{-1 \pm \sqrt{1^{2}-4 \cdot 1 \cdot(-2)}}{2 \cdot 1}=\frac{-1 \pm \sqrt{9}}{2}=\frac{-1 \pm 3}{2}=-\frac{1}{2} \pm \frac{3}{2}$,
das heisst

$$
x_{1}=-\frac{1}{2}-\frac{3}{2}=-\frac{4}{2}=-2 \quad \text { und } \quad x_{2}=-\frac{1}{2}+\frac{3}{2}=\frac{2}{2}=1
$$

Durch Einsetzen finden wir die Werte

$$
\begin{aligned}
b\left(x_{1}\right) & =b(-2)=2 \cdot(-2)^{3}+3 \cdot(-2)^{2}-12 \cdot(-2)=-16+12+24=20 \\
b^{\prime \prime}\left(x_{1}\right) & =b^{\prime \prime}(-2)=12 \cdot(-2)+6=-18<0 \\
b\left(x_{2}\right) & =b(1)=2 \cdot 1^{3}+3 \cdot 1^{2}-12 \cdot 1=2+3-12=-7 \\
b^{\prime \prime}\left(x_{2}\right) & =b^{\prime \prime}(1)=12 \cdot 1+6=+18>0
\end{aligned}
$$

Wir stellen die Ergebnisse in der folgenden Tabelle zusammen.

| $k$ | $x_{k}$ | $b\left(x_{k}\right)$ | $b^{\prime}\left(x_{k}\right)$ | $b^{\prime \prime}\left(x_{k}\right)$ | Typ |
| :--: | :--: | --: | --: | :--: | :--: |
| 1 | -2 | 20 | 0 | $-18<0$ | lokales Maximum |
| 2 | 1 | -7 | 0 | $+18>0$ | lokales Minimum |

c) Wir betrachten die Funktion
$c(x)=x^{4}-2 x^{2}+2$.

# --- PAGE page_4 ---

Für die erste und zweite Ableitung von $c$ erhalten wir

$$
\begin{aligned}
c^{\prime}(x) & =4 x^{4-1}-2 \cdot 2 x^{2-1}+0=4 x^{3}-4 x \\
c^{\prime \prime}(x) & =4 \cdot 3 x^{3-1}-4=12 x^{2}-4
\end{aligned}
$$

Da $c^{\prime}$ ein Polynom dritten Grades ist, hat $c$ höchstens drei kritische Stellen. Aus

$$
0=c^{\prime}(x)=4 x^{3}-4 x=4 x\left(x^{2}-1\right)=4 x(x+1)(x-1)
$$

erhalten wir die kritischen Stellen

$$
x_{1}=-1, x_{2}=0 \quad \text { und } \quad x_{3}=1
$$

Durch Einsetzen finden wir die Werte

$$
\begin{aligned}
c\left(x_{1}\right) & =c(-1)=(-1)^{4}-2 \cdot(-1)^{2}+2=1-2+2=1 \\
c^{\prime \prime}\left(x_{1}\right) & =c^{\prime \prime}(-1)=12 \cdot(-1)^{2}-4=12-4=8 \\
c\left(x_{2}\right) & =c(0)=0^{4}-2 \cdot 0^{2}+2=0-0+2=2 \\
c^{\prime \prime}\left(x_{2}\right) & =c^{\prime \prime}(0)=12 \cdot 0^{2}-4=0-4=-4 \\
c\left(x_{3}\right) & =c(1)=1^{4}-2 \cdot 1^{2}+2=1-2+2=1 \\
c^{\prime \prime}\left(x_{3}\right) & =c^{\prime \prime}(1)=12 \cdot 1^{2}-4=12-4=8
\end{aligned}
$$

Wir stellen die Ergebnisse in der folgenden Tabelle zusammen.

| $k$ | $x_{k}$ | $c\left(x_{k}\right)$ | $c^{\prime}\left(x_{k}\right)$ | $c^{\prime \prime}\left(x_{k}\right)$ | Typ |
| :--: | --: | --: | --: | --: | :-- |
| 1 | -1 | 1 | 0 | $8>0$ | lokales Minimum |
| 2 | 0 | 2 | 0 | $-4<0$ | lokales Maximum |
| 3 | +1 | 1 | 0 | $8>0$ | lokales Minimum |

d) Wir betrachten die Funktion
$d(x)=x^{4}-2 x^{3}-1$.
Für die erste und zweite Ableitung von $d$ erhalten wir

$$
\begin{aligned}
d^{\prime}(x) & =4 x^{4-1}-2 \cdot 3 x^{3-1}-0=4 x^{3}-6 x^{2} \\
d^{\prime \prime}(x) & =4 \cdot 3 x^{3-1}-6 \cdot 2 x=12 x^{2}-12 x
\end{aligned}
$$

Da $d^{\prime}$ ein Polynom dritten Grades ist, hat $d$ höchstens drei kritische Stellen. Aus

$$
0=d^{\prime}(x)=4 x^{3}-6 x^{2}=2 x^{2}(2 x-3)
$$

erhalten wir die kritischen Stellen

$$
x_{1}=0 \quad \text { und } \quad x_{2}=\frac{3}{2}
$$

Durch Einsetzen finden wir die Werte

$$
d\left(x_{1}\right)=d(0)=0^{4}-2 \cdot 0^{3}-1=-1
$$

# --- PAGE page_5 ---

$$
\begin{aligned}
d^{\prime \prime}\left(x_{1}\right) & =d^{\prime \prime}(0)=12 \cdot 0^{2}-12 \cdot 0=0 \\
d\left(x_{2}\right) & =d\left(\frac{3}{2}\right)=\left(\frac{3}{2}\right)^{4}-2 \cdot\left(\frac{3}{2}\right)^{3}-1=\frac{81}{16}-\frac{108}{16}-\frac{16}{16}=-\frac{43}{16} \\
d^{\prime \prime}\left(x_{2}\right) & =d^{\prime \prime}\left(\frac{3}{2}\right)=12 \cdot\left(\frac{3}{2}\right)^{2}-12 \cdot \frac{3}{2}=27-18=9
\end{aligned}
$$

Weil $d^{\prime \prime}\left(x_{1}\right)=0$, lässt sich der Typ der kritischen Stelle $x_{1}=0$ mit den bisher berechneten Grössen nicht eindeutig bestimmen. Wir zeigen zwei Varianten, um die kritische Stelle $x_{1}$ genauer zu beurteilen.
Variante 1: Die dritte Ableitung von $d$ ist

$$
d^{\prime \prime \prime}(x)=12 \cdot 2 x^{2-1}-12=24 x-12
$$

Es gilt

$$
d^{\prime \prime \prime}\left(x_{1}\right)=d^{\prime \prime \prime}(0)=24 \cdot 0-12=-12 \neq 0
$$

Die erste nicht verschwindende Ableitung von $d$ an der kritischen Stelle $x_{1}$ ist demnach von ungerader Ordnung.
Variante 2: Weil $x_{1}=0$ die kleinste kritische Stelle von $d$ ist, verläuft die Funktion für alle $x<0$ streng monoton. Wir betrachten als Beispiel die Stelle $x_{b}=-1$. Es gilt

$$
d\left(x_{b}\right)=d(-1)=(-1)^{4}-2 \cdot(-1)^{3}-1=1+2-1=2
$$

Es gilt demnach

$$
d\left(x_{b}\right)=2>-1=d\left(x_{1}\right)>-\frac{43}{16}=d\left(x_{2}\right)
$$

Die Funktion $d$ ist demnach sowohl unmittelbar links als auch unmittelbar rechts von der kritischen Stelle $x_{1}$ streng monoton fallend.
Es folgt, dass $d$ an der Stelle $x_{1}=0$ einen Sattelpunkt haben muss. Wir stellen die Ergebnisse in der folgenden Tabelle zusammen.

| $k$ | $x_{k}$ | $d\left(x_{k}\right)$ | $d^{\prime}\left(x_{k}\right)$ | $d^{\prime \prime}\left(x_{k}\right)$ | $d^{\prime \prime \prime}\left(x_{k}\right)$ | Typ |
| :--: | :--: | --: | --: | --: | --: | :-- |
| 1 | 0 | -1 | 0 | 0 | -12 | Sattelpunkt |
| 2 | $3 / 2$ | $-43 / 16$ | 0 | $9>0$ | n.v. | lokales Minimum |

e) Wir betrachten die Funktion
$e(x)=\sqrt{3 x^{2}+12 x-7}=\sqrt{a(x)}$.
Für die erste Ableitung von $e$ erhalten wir mit Hilfe der Ketten-Regel
$e^{\prime}(x)=\frac{1}{2 \sqrt{a(x)}} \cdot a^{\prime}(x)$
Alle kritischen Stellen von $e$ sind demnach auch kritische Stellen von $a$. Gemäss (17) erhalten wir somit als einzige Kandidatenstelle

$$
x_{1}=-2
$$

# --- PAGE page_6 ---

Wegen (18) gilt aber
$a\left(x_{1}\right)=a(-2)=-19<0$.
Konsequenterweise liegt die Stelle $x_{1}$ ausserhalb des natürlichen Definitionsbereiches von $e$, weil aus negativen Zahlen keine Wurzel gezogen werden kann. Demnach hat $e$ keine lokalen Extrema.
f) Wir betrachten die Funktion
$f(x)=\frac{1}{2 x^{3}+3 x^{2}-12 x}=\frac{1}{b(x)}$.
Für die erste Ableitung von $f$ erhalten wir mit Hilfe der Reziproken-Regel
$f^{\prime}(x)=-\frac{1}{b^{2}(x)} \cdot b^{\prime}(x)$.
Alle kritischen Stellen von $f$ sind demnach auch kritische Stellen von b. Gemäss (26) erhalten wir somit die beiden Kandidaten-Stellen

$$
x_{1}=-2 \quad \text { und } \quad x_{2}=1
$$

Mit Hilfe von (28) und (30) sehen wir, dass beide Kandidaten-Stellen innerhalb des natürlichen Definitionsbereiches von $f$ liegen. Durch Einsetzen finden wir die Werte
$f\left(x_{1}\right)=f(-2)=\frac{1}{b(-2)}=\frac{1}{20} \quad$ und $\quad f\left(x_{2}\right)=f(1)=\frac{1}{b(1)}=\frac{1}{-7}=-\frac{1}{7}$.
Da $f$ und $b$ zueinander reziproke Funktionen sind, ist das lokale Maximum von $f$ ein lokales Minimum von $b$ und das lokale Minimum von $f$ ein lokales Maximum von $b$. Wir stellen die Ergebnisse in der folgenden Tabelle zusammen.

| $k$ | $x_{k}$ | $f\left(x_{k}\right)$ | $f^{\prime}\left(x_{k}\right)$ | Typ |
| :--: | :--: | :--: | :--: | :--: |
| 1 | -2 | $1 / 20$ | 0 | lokales Minimum |
| 2 | 1 | $-1 / 7$ | 0 | lokales Maximum |

# 4. Aussagen über das Verhalten einer Funktion 

Wir betrachten die Funktion

$$
\begin{aligned}
f: \mathbb{R} & \rightarrow \mathbb{R} \\
x & \mapsto f(x):=-3 x \cdot(x+3) \cdot(3-x)
\end{aligned}
$$

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) Die Funktion $f$ ist nach oben unbeschränkt. | $\bullet$ | $\bigcirc$ |
| b) Die Funktion $f$ ist injektiv. | $\bigcirc$ | $\bullet$ |
| c) Die Funktion $f$ ist surjektiv. | $\bullet$ | $\bigcirc$ |
| d) Die Funktion $f$ hat bei $x=4$ einen Sattelpunkt. | $\bigcirc$ | $\bullet$ |
| e) Die Funktion $f$ hat im Intervall $[0,3]$ ein lokales Maximum. | $\bigcirc$ | $\bullet$ |
| f) Die Funktion $f$ hat genau zwei lokale Extremstellen. | $\bullet$ | $\bigcirc$ |

# --- PAGE page_7 ---

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

# --- PAGE page_8 ---

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

# --- PAGE page_9 ---

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

# --- PAGE page_10 ---

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

# --- PAGE page_11 ---

$$
\begin{array}{ll}
\Leftrightarrow & \frac{2 V}{x^{2}}=4 \pi x \\
\Leftrightarrow & \frac{2 V}{4 \pi}=x^{3}
\end{array} \quad \begin{aligned}
& \cdot \frac{x^{2}}{4 \pi} \\
& \sqrt[3]{\cdots}
\end{array}
$$

Daraus erhalten wir genau eine kritische Stelle von $A(x)$, nämlich

$$
x_{1}=\sqrt[3]{\frac{2 V}{4 \pi}}=\sqrt[3]{\frac{V}{2 \pi}}
$$

Ferner berechnen wir gemäss (110) bis (112) die Werte

$$
\begin{aligned}
R_{1} & =R\left(x_{1}\right)=x_{1}=\sqrt[3]{\frac{V}{2 \pi}} \approx \sqrt[3]{\frac{1.00 \mathrm{dm}^{3}}{2 \pi}} \approx 0.542 \mathrm{dm}=5.42 \mathrm{~cm} \\
H_{1} & =H\left(x_{1}\right)=\frac{V}{\pi x_{1}^{2}}=\frac{V}{\pi\left(\sqrt[3]{\frac{V}{2 \pi}}\right)^{2}}=\frac{V}{\pi \sqrt[3]{\left(\frac{V}{2 \pi}\right)^{2}}}=\frac{\sqrt[3]{V^{3}}}{\sqrt[3]{\pi^{3}} \sqrt[3]{\frac{V^{2}}{4 \pi^{2}}}}=\sqrt[3]{\frac{V^{3}}{\pi^{3} \frac{V^{2}}{4 \pi^{2}}}}=\sqrt[3]{\frac{4 \pi^{2} V^{3}}{\pi^{3} V^{2}}} \\
& =\sqrt[3]{\frac{4 V}{\pi}}=\sqrt[3]{\frac{8 V}{2 \pi}}=\sqrt[3]{8} \cdot \sqrt[3]{\frac{V}{2 \pi}}=2 R \approx 2 \cdot 5.42 \mathrm{~cm} \approx 10.8 \mathrm{~cm} . \\
A_{1} & =A\left(x_{1}\right)=2 \pi x_{1}^{2}+\frac{2 V}{x_{1}} \approx 2 \pi \cdot(0.542 \mathrm{dm})^{2}+\frac{2 \cdot 1.00 \mathrm{dm}^{3}}{0.542 \mathrm{dm}} \approx 5.54 \mathrm{dm}^{2}
\end{aligned}
$$

S2 Rand stellen: Das offene Intervall $I$ hat keine Randstellen, es gilt jedoch

$$
A(x)=2 \pi x^{2}+\frac{2 V}{x} \xrightarrow{x \rightarrow 0} \infty \quad \text { und } \quad A(x)=2 \pi x^{2}+\frac{2 V}{x} \xrightarrow{x \rightarrow \infty} \infty
$$

Die Oberfläche der Konservendose ist demnach gegen beide Grenzen des Intervalls I nach oben unbeschränkt.
S3 Kandidatenverglei ch: Wir stellen die Ergebnisse in der folgenden Tabelle zusammen.

| $k$ | $x_{k}$ | $R_{k}$ | $H_{k}$ | $A_{k}$ | Typ |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | 5.42 cm | 5.42 cm | 10.8 cm | $5.54 \mathrm{dm}^{2}$ | globales Minimum |

Die Oberfläche der Konservendose ist also genau dann minimal, wenn gilt

$$
\underline{R} \approx 5.42 \mathrm{~cm} \quad \text { und } \quad \underline{H} \approx 10.8 \mathrm{~cm}
$$

# --- PAGE page_12 ---

# 7. Kürzeste Verbindung zu einer Parabel 

Wir betrachten die Normalparabel, d.h. den Graphen der quadratischen Standardfunktion

$$
f(x):=x^{2}
$$

Die Situation ist in der folgenden Skizze dargestellt.

a) Es sei $g: \mathbb{R} \rightarrow] 0, \infty[$ die Funktion, welche jedem $x \in \mathbb{R}$ den Abstand $d$ zwischen dem Punkt $P=(x ; f(x))$ auf der Parabel und dem fixen Punkt $Q:=(0 ; 2)$ zuordnet. Ferner definieren wir $G(x):=g^{2}(x)$. Mit Hilfe des Pythagoras-Satzes erhalten wir

$$
\begin{aligned}
G(x) & =\left(x-q_{x}\right)^{2}+\left(f(x)-q_{y}\right)^{2}=(x-0)^{2}+\left(x^{2}-2\right)^{2}=x^{2}+\left(x^{2}\right)^{2}-2 \cdot x^{2} \cdot 2+4 \\
& =x^{2}+x^{4}-4 x^{2}+4=x^{4}-3 x^{2}+4
\end{aligned}
$$

und somit

$$
g(x)=\sqrt{G(x)}=\sqrt{x^{4}-3 x^{2}+4}
$$

b) Wir skizzieren den Graphen von $g(x)$


# --- PAGE page_13 ---

c) Für die erste und zweite Ableitung von $G$ erhalten wir

$$
\begin{aligned}
G^{\prime}(x) & =4 x^{4-1}-3 \cdot 2 x^{2-1}+0=4 x^{3}-6 x \\
G^{\prime \prime}(x) & =4 \cdot 3 x^{3-1}-6=12 x^{2}-6
\end{aligned}
$$

Da $G^{\prime}(x)$ ein kubisches Polynom ist, hat $G$ höchstens drei kritische Stellen. Die Gleichung

$$
0=G^{\prime}(x)=4 x^{3}-6 x=2 x \cdot\left(2 x^{2}-3\right)
$$

hat offensichtlich die Lösung

$$
x_{1}=0
$$

Zudem finden wir aus

$$
\begin{array}{rlrl}
2 x^{2}-3 & =0 & & +3 \\
\Leftrightarrow & 2 x^{2} & =3 & & 2 \\
\Leftrightarrow & x^{2} & =\frac{3}{2} & & \pm \sqrt{\cdots}
\end{array}
$$

zwei weitere Lösungen, nämlich

$$
x_{2,3}= \pm \sqrt{\frac{3}{2}}
$$

Ferner berechnen wir die Werte

$$
\begin{aligned}
G\left(x_{1}\right) & =G(0)=0^{4}-3 \cdot 0^{2}+4=0+0+4=4 \\
G^{\prime \prime}\left(x_{1}\right) & =G^{\prime \prime}(0)=12 \cdot 0^{2}-6=0-6=-6<0 \\
G\left(x_{2}\right) & =G\left(+\sqrt{\frac{3}{2}}\right)=\left(+\sqrt{\frac{3}{2}}\right)^{4}-3\left(+\sqrt{\frac{3}{2}}\right)^{2}+4=\frac{9}{4}-3 \cdot \frac{3}{2}+4 \\
& =\frac{9}{4}-\frac{18}{4}+\frac{16}{4}=\frac{7}{4} \\
G^{\prime \prime}\left(x_{2}\right) & =G^{\prime \prime}\left(+\sqrt{\frac{3}{2}}\right)=12\left(+\sqrt{\frac{3}{2}}\right)^{2}-6=12 \cdot \frac{3}{2}-6=18-6=12>0 \\
G\left(x_{3}\right) & =G\left(+\sqrt{\frac{3}{2}}\right)=\left(+\sqrt{\frac{3}{2}}\right)^{4}-3\left(+\sqrt{\frac{3}{2}}\right)^{2}+4=\frac{9}{4}-3 \cdot \frac{3}{2}+4 \\
& =\frac{9}{4}-\frac{18}{4}+\frac{16}{4}=\frac{7}{4} \\
G^{\prime \prime}\left(x_{3}\right) & =G^{\prime \prime}\left(+\sqrt{\frac{3}{2}}\right)=12\left(+\sqrt{\frac{3}{2}}\right)^{2}-6=12 \cdot \frac{3}{2}-6=18-6=12>0
\end{aligned}
$$

Wir stellen die Ergebnisse in der folgenden Tabelle zusammen.

| $k$ | $x_{k}$ | $G\left(x_{k}\right)$ | $G^{\prime}\left(x_{k}\right)$ | $G^{\prime \prime}\left(x_{k}\right)$ | Typ |
| :--: | --: | --: | --: | :--: | :--: |
| 1 | 0 | 4 | 0 | $-6<0$ | lokales Maximum |
| 2 | $-\sqrt{3 / 2}$ | $7 / 4$ | 0 | $+12>0$ | lokales Minimum |
| 3 | $+\sqrt{3 / 2}$ | $7 / 4$ | 0 | $+12>0$ | lokales Minimum |

# --- PAGE page_14 ---

Es gibt daher zwei Punkte auf der Parabel, welche den minimalen Abstand zum Punkt $Q$ haben. Es sind dies

$$
\begin{aligned}
& \underline{\underline{P_{2}}}=\left(-\sqrt{\frac{3}{2}} ; f\left(-\sqrt{\frac{3}{2}}\right)\right)=\left(-\sqrt{\frac{3}{2}} ;\left(-\sqrt{\frac{3}{2}}\right)^{2}\right)=\underline{\left(-\sqrt{\frac{3}{2}} ; \frac{3}{2}\right)} \\
& \underline{\underline{P_{3}}}=\left(+\sqrt{\frac{3}{2}} ; f\left(+\sqrt{\frac{3}{2}}\right)\right)=\left(+\sqrt{\frac{3}{2}} ;\left(+\sqrt{\frac{3}{2}}\right)^{2}\right)=\underline{\left(+\sqrt{\frac{3}{2}} ; \frac{3}{2}\right)}
\end{aligned}
$$

Beide Punkte haben zum Punkt $Q$ jeweils einen Abstand von

$$
\underline{\underline{d}}=g\left( \pm \sqrt{\frac{3}{2}}\right)=\sqrt{G\left( \pm \sqrt{\frac{3}{2}}\right)}=\sqrt{\frac{7}{4}}=\underline{\underline{\sqrt{7}}}
$$