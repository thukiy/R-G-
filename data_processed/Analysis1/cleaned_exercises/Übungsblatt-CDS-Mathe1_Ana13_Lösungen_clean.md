# --- PAGE page_1 ---

# -`sleq`j_rr ?1_13 Computational and Data Science BSc HS 2023 

## 1. Aussagen über die Krümmung

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) Verschwindet die analytische Krümmung einer Funktion an jeder Stelle <br> $x \in \mathbb{R}$, dann ist die Funktion linear oder sogar konstant. |  |  |
| b) Haben zwei Funktionen die gleiche analytische Krümmung, dann haben <br> ihre Funktionsgraphen auch die gleiche geometrische Krümmung. |  |  |
| c) Die geometrische Krümmung jedes Funktionsgraphen ist gerade $f^{\prime \prime}(x)$. |  |  |
| d) Jede quadratische Funktion hat konstante, analytische Krümmung. |  |  |
| e) Jede Parabel hat konstante geometrische Krümmung. |  |  |
| f) Verschwindet an einem Punkt die analytische Krümmung einer Funktion, <br> dann gilt dies auch für die geometrische Krümmung ihres Funktionsgra- <br> phen. |  |  |

## 2. Bestimmung von Wendestellen

Wir bestimmen jeweils alle Wendepunkte der angegebenen Funktion.
a) Wir betrachten die Funktion

$$
a(x):=x^{3}-x+1
$$

Für die erste, zweite und dritte Ableitung von $a$ erhalten wir

$$
\begin{aligned}
& a^{\prime}(x)=3 \cdot x^{3-1}-1+0=3 x^{2}-1 \\
& a^{\prime \prime}(x)=3 \cdot 2 x^{2-1}-0=6 x \\
& a^{\prime \prime \prime}(x)=6
\end{aligned}
$$

Da $a^{\prime \prime}$ linear ist, kann $a$ höchstens eine Wendestelle haben. Aus

$$
0=a^{\prime \prime}(x)=6 x \quad \mid: 6
$$

erhalten wir die Wendestelle

$$
x_{1}=0
$$

# --- PAGE page_2 ---

Durch Einsetzen finden wir die Werte

$$
\begin{aligned}
a\left(x_{1}\right) & =a(0)=0^{3}-0+1=1 \\
a^{\prime}\left(x_{1}\right) & =a^{\prime}(0)=3 \cdot 0^{2}-1=-1 \\
a^{\prime \prime \prime}\left(x_{1}\right) & =a^{\prime \prime \prime}(0)=6>0
\end{aligned}
$$

Wir stellen die Ergebnisse in der folgenden Tabelle zusammen.

| $k$ | $x_{k}$ | $a\left(x_{k}\right)$ | $a^{\prime}\left(x_{k}\right)$ | $a^{\prime \prime}\left(x_{k}\right)$ | $a^{\prime \prime \prime}\left(x_{k}\right)$ | Typ |
| :--: | :--: | --: | --: | --: | --: | :--: |
| 1 | 0 | 1 | -1 | 0 | $6>0$ | Wendepunkt |

b) Wir betrachten die Funktion

$$
b(x):=x^{4}-6 x^{2}+2
$$

Für die erste, zweite und dritte Ableitung von $b$ erhalten wir

$$
\begin{aligned}
b^{\prime}(x) & =4 \cdot x^{4-1}-6 \cdot 2 x^{2-1}+0=4 x^{3}-12 x \\
b^{\prime \prime}(x) & =4 \cdot 3 x^{3-1}-12=12 x^{2}-12 \\
b^{\prime \prime \prime}(x) & =12 \cdot 2 x^{2-1}-0=24 x
\end{aligned}
$$

Da $b^{\prime \prime}(x)$ quadratisch ist, hat $b$ höchstens zwei Wendestellen. Aus

$$
0=b^{\prime \prime}(x)=12 x^{2}-12=12 \cdot\left(x^{2}-1\right)=12 \cdot(x+1) \cdot(x-1)
$$

