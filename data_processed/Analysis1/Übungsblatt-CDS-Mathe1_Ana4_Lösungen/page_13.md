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