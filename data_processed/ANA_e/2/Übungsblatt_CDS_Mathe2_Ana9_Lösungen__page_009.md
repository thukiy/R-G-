<|ref|>text<|/ref|><|det|>[[119, 86, 585, 102]]<|/det|>
Wegen der erwähnten Symmetrie gilt (x wird durch y bzw. z ersetzt): 

<|ref|>equation<|/ref|><|det|>[[162, 107, 465, 142]]<|/det|>
\[u_y = \frac{3y}{x^2 + y^2 + z^2}, \quad u_z = \frac{3z}{x^2 + y^2 + z^2}\]

<|ref|>text<|/ref|><|det|>[[119, 147, 485, 163]]<|/det|>
Das totale Differential besitzt dann die folgende Gestalt: 

<|ref|>equation<|/ref|><|det|>[[162, 166, 815, 234]]<|/det|>
\[ \begin{aligned} du &= u_x dx + u_y dy + u_z dz = \frac{3x}{x^2 + y^2 + z^2} dx + \frac{3y}{x^2 + y^2 + z^2} dy + \frac{3z}{x^2 + y^2 + z^2} dz = \\ &= \frac{3x dx + 3y dy + 3z dz}{x^2 + y^2 + z^2} = \frac{3(x dx + y dy + z dz)}{x^2 + y^2 + z^2} \end{aligned} \]

<|ref|>text<|/ref|><|det|>[[119, 233, 645, 248]]<|/det|>
An der Stelle \(x = -1, y = 2, z = -2\) lautet das totale Differential wie folgt: 

<|ref|>equation<|/ref|><|det|>[[162, 252, 772, 288]]<|/det|>
\[ du = \frac{3(-1 dx + 2 dy - 2 dz)}{(-1)^2 + 2^2 + (-2)^2} = \frac{3}{9} (-dx + 2 dy - 2 dz) = \frac{1}{3} (-dx + 2 dy - 2 dz) \]

<|ref|>text<|/ref|><|det|>[[119, 293, 525, 308]]<|/det|>
**Näherungswert für \(dx = 0,1\), \(dy = -0,2\) und \(dz = -0,1\)** 

<|ref|>equation<|/ref|><|det|>[[162, 312, 699, 373]]<|/det|>
\[ \begin{aligned} u(x = -1; y = 2; z = -2) &= \frac{3}{2} \cdot \ln [2 \cdot (-1)^2 + 2 \cdot 2^2 + 2 \cdot (-2)^2] = \\ &= \frac{3}{2} \cdot \ln (2 + 8 + 8) = \frac{3}{2} \cdot \ln 18 = 4,3356 \end{aligned} \]

<|ref|>text<|/ref|><|det|>[[119, 374, 555, 390]]<|/det|>
Totales Differential für \(dx = 0,1\), \(dy = -0,2\) und \( dz = -0,1\): 

<|ref|>equation<|/ref|><|det|>[[162, 393, 800, 423]]<|/det|>
\[ du = \frac{1}{3} [-0,1 + 2 \cdot (-0,2) - 2 \cdot (-0,1)] = \frac{1}{3} (-0,1 - 0,4 + 0,2) = \frac{1}{3} \cdot (-0,3) = -0,1 \]

<|ref|>text<|/ref|><|det|>[[119, 426, 465, 441]]<|/det|>
Näherungswert: \(u + du = 4,3356 - 0,1 = 4,2356\) 

<|ref|>text<|/ref|><|det|>[[119, 448, 585, 463]]<|/det|>
Exakter Funktionswert: \(u(x = -0,9; y = 1,8; z = -2,1) = 4,2427\) 

<|ref|>sub_title<|/ref|><|det|>[[119, 477, 585, 496]]<|/det|>
## 7. Ableitungen von Funktionen in zwei Variablen 

<|ref|>text<|/ref|><|det|>[[119, 495, 800, 528]]<|/det|>
Berechnen Sie jeweils den Gradienten und die Hesse-Matrix der gegebenen Funktion. 

<|ref|>equation<|/ref|><|det|>[[119, 527, 873, 565]]<|/det|>
\[ \begin{aligned} a) f(x, y) &= 3x + 5y \\ d) f(x, y) &= 2^{3x-5y} \end{aligned} \qquad \begin{aligned} b) f(x, y) &= x^2 + 2xy - 3y^2 \\ e) V(r, h) &= \pi r^2 h \end{aligned} \qquad \begin{aligned} c) f(x, y) &= x^2y^2 + 1 \\ f) \psi(t, x) &= A \sin(\omega t - kx) \end{aligned} \]

<|ref|>text<|/ref|><|det|>[[119, 580, 150, 596]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[119, 595, 512, 613]]<|/det|>
Gradient und Hesse-Matrix ergeben sich zu 

<|ref|>equation<|/ref|><|det|>[[125, 616, 500, 664]]<|/det|>
\[ \nabla f = \begin{bmatrix} f_{,1} \\ f_{,2} \end{bmatrix} = \begin{bmatrix} 3 \cdot 1 + 0 \\ 0 + 5 \cdot 1 \end{bmatrix} = \begin{bmatrix} 3 \\ 5 \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[119, 679, 435, 727]]<|/det|>
\[ \nabla^2 f = \begin{bmatrix} f_{,1,1} & f_{,1,2} \\ f_{,2,1} & f_{,2,2} \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} \]

<|ref|>text<|/ref|><|det|>[[119, 732, 150, 748]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[119, 747, 512, 765]]<|/det|>
Gradient und Hesse-Matrix ergeben sich zu 

<|ref|>equation<|/ref|><|det|> [[125, 765, 660, 813]]<|/det|>
\[ \nabla f = \begin{bmatrix} f_{,1} \\ f_2 \end{bmatrix} = \begin{bmatrix} 2x^{2-1} + 2 \cdot 1 \cdot y - 0 \\ 0 + 2x \cdot 1 - 3 \cdot 2y^{2-1} \end{bmatrix} = \begin{bmatrix} 2x + 2y \\ 2x - 6y \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[119, 828, 686, 875]]<|/det|>
\[ \nabla^2 f = \begin{bmatrix} f_{,1,2} & f_{,1,2} \\ f_{,2,1} & f_2,2 \end{bmatrix} = \begin{bmatrix} 2 \cdot 1 + 0 & 0 + 2 \cdot 1 \\ 2 \cdot 1 - 0 & 0 - 6 \cdot 1 \end{bmatrix} = \begin{bmatrix} 2 & 2 \\ 2 & -6 \end{bmatrix} \]