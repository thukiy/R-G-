<|ref|>text<|/ref|><|det|>[[119, 81, 875, 110]]<|/det|>
Zu Beginn der Bewegung (d. h. zur Zeit \(t=0\)) beträgt die Geschwindigkeit \(v(0)=10\). Aus dieser Anfangsgeschwindigkeit lässt sich die Integrationskonstante \(K\) wie folgt berechnen: 

<|ref|>equation<|/ref|><|det|>[[164, 117, 797, 133]]<|/det|>
\[v(0) = 10 \Rightarrow 40 + K \cdot e^0 = 40 + K \cdot 1 = 40 + K = 10 \Rightarrow K = 10 - 40 = -30\]

<|ref|>text<|/ref|><|det|>[[119, 140, 468, 155]]<|/det|>
Das gesuchte Geschwindigkeit-Zeit-Gesetz lautet damit 

<|ref|>equation<|/ref|><|det|>[[164, 175, 377, 192]]<|/det|>
\[v = 40 - 30 \cdot e^{-0,1t}, \quad t \ge 0\]

<|ref|>text<|/ref|><|det|>[[119, 199, 490, 227]]<|/det|>
Die Endgeschwindigkeit \(v_E\) erhält man für \(t \to \infty\), d. h. nach (theoretisch) unendlich langer Zeit: 

<|ref|>equation<|/ref|><|det|>[[164, 234, 500, 258]]<|/det|>
\[v_E = \lim_{t \to \infty} v(t) = \lim_{t \to \infty} (40 - 30 \cdot e^{-0,1t}) = 40\]

<|ref|>text<|/ref|><|det|>[[119, 264, 360, 281]]<|/det|>
(e\(^{-0,1t}\) strebt für \(t \to \infty\) gegen 0) 

<|ref|>image<|/ref|><|det|>[[565, 142, 872, 283]]<|/det|>
 

<|ref|>sub_title<|/ref|><|det|>[[115, 308, 397, 326]]<|/det|>
## 6. Salzzugabe in Wassertank 

<|ref|>text<|/ref|><|det|>[[115, 325, 875, 392]]<|/det|>
Ein Tank enthalte 1000 l Wasser, in dem 50 kg Salz gelöst sind. Ab dem Zeitpunkt to = 0 strömen pro Minute 10 l der Lösung aus dem Tank heraus sowie 10 l Wasser mit einem Salzgehalt von 2 kg hinzu. Ein Superrührgerät mischt die Losung sofort vollständig. 

<|ref|>text<|/ref|><|det|>[[115, 390, 490, 408]]<|/det|>
Wie gross ist der Salzgehalt u(t) für t > 0? 

<|ref|>text<|/ref|><|det|>[[119, 423, 710, 475]]<|/det|>
Das Volumen des Wassers im Tank ist konstant, deshalb enthält jeder Liter zur Zeit \(t \ge 0\) die Menge \(u(t)/1000\) kg Salz. Der Ausfluss an Salz (in kg) im (kleinen) Zeitraum \(\Delta t\) ist 

<|ref|>equation<|/ref|><|det|>[[297, 487, 530, 518]]<|/det|>
\[10 \cdot \frac{u(t)}{1000} \Delta t = 0,01 u(t) \Delta t.\]

<|ref|>text<|/ref|><|det|>[[119, 528, 710, 561]]<|/det|>
Zugleich werden \(2\Delta t\) kg Salz in den Tank eingebracht. Die Änderung des Salzgehaltes ist also 

<|ref|>equation<|/ref|><|det|>[[297, 574, 530, 591]]<|/det|>
\[\Delta u = -0,01 u(t) \Delta t + 2 \Delta t.\]

<|ref|>text<|/ref|><|det|>[[119, 602, 540, 620]]<|/det|>
Für \(\Delta t \to 0\) führt dies auf die Differentialgleichung 

<|ref|>equation<|/ref|><|det|>[[338, 632, 488, 649]]<|/det|>
\[u' = -0,01 u + 2.\]

<|ref|>text<|/ref|><|det|>[[119, 660, 588, 678]]<|/det|>
Lösung der Gleichung mit Trennung der Variablen liefert 

<|ref|>equation<|/ref|><|det|>[[140, 686, 688, 723]]<|/det|>
\[\int \frac{du}{-0,01u+2} = \int dt \iff \ln|-0,01u+2| = -\frac{t}{100} + \tilde{c}, \quad \tilde{c} \in \mathbb{R},\]

<|ref|>text<|/ref|><|det|>[[119, 732, 210, 748]]<|/det|>
und damit 

<|ref|>equation<|/ref|><|det|>[[273, 748, 555, 769]]<|/det|>
\[u(t) = 200 - 100 c e^{-t/100}, \quad c \in \mathbb{R}.\]

<|ref|>text<|/ref|><|det|>[[119, 774, 576, 793]]<|/det|>
Aus der Anfangsbedingung \(u(0) = 50\) folgt \(c = 1,5\) und 

<|ref|>equation<|/ref|><|det|>[[310, 801, 520, 821]]<|/det|>
\[u(t) = 200 - 150 e^{-t/100}.\]