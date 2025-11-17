# --- PAGE page_1 ---

# $\stackrel{\text { F }}{ }$ Fachhochschule Graubünden <br> GR University of Applied Sciences 

## Übungsblatt Ana 1

Computational and Data Science BSc HS 2023

## Lösungen

Mathematik 1

## 1. Aussagen über zwei Mengen

Wir betrachten die Mengen

$$
A:=\{0,2,3,4,5,6\} \quad \text { und } \quad B:=\{A, 4,5,6,7\}
$$

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :--: | :--: |
| a) Die Menge $A$ hat sechs Elemente. | $\bullet$ | $\bigcirc$ |
| b) Die Menge $B$ hat sieben Elemente. | $\bigcirc$ | $\bullet$ |
| c) Es gilt $\{4\} \in A$. | $\bigcirc$ | $\bullet$ |
| d) Es gilt $A \subset B$. | $\bigcirc$ | $\bullet$ |
| e) Es gilt $B \ni A$. | $\bullet$ | $\bigcirc$ |
| f) Es gilt $B \supseteq\{A\}$. | $\bullet$ | $\bigcirc$ |

## 2. Elementare Mengenoperationen

Wir betrachten die Mengen

$$
A:=\{1,6,7,9,12\} \quad \text { und } \quad B:=\{2,4,7,8,10,12\}
$$

a) Wir skizzieren das VEnN-Diagramm für die Mengen $A$ und $B$.


# --- PAGE page_2 ---

b) Wenn wir alle Elemente sammeln, welche in $A$ und in $B$ liegen, dann erhalten wir die Schnittmenge
$\underline{A \cap B=\{7,12\}}$.
c) Wenn wir alle Elemente sammeln, welche in $A$ oder in $B$ liegen, dann erhalten wir die Vereinigungsmenge
$\underline{A \cup B=\{1,2,4,6,7,8,9,10,12\}}$
d) Wenn wir alle Elemente sammeln, welche in $A$ aber nicht in $B$ liegen, dann erhalten wir die Mengendifferenz
$\underline{A \backslash B=\{1,6,9\}}$.
Sammeln wir hingegen alle Elemente, welche in $B$ aber nicht in $A$ liegen, dann erhalten wir die Mengendifferenz
$\underline{B \backslash A=\{2,4,8,10\}}$.
e) Wir zeigen mehrere Varianten, um die symmetrische Mengendifferenz $A \Delta B$ zu berechnen.
Variante 1: Die Menge $A \Delta B$ ist die Vereinigung der beiden Mengendifferenzen aus Teilaufgabe d). Wir erhalten

$$
\underline{A \Delta B}=(A \backslash B) \cup(B \backslash A)=\{1,6,9\} \cup\{2,4,8,10\}=\underline{\{1,2,4,6,8,9,10\}}
$$

Variante 2: Die Menge $A \Delta B$ ist die Mengendifferenz der Vereinigungsmenge von $A$ und $B$ aus Teilaufgabe c) ohne die Schnittmenge von $A$ und $B$ aus Teilaufgabe b). Wir erhalten

$$
\begin{aligned}
\underline{A \Delta B} & =(A \cup B) \backslash(B \cap A)=\{1,2,4,6,7,8,9,10,12\} \backslash\{7,12\} \\
& =\underline{\{1,2,4,6,8,9,10\}}
\end{aligned}
$$

f) Wir suchen alle Teilmengen von
$C:=A \cap B=\{7,12\}$.
Da $C$ zwei Elemente hat, hat jede Teilmenge von $C$ entweder null, ein oder zwei Elemente. Wir bestimmen für jede mögliche Anzahl Elemente die zugehörigen Teilmengen von $C$ und stellen die Ergebnisse in einer Tabelle zusammen.

| Anzahl Elemente | Teilmengen |
| :--: | :-- |
| 0 | $\varnothing$ |
| 1 | $\{7\},\{12\}$ |
| 2 | $\{7,12\}$ |

Insgesamt haben wir also vier Teilmengen von $C$ gefunden. Alle Teilmengen ausser $C$ selbst sind echte Teilmengen von $C$, d.h.

$$
\varnothing,\{7\} \quad \text { und } \quad\{12\}
$$

# --- PAGE page_3 ---

# 3. Mengen und Operationen in einer Grundmenge 

Wir betrachten die Grundmenge $G$ der Kleinbuchstaben des lateinischen Alphabetes ohne Umlaute, d.h.

$$
G:=\{a, \ldots, z\}
$$

Ferner seien

$$
A:=\{m, a, t, h, e\}, B:=\{i, s, t, m, e, g, a\} \quad \text { und } \quad C:=\{g, e, n, i, a, l\}
$$

sowie

$$
D:=A \cap B \cap C \quad \text { und } \quad E:=A \cup B \cup C
$$

