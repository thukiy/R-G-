# Ableitung Exponentialfunktion 

$$
f(x)=a^{x} \quad f^{\prime}(x)=2
$$

mit Differentialquotient :

$$
\begin{aligned}
& f^{\prime}(x)=\lim _{\Delta x \rightarrow 0} \frac{f(x+\Delta x)-f(x)}{\Delta x}=\lim _{\Delta x \rightarrow 0} \frac{a^{x+\Delta x}-a^{x}}{\Delta x}=\lim _{\Delta x \rightarrow 0} \frac{a^{x} \cdot a^{\Delta x}-a^{x}}{\Delta x} \\
& =\lim _{\Delta x \rightarrow 0} \frac{a^{x}\left(a^{\Delta x}-1\right)}{\Delta x}=a^{x} \cdot \underbrace{\lim _{\Delta x \rightarrow 0} \frac{a^{\Delta x}-1}{\Delta x}}_{=2 a}=a^{x} \cdot 2 a=2 a \cdot f(x)
\end{aligned}
$$

Näherungswerte für $2 a$ bestimmen :

$$
\begin{aligned}
& a=2: 2_{2}=\lim _{\Delta x \rightarrow 0} \frac{2^{\Delta x}-1}{\Delta x} \approx \frac{2^{0,001}-1}{0,001}=0,69 \\
& \rightarrow\left(2^{x}\right)^{2}=0,69 \cdot 2^{x} \\
& a=3: 2_{3}=\lim _{\Delta x \rightarrow 0} \frac{3^{\Delta x}-1}{\Delta x} \approx \frac{3^{0,001}-1}{0,001}=1,1 \\
& \rightarrow\left(3^{x}\right)^{\prime}=1,1 \cdot 3^{x} \\
& \rightarrow \text { es gibt eine Basis a, für die gilt : } \\
& \left(a^{x}\right)^{\prime}=a^{x} \\
& \quad \longmapsto \text { dies ist die culursche Zahl (nach deonard Euler) } \\
& \quad e=2,7182 \ldots \quad \in R \backslash Q
\end{aligned}
$$

natürliche Exponential - und logarithmustunktion :
$f: R \rightarrow R^{+}$
$f(x)=e^{x}$
$f^{\prime}(x)=e^{x}$
Umkehrfunktion von $f(x)=e^{x}: x=\log _{e} y$

$$
\begin{aligned}
& =\ln y \\
& =f^{-1}(y)
\end{aligned}
$$