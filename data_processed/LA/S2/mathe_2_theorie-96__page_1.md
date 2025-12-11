<|ref|>sub_title<|/ref|><|det|>[[20, 12, 450, 42]]<|/det|>
## Kein und Bild einer Abbildung : 

<|ref|>text<|/ref|><|det|>[[50, 52, 470, 80]]<|/det|>
L : V → W sei lineare Abbildung 

<|ref|>text<|/ref|><|det|>[[50, 87, 911, 160]]<|/det|>
Die Menge \(\ker(L) = \{ \vec{v} \in L \mid L(\vec{v}) = 0 \}\) heisst Kein und die Menge \(\img(L) = L(V) = \{ L(\vec{v}) \in W \mid \vec{v} \in V \}\) das Bild des Abbildung L 

<|ref|>text<|/ref|><|det|>[[44, 168, 440, 197]]<|/det|>
→ \(\ker(L) \in V\), \(\img(L) \in W\) 

<|ref|>text<|/ref|><|det|>[[44, 206, 673, 238]]<|/det|>
→ Defekt des Abbildungsmatrix : \(\dim(\ker(L))\) 

<|ref|>text<|/ref|><|det|>[[100, 243, 675, 280]]<|/det|>
Rang " " : \(\dim(\img(L))\) 

<|ref|>text<|/ref|><|det|>[[44, 286, 888, 355]]<|/det|>
→ \(\dim(\ker(L)) = 0\) : Spaltenvektoren des Abbildungsmatrix sind linear unabhängig 

<|ref|>sub_title<|/ref|><|det|>[[20, 384, 718, 414]]<|/det|>
## Dimensionssatz : \(\dim(V) = \dim(\ker(L)) + \dim(\img(L))\) 

<|ref|>sub_title<|/ref|><|det|>[[20, 442, 455, 471]]<|/det|>
## Bild einer Abbildung bestimmen : 

<|ref|>text<|/ref|><|det|>[[50, 479, 508, 508]]<|/det|>
\(L(\vec{x}) = A \cdot \vec{x} = \vec{w}\), \(\vec{x} \in V\), \(\vec{w} \in W\) 

<|ref|>text<|/ref|><|det|>[[44, 520, 923, 587]]<|/det|>
→ es stellt sich die Frage nach linearer Abhängigkeit / Unabhängigkeit der Spaltenvektoren von A 

<|ref|>text<|/ref|><|det|>[[44, 595, 955, 825]]<|/det|>
\(\begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{pmatrix}\) um herauszufinden, ob ganze Spalten dem Nullevolle entsprechen :

- \(A^T\) bilden
- Gauß-Verfahren, um Dreiecksmatrix zu erhalten
- Rückharmonpioneren
- Spalten ≠ 0 : entsprechen \(\img(L)\)