a) Wir skizzieren das VENn-Diagramm für die drei Mengen $A, B, C$ in der Grundmenge $G$.

b) Mit Hilfe des VENn-Diagramms aus Teilaufgabe a) bestimmen wir die Schnittmengen. Wir erhalten

$$
\begin{aligned}
& \underline{A \cap B}=\{\underline{a, e, m, t}\} \\
& \underline{A \cap C}=\{\underline{a, e}\} \\
& \underline{C \cap B}=\underline{\{\underline{a, e}, g, i\}}
\end{aligned}
$$

und

$$
\underline{D=\{a, e\}}
$$

c) Mit Hilfe des VENn-Diagramms aus Teilaufgabe a) bestimmen wir die Vereinigungsmengen. Wir erhalten

$$
\underline{A \cup B}=\underline{\{\underline{a, e}, g, h, i, m, t, s\}}
$$

# --- PAGE page_4 ---

$\underline{\underline{A \cup C}}=\{a, e, g, h, i, l, m, n, t\}$
$\underline{\underline{C \cup B}}=\underline{\{a, e, g, i, l, m, n, t, s\}}$
und
$\underline{E=\{a, e, g, h, i, l, m, n, t, s\}}$.
d) Für das Komplement der Schnittmenge $D$ erhalten wir

$$
\underline{\bar{D}}=G \backslash D=\{a, \ldots, z\} \backslash\{a, e\}=\underline{\{b, c, d, f, \ldots, z\}}
$$

Mit Hilfe des Venn-Diagramms aus Teilaufgabe a) bestimmen wir das Komplement der Vereinigungsmenge E. Es gilt

$$
\underline{\bar{E}}=G \backslash E=\underline{\{b, c, d, f, j, k, o, p, q, r, u, v, w, x, y, z\}}
$$

# 4. Aussagen über rationale Zahlen 

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) Jede rationale Zahl kann als Bruch von zwei ganzen Zahlen dargestellt <br> werden. | $\bullet$ | $\bigcirc$ |
| b) Es gilt $\mathbb{Q} \supset \mathbb{Z}$. | $\bullet$ | $\bigcirc$ |
| c) Es gilt $\sqrt{9} \notin \mathbb{Q}$. | $\bigcirc$ | $\bullet$ |
| d) Die Wurzel einer rationalen Zahl ist selbst auch rational. | $\bigcirc$ | $\bullet$ |
| e) Alle periodischen Dezimalbrüche sind rational. | $\bullet$ | $\bigcirc$ |

## 5. Aussagen über reelle Zahlen

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) Jede rationale Zahl ist auch eine reelle Zahl, aber nicht umgekehrt. | $\bullet$ | $\bigcirc$ |
| b) Es gilt $\infty \in \mathbb{R}$. | $\bigcirc$ | $\bullet$ |
| c) Falls $x, y \in \mathbb{R}$ und $x \leq y$ sowie $y \leq x$, dann gilt $x=y$. | $\bullet$ | $\bigcirc$ |
| d) Die Wurzel jeder reellen Zahl ist auch eine reelle Zahl. | $\bigcirc$ | $\bullet$ |
| e) Alle Dezimalbrüche sind reelle Zahlen. | $\bullet$ | $\bigcirc$ |

# --- PAGE page_5 ---

# 6. Elemente von Zahlenmengen 

Wir markieren für jede Zahl die Mengen, von welchen die Zahl ein Element ist.

|  | $x$ | $\mathbb{N}$ | $\mathbb{N}^{+}$ | $\mathbb{Z}$ | $\mathbb{Q}$ | $\mathbb{R}$ | $\mathbb{R}_{0}^{+}$ | $\mathbb{R}^{-}$ | $[-1,1]$ | $] 0,2[$ | $]-\infty, 1[$ | $[0, \infty[$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| a) | $-1$ | $\square$ | $\square$ | ■ | ■ | ■ | $\square$ | ■ | ■ | $\square$ | ■ | $\square$ |
| b) | 0.5 | $\square$ | $\square$ | $\square$ | ■ | ■ | ■ | $\square$ | ■ | ■ | ■ | ■ |
| c) | $-1 / 3$ | $\square$ | $\square$ | $\square$ | ■ | ■ | $\square$ | ■ | ■ | $\square$ | ■ | $\square$ |
| d) | $\sqrt{3}$ | $\square$ | $\square$ | $\square$ | $\square$ | ■ | ■ | $\square$ | $\square$ | ■ | $\square$ | ■ |
| e) | 0.33 | $\square$ | $\square$ | $\square$ | ■ | ■ | ■ | $\square$ | ■ | ■ | ■ | ■ |
| f) | $\sqrt{25}$ | ■ | ■ | ■ | ■ | ■ | ■ | $\square$ | $\square$ | $\square$ | $\square$ | ■ |
| g) | $-6 / 3$ | $\square$ | $\square$ | ■ | ■ | ■ | $\square$ | ■ | $\square$ | $\square$ | ■ | $\square$ |
| h) | $-\sqrt{2 / 3}$ | $\square$ | $\square$ | $\square$ | $\square$ | ■ | $\square$ | ■ | ■ | $\square$ | ■ | $\square$ |
| i) | 7.34385 | $\square$ | $\square$ | $\square$ | ■ | ■ | ■ | $\square$ | $\square$ | $\square$ | $\square$ | ■ |
| j) | $-0.99$ | $\square$ | $\square$ | ■ | ■ | ■ | $\square$ | ■ | ■ | $\square$ | ■ | $\square$ |

