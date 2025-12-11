<|ref|>text<|/ref|><|det|>[[115, 82, 144, 99]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[115, 97, 730, 116]]<|/det|>
Das Skalarprodukt ist linear bzgl. der Multiplikation mit einem Skalar. 

<|ref|>equation<|/ref|><|det|>[[115, 115, 770, 214]]<|/det|>
\[ \begin{aligned} \langle a \cdot v, w \rangle &= \left\langle a \begin{bmatrix} v_1 \\ \vdots \\ v_n \end{bmatrix}, \begin{bmatrix} w_1 \\ \vdots \\ w_n \end{bmatrix} \right\rangle = \left\langle \begin{bmatrix} av_1 \\ \vdots \\ av_n \end{bmatrix}, \begin{bmatrix} w_1 \\ \vdots \\ w_n \righ \end{bmatrix} \right\rangle \\ &= av_1 w_1 + \ldots + av_n w_n = a \cdot (v_1 w_1 + \ldots + v_n w_n) = a \cdot \langle v, w \rangle. \end{aligned} \]

<|ref|>text<|/ref|><|det|>[[115, 218, 144, 235]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[115, 234, 655, 252]]<|/det|>
Das Skalarprodukt ist linear bzgl. der Addition von Vektoren. 

<|ref|>equation<|/ref|><|det|>[[115, 250, 880, 370]]<|/det|>
\[ \begin{aligned} \langle \mathbf{u} + \mathbf{v}, \mathbf{w} \rangle &= \left\langle \begin{bmatrix} u_1 \\ \vdots \\ u_n \end{bmatrix} + \begin{bmatrix} v_1 \\ \vdots \\ v_n \end{bmatrix}, \begin{smallmatrix} \mathbf{u} \\ \mathbf{v} \\ \mathbf{w} \end{smallmatrix} \right\rangle = \left\langle \begin{bmatrix} u_1 + v_1 \\ \vdots \\ u_n + v_n \end{bmatrix}, \begin{bmatrix} \mathbf{u} \\ \mathbf{v} \\ \mathbf{w} \end{bmatrix} \right\rangle \\ &= (u_1 + v_1) \cdot w_1 + \ldots + (u_n + v_n) \cdot w_n = u_1 w_1 + v_1 w_1 + \ldots + u_n w_n + v_n w_n \\ &= u_1 w_1 + \ldots + u_n w_n + v_1 w_1 + \ldots + v_n w_n = \langle \mathbf{u}, \mathbf{w} \rangle + \langle \mathbf{v}, \mathbf{w} \rangle. \end{aligned} \]

<|ref|>text<|/ref|><|det|>[[115, 374, 144, 391]]<|/det|>
c) 

<|ref|>equation<|/ref|><|det|>[[115, 389, 660, 413]]<|/det|>
\[ \langle \mathbf{w}, \mathbf{v} \rangle = w_1 v_1 + \ldots + w_n v_n = v_1 w_1 + \ldots + v_n w_n = \langle \mathbf{v}, \mathbf{w} \rangle \]

<|ref|>text<|/ref|><|det|>[[115, 415, 144, 432]]<|/det|>
d) 

<|ref|>equation<|/ref|><|det|>[[115, 430, 580, 476]]<|/det|>
\[ \begin{aligned} \langle \mathbf{v}, \mathbf{v} \rangle &= v_1 v_1 + \ldots + v_n v_n = \frac{v_1^2}{2} + \ldots + \frac{v_n^2}{2} \geq 0 \\ &\geq 0 \end{aligned} \]

<|ref|>text<|/ref|><|det|>[[115, 479, 144, 496]]<|/det|>
e) 

<|ref|>equation<|/ref|><|det|>[[115, 494, 621, 519]]<|/det|>
\[ \langle \mathbf{v}, \mathbf{v} \rangle = 0 \Leftrightarrow v_1^2 + \ldots + v_n^2 = 0 \Leftrightarrow v_1^2 = \ldots = v_n^2 = 0 \]

<|ref|>equation<|/ref|><|det|>[[226, 531, 526, 552]]<|/det|>
\[ \Leftrightarrow v_1 = \ldots = v_n = 0 \Leftrightarrow \underline{\mathbf{v}} = 0. \]

