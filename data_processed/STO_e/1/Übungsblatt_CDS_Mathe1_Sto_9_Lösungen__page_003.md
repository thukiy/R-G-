<|ref|>text<|/ref|><|det|>[[118, 85, 880, 151]]<|/det|>
Die Zufallsvariable \(X\) (= Anzahl der Brennelemente, die den Anforderungen nicht genügen) ist *binomialverteilt* mit den Parametern \(n = 1500\) und \(p = 10^{-4}\). Sie darf jedoch durch eine (rechnerisch bequemere) *Poisson-Verteilung* mit dem Parameter (Mittelwert) \(\mu = np = 0,15\) ersetzt werden: 

<|ref|>equation<|/ref|><|det|>[[118, 149, 737, 186]]<|/det|>
\[P(X = x) = f(x) = \frac{0,15^x}{x!} \cdot e^{-0,15} \quad \Rightarrow \quad P(X = 0) = f(0) = 0,8607\]

<|ref|>text<|/ref|><|det|>[[118, 190, 877, 210]]<|/det|>
Exakte Verteilung (Binomialverteilung mit \(n = 1500\), \(p = 0,0001\) und \(q = 1 - p = 0,9999\)): 

<|ref|>equation<|/ref|><|det|>[[118, 212, 825, 252]]<|/det|>
\[P(X = x) = f(x) = \binom{1500}{x} \cdot 0,0001^x \cdot 0,9999^{1500-x} \quad (x = 0, 1, 2, \dots, 1500)\]

<|ref|>equation<|/ref|><|det|>[[118, 255, 728, 275]]<|/det|>
\[P(X = 0) = f(0) = 0,8607 \quad (\text{in Übereinstimmung mit der Näherung})\]

<|ref|>sub_title<|/ref|><|det|>[[115, 290, 270, 308]]<|/det|>
## 5. Urnenmodell 

<|ref|>text<|/ref|><|det|>[[115, 307, 877, 377]]<|/det|>
Einer Urne mit 5 Kugeln, darunter 3 weissen und zwei schwarzen, entnehmen wir nacheinander zufällig und ohne Zurücklegen 2 Kugeln. Bestimmen Sie die Verteilung der Zufallsvariablen X = Anzahl der gezogenen weissen Kugeln und zeichnen Sie das zugehörige Stabdiagramm. 

<|ref|>text<|/ref|><|det|>[[118, 391, 875, 426]]<|/det|>
**Hypergeometrische Verteilung mit den Parametern \(N = 5\), \(M = 3\) (Anzahl der weißen Kugeln) und \(n = 2\):** 

<|ref|>equation<|/ref|><|det|>[[118, 428, 550, 610]]<|/det|>
\[P(X = x) = f(x) = \frac{\binom{3}{x} \binom{2}{2-x}}{\binom{5}{2}} = \frac{1}{10} \binom{3}{x} \binom{2}{2-x} \quad (x = 0, 1, 2)\]

<|ref|>image<|/ref|><|det|>[[118, 561, 415, 610]]<|/det|>
 

<|ref|>image<|/ref|><|det|>[[660, 442, 872, 631]]<|/det|>
 

<|ref|>sub_title<|/ref|><|det|>[[115, 645, 270, 663]]<|/det|>
## 6. Gabelstapler 

<|ref|>text<|/ref|><|det|>[[115, 661, 872, 780]]<|/det|>
Bei der Montage von Gabelstaplern in einem grossen Maschinenbaubetrieb arbeiten u.a. an einem Fliessband 80 angelernte Arbeitskräfte je Schicht. Die Wahrscheinlichkeit, wegen Krankheit zu fehlen, betragt für diese Arbeitskräfte 5%, wobei die Erkrankung der Arbeitskräfte als unabhängig voneinander angenommen wird. Sinkt die Zahl der Arbeiter am Fliessband in einer Schicht unter 70 Personen, so müssen zur Erhaltung des Arbeitsablaufes zusätzliche Arbeitskräfte eingestellt werden. Mit welcher Wahrscheinlichkeit ist das der Fall? 

<|ref|>text<|/ref|><|det|>[[118, 794, 872, 917]]<|/det|>
diskrete Zufallsgröße X: *Anzahl der Krankenfälle in einer Schicht* ist binomialverteilt mit den Parametern \(n = 80\) und \(p = 0,05\), da \(n \cdot p = 4 < 10\) und \(n = 80 > 1500 \cdot p = 75\) kann die Verteilung von X approximativ durch die POISSON-Verteilung mit \(\lambda = n \cdot p = 4\) dargestellt werden, die Eigenschaft einer POISSON-Verteilung \(E(X) = V(X)\) ist ebenfalls zumindest annähernd erfüllt, da \(E(X) = 4 \approx V(X) = 3,8\) gilt, zusätzliche Arbeitskräfte müssen eingestellt werden, wenn mehr als 10 Personen in einer Schicht erkranken, somit bestimmt man unter Anwendung der POISSON-Verteilung folgende Wahrscheinlichkeit: \(P(X > 10) = 1 - P(X \le 10) \approx 1 - 0,9972 = 0,0028\)