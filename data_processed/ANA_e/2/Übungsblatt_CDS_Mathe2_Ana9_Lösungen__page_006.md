<|ref|>text<|/ref|><|det|>[[117, 81, 715, 98]]<|/det|>
Wir setzen die Ausdrücke für \(z\), \(z_x\) und \(z_y\) seitenweise in die vorgegebene Gleichung ein: 

<|ref|>equation<|/ref|><|det|>[[117, 102, 880, 159]]<|/det|>
\[
\begin{align*}
\text{Linke Seite: } xz_x + yz_y &= x(y + \ln y - \ln x - 1) + y\left(x + \frac{x}{y}\right) = xy + x \cdot \ln y - x \cdot \ln x - x + xy + x = \\
&= 2xy + x \cdot \ln y - x \cdot \ln x = x(2y + \ln y - \ln x)
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[117, 167, 850, 184]]<|/det|>
Rechte Seite: \(xy + z = xy + xy + x \cdot \ln y - x \cdot \ln x = 2xy + x \cdot \ln y - x \cdot \ln x = x (2y + \ln y - \ln x)\) 

<|ref|>text<|/ref|><|det|>[[117, 190, 472, 205]]<|/det|>
Ein Vergleich zeigt, dass beide Seiten übereinstimmen. 

<|ref|>text<|/ref|><|det|>[[117, 205, 150, 222]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[117, 222, 570, 237]]<|/det|>
Wir bilden zunächst die benötigten partiellen Ableitungen \(f_t\) und \(f_{xx}\). 

<|ref|>text<|/ref|><|det|>[[117, 246, 270, 262]]<|/det|>
Partielle Ableitung \(f_t\) 

<|ref|>equation<|/ref|><|det|>[[157, 273, 872, 303]]<|/det|>
\[
f = e^{-\pi^2 a^2 t} \cdot \sin(\pi x) = \sin(\pi x) \cdot e^{-\pi^2 a^2 t} = \sin(\pi x) \cdot e^u \quad \text{mit} \quad u = -\pi^2 a^2 t \quad \text{und} \quad \frac{\partial u}{\partial t} = -\pi^2 a^2
\]

<|ref|>text<|/ref|><|det|>[[117, 310, 560, 326]]<|/det|>
Mit der Kettenregel erhält man \((\sin(\pi x))\) ist ein konstanter Faktor): 

<|ref|>equation<|/ref|><|det|>[[157, 333, 880, 363]]<|/det|>
\[
f_t = \frac{\partial f}{\partial t} = \frac{\partial f}{\partial u} \cdot \frac{\partial u}{\partial t} = \sin(\pi x) \cdot e^u \cdot (-\pi^2 a^2) = -\pi^2 a^2 \cdot \sin(\pi x) \cdot e^u = -\pi^2 a^2 \cdot \sin(\pi x) \cdot e^{-\pi^2 a^2 t}
\]

<|ref|>text<|/ref|><|det|>[[117, 360, 280, 375]]<|/det|>
Partielle Ableitung \(f_{xx}\) 

<|ref|>text<|/ref|><|det|>[[117, 379, 880, 410]]<|/det|>
Wir differenzieren die Funktion \(f(x; t)\) zweimal nacheinander partiell nach \(x\), wobei wir jedes Mal die Kettenregel benutzen (\(e^{-\pi^2 a^2 t}\) ist dabei ein konstanter Faktor): 

<|ref|>equation<|/ref|><|det|>[[157, 415, 666, 455]]<|/det|>
\[
f = e^{-\pi^2 a^2 t} \cdot (\sin(\pi x)) = e^{-\pi^2 a^2 t} \cdot \sin u \quad \text{mit} \quad u = \pi x \quad \text{und} \quad \frac{\partial u}{\partial x} = \pi
\]

<|ref|>equation<|/ref|><|det|>[[157, 463, 835, 499]]<|/det|>
\[
f_x = \frac{\partial f}{\partial x} = \frac{\partial f}{\partial u} \cdot \frac{\partial u}{\frac{\partial u}{\partial x}} = e^{-\pi^2 a^2 t} \cdot (\cos u) \cdot \pi = \pi \cdot e^{-\pi^2 a^2 t} \cdot \cos u \quad \text{mit} \quad u = \pi x \quad \text {und} \quad \frac{\partial u}{\partial x} = \pi
\]

<|ref|>text<|/ref|><|det|>[[117, 540, 415, 556]]<|/det|>
Wir multiplizieren \(f_{xx}\) mit \(a^2\) und erhalten: 

<|ref|>equation<|/ref|><|det|>[[157, 561, 702, 600]]<|/det|>
\[
a^2 \cdot f_{xx} = a^2 \left[-\pi^2 \cdot e^{-\pi^2 a^2 t} \cdot \sin(\pi x)\right] = -\pi^2 a^2 \cdot \sin(\pi x) \cdot e^{-2\pi^2 a^2 t} = f_t
\]

<|ref|>text<|/ref|><|det|>[[117, 607, 714, 624]]<|/det|>
Die gegebene Funktion erfüllt somit (wie behauptet) die Differentialgleichung \(a^2 \cdot f_{xx} = f_t\). 

<|ref|>sub_title<|/ref|><|det|>[[117, 639, 304, 657]]<|/det|>
5. Tangentialebene 

<|ref|>text<|/ref|><|det|>[[117, 656, 470, 674]]<|/det|>
Bestimmen Sie die Tangentialebene zu 

<|ref|>text<|/ref|><|det|>[[117, 673, 496, 704]]<|/det|>
a) \(f(x, y) = \frac{x^3}{y+3}\) im Punkt \((x_0, y_0) = (2; 1)\). 

<|ref|>text<|/ref|><|det|>[[117, 701, 595, 723]]<|/det|>
b) \(f(x, y) = (x^2 + y^2) \cdot e^{-x}\) im Punkt \((x_0, y_0) = (0; 1)\). 

<|ref|>text<|/ref|><|det|>[[117, 720, 702, 755]]<|/det|>
c) \(f(x, y) = 3 \cdot \sqrt{\frac{x^2}{y} + 2 \cdot \cos(\pi(x+2y))}\) im Punkt \((x_0, y_0) = (2; 1)\).