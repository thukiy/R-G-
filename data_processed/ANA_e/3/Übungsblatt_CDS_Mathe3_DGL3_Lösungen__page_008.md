<|ref|>sub_title<|/ref|><|det|>[[114, 81, 559, 100]]<|/det|>
## 4. RC-Schaltkreis mit Gleichspannungsquelle 

<|ref|>text<|/ref|><|det|>[[114, 99, 866, 151]]<|/det|>
Gegeben ist der unten abgebildete RC-Schaltkreis mit Widerstand \(R = 4 \, \Omega\), einer zu Beginn vollständig entladenen Kapazität \(C = 15 \, \text{mF}\) und einer Gleichspannungsquelle mit \(U = 12 \, \text{V}\). 

<|ref|>image<|/ref|><|det|>[[130, 153, 520, 323]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[114, 323, 844, 376]]<|/det|>
a) Stellen Sie die DGL und Anfangsbedingung (also das AWP) für die Spannung \(U_C(t)\) auf, die an der Kapazität \(C\) anliegt, und zwar ab dem Zeitpunkt, wenn der Schalter S geschlossen wird. 

<|ref|>text<|/ref|><|det|>[[114, 373, 857, 425]]<|/det|>
b) Klassifizieren Sie die DGL, bestimmen Sie die statischen Lösungen und plotten Sie das Richtungsvektorfeld mit Python/Numpy. Beurteilen Sie die Stabilität der statischen Lösungen. 

<|ref|>text<|/ref|><|det|>[[114, 422, 485, 441]]<|/det|>
c) Bestimmen Sie die Lösung des AWP. 

<|ref|>text<|/ref|><|det|>[[114, 457, 147, 474]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[114, 472, 872, 506]]<|/det|>
Für die Spannung \(U_C(t)\), die an der Kapazität anliegt, die Ladung \(Q(t)\), die in der Kapazität zur Zeit \(t\) gespeichert ist und den Strom \(I(t)\), der im Schaltkreis vorliegt, gilt: 

<|ref|>equation<|/ref|><|det|>[[114, 503, 295, 534]]<|/det|>
\[I(t) = \frac{dQ}{dt} = C \cdot \frac{dU_C}{dt}\]

<|ref|>text<|/ref|><|det|>[[114, 532, 790, 567]]<|/det|>
Der Schalter S werde zum Zeitpunkt \(t_0\) geschlossen. Solange der Schalter geschlossen ist, kann die Maschenregel nach Kirchhoff angewandt werden: 

<|ref|>equation<|/ref|><|det|>[[125, 565, 280, 588]]<|/det|>
\[U_R + U_C = U\]

<|ref|>equation<|/ref|><|det|>[[125, 590, 268, 614]]<|/det|>
\[R \cdot I + U_C = U\]

<|ref|>equation<|/ref|><|det|>[[125, 614, 339, 648]]<|/det|>
\[R \cdot C \cdot \frac{dU_C}{dt} + U_C = U\]

<|ref|>equation<|/ref|><|det|>[[125, 655, 351, 689]]<|/det|>
\[R \cdot C \cdot \frac{dU_C}{dt} = U - U_C\]

<|ref|>equation<|/ref|><|det|>[[125, 697, 353, 732]]<|/det|>
\[\frac{dU_C}{dt} = \frac{\Lambda}{RC} \cdot (U - U_C)\]

<|ref|>equation<|/ref|><|det|>[[125, 744, 696, 772]]<|/det|>
\[\text{so gilt ausserdem: } U_C(t_0) = 0, \text{ da die Eigenschaft } C \text{ zu}\]

<|ref|>equation<|/ref|><|det|>[[125, 772, 347, 797]]<|/det|>
Beginn entladen ist

<|ref|>equation<|/ref|><|det|>[[125, 800, 435, 826]]<|/det|>
\[\text{so liegt Pflegende AWP von:}\]

<|ref|>equation<|/ref|><|det|>[[125, 825, 468, 860]]<|/det|>
\[\frac{dU_C}{dt} = \frac{\Lambda}{RC} (U - U_C)\]

<|ref|>equation<|/ref|><|det|>[[125, 870, 451, 900]]<|/det|>
\[\text{Anfangspreis betragung: } U_C(t_0) = 0\]