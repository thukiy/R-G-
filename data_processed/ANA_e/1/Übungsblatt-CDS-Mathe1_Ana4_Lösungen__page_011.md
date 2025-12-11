<|ref|>sub_title<|/ref|><|det|>[[108, 66, 345, 85]]<|/det|>
## 13. Martingale Strategie 

<|ref|>text<|/ref|><|det|>[[108, 83, 828, 103]]<|/det|>
Als *Martingale* bezeichnet man folgende Strategie, um beim Roulette zu gewinnen. 

<|ref|>text<|/ref|><|det|>[[108, 105, 923, 159]]<|/det|>
**§1** Es wird nur auf einfache Chancen gesetzt (z.B. Rot und Schwarz), das heisst, der gesetzte Betrag geht bei jedem Spiel entweder als gesamtes verloren oder wird im Gewinnfall durch die Bank verdoppelt. 

<|ref|>text<|/ref|><|det|>[[108, 162, 577, 182]]<|/det|>
**§2** Nach jedem Verlust wird der Einsatz verdoppelt. 

<|ref|>text<|/ref|><|det|>[[123, 189, 923, 226]]<|/det|>
a) Der erste Einsatz betrage \(E_0 := 1\) CHF und jeder weitere Einsatz sei die Verdoppelung des jeweils unmittelbar Vorangegangenen, das heisst 

<|ref|>equation<|/ref|><|det|>[[153, 228, 920, 250]]<|/det|>
\[E_k = 2 \cdot E_{k-1} = 2 \cdot 2 \cdot E_{k-2} = \ldots = 2^k \cdot E_{k-k} = 2^k \cdot E_0. \qquad (53)\]

<|ref|>text<|/ref|><|det|>[[153, 253, 723, 273]]<|/det|>
Der Gesamtverlust nach acht verlorenen Spielen beträgt demnach 

<|ref|>equation<|/ref|><|det|>[[150, 276, 920, 349]]<|/det|>
\[\begin{align*} V_7 &= \sum_{k=0}^{7} E_k = \sum_{k=0}^{7} 2^k \cdot E_0 = E_0 \sum_{k=0}^{7} 2^k = E_0 \cdot G_{(0;7)}(2) = E_0 \cdot \frac{2^0 - 2^8}{1 - 2} = E_0 \cdot \frac{1 - 256}{-1} \\ &= 1 \text{ CHF} \cdot 255 = 255 \text{ CHF}. \end{align*}\] (54) 

<|ref|>text<|/ref|><|det|>[[120, 360, 923, 397]]<|/det|>
b) Wenn das neunte Spiel nach acht verlorenen Spielen gewonnen wird und der erste Einsatz einen Franken betrug, dann erhält der Spieler einen Gesamtgewinn von 

<|ref|>equation<|/ref|><|det|>[[153, 400, 920, 421]]<|/det|>
\[\underline{G} = E_8 - V_7 = 2^8 \cdot E_0 - V_7 = 256 \cdot 1 \text{ CHF} - 255 \text{ CHF} = \underline{1} \text{ CHF}. \qquad (55)\]

<|ref|>text<|/ref|><|det|>[[120, 431, 825, 451]]<|/det|>
c) Es sei \(n \in \mathbb{N}^*\). Der Gesamtverlust nach \(n\) verlorenen Spielen beträgt demnach 

<|ref|>equation<|/ref|><|det|>[[153, 455, 920, 530]]<|/det|>
\[\begin{align*} V_{n-1} &= \sum_{k=0}^{n-1} E_k = \sum_{k=0}^{n-1} 2^k \cdot E_0 = E_0 \sum_{k=0}^n 2^k = E_0 \cdot G_{(0;n-1)}(2) = E_0 \cdot \frac{2^0 - 2^n}{1 - 2} = E_0 \cdot \frac{1 - 2^n}{-1} \\ &= (2^n - 1) \cdot E_0. \end{align*}\] (56)

<|ref|>text<|/ref|><|det|>[[153, 533, 718, 552]]<|/det|>
Wird das Spiel \(n+1\) gewonnen, dann beträgt der Gesamtgewinn 

<|ref|>equation<|/ref|><|det|>[[153, 555, 920, 578]]<|/det|>
\[\underline{G} = E_n - V_{n-1} = 2^n \cdot E_0 - (2^n - 1) \cdot E_0 = 2^n \cdot E_0 - 2^n \cdot E_0 + E_0 = \underline{E_0} > 0. \qquad (57)\]

<|ref|>text<|/ref|><|det|>[[153, 586, 920, 622]]<|/det|>
Unabhängig von der Höhe des ersten Einsatzes gewinnt der Spieler nach \(n\) verlorenen Spielen und einem gewonnenen Spiel \(n+1\) insgesamt gerade den Betrag \(E_0\). 

<|ref|>sub_title<|/ref|><|det|>[[108, 639, 490, 657]]<|/det|>
## 14. Aussagen über eine spezielle Summe 

<|ref|>text<|/ref|><|det|>[[108, 657, 576, 676]]<|/det|>
Es sei \(0 < z < 1\) und \(n \in \mathbb{N}\). Wir betrachten die Summe 

<|ref|>equation<|/ref|><|det|>[[431, 675, 920, 720]]<|/det|>
\[S_n = \sum_{k=0}^{n} \frac{(-1)^{k+1}}{(1+z)^k}. \qquad (58)\]

<|ref|>table<|/ref|><|det|>[[108, 725, 920, 919]]<|/det|>
<table><tr><td>Welche der folgenden Aussagen sind wahr und welche falsch?</td><td>wahr</td><td>falsch</td></tr><tr><td>a) Es gilt \(S_0 < 0\).</td><td>●</td><td>○</td></tr><tr><td>b) Es gibt ein \(x \in \mathbb{R}\), so dass \(S_n = -G_{(0;n)}(x)\) für alle \(n \in \mathbb{N}^+\).</td><td>●</td><td>○</td></tr><tr><td>c) Für alle \(n \in \mathbb{N}^+\) gilt \(S_{n+1} > S_n\).</td><td>○</td><td>●</td></tr><tr><td>d) Für alle \(n \in \mathbb{N}^+\) gilt \(S_n < 0\).</td><td>●</td><td>○</td></tr><tr><td>e) Ist \(z \in \mathbb{Q}\), dann folgt \(S_n \in \mathbb{Q}\) für alle \(n \in \mathbb{N}\).</td><td>●</td><td>○</td></tr><tr><td>f) Für sehr grosse \(n \in \mathbb{N}^+\) gilt \(S_n \approx -\frac{1+z}{2+z}\).</td><td>●</td><td>○</td></tr></table>