erhalten wir die Wendestellen

$$
x_{1}=-1 \quad \text { und } \quad x_{2}=1
$$

Durch Einsetzen finden wir die Werte

$$
\begin{aligned}
b\left(x_{1}\right) & =b(-1)=(-1)^{4}-6 \cdot(-1)^{2}+2=1-6+2=-3 \\
b^{\prime}\left(x_{1}\right) & =b^{\prime}(-1)=4 \cdot(-1)^{3}-12 \cdot(-1)=-4+12=8 \\
b^{\prime \prime \prime}\left(x_{1}\right) & =b^{\prime \prime \prime}(-1)=24 \cdot(-1)=-24<0 \\
b\left(x_{2}\right) & =b(1)=1^{4}-6 \cdot 1^{2}+2=1-6+2=-3 \\
b^{\prime}\left(x_{2}\right) & =b^{\prime}(1)=4 \cdot 1^{3}-12 \cdot 1=4-12=-8 \\
b^{\prime \prime \prime}\left(x_{2}\right) & =b^{\prime \prime \prime}(1)=24 \cdot 1=24>0
\end{aligned}
$$

Wir stellen die Ergebnisse in der folgenden Tabelle zusammen.

| $k$ | $x_{k}$ | $b\left(x_{k}\right)$ | $b^{\prime}\left(x_{k}\right)$ | $b^{\prime \prime}\left(x_{k}\right)$ | $b^{\prime \prime \prime}\left(x_{k}\right)$ | Typ |
| :--: | --: | --: | --: | --: | --: | :--: |
| 1 | -1 | -3 | +8 | 0 | $-24<0$ | Wendepunkt |
| 2 | +1 | -3 | -8 | 0 | $+24>0$ | Wendepunkt |

# --- PAGE page_3 ---

c) Wir betrachten die Funktion

$$
c(x):=4^{x}-2^{x}-1
$$

Für die erste, zweite und dritte Ableitung von $c$ erhalten wir

$$
\begin{aligned}
c^{\prime}(x) & =\ln (4) \cdot 4^{x}-\ln (2) \cdot 2^{x}-0=2 \ln (2) \cdot 4^{x}-\ln (2) \cdot 2^{x} \\
c^{\prime \prime}(x) & =2 \ln (2) \cdot \ln (4) \cdot 4^{x}-\ln (2) \cdot \ln (2) \cdot 2^{x}=4 \ln ^{2}(2) \cdot 4^{x}-\ln ^{2}(2) \cdot 2^{x} \\
c^{\prime \prime \prime}(x) & =4 \ln ^{2}(2) \cdot \ln (4) \cdot 4^{x}-\ln ^{2}(2) \cdot \ln (2) \cdot 2^{x}=8 \ln ^{3}(2) \cdot 4^{x}-\ln ^{3}(2) \cdot 2^{x}
\end{aligned}
$$

An den Wendestellen von $c$ gilt

$$
\begin{array}{ll}
0=c^{\prime \prime}(x)=4 \ln ^{2}(2) \cdot 4^{x}-\ln ^{2}(2) \cdot 2^{x}=\ln ^{2}(2) \cdot\left(4 \cdot 4^{x}-2^{x}\right) & \mid: \ln ^{2}(2) \\
\Leftrightarrow \quad 0=4 \cdot 4^{x}-2^{x}=2^{2} \cdot\left(2^{2}\right)^{x}-2^{x}=2^{2} \cdot 2^{2 x}-2^{x}=2^{2 x+2}-2^{x} & \mid+2^{x} \\
\Leftrightarrow \quad 2^{x}=2^{2 x+2} & \left\lvert\, \log _{2}(\ldots)\right. \\
\Leftrightarrow \quad x=2 x+2 & \mid-2-x
\end{array}
$$

Daraus erhalten wir die Wendestelle

$$
x_{1}=-2
$$

