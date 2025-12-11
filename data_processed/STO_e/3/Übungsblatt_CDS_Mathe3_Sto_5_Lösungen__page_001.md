<|ref|>title<|/ref|><|det|>[[115, 166, 465, 201]]<|/det|>
# Übungsblatt Sto 5 

<|ref|>text<|/ref|><|det|>[[574, 179, 880, 216]]<|/det|>
Computational and Data Science
BSc HS2024 

<|ref|>text<|/ref|><|det|>[[115, 233, 270, 261]]<|/det|>
## Lösungen 

<|ref|>text<|/ref|><|det|>[[752, 240, 880, 258]]<|/det|>
Mathematik 3 

<|ref|>text<|/ref|><|det|>[[115, 288, 210, 305]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 304, 808, 356]]<|/det|>
- Sie kennen den Zusammenhang zwischen der Binomialverteilung und der Standardnormalverteilung und können eine Binomialverteilung durch eine Standardnormalverteilung approximieren. 

<|ref|>text<|/ref|><|det|>[[115, 354, 840, 404]]<|/det|>
- Sie können die Wahrscheinlichkeitsfunktion, Erwartungswerte und Varianzen stochastisch unabhängiger 2-dimensionaler stetiger Zufallsvariabler aus ihren gegebenen Verteilungen bestimmen. 

<|ref|>text<|/ref|><|det|>[[115, 403, 785, 453]]<|/det|>
- Sie können aus der Dichtefunktion einer stetigen 2-dimensionalen Zufallsvariablen Erwartungswerte, Varianzen und Wahrscheinlichkeiten bestimmen. 

<|ref|>text<|/ref|><|det|>[[115, 451, 835, 486]]<|/det|>
- Sie können die stochastische Unabhängigkeit von 2-dimensionalen diskreten Zufallsvariablen überprüfen. 

<|ref|>sub_title<|/ref|><|det|>[[115, 517, 490, 535]]<|/det|>
### 1. Standardnormalverteilung - Quantile 

<|ref|>text<|/ref|><|det|>[[115, 533, 830, 568]]<|/det|>
Bestimmen Sie anhand der Tabelle für die Standardnormalverteilung die jeweils unbekannte Intervallgrenze (U: standardnormalverteilte Zufallsvariable): 

<|ref|>equation<|/ref|><|det|>[[115, 567, 784, 586]]<|/det|>
\[a) P(U \le a) = 0,321 \quad b) P(-0,22 \le U \le b) = 0,413 \quad c) P(U \ge a) = 0,8002\]

<|ref|>text<|/ref|><|det|>[[115, 601, 142, 618]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[125, 618, 710, 635]]<|/det|>
\[\phi(a) = 0,3210 < 0,5 \quad \Rightarrow \quad a < 0 \quad (\text{Wir setzen } a = -k \text{ mit } k > 0) \quad \Rightarrow\]

<|ref|>equation<|/ref|><|det|>[[125, 637, 640, 655]]<|/det|>
\[\phi(a) = \phi(-k) = 1 - \phi(k) = 0,3210 \quad \Rightarrow \quad \phi(k) = 0,6790 \quad \Rightarrow\]

<|ref|>equation<|/ref|><|det|>[[125, 656, 420, 673]]<|/det|>
\[k = 0,465 \quad \Rightarrow \quad a = -k = -0,465\]

<|ref|>text<|/ref|><|det|>[[115, 674, 142, 691]]<|/det|>
b) 

<|ref|>equation<|/ref|><|det|>[[125, 690, 707, 728]]<|/det|>
\[\phi(b) - \phi(-0,22) = \phi(b) - 1 + \phi(0,22) = \phi(b) - 1 + 0,5871 =\]

<|ref|>equation<|/ref|><|det|>[[185, 710, 707, 728]]<|/det|>
\[= \phi(b) - 0,4129 = 0,413 \quad \Rightarrow \quad \phi(b) = 0,8259 \quad \Rightarrow \quad b = 0,938\]

<|ref|>text<|/ref|><|det|>[[115, 731, 142, 748]]<|/det|>
c) 

<|ref|>equation<|/ref|><|det|>[[125, 747, 702, 765]]<|/det|>
\[P(U \ge a) = 1 - P(U \le a) = 1 - \phi(a) = 0,8002 \quad \Rightarrow\]

<|ref|>equation<|/ref|><|det|>[[125, 766, 704, 784]]<|/det|>
\[\phi(a) = 0,1998 < 0,5 \quad \Rightarrow \quad a < 0 \quad (\text{Wir setzen } a = -k \text{ mit } k > 0) \quad\]

<|ref|>equation<|/ref|><|det|>[[125, 785, 636, 803]]<|/det|>
\[\phi(a) = \phi(-k) = 1 - \phi(-k) = 0,1998 \quad \Rightarrow \quad \phi(-k) = 0,8002 \quad \Rightarrow\]

<|ref|>equation<|/ref|><|det|>[[115, 805, 412, 822]]<|/det|>
\[k = 0,842 \quad \Rightarrow \quad a = -k = -0,842\]