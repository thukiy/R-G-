# Differentialrechnung 

## Produktregel

$f(x)=g(x) \cdot h(x)$
wie sieht $f^{\prime}(x)$ aus?
$\rightarrow f^{\prime}(x)=g^{\prime}(x) \cdot h^{\prime}(x) \quad$ FALSCH
2.B. $f(x)=x^{2}$
$f^{\prime}(x)=2 x$
mit $f(x)=\frac{x \cdot x}{g(x) h(x)}$
wäre $f^{\prime}(x)=g^{\prime}(x) \cdot h^{\prime}(x)=1 \cdot 1=1$
Produktregel: $g, h: R \rightarrow \mathbb{R}, f(x)=g(x) \cdot h(x)$
$g \& h$ sind differenzierbar. Dann gilt :
$f^{\prime}(x)=g^{\prime}(x) \cdot h(x)+g(x) \cdot h^{\prime}(x)$
Bsp: $\quad f(x)=x^{2}=x \cdot x$
$f^{\prime}(x)=x \cdot 1+1 \cdot x=2 x \quad \rightarrow$ stimma mit konomregel überein
behachte Differenzquotient:

$$
\begin{aligned}
& f^{\prime}(x)=\lim _{\Delta x \rightarrow 0} \frac{f(x+\Delta x)-f(x)}{\Delta x}=\lim _{\Delta x \rightarrow 0} \frac{g(x+\Delta x) \cdot h(x+\Delta x)-g(x) \cdot h(x)}{\Delta x} \\
& =\lim _{\Delta x \rightarrow 0} \frac{g(x+\Delta x) \cdot h(x+\Delta x)+g(x) \cdot h(x+\Delta x)-g(x) \cdot h(x+\Delta x)-g(x) \cdot h(x)}{\Delta x} \\
& =\lim _{\Delta x \rightarrow 0} \frac{h(x+\Delta x) \cdot[g(x+\Delta x)-g(x)]+g(x) \cdot[h(x+\Delta x)-h(x)]}{\Delta x} \\
& =\lim _{\Delta x \rightarrow 0} \frac{h(x+\Delta x)[g(x+\Delta x)-g(x)]}{\Delta x}+\lim _{\Delta x \rightarrow 0} \frac{g(x)[h(x+\Delta x)-h(x)]}{\Delta x}
\end{aligned}
$$