Durch Einsetzen finden wir die Werte

$$
\begin{aligned}
c\left(x_{1}\right) & =c(-2)=4^{-2}-2^{-2}-1=\frac{1}{16}-\frac{1}{4}-1=\frac{1}{16}-\frac{4}{16}-\frac{16}{16} \\
& =\frac{1-4-16}{16}=-\frac{19}{16} \\
c^{\prime}\left(x_{1}\right) & =c^{\prime}(-2)=2 \ln (2) \cdot 4^{-2}-\ln (2) \cdot 2^{-2}=\frac{2 \ln (2)}{16}-\frac{\ln (2)}{4} \\
& =\frac{\ln (2)}{8}-\frac{2 \ln (2)}{8}=-\frac{\ln (2)}{8} . \\
c^{\prime \prime \prime}\left(x_{1}\right) & =c^{\prime \prime \prime}(-2)=8 \ln ^{3}(2) \cdot 4^{-2}-\ln ^{3}(2) \cdot 2^{-2}=\frac{8 \ln ^{3}(2)}{16}-\frac{\ln ^{3}(2)}{4} \\
& =\frac{2 \ln ^{3}(2)}{4}-\frac{\ln ^{3}(2)}{4}=\frac{\ln ^{3}(2)}{4}>0
\end{aligned}
$$

Wir stellen die Ergebnisse in der folgenden Tabelle zusammen.

| $k$ | $x_{k}$ | $c\left(x_{k}\right)$ | $c^{\prime}\left(x_{k}\right)$ | $c^{\prime \prime}\left(x_{k}\right)$ | $c^{\prime \prime \prime}\left(x_{k}\right)$ | Typ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | -2 | $-19 / 16$ | $-\ln (2) / 8$ | 0 | $\ln ^{3}(2) / 4>0$ | Wendepunkt |

d) Wir betrachten die Funktion
$d(x)=x \cdot \mathrm{e}^{x}$.
Für die erste, zweite und dritte Ableitung von $d$ erhalten wir

$$
d^{\prime}(x)=1 \cdot \mathrm{e}^{x}+x \cdot \mathrm{e}^{x}=(1+x) \cdot \mathrm{e}^{x}
$$

# --- PAGE page_4 ---

$$
\begin{aligned}
& d^{\prime \prime}(x)=(1+0) \cdot \mathrm{e}^{x}+(1+x) \cdot \mathrm{e}^{x}=(1+1+x) \cdot \mathrm{e}^{x}=(2+x) \cdot \mathrm{e}^{x} \\
& d^{\prime \prime \prime}(x)=(0+1) \cdot \mathrm{e}^{x}+(2+x) \cdot \mathrm{e}^{x}=(1+2+x) \cdot \mathrm{e}^{x}=(3+x) \cdot \mathrm{e}^{x}
\end{aligned}
$$

An den Wendestellen von $d$ gilt

$$
\begin{array}{ll}
0=d^{\prime \prime}(x)=(2+x) \cdot \mathrm{e}^{x} & \mid: \mathrm{e}^{x} \\
\Leftrightarrow & 0=2+x & \mid-2
\end{array}
$$

Daraus erhalten wir die Wendestelle

$$
x_{1}=-2
$$

Durch Einsetzen finden wir die Werte

$$
\begin{aligned}
d\left(x_{1}\right) & =d(-2)=-2 \cdot \mathrm{e}^{-2}=-\frac{2}{e^{2}} \\
d^{\prime}\left(x_{1}\right) & =d^{\prime}(-2)=(1-2) \cdot \mathrm{e}^{-2}=-\frac{1}{e^{2}} \\
d^{\prime \prime \prime}\left(x_{1}\right) & =d^{\prime \prime \prime}(-2)=(3-2) \cdot \mathrm{e}^{-2}=\frac{1}{e^{2}}>0
\end{aligned}
$$

Wir stellen die Ergebnisse in der folgenden Tabelle zusammen.

