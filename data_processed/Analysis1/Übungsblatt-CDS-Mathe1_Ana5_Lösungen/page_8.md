# 8. Aussagen über hyperbolische Funktionen 

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :--: | :--: |
| a) Es gilt $\cosh (0) \in \mathbb{N}$. | $\bullet$ | $\bigcirc$ |
| b) Es gilt $\cosh (3)-\sinh (3)=1$. | $\bigcirc$ | $\bullet$ |
| c) Die Funktion $\sinh : \mathbb{R} \rightarrow \mathbb{R}$ ist injektiv. | $\bullet$ | $\bigcirc$ |
| d) Die Funktion $\cosh : \mathbb{R} \rightarrow[1, \infty[$ ist bijektiv. | $\bigcirc$ | $\bullet$ |

## 9. Pythagoras-Satz für hyperbolische Funktionen

Wir betrachten den Pythagoras-Satz für hyperbolische Funktionen gemäss

$$
\cosh ^{2}(x)-\sinh ^{2}(x)=1
$$

a) Für $x=0$ gilt

$$
\begin{aligned}
\underline{\cosh ^{2}(0)-\sinh ^{2}(0)} & =\left(\frac{\mathrm{e}^{0}+\mathrm{e}^{-0}}{2}\right)^{2}-\left(\frac{\mathrm{e}^{0}-\mathrm{e}^{-0}}{2}\right)^{2}=\left(\frac{1+1}{2}\right)^{2}-\left(\frac{1-1}{2}\right)^{2} \\
& =\left(\frac{2}{2}\right)^{2}-\left(\frac{0}{2}\right)^{2}=1^{2}-0^{2}=\underline{1}
\end{aligned}
$$

b) Für alle $x \in \mathbb{R}$ gilt

$$
\begin{aligned}
\underline{\cosh ^{2}(x)-\sinh ^{2}(x)} & =\left(\frac{\mathrm{e}^{x}+\mathrm{e}^{-x}}{2}\right)^{2}-\left(\frac{\mathrm{e}^{x}-\mathrm{e}^{-x}}{2}\right)^{2}=\frac{\left(\mathrm{e}^{x}+\mathrm{e}^{-x}\right)^{2}}{2^{2}}-\frac{\left(\mathrm{e}^{x}-\mathrm{e}^{-x}\right)^{2}}{2^{2}} \\
& =\frac{\left(\mathrm{e}^{x}\right)^{2}+2 \cdot \mathrm{e}^{x} \cdot \mathrm{e}^{-x}+\left(\mathrm{e}^{-x}\right)^{2}}{4}-\frac{\left(\mathrm{e}^{x}\right)^{2}-2 \cdot \mathrm{e}^{x} \cdot \mathrm{e}^{-x}+\left(\mathrm{e}^{-x}\right)^{2}}{4} \\
& =\frac{\mathrm{e}^{2 x}+2 \cdot 1+\mathrm{e}^{-2 x}-\mathrm{e}^{2 x}+2 \cdot 1-\mathrm{e}^{-2 x}}{4}=\frac{2+2}{4}=\frac{4}{4}=\underline{1}
\end{aligned}
$$