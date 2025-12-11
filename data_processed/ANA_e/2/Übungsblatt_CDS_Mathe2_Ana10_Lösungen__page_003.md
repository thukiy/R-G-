<|ref|>equation<|/ref|><|det|>[[120, 84, 650, 106]]<|/det|>
a) \(f(-1,0) = (-1)^3 - 1^2 \ln(0+1) - 3(-1) = -1 + 3 = 2\)

<|ref|>equation<|/ref|><|det|>[[120, 104, 640, 133]]<|/det|>
b) \(grad f(x,y)^T = (3x^2 - 2x \ln(y^2 + 1) - 3, -x^2 \frac{2y}{y^2+1})\)

<|ref|>equation<|/ref|><|det|>[[120, 131, 572, 194]]<|/det|>
c) \(H(x,y) = \begin{pmatrix} 6x - 2 \ln(y^2 + 1) & -\frac{4xy}{y^2+1} \\ -\frac{4xy}{y^2+1} & -2x^2 \frac{1-y^2}{(y^2+1)^2} \end{pmatrix}\)

<|ref|>equation<|/ref|><|det|>[[120, 195, 737, 252]]<|/det|>
d) \(grad f(x,y) = o \iff 3x^2 - 2x \ln(y^2 + 1) - 1 = 0 \quad (\Rightarrow x \neq 0) \\ x^2y = 0 \quad (\Rightarrow y = 0 \text{ wegen } x \neq 0) \\ \Rightarrow 3x^2 - 3 = 0 \text{ bzw. } x = \pm 1\)

<|ref|>equation<|/ref|><|det|>[[147, 250, 585, 271]]<|/det|>
\(grad f(x,y) = o \text{ für } (x,y) = (1,0) \text{ oder } (-1,0)\)

<|ref|>text<|/ref|><|det|>[[115, 270, 144, 288]]<|/det|>
e) 

<|ref|>text<|/ref|><|det|>[[115, 285, 880, 308]]<|/det|>
Gleichung der Tangentialhyperebene \(y = f(\hat{x}) + grad f(\hat{x})^T(x - \hat{x})\) für \((x,y) = (3,1)\) 

<|ref|>equation<|/ref|><|det|>[[115, 312, 875, 428]]<|/det|>
\[
\begin{align*}
(\hat{x}^3 - \hat{x}^2 \ln(\hat{y}^2 + 1) - 3\hat{x}) + (3\hat{x}^2 - 2\hat{x} \ln(\hat{y}^2 + 1) - 3, & -\hat{x}^2 \cdot \frac{2\hat{y}}{\hat{y}^2+1}) \cdot \begin{pmatrix} x - \hat{x} \\ y - \hat{y} \end{pmatrix} \\
&= (3^3 - 3^2 \ln(1^2 + 1) - 3 \cdot 3) + (3 \cdot 3^2 - 2 \cdot 3 \ln(1^2 + 1) - 3, & -3^2 \cdot \frac{2 \cdot 1}{1^2+1}) \cdot \begin{pmatrix} x - 3 \\ y - 1 \end{pmatrix} \\
&= -45 + 9 \ln(2) + 24x - 6x \ln(2) - 9y
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[115, 444, 357, 462]]<|/det|>
3. Kritische Stellen in 3D 

<|ref|>text<|/ref|><|det|>[[115, 461, 702, 480]]<|/det|>
Bestimmen Sie alle kritischen Stellen der gegebenen Funktionen. 

<|ref|>equation<|/ref|><|det|>[[115, 478, 792, 499]]<|/det|>
a) \(f(x,y) = y^3 + x^2y - 3y + 8\) b) \(f(x,y) = 3x^2y + y^3 - 27y + 4\)

<|ref|>text<|/ref|><|det|>[[115, 512, 144, 529]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[115, 527, 512, 546]]<|/det|>
Gradient und Hesse-Matrix ergeben sich zu 

<|ref|>equation<|/ref|><|det|>[[123, 549, 855, 595]]<|/det|>
\[
\nabla f = \begin{bmatrix} f_{,x} \\ f_{,y} \end{bmatrix} = \begin{bmatrix} 2xy \\ 3y^2 + x^2 - 3 \end{bmatrix} \quad \text{und} \quad \nabla^2 f = \begin{bmatrix} f_{,x,x} & f_{,x,y} \\ f_{,y,x} & f_{,y,y} \end{bmatrix} = \begin{bmatrix} 2y & 2x \\ 2x & 6y \end{bmatrix}
\]

<|ref|>text<|/ref|><|det|>[[115, 597, 415, 616]]<|/det|>
Für kritische Stellen muss gelten 

<|ref|>equation<|/ref|><|det|>[[123, 620, 474, 669]]<|/det|>
\[
\nabla f = 0 \Leftrightarrow \begin{cases} \text{I: } & 2xy = 0 \\ \text{II: } & 3y^2 + x^2 - 3 = 0. \end{cases}
\]

<|ref|>text<|/ref|><|det|>[[115, 670, 714, 689]]<|/det|>
Aus Gleichung I folgt, dass entweder \(x = 0\) oder \(y = 0\) gelten muss. 

<|ref|>text<|/ref|><|det|>[[120, 692, 459, 712]]<|/det|>
Fall 1: \(x = 0\). Aus der Gleichung II 

<|ref|>equation<|/ref|><|det|>[[360, 723, 741, 746]]<|/det|>
\[
3y^2 - 3 = 0 \Leftrightarrow y^2 = 1 \Leftrightarrow y \in \{-1, 1\}.
\]

<|ref|>text<|/ref|><|det|>[[120, 758, 457, 778]]<|/det|>
Fall 2: \(y = 0\). Aus der Gleichung II 

<|ref|>equation<|/ref|><|det|>[[340, 788, 763, 820]]<|/det|>
\[
x^2 - 3 = 0 \Leftrightarrow x^2 = 3 \Leftrightarrow x \in \left\{-\sqrt{3}, \sqrt{3}\right\}.
\]