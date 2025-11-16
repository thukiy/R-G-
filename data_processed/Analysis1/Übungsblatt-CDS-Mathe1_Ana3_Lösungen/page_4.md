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