<|ref|>text<|/ref|><|det|>[[140, 80, 875, 123]]<|/det|>
Die Wahrscheinlichkeiten für die Ereignisse \(A\) und \(B\) sind bereits bekannt: \(P(A) = 0,2\) und \(P(B) = 0,4\). Die Wahrscheinlichkeit für das Ereignis \(A \cap B\) (beide Schützen treffen gleichzeitig) erhalten wir aus dem *Multiplikationssatz* für stochastisch unabhängige Ereignisse 

<|ref|>equation<|/ref|><|det|>[[164, 127, 476, 144]]<|/det|>
\[P(A \cap B) = P(A) \cdot P(B) = 0,2 \cdot 0,4 = 0,08\]

<|ref|>text<|/ref|><|det|>[[140, 151, 875, 179]]<|/det|>
(das Ergebnis des einen Schützen hat *keinen* Einfluss auf das Ergebnis des anderen Schützen). Die Scheibe wird somit mit der folgenden Wahrscheinlichkeit getroffen: 

<|ref|>equation<|/ref|><|det|>[[164, 185, 688, 201]]<|/det|>
\[P(A \cup B) = P(A) + P(B) - P(A \cap B) = 0,2 + 0,4 - 0,08 = 0,52 \cong 52\%\]

<|ref|>text<|/ref|><|det|>[[120, 208, 390, 223]]<|/det|>
b) Uns interessiert das folgende Ereignis: 

<|ref|>text<|/ref|><|det|>[[164, 227, 420, 243]]<|/det|>
C: Nur einer der beiden Schützen trifft 

<|ref|>text<|/ref|><|det|>[[140, 247, 875, 276]]<|/det|>
D. h. *entweder* trifft der 1. Schütze und der 2. Schütze trifft nicht (Ereignis \((A \cap \bar{B})\) oder umgekehrt der 2. Schütze trifft und der 1. Schütze trifft nicht (Ereignis \((B \cap \bar{A})\)). Somit lässt sich das Ereignis \(C\) wie folgt beschreiben: 

<|ref|>equation<|/ref|><|det|>[[140, 278, 323, 295]]<|/det|>
\[C = (A \cap \bar{B}) \cup (B \cap \bar{A})\]

<|ref|>text<|/ref|><|det|>[[117, 303, 870, 332]]<|/det|>
Die Wahrscheinlichkeit, dass nur *einer* der beiden Schützen trifft, beträgt dann nach dem *Additionssatz* (die Ereignisse \(A \cap \bar{B}\) und \(B \cap \bar{A}\) schließen sich gegenseitig aus): 

<|ref|>equation<|/ref|><|det|>[[140, 338, 770, 377]]<|/det|>
\[P(C) = P(A \cap \bar{B}) + P(B \cap \bar{A}) = P(A) \cdot P(\bar{B}) + P(B) \cdot P(\bar{A}) = 0,2 \cdot 0,6 + 0,4 \cdot 0,8 = \\ = 0,12 + 0,32 = 0,44 \cong 44\%\]

<|ref|>equation<|/ref|><|det|>[[140, 384, 688, 403]]<|/det|>
\[(P(\bar{A}) = 1 - P(A) = 1 - 0,2 = 0,8; \quad P(\bar{B}) = 1 - P(B) = 1 - 0,4 = 0,6)\]

<|ref|>sub_title<|/ref|><|det|>[[117, 421, 333, 440]]<|/det|>
## 3. Einmaliges Würfeln 

<|ref|>text<|/ref|><|det|>[[117, 439, 861, 491]]<|/det|>
Betrachten Sie einmaliges Würfeln eines idealen Würfels und die beiden Ereignisse A (eine 2 wird gewürfelt) und B (eine gerade Zahl wird gewürfelt). Sind die beiden Ereignisse unabhängig voneinander? 

<|ref|>text<|/ref|><|det|>[[120, 504, 780, 523]]<|/det|>
Zur Lösung sind die folgenden Ereignisse und Wahrscheinlichkeiten festzulegen: 

<|ref|>equation<|/ref|><|det|>[[397, 536, 512, 555]]<|/det|>
\[A \cap B = \{2\}\]

<|ref|>equation<|/ref|><|det|>[[390, 568, 525, 604]]<|/det|>
\[W(A \cap B) = \frac{1}{6}\]

<|ref|>equation<|/ref|><|det|>[[405, 616, 504, 653]]<|/det|>
\[W(A) = \frac{1}{6}\]

<|ref|>equation<|/ref|><|det|>[[390, 663, 525, 700]]<|/det|>
\[W(B) = \frac{3}{6} = \frac{1}{2}\]

<|ref|>text<|/ref|><|det|>[[120, 713, 201, 731]]<|/det|>
Weil gilt 

<|ref|>equation<|/ref|><|det|>[[256, 743, 655, 782]]<|/det|>
\[W(A \cap B) = \frac{1}{6} \neq W(A)W(B) = \left(\frac{1}{6}\right)\left(\frac{1}{2}\right) = \frac{1}{12}\]

<|ref|>text<|/ref|><|det|>[[120, 794, 654, 812]]<|/det|>
sind die Ereignisse A und B (stochastisch) abhängig voneinander. 

<|ref|>sub_title<|/ref|><|det|>[[117, 829, 241, 847]]<|/det|>
## 4. Münzwurf 

<|ref|>text<|/ref|><|det|>[[117, 846, 861, 914]]<|/det|>
Zwei Münzen werden einmal geworfen. Für jede kann entweder Kopf oder Zahl eintreten. Als Ergebnismenge ergibt sich somit \(\Omega = \{(K,K),(K,Z),(Z,K),(Z,Z)\}\). Jedes der 4 Ereignisse ist gleichwahrscheinlich und hat somit die Wahrscheinlichkeit 0,25. Es seien die folgenden Ereignisse definiert: