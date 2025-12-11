<|ref|>text<|/ref|><|det|>[[120, 81, 621, 99]]<|/det|>
Variante 2: Wir wenden das GAUSS-JORDAN-Verfahren an. Es gilt 

<|ref|>equation<|/ref|><|det|>[[140, 103, 728, 163]]<|/det|>
\[ \begin{bmatrix} 3 & -2 & 1 & 2 & 4 \\ -1 & 3 & -1 & 1 & 1 \\ 2 & 1 & -3 & 0 & 5 \end{bmatrix} \Leftrightarrow \begin{bmatrix} -1 & 3 & -1 & 1 & 1 \\ 3 & -2 & 1 & 2 & 4 \\ 2 & 1 & -3 & 0 & 5 \end{bmatrix} + \begin{bmatrix} 1 & -3 & 1 & -1 & -1 \\ 3 & -2 & 1 & 2 & 4 \\ 2& 1 & -3 & 0 & 5 \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[140, 168, 830, 228]]<|/det|>
\[ \begin{bmatrix} 1 & -3 & 1 & -1 & -1 \\ \Leftrightarrow & 0 & [7] & -2 & 5 \\ 1 & 0 & 7 & -5 & 2 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & -3 & 1 & -1 & -1 \\ [7] & -2 & 5 & 7 \\ 0 & 0 & -3 & -3 & 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & -3 & 1 \\ 0 & [7] & -2 & 5 \\ 0 & 0 & [1] & 1 \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[140, 233, 780, 293]]<|/det|>
\[ \begin{bmatrix} 1 & -3 & 0 & -2 & -1 \\ \Leftrightarrow & 0 & [7] & 0 & 7 \\ 0 & 0 & [1] & 1 & 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & -3 \\ 0 & [1] & 0 & 1 & 1 \\ 0 & 0 & [1] & 1 & 0 \end{bmatrix}\]

<|ref|>text<|/ref|><|det|>[[120, 302, 812, 319]]<|/det|>
Die Lösungsmengen des Gleichungssystems für die erste und zweite rechte Seite sind demnach 

<|ref|>equation<|/ref|><|det|>[[300, 323, 631, 345]]<|/det|>
\[ \mathbb{L}_1 = \{(1; 1; 1)\} \quad \text{bzw.} \quad \mathbb{L}_2 = \{(2; 1; 0)\}. \]

<|ref|>title<|/ref|><|det|>[[115, 363, 350, 381]]<|/det|>
8. Planung von 2 Hotels 

<|ref|>text<|/ref|><|det|>[[115, 380, 875, 450]]<|/det|>
Es sollen 2 neue Hotels gebaut werden, in denen es jeweils Zweier- und Dreierzimmer geben soll. Das kleinere Hotel soll 21 Zimmer für 50 Gäste und das grössere 45 Zimmer für 100 Gäste zur Verfügung stellen. Aus wie vielen Zweier- und Dreierzimmern können die Hotels gebaut werden? 

<|ref|>text<|/ref|><|det|>[[120, 464, 562, 481]]<|/det|>
Variante 1: Wir wenden das GAUSS-Verfahren an. Es gilt 

<|ref|>equation<|/ref|><|det|>[[140, 485, 625, 530]]<|/det|>
\[ \begin{bmatrix} 1 & 1 & 21 & 45 \\ 2 & 3 & 50 & 100 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & 1 & 21 & 45 \\ 2 & \begin{matrix} 2 & 3 & 50 & 100 \end{matrix} \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & 1 & 21 \\ 0 & [1] & 8 & 10 \end{bmatrix} \]

<|ref|>text<|/ref|><|det|>[[140, 533, 610, 550]]<|/det|>
Durch Rückwärtseinsetzen für das kleinere Hotel erhalten wir 

<|ref|>equation<|/ref|><|det|>[[344, 553, 525, 571]]<|/det|>
\[ 1 \cdot y_k = 8 \Rightarrow y_k = 8 \]

<|ref|>equation<|/ref|><|det|>[[285, 574, 683, 592]]<|/det|>
\[ 1 \cdot x_k + 1 \cdot y_k = 21 \Rightarrow x_k = 21 - y_k = 21 - 8 = 13. \]

<|ref|>text<|/ref|><|det|>[[140, 595, 610, 612]]<|/det|>
Durch Rückwärtseinsetzen für das grössere Hotel erhalten wir 

<|ref|>equation<|/ref|><|det|>[[340, 616, 530, 635]]<|/det|>
\[ 1 \cdot y_g = 10 \Rightarrow y_g = 10 \]

<|ref|>equation<|/ref|><|det|>[[280, 637, 686, 656]]<|/det|>
\[ 1 \cdot x_g + 1 \cdot y_g = 45 \Rightarrow x_g = 45 - y_g = 45 - 10 = 35. \]

<|ref|>text<|/ref|><|det|>[[120, 657, 635, 674]]<|/det|>
Variante 2: Wir wenden das GAUSS-JORDAN-Verfahrenan. Es gilt 

<|ref|>equation<|/ref|><|det|>[[140, 678, 645, 725]]<|/det|>
\[ \begin{bmatrix} 1 & 1 & 21 & 45 & 2 \\ 2 & 3 & 50 & 100 \end{bmatrix} \Leftrightarrow 2 \begin{bmatrix} 1 & 1 & 21 & 45 & 2 \\ \begin{matrix} 2 & 3 & 50 & 100 \end{matrix} & 0 & [1] & 8 & 10 \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[140, 730, 325, 770]]<|/det|>
\[ \Leftrightarrow \begin{bmatrix} 1 & 0 & 13 & 35 \\ 0 & [1] & 8 & 10 \end{bmatrix} \]

**9. Lineares Gleichungssystem mit Parameter** 

<|ref|>text<|/ref|><|det|>[[115, 808, 841, 844]]<|/det|>
Bestimmen Sie die Lösungsmenge des folgenden linearen Gleichungssystems in Abhängigkeit von \(r \in \mathbb{R}\): 

<|ref|>equation<|/ref|><|det|>[[115, 843, 260, 860]]<|/det|>
\[ rx_1 + x_2 + x_3 = 1 \]

<|ref|>equation<|/ref|><|det|>[[115, 860, 260, 877]]<|/det|>
\[ x_1 + rx_2 + x_3 = 1 \]

<|ref|>equation<|/ref|><|det|>[[115, 877, 260, 894]]<|/det|>
\[ x_1 + x_2 + rx_3 = 1 \]