| $k$ | $x_{k}$ | $d\left(x_{k}\right)$ | $d^{\prime}\left(x_{k}\right)$ | $d^{\prime \prime}\left(x_{k}\right)$ | $d^{\prime \prime \prime}\left(x_{k}\right)$ | Typ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | -2 | $-2 / \mathrm{e}^{2}$ | $-1 / \mathrm{e}^{2}$ | 0 | $1 / \mathrm{e}^{2}>0$ | Wendepunkt |

e) Wir betrachten die Funktion
$e(x):=\frac{\mathrm{e}^{x}-\mathrm{e}^{-x}}{2}$.
Für die erste, zweite und dritte Ableitung von $e$ erhalten wir

$$
\begin{aligned}
e^{\prime}(x) & =\frac{\mathrm{e}^{x}-(-1) \cdot \mathrm{e}^{-x}}{2}=\frac{\mathrm{e}^{x}+\mathrm{e}^{-x}}{2} \\
e^{\prime \prime}(x) & =\frac{\mathrm{e}^{x}+(-1) \cdot \mathrm{e}^{-x}}{2}=\frac{\mathrm{e}^{x}-\mathrm{e}^{-x}}{2} \\
e^{\prime \prime \prime}(x) & =\frac{\mathrm{e}^{x}-(-1) \cdot \mathrm{e}^{-x}}{2}=\frac{\mathrm{e}^{x}+\mathrm{e}^{-x}}{2}
\end{aligned}
$$

An den Wendestellen von $e$ gilt

$$
\begin{array}{ll}
0=e^{\prime \prime}(x)=\frac{\mathrm{e}^{x}-\mathrm{e}^{-x}}{2} & \mid \cdot 2 \\
\Leftrightarrow & 0=\mathrm{e}^{x}-\mathrm{e}^{-x} & \mid+\mathrm{e}^{-x} \\
\Leftrightarrow & \mathrm{e}^{-x}=\mathrm{e}^{x} & \mid \ln (\ldots) \\
\Leftrightarrow & -x=x & \mid+x \\
\Leftrightarrow & 0=2 x & \mid: 2
\end{array}
$$

# --- PAGE page_5 ---

Daraus erhalten wir die Wendestelle

$$
x_{1}=0
$$

Durch Einsetzen finden wir die Werte

$$
\begin{aligned}
e\left(x_{1}\right) & =e(0)=\frac{\mathrm{e}^{0}-\mathrm{e}^{-0}}{2}=\frac{1-1}{2}=0 \\
e^{\prime}\left(x_{1}\right) & =e^{\prime}(0)=\frac{\mathrm{e}^{0}+\mathrm{e}^{-0}}{2}=\frac{1+1}{2}=1 \\
e^{\prime \prime \prime}\left(x_{1}\right) & =e^{\prime \prime \prime}(0)=\frac{\mathrm{e}^{0}+\mathrm{e}^{-0}}{2}=\frac{1+1}{2}=1
\end{aligned}
$$

Wir stellen die Ergebnisse in der folgenden Tabelle zusammen.

| $k$ | $x_{k}$ | $e\left(x_{k}\right)$ | $e^{\prime}\left(x_{k}\right)$ | $e^{\prime \prime}\left(x_{k}\right)$ | $e^{\prime \prime \prime}\left(x_{k}\right)$ | Typ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | 0 | 0 | 1 | 0 | $1>0$ | Wendepunkt |

f) Wir betrachten die Funktion
$f(x):=\mathrm{e}^{-\frac{x^{2}}{2}}$.
Für die erste, zweite und dritte Ableitung von $d$ erhalten wir

