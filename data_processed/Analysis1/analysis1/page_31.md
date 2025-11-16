- Summe der ersten $n$ natur lichen zahlen :

$$
\begin{aligned}
\sum_{k=1}^{n} k & =\sum_{k=1}^{n}(n+1-k) \\
& =\sum_{k=1}^{n} \frac{(n+1)-\sum_{k=1}^{n} k}{(\text { fixe zaine } \sum_{k=1}^{n} k} \\
& =(n+1)(n+1-1)-\sum_{k=1}^{n} k= \\
2 \cdot \sum_{k=1}^{n} k & =(n+1) \cdot n \\
\sum_{k=1}^{n} k & =\frac{1}{2}(n+1) \cdot n
\end{aligned}
$$

- Geometrische Summe

$$
\begin{aligned}
& G_{m, n}(x)=\sum_{k=m}^{n}(x)^{k}=x^{m}+x^{m+1}+\ldots+x^{n}=\frac{x^{m}-x^{n+1}}{1-x} \\
& m, n \in \mathbb{N}, \quad x \in \mathbb{R} \backslash\{0 ; 1\} \\
& \text { Bsp: } \quad \cdot \sum_{k=1}^{n}\left(\frac{1}{2}\right)^{k}=\frac{\left(\frac{1}{2}\right)-\left(\frac{1}{2}\right)^{m}}{1-\frac{1}{2}}=\frac{\frac{1}{2}-\frac{1}{2 m}}{-\frac{1}{2}}=2 \cdot\left(\frac{1}{2}-\frac{1}{2 m}\right)=1-\frac{1}{2^{3}} \\
& \rightarrow \text { typische Anwendung: Renterrechnung }
\end{aligned}
$$

# Reihen 

- Partial-/Teilsumme:
$a_{n}$ sei Folge reeller zahlen
$s_{n}:=\sum_{k=1}^{n} a_{k}$ heisst Partialsumme
Die einzelnen $s_{n}$ bilden auch eine Folge : $\left(s_{n}\right)$.
$\rightarrow$ Die unendliche Summe $\sum_{k=1}^{m} a_{k}$ heisst Reihe.
$\rightarrow$ Die Reihe konvergiert gegen ein $s \in \mathbb{R}$, wenn gilt : $\lim _{n \rightarrow \infty} s_{n}=s$