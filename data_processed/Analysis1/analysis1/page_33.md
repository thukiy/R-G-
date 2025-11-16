# Divergenzkriterium: 

Konvergiert $\sum_{k=1}^{n} a_{k}$, dann folgt, dass $\lim _{k \rightarrow \infty} a_{k}=0$ gilt. Jedoch folgt aus $\lim _{k \rightarrow \infty} a_{k}=0$ nicht, dass $\sum_{k=1}^{n} a_{k}$ konvergiert.

Bsp: $\quad \sum_{k=1}^{n} \frac{1}{k}$ ist divergent
es gilt : $\lim _{k \rightarrow \infty} \frac{1}{k}=0$

$$
\begin{aligned}
& \sum_{k=1}^{n} \frac{1}{k}=1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+\frac{1}{5}+\frac{1}{6}+\frac{1}{7}+\frac{1}{8}+\ldots+\frac{1}{2^{m}} \\
& \geqslant 1+\frac{1}{2}+\underbrace{1}_{1}+\frac{1}{4}+\underbrace{\frac{1}{8}+\frac{1}{8}+\frac{1}{8}+\frac{1}{8}}_{=2 \cdot \frac{1}{2^{2}}}=\frac{1}{2}=4 \cdot \frac{1}{2^{2}}=\frac{1}{2} \\
& =1+m \cdot \frac{1}{2} \xrightarrow{m \rightarrow \infty} \infty
\end{aligned}
$$

## Sympy

Summenberechnung: $\quad S=$ sp. summation $(k *=2,(k, 1,5)) ;$

$$
\rightarrow S=\sum_{k=1}^{5} k^{2}
$$

Grenzwertberechnung: $\quad a=$ sp. limit_seq $(1 / k, k)$;

$$
\rightarrow \lim _{k \rightarrow \infty} \frac{1}{k}
$$

## Geometrische Summenformel

$G_{(m ; n)}(x):=\sum_{k=m}^{n} x^{k}$
$\rightarrow(1-x) \cdot G_{(m ; n)}(x)=x^{m}-x^{n+1} \quad \times \notin \S 0 ; 1 \S$