$$
\begin{aligned}
f^{\prime}(x) & =-\frac{2 x}{2} \cdot \mathrm{e}^{-\frac{x^{2}}{2}}=-x \cdot \mathrm{e}^{-\frac{x^{2}}{2}} \\
f^{\prime \prime}(x) & =-1 \cdot \mathrm{e}^{-\frac{x^{2}}{2}}-x \cdot(-1) \cdot \frac{2 x}{2} \cdot \mathrm{e}^{-\frac{x^{2}}{2}}=\left(x^{2}-1\right) \cdot \mathrm{e}^{-\frac{x^{2}}{2}} \\
f^{\prime \prime \prime}(x) & =(2 x-0) \cdot \mathrm{e}^{-\frac{x^{2}}{2}}+\left(x^{2}-1\right) \cdot(-1) \cdot \frac{2 x}{2} \cdot \mathrm{e}^{-\frac{x^{2}}{2}}=\left(3 x-x^{3}\right) \cdot \mathrm{e}^{-\frac{x^{2}}{2}}
\end{aligned}
$$

An den Wendestellen von $f$ gilt

$$
\begin{aligned}
& 0=f^{\prime \prime}(x)=\left(x^{2}-1\right) \cdot \mathrm{e}^{-\frac{x^{2}}{2}} \\
& 0=\left(x^{2}-1\right)=(x+1) \cdot(x-1)
\end{aligned}
$$

Daraus erhalten wir die Wendestellen

$$
x_{1}=-1 \quad \text { und } \quad x_{2}=1
$$

Durch Einsetzen finden wir die Werte

$$
\begin{aligned}
f\left(x_{1}\right) & =f(-1)=\mathrm{e}^{-\frac{(-1)^{2}}{2}}=\mathrm{e}^{-\frac{1}{2}}=\frac{1}{\sqrt{\mathrm{e}}} \\
f^{\prime}\left(x_{1}\right) & =f^{\prime}(-1)=-(-1) \cdot \mathrm{e}^{-\frac{(-1)^{2}}{2}}=\mathrm{e}^{-\frac{1}{2}}=\frac{1}{\sqrt{\mathrm{e}}} \\
f^{\prime \prime \prime}\left(x_{1}\right) & =f^{\prime \prime \prime}(-1)=\left(3 \cdot(-1)-(-1)^{3}\right) \cdot \mathrm{e}^{-\frac{(-1)^{2}}{2}}=(-3+1) \cdot \mathrm{e}^{-\frac{1}{2}}=-\frac{2}{\sqrt{\mathrm{e}}}
\end{aligned}
$$

# --- PAGE page_6 ---

$$
\begin{aligned}
f\left(x_{2}\right) & =f(1)=\mathrm{e}^{-\frac{1^{2}}{2}}=\mathrm{e}^{-\frac{1}{2}}=\frac{1}{\sqrt{\mathrm{e}}} \\
f^{\prime}\left(x_{2}\right) & =f^{\prime}(1)=-1 \cdot \mathrm{e}^{-\frac{1^{2}}{2}}=-\mathrm{e}^{-\frac{1}{2}}=-\frac{1}{\sqrt{\mathrm{e}}} \\
f^{\prime \prime \prime}\left(x_{2}\right) & =f^{\prime \prime \prime}(1)=\left(3 \cdot 1-1^{3}\right) \cdot \mathrm{e}^{-\frac{1^{2}}{2}}=(3-1) \cdot \mathrm{e}^{-\frac{1}{2}}=\frac{2}{\sqrt{\mathrm{e}}}
\end{aligned}
$$

Wir stellen die Ergebnisse in der folgenden Tabelle zusammen.

| $k$ | $x_{k}$ | $f\left(x_{k}\right)$ | $f^{\prime}\left(x_{k}\right)$ | $f^{\prime \prime}\left(x_{k}\right)$ | $f^{\prime \prime \prime}\left(x_{k}\right)$ | Typ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | -1 | $1 / \sqrt{\mathrm{e}}$ | $+1 / \sqrt{\mathrm{e}}$ | 0 | $-2 / \sqrt{\mathrm{e}}<0$ | Wendepunkt |
| 2 | +1 | $1 / \sqrt{\mathrm{e}}$ | $-1 / \sqrt{\mathrm{e}}$ | 0 | $+2 / \sqrt{\mathrm{e}}>0$ | Wendepunkt |

