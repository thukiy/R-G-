<|ref|>equation<|/ref|><|det|>[[25, 15, 440, 48]]<|/det|>
\[8) f(x, y) = 3x^2y + y^3 - 27y + 4\]

<|ref|>equation<|/ref|><|det|>[[75, 52, 375, 100]]<|/det|>
\[\nabla f(x, y) = \begin{pmatrix} 6xy \\ 3x^2 + 3y^2 - 27 \end{pmatrix}\]

<|ref|>equation<|/ref|><|det|>[[75, 110, 644, 140]]<|/det|>
\[\nabla f(x, y) = 0 \quad \text{um wütsche Stellen zu finden}\]

<|ref|>equation<|/ref|><|det|>[[100, 150, 380, 179]]<|/det|>
\[6xy = 0 \quad (1)\]

<|ref|>equation<|/ref|><|det|>[[100, 188, 380, 216]]<|/det|>
\[3x^2 + 3y^2 - 27 = 0 \quad (2)\]

<|ref|>equation<|/ref|><|det|>[[100, 226, 577, 255]]<|/det|>
aus (1): entweder \(x = 0\) oder \(y = 0\)

<|ref|>equation<|/ref|><|det|>[[100, 264, 300, 291]]<|/det|>
Fall 1: \(x = 0\)

<|ref|>equation<|/ref|><|det|>[[228, 301, 375, 328]]<|/det|>
\[3y^2 - 27 = 0\]

<|ref|>equation<|/ref|><|det|>[[228, 340, 525, 368]]<|/det|>
\[y^2 = 9 \quad y_{1,2} = \pm 3\]

<|ref|>equation<|/ref|><|det|>[[192, 378, 515, 405]]<|/det|>
\[\Rightarrow P_1(0; 3) \quad P_2(0; -3)\]

<|ref|>equation<|/ref|><|det|>[[100, 415, 300, 442]]<|/det|>
Fall 2: \(y = 0\)

<|ref|>equation<|/ref|><|det|>[[228, 452, 350, 479]]<|/det|>
\[3x^2 - 27 = 0\]

<|ref|>equation<|/ref|><|det|>[[228, 490, 456, 518]]<|/det|>
\[x^2 = 9 \quad x_{1,2} = \pm 3\]

<|ref|>equation<|/ref|><|det|>[[192, 528, 511, 555]]<|/det|>
\[\Rightarrow P_3(3; 0) \quad P_4(-3; 0)\]

<|ref|>text<|/ref|><|det|>[[85, 587, 830, 615]]<|/det|>
Hesse Matrix bilden, um Art des Extremums zu bestimmen: 

<|ref|>equation<|/ref|><|det|>[[115, 622, 500, 677]]<|/det|>
\[H_f = \begin{pmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{pmatrix} = \begin{pmatrix} 6y & 6x \\ 6x & 6y \end{pmatrix}\]

<|ref|>equation<|/ref|><|det|>[[115, 686, 375, 710]]<|/det|>
\[\det H_f = 36y^2 - 36x^2\]

<|ref|>table<|/ref|><|det|>[[78, 737, 833, 885]]<|/det|>
<table><tr><td>\(P_1(0; 3)\)</td><td>\(\det H_f > 0\)</td><td>\(f_{xx} = 18 > 0\)</td><td>kolales Minimum</td></tr><tr><td>\(P_2(0; -3)\)</td><td>\(\det H_f > 0\)</td><td>\(f_{xx} =-18 < 0\)</td><td>kolales Maximum</td></tr><tr><td>\(P_3(3; 0)\)</td><td>\(\det H_f < 0\)</td><td>Sahlepunkt</td><td></td></tr><tr><td>\(P_4(-3; 0)\)</td><td>\(\det H_f < 0\)</td><td>Sahlepunkt</td><td></td></tr></table>