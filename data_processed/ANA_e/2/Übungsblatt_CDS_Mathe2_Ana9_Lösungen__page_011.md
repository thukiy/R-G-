<|ref|>equation<|/ref|><|det|>[[120, 84, 650, 106]]<|/det|>
a) \(f(-1,0) = (-1)^3 - 1^2 \ln(0+1) - 3(-1) = -1 + 3 = 2\)

<|ref|>equation<|/ref|><|det|>[[120, 103, 640, 132]]<|/det|>
b) \(grad f(x,y)^T = (3x^2 - 2x \ln(y^2 + 1) - 3, -x^2 \frac{2y}{y^2+1})\)

<|ref|>equation<|/ref|><|det|>[[120, 130, 570, 193]]<|/det|>
c) \(H(x,y) = \begin{pmatrix} 6x - 2 \ln(y^2 + 1) & -\frac{4xy}{y^2+1} \\ -\frac{4xy}{y^2+1} & -2x^2 \frac{1-y^2}{(y^2+1)^2} \end{pmatrix}\)

<|ref|>equation<|/ref|><|det|>[[120, 196, 737, 255]]<|/det|>
d) \(grad f(x,y) = o \iff 3x^2 - 2x \ln(y^2 + 1) - 2 = 0 \quad (\Rightarrow x \neq 0) \\ x^2y = 0 \quad (\Rightarrow y = 0 \text{ wegen } x \neq 0) \\ \Rightarrow 3x^2 - 3 = 0 \text{ bzw. } x = \pm 1\)

<|ref|>equation<|/ref|><|det|>[[120, 252, 585, 272]]<|/det|>
\(grad f(x,y) = o \text{ für } (x,y) = (1,0) \text{ oder } (-1,0)\)

<|ref|>text<|/ref|><|det|>[[115, 271, 144, 288]]<|/det|>
e) 

<|ref|>text<|/ref|><|det|>[[115, 285, 880, 308]]<|/det|>
Gleichung der Tangentialhypeberene \(y = f(\hat{x}) + grad f(\hat{x})^T(x - \hat{x})\) für \((x,y) = (3,1)\) 

<|ref|>equation<|/ref|><|det|>[[115, 312, 875, 425]]<|/det|>
\[
\begin{align*}
(\hat{x}^3 - \hat{x}^2 \ln(\hat{y}^2 + 1) - 3\hat{x}) + (3\hat{x}^2 - 2\hat{x} \ln(\hat{y}^2 + 1) - 3, & -\hat{x}^2 \cdot \frac{2\hat{y}}{\hat{y}^2+1}) \cdot \begin{pmatrix} x - \hat{x} \\ y - \hat{y} \end{pmatrix} \\
= (3^3 - 3^2 \ln(1^2 + 1) - 3 \cdot 3) + (3 \cdot 3^2 - 2 \cdot 3 \ln(1^2 + 1) - 3, & -3^2 \cdot \frac{2 \cdot 1}{1^2+1}) \cdot \begin{pmatrix} x - 3 \\ y - 1 \end{pmatrix} \\
= -45 + 9 \ln(2) + 24x - 6x \ln(2) - 9y
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[115, 444, 387, 463]]<|/det|>
9. Volumenänderung Tonne 

<|ref|>text<|/ref|><|det|>[[115, 461, 853, 545]]<|/det|>
Das Volumen einer Tonne wird nach der Formel \(V = \frac{1}{3} \pi h (2R^2 + r^2)\) berechnet. Es liegen folgende Werte vor: \(R = 1\) m, \(r = 0,8\) m, \(h = 1,5\) m. Wie ändert sich das Volumen \(V\), wenn man bei unveränderter Höhe \(h\) den Radius \(R\) um 2% vergrössert und gleichzeitig den Radius \(r\) um 2,5% verkleinert? 

<|ref|>text<|/ref|><|det|>[[115, 539, 856, 573]]<|/det|>
Führen Sie sowohl eine exakte als auch eine näherungsweise Berechnung (totales Differenzial) durch. 

<|ref|>sub_title<|/ref|><|det|>[[115, 586, 297, 601]]<|/det|>
Exakte Volumenänderung 

<|ref|>equation<|/ref|><|det|>[[115, 605, 470, 622]]<|/det|>
Ausgangswerte: \(R = 1\) m, \(r = 0,8\) m, h = 1,50 m

<|ref|>equation<|/ref|><|det|>[[231, 625, 577, 653]]<|/det|>
\[
V_1 = \frac{1}{3} \pi \cdot 1,50 (2 \cdot 1^2 + 0,8^2) \, \text{m}^3 = 4,1469 \, \text{m}^3
\]

<|ref|>equation<|/ref|><|det|>[[115, 657, 707, 673]]<|/det|>
Neue Werte: \(R = 1,02 \cdot 1\) m = 1,02 m, \(r = 0,975 \cdot 0,8\) m = 0,78 m, h = 1,50 m

<|ref|>equation<|/ref|><|det|>[[231, 675, 601, 703]]<|/det|>
\[
V_2 = \frac{1}{3} \pi \cdot 1,50 (2 \times 1,02^2 + 0,78^2) \, \text{m}^3 = 4,2242 \, \text{m}^3
\]

<|ref|>equation<|/ref|><|det|>[[115, 703, 675, 720]]<|/det|>
Exakte Volumenänderung: \(\Delta V = V_2 - V_1 = (4,2242 - 4,1469) \, \text{m}^3 = 0,0773 \, \text{m}^3\)

<|ref|>equation<|/ref|><|det|>[[115, 723, 671, 760]]<|/det|>
Prozentuale Änderung des Volumens: \(\frac{\Delta V}{V_1} \cdot 100\% = \frac{0,0773 \, \text{m}^3}{4,1469 \, \text{m}^3} \cdot 100\% = 1,86\%\)

<|ref|>sub_title<|/ref|><|det|>[[115, 770, 450, 786]]<|/det|>
Näherungsrechnung mit dem totalen Differential 

<|ref|>text<|/ref|><|det|>[[115, 790, 880, 832]]<|/det|>
Es ändern sich die Radien \(R\) und \(r\), nicht aber die Höhe \(h\) der Tonne. Daher können wir in diesem Zusammenhang das Volumen \(V\) als eine nur von \(R\) und \(r\) abhängige Funktion betrachten (Alternative: \(V\) als eine von \(R\), \(r\) und \(h\) abhängige Funktion ansehen und im totalen Differential \(dh = 0\) setzen):