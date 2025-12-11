<|ref|>text<|/ref|><|det|>[[20, 15, 744, 50]]<|/det|>
Bsp: \(a_{11}(\vec{x}) = 1\), \(a_{12}(\vec{x}) = a_{21}(\vec{x}) = x_1 x_2\), \(a_{22}(\vec{x}) = x_2\) 

<|ref|>equation<|/ref|><|det|>[[110, 57, 255, 85]]<|/det|>
\(b_1 = b_2 = 0\)

<|ref|>equation<|/ref|><|det|>[[110, 95, 395, 124]]<|/det|>
\(c(\vec{x}) = x_1 x_2\), \(g = 0\)

<|ref|>equation<|/ref|><|det|>[[110, 147, 672, 186]]<|/det|>
\[\frac{\partial^2 u}{\partial x_1^2} + 2x_1 x_2 \frac{\partial^2 u}{\partial x_1 \partial x_2} + x_2^2 \frac{\partial^2 u}{\partial x_2^2} + x_1^2 x_2^2 \cdot u = 0\]

<|ref|>text<|/ref|><|det|>[[40, 199, 830, 241]]<|/det|>
→ \(\sum_{i,j=1}^n a_{ij} \frac{\partial^2 u}{\partial x_i \partial x_j}\) wird Hauptkrei der PDGL 2. Ordnung genannt 

<|ref|>text<|/ref|><|det|>[[110, 243, 886, 310]]<|/det|>
↪ verschiedene Typen von PDGL werden nun über Eigenschaften
der Matrix A definiert 

<|ref|>text<|/ref|><|det|>[[20, 340, 666, 370]]<|/det|>
zur Erinnerung: Eigenwert \(n\) einer \(n \times n\) Matrix 

<|ref|>equation<|/ref|><|det|>[[255, 373, 666, 485]]<|/det|>
\[\begin{align*}
&\to \text{es gibt Vektoren } \vec{E} \in \mathbb{R}^n \text{ mit } \\
&A \cdot \vec{E} = n \cdot \vec{E} \\
&(A - n \cdot I) \cdot \vec{E} = 0
\end{align*}\]

<|ref|>text<|/ref|><|det|>[[20, 511, 593, 540]]<|/det|>
Def: Eine lineare PDGL 2. Ordnung heisst 

<|ref|>text<|/ref|><|det|>[[50, 547, 930, 614]]<|/det|>
a) elliptisch, wenn Matrix A omaechnisch positive oder negative
eigenweite besitzt 

<|ref|>text<|/ref|><|det|>[[50, 621, 911, 693]]<|/det|>
b) parabolisch, wenn Matrix A 0 als einfachen Eigenwert entweder
nur positiv oder nur negativ sind 

<|ref|>text<|/ref|><|det|>[[50, 700, 904, 770]]<|/det|>
c) hyperbolisch, wenn Matrix A genau einen einfachen negativen
eigenweite und sonst nur positive Eigenweite besitzt oder umgelehrt 

<|ref|>text<|/ref|><|det|>[[20, 797, 556, 828]]<|/det|>
Bsp: \((1-x^2-y^2) \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} - (x^2+y^2) u = 0\) 

<|ref|>equation<|/ref|><|det|>[[110, 835, 290, 864]]<|/det|>
\(a_{11} = 1 - x^2 - y^2\)

<|ref|>equation<|/ref|><|det|>[[110, 872, 955, 901]]<|/det|>
\(a_{12} = a_{21} = 0\) keine "gemischten" Ableitungen 2. Ordnung vorhanden

<|ref|>equation<|/ref|><|det|>[[110, 910, 201, 937]]<|/det|>
\(a_{22} = 1\)

<|ref|>equation<|/ref|><|det|>[[110, 944, 360, 991]]<|/det|>
\(A = \begin{pmatrix} 1 - x^2 - y^2 & 0 \\ 0 & 1 \end{pmatrix}\)