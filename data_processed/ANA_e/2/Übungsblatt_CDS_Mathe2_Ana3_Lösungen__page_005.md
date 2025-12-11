<|ref|>text<|/ref|><|det|>[[115, 85, 145, 102]]<|/det|>
b) 

<|ref|>equation<|/ref|><|det|>[[117, 99, 878, 268]]<|/det|>
\[
\begin{align*}
I &= \int_{1}^{2} x \sqrt{x-1} \, dx = \int_{1}^{2} x \cdot \sqrt{x-1} \, dx = \left[ x \cdot \frac{2}{3} \cdot (x-1)^{\frac{3}{2}} \right]_{1}^{2} - \int_{1}^{2} 1 \cdot \frac{2}{3} \cdot (x-1)^{\frac{3}2} \, dx \\
&= \frac{2}{3} \cdot \left[ x(x-1)^{\frac{3}{2}} \right]_{1}^{2} - \frac{2}{3} \cdot \frac{2}{5} \cdot \left[ (x-1)^{\frac{5}{2}} \right]_{1}^{2} \\
&= \frac{2}{3} \cdot 2 \cdot (2-1)^{\frac{3}{2}} - \frac{2}{3} \cdot 1 \cdot (1-1)^{\frac{3}{2}} - \frac{4}{15} \cdot (2-1)^{\frac{5}{2}} + \frac{4}{15} \cdot (1-1)^{\frac{5}{2}} = \frac{4}{3} - 0 - \frac{4}{15} + 0 \\
&= \frac{20}{15} - \frac{4}{15} = \frac{16}{15}.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 270, 145, 287]]<|/det|>
c) 

<|ref|>equation<|/ref|><|det|>[[125, 287, 875, 415]]<|/det|>
\[
\begin{align*}
I &= \int_{1}^{2} \ln(x) \cdot x \, dx = \left[ \ln(x) \cdot \frac{1}{2} \cdot x^2 \right]_{1}^{2} - \int_{1}^{2} \frac{1}{x} \cdot x^2 \, dx = \frac{1}{2} \cdot \left[ x^2 \cdot \ln(x) \right]_{1}^{2} - \frac{1}{2} \int_{1}^{2} x \, dx \\
&= \frac{1}{2} \cdot \left[ x^2 \cdot \ln(1) \right]_{1}^{2} - \frac{1}{2} \cdot \frac{1}{2} \cdot \left[ x^2 \right]_{1}^{2} = \frac{1}{2} \cdot 2^2 \cdot \ln(2) - \frac{1}{2} \cdot 1^2 \cdot \ln(1) - \frac{1}{4} \cdot 2^2 + \frac{1}{4} \cdot 1^2 \\
&= 2 \cdot \ln(2) - 0 - 1 + \frac{1}{4} = 2 \ln(2) - \frac{3}{4}.
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[115, 428, 426, 446]]<|/det|>
4. Stammfunktionen bestimmen 

<|ref|>text<|/ref|><|det|>[[115, 445, 870, 465]]<|/det|>
Berechnen Sie die folgenden unbestimmten Integrale mit einer geeigneten Methode. 

<|ref|>text<|/ref|><|det|>[[115, 462, 230, 490]]<|/det|>
a) \(\int \frac{x}{1+x^4} dx\) 

<|ref|>text<|/ref|><|det|>[[115, 485, 270, 508]]<|/det|>
c) \(\int r^3(\cos r^2)dr\) 

<|ref|>text<|/ref|><|det|>[[115, 510, 222, 540]]<|/det|>
e) \(\int \frac{e^{2x}}{1+e^x} dx\) 

<|ref|>text<|/ref|><|det|>[[115, 555, 145, 571]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[115, 570, 345, 587]]<|/det|>
mittels Substitution lösen 

<|ref|>equation<|/ref|><|det|>[[122, 594, 366, 653]]<|/det|>
\[
\begin{align*}
u(x) &= x^2 \Rightarrow u'(x) = 2x. \\
\frac{du}{dx} &= 2x \Leftrightarrow du = 2x dx \Leftrightarrow dx = \frac{du}{2x} = \frac{1}{2x} du
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[122, 658, 216, 675]]<|/det|>
und somit 

<|ref|>equation<|/ref|><|det|>[[122, 680, 816, 763]]<|/det|>
\[
\begin{align*}
F(x) &= \int \frac{x}{1+x^4} dx = \int \frac{x}{1+u^2} \cdot \frac{1}{2x} du = \frac{1}{2} \int \frac{1}{1+u^2} du = \frac{1}{2} \cdot \arctan(u) + c \\
&= \frac{1}{2} \cdot \arctan(x^2) + c.
\end{align*}
\]