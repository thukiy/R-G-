# 5. Aussagen über eine Funktion 

Wir betrachten die Mengen

$$
A:=\{-1,0,1,3,5\} \quad \text { und } \quad B:=\{-1,0,1,3,7,11\}
$$

sowie die Funktion

$$
\begin{aligned}
f: A & \rightarrow B \\
x & \mapsto f(x):=2 x+1
\end{aligned}
$$

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :--: | :--: |
| a) Es gilt $f(0)=0$. | $\bigcirc$ | $\bullet$ |
| b) Es gilt $f(\{3,5\})=\{7,11\}$. | $\bullet$ | $\bigcirc$ |
| c) Es gilt $f^{-1}(\{0\})=\varnothing$. | $\bullet$ | $\bigcirc$ |
| d) Die Funktion $f$ ist surjektiv. | $\bigcirc$ | $\bullet$ |
| e) Die Funktion $f$ ist injektiv. | $\bullet$ | $\bigcirc$ |
| f) Die Funktion $f$ ist bijektiv. | $\bigcirc$ | $\bullet$ |

Um eine Übersicht über die Wirkung der Funktion $f$ zu erhalten, stellen wir die Funktionswerte in einer Tabelle zusammen.

| $x$ | -1 | 0 | 1 | 3 | 5 |
| :--: | :--: | :--: | :--: | :--: | :--: |
| $f(x)$ | -1 | 1 | 3 | 7 | 11 |

Zu einzelnen Teilaufgaben machen wir ein paar Bemerkungen.
a) Es ist zwar $0 \in A$ und $0 \in B$ aber gemäss Tabelle (22) gilt $f(0)=1$.
b) Es ist $\{3,5\} \subseteq A,\{7,11\} \subseteq B$ und gemäss Tabelle (22) gilt

$$
\underline{f(\{3,5\})}=\{f(3), f(5)\}=\underline{\{7,11\}}
$$

c) Es gilt zwar $0 \in B$, aber in der zweiten Zeile der Tabelle (22) steht keine 0 . Somit tritt 0 nicht als Funktionswert von $f$ auf. Es gibt daher kein $x \in A$ mit $f(x)=0$ und es folgt $f$ $\underline{-1}(\{0\})=\varnothing$
d) Weil das Element $0 \in B$ als Funktionswert in der zweiten Zeile der Tabelle (22) nicht auftritt, kann $f$ nicht surjektiv sein.
e) Weil jedes Element aus $B$ als Funktionswert in der zweiten Zeile der Tabelle (22) höchstens einmal auftritt, ist $f$ injektiv.
f) Weil $f$ gemäss Teilaufgabe d) nicht surjektiv ist, kann $f$ auch nicht bijektiv sein.