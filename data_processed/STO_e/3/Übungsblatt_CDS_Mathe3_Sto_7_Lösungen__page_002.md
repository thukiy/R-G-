<|ref|>text<|/ref|><|det|>[[115, 80, 870, 135]]<|/det|>
b) Wie gross ist höchstens die Wahrscheinlichkeit, dass in eine Flasche weniger als 0,7 l abgefüllt werden, wenn die Verteilung der von der Abfüllanlage abgegebenen Menge symmetrisch ist? 

<|ref|>text<|/ref|><|det|>[[115, 150, 660, 190]]<|/det|>
1. Sei \(X\) die fragliche Weinmenge \(E(X) = 0.72\),
\(\sigma_X = 0.01\). Dann ist 

<|ref|>equation<|/ref|><|det|>[[120, 200, 688, 222]]<|/det|>
\[P(0.7 \le X \le 0.9) \ge P(0.7 \le X \le 0.74) = P(|X - 0.72| \le 0.02)\]

<|ref|>text<|/ref|><|det|>[[120, 231, 660, 286]]<|/det|>
Nach der Tschebyscheffschen Ungleichung gilt \(P(|X - E(X)| \le k \sigma_X) \ge 1 - \frac{1}{k^2}\). Setzen wir \(k \sigma_X = 0.02\), dann ist bei einem \(\sigma_X = 0.01\) der Faktor \(k = 2\). Also gilt 

<|ref|>equation<|/ref|><|det|>[[230, 295, 550, 331]]<|/det|>
\[P(|X - 0.72| \le 0.02) \ge 1 - \frac{1}{4} = \frac{3}{4}\]

<|ref|>text<|/ref|><|det|>[[120, 334, 686, 372]]<|/det|>
2. Die Verteilung von \(X\) ist symmetrisch um \(E(X) - 0.72\). Dann folgt: 

<|ref|>equation<|/ref|><|det|>[[123, 383, 682, 448]]<|/det|>
\[ 
\begin{align*} 
P(X < 0.7) &= P(X - 0.72 < -0.2) \\
&= P(X - 0.72 > 0.2) = \frac{1}{2} P(|X - 0.72| > 0.2) 
\end{align*} 
\]

<|ref|>text<|/ref|><|det|>[[120, 450, 686, 515]]<|/det|>
Für \(E(X) = 0.72\) und \(\sigma_X = 0.01\) sagt die Ungleichung von Tschebyscheff \(P(|X - 0.72| > 0.2) \le \frac{1}{4}\). Daher ist \(P(X < 0.7) \le \frac{1}{8}\). 

<|ref|>sub_title<|/ref|><|det|>[[115, 531, 352, 549]]<|/det|>
### 3. Kundschaft im Laden 

<|ref|>text<|/ref|><|det|>[[115, 547, 850, 619]]<|/det|>
Die Zeit zwischen den Ankünften zweier aufeinanderfolgender Kunden in einem Telekommunikationsladen seien unabhängig und identisch verteilt mit den Parametern \(\mu = 8\) Minuten und \(\sigma = 2\). Wie hoch ist die Wahrscheinlichkeit, dass es bis zur Ankunft des 55-ten Kunden mindestens 7,5 Stunden dauert? 

<|ref|>text<|/ref|><|det|>[[120, 634, 175, 651]]<|/det|>
Seien 

<|ref|>text<|/ref|><|det|>[[145, 665, 780, 703]]<|/det|>
\(X_i\): Zeitabstand (Zwischenankunftszeit) zwischen dem \((i-1)\)-ten und \(i\)-ten Kunden 

<|ref|>text<|/ref|><|det|>[[375, 717, 550, 736]]<|/det|>
\(t_i\): \(i\)-te Ankunftszeit 

<|ref|>text<|/ref|><|det|>[[115, 737, 520, 757]]<|/det|>
Wie in der Abbildung dargestellt, gilt für \(i \ge 1\): 

<|ref|>equation<|/ref|><|det|>[[120, 757, 300, 775]]<|/det|>
\[t_i = X_1 + X_2 + \cdots + X_i\]

<|ref|>image<|/ref|><|det|>[[239, 789, 760, 860]]<|/det|>