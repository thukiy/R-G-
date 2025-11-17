# --- PAGE page_1 ---

# Übungsblatt Ana 3 

## 1. Aussagen über Folgen

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) Jede Folge ist eine Funktion mit ganzzahligen Argumenten. | - | $\bigcirc$ |
| b) Eine Funktion des Typs $a: \mathbb{N} \rightarrow \mathbb{N}$ beschreibt eine Folge von natürlichen <br> Zahlen. | - | $\bigcirc$ |
| c) Jede Folge hat unendlich viele, voneinander verschiedene Funktionswerte. | $\bigcirc$ | $\bullet$ |
| d) Jede reelle Zahlenfolge ist entweder eine arithmetische oder geometrische <br> Folge. | $\bigcirc$ | $\bullet$ |

## 2. Untersuchung einer einfachen Folge

Betrachten Sie die Folge, welche definiert ist durch

$$
a_{n}:=\frac{2 n}{n+1} \text { für alle } n \in \mathbb{N} \text {. }
$$

a) Wir berechnen einige Folgeglieder der Folge $a_{n}$ und stellen die Ergebnisse in einer Tabelle zusammen.

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $a_{n}$ | 0 | 1 | $\frac{4}{3}$ | $\frac{3}{2}$ | $\frac{8}{5}$ | $\frac{5}{3}$ | $\frac{12}{7}$ | $\frac{7}{4}$ | $\frac{16}{9}$ | $\frac{9}{5}$ | $\frac{20}{11}$ | $\frac{11}{6}$ | $\frac{24}{13}$ | $\frac{13}{7}$ | $\frac{28}{15}$ | $\frac{15}{8}$ |

b) Aufgrund unserer Ergebnisse aus Teilaufgabe a) vermuten wir, dass die Folge $a_{n}$ nach unten beschränkt ist durch die untere Schranke $a_{\mathrm{U}}:=0$. Für alle $n \in \mathbb{N}$ gilt offensichtlich

$$
2 n \geq n \geq 0 \quad \text { und } \quad n+1>n \geq 0
$$

Da gemäss (3) sowohl Zähler als auch Nenner in (1) positiv sind, muss gelten

$$
\underline{a_{n}}=\frac{2 n}{n+1} \geq \underline{0=a_{\mathrm{U}}}
$$

# --- PAGE page_2 ---

c) Aufgrund unserer Ergebnisse aus Teilaufgabe a) vermuten wir, dass die Folge $a_{n}$ nach oben beschränkt ist durch die obere Schranke $a_{\mathrm{O}}:=2$. Für alle $n \in \mathbb{N}$ gilt offensichtlich
$\underline{\underline{a_{n}}}=\frac{2 n}{n+1} \leq \frac{2 n+2}{n+1}=\frac{2(n+1)}{n+1}=\underline{\underline{2=a_{\mathrm{O}}}}$
d) Durch gleichnamig machen und Subtrahieren der Brüche erhalten wir die Abschätzung

$$
\begin{aligned}
& \underline{\underline{a_{n+1}-a_{n}}}=\frac{2(n+1)}{(n+1)+1}-\frac{2 n}{n+1}=\frac{2 n+2}{n+2}-\frac{2 n}{n+1}=\frac{(2 n+2)(n+1)-2 n(n+2)}{(n+2)(n+1)} \\
& =\frac{2 n^{2}+2 n+2 n+2-2 n^{2}-4 n}{(n+2)(n+1)}=\frac{2}{(n+2)(n+1)} \geq \underline{\underline{0}}
\end{aligned}
$$

e) Durch Ausklammern in Zähler und Nenner eines Faktors $n$ und Kürzen in (1) finden wir den Grenzwert

$$
a_{n}=\frac{2 n}{n+1}=\frac{n \cdot 2}{n \cdot\left(\frac{n}{n}+\frac{1}{n}\right)}=\frac{2}{\frac{n}{n}+\frac{1}{n}}=\frac{2}{1+\frac{1}{n}} \xrightarrow{n \rightarrow \infty} \frac{2}{1+0}=2
$$