## 7. Aussagen über Intervalle

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) Es gilt $[1,10] \subset \mathbb{N}$. | $\bigcirc$ | $\bullet$ |
| b) Es gilt $] 2,3[\cap \mathbb{Z}=\varnothing$. | $\bullet$ | $\bigcirc$ |
| c) Für alle $a, b \in \mathbb{R}$ mit $a<b$ gilt $] a, b] \subset[a, b[$. | $\bigcirc$ | $\bullet$ |
| d) Für alle $x \in \mathbb{R}$ gilt $]-\infty, x] \cap\left[x, \infty[=\{x\}\right.$. | $\bullet$ | $\bigcirc$ |
| e) Falls $] a, b[\cap] c, d[=\varnothing$, dann gilt $c>b$. | $\bigcirc$ | $\bullet$ |
| f) Für alle $a, b \in \mathbb{R}$ mit $a<b$ gilt $[a, b] \cap \mathbb{Q} \neq \varnothing$. | $\bullet$ | $\bigcirc$ |

## 8. Aussagen über das kartesische Produkt

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) Das kartesische Produkt ist eine Operation zwischen zwei Zahlen. | $\bigcirc$ | $\bullet$ |
| b) Das kartesische Produkt ist eine Operation zwischen zwei Mengen. | $\bullet$ | $\bigcirc$ |
| c) In jedem Fall gilt $A \times B=B \times A$. | $\bigcirc$ | $\bullet$ |
| d) Kartesische Produkte können nur zwischen Mengen gebildet werden, wel- <br> che aus Zahlen bestehen. | $\bigcirc$ | $\bullet$ |
| e) Haben $A$ und $B$ jeweils 10 Elemente, dann haben $A \times B$ und $B \times A$ jeweils <br> 100 Elemente. | $\bullet$ | $\bigcirc$ |
| f) Für jede Menge $A$ gilt $\varnothing \times A=A$. | $\bigcirc$ | $\bullet$ |

# --- PAGE page_6 ---

# 9. Kartesische Produkte 

Wir bestimmen die folgenden kartesischen Produkte und stellen diese auf sinnvolle Weise dar.
a) Wir betrachten die Menge

$$
\underline{A}=\{1,2\} \times\{1,2\}=\underline{\{(1 ; 1),(1 ; 2),(2 ; 1),(2 ; 2)\}}
$$

b) Wir betrachten die Menge

$$
\underline{B}=\{1,2\} \times\{2,3,4\}=\underline{\{(1 ; 2),(1 ; 3),(1 ; 4),(2 ; 2),(2 ; 3),(2 ; 4)\}}
$$

c) Wir betrachten die Menge

$$
\underline{C}=\{2,3,4\} \times\{1,2\}=\underline{\{(2 ; 1),(2 ; 2),(3 ; 1),(3 ; 2),(4 ; 1),(4 ; 2)\}}
$$

Wir stellen die Mengen

$$
D=[0,1] \times\{1,2\}, E=\{1,2\} \times[0,1] \quad \text { und } \quad F=[0,1] \times[1,2]
$$

jeweils in einem $x y$-Diagramm dar.


## 10. Aussagen über zwei Mengen

Wir betrachten die Mengen

$$
A:=\{-1,0,1\} \quad \text { und } \quad B:=\{3,4,5\}
$$

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) Die Menge $A \times B$ hat drei Elemente. | $\bigcirc$ | $\bullet$ |
| b) Es gilt $-1 \in A \times B$. | $\bigcirc$ | $\bullet$ |
| c) Es gilt $(3 ; 0) \in B \times A$. | $\bullet$ | $\bigcirc$ |
| d) Es gilt $A \times B=B \times A$. | $\bigcirc$ | $\bullet$ |
| e) Die graphische Darstellung von $A \times B$ im $x y$-Diagramm ist ein Rechteck. | $\bigcirc$ | $\bullet$ |
| f) Es gilt $A \times B \subset \mathbb{Z} \times \mathbb{N}$. | $\bullet$ | $\bigcirc$ |