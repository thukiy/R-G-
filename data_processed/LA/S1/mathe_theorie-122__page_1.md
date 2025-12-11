<|ref|>sub_title<|/ref|><|det|>[[40, 10, 655, 66]]<|/det|>
Orthogonale Projektion 

<|ref|>equation<|/ref|><|det|>[[75, 85, 280, 118]]<|/det|>
\[ \vec{v}, \vec{w} \in \mathbb{R}^n \]

<|ref|>text<|/ref|><|det|>[[75, 125, 696, 159]]<|/det|>
Vektor \(\vec{v}\) orthogonale auf Vektor \(\vec{w}\) projazieren 

<|ref|>equation<|/ref|><|det|>[[150, 175, 375, 300]]<|/det|>
\[ \begin{tikzcd}
 & \vec{v} \\
 & \downarrow \\
 \alpha & \rightarrow \vec{w} \\
 & \downarrow \\
 & \vec{v} \\
 & \downarrow \\
 & \vec{w} \\
 & \downarrow \\
 & \vec{v} \\
 & \downarrow \\
 \text{|\vec{v}|} \cdot \cos \alpha & \rightarrow \vec{w} \\
 & \downarrow \\
 & \vec{w} \\
 & \downarrow \\
 & \vec{w} \\
 & \downarrow \\
 \text{|\vec{w}|} & = & \text{|\vec{v}|} \cdot \cos \alpha = \frac{\langle \vec{v}, \vec{w} \rangle}{|\vec{w}|}
 \end{tikzcd} \]

<|ref|>equation<|/ref|><|det|>[[433, 290, 940, 380]]<|/det|>
\[ \langle \vec{v}, \vec{w} \rangle = |\vec{v}| \cdot |\vec{w}| \cdot \cos \alpha = \frac{\langle \vec{v}, \vec{w} | \rangle}{|\vec{w}|} \]

<|ref|>text<|/ref|><|det|>[[156, 398, 945, 550]]<|/det|>
bisher: dünge von \(\vec{v}\), bekannt, es fehlt noch Richtung \(\rightarrow\) da \(\vec{v}, \vec{w}\) || \(\vec{w}\), können wir die dünge mit der Richtung von \(\vec{w}\) oder dünge 1 multiplizieren und erhalten dann \(\vec{v}\),

\[\vec{v} \rightarrow \text{wir brauchen } \vec{w}\]

<|ref|>equation<|/ref|><|det|>[[150, 610, 610, 725]]<|/det|>
\[ \begin{aligned} \vec{v}_n &= |\vec{v}_n| \cdot \vec{w} = |\vec{v}| \cdot \cos \alpha \cdot \vec{w} \\ &= \frac{\langle \vec{v}, \vec{w} \rangle}{|\vec{w}|} \cdot \vec{w} = \frac{\langle \vec{v}, \vec{w} \rangle}{|\vec{w} |} \cdot \frac{\vec{w}}{|\vec{w}|} \\ &= \frac{\langle \vec{v}, \vec{w} \rangle}{\langle \vec{w}, \vec{w} \rangle} \cdot \vec{w} \end{aligned} \]

<|ref|>equation<|/ref|><|det|>[[150, 745, 339, 780]]<|/det|>
\[ \vec{v}_1 = \vec{v} - \vec{v}_n \]

<|ref|>text<|/ref|><|det|>[[150, 808, 733, 844]]<|/det|>
→ Anwendung: Kräftezeugung in Physik 

<|ref|>text<|/ref|><|det|>[[150, 848, 938, 955]]<|/det|>
→ für weit des Skalaprodukts sind nun die parallelen Anteile des beiden Vektoren relevant
(Orthopartialität des Skalaprodukts)