Die Folge $a_{n}$ konvergiert demnach gegen den Grenzwert $\underline{a=2}$.
f) Wir berechnen die Folge $D_{n}$ der Abweichungen (Betrag der Differenz) der Folge $a_{n}$ zum Grenzwert $a=2$ aus Teilaufgabe e). Durch gleichnamig machen und Subtrahieren der Brüche erhalten wir die Abschätzung

$$
\begin{aligned}
\underline{\underline{D_{n}}} & =\left|a-a_{n}\right|=\left|2-\frac{2 n}{n+1}\right|=\left|\frac{2(n+1)-2 n}{n+1}\right|=\left|\frac{2 n+2-2 n}{n+1}\right|=\left|\frac{2}{n+1}\right| \\
& =\frac{2}{\underline{n+1}} \xrightarrow{n \rightarrow \infty} 0
\end{aligned}
$$

Die Folge $D_{n}$ konvergiert erwartungsgemäss gegen den Grenzwert $\underline{D=0}$.
g) Wir suchen ein $N \in \mathbb{N}$, so dass für alle $n \geq N$ das Folgeglied $a_{n}$ nicht weiter vom Grenzwert $a=2$ aus Teilaufgabe e) entfernt ist als die Vorgabe $\varepsilon=1 / 1^{\prime} 000^{\prime} 000$. Dazu betrachten wir den Ausdruck für die Abweichung aus Teilaufgabe f). Gemäss (8) muss gelten

$$
\begin{aligned}
D_{N}=\left|a-a_{N}\right| & \leq \varepsilon \\
\Leftrightarrow & \frac{2}{N+1} & \leq \frac{1}{1^{\prime} 000^{\prime} 000} \\
\Leftrightarrow & \frac{N+1}{2} & \geq 1^{\prime} 000^{\prime} 000 \\
\Leftrightarrow & N+1 & \geq 2^{\prime} 000^{\prime} 000
\end{aligned} \quad \left\lvert\, \begin{aligned}
& \frac{1}{(\ldots)} \\
& \mid \cdot 2 \\
& \mid-1
\end{aligned}
$$

Daraus erhalten wir die Bedingung

$$
N \geq 2^{\prime} 000^{\prime} 000-1=1^{\prime} 999^{\prime} 999
$$

Das kleinste $N \in \mathbb{N}$, welches diese Bedingung erfüllt ist offensichtlich $\underline{N=1^{\prime} 999^{\prime} 999}$.

# --- PAGE page_3 ---

# 3. Aussagen über Monotonie und Beschränktheit von Folgen 

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) Jede reelle Zahlenfolge ist entweder monoton steigend oder monoton fal- <br> lend. | $\bigcirc$ | $\bullet$ |
| b) Konstante, reelle Zahlenfolgen sind monoton steigend. | $\bullet$ | $\bigcirc$ |
| c) Eine streng monoton steigende, reelle Zahlenfolge ist niemals beschränkt. | $\bigcirc$ | $\bullet$ |
| d) Jede monoton fallende, reelle Zahlenfolge ist nach oben beschränkt. | $\bullet$ | $\bigcirc$ |
| e) Eine reelle Zahlenfolge kann niemals gleichzeitig monoton steigend und <br> monoton fallend sein. | $\bigcirc$ | $\bullet$ |
| f) Ist eine reelle Zahlenfolge $a_{n}$ monoton steigend und beschränkt, dann ist <br> die Folge $b_{n}:=n \cdot a_{n}$ monoton steigend und unbeschränkt. | $\bigcirc$ | $\bullet$ |

## 4. Eigenschaften von Folgen

