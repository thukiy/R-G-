<|ref|>sub_title<|/ref|><|det|>[[114, 81, 810, 100]]<|/det|>
## 2. Erwartungswert, Varianz, Standardabweichung diskreter Verteilungen 

<|ref|>text<|/ref|><|det|>[[114, 99, 860, 135]]<|/det|>
Bestimmen Sie den Mittelwert μ, die Varianz σ² und die Standardabweichung σ der folgenden diskreten Verteilungen: 

<|ref|>text<|/ref|><|det|>[[114, 135, 145, 151]]<|/det|>
a) 

<|ref|>table<|/ref|><|det|>[[114, 149, 690, 186]]<|/det|>
<table><tr><td>xi</td><td>-2</td><td>2</td><td>4</td><td>6</td><td>8</td></tr><tr><td>f(xi)</td><td>1/4</td><td>1/6</td><td>1/4</td><td>1/4</td><td>1/12</td></tr></table>

<|ref|>text<|/ref|><|det|>[[114, 185, 145, 200]]<|/det|>
b) 

<|ref|>table<|/ref|><|det|>[[114, 199, 690, 235]]<|/det|>
<table><tr><td>xi</td><td>-2</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>f(xi)</td><td>1/8</td><td>1/4</td><td>1/2</td><td>1/16</td><td>1/16</td></tr></table>

<|ref|>text<|/ref|><|det|>[[114, 235, 145, 251]]<|/det|>
c) 

<|ref|>table<|/ref|><|det|>[[114, 250, 787, 287]]<|/det|>
<table><tr><td>xi</td><td>-2</td><td>-1</td><td>0</td><td>1</td><td>2</td><td>3</td></tr><tr><td>f(xi)</td><td>0,2</td><td>0,3</td><td>0,2</td><td>0,1</td><td>0,05</td><td>0,15</td></tr></table>

<|ref|>text<|/ref|><|det|>[[114, 286, 810, 320]]<|/det|>
d) Bestimmen Sie für c) ausserdem die entsprechenden Kennwerte der von X abhängigen Funktion Z = (X-μ)². 

<|ref|>equation<|/ref|><|det|>[[119, 336, 550, 371]]<|/det|>
\[
\text{a) } \mu = E(X) = -\frac{2}{4} + \frac{2}{6} + \frac{4}{4} + \frac{6}{4} + \frac{8}{12} = 3
\]

<|ref|>equation<|/ref|><|det|>[[155, 378, 515, 413]]<|/det|>
\[
E(X^2) = \frac{4}{4} + \frac{4}{6} + \frac{16}{4} + \frac{36}{4} + \frac{64}{12} = 20
\]

<|ref|>equation<|/ref|><|det|>[[155, 416, 686, 437]]<|/det|>
\[
\sigma^2 = E(X^2) - \mu^2 = 20 - 3^2 = 11; \quad \sigma = \sqrt{11} = 3,3166
\]

<|ref|>equation<|/ref|><|det|>[[119, 445, 675, 480]]<|/det|>
\[
\text{b) } \mu = \frac{23}{16} = 1,4375; \quad \sigma^2 = \frac{575}{256} = 2,2461; \quad \sigma = 1,4987
\]

<|ref|>text<|/ref|><|det|>[[114, 485, 145, 501]]<|/det|>
c) 

<|ref|>equation<|/ref|><|det|>[[119, 500, 645, 520]]<|/det|>
\[
\mu = E(X) = -0,4 - 0,3 + 0 + 0,1 + 0,1 + 0,45 = -0,05
\]

<|ref|>equation<|/ref|><|det|>[[119, 529, 576, 549]]<|/det|>
\[
E(X^2) = 0,8 + 0,3 + 0 + 0,1 + 0,2 + 1,35 = 2,75
\]

<|ref|>equation<|/ref|><|det|>[[119, 556, 835, 578]]<|/det|>
\[
\sigma^2 = E[(X - \mu)^2] = E(X^2) - \mu^2 = 2,75 - (-0,05)^2 = 2,7475; \quad \sigma = 1,6576
\]

<|ref|>text<|/ref|><|det|>[[114, 583, 145, 599]]<|/det|>
d) 

<|ref|>equation<|/ref|><|det|>[[119, 599, 670, 640]]<|/det|>
\[
\mu_Z = E(Z) = \underbrace{E[(X - \mu)^2]}_{\sigma^2} = E[(X + 0,05)^2] = \sigma^2 = 2,7475
\]

<|ref|>equation<|/ref|><|det|>[[119, 645, 785, 732]]<|/det|>
\[
\begin{align*}
E(Z^2) &= E[(X - \mu)^4] = E[(X + 0,05)^4] = \sum_i (x_i + 0,05)^4 \cdot f(x_i) = \\
&= (-2 + 0,05)^4 \cdot 0,2 + (-1 + 0,05)^4 \cdot 0,3 + (0 + 0,05)^4 \cdot 0,2 + \\
&\quad + (1 + 0,05)^4 \cdot 0,1 + (2 + 0,05)^4 \cdot 0,05 + (3 + 0,05)^4 \cdot 0,15 = 17,1212
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[119, 736, 710, 758]]<|/det|>
\[
\sigma_Z^2 = E(Z^2) - \mu_Z^2 = 17,1212 - 2,7475^2 = 9,5724; \quad \sigma_Z = 3,0939
\]

<|ref|>sub_title<|/ref|><|det|>[[114, 776, 370, 793]]<|/det|>
## 3. Lineare Transformation 

<|ref|>text<|/ref|><|det|>[[114, 792, 852, 845]]<|/det|>
Die Zufallsvariable X besitze den Mittelwert E(X) = μx = 2 und die Varianz Var(X) = σx² = 0,5. Berechnen Sie die entsprechenden Kennwerte der folgenden linearen Funktionen von X: 

<|ref|>text<|/ref|><|det|>[[114, 844, 235, 860]]<|/det|>
a) Z = 2X-3, 

<|ref|>text<|/ref|><|det|>[[114, 860, 263, 877]]<|/det|>
b) Z = -0,5X+2, 

<|ref|>text<|/ref|><|det|>[[114, 876, 213, 892]]<|/det|>
c) Z = -X.