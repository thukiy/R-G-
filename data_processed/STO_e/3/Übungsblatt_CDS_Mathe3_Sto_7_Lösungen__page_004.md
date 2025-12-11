<|ref|>text<|/ref|><|det|>[[144, 81, 863, 118]]<|/det|>
ii) mit Hilfe des Grenzwertsatzes von De Moivre-Laplace (Annäherung Binomialdurch Normalverteilung). 

<|ref|>text<|/ref|><|det|>[[115, 116, 150, 133]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[115, 131, 740, 150]]<|/det|>
\(X_n\) ist binomialverteilt mit den Parametern \(p = 0,5\) und \(n\). Daher ist der 

<|ref|>text<|/ref|><|det|>[[115, 147, 715, 177]]<|/det|>
Erwartungswert \(E\left(\frac{1}{n} \cdot X_n\right) = 0,5\) und die Varianz \(Var\left(\frac{1}{n} \cdot X_n\right) = \frac{0,25}{n}\). 

<|ref|>text<|/ref|><|det|>[[115, 174, 585, 194]]<|/det|>
Verwendung der Tschebyscheff Ungleichung ergibt: 

<|ref|>equation<|/ref|><|det|>[[115, 191, 420, 220]]<|/det|>
\[P\left(\left|\frac{1}{n} \cdot X_n - 0,5\right| \geq \varepsilon\right) \leq \frac{0,25}{n \cdot \varepsilon^2} \xrightarrow[n \to \infty]{} 0.\]

<|ref|>text<|/ref|><|det|>[[115, 217, 830, 252]]<|/det|>
D. h. die relative Häufigkeit des Auftretens eines Zahlwurfs in einer Reihe von n Würfen konvergiert im angegebenen Sinne gegen die (klassische) 

<|ref|>text<|/ref|><|det|>[[115, 250, 844, 285]]<|/det|>
Wahrscheinlichkeit für das Eintreten eines Zahlwurfes. Dies ist ein Spezialfall des (schwachen) Gesetzes der grossen Zahlen. 

<|ref|>text<|/ref|><|det|>[[115, 284, 150, 301]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[115, 298, 399, 317]]<|/det|>
(i) Tschebyscheff Ungleichung: 

<|ref|>equation<|/ref|><|det|>[[115, 314, 808, 355]]<|/det|>
\[P(0,49 \cdot n < X_n < 0,51 \cdot n) = 1 - P\left(\left|\frac{X_n}{n} - 0,5\right| \leq 0,01\right) \geq 1 - \frac{0,25}{n \cdot 0,01^2} \geq 0,8 \text{ ergibt } n \geq 12500.\]

<|ref|>text<|/ref|><|det|>[[115, 358, 797, 392]]<|/det|>
(ii) Grenzwertsatz von De Moivre-Laplace bzw. Annäherung Binomial- durch Normalverteilung 

<|ref|>equation<|/ref|><|det|>[[115, 390, 692, 425]]<|/det|>
\[P(0,49 \cdot n < X_n < 0,5 \cdot n) = P\left(-0,02 \cdot \sqrt{n} < \frac{X_n - 0,5n}{\sqrt{0,25n}} < 0,02 \cdot \sqrt{n}\right)\]

<|ref|>equation<|/ref|><|det|>[[115, 419, 323, 439]]<|/det|>
\[\approx 2 \cdot \Phi(0,02 \cdot \sqrt{n}) - 1\]

<|ref|>text<|/ref|><|det|>[[115, 439, 579, 459]]<|/det|>
Aus \(2 \cdot \Phi(0,02 \cdot \sqrt{n}) - 1 \geq 0,8\) erhält man \(n \geq 4109\). 

<|ref|>sub_title<|/ref|><|det|>[[115, 474, 286, 492]]<|/det|>
## 6. Fahrradverleih 

<|ref|>text<|/ref|><|det|>[[115, 491, 867, 575]]<|/det|>
In einem Fahrradverleih stehen 100 Fahrräder zur Verfügung. Erfahrungsgemäss ist jedes Fahrrad wahrend 80 % der Öffnungszeit verliehen. Unter der Voraussetzung, dass die einzelnen Fahrräder unabhängig voneinander entliehen werden, berechne man näherungsweise die Wahrscheinlichkeit dafür, dass zu einem bestimmten Zeitpunkt 

<|ref|>text<|/ref|><|det|>[[115, 574, 293, 592]]<|/det|>
a) höchstens 90%, 

<|ref|>text<|/ref|><|det|>[[115, 590, 280, 608]]<|/det|>
b) mehr als 90%, 

<|ref|>text<|/ref|><|det|>[[115, 607, 348, 624]]<|/det|>
c) zwischen 70 und 90% 

<|ref|>text<|/ref|><|det|>[[115, 623, 345, 640]]<|/det|>
der Räder verliehen sind. 

<|ref|>text<|/ref|><|det|>[[115, 656, 790, 674]]<|/det|>
Die diskrete und binomialverteilte Zufallsvariable X: Anzahl der entliehenen 

<|ref|>text<|/ref|><|det|>[[115, 672, 754, 690]]<|/det|>
Fahrräder kann gemäss dem Grenzwertsatz von De Moivre-Laplace als 

<|ref|>text<|/ref|><|det|>[[115, 688, 872, 723]]<|/det|>
näherungsweise normalverteilt mit den Parametern \(\mu = 100 \cdot 0,8 = 80\) Fahrräder und \(\sigma^2 = 100 \cdot 0,8 \cdot (1 - 0,8) = 16\) angenommen werden. Es ergibt sich: 

<|ref|>equation<|/ref|><|det|>[[115, 721, 400, 740]]<|/det|>
a) \(P(X \leq 90) = \Phi(2,5) = 0,9938\)

<|ref|>equation<|/ref|><|det|>[[115, 738, 443, 757]]<|/det|>
b) \(P(X > 90) = 1 - \Phi(2,5) = 0,0062\)

<|ref|>equation<|/ref|><|det|>[[115, 755, 551, 775]]<|/det|>
c) \(P(70 \leq X \leq 90) = \Phi(2,5) - \Phi(-2,5) = 0,9876\)