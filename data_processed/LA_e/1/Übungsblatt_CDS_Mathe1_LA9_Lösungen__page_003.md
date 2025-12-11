<|ref|>sub_title<|/ref|><|det|>[[114, 81, 571, 100]]<|/det|>
## 4. Vektorprodukt mit Python/Sympy berechnen 

<|ref|>text<|/ref|><|det|>[[114, 99, 733, 118]]<|/det|>
Berechnen Sie die Vektorprodukte aus Aufgabe 2 mit Python/Sympy. 

<|ref|>text<|/ref|><|det|>[[114, 133, 144, 150]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[114, 149, 408, 165]]<|/det|>
# Python initialisieren: 

<|ref|>text<|/ref|><|det|>[[114, 165, 346, 182]]<|/det|>
import sympy as sp; 

<|ref|>text<|/ref|><|det|>[[114, 181, 466, 198]]<|/det|>
import IPython.display as dp; 

<|ref|>text<|/ref|><|det|>[[114, 198, 264, 214]]<|/det|>
# Parameter: 

<|ref|>text<|/ref|><|det|>[[114, 214, 340, 231]]<|/det|>
sp.init_printing(); 

<|ref|>text<|/ref|><|det|>[[114, 230, 370, 247]]<|/det|>
v=sp.Matrix([1,2,3]); 

<|ref|>text<|/ref|><|det|>[[114, 246, 370, 263]]<|/det|>
w=sp.Matrix([4,5,6]); 

<|ref|>text<|/ref|><|det|>[[114, 262, 300, 279]]<|/det|>
# Berechnungen: 

<|ref|>text<|/ref|><|det|>[[114, 278, 272, 295]]<|/det|>
u=v.cross(w); 

<|ref|>text<|/ref|><|det|>[[114, 295, 240, 311]]<|/det|>
# Ausgabe: 

<|ref|>text<|/ref|><|det|>[[114, 310, 286, 328]]<|/det|>
dp.display(u); 

<|ref|>text<|/ref|><|det|>[[114, 342, 270, 361]]<|/det|>
analog für b) - f) 

<|ref|>sub_title<|/ref|><|det|>[[114, 375, 381, 394]]<|/det|>
## 5. Aussagen über Vektoren 

<|ref|>text<|/ref|><|det|>[[114, 394, 680, 440]]<|/det|>
Gegeben seien die beiden Vektoren \(\vec{v} = \frac{1}{\sqrt{3}} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}\) und \(\vec{w} = \begin{pmatrix} -2 \\ 0 \\ 2 \end{pmatrix}\). 

<|ref|>text<|/ref|><|det|>[[114, 437, 620, 454]]<|/det|>
Welche der folgenden Aussagen sind wahr bzw. falsch? 

<|ref|>table<|/ref|><|det|>[[114, 453, 880, 577]]<|/det|>
<table><tr><td></td><td>Wahr</td><td>Falsch</td></tr><tr><td>a) Der Vektor \(\vec{v}\) ist ein Einheitsvektor.</td><td>X</td><td></td></tr><tr><td>b) Es gilt: \(\vec{w} = 2 \cdot \vec{w}\).</td><td></td><td>X</td></tr><tr><td>c) Es gilt: \(\langle \vec{w}, \vec{v} \rangle = |\vec{w}| \cdot |\vec{v}|\).</td><td></td><td>X</td></tr><tr><td>d) Es gilt: \(|\vec{v} \times \vec{w}| = |\vec{w}|\).</td><td>X</td><td></td></tr><tr><td>e) Es gilt: \(\vec{4}(\vec{v}, \vec{w}) = 0\).</td><td></td><td>X</td></tr><tr><td>f) Es gibt \(a, b \in \mathbb{R}\) mit \(a \neq 0\), so dass \(a \cdot \vec{v} + b \cdot \vec{w} = 0\).</td><td></td><td>X</td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[114, 591, 475, 609]]<|/det|>
## 6. Eigenschaften des Vektorprodukts 

<|ref|>text<|/ref|><|det|>[[114, 608, 803, 626]]<|/det|>
Beweisen Sie die folgenden Eigenschaften des Vektorprodukts für \(a \in \mathbb{R}\) und 

<|ref|>text<|/ref|><|det|>[[114, 626, 587, 645]]<|/det|>
beliebige Vektoren \(\vec{a}, \vec{b}, \vec{u}, \vec{v}, \vec{w} \in \mathbb{R}^3\) durch Einsetzen. 

