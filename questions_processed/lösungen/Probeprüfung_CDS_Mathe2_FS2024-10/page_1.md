<|ref|>text<|/ref|><|det|>[[30, 15, 100, 45]]<|/det|>
7) e) 

<|ref|>equation<|/ref|><|det|>[[140, 15, 910, 66]]<|/det|>
\[
\vec{F}(t) = \begin{pmatrix} x(t) \\ y(t) \end{pmatrix} = \begin{pmatrix} (\cos t)/t \\ (\sin t)/t \end{pmatrix} = \frac{1}{t} \begin{pmatrix} \cos t \\ \sin t \end{pmatrix} \quad \begin{cases} 0 < t < 1 \\ f(x,y) = (x^2 + y^2)^{-3/2} \end{cases}
\]

<|ref|>text<|/ref|><|det|>[[140, 72, 456, 99]]<|/det|>
skalares Kurvenintegral : 

<|ref|>equation<|/ref|><|det|>[[140, 103, 710, 420]]<|/det|>
\[
\begin{align*}
I &= \int f(\vec{F}(t)) \cdot |\vec{F}(t)| \, dt \\
f(\vec{F}(t)) &= \left[ \frac{1}{t^2} \cdot (\cos^2 t + \sin^2 t) \right]^{-3/2} = t^{-2 \cdot (-3/2)} = t^3 \\
\dot{x}(t) &= -\sin t \cdot \frac{1}{t} + \cos t \cdot (-t^{-2}) = -\frac{1}{t} (\sin t + \frac{1}{t} \cos t) \\
\dot{y}(t) &= \cos t \cdot \frac{1}{t} + \sin t \cdot (-t^{-2}) = \frac{1}{t} (\cos t - \frac{1}{t} \sin t) \\
|\dot{y}(t)| &= \sqrt{\frac{1}{t^2} (\sin^2 t + \frac{2}{t} \sin t \cdot \cos t + \frac{1}{t^2} \cos^2 t)} \\
&\qquad + \frac{1}{t^2} (\cos^2 t - \frac{2}{t} \cos t \sin t + \frac{1}{t^2} \sin^2 t) \\
&= \sqrt{\frac{1}{t^2} (\sin^2 t + \frac{\pi}{t^2} \cos^2 t) + \frac{1}{t^2} (\cos^2 t + \frac{\pi}{t^2} \sin^2 t)} \\
&= \sqrt{\frac{1}{t^2} (1 + \frac{1}{t^2})} = \sqrt{\frac{1}{t^2} \cdot \left(\frac{t^2 + 1}{t^2}\right)} = \frac{1}{t^2} \sqrt{t^2 + 1}
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[160, 444, 850, 594]]<|/det|>
\[
\begin{align*}
I &= \int f(t^3 \cdot \frac{1}{t^2} \cdot \sqrt{t^2 + 1}) \, dt = \int f(t \cdot \sqrt{t^2 + 1}) \, dt \\
\text{Substitution:} \quad t^2 + 1 = u \quad \frac{du}{dt} = 2t \quad \Rightarrow \quad dt = \frac{du}{2t} \\
&= \int_{0^2 + 1}^{\frac{1}{2} + 1} f(t \cdot \sqrt{u}) \frac{du}{2t} = \frac{1}{2} \int_0^1 \sqrt{u} \, du = \frac{1}{2} \left[ \frac{2}{3} u^{3/2} \right]_0^1 \\
&= \frac{1}{2} \left( \frac{2}{3} \cdot 2^{2/3} - \frac{2}{3} \right) = \frac{1}{3} \cdot (\sqrt{8} - 1) = 0,609
\end{align*}
\]