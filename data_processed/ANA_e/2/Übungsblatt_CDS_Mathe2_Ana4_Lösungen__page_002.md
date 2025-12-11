<|ref|>text<|/ref|><|det|>[[115, 84, 142, 101]]<|/det|>
b) 

<|ref|>equation<|/ref|><|det|>[[115, 100, 879, 188]]<|/det|>
\[
\begin{align*}
\frac{I}{2} &= \int_0^\infty 2^{-x} \, dx = \lim_{s \to \infty} \int_0^s 2^{-x} \, dx = -\frac{1}{\ln(2)} \cdot \lim_{s \to \infty} \left[ 2^{-x} \right]_0^s = -\frac{1}{\ln(2)} \cdot \lim_{s \to \infin} \left( 2^{-s} - 2^{-0} \right) \\
&= -\frac{1}{\ln(2)} \cdot (0 - 1) = \frac{1}{\ln(2)}.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 191, 142, 208]]<|/det|>
c) 

<|ref|>equation<|/ref|><|det|>[[122, 211, 702, 252]]<|/det|>
\[
I = \int_1^\infty \frac{1}{x} \, dx = \lim_{s \to \infty} \int_1^s \frac{1}{x} \, dx = \lim_{s \to \infty} (\frac{s}{1}) = \lim_{s \to \infty} \ln(s) = \infty.
\]

<|ref|>text<|/ref|><|det|>[[122, 256, 757, 277]]<|/det|>
Dieses uneigentliche Integral ist divergent und existiert daher nicht. 

<|ref|>text<|/ref|><|det|>[[115, 281, 142, 299]]<|/det|>
d) 

<|ref|>equation<|/ref|><|det|>[[122, 301, 876, 344]]<|/det|>
\[
\frac{I}{2} = \int_1^\infty \frac{1}{x^2} \, dx = \lim_{s \to \infty} \int_1^s (\frac{1}{x^2}) \, dx = \lim_{s \to \infty} \left[ -\frac{1}{x} \right]_1^s = \lim_{s \to \infty} \left( -\frac{1}{s} + \frac{1}{1} \right) = (-0 + 1) = \frac{1}{e}.
\]

<|ref|>text<|/ref|><|det|>[[115, 346, 142, 363]]<|/det|>
e) 

<|ref|>equation<|/ref|><|det|>[[122, 363, 568, 405]]<|/det|>
\[
I = \int_0^1 \frac{1}{x} \, dx = \lim_{s \to 0} \int_s^1 \frac{1}{x} \, dx = \lim_{s \to 1} \ln\left(\frac{1}{s}\right) = \infty.
\]

<|ref|>text<|/ref|><|det|>[[122, 413, 750, 433]]<|/det|>
Dieses uneigentliche Integral ist divergent und existiert daher nicht. 

**f)** 

<|ref|>equation<|/ref|><|det|>[[122, 435, 875, 530]]<|/det|>
\[
\begin{align*}
I &= \int_0^1 \frac{1}{\sqrt{x}} \, dx = \lim_{s \to 0} \int_s^1 \frac{\sqrt{x}}{x} \, dx = \lim_{s \to 0} \left[ 2 \cdot \sqrt{x} \right]_s^1 = 2 \cdot \lim_{s \to 0} \left( \sqrt{1} - \sqrt{s} \right) = 2 \cdot (1 - 0) \\
&= \frac{2}{e}.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 530, 142, 547]]<|/det|>
g) 

<|ref|>equation<|/ref|><|det|>[[122, 546, 875, 666]]<|/det|>
\[
\begin{align*}
I &= \int_{-\infty}^{\infty} e^{-|x|} \, dx = \lim_{r \to \infty} \int_{-r}^{0} e^{-|x|} \, dx + \lim_{s \to \infty} \int_{0}^{s} e^{-|x|} \, dx = \lim_{r \to \infty} \left( \int_{-r}^{0} e^{x} \, dx + \lim_{s \to \infty} \int_{0}^{s} \mathrm{e}^{-x} \, dx \right) \\
&= \lim_{r \to \infty} \left[ \mathrm{e}^{x} \right]_{-r}^{0} + \lim_{s \to \infty} \left[ -\mathrm{e}^{-x} \right]_{0}^{s} = \lim_{r \to \infty} \left( \mathrm{e}^{0} - \mathrm{e}^{-r} \right) + \lim_{s \to \infty} \left( -\mathrm{e}^{-s} + \mathrm{e}^{0} \right) \\
&= \lim_{r \to \infty} \left( 1 - \mathrm{e}^{-r} \right) + \lim_{s \to \infty}\left( 1 - \mathrm{e}^{-s} \right) = 1 - 0 + 1 - 0 = \frac{2}{e}.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 664, 142, 681]]<|/det|>
h) 

<|ref|>equation<|/ref|><|det|>[[152, 680, 843, 787]]<|/det|>
\[
\begin{align*}
I &= \int_{-\infty}^{\infty} \frac{1}{x^2} \, dx = \lim_{a \to -\infty} \int_a^{-1} \frac{1}{x^2} \, dx + \lim_{b \to 0} \int_{-1}^{b} \frac{1}{x^2} \, dx + \lim_{c \to 0} \int_c^{1} \frac{1}{x^2} \, dx + \lim_{d \to \infty} \int_1^{d} \frac{1}{x^2} \, dx \\
&= \lim_{a \to -\infty} \left[ -\frac{1}{x^2} \right]_a^{-1} + \lim_{b \to 0} \left[ -\frac{1}{x^2} \right]_b^{-1} + \lim_{c \to 0} \left[ -\frac{1}{x^2} \right]_{c}^{1} + \lim_{d \to \infty} \left[ -\frac{1}{x^2} \right]_{d}^{1} \\
&= \lim_{a \to -\infty} \left( 1 + \frac{1}{a} \right) + \lim_{b \to 0} \left( -\frac{1}{b} - 1 \right) + \lim_{c \to 0} \left( -1 + \frac{1}{c} \right) + \lim_{d \to \infty} \left( -\frac{1}{d} + 1 \right)
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 780, 690, 812]]<|/det|>
Grenzwert existiert nicht, da \(\lim_{b \to 0} \left( -\frac{1}{b} \right) \to -\infty\) und \(\lim_{d \to \infty} \left( -\frac{1}{d} \right) \to \infty\)