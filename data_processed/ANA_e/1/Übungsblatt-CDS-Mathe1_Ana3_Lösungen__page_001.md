<|ref|>title<|/ref|><|det|>[[108, 150, 510, 194]]<|/det|>
# Übungsblatt Ana 3 

<|ref|>text<|/ref|><|det|>[[568, 156, 926, 196]]<|/det|>
Computational and Data Science BSc
HS 2023 

<|ref|>text<|/ref|><|det|>[[108, 234, 257, 261]]<|/det|>
## Lösungen 

<|ref|>text<|/ref|><|det|>[[783, 241, 923, 260]]<|/det|>
Mathematik 1 

<|ref|>sub_title<|/ref|><|det|>[[108, 289, 343, 308]]<|/det|>
### 1. Aussagen über Folgen 

<|ref|>table<|/ref|><|det|>[[108, 316, 920, 473]]<|/det|>
<table><tr><td>Welche der folgenden Aussagen sind wahr und welche falsch?</td><td>wahr</td><td>falsch</td></tr><tr><td>a) Jede Folge ist eine Funktion mit ganzzahligen Argumenten.</td><td>●</td><td>○</td></tr><tr><td>b) Eine Funktion des Typs \(a: \mathbb{N} \to \mathbb{N}\) beschreibt eine Folge von natürlichen Zahlen.</td><td>●</td><td>○</td></tr><tr><td>c) Jede Folge hat unendlich viele, voneinander verschiedene Funktionswerte.</td><td>○</td><td>●</td></tr><tr><td>d) Jede reelle Zahlenfolge ist entweder eine arithmetische oder geometrische Folge.</td><td>○</td><td>●</td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[108, 550, 468, 567]]<|/det|>
### 2. Untersuchung einer einfachen Folge 

<|ref|>text<|/ref|><|det|>[[108, 567, 549, 584]]<|/det|>
Betrachten Sie die Folge, welche definiert ist durch 

<|ref|>equation<|/ref|><|det|>[[386, 594, 920, 629]]<|/det|>
\[a_n := \frac{2n}{n+1} \quad \text{für alle } n \in \mathbb{N}. \qquad (1)\]

<|ref|>text<|/ref|><|det|>[[120, 645, 920, 680]]<|/det|>
a) Wir berechnen einige Folgeglieder der Folge \(a_n\) und stellen die Ergebnisse in einer Tabelle zusammen. 

<|ref|>table<|/ref|><|det|>[[258, 689, 810, 744]]<|/det|>
<table><tr><td>n</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td></tr><tr><td>\(a_n\)</td><td>0</td><td>1</td><td>\(\frac{4}{3}\)</td><td>\(\frac{3}{2}\)</td><td>\(\frac{8}{5}\)</td><td>\(\frac{5}{3}\)</td><td>\(\frac{12}{7}\)</td><td>\(\frac{7}{4}\)</td><td>\(\frac{16}{9}\)</td><td>\(\frac{9}{5}\)</td><td>\(\frac{20}{11}\)</td><td>\(\frac{11}{6}\)</td><td>\(\frac{24}{13}\)</td><td>\(\frac{13}{7}\)</td><td>\(\frac{28}{15}\)</td><td>\(\frac{15}{8}\)</td></tr></table>

<|ref|>text<|/ref|><|det|>[[120, 758, 920, 794]]<|/det|>
b) Aufgrund unserer Ergebnisse aus Teilaufgabe a) vermuten wir, dass die Folge \(a_n\) nach unten beschränkt ist durch die untere Schranke \(a_U := 0\). Für alle \(n \in \mathbb{N}\) gilt offensichtlich 

<|ref|>equation<|/ref|><|det|>[[383, 807, 920, 825]]<|/det|>
\[2n \ge n \ge 0 \quad \text{und} \quad n+1 > n \ge 0. \qquad (3)\]

<|ref|>text<|/ref|><|det|>[[150, 839, 820, 857]]<|/det|>
Da gemäss (3) sowohl Zähler als auch Nenner in (1) positiv sind, muss gelten 

<|ref|>equation<|/ref|><|det|>[[150, 867, 920, 903]]<|/det|>
\[a_n = \frac{2n}{n+1} \ge 0 = a_U. \qquad (4)\]