# --- PAGE page_1 ---

# Übungsblatt Ana 4 

## 1. Aussagen über Summen und das Summen-Zeichen

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :--: | :--: |
| a) Das Summen-Zeichen ist ein vergrössertes altgriechisches Sigma. | $\bullet$ | $\bigcirc$ |
| b) Mit Hilfe des Summen-Zeichens kann jede Summe mit vielen Summanden <br> effizient geschrieben werden. | $\bigcirc$ | $\bullet$ |
| c) Mit Hilfe des Summen-Zeichens kann eine geeignete Summe mit vielen <br> gleichartigen Summanden effizient geschrieben werden. | $\bullet$ | $\bigcirc$ |
| d) Mit Hilfe des Summen-Zeichens kann eine geeignete Summe mit vielen <br> gleichartigen Summanden effizient berechnet werden. | $\bigcirc$ | $\bullet$ |
| e) Es gilt $\sum_{k=1}^{3} k=6$. | $\bullet$ | $\bigcirc$ |
| f) Es gilt $\sum_{k=7}^{500}\left(3 k^{2}+6 k^{3}\right)=3 \sum_{k=7}^{500}\left(k^{2}+2 k^{3}\right)$. | $\bullet$ | $\bigcirc$ |

## 2. Summen ausschreiben und berechnen

Wir berechnen, die folgenden Summen.
a) Wir erhalten

$$
\sum_{k=1}^{10} k=4+5+6+7+8+9+10=\underline{\underline{49}}
$$

b) Wir zeigen mehrere Varianten, um diese Teilaufgabe zu bearbeiten.

Variante 1: Wir erhalten

$$
\begin{aligned}
\sum_{\underline{k=4}}^{10} 2 k & =2 \cdot 4+2 \cdot 5+2 \cdot 6+2 \cdot 7+2 \cdot 8+2 \cdot 9+2 \cdot 10 \\
& =8+10+12+14+16+18+20=\underline{\underline{98}}
\end{aligned}
$$

Variante 2: Durch Ausklammern von 2 erhalten wir

$$
\underline{\sum_{k=4}^{10} 2 k}=2 \sum_{k=4}^{10} k=2 \cdot(4+5+6+7+8+9+10)=2 \cdot 49=\underline{\underline{98}}
$$

# --- PAGE page_2 ---

c) Wir erhalten

$$
\underline{\sum_{k=-2}^{2} k^{3}}=(-2)^{3}+(-1)^{3}+0^{3}+1^{3}+2^{3}=-8-1+0+1+8=\underline{0}
$$

d) Wir erhalten

$$
\underline{\sum_{k=2}^{4} \frac{1}{k}}=\frac{1}{2}+\frac{1}{3}+\frac{1}{4}=\frac{6}{12}+\frac{4}{12}+\frac{3}{12}=\frac{6+4+3}{12}=\frac{13}{\underline{12}}
$$

e) Wir erhalten

$$
\sum_{\substack{k=0}}^{4} 2^{k}=2^{0}+2^{1}+2^{2}+2^{3}+2^{4}=1+2+4+8+16=\underline{31}
$$

f) Wir erhalten

$$
\begin{aligned}
\sum_{k=4}^{9}(-1)^{k} k & =(-1)^{4} \cdot 4+(-1)^{5} \cdot 5+(-1)^{6} \cdot 6+(-1)^{7} \cdot 7+(-1)^{8} \cdot 8+(-1)^{9} \cdot 9 \\
& =1 \cdot 4+(-1) \cdot 5+1 \cdot 6+(-1) \cdot 7+1 \cdot 8+(-1) \cdot 9 \\
& =4-5+6-7+8-9=\underline{-3}
\end{aligned}
$$

# 3. Summen berechnen mit Python/Sympy 

Wir berechnen die Summen aus Aufgabe 2 mit Python/Sympy. Dazu implementieren wir den folgendne Code, den wir für jede Teilaufgabe modifizieren:

```
# Python initialisieren:
import IPython.display as dp;
import sympy as sp;
# Python konfigurieren:
sp.init_printing();
k,S=sp.symbols('k,S');
# Berechnungen:
S=sp.summation(...,(...,...,...));
# Ausgabe:
dp.display(S);
```

a) Wir modifizieren den Code.

```
# Berechnungen:
S=sp.summation(k,(k,4,10));
```

Gemäss Ausgabe ist $\underline{S=49}$.
b) Wir modifizieren den Code.

```
# Berechnungen:
S=sp.summation(2*k,(k,4,10));
```

# --- PAGE page_3 ---

Gemäss Ausgabe ist $\underline{S=98}$.
c) Wir modifizieren den Code.
\# Berechnungen:
S=sp.summation(k**3,(k,-2,
Gemäss Ausgabe ist $\underline{S=0}$.
d) Wir modifizieren den Code.
\# Berechnungen:
S=sp.summation $(1 / k,(k, 2,4))$;
Gemäss Ausgabe ist $\underline{S=\frac{13}{12}}$.
e) Wir modifizieren den Code.
\# Berechnungen:
S=sp.summation $(2 * * k,(k, 0,4))$;
Gemäss Ausgabe ist $\underline{S=31}$.
f) Wir modifizieren den Code.
\# Berechnungen:
S=sp.summation((-1)**k*k,(k,4,9));]
Gemäss Ausgabe ist $\underline{S=-3}$.

# 4. Summen mit dem Summen-Zeichen darstellen 

Wir schreiben die folgenden Summen mit Hilfe des Summen-Zeichens.
a) Wir erhalten

$$
4+5+6+7+8+9+10+11=\sum_{k=4}^{11} k
$$

b) Wir erhalten

$$
0+2+4+6+8+10=\sum_{k=0}^{5} 2 k
$$

c) Wir erhalten

$$
1+3+5+7+9+11=\sum_{k=0}^{5}(2 k+1)=\sum_{k=1}^{6}(2 k-1)
$$

d) Wir erhalten

$$
1-3+5-7+9-11=\sum_{k=0}^{5}(-1)^{k}(2 k+1)
$$

# --- PAGE page_4 ---

e) Wir erhalten

$$
\frac{1}{6}+\frac{1}{8}+\frac{1}{10}+\frac{1}{12}+\frac{1}{14}=\sum_{k=3}^{7} \frac{1}{2 k}
$$

f) Wir erhalten

$$
\frac{1}{25}+\frac{1}{36}+\frac{1}{49}+\frac{1}{64}+\frac{1}{81}=\sum_{k=5}^{9} \frac{1}{k^{2}}
$$

# 5. Aussagen über eine Summe 

Wir betrachten die Summe

$$
S=\sum_{k=a}^{N}\left(2 k^{2}-4 k\right)
$$

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) Für $a=3$ und $N=6$ besteht die Summe aus sechs gleichartigen Sum- <br> manden. | $\bigcirc$ | $\bullet$ |
| b) Sinnvollerweise könnte ein Faktor 2 vor das Summen-Zeichen gezogen <br> werden. | $\bullet$ | $\bigcirc$ |
| c) Die Summe $S$ ist eine ungerade Zahl. | $\bigcirc$ | $\bullet$ |
| d) Für $N=-a$ verschwindet die Summe $S$. | $\bigcirc$ | $\bullet$ |
| e) Die Summe $S$ besteht aus $2 \cdot(N-k)$ Summanden. | $\bigcirc$ | $\bullet$ |
| f) Für $a=3$ und $N=6$ gilt $S=100$. | $\bullet$ | $\bigcirc$ |

## 6. Summen ausschreiben und berechnen

Wir berechnen, falls möglich, die folgenden Summen.
a) Wir zeigen mehrere Varianten, um diese Teilaufgabe zu bearbeiten.

Variante 1: Wir erhalten

$$
\begin{aligned}
\underline{\sum_{k=-3}^{1}\left(k^{2}+1\right)} & =\left((-3)^{2}+1\right)+\left((-2)^{2}+1\right)+\left((-1)^{2}+1\right)+\left(0^{2}+1\right)+\left(1^{2}+1\right) \\
& =9+1+4+1+1+1+0+1+1+1=\underline{20}
\end{aligned}
$$

Variante 2: Durch Aufteilen der Summanden erhalten wir

$$
\begin{aligned}
\underline{\sum_{k=-3}^{1}\left(k^{2}+1\right)} & =\sum_{k=-3}^{1} k^{2}+\sum_{k=-3}^{1} 1 \\
& =(-3)^{2}+(-2)^{2}+(-1)^{2}+0^{2}+1^{2}+(1-(-3)+1) \cdot 1 \\
& =9+4+1+0+1+5=\underline{20}
\end{aligned}
$$

# --- PAGE page_5 ---

b) Wir erhalten

$$
\underline{\sum_{k=-3}^{1} k^{2}+1}=(-3)^{2}+(-2)^{2}+(-1)^{2}+0^{2}+1^{2}+1=9+4+1+0+1+1=\underline{\underline{16}}
$$

c) Wir erhalten

$$
\sum_{k=-3}^{3} \frac{1}{k}=\frac{1}{-3}+\frac{1}{-2}+\frac{1}{-1}+\frac{1}{0}+\frac{1}{1}+\frac{1}{2}+\frac{1}{3}=?
$$

Diese Summe enthält formell eine Division durch 0 und ist daher nicht definiert.
d) Durch Ausklammern von $1 / l$ aus der inneren Summe erhalten wir

$$
\begin{aligned}
\underline{\sum_{l=1}^{3} \sum_{k=0}^{3} \frac{k}{l}} & =\sum_{l=1}^{3} \frac{1}{l} \sum_{k=0}^{3} k=\sum_{l=1}^{3} \frac{1}{l} \cdot(0+1+2+3)=\sum_{l=1}^{3} \frac{1}{l} \cdot 6=\frac{1}{1} \cdot 6+\frac{1}{2} \cdot 6+\frac{1}{3} \cdot 6 \\
& =6+3+2=\underline{\underline{11}}
\end{aligned}
$$

# 7. Summen mit dem Summen-Zeichen darstellen 

Wir schreiben die folgenden Summen mit Hilfe des Summen-Zeichens.
a) Wir erhalten

$$
\underline{\underline{S}}=\frac{1}{2}-\frac{1}{3}+\frac{1}{4}-\frac{1}{5}+\frac{1}{6}-\frac{1}{7}+\frac{1}{8}-\frac{1}{9}=\underline{\underline{\sum_{k=2}^{9} \frac{(-1)^{k}}{k}}}
$$

b) Wir erhalten

$$
\underline{\underline{S}}=1+2-3-4+5+6-7-8+9+10=\underline{\sum_{k=0}^{4}(-1)^{k} \sum_{l=1}^{2}(2 k+l)}
$$

## 8. Geometrische Summen-Formel

Es seien $m, n \in \mathbb{N}$ mit $m<n$ und $x \in \mathbb{R} \backslash\{0,1\}$. Eine geometrische Summe ist eine Summe der Form

$$
G_{(m ; n)}(x):=\sum_{k=m}^{n} x^{k}
$$

a) Wir schreiben die folgenden, geometrischen Summen ohne Summen-Zeichen aus.
i) Wir erhalten

$$
\underline{G_{(1 ; 4)}(3)}=\sum_{k=1}^{4} 3^{k}=3^{1}+3^{2}+3^{3}+3^{4}=3+9+27+81=\underline{\underline{120}}
$$

# --- PAGE page_6 ---

ii) Wir erhalten

$$
\underline{G_{(2 ; 5)}(2)}=\sum_{k=2}^{5} 2^{k}=2^{2}+2^{3}+2^{4}+2^{5}=4+8+16+32=\underline{\underline{60}}
$$

iii) Wir erhalten

$$
\underline{G_{(12 ; 17)}(7)}=\sum_{k=12}^{17} 7^{k}=\underline{7^{12}+7^{13}+7^{14}+7^{15}+7^{16}+7^{17}}
$$

iv) Wir erhalten

$$
\underline{G_{(12 ; 17)}(x)}=\sum_{k=12}^{17} x^{k}=\underline{x^{12}+x^{13}+x^{14}+x^{15}+x^{16}+x^{17}}
$$

b) Wir berechnen die folgenden Produkte, indem wir jeweils die geometrische Summe ohne Summen-Zeichen ausschreiben und dann ausmultiplizieren
i) Wir erhalten

$$
\begin{aligned}
\underline{(1-x) \cdot G_{(5 ; 6)}(x)} & =(1-x) \cdot\left(x^{5}+x^{6}\right)=1 \cdot x^{5}-x \cdot x^{5}+1 \cdot x^{6}-x \cdot x^{6} \\
& =x^{5}-x^{6}+x^{6}-x^{7} \\
& =\underline{x^{5}-x^{7}}
\end{aligned}
$$

ii) Wir erhalten

$$
\begin{aligned}
\underline{(1-x) \cdot G_{(5 ; 8)}(x)} & =(1-x) \cdot\left(x^{5}+x^{6}+x^{7}+x^{8}\right) \\
& =x^{5}-x^{6}+x^{6}-x^{7}+x^{7}-x^{8}+x^{8}-x^{9} \\
& =\underline{x^{5}-x^{9}}
\end{aligned}
$$

iii) Wir erhalten

$$
\begin{aligned}
\underline{(1-x) \cdot G_{(2 ; 6)}(x)} & =(1-x) \cdot\left(x^{2}+x^{3}+x^{4}+x^{5}+x^{6}\right) \\
& =x^{2}-x^{3}+x^{3}-x^{4}+x^{4}-x^{5}+x^{5}-x^{6}+x^{6}-x^{7} \\
& =\underline{x^{2}-x^{7}}
\end{aligned}
$$

iv) Wir erhalten

$$
\begin{aligned}
\underline{(1-x) \cdot G_{(2 ; 8)}(x)}= & (1-x) \cdot\left(x^{2}+x^{3}+x^{4}+x^{5}+x^{6}+x^{7}+x^{8}\right) \\
= & x^{2}-x^{3}+x^{3}-x^{4}+x^{4}-x^{5}+x^{5}-x^{6}+x^{6}-x^{7}+x^{7} \\
& -x^{8}+x^{8}-x^{9} \\
= & \underline{x^{2}-x^{9}}
\end{aligned}
$$

# --- PAGE page_7 ---

v) Wir erhalten

