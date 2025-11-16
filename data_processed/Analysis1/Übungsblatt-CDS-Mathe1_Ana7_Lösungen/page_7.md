# 7. Ableitung der Wurzelfunktion 

Wir betrachten die Wurzel-Funktion $f: \mathbb{R}^{+} \rightarrow \mathbb{R}$ mit

$$
f(x):=\sqrt{x}
$$

a) Wir berechnen die Ableitung $f^{\prime}(x)$ mit Hilfe der Monom-Ableitung. Es gilt

$$
\underline{\underline{f^{\prime}(x)}}=(\sqrt{x})^{\prime}=\left(x^{\frac{1}{2}}\right)^{\prime}=\frac{1}{2} \cdot x^{\frac{1}{2}-1}=\frac{1}{2} \cdot x^{-\frac{1}{2}}=\frac{1}{2} \cdot \frac{1}{\sqrt{x}}=\underline{\underline{1 \sqrt{x}}}
$$

b) Wir berechnen die Ableitung $f^{\prime}(x)$ mit Hilfe des Differenzquotienten, wobei wir den Bruch mit $(\sqrt{x+\delta x}+\sqrt{x})$ erweitern und dann im Zähler ausmultiplizieren. Es gilt

$$
\begin{aligned}
& \underline{\underline{f^{\prime}(x)}}=\lim _{\delta x \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x}=\lim _{\delta x \rightarrow 0} \frac{\sqrt{x+\delta x}-\sqrt{x}}{\delta x} \\
& =\lim _{\delta x \rightarrow 0} \frac{(\sqrt{x+\delta x}-\sqrt{x}) \cdot(\sqrt{x+\delta x}+\sqrt{x})}{\delta x \cdot(\sqrt{x+\delta x}+\sqrt{x})}=\lim _{\delta x \rightarrow 0} \frac{(\sqrt{x+\delta x})^{2}-(\sqrt{x})^{2}}{\delta x \cdot(\sqrt{x+\delta x}+\sqrt{x})} \\
& =\lim _{\delta x \rightarrow 0} \frac{x+\delta x-x}{\delta x \cdot(\sqrt{x+\delta x}+\sqrt{x})}=\lim _{\delta x \rightarrow 0} \frac{\delta x}{\delta x \cdot(\sqrt{x+\delta x}+\sqrt{x})}=\lim _{\delta x \rightarrow 0} \frac{1}{\sqrt{x+\delta x}+\sqrt{x}} \\
& =\frac{1}{\sqrt{x+0}+\sqrt{x}}=\frac{1}{\sqrt{x}+\sqrt{x}}=\underline{\underline{1 \sqrt{x}}}
\end{aligned}
$$

c) Wir berechnen die zweite Ableitung von $f$ mit Hilfe der Monom-Ableitung. Es gilt

$$
\begin{aligned}
& \underline{\underline{f^{\prime \prime}(x)}}=\left(f^{\prime}(x)\right)^{\prime}=\left(\frac{1}{2} \cdot x^{-\frac{1}{2}}\right)^{\prime}=\frac{1}{2} \cdot\left(-\frac{1}{2}\right) \cdot x^{-\frac{1}{2}-1}=-\frac{1}{4} \cdot x^{-\frac{3}{2}}=-\frac{1}{4} \cdot \frac{1}{\sqrt{x^{3}}} \\
& =\underline{-\frac{1}{4 \sqrt{x^{3}}}}
\end{aligned}
$$