# 3. Aussagen über Wendestellen 

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) Die quadratische Standardfunktion hat keine Wendestellen. | - | $\bigcirc$ |
| b) Null ist eine Wendestelle der kubischen Standardfunktion. | - | $\bigcirc$ |
| c) Gilt $f^{\prime}(3)=f^{\prime \prime}(3)=f^{\prime \prime \prime}(3)=0$ und $f^{I V}(3)<0$, dann hat $f$ an der Stelle <br> $x=3$ eine Wendestelle. | $\bigcirc$ | - |
| d) An jeder Wendestelle einer Funktion verschwindet die geometrische <br> Krümmung ihres Funktionsgraphen. | - | $\bigcirc$ |
| e) Ein Sattel punkt einer Funktion kann niemals an einer Wendestelle der <br> Funktion liegen. | $\bigcirc$ | - |

# --- PAGE page_7 ---

# 4. Torbogen 

Wir betrachten einen parabelförmigen Torbogen, der sich als Graph der Funktion

$$
f(x)=4.00 \mathrm{~m}-\frac{4.00}{9.00 \mathrm{~m}} x^{2}=: c-a \cdot x^{2}
$$

beschreiben lässt. In den Torbogen soll eine rechteckige Türe eingebaut werden, deren untere beiden Ecken auf dem Boden und obere beiden Ecken auf dem Graphen von $f$ liegen. Dabei stehen mehrere Varianten zur Diskussion. Die Situation ist in der folgenden Skizze dargestellt.


Wir bestimmen jeweils die Breite $b$ und die Höhe $h$ der Türe, welche die angegebenen Bedingungen erfüllt. In jedem Fall muss gelten
$h=f\left(\frac{b}{2}\right)=c-a \cdot\left(\frac{b}{2}\right)^{2}=c-a \cdot \frac{b^{2}}{4}=c-\frac{a}{4} \cdot b^{2}$.
Die Schnittpunkte des Torbogens mit der $x$-Achse sind gerade die Nullstellen von $f$. Diese erfüllen die Gleichung

$$
\begin{array}{rlrl} 
& 0 & =c-a \cdot x^{2} & & +a \cdot x^{2} \\
\Leftrightarrow & a \cdot x^{2} & =c & \mid: a \\
\Leftrightarrow & x^{2} & =\frac{c}{a} & \mid \pm \sqrt{\ldots}
\end{array}
$$

Daraus erhalten wir die beiden Lösungen
$x_{1,2}= \pm \sqrt{\frac{c}{a}} \approx \pm \sqrt{\frac{4.00 \mathrm{~m}}{\frac{4.00}{9.00 \mathrm{~m}}}}= \pm \sqrt{9.00 \mathrm{~m}^{2}}= \pm 3.00 \mathrm{~m}$.

# --- PAGE page_8 ---

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

# --- PAGE page_9 ---

S1 Kritische Stellen: Die erste Ableitung von $A$ ist
$A^{\prime}(z)=c \cdot 1-\frac{a}{4} \cdot 3 z^{3-1}=c-\frac{3 a}{4} \cdot z^{2}$.
Für die kritischen Stellen von $A$ gilt

$$
\begin{aligned}
0 & =A^{\prime}(z)=c-\frac{3 a}{4} \cdot z^{2} & \left\lvert\,+\frac{3 a}{4} \cdot z^{2}\right. \\
\Leftrightarrow & \frac{3 a}{4} \cdot z^{2} & =c & \left\lvert\, \frac{4}{3 a}\right. \\
\Leftrightarrow & z^{2} & =c \cdot \frac{4}{3 a}=\frac{4 c}{3 a} & \mid \sqrt{\ldots}
\end{aligned}
$$

