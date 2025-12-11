<|ref|>image<|/ref|><|det|>[[118, 83, 740, 344]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[118, 346, 300, 365]]<|/det|>
Gemäss Skizze gilt 

<|ref|>equation<|/ref|><|det|>[[118, 372, 280, 410]]<|/det|>
\[ \tan(\eta) = \frac{2}{4} = \frac{1}{2}. \]

<|ref|>text<|/ref|><|det|>[[118, 417, 241, 437]]<|/det|>
Daraus folgt 

<|ref|>equation<|/ref|><|det|>[[118, 444, 822, 545]]<|/det|>
\[ \cos(\eta) = \frac{1}{\sqrt{1 + \tan^2(\eta)}} = \frac{1}{\sqrt{1 + \left(\frac{1}{2}\right)^2}} = \frac{1}{\sqrt{1 + \frac{1}{4}}} = \frac{1}{\sqrt{\frac{5}{4}}} = \frac{1}{\sqrt{\frac{5}{4}}} = \sqrt{\frac{4}{5}} = \frac{2}{\sqrt{5}} = \frac{2}{\sqrt{5}} = \frac{2}{\sqrt{\frac{5}{4}}} = \frac{2}{\sqrt{5}} = \frac{2}{\sqrt{5}}. \]

<|ref|>text<|/ref|><|det|>[[118, 548, 150, 565]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[118, 564, 660, 582]]<|/det|>
Wir bestimmen die Ecke A durch Drehung des Seitenvektors 

<|ref|>equation<|/ref|><|det|>[[118, 582, 680, 625]]<|/det|>
\[ \mathbf{a} = \mathbf{B} - \mathbf{C} = \begin{bmatrix} 2 \\ 1/4 \end{bmatrix} - \begin{bmatrix} 2 \\ 4 \end{bmatrix} = \begin{bmatrix} 2 - 2 \\ 0.25 - 4 \end{bmatrix} = \begin{bmatrix} 0 \\ -3.75 \end{bmatrix} \]

<|ref|>text<|/ref|><|det|>[[118, 628, 500, 647]]<|/det|>
Die hierfür benötigte Drehmatrix \(\mathbf{R}(-2\eta)\) ist 

<|ref|>equation<|/ref|><|det|>[[118, 644, 875, 770]]<|/det|>
\[ \begin{aligned} R(-\eta) &= R^T(\eta) = \begin{bmatrix} \cos(\eta) & \sin(\eta) \\ -\sin(\eta) & \cos(\eta) \end{bmatrix} = \begin{bmatrix} \frac{2}{\sqrt{5}} & \frac{1}{\sqrt{5}} \\ -\frac{1}{\sqrt{5}} & \frac{2}{\sqrt{5}} \end{bmatrix} = \frac{1}{\sqrt{5}} \begin{bmatrix} 2 & 1 \\ -1 & 2 \end{bmatrix} \\ R(-2\eta) &= R^2(-\eta) = \left(\frac{1}{\sqrt{5}}\right)^2 \cdot \begin{bmatrix} 2 & 1 \\ -1 & 2 \end{bmatrix}^2 = \frac{1}{5} \cdot \begin{bmatrix} 2 \cdot 2 + 1 \cdot (-1) & 2 \cdot 1 + 1 \cdot 2 \\ (-1) \cdot 2 + 2 \cdot (-1) & (-1) \cdot 1 + 2 \cdot 2 \end{bmatrix} \\ &= \frac{1}{5} \cdot \begin{bmatrix} 3 & 4 \\ -4 & 3 \end{bmatrix}. \end{aligned} \]

<|ref|>text<|/ref|><|det|>[[118, 780, 430, 798]]<|/det|>
Es ergibt sich für den Seitenvektor 

<|ref|>equation<|/ref|><|det|>[[118, 800, 824, 900]]<|/det|>
\[ \mathbf{b} = R(-2\eta) \cdot \mathbf{a} = \frac{1}{5} \cdot \begin{bmatrix} 3 & 4 \\ 4 & 3 \end{bmatrix} \cdot \begin{bmatrix} 0 \\ -3.75 \end{bmatrix} = \frac{1}{5} \cdot \begin{bmatrix} 3 \cdot 0 + 4 \cdot (-3.75) \\ (-4) \cdot 0 + 3 \cdot (-3.75) \end{bmatrix} \\ = \frac{1}{5} \cdot \begin{bmatrix} -15 \\ -11.25 \end{bmatrix} = \begin{bmatrix} -3 \\ -2.25 \end{bmatrix} \]

<|ref|>text<|/ref|><|det|>[[118, 899, 384, 917]]<|/det|>
Und somit der Eckpunkt A zu