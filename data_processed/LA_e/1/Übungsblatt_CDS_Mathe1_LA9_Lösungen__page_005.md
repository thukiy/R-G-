<|ref|>text<|/ref|><|det|>[[115, 81, 420, 99]]<|/det|>
Mit Hilfe von g) und d) ergibt sich: 

<|ref|>equation<|/ref|><|det|>[[130, 102, 437, 119]]<|/det|>
\[ \langle \mathbf{v}, \mathbf{v} \times \mathbf{w} \rangle = \langle \mathbf{v} \times \mathbf{v}, \mathbf{w} \rangle = \langle 0, \mathbf{w} \rangle = 0 \]

<|ref|>equation<|/ref|><|det|>[[123, 125, 552, 143]]<|/det|>
\[ \langle \mathbf{w}, \mathbf{v} \times \mathbf{w} \rangle = \langle \mathbf{v}, \mathbf{w} \times \mathbf{w} \rangle = \langle \mathbf{v}, \mathbf{w}, \mathbf{w} \rangle = \langle \mathbf{v}, 0 \rangle = 0. \]

<|ref|>text<|/ref|><|det|>[[115, 147, 210, 163]]<|/det|>
Somit gilt: 

<|ref|>equation<|/ref|><|det|>[[117, 165, 396, 184]]<|/det|>
\[ \frac{\mathbf{v} \perp (\mathbf{v} \times \mathbf{w})}{\mathbf{v} \perp (\mathbf{v} \times \mathbf{w})} \quad \text{und} \quad \frac{\mathbf{w} \perp (\mathbf{v} \times \mathbf{w})}{\mathbf{w} \perp (\mathbf{v} \times \mathbf{w})}. \]

<|ref|>text<|/ref|><|det|>[[115, 189, 135, 205]]<|/det|>
i) 

