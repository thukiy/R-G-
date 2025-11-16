e) Es gilt

$$
\underline{e^{\prime}(z)}=\frac{1}{3} \cdot z^{\frac{1}{3}-1}=\frac{1}{3} \cdot z^{\frac{1}{3}-\frac{3}{3}}=\frac{1}{\underline{3}} \cdot z^{-\frac{2}{3}}
$$

f) Es gilt

$$
\underline{f^{\prime}(k)}=2 \cdot \frac{2}{3} \cdot k^{\frac{2}{3}-1}=\frac{2 \cdot 2}{3} \cdot k^{\frac{2}{3}-\frac{3}{3}}=\frac{4}{\underline{3}} \cdot k^{-\frac{1}{3}}
$$

g) Es gilt

$$
\underline{g^{\prime}(w)}=-p \cdot w^{p-1}
$$

h) Es gilt

$$
h^{\prime}(v)=u^{2} \cdot 2 \cdot v^{2-1} \cdot w^{2}=\underline{2 u^{2} v w^{2}}
$$

i) Es gilt

$$
\underline{i^{\prime}(q)}=\frac{p^{2} \cdot 1}{r s}=\frac{p^{2}}{\underline{r s}}
$$

# 5. Ableitung der kubischen Standardfunktion 

Wir betrachten die kubische Standard-Funktion $f: \mathbb{R} \rightarrow \mathbb{R}$ mit

$$
f(x):=x^{3}
$$

a) Mit Hilfe der Monom-Ableitung erhalten wir

$$
\underline{f^{\prime}(x)}=3 \cdot x^{3-1}=\underline{3 x^{2}}
$$

b) Mit Hilfe des Differenzquotienten und der binomischen Formel für dritte Potenzen erhalten wir

$$
\begin{aligned}
\underline{f^{\prime}(x)} & =\lim _{\delta x \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x}=\lim _{\delta x \rightarrow 0} \frac{(x+\delta x)^{3}-x^{3}}{\delta x} \\
& =\lim _{\delta x \rightarrow 0} \frac{x^{3}+3 \cdot x^{2} \cdot \delta x+3 \cdot x \cdot \delta x^{2}+\delta x^{3}-x^{3}}{\delta x}=\lim _{\delta x \rightarrow 0} \frac{3 \cdot x^{2} \cdot \delta x+3 \cdot x \cdot \delta x^{2}+\delta x^{3}}{\delta x} \\
& =\lim _{\delta x \rightarrow 0} \frac{\delta x \cdot\left(3 \cdot x^{2}+3 \cdot x \cdot \delta x+\delta x^{2}\right)}{\delta x}=\lim _{\delta x \rightarrow 0}\left(3 \cdot x^{2}+3 \cdot x \cdot \delta x+\delta x^{2}\right) \\
& =3 \cdot x^{2}+3 \cdot x \cdot 0+0^{2}=3 \cdot x^{2}+0+0=\underline{3 x^{2}}
\end{aligned}
$$

c) Mit Hilfe der Monom-Ableitung erhalten wir

$$
\begin{aligned}
& \underline{f^{\prime \prime}(x)}=2 \cdot 3 \cdot x^{2-1}=\underline{\underline{6 x}} \\
& \underline{f^{\prime \prime \prime}(x)}=\underline{\underline{6}} \\
& \underline{f^{\prime \prime \prime \prime}(x)}=\underline{\underline{0}}
\end{aligned}
$$