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