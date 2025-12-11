<|ref|>text<|/ref|><|det|>[[115, 82, 144, 99]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[115, 98, 625, 116]]<|/det|>
Zufallsvariable X: Anzahl der kurzfristigen Stornierungen 

<|ref|>text<|/ref|><|det|>[[115, 115, 541, 133]]<|/det|>
X ist binominalverteilt mit \(\Theta = 0,05\) und \(n = 10\). 

<|ref|>equation<|/ref|><|det|>[[122, 134, 639, 212]]<|/det|>
\[f_B(x | n; \Theta) = \begin{cases} \left( \frac{n}{x} \right) \cdot \Theta^x \cdot (1 - \Theta)^{n-x} & \text{für } x = 0, 1, 2, \dots, n \\ 0 & \text{sonst} \end{cases}\]

<|ref|>text<|/ref|><|det|>[[115, 213, 861, 246]]<|/det|>
Das Risiko tritt ein, wenn keiner der Teilnehmer storniert, d. h. X nimmt den Wert 0 an. 

<|ref|>equation<|/ref|><|det|>[[122, 247, 495, 309]]<|/det|>
\[f_B(0 | 10; 0,05) = \begin{pmatrix} 10 \\ 0 \end{pmatrix} \cdot 0,05^0 \cdot (1 - 0,05)^{10} = 0,5987 \quad \text{bzw.} \quad 59,87\%\]

<|ref|>text<|/ref|><|det|>[[115, 308, 682, 326]]<|/det|>
Das Risiko, dass keine Buchung storniert wird, beträgt 59,87%. 

<|ref|>text<|/ref|><|det|>[[115, 325, 150, 342]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[115, 341, 861, 376]]<|/det|>
Der Unternehmer bleibt in der Gewinnzone, wenn höchstens \(10 - 8 = 2\) Buchungen storniert werden, d. h. \(X \le 2\). 

<|ref|>equation<|/ref|><|det|>[[122, 375, 642, 416]]<|/det|>
\[F_B(2|10; 0,05) = \sum_{a=0}^{2} \begin{pmatrix} 10 \\ a \end{pmatrix} \cdot 0,05^a \cdot (1 - 0,05)^{10-a} = 0,9885\]

<|ref|>text<|/ref|><|det|>[[115, 417, 827, 451]]<|/det|>
Mit \(100 - 98,85\% = 1,15\%\) wird der Unternehmer nach Ersatzreisenden suchen müssen, um keinen Verlust zu machen. 

<|ref|>text<|/ref|><|det|>[[115, 451, 147, 468]]<|/det|>
c) 

<|ref|>text<|/ref|><|det|>[[115, 467, 852, 501]]<|/det|>
Der Erwartungswert muss bestimmt werden. Für die Binomialverteilung gilt: \(E(X) = n^*\Theta = 10^*0,05 = 0,5\). 

<|ref|>sub_title<|/ref|><|det|>[[115, 517, 317, 534]]<|/det|>
## 6. Elektronikbauteile 

<|ref|>text<|/ref|><|det|>[[115, 533, 868, 666]]<|/det|>
Ein Produzent von Elektronikbauteilen liefert einem Kunden jeden Montag 3.800 Bauteile. Der Kunde nimmt Lieferungen mit einer Ausschussquote von 4% und höher nicht an. Die Qualitätskontrolle wird vom Lieferanten und Kunden gemeinsam durchgeführt. Der Prüfplan sieht die zufällige Entnahme ohne Zurücklegen von 180 Bauteilen vor. Sind davon höchstens 6 Bauteile Ausschuss (3,33%), dann wird die Lieferung angenommen, anderenfalls wird sie nicht angenommen. Wie gross ist das Risiko des Produzenten, dass eine Lieferung, in der nur 2% der Bauteile Ausschuss sein mögen, nicht angenommen wird? 

<|ref|>text<|/ref|><|det|>[[115, 681, 861, 750]]<|/det|>
Das Produzentenrisiko besteht darin, dass die Lieferung wegen des Auffindens von mehr als 6 Ausschuss-Bauteilen in der Stichprobe von 180 Bauteilen nicht angenommen wird, obwohl die Lieferung mit 2% bzw. 76 Ausschuss-Bauteilen deutlich unter 4% Ausschuss bzw. 152 Ausschuss-Bauteilen liegt. 

<|ref|>text<|/ref|><|det|>[[115, 749, 650, 766]]<|/det|>
Zufallsvariable X = Anzahl der Bauteile, die Ausschuss sind 

<|ref|>text<|/ref|><|det|>[[115, 765, 395, 782]]<|/det|>
X ist hypergeometrisch verteilt. 

<|ref|>text<|/ref|><|det|>[[115, 781, 598, 799]]<|/det|>
\(N = 3800\), \(M = 76\) (entspricht 2% Ausschuss), \(n = 180\) 

<|ref|>equation<|/ref|><|det|>[[115, 797, 590, 873]]<|/det|>
\[1 - F_H(6 | 3.800; 76; 180) = 1 - \sum_{a=0}^{6} \begin{pmatrix} 76 \\ a \end{pmatrix} \cdot \begin{pmatrix} 3800 - 76 \\ 180 - a \end{pmatrix}\]

<|ref|>text<|/ref|><|det|>[[115, 874, 843, 909]]<|/det|>
Die Wahrscheinlichkeit, dass eine Lieferung fälschlicherweise nicht angenommen wird, beträgt 6,65%.