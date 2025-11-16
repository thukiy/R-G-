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