Wir untersuchen, für welche der folgenden Kombinationen von Eigenschaften es eine reelle Zahlenfolge gibt, welche alle Anforderungen erfüllt. Falls möglich, geben wir ein Beispiel an.
a) Die Folge $a_{n}:=\frac{1}{n}$ für $n \in \mathbb{N}^{+}$
ist streng monoton fallend und nach unten beschränkt durch die Schranke 0.
b) Die Folge $a_{n}:=(-1)^{n}$ für $n \in \mathbb{N}$
springt ständig zwischen den Werten -1 und 1 hin und her. Sie ist damit nach unten beschränkt durch die Schranke -1, nach oben beschränkt durch die Schranke 1 und divergent.
c) Ist eine Folge streng monoton steigend, dann gilt $a_{n} \geq a_{0}$ für alle $n \in \mathbb{N}$ bzw. $a_{n} \geq a_{1}$ für alle $n \in \mathbb{N}^{+}$. Die Folge ist somit nach unten beschränkt durch das nullte bzw. erste Folgeglied als untere Schranke. Es kann daher keine Folge geben, welche sowohl monoton steigend als auch nach unten unbeschränkt ist.
d) Die Folge $a_{n}:=-\frac{1}{n}$ für $n \in \mathbb{N}^{+}$.
ist monoton steigend, nach oben beschränkt durch die Schranke 0, konvergent gegen den Grenzwert 0 und injektiv.
e) Die Folge $a_{n}:=0$ für $n \in \mathbb{N}$
bleibt konstant beim Wert 0 . Sie ist somit monoton fallend und konvergent mit Grenzwert 0 .

# --- PAGE page_4 ---

f) Jede monotone und beschränkte Folge ist gemäss Theorie konvergent. Es kann daher keine Folge geben, welche sowohl monoton steigend und beschränkt als auch divergent ist.

# 5. Aussagen über die Konvergenz von Folgen 

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :--: |
| a) Jede konvergente, reelle Zahlenfolge ist nach unten beschränkt. | $\bullet$ | $\bigcirc$ |
| b) Jede konvergente, monotone, reelle Zahlenfolge ist streng monoton. | $\bigcirc$ | $\bullet$ |
| c) Die Folge $a_{n}:=n-n^{3}$ konvergiert gegen $-\infty$. | $\bigcirc$ | $\bullet$ |
| d) Ist eine reelle Zahlenfolge streng monoton und beschränkt, dann ist sie <br> konvergent. | $\bullet$ | $\bigcirc$ |
| e) Gilt für alle Folgeglieder $a_{n}$ einer reellen Zahlenfolge dass $0<a_{n}<{ }_{n}^{1}$ <br> dann konvergiert $a_{n}$ gegen Null. | $\bullet$ | $\bigcirc$ |

## 6. Konvergenzverhalten und Grenzwerte

Wir bestimmen in jeder Teilaufgabe, ob die gegebene Folge divergiert oder konvergiert und berechnen in letzterem Fall den Grenzwert.
a) Wir betrachten die Folge

$$
a_{n}:=\frac{3}{n+2}
$$

Wir zeigen zwei Varianten, um das Verhalten der Folge zu untersuchen.
Variante 1: Durch Ausklammern in Zähler und Nenner eines Faktors $n$ und Kürzen erhalten wir

$$
a_{n}=\frac{3}{n+2}=\frac{n \cdot \frac{3}{n}}{n \cdot\left(\frac{n}{n}+\frac{2}{n}\right)}=\frac{\frac{3}{n}}{1+\frac{2}{n}} \xrightarrow{n \rightarrow \infty} \frac{0}{1+0}=0
$$

Variante 2: Offensichtlich gilt

$$
0 \leq a_{n}
$$

und durch Abschätzen nach oben erhalten wir für alle $n \geq 1$, dass

$$
a_{n}=\frac{3}{n+2} \leq \frac{3}{n}=3 \cdot \frac{1}{n} \xrightarrow{n \rightarrow \infty} 3 \cdot 0=0
$$

Die Folge konvergiert demnach gegen den Grenzwert $\underline{a}=0$.
b) Durch Abschätzen nach unten erhalten wir

$$
a_{n}:=\frac{n+2}{3} \geq \frac{n}{3}=\frac{1}{3} \cdot n \xrightarrow{n \rightarrow \infty} \infty
$$

