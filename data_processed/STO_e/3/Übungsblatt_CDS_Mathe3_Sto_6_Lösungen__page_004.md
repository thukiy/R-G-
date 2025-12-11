<|ref|>text<|/ref|><|det|>[[117, 83, 870, 142]]<|/det|>
Bei der Lösung der Aufgabe müssen wir Folgendes beachten: Wir haben 100 Bleche mit den Dicken \(X_1, X_2, \ldots, X_{100}\), die alle die *gleiche* Verteilung besitzen wie die Zufallsvariable \(X\): 

<|ref|>equation<|/ref|><|det|>[[168, 152, 483, 173]]<|/det|>
\[E(X_i) = E(X) = \mu_X = 0,6 \text{ mm}\]

<|ref|>equation<|/ref|><|det|>[[168, 182, 560, 207]]<|/det|>
\[\text{Var}(X_i) = \text{Var}(X) = \sigma_X^2 = (0,03 \text{ mm})^2\]

<|ref|>text<|/ref|><|det|>[[117, 218, 870, 276]]<|/det|>
\((i = 1, 2, \ldots, 100)\). Die Dicken der 99 Zwischenlagen beschreiben wir durch die Zufallsvariablen \(Y_1, Y_2, \ldots, Y_{99}\), die alle die *gleiche* Verteilung besitzen wie die Zufallsvariable \(Y\): 

<|ref|>equation<|/ref|><|det|>[[168, 287, 495, 308]]<|/det|>
\[E(Y_k) = E(Y) = \mu_Y = 0,05 \text{ mm}\]

<|ref|>equation<|/ref|><|det|>[[168, 316, 560, 342]]<|/det|>
\[\text{Var}(Y_k) = \text{Var}(Y) = \sigma_Y^2 = (0,01 \text{ mm})^2\]

<|ref|>text<|/ref|><|det|>[[117, 354, 870, 393]]<|/det|>
\((k = 1, 2, \ldots, 99)\). Die Dicke des Transformatorkerns ist somit eine *Summe* aus genau 199 *stochastisch unabhängigen* und *normalverteilten* Zufallsvariablen: 

<|ref|>equation<|/ref|><|det|>[[168, 404, 380, 453]]<|/det|>
\[Z = \sum_{i=1}^{100} X_i + \sum_{k=1}^{99} Y_k\]

<|ref|>text<|/ref|><|det|>[[117, 455, 632, 473]]<|/det|>
Die Zufallsvariable besitzt dann den folgenden Mittelwert: 

<|ref|>equation<|/ref|><|det|>[[120, 476, 690, 575]]<|/det|>
\[E(Z) = \sum_{i=1}^{100} E(X_i) + \sum_{k=1}^{99} E(Y_k) = 100 \cdot E(X) + 99 \cdot E(Y) = \\
= 100 \cdot \mu_X + 99 \cdot \mu_Y = 100 \cdot 0,6 \text{ mm} + 99 \cdot 0,05 \text{ mm} = \\
= (60 + 4,95) \text{ mm} = 64,95 \text{ mm}\]

<|ref|>text<|/ref|><|det|>[[117, 575, 820, 595]]<|/det|>
Die Varianz der Gesamtdicke \(Z\) beträgt nach dem Additionssatz für Varianzen: 

<|ref|>equation<|/ref|><|det|>[[163, 594, 808, 735]]<|/det|>
\[\begin{align*}
\sigma_Z^2 &= \text{Var}(Z) = \sum_{i=1}^{100} \text{Var}(X_i) + \sum_{k=1}^{99} \text{Var}(Y_k) = \\
&= 100 \cdot \text{Var}(X) + 99 \cdot \text{Var}(Y) = 100 \cdot \sigma_X^2 + 99 \cdot \sigma_Y^2 = \\
&= 100 \cdot (0,03 \text{ mm})^2 + 99 \cdot (0,01 \text{ mm})^2 = (0,09 + 0,0099) \text{ mm}^2 = \\
&= 0,0999 \text{ mm}^2
\end{align*}\]

<|ref|>text<|/ref|><|det|>[[117, 743, 777, 768]]<|/det|>
Die *Standardabweichung* beträgt somit \(\sigma_Z = \sqrt{0,0999 \text{ mm}^2} = 0,316 \text{ mm}\). 

<|ref|>text<|/ref|><|det|>[[117, 771, 833, 863]]<|/det|>
Da alle 199 unabhängigen Zufallsvariablen \(X_1, X_2, \ldots, X_{100}\), \(Y_1, Y_2, \ldots, Y_{99}\) *stochastisch unabhängig* und *normalverteilt* sind, trifft diese Eigenschaft auch auf die *Summe* \(Z\) zu. Daher gilt: Die Gesamtdicke \(Z\) des Transformatorkerns ist eine *normalverteilte* Zufallsvariable mit dem *Mittelwert* \(\mu_Z = 64,95 \text{ mm}\) und der *Standardabweichung* \(\sigma_Z = 0,316 \text{ mm}\)