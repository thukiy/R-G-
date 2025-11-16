# 12. Falten eines Papiers 

Wir betrachten ein rechteckiges Blatt Papier mit Dicke und Fläche gemäss

$$
\begin{aligned}
d_{0} & \approx 0.100 \mathrm{~mm}=1.00 \cdot 10^{-1} \cdot 10^{-3} \mathrm{~m}=1.00 \cdot 10^{-1-3} \mathrm{~m}=1.00 \cdot 10^{-4} \mathrm{~m} \\
A_{0} & \approx 1.00 \mathrm{~m}^{2}
\end{aligned}
$$

a) Das Papier werde in der Mitte gefaltet. Dabei werden die beiden Falt-Teile aufeinander gelegt und das Ganze als neues Blatt betrachtet. Dicke und Fläche des Papiers ändern beim Falten um die Faktoren

$$
\underline{a=2} \quad \text { bzw. } \quad \underline{b=\frac{1}{2}}
$$

b) Wir beschreiben die Entwicklungen der Dicke und der Fläche des Papiers bei wiederholtem Falten durch je eine verallgemeinerte Exponentialfunktion. Als unabhängige Variable verwenden wir dazu

$$
n: \equiv \text { Anzahl durchgeführte Faltungen. }
$$

Gemäss Situationsangaben legen wir sinnvollerweise die folgenden Parameter fest.

| Funktion: | RS: | RW: | BA: | SW: |
| :--: | :--: | :--: | :--: | :--: |
| Dicke: | $n_{0}=0$ | $d_{0} \approx 1.00 \cdot 10^{-4} \mathrm{~m}$ | $a=2$ | $\Sigma=1$ |
| Fläche: | $n_{0}=0$ | $A_{0} \approx 1.00 \mathrm{~m}^{2}$ | $b=1 / 2$ | $\Sigma=1$ |

Daraus erhalten wir die verallgemeinerten Exponentialfunktionen
Dicke: $\quad \underline{d(n)}=d_{0} \cdot a^{\frac{n-n_{0}}{\Sigma}}=d_{0} \cdot 2^{\frac{n-0}{1}}=d_{0} \cdot 2^{n} \approx \underline{1.00 \cdot 10^{-4} \mathrm{~m} \cdot 2^{n}}$
Fläche: $\quad \underline{A(n)}=A_{0} \cdot b^{\frac{n-n_{0}}{\Sigma}}=A_{0} \cdot\left(\frac{1}{2}\right)^{\frac{n-0}{1}}=A_{0} \cdot\left(\frac{1}{2}\right)^{n} \approx \underline{1.00 \mathrm{~m}^{2} \cdot \frac{1}{2^{n}}}$.
c) Es sei $n_{\mathrm{E}}$ die Anzahl durchzuführende Faltungen, bis die Dicke des Papiers die mittlere Distanz zwischen Erde und Mond von
$d_{\mathrm{E}} \approx 400 \cdot 10^{3} \mathrm{~km}=4.00 \cdot 10^{2} \cdot 10^{3} \cdot 10^{3} \mathrm{~m}=4.00 \cdot 10^{2+3+3} \mathrm{~m}=4.00 \cdot 10^{8} \mathrm{~m}$
übersteigt. Gemäss (58) gilt

$$
\begin{aligned}
d_{\mathrm{E}}=d\left(n_{\mathrm{E}}\right) & =d_{0} \cdot 2^{n_{\mathrm{E}}} & \mid: d_{0} \\
\Leftrightarrow & \frac{d_{\mathrm{E}}}{d_{0}} & =2^{n_{\mathrm{E}}} & \left\lvert\, \log _{2}(\ldots)\right.
\end{aligned}
$$

Daraus und durch Aufrunden auf die nächst grössere natürliche Zahl erhalten wir

$$
\begin{aligned}
\underline{n_{\mathrm{E}}} & =\left\lceil\log _{2}\left(\frac{d_{\mathrm{E}}}{d_{0}}\right)\right\rceil \approx\left\lceil\log _{2}\left(\frac{4.00 \cdot 10^{8} \mathrm{~m}}{1.00 \cdot 10^{-4} \mathrm{~m}}\right)\right\rceil=\left\lceil\log _{2}\left(4.00 \cdot 10^{12}\right)\right\rceil \\
& =\left\lceil\log _{2}(4.00)+12 \cdot \log _{2}(10)\right\rceil \approx\lceil 41.9\rceil=\underline{42}
\end{aligned}
$$