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