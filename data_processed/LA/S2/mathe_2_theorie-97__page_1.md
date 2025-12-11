<|ref|>text<|/ref|><|det|>[[25, 15, 333, 42]]<|/det|>
n × n Matrix gegeben. 

<|ref|>equation<|/ref|><|det|>[[30, 50, 567, 80]]<|/det|>
\[P_A(n) = \det(A - nI) \overset{!}{=} 0 \quad \text{für Eigenwerte}\]

<|ref|>text<|/ref|><|det|>[[50, 90, 880, 160]]<|/det|>
→ ist \(n_i\) eine \(K_i\)-fache Nullstelle von \(P_A(n)\), so heisst \(K_i\) die algebraische Vielfachheit Dimension von \(n_i\) 

<|ref|>text<|/ref|><|det|>[[50, 170, 940, 275]]<|/det|>
→ die Eigenvektoren \(\vec{E}_1 \dots \vec{E}_s \in \mathbb{R}^n\) zum Eigenwelt \(n_i\) spannen einen Unkeveltraum, den Eigenraum zu \(n_i\). Die Dimension
\(\dim(\ker(A - n_iI))\) heisst geometrische Vielfachheit / Dimension von \(n_i\). 

<|ref|>sub_title<|/ref|><|det|>[[25, 305, 240, 330]]<|/det|>
## Transformation : 

<|ref|>text<|/ref|><|det|>[[55, 342, 660, 373]]<|/det|>
L : \(\mathbb{R}^n \to \mathbb{R}^n\) sei lineare Abbildung mit Matrix \(K\) 

<|ref|>text<|/ref|><|det|>[[85, 382, 548, 410]]<|/det|>
bzw. Basis \((a_i)\). \(L(\vec{x}_a) = K \cdot \vec{x}_a\) 

<|ref|>text<|/ref|><|det|>[[85, 421, 904, 450]]<|/det|>
Bzw. Basis \((b_i)\) sei die Abbildungsmatrix \(M\). \(L(\vec{x}_b) = M \cdot \vec{x}_b\) 

<|ref|>text<|/ref|><|det|>[[45, 461, 712, 490]]<|/det|>
Es gibt eine Transformationmatrix \(T\), so dass gilt : 

<|ref|>equation<|/ref|><|det|>[[90, 499, 275, 525]]<|/det|>
\[W = T^{-1} \cdot M \cdot T\]

<|ref|>text<|/ref|><|det|>[[72, 539, 572, 564]]<|/det|>
→ \(W\) und \(M\) heissen ähnlich zueinander 

<|ref|>text<|/ref|><|det|>[[72, 577, 896, 644]]<|/det|>
→ die Eigenwerte \(n_i\) einschliesslich ihrer algebraischen Vielfachheit bleiben erhalten 

<|ref|>sub_title<|/ref|><|det|>[[25, 675, 310, 701]]<|/det|>
## Diagonalisierbarkeit : 

<|ref|>text<|/ref|><|det|>[[50, 715, 857, 741]]<|/det|>
n × n Matrix heisst diagonalisierbar, wenn es eine invertierbare 

<|ref|>text<|/ref|><|det|>[[55, 752, 431, 779]]<|/det|>
Matrix \(B\) gibt, so dass gilt : 

<|ref|>equation<|/ref|><|det|>[[85, 790, 555, 816]]<|/det|>
\[B^{-1} \cdot A \cdot B = D \quad (\text{Diagonalmatrix})\]