$$
\begin{aligned}
& =\lim _{\Delta x \rightarrow 0} h(x+\Delta x) \cdot \underbrace{\lim _{\Delta x \rightarrow 0}} \frac{g(x+\Delta x)-g(x)}{\Delta x}+g(x) \cdot \underbrace{\lim _{x \rightarrow 0}} \frac{h(x+\Delta x-h(x)}{\Delta x} \\
& =h(x) \\
& =g^{\prime}(x) \\
& =h^{\prime}(x) \\
& =h(x) \cdot g^{\prime}(x)+g(x) \cdot h^{\prime}(x)
\end{aligned}
$$

Bsp: $\quad f(x)=x^{3}=x^{2} \cdot x$

$$
f^{\prime}(x)=2 x \cdot x+x^{2} \cdot 1=2 x^{2}+x^{2}=3 x^{2}
$$

$$
\begin{aligned}
& \text { - } f(x)=\underbrace{\left(4 x^{3}-3 x\right)(\sqrt{x}-7)}_{g(x)} \\
& f^{\prime}(x)=\left(4 \cdot 3 \cdot x^{2}-3\right)(\sqrt{x}-7)+\left(4 x^{3}-3 x\right)\left(\frac{7}{2} x^{-\frac{7}{2}}\right) \\
& =\left(12 x^{2}-3\right)(\sqrt{x}-7)+\left(4 x^{3}-3 x\right)\left(\frac{4}{2 \sqrt{x}}\right)
\end{aligned}
$$

# Quotiententegel: 

$f: \mathbb{R} \backslash \xi \in \mathbb{R} \mid h(x)=0 \xi \rightarrow \mathbb{R}$

$$
x \rightarrow f(x)=\frac{g(x)}{h(x)}
$$

$g(x)$ und $h(x)$ sind differenzierbar
$f^{\prime}(x)=\frac{g^{\prime}(x) \cdot h(x)-g(x) \cdot h^{\prime}(x)}{h(x)^{2}}$

Bsp: $\quad f(x)=\frac{1}{x} \quad g(x)=1, h(x)=x$

$$
f^{\prime}(x)=\frac{0 \cdot x-1 \cdot 1}{x^{2}}=-\frac{1}{x^{2}}
$$

mit Kononregel : $f(x)=x^{-1}$

$$
f^{\prime}(x)=-1 \cdot x^{-2}=-\frac{1}{x^{2}}
$$

- $f(x)=\frac{x^{2}}{1+x} \quad g(x)=x^{2}, h(x)=1+x$

$$
\begin{aligned}
f^{\prime}(x) & =\frac{2 x \cdot(1+x)-x^{2}-x^{2} \cdot 1}{(1+x)^{2}}=\frac{2 x+2 x^{2}-x^{2}}{(1+x)^{2}} \\
& =\frac{2 x+x^{2}}{(1+x)^{2}}
\end{aligned}
$$