Daraus erhalten wir die kritische Stelle
$z_{1}=\sqrt{\frac{4 c}{3 a}} \approx \sqrt{\frac{4 \cdot 4.00 \mathrm{~m}}{3 \cdot \frac{4.00}{9.00 \mathrm{~m}}}}=\sqrt{\frac{4 \cdot 4.00 \mathrm{~m} \cdot 9.00 \mathrm{~m}}{3 \cdot 4.00}}=\sqrt{4 \cdot 3.00 \mathrm{~m}^{2}}=2 \sqrt{3.00} \mathrm{~m}$.
Durch Einsetzen finden wir die Werte

$$
\begin{aligned}
& b_{1}=b\left(z_{1}\right)=z_{1} \approx 2 \sqrt{3.00} \mathrm{~m} \approx 3.46 \mathrm{~m} \\
& h_{1}=h\left(z_{1}\right)=c-\frac{a}{4} \cdot z_{1}^{2} \approx 4.00 \mathrm{~m}-\frac{\frac{4.00}{9.00 \mathrm{~m}}}{4} \cdot(2 \sqrt{3.00} \mathrm{~m})^{2}=\frac{8.00 \mathrm{~m}}{3} \approx 2.67 \mathrm{~m} \\
& A_{1}=b_{1} \cdot h_{1}=2 \sqrt{3.00} \mathrm{~m} \cdot \frac{8}{3} \cdot 1.00 \mathrm{~m} \approx 9.24 \mathrm{~m}^{2}
\end{aligned}
$$

S2 Randstellen: An den Rand stellen $z_{0}=0$ und $z_{\mathrm{E}}=6.00 \mathrm{~m}$ finden wir die Werte

$$
\begin{aligned}
& b_{0}=z_{0}=0 \\
& h_{0}=h\left(z_{0}\right)=c-\frac{a}{4} \cdot z_{0}^{2} \approx 4.00 \mathrm{~m}-\frac{\frac{4.00}{9.00 \mathrm{~m}}}{4} \cdot 0^{2}=4.00 \mathrm{~m} \\
& A_{0}=b_{0} \cdot h_{0} \approx 0 \cdot 4.00 \mathrm{~m}=0 \\
& b_{\mathrm{E}}=z_{\mathrm{E}} \approx 6.00 \mathrm{~m} \\
& h_{\mathrm{E}}=h\left(z_{\mathrm{E}}\right)=c-\frac{a}{4} \cdot z_{\mathrm{E}}^{2} \approx 4.00 \mathrm{~m}-\frac{\frac{4.00}{9.00 \mathrm{~m}}}{4} \cdot(6.00 \mathrm{~m})^{2}=0.00 \mathrm{~m} \\
& A_{\mathrm{E}}=b_{\mathrm{E}} \cdot h_{\mathrm{E}} \approx 6.00 \mathrm{~m} \cdot 0.00 \mathrm{~m}=0.00 \mathrm{~m}^{2}
\end{aligned}
$$

S3 Kandidatenvergleich: Wir stellen die Ergebnisse in der folgenden Tabelle zusammen.

| $k$ | $z_{k}$ | $b_{k}$ | $h_{k}$ | $A_{k}$ | Typ |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 0 | 0 | 0 | 4.00 m | 0 | globales Minimum |
| 1 | 3.46 m | 3.46 m | 2.67 m | $9.24 \mathrm{~m}^{2}$ | globales Maximum |
| E | 6.00 m | 6.00 m | 0.00 m | $0.00 \mathrm{~m}^{2}$ | globales Minimum |

Die Türe hat demnach genau dann die maximal mögliche Fläche, wenn gilt

$$
\underline{h}=b_{1} \approx \underline{3.46 \mathrm{~m}} \quad \text { und } \quad \underline{h}=h_{1} \approx \underline{2.67 \mathrm{~m}}
$$

Die maximal mögliche Fläche der Türe ist somit

$$
A=A_{1} \approx 9.24 \mathrm{~m}^{2}
$$

