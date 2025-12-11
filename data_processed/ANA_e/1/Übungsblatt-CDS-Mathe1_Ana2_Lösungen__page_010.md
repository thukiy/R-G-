<|ref|>sub_title<|/ref|><|det|>[[107, 67, 386, 85]]<|/det|>
## 7. Aussagen über Funktionen 

<|ref|>text<|/ref|><|det|>[[107, 85, 650, 103]]<|/det|>
Wir betrachten eine allgemeine Funktion der Form \(f: A \to B\). 

<|ref|>table<|/ref|><|det|>[[107, 111, 920, 305]]<|/det|>
<table><tr><td>Welche der folgenden Aussagen sind wahr und welche falsch?</td><td>wahr</td><td>falsch</td></tr><tr><td>a) In jedem Fall kann B durch \(\mathbb{R}\) ersetzt werden.</td><td>○</td><td>●</td></tr><tr><td>b) Es muss gelten \(A \subseteq B\).</td><td>○</td><td>●</td></tr><tr><td>c) Es muss gelten \(f(A) = B\).</td><td>○</td><td>●</td></tr><tr><td>d) Es muss gelten \(f^{-1}(B) = A\).</td><td>●</td><td>○</td></tr><tr><td>e) Die Umkehrfunktion \(f^{-1}: B \to A\) existiert genau dann, wenn \(f\) bijektiv ist.</td><td>●</td><td>○</td></tr><tr><td>f) Falls \(A \subset B\), dann kann \(f\) nicht surjektiv sein.</td><td>○</td><td>●</td></tr></table>

<|ref|>text<|/ref|><|det|>[[107, 321, 644, 340]]<|/det|>
Zu einzelnen Teilaufgaben machen wir ein paar Bemerkungen. 

<|ref|>text<|/ref|><|det|>[[120, 343, 810, 363]]<|/det|>
a) Die Zielmenge \(B\) kann nur durch \(\mathbb{R}\) ersetzt werden, wenn bereits gilt \(B \subseteq \mathbb{R}\). 

<|ref|>text<|/ref|><|det|>[[120, 370, 920, 407]]<|/det|>
b) Definitions- und Zielmenge müssen keine gemeinsamen Elemente haben. Als Gegenbeispiel betrachten wir \(A = \{1, 3\}\) und \(B = \{2, 6, 10\}\) sowie die Funktion 

<|ref|>equation<|/ref|><|det|>[[455, 419, 920, 460]]<|/det|>
\[f: A \to B \quad (40) \\ x \mapsto f(x) := 2x. \]

<|ref|>text<|/ref|><|det|>[[150, 472, 572, 491]]<|/det|>
Offensichtlich gilt \(A \cap B = \emptyset\) und somit \(A \not\subseteq B\). 

<|ref|>text<|/ref|><|det|>[[120, 498, 815, 517]]<|/det|>
c) Die Zielmenge \(B\) darf "zu gross" sein. Im Beispiel aus (40) gilt offensichtlich 

<|ref|>equation<|/ref|><|det|>[[280, 529, 920, 551]]<|/det|>
\[f(A) = f(\{1, 3\}) = \{f(1), f(3)\} = \{2, 6\} \subset \{2, 6, 10\} = B. \quad (41)\]

<|ref|>text<|/ref|><|det|>[[150, 561, 464, 580]]<|/det|>
In jedem Fall gilt jedoch \(f(A) \subseteq B\). 

<|ref|>text<|/ref|><|det|>[[120, 587, 323, 605]]<|/det|>
d) Nach Definition ist 

<|ref|>equation<|/ref|><|det|>[[398, 618, 920, 640]]<|/det|>
\[f^{-1}(B) = \{x \in A \mid f(x) \in B\}. \quad (42)\]

<|ref|>text<|/ref|><|det|>[[150, 650, 920, 687]]<|/det|>
Offensichtlich ist \(f^{-1}(B) \subseteq A\). Weil für jedes \(x \in A\) gilt \(f(x) \in B\) folgt auch \(A \subseteq f^{-1}(B)\). Insgesamt ist also zwingend \(f^{-1}(B) = A\). 

<|ref|>text<|/ref|><|det|>[[120, 694, 567, 713]]<|/det|>
e) Wir betrachten die auftretenden Fälle getrennt. 

<|ref|>text<|/ref|><|det|>[[150, 716, 920, 752]]<|/det|>
**Fall 1:** \(f\) ist bijektiv. In diesem Fall existiert die Umkehrfunktion, wie das folgende Schema illustriert. 

<|ref|>image<|/ref|><|det|>[[330, 755, 770, 862]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[150, 869, 895, 888]]<|/det|>
**Fall 2:** \(f\) ist nicht bijektiv. In diesem Fall ist \(f\) nicht surjektiv und/oder nicht injektiv.