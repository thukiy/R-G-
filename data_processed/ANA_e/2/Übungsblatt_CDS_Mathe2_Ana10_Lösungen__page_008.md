<|ref|>text<|/ref|><|det|>[[114, 84, 140, 100]]<|/det|>
a) 

<|ref|>sub_title<|/ref|><|det|>[[114, 99, 420, 117]]<|/det|>
Wir bilden die Lagrange-Funktion 

<|ref|>equation<|/ref|><|det|>[[300, 120, 546, 138]]<|/det|>
\[
L(x, y, \lambda) := f(x, y) + \lambda g(x, y)
\]

<|ref|>text<|/ref|><|det|>[[122, 149, 298, 165]]<|/det|>
und lösen das System 

<|ref|>equation<|/ref|><|det|>[[292, 175, 551, 199]]<|/det|>
\[
\text{grad } f(x, y) + \lambda \text{ grad } g(x, y) \stackrel{!}{=} 0.
\]

<|ref|>text<|/ref|><|det|>[[122, 215, 337, 231]]<|/det|>
Ausgeschrieben ergibt sich 

<|ref|>equation<|/ref|><|det|>[[368, 235, 478, 252]]<|/det|>
\[
-x + \lambda = 0,
\]

<|ref|>equation<|/ref|><|det|>[[368, 258, 478, 275]]<|/det|>
\[
-2y + \lambda = 0,
\]

<|ref|>equation<|/ref|><|det|>[[390, 282, 476, 298]]<|/det|>
\[
x + y = 1.
\]

<|ref|>text<|/ref|><|det|>[[122, 305, 723, 339]]<|/det|>
Dies ist glücklicherweise ein lineares Gleichungssystem mit den Unbekannten
\(x, y, \lambda \in \mathbb{R}\), und wie Sie leicht nachrechnen, lautet die eindeutige Lösung 

<|ref|>equation<|/ref|><|det|>[[315, 350, 530, 367]]<|/det|>
\[
(x, y, \lambda) = (2/3, 1/3, 2/3).
\]

<|ref|>text<|/ref|><|det|>[[122, 383, 723, 433]]<|/det|>
Die Funktion \(f\) nimmt also über der Geraden \(G := \{(x, y)^T \in \mathbb{R}^2 : x + y = 1\}\)
im Punkt \(x_0 = (2/3, 1/3)\) ein Maximum an mit dem Funktionswert \(f(x_0) = 11/3\). 

<|ref|>text<|/ref|><|det|>[[122, 435, 720, 468]]<|/det|>
Alternativ lässt sich hier die Nebenbedingung sehr leicht nach einer der beiden
Variablen auflösen, z. B. 

<|ref|>equation<|/ref|><|det|>[[377, 467, 460, 483]]<|/det|>
\[
y = 1 - x.
\]

<|ref|>text<|/ref|><|det|>[[122, 496, 521, 513]]<|/det|>
Damit ergibt sich eine Funktion in einer Variablen 

<|ref|>equation<|/ref|><|det|>[[270, 521, 569, 553]]<|/det|>
\[
h(x) := f(x, 1 - x) = -\frac{3}{2}x^2 + 2x + 3.
\]

<|ref|>text<|/ref|><|det|>[[122, 569, 483, 586]]<|/det|>
Die notwendige Optimalitätsbedingung liefert 

<|ref|>equation<|/ref|><|det|>[[283, 595, 556, 626]]<|/det|>
\[
h'(x) = -3x + 2 \stackrel{!}{=} 0 \iff x = \frac{2}{3}
\]

<|ref|>text<|/ref|><|det|>[[122, 635, 504, 652]]<|/det|>
und damit \(y = 1/3\). Die hinreichende Bedingung 

<|ref|>equation<|/ref|><|det|>[[317, 662, 523, 681]]<|/det|>
\[
h''(x) = -3 = h(2/3) < 0
\]

<|ref|>text<|/ref|><|det|>[[122, 692, 450, 708]]<|/det|>
bestätigt das Maximum in diesem Punkt. 

<|ref|>text<|/ref|><|det|>[[114, 707, 140, 723]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[114, 723, 463, 741]]<|/det|>
Sind x, y, z die Seitenlängen, dann gilt 

<|ref|>equation<|/ref|><|det|>[[359, 741, 484, 758]]<|/det|>
\[
U = x + y + z,
\]

<|ref|>text<|/ref|><|det|>[[122, 768, 567, 786]]<|/det|>
wobei \(\in \mathbb{R}_+\) gegeben ist. Der Flächeninhalt lautet damit 

<|ref|>equation<|/ref|><|det|>[[229, 797, 612, 840]]<|/det|>
\[
F(x, y, z) = \sqrt{\frac{U}{2} \left(\frac{U}{2} - x\right) \left(\frac{U}{2} - y\right) \left(\frac{U}{2} - z\right)}.
\]