<|ref|>text<|/ref|><|det|>[[115, 552, 140, 569]]<|/det|>
f) 

<|ref|>equation<|/ref|><|det|>[[115, 567, 880, 630]]<|/det|>
\[ \begin{aligned} \langle \mathbf{v} + \mathbf{w}, \mathbf{v} + \mathbf{w} \rangle &= \langle \mathbf{v} + \mathbf{w}, \mathbf{v} \rangle + \langle \mathbf{v} + \mathbf{w}, \mathbf{w} \rangle = \langle \mathbf{v}, \mathbf{v} \rangle + \langle \mathbf{w}, \mathbf{v} \rangle + \langle \mathbf{v}, \mathbf{w} \rangle + \langle \mathbf{w}, \mathbf{w} \rangle \\ &= |\mathbf{v}|^2 + |\mathbf{w}|^2 + 2 \cdot \langle \mathbf{v}, \mathbf{w} \rangle. \end{aligned} \]

g) 

<|ref|>equation<|/ref|><|det|>[[115, 650, 872, 672]]<|/det|>
\[ \langle \mathbf{v} - \mathbf{w}, \mathbf{v} - \mathbf{w} \rangle = \langle \mathbf{v} - \mathbf{w}, \mathbf{v} \rangle - \langle \mathbf{v} - \mathbf{w}, \mathbf{w} \rangle = \langle \mathbf{v}, \mathbf{w} \rangle - \langle \mathbf{w}, \mathbf{v} \rangle - \langle \mathbf{v}, \mathbf{w} \rangle + \langle \mathbf{w}, (\mathbf{w} - \mathbf{w}) \rangle \]

<|ref|>equation<|/ref|><|det|>[[115, 685, 520, 715]]<|/det|>
\[ \begin{aligned} &= |\mathbf{v}|^2 + |\mathbf{w}|^2 - 2 \cdot \langle \mathbf{v}, \mathbf{w} \rangle. \end{ aligned} \]

<|ref|>text<|/ref|><|det|>[[115, 714, 140, 731]]<|/det|>
h) 

<|ref|>equation<|/ref|><|det|>[[115, 729, 875, 750]]<|/det|>
\[ \langle \mathbf{v} + \mathbf{w}, \mathbf{v} - \mathbf{w} \rangle = \langle \v{v} + \mathbf{w}, \mathbf{v} \rangle - \langle \mathbf{v} + \mathbf{w}, \mathbf{w} \rangle = \v{v} + \mathbf{w}, \mathbf{v} \rangle - \langle \v{v}, \mathbf{w} \rangle - \langle \mathbf{v}, \mathbf{w} \rangle + \langle\mathbf{w}, \mathbf{w} \rangle \]

<|ref|>equation<|/ref|><|det|>[[115, 763, 400, 795]]<|/det|>
\[ = |\mathbf{v}|^2 - |\mathbf{w}|^2. \]

<|ref|>text<|/ref|><|det|>[[115, 808, 785, 826]]<|/det|>
6. Schreibweise mit Spitzklammern verglichen mit Punktschreibweise 

<|ref|>text<|/ref|><|det|>[[115, 823, 650, 856]]<|/det|>
Gegeben seien die Vektoren \(\vec{u} = \begin{pmatrix} 2 \\ -1 \end{pmatrix}\), \(\vec{v} = \begin{pmatrix} 1 \\ 3 \end{pmatrix}\), \(\vec{w} = \begin{pmatrix} -1 \\ 1 \end{pmatrix}\). 

<|ref|>text<|/ref|><|det|>[[115, 853, 600, 874]]<|/det|>
a) Berechnen Sie die Komponenten von \(\vec{a} = \langle \vec{u}, \vec{v} \rangle \cdot \vec{w}\). 

<|ref|>text<|/ref|><|det|>[[115, 872, 600, 892]]<|/det|>
b) Berechnen Sie die Komponenten von \(\vec{b} = \vec{u} \cdot \langle \vec{v}, \vec{w} \rangle\). 

<|ref|>text<|/ref|><|det|>[[115, 890, 780, 909]]<|/det|>
c) Schreiben Sie die Terme aus Aufgabe a) und b) mit Punktschreibweise.