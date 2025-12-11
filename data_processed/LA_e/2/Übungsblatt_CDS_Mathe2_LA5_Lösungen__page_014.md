<|ref|>sub_title<|/ref|><|det|>[[114, 81, 330, 100]]<|/det|>
## 9. Drehmatrizen in 2D 

<|ref|>text<|/ref|><|det|>[[114, 98, 870, 118]]<|/det|>
Im Folgenden lernen Sie Form und Eigenschaften von Drehmatrizen in 2D kennen. 

<|ref|>text<|/ref|><|det|>[[114, 115, 875, 152]]<|/det|>
a) Bestimmen Sie die Matrix \(R_\alpha\) mit Hilfe des Spaltenvektor Konstruktionsverfahrens, die die Drehung um den Ursprung um den Winkel \(\alpha \in \mathbb{R}\) beschreibt. 

<|ref|>text<|/ref|><|det|>[[114, 150, 875, 222]]<|/det|>
b) Bestimmen Sie die Matrix \(R_{-\alpha}\) mit Hilfe des Spaltenvektor Konstruktionsverfahrens, die die Drehung um dem Ursprung um den Winkel \(-\alpha \in \mathbb{R}\) (also Drehung im Uhrzeigersinn) beschreibt. Hinweis: Verwenden Sie die Paritätseigenschaften, dass gilt: \(\sin(-\alpha) = -\sin \alpha\) und \(\cos(-\alpha) = \cos \alpha\). 

<|ref|>text<|/ref|><|det|>[[114, 230, 844, 267]]<|/det|>
c) Welcher Zusammenhang besteht zwischen den Drehmatrizen aus Aufgabe a) und b)? Berechnen Sie die Matrixprodukte \(R_\alpha \cdot R_{-\alpha}\) und \(R_{-\alpha} \cdot R_\alpha\). 

<|ref|>text<|/ref|><|det|>[[114, 265, 737, 284]]<|/det|>
d) Berechnen Sie die Matrixprodukte \(R_\alpha \cdot R_\beta\) und \(R_\beta \cdot R_\alpha\) mit \(\alpha, \beta \in \mathbb{R}\). 

<|ref|>text<|/ref|><|det|>[[144, 283, 875, 335]]<|/det|>
Hinweis: Überlegen Sie sich, was passiert, wenn man nacheinander die Drehungen auf denselben Vektor ausführt. Nutzen Sie die Additionstheoreme zur Vereinfachung der Matrizen. 

<|ref|>text<|/ref|><|det|>[[114, 335, 792, 364]]<|/det|>
e) Geben Sie die Drehmatrizen für \(\alpha \in \{0, \pm \frac{\pi}{6}, \pm \frac{\pi}{4}, \pm \frac{\pi}{3}, \pm \frac{\pi}{2}, \pm \pi\}\) explizit an. 

<|ref|>text<|/ref|><|det|>[[114, 377, 144, 394]]<|/det|>
a) 

<|ref|>image<|/ref|><|det|>[[114, 393, 655, 688]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[114, 692, 880, 765]]<|/det|>
In der Zeichnung haben wir die Bilder der Vektoren \(\hat{e}_x\) und \(\hat{e}_y\) eingezeichnet, die wir durch Anwenden der Matrix \(R_\alpha\) erhalten. Somit können wir aus der Zeichnung nun die Vektorkomponenten ablesen und das Spaltenvektor Konstruktionsverfahren zur Bestimmung der Matrix \(R_\alpha\) anwenden. 

<|ref|>equation<|/ref|><|det|>[[114, 760, 777, 802]]<|/det|>
\[ \frac{R_\alpha}{R_\alpha} = \begin{bmatrix} R_\alpha \cdot \hat{e}_x & R_\alpha \cdot \hat{e}_y \end{bmatrix} = \begin{bmatrix} \cos(\alpha) \\ \sin(\alpha) \end{bmatrix} \begin{bmatrix} -\sin(\alpha) \\ \cos(\alpha) \end{bmatrix} = \begin{bmatrix} \cos(\alpha) & -\sin(\alpha) \\ \sin(\alpha) & \cos(\alpha) \end{bmatrix}. \]

<|ref|>text<|/ref|><|det|>[[114, 805, 147, 822]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[114, 821, 699, 840]]<|/det|>
Wir ersetzen in der Matrix \(R_\alpha\) den Winkel \(\alpha\) durch \(-\alpha\) und erhalten 

<|ref|>equation<|/ref|><|det|>[[119, 840, 583, 880]]<|/det|>
\[ \frac{R_{-\alpha}}{R_{-\alpha}} = \begin{bmatrix} \cos(-\alpha) & -\sin(-\alpha) \\ \sin(-\alpha) & \cos(-\alpha) \end{bmatrix} = \begin{bmatrix} \cos(\alpha) & \sin(\alpha) \\ -\sin(\alpha) & \cos(\alpha) \end{bmatrix}. \]