Die Folge ist offenbar nach oben unbeschränkt und somit divergent.

# --- PAGE page_5 ---

c) Durch Ausklammern in Zähler und Nenner eines Faktors $n$ und Kürzen erhalten wir
$a_{n}:=\frac{n+2}{3 n}=\frac{n \cdot\left(\frac{n}{n}+\frac{2}{n}\right)}{n \cdot 3}=\frac{1+\frac{2}{n}}{3} \xrightarrow{n \rightarrow \infty} \frac{1+0}{3}=\frac{1}{3}$.
Die Folge konvergiert demnach gegen den Grenzwert $\underline{a=1 / 3}$.
d) Durch Ausklammern in Zähler und Nenner eines Faktors $n$ und Kürzen erhalten wir
$a_{n}:=\frac{3 n}{n+2}=\frac{n \cdot 3}{n \cdot\left(\frac{n}{n}+\frac{2}{n}\right)}=\frac{3}{1+\frac{2}{n}} \xrightarrow{n \rightarrow \infty} \frac{3}{1+0}=\frac{3}{1}=3$.
Die Folge konvergiert demnach gegen den Grenzwert $\underline{a=3}$.
e) Durch Ausklammern in Zähler und Nenner eines Faktors $n$ und Kürzen erhalten wir
$a_{n}:=\frac{3 n}{6 n+2}=\frac{n \cdot 3}{n \cdot\left(\frac{6 n}{n}+\frac{2}{n}\right)}=\frac{3}{6+\frac{2}{n}} \xrightarrow{n \rightarrow \infty} \frac{3}{6+0}=\frac{3}{6}=\frac{1}{2}$.
Die Folge konvergiert demnach gegen den Grenzwert $\underline{a=1 / 2}$.
f) Durch Faktorisieren und Kürzen sowie anschliessendem Ausklammern in Zähler und Nenner eines Faktors $n$ und Kürzen erhalten wir

$$
\begin{aligned}
a_{n} & :=\frac{4-n^{2}}{(2+n)^{2}}=\frac{(2-n) \cdot(2+n)}{(2+n) \cdot(2+n)}=\frac{2-n}{2+n}=\frac{n \cdot\left(\frac{2}{n}-\frac{n}{n}\right)}{n \cdot\left(\frac{2}{n}+\frac{n}{n}\right)}=\frac{\frac{2}{n}-1}{\frac{2}{n}+1} \xrightarrow{n \rightarrow \infty} \frac{0-1}{0+1} \\
& =\frac{-1}{1}=-1
\end{aligned}
$$

Die Folge konvergiert demnach gegen den Grenzwert $\underline{a=-1}$.
g) Durch Ausklammern in Zähler und Nenner eines Faktors $n^{2}$ und Kürzen erhalten wir

$$
\begin{aligned}
a_{n} & :=\frac{2 n-5-4 n^{2}}{3-8 n^{2}-10 n}=\frac{n^{2} \cdot\left(\frac{2 n}{n^{2}}-\frac{5}{n^{2}}-\frac{4 n^{2}}{n^{2}}\right)}{n^{2} \cdot\left(\frac{3}{n^{2}}-\frac{8 n^{2}}{n^{2}}-\frac{10 n}{n^{2}}\right)}=\frac{\frac{2}{n}-\frac{5}{n^{2}}-4}{\frac{3}{n^{2}}-8-\frac{10}{n}} \xrightarrow{n \rightarrow \infty} \frac{0-0-4}{0-8-0} \\
& =\frac{-4}{-8}=\frac{1}{2}
\end{aligned}
$$

Die Folge konvergiert demnach gegen den Grenzwert $\underline{a=1 / 2}$.
h) Durch Ausmultiplizieren des Nenners sowie anschliessendem Ausklammern in Zähler und Nenner eines Faktors $n^{2}$ und Kürzen erhalten wir

