<|ref|>text<|/ref|><|det|>[[115, 85, 142, 100]]<|/det|>
b) 

<|ref|>equation<|/ref|><|det|>[[118, 105, 572, 164]]<|/det|>
\[
\begin{align*}
u(x) & := 2x^2 + 9 \Rightarrow u'(x) = 2 \cdot 2x + 0 = 4x \\
\frac{du}{dx} & = 4x \Leftrightarrow du = 4x \, dx \Leftrightarrow dx = \frac{du}{4x} = \frac{1}{4x} \, du
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[120, 169, 220, 185]]<|/det|>
und somit 

<|ref|>equation<|/ref|><|det|>[[120, 190, 850, 237]]<|/det|>
\[
\frac{I}{I} = \int_{0}^{2} \frac{4x}{2x^2 + 9} \, dx = \int_{u(0)}^{u(2)} \frac{4x}{u} \cdot \frac{1}{4x} \, du = \int_{9}^{17} \frac{1}{u} \, du = \left[ \ln\left(|u|\right) \right]_{9}^{17} = \ln\left(\frac{17}{9}\right).
\]

<|ref|>text<|/ref|><|det|>[[115, 241, 142, 257]]<|/det|>
c) 

<|ref|>equation<|/ref|><|det|>[[120, 259, 642, 316]]<|/det|>
\[
\begin{align*} u(x) & := 25 - x^2 \Rightarrow u'(x) = 0 - 2x = -2x \\ \frac{du}{dx} & = -2x \Leftrightarrow du = -2x \, dx \Leftrightarrow dx = -\frac{du}{-2x} = -\frac{1}{2x} \, du \end{align*}
\]

<|ref|>text<|/ref|><|det|>[[120, 321, 220, 337]]<|/det|>
und somit 

<|ref|>equation<|/ref|><|det|>[[120, 342, 840, 430]]<|/det|>
\[
\begin{align*} \frac{I}{I} &= \int_{0}^{3} \frac{x}{\sqrt{25 - x^2}} \, dx = \int_{u(0)}^{u(s)} \frac{x}{\sqrt{u}} \cdot \frac{-1}{2x} \, du = -\int_{25}^{16} \frac{1}{2\sqrt{u}} \, du = \int_{16}^{25} \frac{1}{2\sqrt{u}} \, du \\ &= \left[ \sqrt{u} \right]_{16}^{25} = \sqrt{25} - \sqrt{16} = 5 - 4 = \frac{1}{2e} \end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 432, 142, 448]]<|/det|>
d) 

<|ref|>equation<|/ref|><|det|>[[120, 453, 636, 510]]<|/det|>
\[
\begin{align*} u(x) & := a^2 - x^2 \Rightarrow u'(x) = 0 - 2x = - 2x \\ \frac{du}{dx} & = -2x \Leftrightarrow du=-2x \, dx \Leftrightarrow dx = \frac{du}{-2x} = -\frac{1}{2x} \, du
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[120, 518, 220, 533]]<|/det|>
und somit 

<|ref|>equation<|/ref|><|det|>[[120, 540, 842, 637]]<|/det|>
\[
\begin{align*} \frac{I}{I} &= \int_{0}^{\infty} x \sqrt{a^2 - x^2} \, dx = \int_{u(0)}^{u(a)} x \sqrt{u} \cdot \frac{-1}{2x} \, du = -\frac{1}{2} \int_{a^2}^{0} \sqrt{u} \, du = \frac{1}{2} \int_{0}^{a^2} \sqrt{u} \, du \\ &= \frac{1}{2} \cdot \frac{2}{3} \cdot \left[ u^{\frac{3}{2}} \right]_{0}^{a^2} = \frac{1}{3} \cdot \left( (a^2)^{\frac{3}{2}} - 0^{\frac{3}{2}} \right) = \frac{1}{3} \cdot \sqrt{a^6} = \frac{1}{3} \cdot |a|^3. \end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 640, 142, 656]]<|/det|>
e) 

<|ref|>equation<|/ref|><|det|>[[120, 660, 475, 678]]<|/det|>
\[
u(x) := 2x + \frac{\pi}{3} \Rightarrow u'(x) = 2 + 0 = 2
\]

<|ref|>equation<|/ref|><|det|>[[120, 684, 504, 722]]<|/det|>
\[
\frac{du}{dx} = 2 \Leftrightarrow du = 2 \, dx \Leftrightarrow dx = \frac{du}{2} = \frac{1}{2} \, du
\]

<|ref|>text<|/ref|><|det|>[[120, 730, 220, 746]]<|/det|>
und somit 

<|ref|>equation<|/ref|><|det|>[[120, 752, 875, 845]]<|/det|>
\[
\begin{align*} \frac{I}{I} &= \int_{0} ^{\pi/2} \cos\left(2x + \frac{\pi}{3}\right) \, dx = \int_{u(0)}^{u(\pi/2)} \cos(u) \, \frac{1}{2} \, du = \frac{1}{2} \int_{\pi/3}^{4\pi/3} \cos(u) \, du = \frac{1}{2} \cdot \left[ \sin(u) \right]_{\pi/3}^{4\pi/3} \\ &= \frac{1}{2} \cdot \left( \sin(4\pi/3) - \sin(\pi/3) \right) = \frac{1}{2} \cdot \left( -\frac{\sqrt{3}}{2} - \frac{\sqrt{3}}{2} \right) = \frac{1}{2} \cdot (-2) \cdot \frac{\sqrt{3}}{2} = \frac{-\sqrt{3}}{2}. \end{align*}
\]