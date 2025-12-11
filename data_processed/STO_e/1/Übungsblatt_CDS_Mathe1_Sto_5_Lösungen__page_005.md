<|ref|>text<|/ref|><|det|>[[114, 81, 850, 166]]<|/det|>
30% auf die Monitore und 50% auf die Drucker (die Anteile sind als
Wahrscheinlichkeiten interpretierbar). Aus Erfahrung wissen Sie, dass von den
verkauften PCs 20 %, von den verkauften Monitoren 10% und den abgesetzten
Druckern 15% reklamiert werden. Wie gross ist die Wahrscheinlichkeit dafür, dass
ein verkauftes Produkt reklamiert wird? 

<|ref|>text<|/ref|><|det|>[[117, 180, 330, 199]]<|/det|>
Definition der Ereignisse: 

<|ref|>equation<|/ref|><|det|>[[212, 204, 425, 223]]<|/det|>
\[A_1 = "Verkauf eines PCs"\]

<|ref|>equation<|/ref|><|det|>[[212, 227, 465, 246]]<|/det|>
\[A_2 = "Verkauf eines Monitors"\]

<|ref|>equation<|/ref|><|det|>[[212, 250, 465, 269]]<|/det|>
\[A_3 = "Verkauf eines Druckers"\]

<|ref|>equation<|/ref|><|det|>[[212, 272, 525, 291]]<|/det|>
\[B = "Verkauftes Gerät wird reklamiert"\]

<|ref|>text<|/ref|><|det|>[[117, 300, 771, 334]]<|/det|>
Gegeben sind die einfachen Wahrscheinlichkeiten, dass die einzelnen Produkte verkauft werden: 

<|ref|>equation<|/ref|><|det|>[[212, 338, 511, 359]]<|/det|>
\[P(A_1) = 0,2; P(A_2) = 0,3; P(A_3) = 0,5.\]

<|ref|>text<|/ref|><|det|>[[117, 364, 771, 433]]<|/det|>
Zusätzlich sind die Anteile der Reklamationen bei den einzelnen Produkten gegeben. Von den verkauften PCs (B unter der Bedingung, dass \(A_1\) bereits eingetreten ist) beträgt die Wahrscheinlichkeit einer Reklamation \(P(B|A_1) = 0,20\). Alle bedingten Wahrscheinlichkeiten lauten: 

<|ref|>equation<|/ref|><|det|>[[212, 437, 580, 458]]<|/det|>
\[P(B|A_1) = 0,20; P(B|A_2) = 0,10; P(B|A_3) = 0,15.\]

<|ref|>text<|/ref|><|det|>[[117, 462, 770, 497]]<|/det|>
Die Voraussetzungen für die Anwendung des Satzes der totalen Wahrscheinlichkeit sind erfüllt, 

<|ref|>text<|/ref|><|det|>[[127, 503, 770, 539]]<|/det|>
- \(A_1 \cup A_2 \cup A_3 = \Omega\) [nur die drei Produkte werden vertrieben \((P(A_1) + P(A_2) + P(A_3) = 0,2 + 0,3 + 0,5 = 1)\)] 

<|ref|>text<|/ref|><|det|>[[127, 541, 770, 576]]<|/det|>
- \(A_j \cap A_k = \emptyset\) für \(j \neq k; j, k = 1,2,3\) (ein Produkt ist nicht gleichzeitig PC und Monitor bzw. PC und Drucker bzw. Monitor und Drucker), 

<|ref|>text<|/ref|><|det|>[[117, 585, 370, 603]]<|/det|>
erhält man folgendes Ergebnis: 

<|ref|>equation<|/ref|><|det|>[[212, 610, 670, 703]]<|/det|>
\[ 
\begin{align*} 
P(B) &= \sum_{j=1}^{3} P(B|A_j) \cdot P(A_j) \\
&= P(B|A_1) \cdot P(A_1) + P(B|A_2) \cdot P(A_2) + P(B|A_3) \cdot P(A_3) \\
&= 0,2 \cdot 0,2 + 0,10 \cdot 0,3 + 0,15 \cdot 0,5 = 0,145 \quad [\text{= 14,5\%}]. 
\end{align*} 
\]

<|ref|>sub_title<|/ref|><|det|>[[117, 721, 283, 739]]<|/det|>
## 6. Bogenschütze 

<|ref|>text<|/ref|><|det|>[[117, 737, 844, 789]]<|/det|>
Ein Bogenschütze trifft mit einer Wahrscheinlichkeit von \(p = 0,3\) ins „Schwarze“ (= Zentrum der Zielscheibe). Bestimmen Sie bei drei abgegebenen Schüssen die Wahrscheinlichkeiten der folgenden Ereignisse (Resultate): 

<|ref|>text<|/ref|><|det|>[[117, 787, 234, 805]]<|/det|>
a) 3 Treffer, 

<|ref|>text<|/ref|><|det|>[[117, 804, 234, 822]]<|/det|>
b) 2 Treffer, 

<|ref|>text<|/ref|><|det|>[[117, 821, 340, 839]]<|/det|>
c) mindestens 2 Treffer. 

<|ref|>text<|/ref|><|det|>[[117, 837, 870, 872]]<|/det|>
d) Wie oft muss er mindestens schiessen, um mit einer Wahrscheinlichkeit von 90% wenigstens einmal zu treffen?