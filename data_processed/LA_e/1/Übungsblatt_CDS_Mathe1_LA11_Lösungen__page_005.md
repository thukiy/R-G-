<|ref|>text<|/ref|><|det|>[[118, 81, 707, 101]]<|/det|>
Berechnung des Schnittpunktes \(S\) mit dem Ortsvektor \(\vec{r}_S = \vec{r}(\lambda_1) = \vec{r}(\lambda_2)\): 

<|ref|>equation<|/ref|><|det|>[[118, 108, 810, 170]]<|/det|>
\[ \begin{pmatrix} 1 + 2\lambda_1 \\ 2 \\ 5\lambda_1 \end{pmatrix} = \begin{pmatrix} 6 + \lambda_2 \\ -2\lambda_2 \\ 13 + 3\lambda_2 \end{pmatrix} \Rightarrow \begin{pmatrix} 2\lambda_1 - \lambda_2 = 5 \\ 2\lambda_2 = -2 \\ 5\lambda_1 - 3\lambda_2 = 13 \end{pmatrix} \Rightarrow \lambda_1 = 2; \lambda_2 = -1 \]

<|ref|>equation<|/ref|><|det|>[[118, 174, 643, 234]]<|/det|>
\[ \vec{r}_S = \vec{r}(\lambda_1 = 2) = \vec{r}(\lambda_2 = -1) = \begin{pmatrix} 5 \\ 2 \\ 10 \end{pmatrix} \Rightarrow S = (5; 2; 10) \]

<|ref|>equation<|/ref|><|det|>[[118, 239, 723, 279]]<|/det|>
\[ \text{Schnittwinkel: } \varphi = \arccos \left( \frac{\vec{a}_1 \cdot \vec{a}_2}{|\vec{a}_1| \cdot |\vec{a}_2|} \right) = \arccos \left( \frac{17}{\sqrt{29} \cdot \sqrt{14}} \right) = 32,47^\circ \]

<|ref|>sub_title<|/ref|><|det|>[[115, 294, 496, 312]]<|/det|>
## 6. Abstand Gerade - Koordinatenachse 

<|ref|>text<|/ref|><|det|>[[115, 310, 880, 346]]<|/det|>
Die in der x-y-Ebene verlaufende Gerade \(g_1\) schneidet die beiden Koordinatenachsen jeweils bei 3. Welchen Abstand besitzt diese Gerade von der z-Achse? 

<|ref|>text<|/ref|><|det|>[[118, 362, 816, 381]]<|/det|>
Gleichung der Geraden durch die Achsenschnittpunkte \(P_1 = (3; 0; 0)\) und \(P_2 = (0; 3; 0)\): 

<|ref|>equation<|/ref|><|det|>[[118, 384, 654, 444]]<|/det|>
\[ g_1: \vec{r}(\lambda_1) = \vec{r}_1 + \lambda_1 \overrightarrow{P_1 P_2} = \vec{r}_1 + \lambda_1 \vec{a}_1 = \begin{pmatrix} 3 \\ 0 \\ 0 \end{pmatrix} + \lambda_1 \begin{pmatrix} -3 \\ 3 \\ 0 \end{pmatrix} \]

<|ref|>text<|/ref|><|det|>[[118, 456, 630, 475]]<|/det|>
Gleichung der z-Achse durch \(P_3 = (0; 0; 0)\) und \(P_4 = (0; 0; 1)\): 

<|ref|>equation<|/ref|><|det|>[[118, 481, 640, 542]]<|/det|>
\[ g_2: \vec{r}(\lambda_2) = \vec{r}_3 + \lambda_2 \overrightarrow{P_3 P_4} = \vec{r}_3 + \lambda_2 \vec{a}_2 = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} + \lambda_2 \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} \]

<|ref|>text<|/ref|><|det|>[[115, 542, 825, 579]]<|/det|>
Die Geraden sind windschief, da sie weder parallel (\(\vec{a}_1 \times \vec{a}_2 \neq 0\)) sind noch einen Schnittpunkt haben. 

<|ref|>equation<|/ref|><|det|>[[123, 577, 636, 615]]<|/det|>
\[ \text{Abstand der Geraden: } d = \frac{|\vec{a}_1 \vec{a}_2 (\vec{r}_3 - \vec{r}_1)|}{|\vec{a}_1 \times \vec{a}_2|} = \frac{| -9 |}{\sqrt{18}} = 2,12 \]