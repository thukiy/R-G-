<|ref|>title<|/ref|><|det|>[[115, 183, 476, 217]]<|/det|>
# Übungsblatt Ana 6 

<|ref|>text<|/ref|><|det|>[[579, 197, 881, 231]]<|/det|>
Computational and Data Science
FS2024 

<|ref|>text<|/ref|><|det|>[[115, 250, 270, 277]]<|/det|>
## Lösungen 

<|ref|>text<|/ref|><|det|>[[750, 258, 880, 275]]<|/det|>
Mathematik 2 

<|ref|>text<|/ref|><|det|>[[115, 303, 210, 320]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 320, 841, 354]]<|/det|>
- Sie kennen die Begriffe Schwerpunkt, Flächenschwerpunkt, Polarkoordinaten, Zylinderkoordinaten und ihre wichtigsten Eigenschaften. 

<|ref|>text<|/ref|><|det|>[[115, 353, 848, 386]]<|/det|>
- Sie können mit Hilfe der Integration den Schwerpunkt homogener Flächen und von Rotationskörpern berechnen. 

<|ref|>text<|/ref|><|det|>[[115, 386, 789, 403]]<|/det|>
- Sie können kartesische in Polarkoordinaten umwandeln und umgekehrt. 

<|ref|>sub_title<|/ref|><|det|>[[115, 435, 432, 453]]<|/det|>
### 1. Schwerpunkt Rotationskörper 

<|ref|>text<|/ref|><|det|>[[115, 452, 825, 486]]<|/det|>
Bestimmen Sie den Schwerpunkt des Rotationskörpers, der durch Drehung der Funktion \(f(x) = \ln x, 1 \le x \le e\) um die x-Achse entsteht. 

<|ref|>text<|/ref|><|det|>[[115, 501, 830, 536]]<|/det|>
Zuerst Berechnung des Volumens des Rotationskörpers (Integral durch 2malige partielle Integration lösen – Integrand ist \(1 \cdot (\ln x)^2\)): 

<|ref|>equation<|/ref|><|det|>[[120, 535, 816, 589]]<|/det|>
\[V_x = \pi \cdot \int_{1}^{e} (\ln x)^2 dx = \pi \left[ x \left((\ln x)^2 - 2 \cdot \ln x + 2\right) \right]_{1}^{e} = \pi (e - 2) = 2,257\]

<|ref|>text<|/ref|><|det|>[[115, 589, 856, 623]]<|/det|>
Der Schwerpunkt liegt auf der x-Achse, d. h. \(y_s = 0\). Integral durch 2malige partielle Integration lösen. 

<|ref|>equation<|/ref|><|det|>[[120, 622, 907, 678]]<|/det|>
\[x_s = \frac{\pi}{V_x} \cdot \int_{1}^{e} x (\ln x)^2 dx = \frac{1}{e - 2} \left[ \frac{1}{2} x^2 \left((\ln x)^2 - \ln x + \frac{1}{2}\right) \right]_{1}^{e} = \frac{e^2 - 1}{4(e - 2)} = 2,224\]

<|ref|>sub_title<|/ref|><|det|>[[115, 695, 250, 712]]<|/det|>
### 2. Kreiskegel 

<|ref|>text<|/ref|><|det|>[[115, 712, 866, 747]]<|/det|>
Gegeben sei ein homogener gerader Kreiskegel mit Radius R, Höhe H und Dichte ρ. Bestimmen Sie das Volumen des Kreiskegels und seinen Schwerpunkt. 

<|ref|>text<|/ref|><|det|>[[115, 761, 870, 836]]<|/det|>
Wir legen den Kegel so ins xy-Koordinatensystem, dass die x-Achse der Symmetrieachse des Kreiskegels entspricht, seine Spitze im Ursprung des Koordinatensystems ist und der Kegel durch Rotation der Geraden \(y = \frac{R}{H}x\) um die x-Achse entsteht.