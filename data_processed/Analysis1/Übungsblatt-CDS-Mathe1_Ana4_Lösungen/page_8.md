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