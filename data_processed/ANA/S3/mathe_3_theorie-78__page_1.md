<|ref|>text<|/ref|><|det|>[[20, 10, 365, 45]]<|/det|>
Bsp: \(\frac{\partial u(x)}{\partial x_1} - \frac{1}{x_1^2} \frac{\partial u(x)}{\partial x_2} = 0\) 

<|ref|>equation<|/ref|><|det|>[[100, 50, 500, 82]]<|/det|>
AB: \(u(x) = x_1\) \(\vec{x} = (\frac{x_1}{x_2})\)

<|ref|>equation<|/ref|><|det|>[[100, 88, 536, 120]]<|/det|>
mit \(\vec{x} \in \Gamma = \{x_1 = x_2; x_1, x_2 > 0\}\)

<|ref|>equation<|/ref|><|det|>[[100, 125, 722, 159]]<|/det|>
geschätzt ist eine Rache \(\{(x_1, x_2, u(x))\} | x_1, x_2 > 0\}\)

<|ref|>equation<|/ref|><|det|>[[100, -1, 632, 201]]<|/det|>
die \(\Gamma = \{(x_1, x_1, x_1), x_1 \in \mathbb{R}\} \text{ enthält}\)

<|ref|>text<|/ref|><|det|>[[100, 225, 435, 250]]<|/det|>
Charakteristisches System : 

<|ref|>equation<|/ref|><|det|>[[135, 262, 375, 287]]<|/det|>
\(k_1'(s) = 1 \quad (= a_1)\)

<|ref|>equation<|/ref|><|det|>[[135, 293, 400, 327]]<|/det|>
\(k_2'(s) = -\frac{1}{x_1^2} \quad (= a_2)\)

<|ref|>equation<|/ref|><|det|>[[135, 333, 320, 368]]<|/det|>
\(= -\frac{1}{x_1^2}\)

<|ref|>equation<|/ref|><|det|>[[135, 375, 380, 404]]<|/det|>
\(w'(s) = 0 \quad (= -b)\)

<|ref|>equation<|/ref|><|det|>[[135, 410, 724, 480]]<|/det|>
Abb. \(s \to \begin{pmatrix} k_1(s) \\ k_2(s) \\ k_3(s) \end{pmatrix}\) beschreibt Charakteristik

<|ref|>text<|/ref|><|det|>[[135, 492, 490, 518]]<|/det|>
1. Schritt : lösen der DGL 

<|ref|>equation<|/ref|><|det|>[[175, 529, 333, 555]]<|/det|>
\(k_1'(s) = 1\)

<|ref|>equation<|/ref|><|det|>[[208, 570, 384, 595]]<|/det|>
\(k_1(s) = s + c_1\)

<|ref|>equation<|/ref|><|det|>[[175, 600, 380, 633]]<|/det|>
\(k_2'(s) = -\frac{1}{x_1^{2}(s)}\)

<|ref|>equation<|/ref|><|det|>[[208, 638, 600, 670]]<|/det|>
\(k_2(s) = -\int \frac{1}{x_1^2} ds = -\int \frac{1}{s+c_1^2} ds\)

<|ref|>equation<|/ref|><|det|>[[278, 680, 494, 705]]<|/det|>
\(= +(s+c_1)^{-1} + c_2\)

<|ref|>equation<|/ref|><|det|>[[175, 720, 330, 745]]<|/det|>
\(w'(s) = 0\)

<|ref|>equation<|/ref|><|det|>[[208, 760, 570, 784]]<|/det|>
\(w(s) = 0 \quad c_1, c_2, c \in \mathbb{R}\)

<|ref|>text<|/ref|><|det|>[[135, 816, 733, 843]]<|/det|>
2. Schritt : Parameterisierung der Anfangslösung 

<|ref|>equation<|/ref|><|det|>[[295, 845, 666, 884]]<|/det|>
mit \(x_1 = t : \begin{pmatrix} \frac{t}{e} \\ 1 \end{pmatrix} \quad t \in \mathbb{R}^+\)

<|ref|>equation<|/ref|><|det|>[[187, 888, 675, 955]]<|/det|>
vergleiche mit Charakteristik \(\begin{pmatrix} \frac{s+c_1}{s+c_1} + c_2 \\ c \end{pmatrix}\)