$$
\begin{aligned}
a_{n} & :=\frac{3 n^{2}+5 n+1}{(n-1)^{2}}=\frac{3 n^{2}+5 n+1}{n^{2}-2 n+1}=\frac{n^{2} \cdot\left(\frac{3 n^{2}}{n^{2}}+\frac{5 n}{n^{2}}+\frac{1}{n^{2}}\right)}{n^{2} \cdot\left(\frac{n^{2}}{n^{2}}-\frac{2 n}{n^{2}}+\frac{1}{n^{2}}\right)}=\frac{3+\frac{5}{n}+\frac{1}{n^{2}}}{1-\frac{2}{n}+\frac{1}{n^{2}}} \\
& \xrightarrow{n \rightarrow \infty} \frac{3+0+0}{1-0+0}=\frac{3}{1}=3
\end{aligned}
$$

Die Folge konvergiert demnach gegen den Grenzwert $\underline{a=3}$.

# --- PAGE page_6 ---

i) Durch Ausklammern in Zähler und Nenner eines Faktors $n^{4}$ und Kürzen erhalten wir

$$
\begin{aligned}
a_{n} & :=\frac{10^{12}-5 n^{2}+6 n^{3}+10^{10} n}{5-7 n^{4}-5 n^{2}}=\frac{n^{4} \cdot\left(\frac{10^{12}}{n^{4}}-\frac{5 n^{2}}{n^{4}}+\frac{6 n^{3}}{n^{4}}+\frac{10^{10} n}{n^{4}}\right)}{n^{4} \cdot\left(\frac{5}{n^{4}}-\frac{7 n^{4}}{n^{4}}-\frac{5 n^{2}}{n^{4}}\right)} \\
& =\frac{\frac{10^{12}}{n^{4}}-\frac{5}{n^{2}}+\frac{6}{n}+\frac{10^{10}}{n^{4}}}{\frac{5}{n^{4}}-7-\frac{5}{n^{2}}} \xrightarrow{n \rightarrow \infty} \frac{0-0+0+0}{0-7-0}=0
\end{aligned}
$$

Die Folge konvergiert demnach gegen den Grenzwert $\underline{a=0}$.
j) Durch Ausklammern in Zähler und Nenner eines Faktors $3^{n}$ und Kürzen erhalten wir

$$
\begin{aligned}
a_{n} & :=\frac{2^{n}+3}{3^{n}+2}-1=\frac{3^{n} \cdot\left(\frac{2^{n}}{3^{n}}+\frac{3}{3^{n}}\right)}{3^{n} \cdot\left(\frac{3^{n}}{3^{n}}+\frac{2}{3^{n}}\right)}-1=\frac{\left(\frac{2}{3}\right)^{n}+\frac{3}{3^{n}}}{1+\frac{2}{3^{n}}}-1 \xrightarrow{n \rightarrow \infty} \frac{0+0}{1+0}-1 \\
& =0-1=-1
\end{aligned}
$$

Die Folge konvergiert demnach gegen den Grenzwert $\underline{a=-1}$.
k) Durch Ausklammern in Zähler und Nenner eines Faktors $3^{n}$ und Kürzen erhalten wir

$$
\begin{aligned}
a_{n} & :=\frac{3+n^{100}+2^{n}}{n^{2}-3^{n}-2}+4=\frac{3^{n} \cdot\left(\frac{3}{3^{n}}+\frac{n^{100}}{3^{n}}+\frac{2^{n}}{3^{n}}\right)}{3^{n} \cdot\left(\frac{n^{2}}{3^{n}}-\frac{3^{n}}{3^{n}}-\frac{2}{3^{n}}\right)}+4=\frac{\frac{3}{3^{n}}+\frac{n^{100}}{3^{n}}+\left(\frac{2}{3}\right)^{n}}{\frac{n^{2}}{3^{n}}-1-\frac{2}{3^{n}}}+4 \\
& \xrightarrow{n \rightarrow \infty} \frac{0+0+0}{0-1-0}+4=0+4=4
\end{aligned}
$$

