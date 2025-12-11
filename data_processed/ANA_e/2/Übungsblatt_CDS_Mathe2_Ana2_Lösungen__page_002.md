<|ref|>sub_title<|/ref|><|det|>[[114, 81, 576, 99]]<|/det|>
## 2. Aussagen über die Methode der Substitution 

<|ref|>text<|/ref|><|det|>[[114, 99, 682, 116]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[114, 114, 880, 300]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Die Methode Substitution basiert auf der Kettenregel der Differentialrechnung.</td><td>X</td><td></td></tr><tr><td>b) Die Hilfe der Methode der Substitution kann jede Verschachtelung von zwei Funktionen problemlos integriert werden.</td><td></td><td>X</td></tr><tr><td>c) Die Methode der Substitution eignet sich zur Integration von Produkten der Form \(x \cdot f(x^2)\).</td><td>X</td><td></td></tr><tr><td>d) Es gilt: \(\int_{1}^{2} \sin(2x) \, dx = 1/2 \int_{1}^{2} \sin u \, du\).</td><td></td><td>X</td></tr><tr><td>e) Es gilt: \(\int_{1}^{2} \sin(2x) \, dx \neq \int_{1}^{2} \sin u \, du\).</td><td></td><td>X</td><td></td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[114, 314, 712, 331]]<|/det|>
## 3. Stammfunktion durch Methode der Substitution bestimmen 

<|ref|>text<|/ref|><|det|>[[114, 331, 780, 364]]<|/det|>
Berechnen Sie die folgenden unbestimmten Integrale mit der Methode der Substitution. 

<|ref|>text<|/ref|><|det|>[[114, 364, 243, 384]]<|/det|>
a) \(\int \sqrt{5 - x} \, dx\) 

<|ref|>text<|/ref|><|det|>[[114, 381, 243, 401]]<|/det|>
c) \(\int e^{4x+2} \, dx\) 

<|ref|>text<|/ref|><|det|>[[114, 400, 258, 421]]<|/det|>
e) \(\int \sqrt[3]{1 - x} \, dx\) 

<|ref|>text<|/ref|><|det|>[[114, 420, 275, 439]]<|/det|>
g) \(\int \sin x \cos x \, dx\) 

<|ref|>text<|/ref|><|det|>[[114, 438, 230, 457]]<|/det|>
i) \(\int \tan x \, dx\) 

<|ref|>text<|/ref|><|det|>[[114, 456, 241, 475]]<|/det|>
k) \(\int \tanh x \, dx\) 

<|ref|>text<|/ref|><|det|>[[484, 364, 644, 384]]<|/det|>
b) \(\int \sqrt{5x + 12} \, dx\) 

<|ref|>text<|/ref|><|det|>[[484, 382, 639, 402]]<|/det|>
d) \(\int (x^2 - 1)^3 \, dx\) 

<|ref|>text<|/ref|><|det|>[[484, 401, 650, 421]]<|/det|>
f) \(\int x \cdot \cos(x^2) \, dx\) 

<|ref|>text<|/ref|><|det|>[[484, 420, 675, 439]]<|/det|>
h) \(\int \sinh x \cosh x \, dx\) 

<|ref|>text<|/ref|><|det|>[[484, 438, 595, 457]]<|/det|>
j) \(\int \cot x \, dx\) 

<|ref|>text<|/ref|><|det|>[[484, 456, 610, 475]]<|/det|>
l) \(\int \coth x \, dx\) 

<|ref|>text<|/ref|><|det|>[[114, 491, 147, 508]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[122, 515, 456, 535]]<|/det|>
\[u(x) := 5 - x \Rightarrow u'(x) = 0 - 1 = -1\]

<|ref|>equation<|/ref|><|det|>[[122, 536, 617, 575]]<|/det|>
\[\frac{du}{dx} = -1 \Leftrightarrow du = (-1) \, dx \Leftrightarrow dx = \frac{du}{-1} = (-1) \, du\]

<|ref|>equation<|/ref|><|det|>[[122, 580, 757, 670]]<|/det|>
\[\begin{align*}
F(x) &= \int \sqrt{5 - x} \, dx = \int \sqrt{u} \cdot (-1) \, du = -\int \sqrt{u} \, du = -\frac{2}{3} u^{\frac{3}{2}} + c \\
&= -\frac{2}{3} (5 - x)^{\frac{3}{2}} + c = -\frac{2}{3} \sqrt{(5 - x)^3} + c.
\end{align*}\]

<|ref|>text<|/ref|><|det|>[[114, 673, 147, 690]]<|/det|>
b) 

<|ref|>equation<|/ref|><|det|>[[122, 694, 540, 752]]<|/det|>
\[\begin{align*}
u(x) &:= 5x + 12 \Rightarrow u'(x) = 5 + 0 = 5 \\
\frac{du}{dx} &= 5 \Leftrightarrow du = 5 \, dx \Leftrightarrow dx = \frac{du}{5} = \frac{1}{5} \, du
\end{align*}\]

<|ref|>text<|/ref|><|det|>[[122, 759, 225, 777]]<|/det|>
und somit 

<|ref|>equation<|/ref|><|det|>[[122, 783, 810, 872]]<|/det|>
\[\begin{align*}
F(x) &= \int \sqrt{5x + 12} \, dx = \frac{1}{5} \int \sqrt{u} \, du = \frac{1}{5} \cdot \frac{2}{3} u^{\frac{3}{2}} + c = \frac{2}{15} (5x + 12)^{\frac{3}{2}} + c \\
&= \frac{2}{15} \sqrt{(5x + 12)^3} + c.
\end{align*}\]