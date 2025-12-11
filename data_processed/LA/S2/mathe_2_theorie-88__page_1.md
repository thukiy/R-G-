<|ref|>text<|/ref|><|det|>[[20, 12, 375, 36]]<|/det|>
Sata : A sei n x n Matrix 

<|ref|>text<|/ref|><|det|>[[129, 52, 812, 80]]<|/det|>
a) det(A) ≠ 0 ⇔ A ist regulär d.h. es existiert A⁻¹ 

<|ref|>text<|/ref|><|det|>[[129, 90, 560, 116]]<|/det|>
b) det(A) = 0 ⇔ A ist singulär 

<|ref|>text<|/ref|><|det|>[[40, 148, 550, 177]]<|/det|>
→ A sei orthogonal: det(A) ∈ {-1, 1} 

<|ref|>text<|/ref|><|det|>[[20, 208, 260, 232]]<|/det|>
Def: Gram Matrix 

<|ref|>equation<|/ref|><|det|>[[100, 245, 300, 272]]<|/det|>
\[ \vec{v}_1 \dots \vec{v}_m \in \mathbb{R}^n \]

<|ref|>equation<|/ref|><|det|>[[110, 300, 490, 390]]<|/det|>
\[ G = \begin{pmatrix} \langle \vec{v}_1, \vec{v}_1 \rangle & \dots & \langle \vec{v}_1, \vec{v}_m \rangle \\ \langle \vec{v}_2, \vec{v}_1 \rangle & \dots & \langle \vec{v}_2, \vec{v}_m \rangle \\ \vdots & \ddots & \vdots \\ \langle \vec{v}_m, \vec{v}_1 \rangle & \dots & \langle \vec{v}_m, \vec{v}_m \rangle \end{pmatrix} \]

<|ref|>equation<|/ref|><|det|>[[40, 421, 201, 447]]<|/det|>
→ Gᵀ = G

<|ref|>equation<|/ref|><|det|>[[40, 460, 238, 487]]<|/det|>
→ det(G) = 0 

<|ref|>text<|/ref|><|det|>[[20, 519, 170, 543]]<|/det|>
Def: Mass 

<|ref|>equation<|/ref|><|det|>[[110, 556, 476, 582]]<|/det|>
\[ \text{Mass des Vektoren } \vec{v}_1 \dots \vec{v}_m : \]

<|ref|>equation<|/ref|><|det|>[[115, 593, 415, 621]]<|/det|>
\[ \mu(\vec{v}_1 \dots \vec{v}_m) = \sqrt{\det(G)} \]

<|ref|>equation<|/ref|><|det|>[[40, 653, 605, 680]]<|/det|>
→ \(\mu(\vec{v}) = \sqrt{\langle \vec{v}, \vec{v} \rangle} = |\vec{v}|\)

<|ref|>text<|/ref|><|det|>[[440, 656, 608, 680]]<|/det|>
dange von \(\vec{v}\) 

<|ref|>equation<|/ref|><|det|>[[40, 691, 760, 718]]<|/det|>
→ \(\mu(\vec{v}_1, \vec{v}_2)\) Reiche von aufgebrannten Parallelogramm

<|ref|>equation<|/ref|><|det|>[[40, 728, 725, 757]]<|/det|>
→ \(\mu(\vec{v}_1, \vec{v}_2, \vec{v}_3)\) Volumen des Spats aus \(\vec{v}_1, \vec{v}_2, \vec{v}_3\)