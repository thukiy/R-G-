<|ref|>sub_title<|/ref|><|det|>[[114, 81, 500, 101]]<|/det|>
## 6. RC-Schaltkreis mit Spannungsquelle 

<|ref|>text<|/ref|><|det|>[[114, 100, 866, 167]]<|/det|>
Ein RC-Schaltkreis bestehe aus einem Widerstand \(R = 4 \Omega\), einer Kapazität \(C = 15\) mF, die zu Beginn vollständig entladen sei, und einer Spannungsquelle, die ab dem Einschaltzeitpunkt \(t_0\) eine zeitabhängige Spannung \(U(t) = a(t - t_0)\) mit \(a = 12\) V/S liefert. 

<|ref|>image<|/ref|><|det|>[[319, 175, 690, 338]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[114, 339, 870, 376]]<|/det|>
a) Ermitteln Sie das AWP für die Spannung \(U_C(t)\) über der Kapazität ab Einschalten der Spannungsquelle. 

<|ref|>text<|/ref|><|det|>[[114, 373, 878, 425]]<|/det|>
b) Klassifizieren Sie die DGL, bestimmen Sie ihre statischen Lösungen, plotten Sie das Richtungsvektorfeld (z. B. mit Python/Numpy) und beurteilen Sie die Stabilität der statischen Lösungen. 

<|ref|>text<|/ref|><|det|>[[114, 422, 805, 457]]<|/det|>
c) Bestimmen Sie die Lösung das AWP. Wie gross kann der Strom maximal werden? 

<|ref|>text<|/ref|><|det|>[[114, 473, 144, 490]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[114, 488, 852, 524]]<|/det|>
Für die Spannung \(U_C(t)\) über der Kapazität, die Ladung \(Q(t)\) der Kapazität und den Strom \(I(t)\) im Schaltkreis gilt zu jeder Zeit 

<|ref|>equation<|/ref|><|det|>[[114, 521, 323, 542]]<|/det|>
\[I(t) = \dot{Q}(t) = C \cdot U_C(t).\]

<|ref|>text<|/ref|><|det|>[[114, 540, 851, 559]]<|/det|>
Ab dem Einschaltzeitpunkt \(t_0\) der Spannungsquelle gilt (Maschenregel anwenden): 

<|ref|>equation<|/ref|><|det|>[[303, 562, 448, 582]]<|/det|>
\[U_R + U_C = U(t)\]

<|ref|>equation<|/ref|><|det|>[[120, 587, 448, 608]]<|/det|>
\[\Leftrightarrow R \cdot I + U_C = U(t)\]

<|ref|>equation<|/ref|><|det|>[[120, 618, 448, 640]]<|/det|>
\[\Leftrightarrow R \cdot C \cdot \dot{U}_C + U_C = U(t)\]

<|ref|>equation<|/ref|><|det|>[[120, 656, 495, 677]]<|/det|>
\[\Leftrightarrow R \cdot C \cdot \dot{U}_C = U(t) - U_C\]

<|ref|>text<|/ref|><|det|>[[114, 677, 390, 696]]<|/det|>
Es ergibt sich daraus die DGL 

<|ref|>equation<|/ref|><|det|>[[120, 695, 533, 735]]<|/det|>
\[\dot{U}_C = \frac{U(t) - U_C}{R \cdot C} = -\frac{1}{R \cdot C} \cdot U_C + \frac{1}{R \cdot C} \cdot U(t)\]

<|ref|>text<|/ref|><|det|>[[114, 738, 794, 757]]<|/det|>
Zu Beginn, also bei \(t_0\), ist die Kapazität nicht geladen, d. h. es gilt: \(U_C(t_0) = 0\). 

<|ref|>text<|/ref|><|det|>[[114, 755, 480, 773]]<|/det|>
Es ergibt sich für \(U_C\) das folgende AWP: 

<|ref|>equation<|/ref|><|det|>[[114, 771, 373, 801]]<|/det|>
\[\text{DGL: } \dot{U}_C = -\frac{1}{RC} U_C + \frac{1}{RC} U(t)\]

<|ref|>text<|/ref|><|det|>[[114, 796, 255, 815]]<|/det|>
AB: \(U_C(t_0) = 0\) 

<|ref|>text<|/ref|><|det|>[[114, 813, 150, 831]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[114, 829, 852, 864]]<|/det|>
Die DGL ist 1. Ordnung, analytisch isolierbar und linear inhomogen mit konstanten Koeffizienten. Für die statischen Lösungen muss gelten: 

<|ref|>equation<|/ref|><|det|>[[122, 867, 606, 902]]<|/det|>
\[0 = -\frac{1}{R \cdot C} \cdot U_C + \frac{2}{R \cdot C} \cdot U(t) = -\frac{1}{R \cdot C} \cdot (U_C - U(t)).\]