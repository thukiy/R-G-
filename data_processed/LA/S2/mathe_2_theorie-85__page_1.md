<|ref|>sub_title<|/ref|><|det|>[[20, 12, 515, 42]]<|/det|>
Charakterisierung von Permutationen : 

<|ref|>text<|/ref|><|det|>[[50, 52, 371, 78]]<|/det|>
Inversionzahl / Fehlstand 

<|ref|>equation<|/ref|><|det|>[[55, 85, 860, 122]]<|/det|>
\[
\zeta(p) = \text{inv}(p) = \{\zeta(i, j) \in \{1 \ldots n\}^2 \mid i < j \text{ und } p(i) > p(j)\}
\]

<|ref|>text<|/ref|><|det|>[[20, 149, 99, 175]]<|/det|>
Bsp : 

<|ref|>table<|/ref|><|det|>[[130, 146, 640, 273]]<|/det|>
<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>3</td><td>5</td><td>1</td><td>2</td><td>4</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr></table>

<|ref|>equation<|/ref|><|det|>[[130, 240, 640, 270]]<|/det|>
\[
\text{inv}(p) = \{(1,3), (1,4), (2,3), (2,4), (2,5)\}
\]

<|ref|>text<|/ref|><|det|>[[150, 245, 370, 271]]<|/det|>
→ 5 Fehlstände 

<|ref|>sub_title<|/ref|><|det|>[[20, 304, 405, 330]]<|/det|>
- Vorzeichen / Signum / Parität 

<|ref|>equation<|/ref|><|det|>[[65, 336, 400, 367]]<|/det|>
\[
\delta(p) = (-1)^{\zeta(p)} = (-1)^{\text{inv}(p)}
\]

<|ref|>text<|/ref|><|det|>[[80, 381, 720, 408]]<|/det|>
↔ kann +1 (für gerade Anzahl Fehlstände) oder 

<|ref|>text<|/ref|><|det|>[[194, 415, 808, 444]]<|/det|>
- 1 (" ungeaade " " ) annehmen 

<|ref|>sub_title<|/ref|><|det|>[[20, 479, 270, 505]]<|/det|>
Def : Determinante 

<|ref|>text<|/ref|><|det|>[[108, 519, 830, 550]]<|/det|>
A sei \(n \times n\) Matrix. Die Determinante ist gegeben durch 

<|ref|>equation<|/ref|><|det|>[[140, 556, 714, 599]]<|/det|>
\[
\text{det}(A) = \sum_{p \in S_n} \delta(p) \cdot a_{1p(1)} \cdot a_{2p(2)} \cdot \ldots \cdot a_{np(n)}
\]

<|ref|>text<|/ref|><|det|>[[16, 616, 815, 644]]<|/det|>
(1) → n Elemente auswählen : aus jede Spalte und ziele eines 

<|ref|>text<|/ref|><|det|>[[16, 656, 515, 683]]<|/det|>
(2) → diese n Elemente multiplizieren 

<|ref|>text<|/ref|><|det|>[[16, 695, 940, 760]]<|/det|>
(3) → Vorzeichen für Permutation für diese Elemente bestimmen und mit
Wert aus (2) multiplizieren 

<|ref|>text<|/ref|><|det|>[[16, 772, 861, 838]]<|/det|>
(4) → für jede Permutation wiederholen wir Schritte (1) - (3) und
ausschliessend addieren