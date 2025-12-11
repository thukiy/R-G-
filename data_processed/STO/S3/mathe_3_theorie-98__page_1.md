<|ref|>sub_title<|/ref|><|det|>[[25, 12, 880, 45]]<|/det|>
Wahrscheinlichkeitsverteilung von mehreren Zufallsvariablen 

<|ref|>text<|/ref|><|det|>[[25, 54, 470, 80]]<|/det|>
bisher: Beobachtung eines Meumals 

<|ref|>text<|/ref|><|det|>[[25, 92, 600, 118]]<|/det|>
jetzt: 2 oder mehrere Meumale von Interne 

<|ref|>text<|/ref|><|det|>[[20, 130, 884, 159]]<|/det|>
→ Meumale werden nicht nur einzeln überprüft, sondern es kann nach 

<|ref|>text<|/ref|><|det|>[[70, 170, 485, 196]]<|/det|>
Zusammenhängen geschaut werden 

<|ref|>sub_title<|/ref|><|det|>[[25, 223, 520, 252]]<|/det|>
2D-Wahrscheinlichkeitsverteilungen: 

<|ref|>text<|/ref|><|det|>[[60, 263, 386, 289]]<|/det|>
2D-Zufallsvariable (X, Y) 

<|ref|>text<|/ref|><|det|>[[25, 321, 465, 347]]<|/det|>
Verteilungsfunktion ergibt sich aus 

<|ref|>equation<|/ref|><|det|>[[60, 360, 370, 385]]<|/det|>
\[F(x, y) = P(X \le x, Y \le y)\]

<|ref|>text<|/ref|><|det|>[[25, 397, 440, 423]]<|/det|>
und hat folgende Eigenschaften 

<|ref|>text<|/ref|><|det|>[[25, 434, 460, 470]]<|/det|>
a) \(\lim_{x \to -\infty} F(x, y) = \lim_{y \to -\infty} F(x, y) = 0\) 

<|ref|>text<|/ref|><|det|>[[25, 491, 456, 527]]<|/det|>
b) \(\lim_{x \to \infty} F(x, y) = \lim_{y \to \infty} F(x, y) = 1\) 

<|ref|>text<|/ref|><|det|>[[25, 550, 435, 576]]<|/det|>
c) \(P(a_1 < X < a_2 ; b_1 < X < b_2)\) 

<|ref|>equation<|/ref|><|det|>[[60, 589, 640, 614]]<|/det|>
\[= F(a_1, b_1) + F(a_2, b_2) - F(a_1, b_2) - F(a_2, b_1)\]

<|ref|>equation<|/ref|><|det|>[[60, 627, 315, 653]]<|/det|>
\[a_1 < a_2 ; b_1 < b_2\]

<|ref|>sub_title<|/ref|><|det|>[[25, 700, 386, 729]]<|/det|>
diskrete 2D-Verteilung: 

<|ref|>text<|/ref|><|det|>[[60, 740, 546, 766]]<|/det|>
X und Y sind diskrete Zufallsvariablen 

<|ref|>text<|/ref|><|det|>[[60, 778, 808, 805]]<|/det|>
Beschreibung mittels normierter Wahrscheinlichkeitsfunktion 

<|ref|>equation<|/ref|><|det|>[[110, 815, 710, 880]]<|/det|>
\[f(x, y) = \begin{cases} p_{ik} & x = x_i, y = y_k \\ 0 & \text{Somst} \end{cases} \quad i = 1 \dots m \\ u = 1 \dots n\]

<|ref|>text<|/ref|><|det|>[[60, 910, 664, 947]]<|/det|>
Verteilungsfunktion \(F(x, y) = \sum_{x_i \le x} \sum_{y_k \le y} f(x_i, y_k)\)