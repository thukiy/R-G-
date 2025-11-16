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