<|ref|>equation<|/ref|><|det|>[[120, 205, 780, 256]]<|/det|>
\[ G = \mathbf{u} \times (\mathbf{v} \times \mathbf{w}) = \begin{bmatrix} u_1 \\ u_2 \\ u_3 \end{bmatrix} \times \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix} \times \begin{bmatrix} w_1 \\ w_2 \\ w_3 \end{bmatrix} = \begin{bmatrix} u_1 \\ u_2 \\ u_3 \end{bmatrix}\times \begin{bmatrix} v_2 \cdot w_3 - v_3 \cdot w_2 \\ v_3 \cdot w_1 - v_1 \cdot w_3 \\ v_1 \cdot w_2 - v_2 \cdot w_1 \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[137, 262, 540, 310]]<|/det|>
\[ = \begin{bmatrix} u_2 \cdot (v_1 \cdot w_2 - v_2 \cdot w_1) - u_3 \cdot (v_3 \cdot w_1 - v_1 \cdot w_3) \\ u_3 \cdot (v_2 \cdot w_3 - v_3 \cdot w_2) - u_1 \cdot (v_1 \cdot w_2 - v_2 \cdot w_2) \\ u_1 \cdot (v_3 \cdot w_1 - v_1 \cdot w_1) - u_2 \cdot (v_2 \cdot w_3 - v_3 \cdot w_3) \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[137, 316, 575, 364]]<|/det|>
\[ = \begin{bmatrix} u_2 \cdot v_1 \cdot w_2 - u_2 \cdot v_2 \cdot w_1 - u_3 \cdot v_3 \cdot w_1 + u_3 \cdot v_1 \cdot w_3 \\ u_3 \cdot v_2 \cdot w_3 - u_3 \cdot v_3 \cdot w_2 - u_1 \cdot v_1 \cdot w_2 + u_1 \cdot v_2 \cdot w_1 \\ u_1 \cdot v_3 \cdot w_1 - u_1 \cdot v_1 \cdot w_3 - u_2 \cdot v_2 \cdot w_3 + u_2 \cdot v_3 \cdot w_2 \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[137, 369, 550, 417]]<|/det|>
\[ = \begin{bmatrix} u_2 \cdot v_1 \cdot \mathbf{w}_2 + u_3 \cdot v_1 \cdot \mathbf{w}_3 - u_2 \cdot v_2 \cdot \mathbf{w}_1 - u_3 \cdot v_3 \cdot \mathbf{w}_1 \\ u_1 \cdot v_2 \cdot \mathbf{w}_1 + u_3 \cdot v_2 \cdot \mathbf{w}_3 - u_1 \cdot v_1 \cdot \mathbf{w}_2 - u_3 \cdot v_3 \cdot \mathbf{w}_2 \\ u_1 \cdot v_3 \cdot \mathbf{w}_1 + u_2 \cdot v_3 \cdot \mathbf{w}_2 - u_1 \cdot v_1 \cdot \mathbf{w}_3 - u_2 \cdot v_{2} \cdot \mathbf{w}_3 \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[137, 423, 760, 472]]<|/det|>
\[ = \begin{bmatrix} u_1 \cdot v_1 \cdot \mathbf{w}_1 + u_2 \cdot v_1 \cdot \mathbf{w}_2 + u_3\cdot v_1 \cdot \mathbf{w}_3 - u_1 \cdot v_1 \cdot \dot{\mathbf{w}}_1 - u_2 \cdot v_2 \cdot \dot{\mathbf{w}}_1 - u_3 \cdot v_3 \cdot \dot{\mathbf{w}}_1 \\ u_1 \cdot v_2 \cdot \dot{\mathbf{w}}_1 + u_2 \cdot v_2 \cdot \dot{\mathbf{w}}_2 + u_3 \cdot v_2 \cdot \dot{\mathbf{w}}_3 - u_1 \cdot v_1 \cdot \dot{\mathbf{w}}_2 - u_2 \cdot v_2 \cdot \dot{\mathbf{w}}_2 - u_3 \cdot v_3 \cdot \dot{\mathbf{w}}_2 \\ u_1 \cdot v_3 \cdot \dot{\mathbf{w}}_1 + u_2 \cdot v_3 \cdot \dot{\mathbf{w}}_2 + u_3 \cdot v_3 \cdot \dot{\mathbf{w}}_3 - u_1 \cdot v_1\dot{\mathbf{w}}_3 - u_2 \cdot v_2 \cdot \dot{\mathbf{w}}_3 - u_3 \cdot v_3 \cdot \dot{\mathbf{w}}_3 \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[137, 478, 660, 526]]<|/det|>
\[ = \begin{bmatrix} (u_1 \cdot w_1 + u_2 \cdot w_2 + u_3 \cdot w_3) \cdot v_1 - (u_1 \cdot v_1 + u_2 \cdot v_2 + u_3 \cdot v_3) \cdot w_1 \\ (u_1 \cdot w_1 + u_2 \cdot w_2 + \dot{u}_3 \cdot w_3) \cdot v_2 - (u_1 \cdot v_1 + u_2 \cdot v_2 \cdot \dot{u}_3 + \dot{u}_3 \cdot w_3) \cdot w_2 \\ (u_1 \cdot w_1 + u_2 \cdot w_2 \cdot \dot{u}_3 + \dot{u}_3 \cdot w_2) \cdot v_3 - (u_1 \cdot v_1 + u_2 \cdot v_2) \cdot w_3 \cdot w_3 \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[137, 531, 690, 579]]<|/det|>
\[ = \begin{bmatrix} \langle \mathbf{u}, \mathbf{w} \rangle \cdot v_1 \\ \langle \mathbf{u}, \mathbf{w} \rangle \cdot v_2 \\ \langle \mathbf{u}, \mathbf{w} \rangle \cdot v_3 \end{bmatrix} - \begin{bmatrix} \langle \mathbf{u}, \mathbf{v} \rangle \cdot w_1 \\ \langle \mathbf{u}, \mathbf{v} \rangle \cdot w_2 \\ \langle \mathbf{u}, \mathbf{v} \rangle \cdot w_3 \end{bmatrix} = \langle \mathbf{u}, \mathbf{w} \rangle \cdot \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix} - \langle \mathbf{u}, \mathbf{v} \rangle \cdot \begin{bmatrix} w_1 \\ w_2 \\ w_3 \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[123, 585, 327, 603]]<|/det|>
\[ = \langle \mathbf{u}, \mathbf{w} \rangle \cdot \mathbf{v} - \langle \mathbf{u}, \mathbf{v} \rangle \cdot \mathbf{w}. \]

<|ref|>text<|/ref|><|det|>[[115, 610, 135, 626]]<|/det|>
j) 

<|ref|>equation<|/ref|><|det|>[[120, 627, 490, 646]]<|/det|>
\[ J = \mathbf{u} \times (\mathbf{v} \times \mathbf{w}) + \mathbf{v} \times (\mathbf{w} \times \mathbf{u}) + \mathbf{w} \times (\mathbf{u} \times \mathbf{v}) \]