$$
\begin{aligned}
\underline{(1-x) \cdot G_{(1 ; 9)}(x)}= & (1-x) \cdot\left(x+x^{2}+x^{3}+x^{4}+x^{5}+x^{6}+x^{7}+x^{8}+x^{9}\right) \\
= & x-x^{2}+x^{2}-x^{3}+x^{3}-x^{4}+x^{4}-x^{5}+x^{5}-x^{6}+x^{6} \\
& -x^{7}+x^{7}-x^{8}+x^{8}-x^{9}+x^{9}-x^{10} \\
= & \underline{x-x^{10}}
\end{aligned}
$$

vi) Wir erhalten

$$
\begin{aligned}
\underline{(1-x) \cdot G_{(13 ; 16)}(x)}= & (1-x) \cdot\left(x^{13}+x^{14}+x^{15}+x^{16}\right) \\
= & x^{13}-x^{14}+x^{14}-x^{15}+x^{15}-x^{16}+x^{16}-x^{17} \\
= & \underline{x^{13}-x^{17}}
\end{aligned}
$$

c) Bei der Multiplikation einer geometrischen Summe $G_{(m ; n)}(x)$ mit dem Faktor $(1-x)$ in Teilaufgabe b) beobachten wir, dass nur gerade die Terme $x^{m}$ und $-x^{n+1}$ übrig bleiben, während alle anderen Terme sich gegenseitig kompensieren. Allgemein gilt

$$
\begin{aligned}
\underline{(1-x) \cdot G_{(m ; n)}(x)}= & (1-x) \cdot\left(x^{m}+x^{m+1}+\ldots+x^{n-1}+x^{n}\right) \\
& =x^{m}-x^{m+1}+x^{m+1}-\ldots-x^{n-1}+x^{n-1}-x^{n}+x^{n}-x^{n+1} \\
& =\underline{x^{m}-x^{n+1}}
\end{aligned}
$$

d) Durch Auflösen der Formel (33) nach $G_{(m ; n)}(x)$ können wir die geometrische SummenFormel herleiten. Für $(1-x) \neq 0$ gilt

$$
(1-x) \cdot G_{(m ; n)}(x)=x^{m}-x^{n+1} \quad \mid:(1-x)
$$

Daraus erhalten wir

$$
\underline{G_{(m ; n)}(x)}=\frac{x^{m}-x^{n+1}}{1-x}
$$

e) Wir wenden die geometrische Summen-Formel aus (35) an, um die folgenden geometrischen Summen zu berechnen.
i) Wir erhalten

$$
\underline{G_{(0 ; 5)}(3)}=\frac{3^{0}-3^{5+1}}{1-3}=\frac{1-729}{-2}=\frac{728}{2}=\underline{364}
$$

ii) Wir erhalten

$$
\underline{G_{\left(1 ; 2^{\prime} 539\right)}(-1)}=\frac{(-1)^{1}-(-1)^{2^{\prime} 539+1}}{1-(-1)}=\frac{-1-1}{2}=\frac{-2}{2}=\underline{-1}
$$

iii) Wir erhalten

$$
\sum_{k=0}^{10} 2^{k}=G_{(0 ; 10)}(2)=\frac{2^{0}-2^{10+1}}{1-2}=\frac{1-2^{\prime} 048}{-1}=2^{\prime} 048-1=\underline{2^{\prime} 047}
$$

# --- PAGE page_8 ---

iv) Wir erhalten

$$
\begin{aligned}
& \sum_{k=2}^{11}\left(\frac{1}{2}\right)^{k}=G_{(2 ; 11)}\left(\frac{1}{2}\right)=\frac{\left(\frac{1}{2}\right)^{2}-\left(\frac{1}{2}\right)^{11+1}}{1-\frac{1}{2}}=\frac{\frac{1}{27}-\frac{1}{2^{12}}}{\frac{1}{2}}=2 \cdot\left(\frac{1}{2^{2}}-\frac{1}{2^{12}}\right) \\
& =\frac{1}{2}-\frac{1}{2^{11}}=\frac{2^{10}}{2^{11}}-\frac{1}{2^{11}}=\frac{2^{10}-1}{2^{11}}=\frac{1^{\prime} 024-1}{2^{\prime} 048}=\frac{1^{\prime} 023}{2^{\prime} 048}
\end{aligned}
$$

f) Wir betrachten geometrische Summen für die Fälle $x=0$ und $x=1$.

Fall 1: $x=0$. Wird in diesem Fall $m=0$ gewählt, dann kann die Formel aus (22) nicht angewendet werden, weil darin der nicht definierte Term $0^{0}$ auftritt. Formal erhalten wir nämlich

$$
G_{(0 ; n)}(0):=\underbrace{0^{0}}_{=?}+0^{1}+\ldots+0^{n}=?
$$

Fall 2: $x=1$. In diesem Fall kann die geometrische Summen-Formel aus (35) nicht angewendet werden, weil der Nenner $(1-x)$ nicht verschwinden darf.
Um diese Schwierigkeiten zu vermeiden, wurde bei der Definition der geometrischen Summe in (22) sinnvollerweise die Bedingung $x \notin\{0,1\}$ vorausgesetzt.

# 9. Aussagen über geometrische Summen 

Es seien $x, y \in \mathbb{R} \backslash\{0,1\}$ und $m, n \in \mathbb{N}^{+}$mit $m<n$.

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) In jedem Fall gilt $G_{(0 ; n)}(x+y) \in \mathbb{R}$. | $\bigcirc$ | $\bullet$ |
| b) In jedem Fall gilt $G_{(10 ; 30)}(x)=G_{(10 ; 20)}(x)+G_{(20 ; 30)}(x)$. | $\bigcirc$ | $\bullet$ |
| c) In jedem Fall gilt $G_{(m ; n)}(x+y)=G_{(m ; n)}(x)+G_{(m ; n)}(y)$. | $\bigcirc$ | $\bullet$ |
| d) In jedem Fall gilt $G_{(m ; n)}(y)<G_{(m ; n+1)}(y)$. | $\bigcirc$ | $\bullet$ |
| e) In jedem Fall gilt $G_{(m+7 ; n+7)}(x)=x^{7} \cdot G_{(m ; n)}(x)$. | $\bullet$ | $\bigcirc$ |
| f) In jedem Fall gilt $G_{(m ; n)}\left(x^{2}\right)=G_{(2 m ; 2 n)}(x)$. | $\bigcirc$ | $\bullet$ |

## 10. Geometrische Summen berechnen

Wir berechnen die folgenden geometrischen Summen.
a) Es gilt

$$
\underline{A}=\sum_{k=0}^{12} 2^{k}=G_{(0 ; 12)}(2)=\frac{2^{0}-2^{12+1}}{1-2}=\frac{1-8^{\prime} 192}{1-2}=\frac{-8^{\prime} 191}{-1}=\underline{8^{\prime} 191}
$$

b) Es gilt

$$
\begin{aligned}
\underline{B} & =\sum_{k=1}^{10} 2 \cdot 3^{k}=2 \sum_{k=1}^{10} 3^{k}=2 G_{(1 ; 10)}(3)=2 \cdot \frac{3^{1}-3^{10+1}}{1-3}=2 \cdot \frac{3-177^{\prime} 147}{1-3} \\
& =2 \cdot \frac{-177^{\prime} 144}{-2}=\underline{177^{\prime} 144}
\end{aligned}
$$

# --- PAGE page_9 ---

c) Es gilt

