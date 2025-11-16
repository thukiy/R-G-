Additionstheorem nutzen :
$\sin (\alpha+\beta)=\sin \alpha \cos \beta+\sin \beta \cos \alpha$
$\sin (\alpha-\beta)=\sin \alpha \cos \beta-\sin \beta \cos \alpha$
(1) - (2) : $\sin (\alpha+\beta)-\sin (\alpha-\beta)=2 \sin \beta \cos \alpha$

Ersetzen: $\alpha=\frac{\alpha+\beta}{2}, \beta=\frac{\alpha-\beta}{2}$
$\rightarrow \sin \alpha-\sin \beta=2 \cdot \sin \frac{\alpha-\beta}{2} \cdot \cos \frac{\alpha+\beta}{2}$
$\rightarrow \alpha=x+\Delta x$ und $\beta=x$ :
Differenzquotient

$$
\begin{aligned}
& \frac{\sin (x+\Delta x)-\sin x}{\Delta x}=2 \cdot \sin \frac{\Delta x}{2} \cdot \cos \frac{2 x+\Delta x}{2} \\
& f^{\prime}(x)=\lim _{\Delta x \rightarrow 0} 2 \cdot \sin \frac{\Delta x}{2} \cdot \cos \frac{2 x+\Delta x}{2} \\
& =\lim _{\Delta x \rightarrow 0} \frac{2 \cdot \sin \frac{\Delta x}{2}}{2} \cdot \cos \left(\frac{2 x+\Delta x}{2}\right)=\cos x
\end{aligned}
$$

weitere trigonometrische Funktionen :

- $f(x)=\cos x$
$f^{\prime}(x)=-\sin x$
- $f(x)=t \tan x$
$f^{\prime}(x)=1+t \tan ^{2} x=\frac{1}{\cos ^{2} x}$
- $f(x)=\cot x$
$f^{\prime}(x)=-1-\cot ^{2} x=-\frac{1}{\sin ^{2} x}$