<|ref|>equation<|/ref|><|det|>[[137, 661, 730, 680]]<|/det|>
\[ = \langle \mathbf{u}, \mathbf{w} \rangle \cdot v - \langle \mathbf{u}, \mathbf{v} \rangle \cdot \mathbf{w} + \langle \mathbf{v}, \mathbf{u} \rangle \cdot \mathbf{w} - \langle \mathbf{v}, \mathbf{w} \rangle \cdot \mathbf{u} + \langle \mathbf{w}, \mathbf{v} \rangle \cdot \mathbf{u} - \langle \mathbf{w}, \mathbf{u} \rangle \cdot \mathbf{v} \]

<|ref|>equation<|/ref|><|det|>[[137, 686, 730, 705]]<|/det|>
\[ = \langle \mathbf{w}, \mathbf{v} \rangle \cdot \mathbf{u} - (\mathbf{v}, \mathbf{w}) \cdot \mathbf{u} + \langle \mathbf{u}, \mathbf{w} \rangle \cdot \mathbf{v} - (\mathbf{w}, \mathbf{u}) \cdot \mathbf{v} + \langle \mathbf{v}, \mathbf{u} \rangle \cdot \mathbf{w - \langle \mathbf{u}, \mathbf{v} \rangle \cdot \mathbf{w}} \]

<|ref|>equation<|/ref|><|det|>[[137, 712, 702, 731]]<|/det|>
\[ = \left( \langle \mathbf{w}, \mathbf{v} \rangle - \langle \mathbf{v}, \mathbf{w} \rangle \right) \cdot \mathbf{u} + \left( \langle \mathbf{u}, \mathbf{w} \rangle - \langle \mathbf{w}, \mathbf{u} \rangle \right) \cdot \mathbf{v} + \left( \langle \mathbf{v}, \mathbf{u} \rangle - \langle \mathbf{u}, \mathbf{v} \rangle \right) \cdot \mathbf{w} \]

<|ref|>equation<|/ref|><|det|>[[137, 737, 430, 754]]<|/det|>
\[ = 0 \cdot \mathbf{u} + 0 \cdot \mathbf{v} + 0 \cdot \mathbf{w} = 0 + 0 + 0 = 0. \]

<|ref|>text<|/ref|><|det|>[[115, 757, 140, 773]]<|/det|>
k) 

<|ref|>text<|/ref|><|det|>[[115, 774, 330, 790]]<|/det|>
Mit g) und i) ergibt sich: 

<|ref|>equation<|/ref|><|det|>[[120, 790, 650, 809]]<|/det|>
\[ \langle \mathbf{a} \times \mathbf{b}, \mathbf{v} \times \mathbf{w} \rangle = \langle \mathbf{a}, \mathbf{b} \times (\mathbf{v} \times \mathbf{w}) \rangle = \langle \mathbf{a}, \langle \mathbf{b}, \mathbf{w} \rangle \cdot \mathbf{v} - \langle \mathbf{b}, \mathbf{v} \rangle \cdot \mathbf{w} \rangle \]

<|ref|>equation<|/ref|><|det|>[[245, 822, 808, 841]]<|/det|>
\[ = \langle \mathbf{a}, \langle \mathbf{b}, \mathbf{w} \rangle - \langle \mathbf{a}, \langle \mathbf{b}, \mathbf{v} \rangle \cdot \mathbf{w} \cdot \mathbf{a} \cdot \langle \mathbf{b}, \mathbf{v} \rangle \cdot \mathbf{w} \right\rangle = \langle \mathbf{a}, \mathbf{v} \rangle \cdot \langle \mathbf{b}, \mathbf{w} \rangle - \langle \mathbf{a}, w \rangle \cdot \langle \mathbf{b}, \mathbf{v} \rangle \cdot \mathbf{w}. \]

<|ref|>text<|/ref|><|det|> [[115, 847, 135, 863]]<|/det|>
l) 

<|ref|>text<|/ref|><|det|>[[115, 864, 184, 881]]<|/det|>
Es gilt: 

<|ref|>equation<|/ref|><|det|>[[120, 881, 416, 900]]<|/det|>
\[ \alpha := \angle(\mathbf{v}, \mathbf{w}) \in [0, \pi] \Rightarrow \sin(\alpha) \geq 0. \]