$$
\begin{aligned}
\underline{C} & =\sum_{k=0}^{9} \sqrt{3^{k}}=\sum_{k=0}^{9}(\sqrt{3})^{k}=G_{(0 ; 9)}(\sqrt{3})=\frac{(\sqrt{3})^{0}-(\sqrt{3})^{9+1}}{1-\sqrt{3}}=\frac{1-(\sqrt{3})^{10}}{1-\sqrt{3}} \\
& =\frac{1-(\sqrt{3})^{2 \cdot 5}}{1-\sqrt{3}}=\frac{1-3^{5}}{1-\sqrt{3}}=\frac{1-243}{1-\sqrt{3}}=\frac{242}{\sqrt{3}-1} \approx \underline{331}
\end{aligned}
$$

d) Es gilt

$$
\begin{aligned}
\underline{D} & =\sum_{k=0}^{8} \frac{4}{2^{k+1}}=\sum_{k=0}^{8} \frac{4}{2 \cdot 2^{k}}=\sum_{k=0}^{8} \frac{2}{2^{k}}=2 \sum_{k=0}^{8} \frac{1}{2^{k}}=2 \sum_{k=0}^{8}\left(\frac{1}{2}\right)^{k}=2 G_{(0 ; 8)}\left(\frac{1}{2}\right) \\
& =2 \cdot \frac{\left(\frac{1}{2}\right)^{0}-\left(\frac{1}{2}\right)^{8+1}}{1-\frac{1}{2}}=2 \cdot \frac{1-\frac{1}{2^{9}}}{\frac{1}{2}}=2 \cdot 2 \cdot\left(1-\frac{1}{2^{9}}\right)=\frac{2^{11}}{2^{9}}-\frac{2^{2}}{2^{9}}=\frac{2^{9}}{2^{7}}-\frac{1}{2^{7}} \\
& =\frac{512-1}{128}=\frac{511}{128} \approx \underline{3.99}
\end{aligned}
$$

e) Es gilt

$$
\begin{aligned}
\underline{E} & =\sum_{k=2}^{5} \frac{10 \sqrt{3^{4 k}}}{5^{k+1}}=\sum_{k=2}^{5} \frac{10 \cdot 3^{\frac{4 k}{2}}}{5 \cdot 5^{k}}=\sum_{k=2}^{5} 2 \cdot \frac{3^{2 k}}{5^{k}}=2 \sum_{k=2}^{5} \frac{9^{k}}{5^{k}}=2 \sum_{k=2}^{5}\left(\frac{9}{5}\right)^{k} \\
& =2 G_{(2 ; 5)}\left(\frac{9}{5}\right)=2 \cdot \frac{\left(\frac{9}{5}\right)^{2}-\left(\frac{9}{5}\right)^{5+1}}{1-\frac{9}{5}}=2 \cdot \frac{\left(\frac{9}{5}\right)^{2}-\left(\frac{9}{5}\right)^{6}}{-\frac{4}{5}}=\frac{5 \cdot 2}{4} \cdot\left(\left(\frac{9}{5}\right)^{6}-\left(\frac{9}{5}\right)^{2}\right) \\
& =\frac{5}{2} \cdot\left(\frac{9^{6}}{5^{6}}-\frac{9^{2}}{5^{2}}\right)=\frac{1}{2} \cdot\left(\frac{9^{6}}{5^{5}}-\frac{9^{2}}{5}\right)=\frac{1}{2} \cdot\left(\frac{9^{6}}{5^{5}}-\frac{5^{4} \cdot 9^{2}}{5^{5}}\right)=\frac{531^{\prime} 441-625 \cdot 81}{2 \cdot 3^{\prime} 125} \\
& =\frac{480^{\prime} 816}{2 \cdot 3^{\prime} 125}=\frac{240^{\prime} 408}{3^{\prime} 125} \approx \underline{76.9}
\end{aligned}
$$

f) Es gilt

$$
\begin{aligned}
\underline{F} & =\sum_{k=3}^{7}\left(1+x^{2 k}\right)=\sum_{k=3}^{7} 1+\sum_{k=3}^{7}\left(x^{2}\right)^{k}=(7-3+1)+G_{(3 ; 7)}\left(x^{2}\right) \\
& =5+\frac{\left(x^{2}\right)^{3}-\left(x^{2}\right)^{7+1}}{1-x^{2}}=5+\frac{x^{2 \cdot 3}-x^{2 \cdot 8}}{1-x^{2}}=\underline{\underline{5+\frac{x^{6}-x^{16}}{1-x^{2}}}}
\end{aligned}
$$

# 11. Lohnerhöhungen 

Ein Einstiegslohn von monatlich $L_{0}:=4^{\prime} 000 \mathrm{CHF}$ werde jährlich um $i:=2 \%=0.02$ erhöht. Dies ergibt einen jährlichen Lohn-Faktor von

$$
a=1+i=1.02
$$

a) Nach 10 Jahren beträgt der Monatslohn

$$
\underline{L_{10}}=a^{10} \cdot L_{0}=1.02^{10} \cdot 4^{\prime} 000 \mathrm{CHF} \approx \underline{4^{\prime} 875.98 \mathrm{CHF}}
$$

# --- PAGE page_10 ---

b) Während dieser 10 Jahre wurde insgesamt eine Lohnsumme ausbezahlt von

$$
\begin{aligned}
\underline{\underline{S}} & =\sum_{k=0}^{9} 12 \cdot L_{k}=\sum_{k=0}^{9} 12 \cdot a^{k} \cdot L_{0}=12 \cdot L_{0} \sum_{k=0}^{9} a^{k}=12 \cdot L_{0} \cdot G_{(0 ; 9)}(a)=12 \cdot L_{0} \cdot \frac{a^{0}-a^{9+1}}{1-a} \\
& =12 \cdot L_{0} \cdot \frac{1-a^{10}}{-i}=12 \cdot \frac{a^{10}-1}{i} \cdot L_{0}=12 \cdot \frac{1.02^{10}-1}{0.02} \cdot 4^{\prime} 000 \mathrm{CHF} \\
& \approx \underline{525}^{\prime} 586.61 \mathrm{CHF}
\end{aligned}
$$

# 12. Anwendung der geometrischen Summen-Formel 

Es sei $x \in \mathbb{R} \backslash\{-1,0,1\}$. Wir berechnen die folgenden Terme mit Hilfe der geometrischen Summen-Formel.
a) Es gilt

$$
\begin{aligned}
\underline{\underline{G}} & =1+\frac{\sqrt{3}}{4}+\frac{3}{16}+\frac{3 \sqrt{3}}{64}=\sum_{k=0}^{3}\left(\frac{\sqrt{3}}{4}\right)^{k}=G_{(0 ; 3)}\left(\frac{\sqrt{3}}{4}\right)=\frac{\left(\frac{\sqrt{3}}{4}\right)^{0}-\left(\frac{\sqrt{3}}{4}\right)^{3+1}}{1-\frac{\sqrt{3}}{4}} \\
& =\frac{1-\frac{(\sqrt{3})^{4}}{\frac{4^{4}}{4-\sqrt{3}}}}{4}=\frac{4}{4-\sqrt{3}} \cdot\left(1-\frac{(\sqrt{3})^{2 \cdot 2}}{4^{4}}\right)=\frac{1}{4-\sqrt{3}} \cdot\left(4-\frac{3^{2}}{4^{3}}\right) \\
& =\frac{1}{4-\sqrt{3}} \cdot\left(\frac{4^{4}}{4^{3}}-\frac{3^{2}}{4^{3}}\right)=\frac{1}{4-\sqrt{3}} \cdot \frac{256-9}{64}=\frac{1}{4-\sqrt{3}} \cdot \frac{247}{64}=\frac{247}{64 \cdot(4-\sqrt{3})} \\
& \approx \underline{1.70}
\end{aligned}
$$

