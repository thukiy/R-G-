<|ref|>sub_title<|/ref|><|det|>[[114, 81, 250, 100]]<|/det|>
## 6. Kreiskegel 

<|ref|>text<|/ref|><|det|>[[114, 99, 870, 136]]<|/det|>
Gegeben sei ein homogener gerader Kreiskegel mit Radius R, Höhe H und Dichte ρ.
Bestimmen Sie das Volumen des Kreiskegels und seinen Schwerpunkt. 

<|ref|>text<|/ref|><|det|>[[114, 149, 872, 224]]<|/det|>
Wir legen den Kegel so ins xy-Koordinatensystem, dass die x-Achse der Symmetrieachse des Kreiskegels entspricht, seine Spitze im Ursprung des Koordinatensystems ist und der Kegel durch Rotation der Geraden \(y = \frac{R}{H}x\) um die x-Achse entsteht. 

<|ref|>image<|/ref|><|det|>[[333, 225, 660, 373]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[114, 372, 210, 390]]<|/det|>
Volumen: 

<|ref|>equation<|/ref|><|det|>[[114, 386, 630, 422]]<|/det|>
\[V = \pi \int_{0}^{H} \left(\frac{R}{H}x\right)^2 dx = \pi \frac{R^2}{H^2} \int_{0}^{H} x^2 dx = \pi \frac{R^2}{H^2} \left[\frac{1}{3}x^3\right]_{0}^{H} = \frac{1}{3}\pi R^2 H\]

<|ref|>text<|/ref|><|det|>[[114, 433, 741, 452]]<|/det|>
Der Schwerpunkt liegt aus Symmetriegründen auf der x-Achse (yₛ=0): 

<|ref|>equation<|/ref|><|det|>[[114, 450, 664, 512]]<|/det|>
\[x_s = \frac{\pi}{\frac{1}{3}\pi R^2 H} \int_{0}^{H} x \left(\frac{R}{H}x\right)^2 dx = \frac{3}{R^2 H} \int_{0}^{H} x \frac{R^2}{H^2} x^2 dx = \frac{3}{R^2 H} \cdot \frac{R^2}{H^2} \int_{0}^{H} x^3 dx \\ = \frac{3}{H^3} \left[\frac{1}{4}x^4\right]_{0}^{H} = \frac{3}{H^3} \cdot \frac{1}{4} H^4 = \frac{3}{4} H\]

<|ref|>sub_title<|/ref|><|det|>[[114, 524, 430, 543]]<|/det|>
## 7. Mantelfläche Rotationskörper 

<|ref|>text<|/ref|><|det|>[[114, 541, 845, 583]]<|/det|>
Bestimmen Sie die Mantelfläche Mₓ des Rotationskörpers, der durch Drehung der Kettenlinie \(f(x) = c \cdot \cosh\left(\frac{x}{c}\right)\), \(-c \le x \le c\) um die x-Achse entsteht. 

<|ref|>image<|/ref|><|det|>[[114, 600, 490, 757]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[114, 758, 618, 778]]<|/det|>
Bestimmung der Mantelfläche bei Rotation um x-Achse: 

<|ref|>equation<|/ref|><|det|>[[124, 777, 386, 824]]<|/det|>
\[M_x = 2\pi \cdot \int_{a}^{b} y \cdot \sqrt{1 + (y')^2} \, dx\]

<|ref|>text<|/ref|><|det|>[[114, 823, 819, 859]]<|/det|>
Ableiten der Funktion f(x)=y, Bestimmung des Radikanden im Integral und des Integranden: