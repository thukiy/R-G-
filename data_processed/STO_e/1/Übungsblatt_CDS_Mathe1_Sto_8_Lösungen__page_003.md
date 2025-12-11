<|ref|>equation<|/ref|><|det|>[[117, 81, 565, 120]]<|/det|>
\[
\text{a) } f(x) = \binom{8}{x} 0,2^x \cdot 0,8^{8-x} \quad (x = 0,1,2, \dots, 8)
\]

<|ref|>text<|/ref|><|det|>[[154, 128, 277, 144]]<|/det|>
Stabdiagramm: 

<|ref|>table<|/ref|><|det|>[[156, 150, 295, 355]]<|/det|>
<table><tr><td>x</td><td>f(x)</td></tr><tr><td>0</td><td>0,1678</td></tr><tr><td>1</td><td>0,3355</td></tr><tr><td>2</td><td>0,2936</td></tr><tr><td>3</td><td>0,1468</td></tr><tr><td>4</td><td>0,0459</td></tr><tr><td>5</td><td>0,0092</td></tr><tr><td>6</td><td>0,0011</td></tr><tr><td>7</td><td>0,0001</td></tr><tr><td>8</td><td>0</td></tr></table>

<|ref|>image<|/ref|><|det|>[[448, 130, 826, 390]]<|/det|>
 

<|ref|>equation<|/ref|><|det|>[[117, 398, 390, 416]]<|/det|>
\[
\text{b) } P(X = 0) = f(0) = 0,1678
\]

<|ref|>equation<|/ref|><|det|>[[154, 422, 580, 441]]<|/det|>
\[
P(X \ge 5) = f(5) + f(6) + f(7) + f(8) = 0,0104
\]

<|ref|>equation<|/ref|><|det|>[[154, 447, 555, 465]]<|/det|>
\[
P(1 \le X \le 3) = f(1) + f(2) + f(3) = 0,7759
\]

<|ref|>sub_title<|/ref|><|det|>[[115, 481, 543, 500]]<|/det|>
3. Qualitätskontrolle → Eckey S. 99 Bsp. 6.5 

<|ref|>text<|/ref|><|det|>[[115, 498, 833, 549]]<|/det|>
Bei der Produktion eines Gutes sind 10% Ausschuss. Wie gross ist die
Wahrscheinlichkeit, dass von 20 produzierten Stücken mindestens 4 Ausschuss
sind? 

<|ref|>text<|/ref|><|det|>[[117, 563, 785, 652]]<|/det|>
Hier ist die Binomialverteilung anzuwenden, weil es nur zwei Ausgänge gibt
(Ausschuss, kein Ausschuss) und eine konstante Wahrscheinlichkeit vorgegeben
ist. Ob ein defektes oder brauchbares Gut ausgewählt wurde, verändert nicht die
Wahrscheinlichkeit dafür, dass das nächste entnommene Teil Ausschuss ist.
Mit Hilfe der Wahrscheinlichkeit für Ausschuss 

<|ref|>equation<|/ref|><|det|>[[216, 657, 277, 675]]<|/det|>
\(p = 0,1\)

<|ref|>text<|/ref|><|det|>[[117, 681, 530, 699]]<|/det|>
erhält man folgende Wahrscheinlichkeitsfunktion: 

<|ref|>equation<|/ref|><|det|>[[214, 704, 598, 789]]<|/det|>
\[
\mathbf{f}(\mathbf{x}) = \begin{cases} (20) \cdot 0,1^x \cdot 0,9^{20-x} & \text{für } x = 0,1,2,\dots,20 \\ 0 & \text{sonst} \end{cases}
\]