<|ref|>table<|/ref|><|det|>[[115, 80, 879, 151]]<|/det|>
<table><tr><td>d) Wegen der AB ist die Lösung des AWP trivial, d. h. x(t) = 0.</td><td>X</td></tr><tr><td>e) Die Anregung der Schwingung erfolgt mit der Resonanzfrequenz des Systems.</td><td>X</td></tr><tr><td>f) Es gilt \(x(t) \to 0\) für \(t \to \infty\).</td><td>X</td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[115, 166, 300, 184]]<|/det|>
## 3. RLC-Schaltkreis 

<|ref|>text<|/ref|><|det|>[[115, 184, 805, 237]]<|/det|>
Gegeben sei ein RLC-Schaltkreis, der aus einem Widerstand \(R = 10 \Omega\), einer Induktivität \(L = 18 \text{ mH}\), einer Kapazität \(C = 141 \mu \text{F}\) und einer externen Wechselspannungsquelle mit Effektivspannung 5 V bestehe. 

<|ref|>image<|/ref|><|det|>[[338, 243, 655, 336]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[115, 341, 840, 360]]<|/det|>
a) Stellen Sie eine DGL für die Spannung \(U_C(t)\) auf, die am Kondensator anliegt. 

<|ref|>text<|/ref|><|det|>[[115, 358, 875, 393]]<|/det|>
b) Bestimmen Sie die ungedämpfte Kreisfrequenz und die Dämpfungskonstante des Systems. Welcher Fall liegt vor? 

<|ref|>text<|/ref|><|det|>[[115, 391, 852, 426]]<|/det|>
c) Bestimmen Sie die Frequenz des ungedämpften und des gedämpften Systems und die Resonanzfrequenz. 

<|ref|>text<|/ref|><|det|>[[115, 442, 142, 458]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[115, 457, 425, 475]]<|/det|>
Wir wenden die Maschenregel an: 

<|ref|>equation<|/ref|><|det|>[[171, 472, 400, 491]]<|/det|>
\[U_R + U_L + U_C - U_a(t) = 0\]

<|ref|>equation<|/ref|><|det|>[[215, 500, 437, 536]]<|/det|>
\[R \cdot I + L \cdot \dot{I} + \frac{Q}{C} = U_a(t)\]

<|ref|>equation<|/ref|><|det|>[[171, 540, 435, 575]]<|/det|>
\[R \cdot \dot{Q} + L \cdot \ddot{Q} + \frac{1}{C} \cdot Q = U_a(t)\]

<|ref|>equation<|/ref|><|det|>[[120, 581, 437, 600]]<|/det|>
\[R \cdot C \cdot \dot{U}_C + L \cdot C \cdot \ddot{U}_C + U_C = U_a(t)\]

<|ref|>text<|/ref|><|det|>[[115, 599, 465, 617]]<|/det|>
Es ergibt sich die folgende DGL für \(U_C\): 

<|ref|>equation<|/ref|><|det|>[[115, 615, 451, 653]]<|/det|>
\[\ddot{U}_C + \frac{R}{L} \cdot \dot{U}_C + \frac{1}{LC} \cdot U_C = \frac{1}{LC} \cdot U_a(t)\]

<|ref|>text<|/ref|><|det|>[[115, 655, 144, 671]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[115, 670, 770, 722]]<|/det|>
Durch Vergleich der vorliegenden DGL mit einer allgemeinen DGL für die erzwungene gedämpfte Schwingung ergibt sich die Kreisfrequenz für die ungedämpfte Schwingung 

<|ref|>equation<|/ref|><|det|>[[115, 719, 571, 757]]<|/det|>
\[\frac{\omega_0}{\sqrt{LC}} \approx \frac{1}{\sqrt{1.80 \cdot 10^{-2} \text{ H} \cdot 1.41 \cdot 10^{-4} \text{ F}}} \approx 628 \frac{1}{s}\]

<|ref|>text<|/ref|><|det|>[[115, 757, 415, 775]]<|/det|>
und für die Dämpfungskonstante 

<|ref|>equation<|/ref|><|det|>[[115, 774, 433, 811]]<|/det|>
\[\delta = \frac{R}{2L} \approx \frac{10.0 \Omega}{2 \cdot 1.80 \cdot 10^{-2} \text{ H}} \approx 278 \frac{1}{s}.\]

<|ref|>text<|/ref|><|det|>[[115, 813, 525, 832]]<|/det|>
Da \(\delta < \omega_0\) gilt, liegt schwache Dämpfung vor. 

<|ref|>text<|/ref|><|det|>[[115, 831, 144, 847]]<|/det|>
c) 

<|ref|>text<|/ref|><|det|>[[115, 846, 655, 864]]<|/det|>
Für die Frequenz der ungedämpften Schwingung ergibt sich 

<|ref|>equation<|/ref|><|det|>[[115, 862, 755, 900]]<|/det|>
\[\frac{\nu_0}{2\pi} = \frac{1}{2\pi} \cdot \omega_0 = \frac{1}{2\pi} \cdot \frac{1}{\sqrt{LC}} \approx \frac{1}{2\pi} \cdot \frac{1}{\sqrt{1.80 \cdot 10^{-2} \text{H} \cdot 1.41 \cdot 10^{-4} \text{F}}} \approx 99.9 \text{ Hz},\]

<|ref|>text<|/ref|><|det|>[[115, 902, 490, 920]]<|/det|>
für die gedämpfte Schwingung ergibt sich