b) Es gilt

$$
\begin{aligned}
\underline{\underline{H}} & =\frac{x^{1^{\prime} 306}-x^{1^{\prime} 310}}{(1+x) \cdot(1-x)}=\frac{x^{1^{\prime} 306}-x^{1^{\prime} 310}}{1-x^{2}}=\frac{x^{2 \cdot 653}-x^{2 \cdot 655}}{1-x^{2}}=\frac{\left(x^{2}\right)^{653}-\left(x^{2}\right)^{654+1}}{1-x^{2}} \\
& =G_{(653 ; 654)}\left(x^{2}\right)=\sum_{k=653}^{654} x^{2 k}=x^{2 \cdot 653}+x^{2 \cdot 654}=\underline{x^{1^{\prime} 306}+x^{1^{\prime} 308}}
\end{aligned}
$$

c) Es gilt

$$
\begin{aligned}
\underline{\underline{I}} & =\sum_{l=2}^{8} \sum_{k=0}^{l} \frac{1}{2^{k}}=\sum_{l=2}^{8} \sum_{k=0}^{l}\left(\frac{1}{2}\right)^{k}=\sum_{l=2}^{8} G_{(0 ; l)}\left(\frac{1}{2}\right)=\sum_{l=2}^{8} \frac{\left(\frac{1}{2}\right)^{0}-\left(\frac{1}{2}\right)^{l+1}}{1-\frac{1}{2}} \\
& =\sum_{l=2}^{8} \frac{1-\left(\frac{1}{2}\right)^{l+1}}{\frac{1}{2}}=2 \sum_{l=2}^{8}\left(1-\left(\frac{1}{2}\right)^{l+1}\right)=2 \sum_{l=2}^{8} 1-2 \sum_{l=2}^{8}\left(\frac{1}{2}\right)^{l+1} \\
& =2 \cdot(8-2+1)-2 \cdot \frac{1}{2} \sum_{l=2}^{8}\left(\frac{1}{2}\right)^{l}=14-G_{(2 ; 8)}\left(\frac{1}{2}\right)=14-\frac{\left(\frac{1}{2}\right)^{2}-\left(\frac{1}{2}\right)^{8+1}}{1-\frac{1}{2}} \\
& =14-\frac{\frac{1}{2^{2}}-\frac{1}{2^{3}}}{\frac{1}{2}}=14-\frac{1}{2}+\frac{1}{2^{8}}=13.5+\frac{1}{256} \approx \underline{13.5}
\end{aligned}
$$

# --- PAGE page_11 ---

# 13. Martingale Strategie 

Als Martingale bezeichnet man folgende Strategie, um beim Roulette zu gewinnen.
§1 Es wird nur auf einfache Chancen gesetzt (z.B. Rot und Schwarz), das heisst, der gesetzte Betrag geht bei jedem Spiel entweder als gesamtes verloren oder wird im Gewinnfall durch die Bank verdoppelt.
§2 Nach jedem Verlust wird der Einsatz verdoppelt.
a) Der erste Einsatz betrage $E_{0}:=1 \mathrm{CHF}$ und jeder weitere Einsatz sei die Verdoppelung des jeweils unmittelbar Vorangegangenen, das heisst
$E_{k}=2 \cdot E_{k-1}=2 \cdot 2 \cdot E_{k-2}=\ldots=2^{k} \cdot E_{k-k}=2^{k} \cdot E_{0}$.
Der Gesamtverlust nach acht verlorenen Spielen beträgt demnach

$$
\begin{aligned}
\underline{V_{7}} & =\sum_{k=0}^{7} E_{k}=\sum_{k=0}^{7} 2^{k} \cdot E_{0}=E_{0} \sum_{k=0}^{7} 2^{k}=E_{0} \cdot G_{(0 ; 7)}(2)=E_{0} \cdot \frac{2^{0}-2^{8}}{1-2}=E_{0} \cdot \frac{1-256}{-1} \\
& =1 \mathrm{CHF} \cdot 255=\underline{255 \mathrm{CHF}}
\end{aligned}
$$

b) Wenn das neunte Spiel nach acht verlorenen Spielen gewonnen wird und der erste Einsatz einen Franken betrug, dann erhält der Spieler einen Gesamtgewinn von
$\underline{G}=E_{8}-V_{7}=2^{8} \cdot E_{0}-V_{7}=256 \cdot 1 \mathrm{CHF}-255 \mathrm{CHF}=\underline{1 \mathrm{CHF}}$.
c) Es sei $n \in \mathbb{N}^{*}$. Der Gesamtverlust nach $n$ verlorenen Spielen beträgt demnach

$$
\begin{aligned}
V_{n-1} & =\sum_{k=0}^{n-1} E_{k}=\sum_{k=0}^{n-1} 2^{k} \cdot E_{0}=E_{0} \sum_{k=0}^{n-1} 2^{k}=E_{0} \cdot G_{(0 ; n-1)}(2)=E_{0} \cdot \frac{2^{0}-2^{n}}{1-2}=E_{0} \cdot \frac{1-2^{n}}{-1} \\
& =\left(2^{n}-1\right) \cdot E_{0}
\end{aligned}
$$

Wird das Spiel $n+1$ gewonnen, dann beträgt der Gesamtgewinn
$\underline{G}=E_{n}-V_{n-1}=2^{n} \cdot E_{0}-\left(2^{n}-1\right) \cdot E_{0}=2^{n} \cdot E_{0}-2^{n} \cdot E_{0}+E_{0}=\underline{E_{0}>0}$.
Unabhängig von der Höhe des ersten Einsatzes gewinnt der Spieler nach $n$ verlorenen Spielen und einem gewonnenen Spiel $n+1$ insgesamt gerade den Betrag $E_{0}$.

## 14. Aussagen über eine spezielle Summe

Es sei $0<z<1$ und $n \in \mathbb{N}$. Wir betrachten die Summe

$$
S_{n}=\sum_{k=0}^{n} \frac{(-1)^{k+1}}{(1+z)^{k}}
$$

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) Es gilt $S_{0}<0$. | $\bullet$ | $\bigcirc$ |
| b) Es gibt ein $x \in \mathbb{R}$, so dass $S_{n}=-G_{(0 ; n)}(x)$ für alle $n \in \mathbb{N}^{+}$. | $\bullet$ | $\bigcirc$ |
| c) Für alle $n \in \mathbb{N}^{+}$gilt $S_{n+1}>S_{n}$. | $\bigcirc$ | $\bullet$ |
| d) Für alle $n \in \mathbb{N}^{+}$gilt $S_{n}<0$. | $\bullet$ | $\bigcirc$ |
| e) Ist $z \in \mathbb{Q}$, dann folgt $S_{n} \in \mathbb{Q}$ für alle $n \in \mathbb{N}$. | $\bullet$ | $\bigcirc$ |
| f) Für sehr grosse $n \in \mathbb{N}^{+}$gilt $S_{n} \approx-\frac{1+z}{2+z}$. | $\bullet$ | $\bigcirc$ |

