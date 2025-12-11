<|ref|>text<|/ref|><|det|>[[115, 83, 141, 100]]<|/det|>
c) 

<|ref|>equation<|/ref|><|det|>[[123, 105, 536, 166]]<|/det|>
\[
\begin{align*}
u(x) & := 4x + 2 \Rightarrow u'(x) = 4 + 0 = 4 \\
\frac{du}{dx} & = 4 \Leftrightarrow du = 4dx \Leftrightarrow dx = \frac{du}{4} = \frac{1}{4} du
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[123, 175, 222, 192]]<|/det|>
und somit 

<|ref|>equation<|/ref|><|det|>[[123, 200, 656, 239]]<|/det|>
\[
F(x) = \int e^{4x+2} dx = \frac{1}{4} \int e^u du = \frac{1}{4} e^u + c = \frac{1}{4} e^{4x+2} + c.
\]

<|ref|>text<|/ref|><|det|>[[115, 243, 141, 259]]<|/det|>
d) 

<|ref|>equation<|/ref|><|det|>[[123, 263, 570, 326]]<|/det|>
\[
\begin{align*} u(x) & := x^2 - 1 \Rightarrow u'(x) = 2x - 0 = 2x \\[1ex] \frac{du}{dx} &= 2x \Leftrightarrow du = 2x dx \Leftrightarrow dx = \frac{du}{2x} = \frac{1}{2x} du \end{align*}
\]

<|ref|>text<|/ref|><|det|>[[123, 331, 222, 348]]<|/det|>
und somit 

<|ref|>equation<|/ref|><|det|>[[123, 355, 797, 440]]<|/det|>
\[
\begin{align*} F(x) &= \int \left( x^2 - 1 \right)^3 \cdot x \, dx = \int u^3 \cdot x \cdot \frac{1}{2x} \, du = \frac{1}{2} \int u^3 \, du = \frac{1}{2} \cdot \frac{1}{4} u^4 + c \\[1ex] &= \frac{1}{8} \left( x^2 - 1 \right)^4 + c. \end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 444, 141, 460]]<|/det|>
e) 

<|ref|>equation<|/ref|><|det|>[[123, 464, 616, 526]]<|/det|>
\[
\begin{align*} u(x) & := 1 - x \Rightarrow u'(x) = 0 - 1 = -1 \\[1ex] \frac{du}{dx} &= -1 \Leftrightarrow du = (-1) dx \Leftrightarrow dx = \frac{du}{-1} = (-1) du \end{align*}
\]

<|ref|>text<|/ref|><|det|>[[123, 533, 222, 550]]<|/det|>
und somit 

<|ref|>equation<|/ref|><|det|>[[123, 557, 875, 641]]<|/det|>
\[
\begin{align*} F(x) &= \int \sqrt[3]{1-x} \, dx = \int \sqrt[3]{u} \cdot (-1) \, du = -\int \sqrt[3]{u} \, du = -\int u^{\frac{1}{3}} \, du = -\frac{3}{4} u^{\frac{4}{3}} + c \\[1ex] &= -\frac{3}{4} (1-x)^{\frac{4}{3}} + c = -\frac{3}{4} \sqrt[3]{(1-x)^4} + c. \end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 644, 141, 660]]<|/det|>
f) 

<|ref|>equation<|/ref|><|det|>[[123, 667, 576, 730]]<|/det|>
\[
\begin{align*} u(x) & := x^2 \Rightarrow u'(x) = 2x \\[1ex] \frac{du}{dx} &= 2 x \Leftrightarrow du = 2x dx \Leftrightarrow dx = \frac{du}{x} = \frac{1}{2x} du \end{align*}
\]

<|ref|>text, 1ex
und somit

\[
F(x) = \int x \cos(x^2) \, dx = \int x \cos(u) \cdot \frac{1}{2x} \, du = \frac{1}{2}\int \cos(u) \, du = \frac{1}{2} \sin(u) + c
\]

<|ref|>equation<|/ref|><|det|>[[123, 767, 850, 850]]<|/det|>
\[
\begin{align*} F(x) &= \int x \cos(x^2) \, dx = \int x \cos(u) - \frac{1}{2x} \, du = \frac{1}{2} \cos(u) \, du = \frac{1}{2} \sin(u) +c \\[1ex] &= \frac{1}{2} \sin(x^2) + c. \end{align*}
\]