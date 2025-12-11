<|ref|>text<|/ref|><|det|>[[115, 82, 142, 100]]<|/det|>
k) 

<|ref|>equation<|/ref|><|det|>[[120, 99, 744, 160]]<|/det|>
\[
\begin{align*}
u(x) &\coloneqq \cosh(x) \Rightarrow u'(x) = \sinh(x) \\
\frac{du}{dx} &= \sinh(x) \Leftrightarrow du = \sinh(x) dx \Leftrightarrow dx = \frac{du}{\sinh(x)} = \frac{1}{\sinh(x)} du
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[120, 172, 220, 190]]<|/det|>
und somit 

<|ref|>equation<|/ref|><|det|>[[120, 199, 797, 275]]<|/det|>
\[
\begin{align*}
F(x) &= \int \tanh(x) \, dx = \int \frac{\sinh(x)}{\cosh(x)} \cdot \frac{1}{\sinh(x)} \, du = \int \frac{1}{u} \, du = \ln(|u|) + c \\
&= \ln\left(|\cosh(x)|\right) + c.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 278, 140, 295]]<|/det|>
l) 

<|ref|>equation<|/ref|><|det|>[[120, 296, 770, 360]]<|/det|>
\[
\begin{align*}
u(x) &\coloneqq \sinh(x) \Rightarrow u'(x) = \cosh(x) \\
\frac{du}{dx} &= \cosh(x) \Leftrightarrow du = \cosh(x) dx \Leftrightarrow dx = \frac{du}{\cosh(x)} = \frac{1}{\cosh(x)} du
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[120, 372, 220, 390]]<|/det|>
und somit 

<|ref|>equation<|/ref|><|det|>[[120, 399, 797, 475]]<|/det|>
\[
\begin{align*}
F(x) &= \int \coth(x) \, dx = \int \frac{\cosh(x)}{\sinh(x)} \cdot \frac{1}{\cosh(x)} du = \int \frac{1}{u} du = \ln(|u|) + c \\
&= \ln\left(|\sinh(x)|\right) + c.
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[115, 490, 710, 508]]<|/det|>
4. Stammfunktion durch Methode der Substitution bestimmen 

<|ref|>text<|/ref|><|det|>[[115, 507, 870, 525]]<|/det|>
Berechnen Sie die folgenden bestimmten Integrale mit der Methode der Substitution. 

<|ref|>equation<|/ref|><|det|>[[115, 523, 664, 602]]<|/det|>
a) \(\int_3^5 \frac{x}{x^2-4} dx\) b) \(\int_0^2 \frac{4x}{2x^2+9}\) c) \(\int_0^3 \frac{x}{\sqrt{25-x^2}} dx\) d) \(\int_0^a x\sqrt{a^2-x^2} dx\) e) \(\int_0^{\pi/2} \cos(2x+\frac{\pi}{3}) dx\) f) \(\int_0^{10} 5xe^{-x^2} dx\) 

<|ref|>text<|/ref|><|det|>[[115, 616, 142, 632]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[120, 633, 555, 693]]<|/det|>
\[
\begin{align*}
u(x) &\coloneqq x^2 - 4 \Rightarrow u'(x) = 2x - 0 = 2x \\
\frac{du}{dx} &= 2x \Leftrightarrow du = 2x \, dx \Leftrightarrow dx = \frac{du}{2x} = \frac{1}{2x} \, du
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[120, 700, 220, 717]]<|/det|>
und somit 

<|ref|>equation<|/ref|><|det|>[[120, 724, 880, 819]]<|/det|>
\[
\begin{align*}
I &= \int_3^5 \frac{x}{x^2-4} dx = \int_{u(3)}^{u(5)} \frac{x}{u} \cdot \frac{1}{2x} du = \frac{1}{2} \int_{u(3)}^{u(5)} \frac{1}{u} du = \frac{1}{2} \int_5^{21} \frac{1}{u} du = \left[ \frac{1}{2} \ln(|u|) \right]_5^{21} \\
&= \frac{1}{2} \ln\left(\frac{21}{5}\right).
\end{align*}
\]