# --- PAGE page_12 ---

# 15. Geometrische Reihen 

Wir berechnen, falls möglich, jeweils den Grenzwert der geometrischen Reihe.
a) Mit Hilfe der geometrischen Summen-Formel erhalten wir

$$
\begin{aligned}
\underline{A} & =\sum_{k=0}^{\infty} \frac{1}{2^{k}}=\lim _{n \rightarrow \infty} \sum_{k=0}^{n} \frac{1}{2^{k}}=\lim _{n \rightarrow \infty} \sum_{k=0}^{n}\left(\frac{1}{2}\right)^{k}=\lim _{n \rightarrow \infty} G_{(0 ; n)}\left(\frac{1}{2}\right)=\lim _{n \rightarrow \infty} \frac{1-\left(\frac{1}{2}\right)^{n+1}}{1-\frac{1}{2}} \\
& =\lim _{n \rightarrow \infty} \frac{1-\frac{1}{2^{n+1}}}{\frac{1}{2}}=\frac{1-0}{\frac{1}{2}}=\underline{\underline{2}}
\end{aligned}
$$

b) Wir zeigen zwei Varianten, um diese Teilaufgabe zu lösen.

Variante 1: Mit Hilfe der geometrischen Summen-Formel erhalten wir

$$
\begin{aligned}
\underline{B} & =\sum_{k=1}^{\infty} \frac{1}{2^{k}}=\lim _{n \rightarrow \infty} \sum_{k=1}^{n} \frac{1}{2^{k}}=\lim _{n \rightarrow \infty} \sum_{k=1}^{n}\left(\frac{1}{2}\right)^{k}=\lim _{n \rightarrow \infty} G_{(1 ; n)}\left(\frac{1}{2}\right)=\lim _{n \rightarrow \infty} \frac{\frac{1}{2}-\left(\frac{1}{2}\right)^{n+1}}{1-\frac{1}{2}} \\
& =\lim _{n \rightarrow \infty} \frac{\frac{1}{2}-\frac{1}{2^{n+1}}}{\frac{1}{2}}=\frac{\frac{1}{2}-0}{\frac{1}{2}}=\underline{\underline{1}}
\end{aligned}
$$

Variante 2: Mit Hilfe des Resultates aus Teilaufgabe a) erhalten wir

$$
\underline{B}=\sum_{k=1}^{\infty} \frac{1}{2^{k}}=\sum_{k=0}^{\infty} \frac{1}{2^{k}}-\frac{1}{2^{0}}=2-\frac{1}{1}=2-1=\underline{\underline{1}}
$$

c) Mit Hilfe des Resultates aus Teilaufgabe b) erhalten wir

$$
\underline{C}=\sum_{k=2}^{\infty} \frac{1}{2^{k}}=\sum_{k=1}^{\infty} \frac{1}{2^{k}}-\frac{1}{2^{1}}=1-\frac{1}{2}=\underline{\underline{1}}
$$

d) Mit Hilfe der geometrischen Summen-Formel erhalten wir

$$
\begin{aligned}
\underline{D} & =\sum_{k=0}^{\infty} \frac{2}{3^{k}}=\lim _{n \rightarrow \infty} \sum_{k=0}^{n} \frac{2}{3^{k}}=\lim _{n \rightarrow \infty} 2 \sum_{k=0}^{n} \frac{1}{3^{k}}=2 \lim _{n \rightarrow \infty} \sum_{k=0}^{n}\left(\frac{1}{3}\right)^{k}=2 \lim _{n \rightarrow \infty} G_{(0 ; n)}\left(\frac{1}{3}\right) \\
& =2 \lim _{n \rightarrow \infty} \frac{1-\left(\frac{1}{3}\right)^{n+1}}{1-\frac{1}{3}}=2 \lim _{n \rightarrow \infty} \frac{1-\frac{1}{3^{n+1}}}{\frac{2}{3}}=2 \cdot \frac{1-0}{\frac{2}{3}}=2 \cdot \frac{3}{2}=\underline{\underline{3}}
\end{aligned}
$$

e) Wir zeigen zwei Varianten, um diese Teilaufgabe zu lösen.

Variante 1: Mit Hilfe der geometrischen Summen-Formel erhalten wir

$$
\begin{aligned}
\underline{E} & =\sum_{k=1}^{\infty} \frac{2}{3^{k}}=\lim _{n \rightarrow \infty} \sum_{k=1}^{n} \frac{2}{3^{k}}=\lim _{n \rightarrow \infty} 2 \sum_{k=1}^{n} \frac{1}{3^{k}}=2 \lim _{n \rightarrow \infty} \sum_{k=1}^{n}\left(\frac{1}{3}\right)^{k}=2 \lim _{n \rightarrow \infty} G_{(1 ; n)}\left(\frac{1}{3}\right) \\
& =2 \lim _{n \rightarrow \infty} \frac{\frac{1}{3}-\left(\frac{1}{3}\right)^{n+1}}{1-\frac{1}{3}}=2 \lim _{n \rightarrow \infty} \frac{\frac{1}{3}-\frac{1}{3^{n+1}}}{\frac{2}{3}}=2 \cdot \frac{\frac{1}{3}-0}{\frac{2}{3}}=2 \cdot \frac{1}{3} \cdot \frac{3}{2}=\underline{\underline{1}}
\end{aligned}
$$

Variante 2: Mit Hilfe des Resultates aus Teilaufgabe d) erhalten wir

$$
\underline{E}=\sum_{k=1}^{\infty} \frac{2}{3^{k}}=\sum_{k=0}^{\infty} \frac{2}{3^{k}}-\frac{2}{3^{0}}=3-\frac{2}{1}=3-2=\underline{\underline{1}}
$$

# --- PAGE page_13 ---

f) Mit Hilfe der geometrischen Summen-Formel erhalten wir

$$
\begin{aligned}
\underline{F} & =\sum_{k=0}^{\infty} \frac{2^{k}}{3^{k}}=\lim _{n \rightarrow \infty} \sum_{k=0}^{n} \frac{2^{k}}{3^{k}}=\lim _{n \rightarrow \infty} \sum_{k=0}^{n}\left(\frac{2}{3}\right)^{k}=\lim _{n \rightarrow \infty} G_{(0 ; n)}\left(\frac{2}{3}\right)=\lim _{n \rightarrow \infty} \frac{1-\left(\frac{2}{3}\right)^{n+1}}{1-\frac{2}{3}} \\
& =\frac{1-0}{\frac{1}{3}}=\underline{\underline{3}}
\end{aligned}
$$

# 16. Geometrische Reihen 

Wir berechnen, falls möglich, jeweils den Grenzwert der geometrischen Reihe.
a) Mit Hilfe der geometrischen Summen-Formel erhalten wir

$$
\underline{G}=\sum_{k=1}^{\infty}\left(\frac{3}{2}\right)^{k}=\lim _{n \rightarrow \infty} \sum_{k=1}^{n}\left(\frac{3}{2}\right)^{k}=\lim _{n \rightarrow \infty} G_{(1 ; n)}\left(\frac{3}{2}\right)=\lim _{n \rightarrow \infty} \frac{\frac{3}{2}-\left(\frac{3}{2}\right)^{n+1}}{1-\frac{3}{2}}
$$

