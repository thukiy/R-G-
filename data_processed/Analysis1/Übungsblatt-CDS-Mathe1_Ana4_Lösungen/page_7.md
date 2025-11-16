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