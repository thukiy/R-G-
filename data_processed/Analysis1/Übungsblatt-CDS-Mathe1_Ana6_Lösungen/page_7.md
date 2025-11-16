# 10. Aussagen über verallgemeinerte Exponentialfunktionen 

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) Verallgemeinerte Exponentialfunktionen beschreiben jeweils die Bezie- <br> hung zwischen zwei Grössen in vielen Anwendungen aus Alltag, Natur- <br> wissenschaft, Technik und Wirtschaft. | $\bullet$ | $\bigcirc$ |
| b) Verallgemeinerte Exponentialfunktionen sind immer injektiv. | $\bullet$ | $\bigcirc$ |
| c) Verallgemeinerte Exponentialfunktionen sind immer strikt monoton. | $\bullet$ | $\bigcirc$ |
| d) Jede verallgemeinerte Exponentialfunktion hat eine Umkehrfunktion, so- <br> fern man die Zielmenge geschickt wählt. | $\bullet$ | $\bigcirc$ |
| e) Jede eigentliche Exponentialfunktion ist auch eine verallgemeinerte Expo- <br> nentialfunktion. | $\bullet$ | $\bigcirc$ |

## 11. Eigenschaften von verallgemeinerten Exponentialfunktionen

Seien $a \in \mathbb{R}^{+} \backslash\{1\}, \Sigma \in \mathbb{R} \backslash\{0\}, x_{0} \in \mathbb{R}, y_{0} \in \mathbb{R} \backslash\{0\}$ und $f$ die verallgemeinerte Exponentialfunktion

$$
\begin{aligned}
f: \mathbb{R} & \rightarrow \mathbb{R} \\
x & \mapsto f(x):=y_{0} \cdot a^{\frac{x-x_{0}}{\Sigma}}
\end{aligned}
$$

Wir beweisen die folgenden Eigenschaften von $f$ für alle $x, \Delta x \in \mathbb{R}$.
a) Es gilt

$$
\underline{\underline{f\left(x_{0}\right)}}=y_{0} \cdot a^{\frac{x_{0}-x_{0}}{\Sigma}}=y_{0} \cdot a^{\frac{0}{\Sigma}}=y_{0} \cdot a^{0}=y_{0} \cdot 1=\underline{\underline{y_{0}}}
$$

b) Für alle $x \in \mathbb{R}$ gilt

$$
\begin{aligned}
\underline{\underline{f(x+\Sigma)}} & =y_{0} \cdot a^{\frac{x+\Sigma-x_{0}}{\Sigma}}=y_{0} \cdot a^{\frac{\Sigma}{\Sigma}+\frac{x-x_{0}}{\Sigma}}=y_{0} \cdot a^{\frac{\Sigma}{\Sigma}} \cdot a^{\frac{x-x_{0}}{\Sigma}}=y_{0} \cdot a^{1} \cdot a^{\frac{x-x_{0}}{\Sigma}}=a \cdot y_{0} \cdot a^{\frac{x-x_{0}}{\Sigma}} \\
& =\underline{\underline{a \cdot f(x)}}
\end{aligned}
$$

c) Für alle $x \in \mathbb{R}$ gilt

$$
\begin{aligned}
\underline{\underline{f(x-\Sigma)}} & =y_{0} \cdot a^{\frac{x-\Sigma-x_{0}}{\Sigma}}=y_{0} \cdot a^{\frac{-\Sigma}{\Sigma}+\frac{x-x_{0}}{\Sigma}}=y_{0} \cdot a^{-\frac{\Sigma}{\Sigma}} \cdot a^{\frac{x-x_{0}}{\Sigma}}=y_{0} \cdot a^{-1} \cdot a^{\frac{x-x_{0}}{\Sigma}} \\
& =\frac{1}{a} \cdot y_{0} \cdot a^{\frac{x-x_{0}}{\Sigma}}=\frac{f(x)}{\underline{\underline{a}}}
\end{aligned}
$$

d) Für alle $x, \Delta x \in \mathbb{R}$ gilt

$$
\underline{\underline{f(x+\Delta x)}}=y_{0} \cdot a^{\frac{x+\Delta x-x_{0}}{\Sigma}}=y_{0} \cdot a^{\frac{\Delta x}{\Sigma}+\frac{x-x_{0}}{\Sigma}}=y_{0} \cdot a^{\frac{\Delta x}{\Sigma}} \cdot a^{\frac{x-x_{0}}{\Sigma}}=\underline{\underline{a^{\frac{\Delta x}{\Sigma}} \cdot f(x)}}
$$