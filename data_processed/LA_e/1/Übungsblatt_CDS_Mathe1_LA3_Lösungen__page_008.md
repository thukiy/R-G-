<|ref|>sub_title<|/ref|><|det|>[[114, 81, 340, 100]]<|/det|>
## 6. Altmetallverwertung 

<|ref|>text<|/ref|><|det|>[[114, 98, 880, 170]]<|/det|>
Es sind 3 verschiedene Altmetalle (AM) vorhanden, die aus jeweils unterschiedlichen Anteilen von Eisen, Kupfer und Zinn bestehen. Es sollen 200 t einer neuen Legierung hergestellt werden, die aus 31 % Eisen, 46 % Kupfer und 23 % Zinn besteht. Die Zusammensetzung der Altmetalle ist folgendermassen gegeben: 

<|ref|>table<|/ref|><|det|>[[114, 164, 880, 235]]<|/det|>
<table><tr><td>Elemente</td><td>AM 1</td><td>AM 2</td><td>AM 3</td></tr><tr><td>Eisen</td><td>60 %</td><td>20 %</td><td>&lt; 0,2 %</td></tr><tr><td>Kupfer</td><td>30 %</td><td>40 %</td><td>70 %</td></tr><tr><td>Zinn</td><td>10 %</td><td>40 %</td><td>30 %</td></tr></table>

<|ref|>text<|/ref|><|det|>[[114, 233, 855, 268]]<|/det|>
Wieviel (Masse) von jedem der 3 Altmetalle muss eingeschmolzen werden, um die gewünschte neue Legierung herstellen zu können? 

<|ref|>text<|/ref|><|det|>[[114, 282, 872, 351]]<|/det|>
Es sind die Massen \(m_1\), \(m_2\) und \(m_3\) der Altmetalle zu berechnen, die eingeschmolzen werden müssen, um die neue Legierung herzustellen. Da der Eisengehalt des 3. Altmetalls sehr gering ist, können wir es vernachlässigen. Es ergibt sich folgendes lineares Gleichungssystem: 

<|ref|>equation<|/ref|><|det|>[[214, 350, 636, 450]]<|/det|>
\[ \begin{align*} 60\% \cdot m_1 + 20\% \cdot m_2 &= 31\% \cdot m = \frac{31}{100} \cdot 200t = 62t \\ 30\% \cdot m_1 + 40\% \cdot m_2 + 70\% \cdot m_3 &= 46\% \cdot m = \frac{46}{100} \cdot 200t = 92t \\ 10\% \cdot m_1 + 40\% \cdot m_2 + 30\% \cdot m_3 &= 23\% \cdot m = \frac{23}{100} \cdot 200t = 46t. \end{align*} \]

<|ref|>text<|/ref|><|det|>[[114, 448, 825, 483]]<|/det|>
Um keine Prozentschreibung nehmen zu müssen, mit 100 multiplizieren (1 % = 1/100): 

<|ref|>equation<|/ref|><|det|>[[120, 488, 498, 551]]<|/det|>
\[ \begin{cases} \text{I: } 60\% \cdot m_1 + 20\% \cdot m_2 = 6\% 200t \\ \text{II: } 30\% \cdot m_1 + 40\% \cdot m_2 + 7\% \cdot m_3 = 9\% 200t \\ \text{III: } 10\% \cdot m_1 + 40\% \cdot m_2 + 3\% \cdot m_3 = 4\% 600t. \end{cases} \]

<|ref|>text<|/ref|><|det|>[[120, 555, 552, 571]]<|/det|>
**Variante 1:** Wir wenden das GAUSS-Verfahren an. Es gilt 

<|ref|>equation<|/ref|><|det|>[[144, 577, 707, 630]]<|/det|>
\[ \begin{bmatrix} 60 & 20 & 0 & 6\% 200t \\ 30 & 40 & 70 & 9\% 200t \\ 10 & 40 & 30 & 4\% 600t \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & 4 & 3 & 460t \\ 3 & 1 & 0 & 310t \\ 3 & 4 & 7 & 920t \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & 4 & 4 & 460t \\ 0 & -11 & -9 & -1\% 070t \\ 0 & -8 & -2 & -460t \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[144, 638, 730, 702]]<|/det|>
\[ \begin{bmatrix} 1 & 4 & 3 & 460t \\ 0 & 4 & 1 & 230t \\ \frac{11}{4} & 0 & 11 & 9\% 070t \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & 4 & 2 & 460t \\ 0 & 4 & 1 & 230t \\ 0 & 0 & \frac{25}{4} & \frac{1750}{4}t \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & 4 & 3 \\ 0 & 4 & 1 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 4 & 3 \\ 0 & 4 & \frac{1}{4} \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} \]

<|ref|>text<|/ref|><|det|>[[142, 706, 437, 722]]<|/det|>
Durch Rückwärtseinsetzen erhalten wir 

<|ref|>equation<|/ref|><|det|>[[315, 725, 540, 741]]<|/det|>
\[ 1 \cdot m_3 = 70t \quad \Rightarrow \quad m_3 = 70t \]

<|ref|>equation<|/ref|><|det|>[[253, 743, 675, 763]]<|/det|>
\[ 4 \cdot m_2 + 1 \cdot m_3 = 230t \quad \Rightarrow \quad m_2 = \frac{1}{4} \cdot (230t - 70t) = 40t \]

<|ref|>equation<|/ref|><|det|>[[192, 765, 732, 783]]<|/det|>
\[ 1 \cdot m_1 + 4 \cdot m_2 + 3 \cdot m_3 = 460t \quad \Rightarrow \quad m_1 = 460t - 4 \cdot 40t - 3 \cdot 70t = 90t. \]