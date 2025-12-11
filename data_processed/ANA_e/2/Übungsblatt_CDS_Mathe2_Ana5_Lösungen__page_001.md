<|ref|>title<|/ref|><|det|>[[115, 183, 390, 217]]<|/det|>
Übungsblatt 5 

<|ref|>text<|/ref|><|det|>[[576, 196, 880, 232]]<|/det|>
Computational and Data Science
FS2024 

<|ref|>text<|/ref|><|det|>[[115, 250, 270, 278]]<|/det|>
Lösungen 

<|ref|>text<|/ref|><|det|>[[750, 256, 880, 274]]<|/det|>
Mathematik 2 

<|ref|>text<|/ref|><|det|>[[115, 303, 210, 320]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 320, 825, 371]]<|/det|>
- Sie kennen die Begriffe Bogenlänge, Mantelfläche von Rotationskörpern, Massenmittelpunkt, Schwerpunkt, Flächenschwerpunkt, und ihre wichtigsten Eigenschaften. 

<|ref|>text<|/ref|><|det|>[[115, 369, 828, 420]]<|/det|>
- Sie können mit Hilfe der Integration die Bogenlänge einer ebenen Kurve, die Mantelfläche und das Volumen von Rotationskörpern und den Schwerpunkt homogener Flächen und Rotationskörper berechnen. 

<|ref|>sub_title<|/ref|><|det|>[[115, 452, 247, 468]]<|/det|>
1. Kettenlinie 

<|ref|>text<|/ref|><|det|>[[115, 468, 825, 519]]<|/det|>
Welche Länge besitzt ein Drahtseil, das gemäss der Funktion \(f(x) = \cosh x\) durchhängt, wenn beide Aufhängepunkte (spiegelsymmetrisch zur y-Achse) die gleiche Höhe und einen Abstand von 4 m voneinander besitzen? 

<|ref|>text<|/ref|><|det|>[[115, 533, 792, 552]]<|/det|>
Zur Bestimmung der Bogenlänge einer ebenen Kurve nutzen wir die Formel 

<|ref|>equation<|/ref|><|det|>[[115, 551, 644, 576]]<|/det|>
\[L = \int_a^b \sqrt{1 + (f'(x))^2} \, dx, \text{ wobei } w = -2 \text{ und } b = 2 \text{ wählen.}\]

<|ref|>text<|/ref|><|det|>[[115, 575, 819, 597]]<|/det|>
Wir können die Funktionsgleichung umschreiben: \(f(x) = \cosh x = \frac{1}{2}(e^x + e^{-x})\). 

<|ref|>text<|/ref|><|det|>[[115, 597, 530, 625]]<|/det|>
Ableitung bilden: \(f'(x) = \sinh x = \frac{1}{2}(e^x - e^{-x})\) 

<|ref|>equation<|/ref|><|det|>[[115, 627, 872, 710]]<|/det|>
\[ \text{Integrand berechnen: } \sqrt{1 + (f'(x))^2} = \sqrt{1 + \left(\frac{1}{2}(e^x - e^{-x})\right)^2} = \sqrt{1 + \frac{1}{4}e^{2x} - \frac{1}{2} + \frac{1}{4}e^{-2x}} \\ = \sqrt{\frac{1}{4}e^{2x} + \frac{1}{2} + \frac{1}{4}e^{-2x}} = \sqrt{\frac{1}{4}(e^{2x} + 2 + e^{-2x})} = \frac{1}{2}\sqrt{(e^x + e^{-x})^2} = \frac{1}{2}(e^x + e^{-x}) \]

<|ref|>text<|/ref|><|det|>[[115, 708, 603, 726]]<|/det|>
Integral berechnen und somit Bogenlänge bestimmen: 

<|ref|>equation<|/ref|><|det|>[[147, 724, 844, 780]]<|/det|>
\[ L = \int_{-2}^{2} \frac{1}{2}(e^x + e^{-x}) \, dx = 2 \cdot \frac{1}{2} \int_{0}^{2}(e^x + e^{-x}) \, dx = [e^x - e^{-x}]_{0}^{2} = e^2 - e^{-2} = 7,254 \]

<|ref|>sub_title<|/ref|><|det|>[[115, 792, 444, 809]]<|/det|>
2. Volumen und Masse einer Vase 

<|ref|>text<|/ref|><|det|>[[115, 809, 336, 826]]<|/det|>
Es seien die Funktionen 

<|ref|>equation<|/ref|><|det|>[[115, 825, 748, 848]]<|/det|>
\[ f_a: [0, H] \to \mathbb{R}, f_a(x) = C \cdot \sqrt{x - x_a} \text{ und } f_i: [x_i, H] \to \mathbb{R}, f_i(x) = C \cdot \sqrt{x - x_i} \]

<|ref|>text<|/ref|><|det|>[[115, 846, 426, 864]]<|/det|>
mit \(x_a < 0 < H\) und \(C > 0\) gegeben. 

<|ref|>text<|/ref|><|det|>[[115, 863, 875, 913]]<|/det|>
Die Vase entsteht durch Rotation um die x-Achse der Querschnittsfläche (grün in der Skizze), die durch die beiden Funktionen zwischen \(x = 0\) und \(x = H\) eingeschlossen wird.