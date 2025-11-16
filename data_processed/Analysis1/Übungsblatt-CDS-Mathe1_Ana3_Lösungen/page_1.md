# Übungsblatt Ana 3 

## 1. Aussagen über Folgen

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) Jede Folge ist eine Funktion mit ganzzahligen Argumenten. | - | $\bigcirc$ |
| b) Eine Funktion des Typs $a: \mathbb{N} \rightarrow \mathbb{N}$ beschreibt eine Folge von natürlichen <br> Zahlen. | - | $\bigcirc$ |
| c) Jede Folge hat unendlich viele, voneinander verschiedene Funktionswerte. | $\bigcirc$ | $\bullet$ |
| d) Jede reelle Zahlenfolge ist entweder eine arithmetische oder geometrische <br> Folge. | $\bigcirc$ | $\bullet$ |

## 2. Untersuchung einer einfachen Folge

Betrachten Sie die Folge, welche definiert ist durch

$$
a_{n}:=\frac{2 n}{n+1} \text { für alle } n \in \mathbb{N} \text {. }
$$

a) Wir berechnen einige Folgeglieder der Folge $a_{n}$ und stellen die Ergebnisse in einer Tabelle zusammen.

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $a_{n}$ | 0 | 1 | $\frac{4}{3}$ | $\frac{3}{2}$ | $\frac{8}{5}$ | $\frac{5}{3}$ | $\frac{12}{7}$ | $\frac{7}{4}$ | $\frac{16}{9}$ | $\frac{9}{5}$ | $\frac{20}{11}$ | $\frac{11}{6}$ | $\frac{24}{13}$ | $\frac{13}{7}$ | $\frac{28}{15}$ | $\frac{15}{8}$ |

b) Aufgrund unserer Ergebnisse aus Teilaufgabe a) vermuten wir, dass die Folge $a_{n}$ nach unten beschränkt ist durch die untere Schranke $a_{\mathrm{U}}:=0$. Für alle $n \in \mathbb{N}$ gilt offensichtlich

$$
2 n \geq n \geq 0 \quad \text { und } \quad n+1>n \geq 0
$$

Da gemäss (3) sowohl Zähler als auch Nenner in (1) positiv sind, muss gelten

$$
\underline{a_{n}}=\frac{2 n}{n+1} \geq \underline{0=a_{\mathrm{U}}}
$$