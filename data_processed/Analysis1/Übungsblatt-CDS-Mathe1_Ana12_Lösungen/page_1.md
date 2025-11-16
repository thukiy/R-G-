# -`sleq`j_rr ?1_12 Computational and Data Science BSc HS 2023 

## Lösungen

Mathematik 1

1. Aussagen über lokale Extremalstellen

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :--: | :--: |
| a) Null ist ein lokales Minimum der quadratischen Standardfunktion. | $\bullet$ | $\bigcirc$ |
| b) Null ist ein lokales Minimum der kubischen Standardfunktion. | $\bigcirc$ | $\bullet$ |
| c) Die Funktion $2^{x}$ hat keine lokalen Extremstellen. | $\bullet$ | $\bigcirc$ |
| d) Der höchstmögliche Funktionswert einer Funktion liegt immer an einem <br> lokalen Maximum der Funktion. | $\bigcirc$ | $\bullet$ |
| e) Ein Polynom vom Grade 1'000 kann bis zu 1'000 lokale Extremstellen <br> haben. | $\bigcirc$ | $\bullet$ |
| f) Falls gilt $f^{\prime}(-3)=0$, dann hat $f$ an der Stelle $x=-3$ ein lokales Mini- <br> mum oder ein lokales Maximum. | $\bigcirc$ | $\bullet$ |

2. Analysis einer quadratischen Funktion

Es seien $a, b, c \in \mathbb{R}$ mit $a \neq 0$. Wir bestimmen die lokalen Extremstellen der allgemeinen, quadratischen Funktion

$$
f(x):=a x^{2}+b x+c
$$

Für die erste und zweite Ableitung von $f$ erhalten wir

$$
\begin{aligned}
& f^{\prime}(x)=a \cdot 2 x+b+0=2 a x+b \\
& f^{\prime \prime}(x)=2 a+0=2 a
\end{aligned}
$$

Da $f^{\prime}$ linear ist, kann $f$ höchstens eine kritische Stelle haben. Aus

$$
\begin{aligned}
0 & =f^{\prime}(x)=2 a x+b & \mid-b \\
\Leftrightarrow \quad-b & =2 a x & \mid:(2 a)
\end{aligned}
$$

folgt, dass $f$ genau eine kritische Stelle hat bei

$$
x_{\mathrm{S}}=-\frac{b}{2 a}
$$