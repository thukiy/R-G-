# Summenzeichen: $\sum$ 

verwendet, um eine Summe mit gleichartigen Summanden
kure aufschreiben

$$
\sum_{k=1}^{n} a_{k}:=a_{1}+a_{2}+a_{3}+\ldots+a_{n}
$$

$k$ : Laufvariable, durchläuft Werte von 1...n
$\rightarrow$ Laufvariable kann geändert werden

$$
\sum_{k=1}^{n} a_{k}=\sum_{m=1}^{n} a_{m}
$$

$\rightarrow$ Indexverschiebung kann durchgefuhrt werden

$$
\sum_{k=1}^{n} a_{k}=\sum_{k=1+5}^{n+5} a_{k-5}
$$

$\rightarrow$ hilfreich beim Zusammenfassen von 2 oder mehr Summen

$$
\begin{aligned}
& \rightarrow \text { Regeln: } \quad \circ \sum_{k=1}^{n}\left(a_{k}+b_{k}\right)=\sum_{k=1}^{n} a_{k}+\sum_{k=1}^{n} b_{k} \\
& \circ \sum_{k=1}^{n}\left(c \cdot a_{k}\right)=c \cdot \sum_{k=1}^{n} a_{k}
\end{aligned}
$$

Bsp: $\quad \sum_{k=1}^{5} k^{2}=1^{2}+2^{2}+3^{2}+4^{2}+5^{2}=55$

$$
\begin{aligned}
& \circ \sum_{k=m}^{n} c=c \cdot \sum_{k=m}^{n} 1=c \cdot(n-m+1) \quad C \in \mathbb{R} \\
& \circ \sum_{k=1}^{5} \frac{(-1)^{k}}{2^{k}}=\frac{-1}{2}+\frac{1}{4}+\frac{-1}{8}+\frac{1}{16}+\frac{-1}{32} \\
& \circ \sum_{k=5}^{8} a_{k}=\sum_{k=0}^{3} a_{k+5} \quad \rightarrow \text { Indexverschiebung } \\
& \circ \sum_{k=4}^{40}(k+4)^{2}=\sum_{k=8}^{40} k^{2} \\
& \circ \sum_{k=1}^{n} a_{k}=\sum_{k=1}^{n} a_{n+1-k}
\end{aligned}
$$