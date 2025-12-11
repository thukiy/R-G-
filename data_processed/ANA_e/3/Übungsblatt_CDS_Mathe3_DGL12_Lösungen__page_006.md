<|ref|>sub_title<|/ref|><|det|>[[114, 81, 404, 100]]<|/det|>
## 3. Klassifizierung von PDGLs 

<|ref|>text<|/ref|><|det|>[[114, 98, 872, 134]]<|/det|>
Geben Sie für die folgenden PDGLs die Ordnung und (falls möglich) den Typ an und ob die PDGL linear ist oder nicht: 

<|ref|>equation<|/ref|><|det|>[[114, 131, 610, 164]]<|/det|>
\[
a) \frac{\partial u(\vec{x}, t)}{\partial t} + \langle \vec{a}, \nabla_x (u(\vec{x}, t)) \rangle = 0 \quad (\text{Transportgleichung})
\]

<|ref|>equation<|/ref|><|det|>[[114, 163, 425, 184]]<|/det|>
\[
b) \triangle u = 0 \quad (\text{Laplace-Gleichung})
\]

<|ref|>equation<|/ref|><|det|>[[114, 182, 722, 205]]<|/det|>
\[
c) \triangle u + k^2 u = 0, \quad k \in \mathbb{C} \quad (\text{Helmholtz- oder Schwingungsgleichung})
\]

<|ref|>equation<|/ref|><|det|>[[114, 203, 465, 236]]<|/det|>
\[
d) \frac{\partial^2 u}{\partial t^2} - \triangle_x u = 0 \quad (\text{Wellengleichung})
\]

<|ref|>equation<|/ref|><|det|>[[114, 234, 675, 266]]<|/det|>
\[
e) \frac{\partial u}{\partial t} - \triangle_x u = 0 \quad (\text{Diffusions- oder Wärmeleitungsgleichung})
\]

<|ref|>equation<|/ref|><|det|>[[114, 263, 639, 297]]<|/det|>
\[
f) \frac{\partial u}{\partial t} + 6u \frac{\partial u}{\partial x} + \frac{\partial^3 u}{\partial x^3} = 0 \quad (\text{Korteweg-de-Vries-Gleichung})
\]

<|ref|>equation<|/ref|><|det|>[[114, 293, 400, 335]]<|/det|>
\[
g) \frac{\partial \vec{u}}{\partial t} + \langle \vec{u}, \nabla_x \rangle \vec{u} - \triangle_x \vec{u} = -\nabla_x p \\
\text{div } \vec{u} = 0 \quad \text{(Navier-Stokes-Gleichungen).}
\]

<|ref|>equation<|/ref|><|det|>[[139, 351, 880, 401]]<|/det|>
\[
a) \text{ Ordnung: } 1 \quad \text{—} \quad \text{—} \quad \text{—} \quad \text{Typenstellung möglich} \\
\text{PDE ist linear}
\]

<|ref|>equation<|/ref|><|det|>[[129, 415, 636, 576]]<|/det|>
\[
b) \text{ Ordnung: } 2 \\
\text{PDE ist linear} \\
\text{mit } \vec{x} = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} : \quad \frac{\partial^2 u}{\partial x_1^2} + \frac{\partial^2 u}{\partial x_2^2} = 0 \\
A(\vec{x}^2) = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
\]

<|ref|>equation<|/ref|><|det|>[[179, 580, 777, 650]]<|/det|>
\[
\text{Eigentwiete bestimmen:} \\
\left| \begin{pmatrix} 1-\lambda & 0 \\ 0 & 1-\lambda \end{pmatrix} \right| = (\lambda-\lambda)^2 = 0 \quad \Rightarrow \lambda = 1
\]

<|ref|>equation<|/ref|><|det|>[[164, 678, 500, 709]]<|/det|>
\[
\Rightarrow \text{PDE ist elliptisch}
\]

<|ref|>equation<|/ref|><|det|>[[114, 713, 880, 835]]<|/det|>
\[
c) \text{ Ordnung: } 2 \\
\text{PDE ist linear} \\
\Rightarrow \text{PDE ist linear} \\
\text{mit } \vec{x} = \begin{pmatrix}
x_1 \\
x_2
\end{pmatrix} : \quad \frac{\partial^2 u}{\partial x_1^2}
+ \frac{\partial^2 u}{\partial x_2^2} = 0 \\
\text{PDE elliptisch}
\]