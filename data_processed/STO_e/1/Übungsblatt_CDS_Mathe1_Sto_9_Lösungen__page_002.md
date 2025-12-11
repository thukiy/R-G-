<|ref|>sub_title<|/ref|><|det|>[[114, 81, 330, 100]]<|/det|>
## 2. Poisson-Verteilung 

<|ref|>text<|/ref|><|det|>[[114, 99, 833, 135]]<|/det|>
X sei eine Poisson-verteilte Zufallsvariable mit dem Parameter \(\lambda = 3\). Berechnen Sie die folgenden Wahrscheinlichkeiten: 

<|ref|>text<|/ref|><|det|>[[114, 133, 565, 153]]<|/det|>
a) \(P(X = 0)\) b) \(P(X \le 3)\) c) \(P(X > 3)\) d) \(P(1 \le X \le 5)\). 

<|ref|>equation<|/ref|><|det|>[[123, 168, 585, 204]]<|/det|>
\[P(X = x) = f(x) = \frac{3^x}{x!} \cdot e^{-3} \quad (x = 0, 1, 2, \dots)\]

<|ref|>text<|/ref|><|det|>[[123, 209, 425, 228]]<|/det|>
a) \(P(X = 0) = f(0) = 0,0498\) 

<|ref|>text<|/ref|><|det|>[[123, 236, 629, 257]]<|/det|>
b) \(P(X \le 3) = f(0) + f(1) + f(2) + f(3) = 0,6472\) 

<|ref|>text<|/ref|><|det|>[[123, 265, 647, 285]]<|/det|>
c) \(P(X > 3) = 1 - P(X \le 3) = 1 - 0,6472 = 0,3528\) 

<|ref|>text<|/ref|><|det|>[[123, 293, 740, 314]]<|/det|>
d) \(P(1 \le X \le 5) = f(1) + f(2) + f(3) + f(4) + f(5) = 0,8663\) 

<|ref|>sub_title<|/ref|><|det|>[[114, 331, 198, 348]]<|/det|>
## 3. Stifte 

<|ref|>text<|/ref|><|det|>[[114, 348, 860, 384]]<|/det|>
Unter 40 Packungen, die laut Aufschrift je 10 Stifte enthalten sollen, befinden sich 4 unvollständige Packungen (sie enthalten weniger Stifte als angegeben). 

<|ref|>text<|/ref|><|det|>[[114, 382, 844, 433]]<|/det|>
a) Welche Wahrscheinlichkeitsverteilung liegt vor, wenn es darum geht, wie viele unvollständige Packungen man beim Kauf einer oder mehrerer Packungen erhält? 

<|ref|>text<|/ref|><|det|>[[114, 430, 541, 449]]<|/det|>
Wie gross ist die Wahrscheinlichkeit, dass man 

<|ref|>text<|/ref|><|det|>[[114, 447, 654, 466]]<|/det|>
b) beim Kauf von einer Packung eine vollständige Packung 

<|ref|>text<|/ref|><|det|>[[114, 464, 825, 483]]<|/det|>
c) beim Kauf von 10 Packungen genau zwei unvollständige Packungen erhält? 

<|ref|>text<|/ref|><|det|>[[114, 497, 144, 514]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[117, 513, 872, 549]]<|/det|>
Die Zufallsvariable \(X\) (= Anzahl der unvollständigen Packungen unter \(n\) gekauften Packungen) ist **hypergeometrisch** verteilt (\(N = 40\); \(M = \text{Anzahl der unvollständigen Packungen} = 4\)): 

<|ref|>text<|/ref|><|det|>[[114, 548, 144, 566]]<|/det|>
b) 

<|ref|>equation<|/ref|><|det|>[[120, 565, 675, 641]]<|/det|>
\[N = 40, \quad M = 4, \quad n = 1; \quad P(X = x) = f(x) = \frac{\binom{4}{x} \binom{36}{1-x}}{\binom{40}{1}}\]

<|ref|>equation<|/ref|><|det|>[[120, 648, 629, 666]]<|/det|>
\[X = 0 \quad (\text{nur vollständige Packungen:}) \quad P(X = 0) = f(0) = 0,9\]

<|ref|>text<|/ref|><|det|>[[114, 666, 144, 684]]<|/det|>
c) 

<|ref|>equation<|/ref|><|det|>[[114, 686, 686, 764]]<|/det|>
\[N = 40, \quad M = 4, \quad n=10; \quad P(X = x) = f(x) = \frac{\binom{4}{\frac{4}{x}} \binom{36}{10-x}}{\binom{40}{10}}\]

<|ref|>sub_title<|/ref|><|det|>[[114, 785, 260, 801]]<|/det|>
## 4. Kernreaktor 

<|ref|>text<|/ref|><|det|>[[114, 801, 712, 819]]<|/det|>
Bei einem Kernreaktor werden an die Brennelemente extrem hohe 

<|ref|>text<|/ref|><|det|>[[114, 817, 752, 835]]<|/det|>
Qualitätsanforderungen gestellt. Die Wahrscheinlichkeit dafür, dass ein 

<|ref|>text<|/ref|><|det|>[[114, 833, 880, 886]]<|/det|>
Brennelement diesen hohen Anforderungen nicht genügt, betrage \(p = 10^{-4}\). Wie gross ist die Wahrscheinlichkeit, dass alle 1500 Brennelemente eines Reaktors die vorgeschriebenen Qualitätsbedingungen erfüllen?