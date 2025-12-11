<|ref|>text<|/ref|><|det|>[[24, 15, 597, 55]]<|/det|>
Bsp: 
\[
A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} \quad 2 \text{ Permutationen}
\]

<|ref|>equation<|/ref|><|det|>[[163, 68, 567, 95]]<|/det|>
\[
\det(A) = + a_{11} \cdot a_{22} - a_{12} \cdot a_{21}
\]

<|ref|>equation<|/ref|><|det|>[[163, 110, 545, 155]]<|/det|>
\[
\begin{pmatrix}
1 & 2 \\
1 & 2
\end{pmatrix}
\begin{pmatrix}
1 & 2 \\
2 & 1
\end{pmatrix}
\]

<|ref|>text<|/ref|><|det|>[[163, 188, 710, 250]]<|/det|>
\[
A = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} \quad 6 \text{ Permutationen}
\]

<|ref|>equation<|/ref|><|det|>[[163, 264, 797, 336]]<|/det|>
\[
\begin{align*}
\det(A) &= + a_{11} a_{22} a_{33} + a_{12} a_{23} a_{31} + a_{13} a_{21} a_{32} \\
&\quad - a_{13} a_{22} a_{31} - a_{11} a_{23} a_{32} - a_{12} a_{21} a_{33}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[50, 364, 480, 391]]<|/det|>
→ det(0) = 0 und det(11) = 1 

<|ref|>text<|/ref|><|det|>[[50, 404, 880, 470]]<|/det|>
→ Diagonalematrix D : nun Einhänge in Hauptdiagonale und somit
det(D) = λ₁ · ... · λₙ (λ₁ sind Einhänge in Hauptdiagonale) 

<|ref|>text<|/ref|><|det|>[[50, 483, 680, 510]]<|/det|>
→ wenn oben bzw. unten Dreiecksmatrix vorliegt : 

<|ref|>equation<|/ref|><|det|>[[103, 522, 450, 547]]<|/det|>
\[
\det(A) = a_{11} \cdot a_{22} \cdot \ldots \cdot a_{nn}
\]

<|ref|>text<|/ref|><|det|>[[24, 579, 252, 606]]<|/det|>
Regel von Sarrus 

<|ref|>text<|/ref|><|det|>[[50, 618, 420, 645]]<|/det|>
→ nun für 3 x 3 Matrix gültig 

<|ref|>equation<|/ref|><|det|>[[90, 656, 410, 737]]<|/det|>
\[
\begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{pmatrix}
\begin{pmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22} \\
a_{31} & a_{32}
\end{pmatrix}
\begin{pmatrix}
a_{11} & a_{12} \\
a_{22} & a_{22} \\
a_{32} & a_{32}
\end{pmatrix}
\begin{pmatrix}
a_{11} & a_{22} \\
a_{21} & a_{22} \\
a_{31} & a_{22}
\end{pmatrix}
\begin{pmatrix}
a_{11} & a_{12} \\
a_{12} & a_{12} \\
a_{12} & a_{12}
\end{pmatrix}
\begin{pmatrix}
a_{11} & a_{12} \\
a_{11} & a_{12} \\
a_{11} & a_{12}
\end{pmatrix}
\begin{pmatrix}
a_{11} & a_{22} \\
a_{11} & a_{22} \\
a_{11} & a_{22}
\end{pmatrix}
\begin{pmatrix}
a_{11} & a_{22} \\
a_{12} & a_{22} \\
a_{12} & a_{22}
\end{pmatrix}
\begin{pmatrix}
a_{11} & a_{11} \\
a_{11} & a_{11} \\
a_{11} & a_{11}
\end{pmatrix}
\begin{pmatrix}
a_{11} & a_{11} \\
a_{12} & a_{11} \\
a_{12} & a_{11}
\end{pmatrix}
\begin{pmatrix}
a_{11} & a_{22} \\
a_{22} & a_{22} \\
a_{22} & a_{22}
\end{pmatrix}
\begin{pmatrix}
a_{11} & a_{21} \\
a_{11} & a_{21} \\
a_{11} & a_{21}
\end{pmatrix}
\begin{pmatrix}
a_{11} & a_{21} \\
a_{12} & a_{21} \\
a_{12} & a_{21}
\end{pmatrix}
\begin{pmatrix}
a_{11} & a_{22} \\
a_{31} & a_{22} \\
a_{31} & a_{22}
\end{pmatrix}
\end{pmatrix}
\begin{pmatrix}
a_{11} & a_{22} \\
a_{32} & a_{22} \\
a_{32} & a_{22}
\end{pmatrix}
\begin{pmatrix}
a_{11} & a_{32} \\
a_{32} & a_{32} \\
a_{32} & a_{32}
\end{pmatrix}
\begin{pmatrix}
a_{22} & a_{22} \\
a_{22} & a_{22} \\
a_{32} & a_{22}
\end{pmatrix}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{32}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{22}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{11}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{12}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{21}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{31}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{33}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{23}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{13}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{14}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{24}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{16}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{26}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{28}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{30}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{40}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{50}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{60}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{70}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{80}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{90}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{100}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{110}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{120}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{130}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{140}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{150}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{160}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{170}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{180}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{190}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{200}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{210}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{220}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{230}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{240}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{250}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{260}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{270}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{280}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{290}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{300}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{310}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{320}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{330}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{340}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{350}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{360}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{370}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{380}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{390}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{400}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{410}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{420}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{430}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{440}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{450}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{460}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{470}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{480}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{490}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{500}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{510}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{520}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{530}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{540}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{550}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{560}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{570}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{580}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{590}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{600}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{610}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{620}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{630}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{640}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{650}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{660}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{670}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{680}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{690}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{700}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{710}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{720}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{730}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{740}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{750}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{760}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{770}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{780}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{790}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{800}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{810}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{820}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{830}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{840}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{850}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{860}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{870}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{880}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{890}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{900}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{910}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{920}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{930}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{940}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{950}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{960}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{970}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{980}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{990}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{1,000}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{2,000}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
b_{000}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
b_000
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
b_100
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
b_200
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
b_300
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
b_400
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
b_500
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
b_600
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
b_700
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
b_800
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
b_900
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
b_{0000}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
b_{1000}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
b_2000
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
b_3,000
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
b_{4000}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
b-5000
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
b-6000
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
b+5000
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\
a_{0000}
\end{pmatrix}
\begin{pmatrix}
a_{11} \\
a_{22} \\