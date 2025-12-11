<|ref|>text<|/ref|><|det|>[[117, 82, 620, 99]]<|/det|>
Variante 2: Wir wenden das GAUSS-JORDAN-Verfahren an. Es gilt 

<|ref|>equation<|/ref|><|det|>[[140, 103, 707, 161]]<|/det|>
\[ \begin{array}{c|cccccc} 60 & 20 & 0 & 6'200t & [1] & 4 & 3 & 460t \\ 30 & 40 & 70 & 9'200t & \Leftrightarrow & 3 & 3 & 310t \\ 10 & 40 & 30 & 4'600t & & 3 & 4 & 7 & 920t \end{array} \quad \begin{array}{c|cccccc} [1] & 4 & 3 & 460t & \Leftrightarrow & 0 & -11 & -9 & -1'070t \\ & & & & & 0 & -8 & -2 & -460t \end{array} \]

<|ref|>equation<|/ref|><|det|>[[140, 168, 737, 225]]<|/det|>
\[ \begin{array}{c|cccccc} [1] & 4 & 3 & \text{460t} & [1] & 4 & 3 & \text{460t} \\ \Leftrightarrow & 0 & [4] & 1 & \text{230t} & \Leftrightarrow & 0 & [4] & 1 & \text{230t}\\ \frac{11}{4} & 0 & 11 & 9 & 1'070t & 0 & 0 & \frac{25}{4} & \frac{1'750}{t} \end{array} \quad \begin{array}{c|cccccc} [1] & \text{460t} & 3 & [1] & 4 & 3 & \text{460t} \\ \Rightarrow & 1 & 0 & [4] & 1 & \text{230t} \\ & 0 & 0 & [1] & 70t \end{array} \]

<|ref|>equation<|/ref|><|det|>[[140, 234, 702, 291]]<|/det|>
\[ \begin{array}{c|cccccc} [1] & 4 0 & 250t & 4 & [1] & 4 0 & 250t \\ \Leftrightarrow & 0 & [4] & 0 & 160t & \Leftrightarrow & 0 & [1] & 0 & 40t \\ & 0 & 0 & [1] & 70t & & 0 & 0 & [1] & 70t \end{array} \quad \begin{array}{c|cccccc} [1] 0 & 0 & 90t \\ \Rightarrow & 0 & [1] & 0 & 40t \\ & 0 & [1] & 70t \end{array} \]

<|ref|>sub_title<|/ref|><|det|>[[114, 314, 866, 348]]<|/det|>
## 7. Eindeutig lösbares lineares Gleichungssystem für 3 Variablen mit 2 rechten Seiten 

<|ref|>text<|/ref|><|det|>[[114, 348, 718, 366]]<|/det|>
Gegeben sei das folgende lineare Gleichungssystem mit \(a, b, c \in \mathbb{R}\): 

<|ref|>equation<|/ref|><|det|>[[114, 365, 255, 382]]<|/det|>
\[ 3x - 2y + z = a \]

<|ref|>equation<|/ref|><|det|>[[114, 382, 250, 399]]<|/det|>
\[ -x + 3y - z = b \]

<|ref|>equation<|/ref|><|det|>[[114, 399, 254, 415]]<|/det|>
\[ 2x + y - 3z = c. \]

<|ref|>text<|/ref|><|det|>[[114, 414, 867, 481]]<|/det|>
Bestimmen Sie jeweils die eindeutige Lösung für die rechten Seiten \(a = 2, b = 1\) und \(c = 0\) bzw. \(a = 4, b = 1\) und \(c = 5\) mit Hilfe des Gauß- oder Gauß-Jordan-Verfahrens. Führen Sie die Berechnung derart durch, dass Sie jeden Gauß-Schritt nur einmal durchführen. 

<|ref|>equation<|/ref|><|det|>[[114, 500, 737, 558]]<|/det|>
\[ \begin{array}{c|cccccc} 3 & -2 & 1 & 2 & 4 & -1 & 3 & -1 & 1 & 1 \\ -1 & 3 & -1 & 1 & 1 & \Leftrightarrow & 3 & -2 & 1 & 2 & 4 \\ 2 & 1 & -3 & 0 & 5 & 2 & 1 & -3 & 0 & 5 \end{array} \quad \begin{array}{c|cccccc} [1] & -3 & 1 & -1 & -1 \\ \Leftrightarrow & 3 & -2 & 1 & 2 & 4 \\ & 2 & 1 & -3 & 0 & 5 \end{array} \\ \begin{array}{c|cccccc} [1] & -3 & 1 & 1 & 1 & \Leftrightarrow & 3 & -2 & 2 & 4 \\ 2 & 1 & -3 & 0 & -5 & 2 & 1 & -3 & 0 & 5 \end{array}\]

<|ref|>equation<|/ref|><|det|>[[114, 566, 822, 632]]<|/det|>
\[ \begin{array}{c|cccccc} 3 & -2 & -1 & 2 & 4 & -1 & 3 & -1 & 1 \\ -1 & 3 & -1 & 1 & 1 \\ 2 & 1 & -3 & 0 & 5 \end{array} \Leftrightarrow \begin{array}{c|cccccc} [1] & -3 & 1 & \text{1} & 1 & \Leftrightarrow & 3 & -2 & 1 & 2 \\ 2 & 1 & -3 & 0 & 5 \end{array} \\ 1 & 0 & 7 & -2 & 5 & 2 & 1 & -3 & 0 & 5 \]

<|ref|>text<|/ref|><|det|>[[117, 641, 625, 657]]<|/det|>
Durch **Rückwärtseinsetzen** erhalten wir für die erste rechte Seite 

<|ref|>equation<|/ref|><|det|>[[396, 667, 455, 683]]<|/det|>
\[ z_1 = 1 \]

<|ref|>equation<|/ref|><|det|>[[228, 685, 660, 718]]<|/det|>
\[ 7y_1 - 2z_1 = 5 \quad \Rightarrow \quad y_1 = \frac{5 + 2z_1}{7} = \frac{5 + 2 \cdot 1}{7} = \frac{7}{7} = 1 \]

<|ref|>equation<|/ref|><|det|>[[196, 720, 752, 737]]<|/det|>
\[ x_1 - 3y_1 + z_1 = -1 \quad \Rightarrow \quad x_1 = 3y_1 - z_1 - 1 = 3 \cdot 1 - 1 - 1 = 3 - 2 = 1. \]

<|ref|>text<|/ref|><|det|>[[117, 739, 625, 755]]<|/det|>
Durch **Rückwärtseinsetzen** erhalten wir für die zweite rechte Seite 

<|ref|>equation<|/ref|><|det|>[[390, 758, 450, 774]]<|/det|>
\[ z_2 = 0 \]

<|ref|>equation<|/ref|><|det|>[[226, 776, 645, 810]]<|/det|>
\[ 7y_2 - 2z_2 = 7 \quad \Rightarrow \quad y_2 = \frac{7 + 2z_2}{7} = \frac{7 + 2 \cdot 0}{7} = \frac{7}{7} = 1 \]

<|ref|>equation<|/ref|><|/det|>
\[ x_2 - 3y_2 + z_2 = -1 \quad \Rightarrow \quad x_2 = 3y_2 - z_2 - 1 = 3 \cdot 1 - 0 - 1 = 3 - 1 = 2. \]