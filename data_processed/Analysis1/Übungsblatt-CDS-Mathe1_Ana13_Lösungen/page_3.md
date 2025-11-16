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