Die geometrische Reihe ist offensichtlich divergent, denn $3 / 2>1$ und für $n \rightarrow \infty$ gilt somit

$$
\left(\frac{3}{2}\right)^{n+1} \rightarrow \infty
$$

b) Mit Hilfe der geometrischen Summen-Formel erhalten wir

$$
\underline{H}=\sum_{k=0}^{\infty}(-1)^{k}=\lim _{n \rightarrow \infty} \sum_{k=0}^{n}(-1)^{k}=\lim _{n \rightarrow \infty} G_{(0 ; n)}(-1)=\lim _{n \rightarrow \infty} \frac{1-(-1)^{n+1}}{1-(-1)}
$$

Die geometrische Reihe ist offensichtlich divergent, weil die Folge $(-1)^{n+1}$ für $n \rightarrow \infty$ divergiert, indem sie zwischen den Werten -1 und 1 hin und her springt.
c) Mit Hilfe der geometrischen Summen-Formel erhalten wir

$$
\begin{aligned}
\underline{I} & =\sum_{k=1}^{\infty} \frac{(-1)^{k}}{3^{k}}=\lim _{n \rightarrow \infty} \sum_{k=1}^{n} \frac{(-1)^{k}}{3^{k}}=\lim _{n \rightarrow \infty} \sum_{k=1}^{n}\left(-\frac{1}{3}\right)^{k}=\lim _{n \rightarrow \infty} G_{(1 ; n)}\left(-\frac{1}{3}\right) \\
& =\lim _{n \rightarrow \infty} \frac{-\frac{1}{3}-\left(-\frac{1}{3}\right)^{n+1}}{1-\left(-\frac{1}{3}\right)}=\frac{-\frac{1}{3}-0}{1+\frac{1}{3}}=\frac{-\frac{1}{3}}{\frac{4}{3}}=-\frac{1}{3} \cdot \frac{3}{4}=\underline{\underline{-\frac{1}{4}}}
\end{aligned}
$$

d) Mit Hilfe der geometrischen Summen-Formel erhalten wir

$$
\begin{aligned}
\underline{J} & =\sum_{k=0}^{\infty} \frac{1}{3^{3 k}}=\lim _{n \rightarrow \infty} \sum_{k=0}^{n} \frac{1}{3^{3 k}}=\lim _{n \rightarrow \infty} \sum_{k=0}^{n} \frac{1}{\left(3^{3}\right)^{k}}=\lim _{n \rightarrow \infty} \sum_{k=0}^{n}\left(\frac{1}{27}\right)^{k}=\lim _{n \rightarrow \infty} G_{(0 ; n)}\left(\frac{1}{27}\right) \\
& =\lim _{n \rightarrow \infty} \frac{1-\left(\frac{1}{27}\right)^{n+1}}{1-\frac{1}{27}}=\lim _{n \rightarrow \infty} \frac{1-\frac{1}{27^{n+1}}}{\frac{26}{27}}=\frac{1-0}{\frac{26}{27}}=\underline{\underline{27}} \approx 1.039
\end{aligned}
$$

e) Mit Hilfe der geometrischen Summen-Formel erhalten wir

$$
\underline{K}=\sum_{k=1}^{\infty} \sqrt{\frac{3}{2^{k}}}=\lim _{n \rightarrow \infty} \sum_{k=1}^{n} \sqrt{\frac{3}{2^{k}}}=\lim _{n \rightarrow \infty} \sum_{k=1}^{n} \frac{\sqrt{3}}{\sqrt{2^{k}}}=\lim _{n \rightarrow \infty} \sqrt{3} \sum_{k=1}^{n} \frac{1}{(\sqrt{2})^{k}}
$$

# --- PAGE page_14 ---

$$
\begin{aligned}
& =\sqrt{3} \lim _{n \rightarrow \infty} \sum_{k=1}^{n}\left(\frac{1}{\sqrt{2}}\right)^{k}=\sqrt{3} \lim _{n \rightarrow \infty} G_{(1 ; n)}\left(\frac{1}{\sqrt{2}}\right)=\sqrt{3} \lim _{n \rightarrow \infty} \frac{\frac{1}{\sqrt{2}}-\left(\frac{1}{\sqrt{2}}\right)^{n+1}}{1-\frac{1}{\sqrt{2}}} \\
& =\sqrt{3} \lim _{n \rightarrow \infty} \frac{\frac{1}{\sqrt{2}}-\frac{1}{(\sqrt{2})^{n+1}}}{1-\frac{1}{\sqrt{2}}}=\sqrt{3} \cdot \frac{\frac{1}{\sqrt{2}}-0}{1-\frac{1}{\sqrt{2}}}=\sqrt{3} \cdot \frac{\frac{1}{\sqrt{2}}}{1-\frac{1}{\sqrt{2}}}=\sqrt{3} \cdot \frac{\sqrt{2} \cdot \frac{1}{\sqrt{2}}}{\sqrt{2} \cdot\left(1-\frac{1}{\sqrt{2}}\right)} \\
& =\sqrt{3} \cdot \frac{1}{\sqrt{2}-\frac{\sqrt{2}}{\sqrt{2}}}=\underline{\frac{\sqrt{3}}{\sqrt{2}-1} \approx 4.182}
\end{aligned}
$$

f) Mit Hilfe der geometrischen Summen-Formel erhalten wir

$$
\begin{aligned}
\underline{I}_{2} & =\sum_{k=0}^{\infty} \sqrt{\frac{3^{k}}{2}}=\lim _{n \rightarrow \infty} \sum_{k=0}^{n} \sqrt{\frac{3^{k}}{2}}=\lim _{n \rightarrow \infty} \sum_{k=0}^{n} \frac{\sqrt{3^{k}}}{\sqrt{2}}=\lim _{n \rightarrow \infty} \frac{1}{\sqrt{2}} \sum_{k=0}^{n}(\sqrt{3})^{k} \\
& =\frac{1}{\sqrt{2}} \lim _{n \rightarrow \infty} G_{(0 ; n)}(\sqrt{3})=\frac{1}{\sqrt{2}} \lim _{n \rightarrow \infty} \frac{1-(\sqrt{3})^{n+1}}{1-\sqrt{3}}
\end{aligned}
$$

Die geometrische Reihe ist offensichtlich divergent, denn $\sqrt{3}>1$ und für $n \rightarrow \infty$ gilt somit $(\sqrt{3})^{n+1} \rightarrow \infty$.

# 17. Aussagen über geometrische Reihen 

Es seien $m \in \mathbb{N}$ und $x \in \mathbb{R} \backslash\{0,1\}$. Wir betrachten die allgemeine geometrische Reihe

$$
\sum_{k=m}^{\infty} x^{k}
$$

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) Für $x>1$ divergiert die geometrische Reihe in jedem Fall. | $\bullet$ | $\bigcirc$ |
| b) Für $x<1$ konvergiert die geometrische Reihe in jedem Fall. | $\bigcirc$ | $\bullet$ |
| c) Für $x=2$ konvergiert die geometrische Reihe gegen $\infty$. | $\bigcirc$ | $\bullet$ |
| d) Für $x=0.5$ und $m=0$ konvergiert die geometrische Reihe gegen 2. | $\bullet$ | $\bigcirc$ |
| e) Um zu beurteilen, ob die geometrische Reihe konvergiert, muss man so- <br> wohl $x$ als auch $m$ kennen. | $\bigcirc$ | $\bullet$ |
| f) Um den Grenzwert der geometrischen Reihe (falls ein solcher existiert) <br> berechnen zu können, muss man sowohl $x$ als auch $m$ kennen. | $\bullet$ | $\bigcirc$ |

