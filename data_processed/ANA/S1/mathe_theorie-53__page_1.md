<|ref|>equation<|/ref|><|det|>[[0, 0, 997, 120]]<|/det|>
\[
\begin{align*}
&= \lim_{\Delta x \to 0} h(x + \Delta x) \cdot \lim_{\Delta x \to 0} \frac{q(x + \Delta x) - q(x)}{\Delta x} + q(x) \cdot \lim_{\Delta x \to 0} \frac{h(x + \Delta x - h(x)}{\Delta x} \\
&= h(x) \cdot q'(x) + q(x) \cdot h'(x)
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[19, 145, 430, 175]]<|/det|>
Bsp: \(\bullet f(x) = x^3 = x^2 \cdot x\) 

<|ref|>equation<|/ref|><|det|>[[175, 185, 720, 214]]<|/det|>
\[
f'(x) = 2x \cdot x + x^2 \cdot 1 = 2x^2 + x^2 = 3x^2
\]

<|ref|>equation<|/ref|><|det|>[[135, 241, 515, 280]]<|/det|>
\[
\bullet f(x) = (4x^3 - 3x)(\sqrt{x} - 7)
\]

<|ref|>equation<|/ref|><|det|>[[175, 320, 802, 391]]<|/det|>
\[
\begin{align*}
f'(x) &= (4 \cdot 3 \cdot x^2 - 3)(\sqrt{x} - 7) + (4x^3 - 3x)(\frac{1}{2}x^{-\frac{1}{2}}) \\
&= (12x^2 - 3)(\sqrt{x} - 7) + (4x^2 - 3x)(\frac{1}{2\sqrt{x}})
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[19, 417, 270, 448]]<|/det|>
Quotientenregel: 

<|ref|>equation<|/ref|><|det|>[[52, 456, 460, 485]]<|/det|>
\[
f: \mathbb{R} \setminus \{x \in \mathbb{R} \mid h(x) = 0\} \to \mathbb{R}
\]

<|ref|>equation<|/ref|><|det|>[[323, 491, 567, 530]]<|/det|>
\[
x \to f(x) = \frac{g(x)}{h(x)}
\]

<|ref|>equation<|/ref|><|det|>[[52, 536, 490, 565]]<|/det|>
\[
q(x) \text{ und } h(x) \text{ sind differenzierbar}
\]

<|ref|>equation<|/ref|><|det|>[[52, 570, 385, 608]]<|/det|>
\[
f'(x) = \frac{q'(x) \cdot h(x) - q(x) \cdot h'(x)}{h(x)^2}
\]

<|ref|>text<|/ref|><|det|>[[19, 633, 626, 667]]<|/det|>
Bsp: \(\bullet f(x) = \frac{1}{x}\) 

<|ref|>equation<|/ref|><|det|>[[163, 667, 504, 707]]<|/det|>
\[
f'(x) = \frac{0 \cdot x - 1 \cdot 1}{x^2} = -\frac{1}{x^2}
\]

<|ref|>equation<|/ref|><|det|>[[183, 711, 565, 744]]<|/det|>
\[
\text{mit Homomregel: } f(x) = x^{-1}
\]

<|ref|>equation<|/ref|><|det|>[[435, 746, 715, 784]]<|/det|>
\[
f'(x) = -1 \cdot x^{-2} = -\frac{1}{x^2}
\]

<|ref|>equation<|/ref|><|det|>[[135, 803, 761, 840]]<|/det|>
\[
\bullet f(x) = \frac{x^2}{1+x} \quad q(x) = x^2, \quad h(x) = 1+x
\]

<|ref|>equation<|/ref|><|det|>[[163, 841, 707, 915]]<|/det|>
\[
\begin{align*}
f'(x) &= \frac{2x \cdot (1+x) - x^2 - x^2 \cdot 1}{(1+x)^2} = \frac{2x + 2x^2 - x^2}{(1+x)^2} \\
&= \frac{2x + x^2}{(1+x)^2}
\end{align*}
\]