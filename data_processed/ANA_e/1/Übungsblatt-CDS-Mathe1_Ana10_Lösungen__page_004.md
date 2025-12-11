<|ref|>sub_title<|/ref|><|det|>[[74, 66, 567, 85]]<|/det|>
5. Aussagen über Ableitungen von Arcus-Funktionen 

<|ref|>table<|/ref|><|det|>[[75, 94, 888, 290]]<|/det|>
<table><tr><td>Welche der folgenden Aussagen sind wahr und welche falsch?</td><td>wahr</td><td>falsch</td></tr><tr><td>a) Die Ableitungen der Arcus-Funktionen sind nur bezüglich des Bogenmass definiert.</td><td>●</td><td>○</td></tr><tr><td>b) Die Ableitungen \(\arcsin'(x)\) und \(\arccos'(x)\) sind für alle \(x \in \mathbb{R}\) definiert.</td><td>○</td><td>●</td></tr><tr><td>c) Die Ableitungen \(\arcsin'(x)\) und \(\arccos'(x)\)s sind genau für alle jene \(x \in \mathbb{R}\) definiert, an welchen auch \(\arcsin(x)\) bzw. \(\arccos(x)\) definiert sind.</td><td>○</td><td>●</td></tr><tr><td>d) Die Ableitungen \(\arctan'(x)\) und \(\arccot'(x)\) sind für alle \(x \in \mathbb{R}\) definiert.</td><td>●</td><td>○</td></tr><tr><td>e) Die Ableitungen \(\arctan'(x)\) und \(\arccot'(x)\)s sind genau für alle jene \(x \in \mathbb{R}\) definierten, an welchen auch \(\arctan(x)\) bzw. \(\arccot(x)\) definiert sind.</td><td>●</td><td>○</td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[74, 357, 408, 375]]<|/det|>
6. Ableitung von Arcus-Funktionen 

<|ref|>text<|/ref|><|det|>[[74, 373, 860, 410]]<|/det|>
Wir verwenden die Ketten-Regel, um jeweils die Ableitung der folgenden Funktionen aus der Ableitung der Umkehrfunktion zu bestimmen. 

<|ref|>text<|/ref|><|det|>[[90, 413, 368, 434]]<|/det|>
a) Für alle \(\varphi \in ]-\pi/2, \pi/2[\) gilt 

<|ref|>equation<|/ref|><|det|>[[417, 444, 888, 465]]<|/det|>
\[ \arcsin(\sin(\varphi)) = \varphi \qquad (24) \]

<|ref|>text<|/ref|><|det|>[[118, 477, 163, 494]]<|/det|>
und 

<|ref|>equation<|/ref|><|det|>[[328, 504, 888, 536]]<|/det|>
\[ \cos(\varphi) > 0 \Rightarrow \cos(\varphi) = \sqrt{1 - \sin^2(\varphi)}. \qquad (25) \]

<|ref|>text<|/ref|><|det|>[[118, 545, 780, 564]]<|/det|>
Durch beidseitiges Ableiten von (24) mit Hilfe der Ketten-Regel erhalten wir 

<|ref|>equation<|/ref|><|det|>[[231, 575, 888, 596]]<|/det|>
\[ \arcsin'(\sin(\varphi)) \cdot \sin'(\varphi) = \varphi' \qquad (26) \]

<|ref|>equation<|/ref|><|det|>[[166, 605, 888, 626]]<|/det|>
\[ \Rightarrow \quad \arcsin'(\sin(\varphi)) \cdot \cos(\varphi) = 1 \qquad |: \cos(\varphi) \qquad (27) \]

<|ref|>equation<|/ref|><|det|>[[166, 633, 888, 671]]<|/det|>
\[ \Rightarrow \quad \arcsin'(\sin(\varphi)) = \frac{1}{\cos(\varphi)} = \frac{1}{\sqrt{1 - \sin^2(\varphi)}}. \qquad (28) \]

<|ref|>text<|/ref|><|det|>[[118, 682, 888, 718]]<|/det|>
Durch die Substitution \(x := \sin(\varphi)\) erhalten wir für alle \(x \in ]-1, 1[\) die Arcussinus-Ableitung 

<|ref|>equation<|/ref|><|det|>[[402, 727, 888, 767]]<|/det|>
\[ \arcsin'(x) = \frac{1}{\sqrt{1 - x^2}}. \qquad (29) \]

<|ref|>text<|/ref|><|det|>[[90, 789, 317, 808]]<|/det|>
b) Für alle \(\varphi \in ]0, \pi[\) gilt 

<|ref|>equation<|/ref|><|det|>[[417, 819, 888, 839]]<|/det|>
\[ \arccos(\cos(\varphi)) = \varphi \qquad (30) \]

<|ref|>text<|/ref|><|det|>[[118, 852, 163, 869]]<|/det|>
und 

<|ref|>equation<|/ref|><|det|>[[330, 880, 888, 901]]<|/det|>
\[ \sin(\varphi) > 0 \Rightarrow \sin(\varphi) = \sqrt{1 - \cos^2(\varphi)}. \qquad (31) \]