## 18. Springender Basketball

Ein Basketball fällt aus einer Höhe von 20 m frei auf den Boden und springt immer wieder von diesem auf. Bei jedem Aufspringen erreicht er $4 / 9$ der Höhe aus welcher er unmittelbar davor heruntergefallen ist. Die Fallhöhen bilden somit eine geometrische Folge, rekursiv definiert durch

$$
H_{0}:=20 \mathrm{~m} \quad \text { und } \quad H_{k+1}:=\frac{4}{9} H_{k} \quad \text { für alle } \quad k \in \mathbb{N}_{0} .
$$

# --- PAGE page_15 ---

In expliziter Form erhalten wir daraus

$$
H_{k}=\left(\frac{4}{9}\right)^{k} H_{0} \approx\left(\frac{4}{9}\right)^{k} \cdot 20 \mathrm{~m} \text { für alle } k \in \mathbb{N}_{0}
$$

a) Wir suchen die Distanz $\Delta s$, welche der Basketball (nach oben und unten zusammengezählt) insgesamt zurücklegt, bevor er am Boden liegen bleibt. Dabei müssen wir berücksichtigen, dass der Basketball über die Anfangshöhe $H_{0}$ nur hinunterfällt, während er über alle anderen Höhen $H_{k}$ für $k \in \mathbb{N}^{+}$vor dem Hinunterfallen auch aufsteigen muss. Mit Hilfe der geometrischen Summen-Formel erhalten wir daher

$$
\begin{aligned}
\underline{\Delta s} & =H_{0}+\sum_{k=1}^{\infty} 2 H_{k}=H_{0}+\lim _{n \rightarrow \infty} \sum_{k=1}^{n} 2 H_{k}=H_{0}+\lim _{n \rightarrow \infty} \sum_{k=1}^{n} 2 \cdot\left(\frac{4}{9}\right)^{k} \cdot H_{0} \\
& =H_{0}+2 H_{0} \lim _{n \rightarrow \infty} \sum_{k=1}^{n}\left(\frac{4}{9}\right)^{k}=H_{0}+2 H_{0} \lim _{n \rightarrow \infty} G_{(1 ; n)}\left(\frac{4}{9}\right)=H_{0}+2 H_{0} \lim _{n \rightarrow \infty} \frac{\frac{4}{9}-\left(\frac{4}{9}\right)^{n+1}}{1-\frac{4}{9}} \\
& =H_{0}+2 H_{0} \cdot \frac{\frac{4}{9}-0}{1-\frac{4}{9}}=H_{0}+2 H_{0} \cdot \frac{\frac{4}{9}}{\frac{5}{9}}=H_{0}+2 H_{0} \cdot \frac{4}{9} \cdot \frac{9}{5}=H_{0}\left(1+\frac{8}{5}\right) \\
& =\frac{13}{5} H_{0} \approx \frac{13}{5} \cdot 20 \mathrm{~m}=\underline{52 \mathrm{~m}}
\end{aligned}
$$

b) Es sei $g \approx 10 \mathrm{~m} / \mathrm{s}^{2}$ die Fallbeschleunigung. Gemäss den klassischen Fallgesetzen aus der Physik sind Fallhöhe $H$ und Fallzeit $T$ verknüpft durch die Beziehung

$$
\begin{array}{rlrl} 
& H & =\frac{g}{2} T^{2} & \left\lvert\, \begin{array}{l}
\cdot \frac{2}{g}
\end{array}\right. \\
\Leftrightarrow & \frac{2}{g} H & =T^{2} & \mid \sqrt{\ldots}
\end{array}
$$

Daraus erhalten wir

$$
T=\sqrt{\frac{2 H}{g}}=\sqrt{\frac{2}{g}} \sqrt{H}
$$

Durch Einsetzen der Folgeglieder aus (77) in (79) erhalten wir die ebenfalls geometrische Folge der Fallzeiten, welche explizit gegeben ist durch

$$
\begin{aligned}
T_{k} & =\sqrt{\frac{2}{g}} \sqrt{H_{k}}=\sqrt{\frac{2}{g}} \sqrt{\left(\frac{4}{9}\right)^{k} H_{0}}=\sqrt{\frac{2}{g}} \sqrt{\left(\frac{4}{9}\right)^{k}} \sqrt{H_{0}}=\left(\sqrt{\frac{4}{9}}\right)^{k} \sqrt{\frac{2}{g}} \sqrt{H_{0}} \\
& =\left(\frac{2}{3}\right)^{k} \sqrt{\frac{2 H_{0}}{g}}=\left(\frac{2}{3}\right)^{k} T_{0} \text { für alle } k \in \mathbb{N} .
\end{aligned}
$$

Wir suchen die Dauer $\Delta t$ vom Zeitpunkt des Fallenlassens bis der Basketball auf dem Boden liegen bleibt. Dabei müssen wir berücksichtigen, dass der Basketball für den ersten Fall über die Höhe $H_{0}$ die Zeit $T_{0}$ benötigt, während die Dauer des Aufstieges und Falles über alle anderen Höhen $H_{k}$ für $k \in \mathbb{N}$ jeweils $2 T_{k}$ beträgt. Mit Hilfe der geometrischen Summen-Formel erhalten wir daher
$\underline{\Delta t}=T_{0}+\sum_{k=1}^{\infty} 2 T_{k}=T_{0}+\lim _{n \rightarrow \infty} \sum_{k=1}^{n} 2 T_{k}=T_{0}+\lim _{n \rightarrow \infty} \sum_{k=1}^{n} 2\left(\frac{2}{3}\right)^{k} T_{0}$

# --- PAGE page_16 ---

$$
\begin{aligned}
& =T_{0}+2 T_{0} \lim _{n \rightarrow \infty} \sum_{k=1}^{n}\left(\frac{2}{3}\right)^{k}=T_{0}+2 T_{0} \lim _{n \rightarrow \infty} G_{(1 ; n)}\left(\frac{2}{3}\right)=T_{0}+2 T_{0} \lim _{n \rightarrow \infty} \frac{\frac{2}{3}-\left(\frac{2}{3}\right)^{n+1}}{1-\frac{2}{3}} \\
& =T_{0}+2 T_{0} \cdot \frac{\frac{2}{3}-0}{1-\frac{2}{3}}=T_{0}+2 T_{0} \cdot \frac{\frac{2}{3}}{\frac{1}{3}}=T_{0}+2 T_{0} \cdot \frac{2}{3} \cdot 3=T_{0}(1+4)=5 T_{0} \\
& =5 \sqrt{\frac{2 H_{0}}{g}} \approx 5 \cdot \sqrt{\frac{2 \cdot 20 \mathrm{~m}}{10 \frac{\mathrm{~m}}{\mathrm{~s}^{2}}}}=5 \cdot \sqrt{4.0 \mathrm{~s}^{2}}=5 \cdot 2.0 \mathrm{~s}=\underline{10 \mathrm{~s}}
\end{aligned}
$$

Der Basketball springt also in der endlichen Zeit $\Delta t$ unendlich viele Male vom Boden auf und fällt wieder hinunter!