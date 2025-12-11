<|ref|>sub_title<|/ref|><|det|>[[114, 81, 303, 100]]<|/det|>
## 3. RLC-Schaltkreis 

<|ref|>text<|/ref|><|det|>[[114, 99, 866, 185]]<|/det|>
Gegeben sei ein RLC-Schaltkreis, der aus einem Widerstand \(R = 1,2 \, \Omega\), einer Induktivität \(L = 15 \, \text{mH}\) und einer Kapazität \(C = 168 \, \mu\text{F}\) bestehe. Der Kondensator werde durch eine externe Spannungsquelle auf eine Spannung von \(5 \, \text{V}\) aufgeladen. Anschliessend wird die Spannungsquelle entfernt und der Schalter S wird geschlossen. 

<|ref|>image<|/ref|><|det|>[[306, 197, 681, 302]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[114, 316, 837, 335]]<|/det|>
a) Stellen Sie das AWP für die Spannung \(U_C(t)\) auf, die am Kondensator anliegt. 

<|ref|>text<|/ref|><|det|>[[114, 333, 875, 369]]<|/det|>
b) Bestimmen Sie die ungedämpfte Kreisfrequenz und die Dämpfungskonstante des Systems. Welcher Fall liegt vor? 

<|ref|>text<|/ref|><|det|>[[114, 367, 550, 386]]<|/det|>
c) Mit welcher Frequenz schwingt das System? 

<|ref|>text<|/ref|><|det|>[[114, 400, 145, 418]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[114, 416, 414, 435]]<|/det|>
Mit der Maschenregel ergibt sich 

<|ref|>equation<|/ref|><|det|>[[232, 435, 404, 455]]<|/det|>
\[U_R + U_L + U_C = 0\]

<|ref|>equation<|/ref|><|det|>[[209, 464, 404, 500]]<|/det|>
\[R \cdot I + L \cdot \dot{I} + \frac{Q}{C} = 0\]

<|ref|>equation<|/ref|><|det|>[[168, 504, 404, 540]]<|/det|>
\[R \cdot \dot{Q} + L \cdot \ddot{Q} + \frac{1}{C} \cdot Q = 0\]

<|ref|>equation<|/ref|><|det|>[[114, 545, 404, 565]]<|/det|>
\[R \cdot C \cdot \dot{U}_C + L \cdot C \cdot \ddot{U}_C + U_C = 0\]

<|ref|>text<|/ref|><|det|>[[114, 565, 830, 584]]<|/det|>
Wir erhalten als DGL (2. Ordnung, homogen, konstante Koeffizienten, autonom) 

<|ref|>equation<|/ref|><|det|>[[114, 581, 368, 615]]<|/det|>
\[\ddot{U}_C + \frac{R}{L} \cdot \dot{U}_C + \frac{1}{LC} \cdot U_C = 0\]

<|ref|>text<|/ref|><|det|>[[114, 614, 777, 633]]<|/det|>
Wir wählen als Anfangszweitpunkt \(t_0 = 0\) und es ergeben sich somit als ABs 

<|ref|>equation<|/ref|><|det|>[[114, 632, 312, 653]]<|/det|>
\[U_C(0) = U_0 \approx 5.00 \, \text{V}\]

<|ref|>equation<|/ref|><|det|>[[114, 659, 495, 696]]<|/det|>
\[\dot{U}_C(0) = \frac{1}{C} \cdot \dot{Q}(0) = \frac{1}{C} \cdot I(0) = \frac{1}{C} \cdot 0 = 0.\]

<|ref|>text<|/ref|><|det|>[[114, 696, 456, 715]]<|/det|>
Das AWP sieht folgendermassen aus 

<|ref|>equation<|/ref|><|det|>[[114, 713, 360, 741]]<|/det|>
\[DGL: \ddot{U}_C + \frac{R}{L} \dot{U}_C + \frac{1}{LC} U_C = 0\]

<|ref|>equation<|/ref|><|det|>[[114, 738, 255, 758]]<|/det|>
\[AB: U_C(0) = U_0\]

<|ref|>equation<|/ref|><|det|>[[159, 755, 250, 775]]<|/det|>
\[\dot{U}_C(0) = 0\]

<|ref|>text<|/ref|><|det|>[[114, 774, 145, 791]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[114, 789, 789, 825]]<|/det|>
Vergleich der DGL aus a) mit der DGL für die freie gedämpfte harmonische Schwingung liefert 

<|ref|>equation<|/ref|><|det|>[[114, 822, 327, 844]]<|/det|>
\[\ddot{U}_C + 2\delta\dot{U}_C + \omega_0^2 U_C = 0.\]

<|ref|>text<|/ref|><|det|>[[114, 841, 530, 860]]<|/det|>
Die ungedämpfte Kreisfrequenz ergibt sich zu 

<|ref|>equation<|/ref|><|det|>[[114, 858, 540, 893]]<|/det|>
\[\frac{\omega_0}{\sqrt{LC}} \approx \frac{1}{\sqrt{1.50 \cdot 10^{-2} \, \text{H} \cdot 1.68 \cdot 10^{-4} \, \text{F}}} \approx \frac{629}{\text{s}},\]

<|ref|>text<|/ref|><|det|>[[114, 895, 371, 914]]<|/det|>
die Dämpfungskonstante zu