<|ref|>text<|/ref|><|det|>[[114, 644, 775, 663]]<|/det|>
a) \((a \cdot \vec{v}) \times \vec{w} = a \cdot (\vec{v} \times \vec{w})\) b) \(\vec{u} \times (\vec{v} + \vec{w}) = \vec{u} \times \vec{v} + \vec{u} \times \vec{w}\) 

<|ref|>text<|/ref|><|det|>[[114, 661, 600, 680]]<|/det|>
c) \(\vec{w} \times \vec{v} = -\vec{v} \times \vec{w}\) d) \(\vec{v} \times \vec{v} = 0\) 

<|ref|>text<|/ref|><|det|>[[114, 678, 857, 698]]<|/det|>
e) \((\vec{v} + \vec{w} \times (\vec{v} - \vec{w})) = 2\vec{w} \times \vec{v}\) f) \(\vec{v} \times \vec{w} = \vec{v} \times \vec{w}_1\) mit \(\vec{w}_1 = \vec{w} - \langle \vec{w}, \vec{v} \rangle \cdot \vec{v}\) 

<|ref|>text<|/ref|><|det|>[[114, 696, 777, 715]]<|/det|>
g) \((\vec{v}, \vec{w} \times \vec{u}) = (\vec{v} \times \vec{w}, \vec{u}) = \langle \vec{u} \times \vec{v}, \vec{w} \rangle\) h) \(\vec{v} \perp (\vec{v} \times \vec{w})\) und \(\vec{w} \perp (\vec{v} \times \vec{w})\) 

<|ref|>text<|/ref|><|det|>[[114, 714, 440, 732]]<|/det|>
i) \(\vec{u} \times (\vec{v} \times \vec{w}) = \langle \vec{u}, \vec{w} \rangle \cdot \vec{v} - \langle \vec{u}, \vec{v} \rangle \cdot \vec{w}\) 

<|ref|>text<|/ref|><|det|>[[114, 730, 530, 749]]<|/det|>
j) \(\vec{u} \times (\vec{v} \times \vec{w}) + \vec{v} \times (\vec{w} \times \vec{u}) + \vec{w} \times (\vec{u} \times \vec{v}) = 0\) 

<|ref|>text<|/ref|><|det|>[[114, 748, 528, 767]]<|/det|>
k) \((\vec{a} \times \vec{b}, \vec{v} \times \vec{w}) = \langle \vec{a}, \vec{v} \rangle \cdot \langle \vec{b}, \vec{w} \rangle - \langle \vec{a}, \vec{w} \rangle \cdot \langle \vec{b}, \vec{v} \rangle\) 

<|ref|>text<|/ref|><|det|>[[114, 766, 607, 789]]<|/det|>
l) \(|\vec{v} \times \vec{w}| = \sqrt{|\vec{v}|^2 \cdot |\vec{w}|^2 - (\vec{v}, \vec{w})^2} = |\vec{v}| \cdot |\vec{w}| \cdot \sin \alpha (\vec{v}, \vec{w})\) 

<|ref|>text<|/ref|><|det|>[[114, 804, 140, 821]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[114, 821, 741, 925]]<|/det|>
\[ \begin{align*} \frac{(a \cdot v) \times w}{a \cdot v} &= \begin{bmatrix} a \cdot v_1 \\ a \cdot v_2 \\ a \cdot v_3 \end{bmatrix} \times \begin{bmatrix} w_1 \\ w_2 \\ w_3 \end{bmatrix} = \begin{bmatrix} a \cdot v_2 \cdot w_3 - a \cdot v_3 \cdot w_2 \\ a \cdot v_3 \cdot w_1 - a \cdot v_1 \cdot w_3 \\ a \cdot v_1 \cdot w_2 - a \cdot v_2 \cdot w_1 \end{bmatrix} \\ &= \begin{bmatrix} a \cdot (v_2 \cdot w_3 - v_3 \cdot w_2) \\ a \cdot (v_3 \cdot w_1 - v_1 \cdot w_3) \\ a \cdot (v_1 \cdot w_2 - v_2 \cdot w_1) \end{bmatrix} = a \cdot \begin{bmatrix} v_2 \cdot w_3 - v_3 \cdot w_2 \\ v_3 \cdot w_1 - v_1 \cdot w_3 \\ v_1 \cdot w_2 - v_2 \cdot w_1 \end{bmatrix} = a \cdot (v \times w) \end{align*} \]