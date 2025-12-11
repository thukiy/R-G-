<|ref|>text<|/ref|><|det|>[[114, 82, 141, 100]]<|/det|>
d) 

<|ref|>text<|/ref|><|det|>[[114, 99, 606, 125]]<|/det|>
Aus dem AWP lesen wir ab: \(x_0 = 4\), \(y_0 = 3\), \(m(x) = \frac{1}{2\sqrt{x}}\). 

<|ref|>text<|/ref|><|det|>[[114, 123, 880, 186]]<|/det|>
Die allgemeine Stammfunktion von m ist \(M(x) = \int \frac{1}{2\sqrt{x}} dx = \sqrt{x} + c\). Durch Nutzen der Information aus b) erhalten wir die Lösung des AWP. Für \(x \ge x_0 = 4\) gilt \(y(x) = y_0 \cdot e^{M(x)-M(x_0)} = 3 \cdot e^{\sqrt{x}-\sqrt{4}} = 3 \cdot e^{\sqrt{x}-2}\). 

<|ref|>sub_title<|/ref|><|det|>[[114, 201, 380, 219]]<|/det|>
## 3. Linear inhomogene DGL 

<|ref|>text<|/ref|><|det|>[[114, 218, 800, 260]]<|/det|>
a) \(y' = 2y + 1\) b) \(y' = 3y + x \cdot e^x\) c) \(y' = y + x\) d) \(y' = 2xy + e^{x^2}\) e) \(y' - \frac{y}{x} = x^2\) f) \(xy' - y = x^2 + 4\) 

<|ref|>text<|/ref|><|det|>[[114, 277, 144, 293]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[114, 292, 700, 311]]<|/det|>
Linear inhomogene DGL mit \(m(x) = 2\) und \(q(x) = 1\). Es ergibt sich 

<|ref|>equation<|/ref|><|det|>[[120, 312, 680, 383]]<|/det|>
\[
\begin{align*}
M(x) &= \int m(x) \, dx = \int 2 \, dx = 2x \\
C(x) &= \int q(x) \cdot e^{-M(x)} \, dx = \int 1 \cdot e^{-2x} \, dx = \frac{1}{-2} \cdot e^{-2x} = -\frac{1}{2} e^{-2x}.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 383, 457, 401]]<|/det|>
Es ergibt sich als allgemeine Lösung: 

<|ref|>equation<|/ref|><|det|>[[120, 408, 586, 441]]<|/det|>
\[
\frac{y(x)}{x} = (C + C(x)) \cdot e^{M(x)} = (C - \frac{1}{2} e^{-2x}) \cdot e^{2x} = C e^{2x} - \frac{1}{2}.
\]

<|ref|>text<|/ref|><|det|>[[114, 443, 144, 460]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[114, 459, 725, 478]]<|/det|>
Linear inhomogene DGL mit \(m(x) = 3\) und \(q(x) = x \cdot e^x\). Es ergibt sich 

<|ref|>equation<|/ref|><|det|>[[120, 483, 640, 640]]<|/det|>
\[
\begin{align*}
M(x) &= \int m(x) \, dx &= \int 3 \, dx = 3x \\
C(x) &= \int q(x) \cdot e^{-M(x)} \,dx &= \int x \cdot e^x \cdot e^{-3x} \, dx = \int \frac{x}{x} \cdot e^{-2x} \, dx \\
&= x \cdot \frac{1}{-2} e^{-2x} - \int 1 \cdot \frac{1}{-2} e^{-2x} \, dx = -\frac{1}{2} x e^{-2x} + \frac{1}{2} \int e^{-2x} \, dx \\
&= -\frac{1}{2} x e^{-2x} + \frac{1}{4} \cdot \frac{1}{-2} e^{-2x} = -\frac{1}{2} x e^{-2x} - \frac{1}{4} e^{-2x}.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 641, 457, 659]]<|/det|>
Es ergibt sich als allgemeine Lösung: 

<|ref|>equation<|/ref|><|det|>[[120,

\[
\begin{align*}
y(x) &= (C + C(x)) \cdot e^{M(x)} &= (C - \frac{1}{2} x e^{-2x} - \frac{1}{4}e^{-2x}) \cdot e^{3x} = C e^{3x} - \frac{1}{2} x e^{x} - \frac{1}{4} e^{x} \\
&= C e^{3x} - \frac{1}{2} \left( x + \frac{1}{2} \right) e^{x}.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 740, 144, 757]]<|/det|>
c) 

<|ref|>text<|/ref|><|det|>[[114, 756, 700, 775]]<|/det|>
Linear inhomogene DGL mit \(m(x) = 1\) und \(q(x) = x\). Es ergibt sich 

<|ref|>equation<|/ref|><|det|>[[120, 775, 390, 808]]<|/det|>
\[
M(x) = \int m(x) \, dx = \int 1 \, dx = x
\]

<|ref|>equation<|/ref|><|det|>[[120, 814, 613, 923]]<|/det|>
\[
\begin{align*}
C(x) &= \int q(x) \cdot e^{-M(x)} \, dx &= \int x \cdot e^{-x} \, dx = \int \frac{x}{x} \cdot e^{-x} \, dx \\
&= x \cdot (-1) e^{-x} - \int 1 \cdot (-1) e^{-x} \, dx = -x e^{-x} + \int e^{-x} \, dx \\
&= -x e^{-x} + (-1) \cdot e^{-x} = -x e^{-x} - e^{-x}.
\end{align*}
\]