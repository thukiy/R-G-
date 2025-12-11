<|ref|>text<|/ref|><|det|>[[118, 81, 544, 99]]<|/det|>
Mit diesem Ansatz und den zugehörigen Ableitungen 

<|ref|>equation<|/ref|><|det|>[[161, 107, 520, 127]]<|/det|>
\[ \dot{x}_p = \omega_0 A \cdot \cos(\omega_0 t) - \omega_0 B \cdot \sin(\omega_0 t) \]

<|ref|>equation<|/ref|><|det|>[[161, 134, 535, 156]]<|/det|>
\[ \ddot{x}_p = -\omega_0^2 A \cdot \sin(\omega_0 t) - \omega_0^2 B \cdot \cos(\omega_0 t) \]

<|ref|>text<|/ref|><|det|>[[118, 166, 427, 183]]<|/det|>
gehen wir in die inhomogene Dgl ein: 

<|ref|>equation<|/ref|><|det|>[[161, 192, 870, 300]]<|/det|>
\[ \begin{align*} -\omega_0^2 A \cdot \sin(\omega_0 t) - \dot{\omega}_0^2 B \cdot \cos(\omega_0 t) + 2\dot{\delta}[\omega_0 A \cdot \cos(\omega_0 t) - \omega_0B \cdot \sin(\omega_0 t)] + \\ + \omega_0^2[A \cdot \sin(\omega_0 t) + B \cdot \cos(\omega_0 t)] = a \cdot \cos(\omega_0 t) \Rightarrow \\ -\omega_0^2 A \cdot \sin(\omega_0 t) - \ddot{\omega}_0^2 B \cdot \cos(\omega_0 t) + 3\dot{\delta}\omega_0 A \cdot \cos(\omega_0 t) - 2\dot{\delta}\omega_0 B \cdot \sin(\omega_0 t) + \\ + \omega_0^2 A \cdot \sin(\omega_0 t) + \omega_0^2 B \cdot \cos(\omega_0 t) = a \cdot \cos(\omega_0 t) \end{align*} \]

<|ref|>text<|/ref|><|det|>[[118, 300, 457, 316]]<|/det|>
Diese Gleichung reduziert sich wie folgt: 

<|ref|>equation<|/ref|><|det|>[[161, 325, 802, 344]]<|/det|>
\[ 2\dot{\delta}\omega_0 A \cdot \cos(\omega_0 t) = 2\dot{\delta}\omega_0 B \cdot \sin(\omega_0) = a \cdot \cos(\omega_0 t) + 0 \cdot \sin(\omega_0 t) \]

<|ref|>text<|/ref|><|det|>[[118, 354, 878, 404]]<|/det|>
Auf der rechten Seite haben wir dabei den verschwindenden Sinusterm \(0 \cdot \sin(\omega_0 t)\) addiert. Durch Koeffizientenvergleich der Kosinus- bzw. Sinusterme beiderseits lassen sich dann die gesuchten Koeffizienten \(A\) und \(B\) bestimmen: 

<|ref|>equation<|/ref|><|det|>[[161, 410, 813, 443]]<|/det|>
\[ 2\dot{\delta}\omega_0 A = a \Rightarrow A = \frac{a}{2\dot{\delta}\omega_0} \quad \text{und} \quad -2\dot{\delta}\omega_0 B = 0 \Rightarrow B = 0 \]

<|ref|>text<|/ref|><|det|>[[118, 452, 410, 469]]<|/det|>
Somit lautet die partikuläre Lösung 

<|ref|>equation<|/ref|><|det|>[[161, 476, 366, 507]]<|/det|>
\[ x_p = \frac{a}{2\dot{\delta}\omega_0} \cdot \sin(\omega_0 t) \]

<|ref|>text<|/ref|><|det|>[[118, algemeine Lösung der inhomogenen Schwingungsgleichung ist dann die Summe aus \(x_0\) und \(x_p\): 

<|ref|>equation<|/ref|><|det|>[[161, 550, 840, 580]]<|/det|>
\[ x(t) = x_0 + x_p = e^{-\delta t} [C_1 \cdot \sin(\omega_d t) + C_2 \cdot \cos(\omega_d t)] + \frac{a}{2\dot{\delta}\omega_0} \cdot \sin(\dot{\omega}_0 t) \]

<|ref|>text<|/ref|><|det|>[[118, 590, 875, 623]]<|/det|>
Die beiden Integrationskonstanten \(C_1\) und \(C_2\) berechnen wir aus den Anfangsbedingungen \(x(0) = 0\) und \(\dot{x}(0) = 0\) wie folgt: 

<|ref|>equation<|/ref|><|det|>[[161, 631, 767, 664]]<|/det|>
\[ x(0) = 0 \Rightarrow 1 [C_1 \cdot \sin 0 + C_2 \cdot \cos 0] + \frac{a}{2\dot{\delta}\omega_0} \cdot \sin 0 = 0 \Rightarrow \]

<|ref|>equation<|/ref|><|det|>[[161, 671, 808, 703]]<|/det|>
\[ C_1 \cdot 0 + C_2 \cdot 1 + \frac{a}{2\dot{\delta}\omega_0} \cdot 0 = 0 \Rightarrow 0 + C_2 + 0 = 0 \Rightarrow C_2 = 0 \]

<|ref|>text<|/ref|><|det|>[[118, 716, 690, 750]]<|/det|>
Zwischenergebnis: \(x(t) = C_1 \cdot e^{-\delta t} \cdot \sin(\omega_d t) + \frac{a}{2\dot{\delta}\omega_0} \cdot \sin (\omega_0 t)\) 

<|ref|>text<|/ref|><|det|>[[118, 756, 775, 774]]<|/det|>
Die benötigte Ableitung \(\dot{x}(t)\) erhalten wir mit Hilfe der Produkt- und Kettenregel: 

<|ref|>equation<|/ref|><|det|>[[161, 781, 875, 822]]<|/det|>
\[ \dot{x}(t) = C_1 [e^{-\delta t} \cdot (-\dot{\delta}) \cdot \sin(\omega_d t) + \cos(\omega_d t) \cdot \omega_d \cdot e^{-\delta t}] + \frac{a}{2\dot{\delta}\omega_0} \cdot \cos(\omega_0 t) \cdot \omega_0 = \\ = C_1 \cdot e^{-\delta t} [-\dot{\delta} \cdot \sin(\omega_d t) + \omega_d \cdot \cos(\omega_d t)] + \frac{a}{2\dot{\delta}} \cdot \cos(\omega_0 t) \]

<|ref|>equation<|/ref|><|det|>[[161, 852, 768, 884]]<|/det|>
\[ \dot{x}(0) = 0 \Rightarrow C_1 \cdot 1 [-\dot{\delta} \cdot \sin 0 + \omega_d \cdot \cos 0] + \frac{a}{2\dot{\delta}} \cdot \cos 0 = 0 \Rightarrow \]

<|ref|>equation<|/ref|><|det|>[[161, 891, 873, 923]]<|/det|>
\[ C_1 [-\dot{\delta} \cdot 0 + \omega_d \cdot 1] + \frac{a}{2\dot{\delta}} \cdot 1 = 0 \Rightarrow C_1 \omega_d + \frac{a}{2\dot{\delta}} = 0 \Rightarrow C_1 = -\frac{a}{2\dot{\delta}\omega_d} \]