<|ref|>text<|/ref|><|det|>[[117, 81, 512, 100]]<|/det|>
Daraus folgt die Ankunftszeit des 55-ten Kunden als 

<|ref|>equation<|/ref|><|det|>[[320, 112, 523, 131]]<|/det|>
\[t_{55} = X_1 + X_2 + \dots + X_{55}\]

<|ref|>text<|/ref|><|det|>[[117, 141, 725, 176]]<|/det|>
Nach dem zentralen Grenzwertsatz der Wahrscheinlichkeitsrechnung gilt für
\(i \to \infty\) 

<|ref|>equation<|/ref|><|det|>[[266, 183, 945, 223]]<|/det|>
\[\frac{X_1 + X_2 + \dots + X_i - 8i}{2\sqrt{i}} \to Z \sim N(0,1) \quad (Anmerkung: N(0,1) ist die Standardnormalverteilung)\]

<|ref|>text<|/ref|><|det|>[[117, 234, 723, 250]]<|/det|>
Die Wahrscheinlichkeit, dass es bis zur Ankunft des 55-ten Kunden mindestens 

<|ref|>text<|/ref|><|det|>[[117, 250, 490, 267]]<|/det|>
7,5 Stunden = 450 Minuten dauert, ergibt sich aus 

<|ref|>equation<|/ref|><|det|>[[220, 277, 904, 350]]<|/det|>
\[ 
\begin{align*} 
W(t_{55} \ge 450) &= W(X_1 + X_2 + \dots + X_{55} \ge 450) \\
&= W\left(\frac{X_1 + X_2 + \dots + X_{55} - 8(55)}{2\sqrt{55}} \ge \frac{450 - 8(55)}{2\sqrt{55}}\right) \\
&= W\left(Z \ge \frac{450 - 8(55)}{2\sqrt{55}}\right) = W(Z \ge 0,6742) = 1 - W(Z < 0,6742) \\
&= 1 - \Phi(0,6742) \ge 1 - 0,7486 = 0,2514 
\end{align*} 
\]

<|ref|>text<|/ref|><|det|>[[639, 272, 905, 305]]<|/det|>
Anmerkung:
W kann durch P ersetzt werden 

<|ref|>sub_title<|/ref|><|det|>[[115, 420, 250, 438]]<|/det|>
## 4. Werkstück 

<|ref|>text<|/ref|><|det|>[[115, 437, 770, 474]]<|/det|>
Die Länge X eines Werkstücks habe den Erwartungswert 50 mm und die Standardabweichung 0,05 mm. Der Sollwert betrage ebenfalls 50 mm. 

<|ref|>text<|/ref|><|det|>[[115, 471, 850, 506]]<|/det|>
a) Schätzen Sie die Wahrscheinlichkeit dafür ab, dass die Länge des Werkstücks um 0,1 mm oder mehr vom Sollwert abweicht. 

<|ref|>text<|/ref|><|det|>[[115, 504, 857, 556]]<|/det|>
b) Man berechne die unter a) abgeschätzte Wahrscheinlichkeit unter der zusätzlichen Voraussetzung, dass X als normalverteilt angesehen werden kann und vergleiche diese mit dem obigen Resultat. 

<|ref|>text<|/ref|><|det|>[[115, 571, 145, 588]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[115, 586, 370, 605]]<|/det|>
\[ E(X) = 50 \text{ mm}, \sigma = 0,05 \text{ mm} \]

<|ref|>text<|/ref|><|det|>[[115, 603, 572, 622]]<|/det|>
Anwendung der Tschebyscheff-Ungleichung liefert 

<|ref|>equation<|/ref|><|det|>[[115, 620, 400, 639]]<|/det|>
\[ P(|X - 50mm| \ge 0,1mm) \le 0,25 \]

<|ref|>text<|/ref|><|det|>[[115, 637, 145, 655]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[115, 653, 430, 671]]<|/det|>
für eine normalverteilte Länge X ist 

<|ref|>equation<|/ref|><|det|>[[115, 669, 833, 705]]<|/det|>
\[ P(|X - 50mm| \ge 0,1mm ) = P(50mm + 0,1mm \le X) + P(X \le 50mm - 0,1mm) \approx 0,0455, \text{ d. h. die Abschätzung unter a) ist sehr grob} \]

<|ref|>sub_title<|/ref|><|det|>[[115, 720, 242, 737]]<|/det|>
## 5. Münzwurf 

<|ref|>text<|/ref|><|det|>[[115, 736, 831, 771]]<|/det|>
Eine ideale Münze wird n-mal geworfen. Es sei Xn die Anzahl der Zahlwürfe, die dabei auftreten. 

<|ref|>text<|/ref|><|det|>[[115, 768, 857, 805]]<|/det|>
a) Überzeugen Sie sich mit Hilfe der Ungleichung von Tschebyscheff davon, dass für eine beliebige positive Zahl ε die Folge der Wahrscheinlichkeiten 

<|ref|>equation<|/ref|><|det|>[[144, 802, 866, 844]]<|/det|>
\[ P\left(\left|\frac{1}{n} \cdot X_n - 0,5\right| \ge \varepsilon\right) \text{ mit wachsendem n gegen Null konvergiert. Erläutern Sie die Bedeutung dieser Aussage.} \]

<|ref|>text<|/ref|><|det|>[[115, 843, 845, 896]]<|/det|>
b) Bestimmen Sie die notwendige Zahl n der Münzwurfe, damit Xn mit einer Wahrscheinlichkeit von wenigstens 0,8 in den Grenzen \(0,49 \cdot n < X_n < 0,51 \cdot n\) liegt 

<|ref|>text<|/ref|><|det|>[[144, 894, 571, 913]]<|/det|>
i) mit Hilfe der Ungleichung von Tschebyscheff,