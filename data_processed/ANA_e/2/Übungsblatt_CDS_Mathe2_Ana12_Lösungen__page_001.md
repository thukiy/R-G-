<|ref|>title<|/ref|><|det|>[[115, 182, 500, 217]]<|/det|>
# Übungsblatt 12 Ana 

<|ref|>text<|/ref|><|det|>[[575, 196, 879, 231]]<|/det|>
Computational and Data Science
FS2024 

<|ref|>text<|/ref|><|det|>[[115, 249, 270, 278]]<|/det|>
## Lösungen 

<|ref|>text<|/ref|><|det|>[[751, 258, 880, 275]]<|/det|>
Mathematik 2 

<|ref|>text<|/ref|><|det|>[[115, 303, 210, 320]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 319, 855, 355]]<|/det|>
- Sie kennen die Begriffe Divergenz, Rotation, quellenfrei, wirbelfrei, konservativ, Potential-/Gradientenfeld und deren wichtigste Eigenschaften. 

<|ref|>text<|/ref|><|det|>[[115, 353, 770, 370]]<|/det|>
- Sie können die Rotation und Divergenz von Vektorfeldern bestimmen. 

<|ref|>text<|/ref|><|det|>[[115, 369, 760, 387]]<|/det|>
- Sie können bestimmen, ob ein Vektorfeld quellen- bzw. wirbelfrei ist. 

<|ref|>sub_title<|/ref|><|det|>[[115, 418, 416, 436]]<|/det|>
### 1. Divergenz von Vektorfeldern 

<|ref|>text<|/ref|><|det|>[[115, 435, 633, 454]]<|/det|>
Bestimmen Sie die Divergenz der folgenden Vektorfelder. 

<|ref|>equation<|/ref|><|det|>[[115, 451, 660, 543]]<|/det|>
\[ 
\begin{align*} 
\text{a) } \vec{F}(x, y) &= \begin{pmatrix} x^3 + 1 \\ xy^2 \end{pmatrix} \quad & \text{b) } \vec{v}(x, y) = \begin{pmatrix} x \cdot e^{-y} \\ y \cdot e^{-x} \end{pmatrix} \nonumber \\ 
\text{c) } \vec{F}(x, y, z) &= \begin{pmatrix} 2x^3 z^2 \\ x^2 - z^2 \\ xy z \end{pmatrix} \quad & \text{d) } \vec{v}(x, y, z) = \begin{pmatrix} xy - x^2 z \\ 2yz^2 \\ x^2 y - yz \end{pmatrix} 
\end{align*} 
\]

<|ref|>text<|/ref|><|det|>[[115, 558, 144, 575]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[125, 577, 670, 620]]<|/det|>
\[ \text{div } \vec{F} = \frac{\partial}{\partial x} (x^3 + 1) + \frac{\partial}{\partial y} (x y^2) = 3x^2 + 2xy \]

<|ref|>text<|/ref|><|det|>[[115, 621, 144, 639]]<|/det|>
b) 

<|ref|>equation<|/ref|><|det|>[[125, 640, 692, 683]]<|/det|>
\[ \text{div } \vec{v} = \frac{\partial}{\partial x} (x \cdot e^{-y}) + \frac{\partial}{\partial y} (y \cdot e^{-x}) = e^{-y} + e^{-x} \]

<|ref|>text<|/ref|><|det|>[[115, 687, 144, 705]]<|/det|>
c) 

<|ref|>equation<|/ref|><|det|>[[125, 706, 707, 799]]<|/det|>
\[ \begin{align*} \text{div } \vec{F} &= \frac{\partial}{\partial x} (2x^3 z^2) + \frac{\partial}{\partial y} (x^2 - z^2) + \frac{\partial}{\partial z} (xy z) = \\ &= 6x^2 z^2 + 0 + xy = 6x^2 z^2 + xy \end{align*} \]

<|ref|>text<|/ref|><|det|>[[115, 810, 144, 828]]<|/det|>
d) 

<|ref|>equation<|/ref|><|det|>[[115, 831, 755, 925]]<|/det|>
\[ \begin{align*} \text{div } \vec{v} &= \frac{\partial}{\partial x} (xy - x^2 z) + \frac{\partial}{\partial y} (2yz^2) + \frac{\partial}{\partial z} (x^2 y + yz) = \\ &= y - 2xz + 2z^2 + y = \end{align*} \]