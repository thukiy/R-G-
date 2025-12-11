<|ref|>text<|/ref|><|det|>[[50, 15, 360, 42]]<|/det|>
Umschreiben von (*): 

<|ref|>equation<|/ref|><|det|>[[75, 46, 456, 90]]<|/det|>
\[ \frac{\partial u_i}{\partial t} + \sum_{i=1}^{3} u_i \frac{\partial u_i}{\partial x_i} - \sum_{i=1}^{3} \frac{\partial^2 u_i}{\partial x_i^2} = -\frac{\partial p}{\partial x_i} \]

<|ref|>text<|/ref|><|det|>[[115, 95, 410, 120]]<|/det|>
j-te reelle mit \(j = 1 \dots 3\) 

<|ref|>text<|/ref|><|det|>[[25, 170, 358, 195]]<|/det|>
Def: Eine PDGL der Form 

<|ref|>equation<|/ref|><|det|>[[50, 199, 475, 237]]<|/det|>
\[ \vec{F}(\vec{x}, u(\vec{x}), \frac{\partial u}{\partial x_1}, \dots, \frac{\partial u}{\partial x_n}) = \vec{q}(\vec{x}) \]

<|ref|>text<|/ref|><|det|>[[100, 245, 950, 310]]<|/det|>
heisst linear, wenn \(\vec{F}\) bzgl. die Funktion \(u\) linear ist. D.h. für alle differenzierbaren Funktionen \(u\), \(w: D \subseteq \mathbb{R}^n \to \mathbb{R}\) und \(n, \mu \in \mathbb{R}\) gilt: 

<|ref|>equation<|/ref|><|det|>[[50, 312, 644, 380]]<|/det|>
\[ \vec{F}(\vec{x}, (n\mu + nw), \frac{\partial(n\mu + nw)}{\partial x_1}, \dots, \frac{\partial(n\mu + nw)}{\partial x_n}) = n\vec{F}(\vec{x}, u, \frac{\partial u}{\partial x_1}, \dots, \frac{\partial u}{ \partial x_n}) + \mu\vec{F}(\vec{x}, w, \frac{\partial w}{\partial x_1}, \dots, \frac{\partial w}{ \partial x_n}) \]

<|ref|>text<|/ref|><|det|>[[100, 396, 820, 424]]<|/det|>
PDGL heisst homogen, wenn \(\vec{q}(\vec{x}) = 0\), sonst inhomogen 

<|ref|>text<|/ref|><|det|>[[25, 456, 833, 483]]<|/det|>
Bsp: *lineare PDGL 1. Ordnung haben typischerweise die Gestalt* 

<|ref|>equation<|/ref|><|det|>[[100, 485, 560, 650]]<|/det|>
\[ \begin{aligned} \sum_{j=1}^{n} a_{ij}(\vec{x}) \frac{\partial u}{\partial x_j} + b(\vec{x}) \cdot u(\vec{x}) &= q(\vec{x}) \\ a_{ij}, b, q: \mathbb{R}^n \to \mathbb{R} \\ \text{mit } \vec{a}(\vec{x}) &= \begin{pmatrix} a_{ij}(\vec{x}) \\ \dot{a}_{ij}(\vec{x}) \end{pmatrix} \end{aligned} \]

<|ref|>text<|/ref|><|det|>[[100, 656, 470, 682]]<|/det|>
→ es ergibt sich 

<|ref|>equation<|/ref|><|det|>[[175, 688, 490, 712]]<|/det|>
\[ \langle \vec{a}(\vec{x}), \nabla u \rangle + b \cdot u = q \]

<|ref|>text<|/ref|><|det|>[[100, 704, 655, 730]]<|/det|>
*lineare PDGL 2. Ordnung haben die Form* 

<|ref|>equation<|/ref|><|det|>[[100, 733, 600, 802]]<|/det|>
\[ \sum_{i,j=1}^{n} a_{ij} \frac{\partial^2 u}{\partial x_i \partial x_j} + \sum_{j=1}^{n} b_i \frac{\partial u}{\partial x_j} + c \cdot u = q \]

<|ref|>text<|/ref|><|det|>[[100, 802, 668, 828]]<|/det|>
\(a_{ij}, b, c: D \subseteq \mathbb{R}^n \to \mathbb{R}\) Koefizienten 

<|ref|>text<|/ref|><|det|>[[100, 830, 680, 857]]<|/det|>
\(q: D \subseteq \mathbb{R}^n \to \mathbb{R}\) Inhomogenität 

<|ref|>text<|/ref|><|det|>[[100, 863, 666, 890]]<|/det|>
→ \(a_{ij}\) bilden Matrix \(A(\vec{x}) = (a_{ij}(\vec{x}))_{i,j=1\dots n}\) 

<|ref|>text<|/ref|><|det|>[[100, 896, 545, 922]]<|/det|>
→ \(A\) ist üblicherweise symmetrisch