Die Folge konvergiert demnach gegen den Grenzwert $\underline{a=4}$.
l) Durch Ausklammern in Zähler und Nenner eines Faktors $n^{3}$ und Kürzen erhalten wir

$$
\begin{aligned}
a_{n} & :=\frac{2+\frac{6 n^{6}}{2+3 n^{3}}-7 n^{3}}{n+(1+n)^{3}}=\frac{2+\frac{n^{3}, \frac{6 n^{6}}{2}}{n^{3} \cdot\left(\frac{2}{n^{3}}+\frac{3 n^{3}}{n^{3}}\right)}-7 n^{3}}{n+1+3 n+3 n^{2}+n^{3}}=\frac{2+\frac{6 n^{3}}{2} \frac{2}{n^{3}}+3}-7 n^{3}}{1+4 n+3 n^{2}+n^{3}} \\
& =\frac{n^{3} \cdot\left(\frac{2}{n^{3}}+\frac{6 n^{3}}{n^{3}\left(\frac{1}{n^{3}}+3\right)}-\frac{7 n^{3}}{n^{3}}\right)}{n^{3} \cdot\left(\frac{1}{n^{3}}+\frac{4 n}{n^{3}}+\frac{3 n^{2}}{n^{3}}+\frac{n^{3}}{n^{3}}\right)}=\frac{\frac{2}{n^{3}}+\frac{6}{n^{3}+3}-7}{\frac{1}{n^{3}}+\frac{4}{n^{3}}+\frac{3}{n}+1} \xrightarrow{n \rightarrow \infty} \frac{0+\frac{6}{0+3}-7}{0+0+0+1} \\
& =\frac{2-7}{1}=-5
\end{aligned}
$$

Die Folge konvergiert demnach gegen den Grenzwert $\underline{a=-5}$.

# --- PAGE page_7 ---

# 7. Grenzwerte berechnen mit Python/Sympy 

Wir berechnen die Grenzwerte aus Aufgabe 6 mit Python/Sympy. Dazu implementieren wir den folgenden Code, den wir für jede Teilaufgabe modifizieren.

```
# Python initialisieren:
import IPython.display as dp;
import sympy as sp;
# Python konfigurieren:
sp.init_printing();
a,n=sp.symbols('a,n');
# Parameter:
a_n=...;
# Berechnungen:
a=sp.limit_seq(a_n,n);
# Ausgabe:
dp.display(a_n);
dp.display(a);
```

a) Wir modifizieren den Code.
\# Parameter:
$\mathrm{a} \_\mathrm{n}=3 /(\mathrm{n}+2)$
Gemäss Ausgabe konvergiert die Folge gegen den Grenzwert $\underline{a}=\underline{0}$.
b) Wir modifizieren den Code.
\# Parameter:
$\mathrm{a} \_\mathrm{n}=(\mathrm{n}+2) / 3$
Gemäss Ausgabe divergiert die Folge.
c) Wir modifizieren den Code.
\# Parameter:
$\mathrm{a} \_\mathrm{n}=(\mathrm{n}+2) /(3 * \mathrm{n})$;
Gemäss Ausgabe konvergiert die Folge gegen den Grenzwert $\underline{a}=\underline{\underline{1}}$.
d) Wir modifizieren den Code.
\# Parameter:
$\mathrm{a} \_\mathrm{n}=3 * \mathrm{n} /(\mathrm{n}+2)$
Gemäss Ausgabe konvergiert die Folge gegen den Grenzwert $\underline{a}=\underline{3}$.
e) Wir modifizieren den Code.
\# Parameter:
$\mathrm{a} \_\mathrm{n}=3 * \mathrm{n} /(6 * \mathrm{n}+2)$
Gemäss Ausgabe konvergiert die Folge gegen den Grenzwert $\underline{a}=\underline{\underline{1}}$.
f) Wir modifizieren den Code.
\# Parameter:
$\mathrm{a} \_\mathrm{n}=(4-\mathrm{n} * * 2) /(2+\mathrm{n}) * * 2$;

# --- PAGE page_8 ---

