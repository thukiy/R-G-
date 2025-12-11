<|ref|>image<|/ref|><|det|>[[117, 81, 720, 501]]<|/det|>
 

<|ref|>sub_title<|/ref|><|det|>[[114, 534, 750, 570]]<|/det|>
## 5. Geschwindigkeit-Zeit-Gesetz einer beschleunigten Masse unter Berücksichtigung der Reibung 

<|ref|>text<|/ref|><|det|>[[114, 568, 844, 620]]<|/det|>
Die Bewegung einer Masse, die durch eine konstante Kraft beschleunigt wird und einer der Geschwindigkeit v proportionalen Reibungskraft unterliegt, genüge der folgenden DGL: 

<|ref|>equation<|/ref|><|det|>[[114, 618, 570, 644]]<|/det|>
\[10 \frac{dv}{dt} + v = 40 \text{ mit Anfangsbedingung } v(0) = 10.\]

<|ref|>text<|/ref|><|det|>[[114, 643, 550, 661]]<|/det|>
a) Wie lautet das Geschwindigkeit-Zeit-Gesetz? 

<|ref|>text<|/ref|><|det|>[[114, 660, 608, 679]]<|/det|>
b) Welche Endgeschwindigkeit \(v_e\) erreicht die Masse? 

<|ref|>text<|/ref|><|det|>[[119, 697, 592, 712]]<|/det|>
Zunächst trennen wir die Variablen, dann werden beide Seiten integriert: 

<|ref|>equation<|/ref|><|det|>[[164, 718, 875, 751]]<|/det|>
\[10 \cdot \frac{dv}{dt} = 40 - v = -(v - 40) \quad \Rightarrow \quad \frac{dv}{v - 40} = -\frac{dt}{10} = -0,1 \, dt \quad \Rightarrow \quad \int \frac{dv}{v - 40} = -0,1 \cdot \int 1 \, dt\]

<|ref|>equation<|/ref|><|det|>[[164, 781, 857, 813]]<|/det|>
\[\ln |v - 40| = -0,1t + \ln |C| \quad \Rightarrow \quad \ln |v - 40| - \ln |C| = -0,1t \quad \Rightarrow \quad \ln \left|\frac{v - 40}{C}\right| = -0,1t\]

<|ref|>equation<|/ref|><|det|>[[125, 819, 833, 852]]<|/det|>
\[\left|\frac{v - 40}{C}\right| = e^{-0,1t} \quad \Rightarrow \quad \frac{v - 40}{C} = \pm e^{-0,1t} \quad \Rightarrow \quad v - 40 = \pm C \cdot e^{-0,1t} = K \cdot e^{-0,1t} \quad \Rightarrow\]

<|ref|>equation<|/ref|><|det|>[[125, 860, 432, 878]]<|/det|>
\[v = 40 + K \cdot e^{-0,1t} \quad (\text{mit } K = \pm C)\]