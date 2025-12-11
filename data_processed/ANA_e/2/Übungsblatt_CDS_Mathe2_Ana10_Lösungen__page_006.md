<|ref|>text<|/ref|><|det|>[[115, 83, 144, 100]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[122, 100, 404, 215]]<|/det|>
\[
\begin{align*}
\vec{e} &= \frac{1}{|\vec{r}|} \vec{r} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix} \\
\frac{\partial f}{\partial x} &= \frac{(x+y) \cdot 1 - x \cdot 1}{(x+y)^2} = \frac{y}{(x+y)^2} \\
\frac{\partial f}{\partial y} &= -\frac{x}{(x+y)^2}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[120, 222, 180, 238]]<|/det|>
Damit: 

<|ref|>equation<|/ref|><|det|>[[120, 245, 800, 287]]<|/det|>
\[
\frac{\partial f}{\partial \vec{e}} (1,2) = \vec{e} \cdot \text{grad} f(1,2) = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \begin{pmatrix} \frac{2}{9} \\ -\frac{1}{9} \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} 2 \\ 9 \\ 9 \end{pmatrix} = \frac{1}{9\sqrt{2}} = \frac{\sqrt{2}}{18}
\]

<|ref|>text<|/ref|><|det|>[[115, 289, 144, 306]]<|/det|>
b) 

<|ref|>equation<|/ref|><|det|>[[122, 308, 335, 466]]<|/det|>
\[
\begin{align*}
\vec{e} &= \frac{1}{|\bar{r}|} \bar{r} = \frac{1}{5} \begin{pmatrix} 0 \\ -3 \\ 4 \end{pmatrix} \\
\frac{\partial f}{\partial x} &= \sin(z) \\
\frac{\partial f}{\partial y} &= -\cos(2z) \\
\frac{\partial f}{\partial z} &= x\cos(z) + 2y\sin(2z)
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[120, 476, 180, 492]]<|/det|>
Damit: 

<|ref|>equation<|/ref|><|det|>[[120, 500, 604, 553]]<|/det|>
\[
\frac{\partial f}{\partial \vec{e}} (0,0,0) = \vec{e} \cdot \text{grad} f(0,0,0) = \frac{1}{5} \begin{pmatrix} 0 \\ -3 \\ 0 \end{pmatrix} \begin{pmatrix} 0 \\ -1 \\ 0 \end{pmatrix} = \frac{3}{5}
\]

<|ref|>text<|/ref|><|det|>[[115, 555, 144, 572]]<|/det|>
c) 

<|ref|>equation<|/ref|><|det|>[[122, 577, 339, 829]]<|/det|>
\[
\begin{align*}
\vec{e} &= \frac{1}{|\overline{r}|} \overline{r} = \frac{1}{2} \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} \\
\frac{\partial f}{\partial x_1} &= 2x_1\sqrt{x_2} \\
\frac{\partial f}{\partial x_2} &= \frac{x_1^2}{2\sqrt{x_2}} \\
\frac{\partial f}{\partial x_3} &= x_4e^{x_3} \\
\frac{\partial f}{\partial x_4} &= e^{x_3}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[120, 795, 180, 812]]<|/det|>
Damit: 

<|ref|>equation<|/ref|><|det|>[[120, 821, 617, 930]]<|/det|>
\[
\begin{align*}
\frac{\partial f}{\partial \vec{e}} (-1,1,0,2) &= \vec{e} \cdot \text{grad} f(-1,1,0,2) = \frac{1}{2} \begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix} \begin{pmatrix} -2 \\ \frac{1}{2} \\ 1 \end{pmatrix} \\
&= \frac{-2 - \frac{1}{2} - 2 + 1}{2} = -\frac{7}{4}
\end{align*}
\]