<|ref|>text<|/ref|><|det|>[[114, 81, 422, 100]]<|/det|>
Aus der 2. und 1. Zeile ergibt sich 

<|ref|>equation<|/ref|><|det|>[[114, 99, 312, 117]]<|/det|>
\(y + z = 1 \rightarrow y = 1 - z\)

<|ref|>equation<|/ref|><|det|>[[114, 115, 338, 133]]<|/det|>
\(x - 2z = -3 \rightarrow x = 2z - 3\)

<|ref|>text<|/ref|><|det|>[[114, 131, 590, 150]]<|/det|>
Die Lösungsmenge ergibt sich zu \(L = \{(2z-3; 1-z; z)\}\). 

<|ref|>text<|/ref|><|det|>[[114, 149, 147, 166]]<|/det|>
c) 

<|ref|>text<|/ref|><|det|>[[114, 164, 490, 183]]<|/det|>
Mit Hilfe des Gauß-Verfahrens ergibt sich 

<|ref|>equation<|/ref|><|det|>[[122, 186, 491, 241]]<|/det|>
\[ \begin{bmatrix} 1 & 2 & p \\ 2 & 2 & q \\ 2 & 2 & 4 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & 2 & p \\ 0 & q-4 & 4-2p \end{bmatrix} \]

<|ref|>text<|/ref|><|det|>[[114, 243, 546, 262]]<|/det|>
Zweite Zeile: für \(q \neq 4\) gibt es ein Pivot-Element. 

<|ref|>text<|/ref|><|det|>[[114, 261, 234, 279]]<|/det|>
1. Fall: \(q \neq 4\) 

<|ref|>equation<|/ref|><|det|>[[122, 280, 325, 334]]<|/det|>
\[ \begin{bmatrix} 1 & 2 & p \\ 0 & [q-4] & 4-2p \end{bmatrix} \]

<|ref|>text<|/ref|><|det|>[[114, s 331, 279, 348]]<|/det|>
Rang und Defekt: 

<|ref|>equation<|/ref|><|det|>[[114, 347, 402, 365]]<|/det|>
\(n_R = 2, n_D = n_V - n_R = 2 - 2 = 0\).

<|ref|>text<|/ref|><|det|>[[114, 364, 860, 399]]<|/det|>
Pivot-Variablen: x und y, es gibt keine freien Parameter. Das LGS ist also eindeutig
lösbar. 

<|ref|>equation<|/ref|><|det|>[[192, 400, 515, 440]]<|/det|>
\[ (q-4)y = 4-2p \Rightarrow y = \frac{4-2p}{q-4} \]

<|ref|>equation<|/ref|><|det|>[[208, 441, 832, 525]]<|/det|>
\[ \begin{align*} x + 2y &= p \Rightarrow x &= p - 2y = p - 2 \frac{4-2p}{q-4} = \frac{p(q-4)}{q-4} - \frac{8-4p}{q-4} \\ &= \frac{pq-4p-8+4p}{q-4} = \frac{pq-8}{q-4}. \end{align*} \]

<|ref|>text<|/ref|><|det|>[[130, 527, 512, 546]]<|/det|>
Die Lösungsmenge des LGLS ist demnach 

<|ref|>equation<|/ref|><|det|>[[406, 549, 664, 593]]<|/det|>
\[ L = \left\{ \left( \frac{pq-8}{q-4}; \frac{4-2p}{q-4} \right) \right\}. \]

<|ref|>text<|/ref|><|det|>[[114, 595, 234, 613]]<|/det|>
2. Fall: \(q = 4\) 

<|ref|>equation<|/ref|><|det|>[[122, 615, 293, 671]]<|/det|>
\[ \begin{bmatrix} 1 & 2 & p \\ 0 & 0 & 4-2p \end{bmatrix} \]

<|ref|>text<|/ref|><|det|>[[114, calligraphy, 279, 617]]<|/det|>
Rang und Defekt: 

<|ref|>equation<|/ref|><|det|>[[114, 616, 293, 671]]<|/det|>
\[ n_R = 2, n_D = n_V - n_R = 2 - 1 = 1. \]

<|ref|>text<|/ref|><|det|>[[114, 670, 325, 688]]<|/det|>
Pivot-Variable: x, es gibt einen freien Parameter: y. Verträglichkeit in der zweiten 

<|ref|>text<|/ref|><|det|>[[114, 686, 675, 705]]<|/det|>
Zeile: für \(4-2p = 0\), also \(p = 2\) ist die Verträglichkeit gegeben. 

<|ref|>text<|/ref|><|det|>[[114, 703, 198, 721]]<|/det|>
→ \(p = 2\): 

<|ref|>equation<|/ref|><|det|>[[122, 721, 245, 815]]<|/det|>
\[ \begin{bmatrix} 1 & 2 & 2 \\ 0 & 0 & 0 \end{bmatrix} \]

<|ref|>text<|/ref|><|det|>[[114, 817, 792, 837]]<|/det|>
Es ergibt sich \(x + 2y = 2 \Rightarrow x = 2 - 2y\). Die Lösungsmenge ist \(L = \{(2-2y; y)\}\). 

<|ref|>text<|/ref|><|det|>[[114, 835, 198, 853]]<|/det|>
→ \(p \neq 2\): 

<|ref|>text<|/ref|><|det|>[[114, 852, 848, 888]]<|/det|>
Verträglichkeit in der zweiten Zeile ist nicht gegeben und somit lässt sich das LGS
nicht lösen, d. h. \(L = \emptyset\). 

<|ref|>text<|/ref|><|det|>[[114, 887, 145, 904]]<|/det|>
d) 

<|ref|>text<|/ref|><|det|>[[114, 903, 415, 922]]<|/det|>
Anwenden des Gauß-Verfahrens