Gemäss Ausgabe konvergiert die Folge gegen den Grenzwert $\underline{a=-1}$.
g) Wir modifizieren den Code.
\# Parameter:
$a_{-} n=\left(2 * n-5-4 * n * * 2\right) /(3-8 * n * * 2-10 * n)$;
Gemäss Ausgabe konvergiert die Folge gegen den Grenzwert $\underline{a}=\frac{1}{2}$.
h) Wir modifizieren den Code.
\# Parameter:
$a_{-} n=\left(3 * n * * 2+5 * n+1\right) /(n-1) * * 2$;
Gemäss Ausgabe konvergiert die Folge gegen den Grenzwert $\underline{a=3}$.
i) Wir modifizieren den Code.
\# Parameter:
$a_{-} n=\left(10 * * 12-5 * n * * 2+6 * n * * 3+10 * * 10 * n\right) /\left(5-7 * n * * 4-5 * n * * 2\right)$;
Gemäss Ausgabe konvergiert die Folge gegen den Grenzwert $\underline{a=0}$.
j) Wir modifizieren den Code.
\# Parameter:
$a_{-} n=\left(2 * * n+3\right) /(3 * * n+2)-1$;
Gemäss Ausgabe konvergiert die Folge gegen den Grenzwert $\underline{a=-1}$.
k) Wir modifizieren den Code.
\# Parameter:
$a_{-} n=\left(3+n * * 100+2 * * n\right) /\left(n * * 2-3 * * n-2\right)+4$;
Gemäss Ausgabe konvergiert die Folge gegen den Grenzwert $\underline{a=4}$.
I) Wir modifizieren den Code.
\# Parameter:
$a_{-} n=\left(2+6 * n * * 6 /\left(2+3 * n * * 3\right)-7 * n * * 3\right) /(n+(1+n) * * 3)$;
Gemäss Ausgabe konvergiert die Folge gegen den Grenzwert $\underline{a=-5}$.

# 8. Aussagen über eine explizit definierte Folge 

Wir betrachten die Folge, welche definiert ist durch

$$
a_{n}:=\frac{7 n^{123}+123 n^{7}+18 n^{73}+73 n^{18}+789 \sqrt{n}+45}{\sqrt[3]{n}+9 n^{23}+23 n^{9}+18 n^{73}+73 n^{18}+7 n^{123}+123 n^{7}+54} \text { für } n \in \mathbb{N}
$$

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :--: |
| a) Es gilt $a_{0}=0$. | $\bigcirc$ | $\bullet$ |
| b) Die Folge $a_{n}$ ist eine arithmetische Folge. | $\bigcirc$ | $\bullet$ |
| c) Die Folge $a_{n}$ ist eine geometrische Folge. | $\bigcirc$ | $\bullet$ |
| d) Die Folge $a_{n}$ divergiert gegen $\infty$. | $\bigcirc$ | $\bullet$ |
| e) Die Folge $a_{n}$ ist beschränkt. | $\bullet$ | $\bigcirc$ |
| f) Die Folge $a_{n}$ konvergiert gegen 1. | $\bullet$ | $\bigcirc$ |

# --- PAGE page_9 ---

# 9. Aussagen über die Konvergenz von Folgen 

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) Die Folge $a_{n}:=n^{3}$ konvergiert gegen $\infty$. | $\bigcirc$ | $\bullet$ |
| b) Jede beschränkte, reelle Zahlenfolge ist konvergent. | $\bigcirc$ | $\bullet$ |
| c) Jede konvergente, reelle Zahlenfolge ist monoton. | $\bigcirc$ | $\bullet$ |
| d) Ist eine reelle Zahlenfolge monoton und beschränkt, dann ist sie konver- <br> gent. | $\bullet$ | $\bigcirc$ |
| e) Eine streng monoton steigende, konvergente, reelle Zahlenfolge nähert sich <br> ihrem Grenzwert an, ohne ihn jemals anzunehmen. | $\bullet$ | $\bigcirc$ |