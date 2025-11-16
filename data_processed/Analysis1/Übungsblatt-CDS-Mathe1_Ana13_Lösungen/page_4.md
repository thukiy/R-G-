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