# --- PAGE page_10 ---

c) Die Fläche innerhalb des Torbogens oberhalb der Türe soll $C \approx 1.00 \mathrm{~m}^{2}$ betragen. In diesem Fall muss gelten

$$
\begin{aligned}
C & =\int_{-b / 2}^{b / 2} f(x) \mathrm{d} x-A=2 \int_{0}^{b / 2} f(x) \mathrm{d} x-b \cdot h=2 \int_{0}^{b / 2}\left(c-a \cdot x^{2}\right) \mathrm{d} x-b \cdot h \\
& =2 \cdot\left.\left(c \cdot x-\frac{a}{3} \cdot x^{3}\right)\right|_{0} ^{b / 2}-b \cdot h=2 \cdot c \cdot \frac{b}{2}-2 \cdot \frac{a}{3} \cdot\left(\frac{b}{2}\right)^{3}-b \cdot\left(c-\frac{a}{4} \cdot b^{2}\right) \\
& =c \cdot b-2 \cdot \frac{a}{3} \cdot \frac{b^{3}}{8}-b \cdot c+\frac{a}{4} \cdot b^{3}=\left(-\frac{1}{12}+\frac{1}{4}\right) \cdot a \cdot b^{3}=\frac{2}{12} \cdot a \cdot b^{3}=\frac{a}{6} \cdot b^{3}
\end{aligned}
$$

Die Breite $b$ erfüllt demnach die Gleichung

$$
\begin{array}{ll}
C=\frac{a}{6} \cdot b^{3} & \left\lvert\, \frac{6}{a}\right. \\
\Leftrightarrow & \frac{6 C}{a}=b^{3} & \mid \sqrt[3]{\ldots}
\end{array}
$$

Daraus erhalten wir

$$
\begin{aligned}
\underline{b} & =\sqrt[3]{\frac{6 C}{a}} \approx \sqrt[3]{\frac{6 \cdot 1.00 \mathrm{~m}^{2}}{\frac{4.00}{9.00 \mathrm{~m}}}}=\sqrt[3]{\frac{6 \cdot 9.00 \mathrm{~m}^{3}}{4.00}}=\sqrt[3]{13.5 \mathrm{~m}^{3}} \approx \underline{2.38 \mathrm{~m}} \\
\underline{h} & =c-\frac{a}{4} \cdot b^{2} \approx 4.00 \mathrm{~m}-\frac{\frac{4.00}{9.00 \mathrm{~m}}}{4} \cdot\left(\sqrt[3]{13.5 \mathrm{~m}^{3}}\right)^{2}=4.00 \mathrm{~m}-\frac{1}{9.00 \mathrm{~m}} \cdot\left(13.5 \mathrm{~m}^{3}\right)^{2 / 3} \\
& \approx \underline{3.37 \mathrm{~m}}
\end{aligned}
$$

# 5. Aussagen über das Verhalten einer Funktion 

Wir betrachten die Funktion

$$
\begin{aligned}
f: \mathbb{R} & \rightarrow \mathbb{R} \\
x & \mapsto f(x):=\mathrm{e}^{x} \cdot(x-1)
\end{aligned}
$$

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| b) Die Funktion $f$ hat genau eine Wendestelle. | $\bullet$ | $\bigcirc$ |
| c) Die Funktion $f$ ist injektiv. | $\bigcirc$ | $\bullet$ |
| d) Die Funktion $f^{\prime}$ hat bei $x=-1$ ein lokales Minimum. | $\bullet$ | $\bigcirc$ |
| e) Die Funktion $g(x):=\mathrm{e}^{x+1} \cdot(x-1)$ fällt nirgends steiler ab als mit einem <br> Winkel von $45^{\circ}$. | $\bullet$ | $\bigcirc$ |
| f) Für alle $x \in \mathbb{R}$ gilt $f(x) \geq-1$. | $\bullet$ | $\bigcirc$ |