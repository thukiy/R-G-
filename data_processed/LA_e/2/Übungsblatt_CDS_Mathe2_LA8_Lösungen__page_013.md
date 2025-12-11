<|ref|>text<|/ref|><|det|>[[115, 81, 728, 220]]<|/det|>
1. Das zweite Bild zeigt das Bild des Quadrats unter der Abbildung \(\Phi_1\). Wir sehen, dass das Quadrat in Richtung \((0, 1)^\top\) um Faktor 2 gestreckt wird, in Richtung \((1, 0)^\top\) keine Änderung vorliegt. Das heisst, dass \(\Phi_1((0, 1)^\top) = 2(0, 1)^\top\) und \(\Phi_1((1, 0)^\top) = (1, 0)^\top\). Damit haben wir schon die zwei Eigenwerte \(\lambda_1 = 2\) und \(\lambda_2 = 1\) von \(\Phi_1\) bestimmt und kennen auch Eigenvektoren \((0, 1)^\top\) und \((1, 0)^\top\). 

<|ref|>text<|/ref|><|det|>[[115, 220, 730, 454]]<|/det|>
2. Im dritten Bild sehen wir das Bild des Quadrats unter \(\Phi_2\), wo offenbar die Punkte \(D\) und \(B\) auf den Ursprung abgebildet wurden. Das bedeutet, dass \(\Phi_2((-1, 1)^\top) = (0, 0)^\top\), und wir erhalten den ersten Eigenwert \(\lambda_1 = 0\) mit einem Eigenvektor \((-1, 1)^\top\). Die Punkte \(A\) und \(C\) wurden nicht nur um Faktor 2 gestreckt, sondern auch am Ursprung gespiegelt, also ist \(\Phi_2((1, 1)^\top) = -2(1, 1)^\top\), und wir erhalten den zweiten Eigenwert \(\lambda_2 = -2\) mit Eigenvektor \((1, 1)^\top\). Diese Abbildung ist aber weder eine Projektion, noch eine Spiegelung oder Streckung im klassischen Sinne, doch bezogen auf den Eigenwert 0 hat sie zumindest einen Charakter einer Projektion auf die Gerade \(G: x_1 - x_2 = 0\). 

<|ref|>sub_title<|/ref|><|det|>[[115, 470, 275, 488]]<|/det|>
## 9. Unternehmen 

<|ref|>text<|/ref|><|det|>[[115, 487, 870, 538]]<|/det|>
Ein Unternehmen produziert in der Periode t drei Güter in den Quantitäten \(x_t, y_t\) und \(z_t\), die in der Folgeperiode t + 1 teilweise als Rohstoffe wieder verwendet werden. Es gilt der Zusammenhang 

<|ref|>equation<|/ref|><|det|>[[115, 535, 583, 588]]<|/det|>
\[ \begin{pmatrix} x_{t+1} \\ y_{t+1} \\ z_{t+1} \end{pmatrix} = \begin{pmatrix} a & 1/2 & 0 \\ b & 1 & c \\ 0 & c & 3/4 \end{pmatrix} \begin{pmatrix} x_t \\ y_t \\ z_t \end{pmatrix} = A \begin{pmatrix} x_t \\ y_t \\ z_t \end{pmatrix}, a, b, c \in \mathbb{R}. \]

<|ref|>text<|/ref|><|det|>[[115, 593, 875, 644]]<|/det|>
Die Matrix A besitzt den Eigenwert \(\lambda = 3/2\) und den zugehörigen Eigenvektor \(\begin{pmatrix} u \\ u \\ 0 \end{pmatrix}\) mit \(u > 0\). 

<|ref|>text<|/ref|><|det|>[[115, 643, 602, 662]]<|/det|>
a) Bestimmen Sie die Konstanten \(a, b, c\), der Matrix A. 

<|ref|>text<|/ref|><|det|>[[115, 660, 835, 707]]<|/det|>
b) Interpretieren Sie den Eigenwert \(\lambda\) und den Eigenvektor \(\begin{pmatrix} u \\ u \\ 0 \end{pmatrix}\) bezogen auf die Aufgabenstellung, wenn ein gleichmässiger Wachstumsprozess unterstellt wird. 

<|ref|>text<|/ref|><|det|>[[115, 707, 875, 803]]<|/det|>
c) Die Gesamtoutput für die 3 Güter im Zeitpunkt t beträgt 200 Einheiten. Wie verteilen sich diese Einheiten bei Unterstellung eines gleichförmigen Wachstumsprozesses auf \(x_t, y_t\) und \(z_t\)? Geben Sie die Anzahl der zu produzierenden Güter für die Perioden t + 1 und t + 2 an, wenn ein gleichmässiger Wachstumsprozess unterstellt wird.