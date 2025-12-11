<|ref|>sub_title<|/ref|><|det|>[[114, 81, 600, 100]]<|/det|>
## 4. Geschwindigkeits- und Beschleunigungsvektor 

<|ref|>text<|/ref|><|det|>[[114, 98, 875, 133]]<|/det|>
Differenzieren Sie die gegebenen Kurven zweimal nach t, um den Geschwindigkeits- und Beschleunigungsvektor zu bestimmen. 

<|ref|>equation<|/ref|><|det|>[[114, 131, 570, 190]]<|/det|>
\[
\text{a) } \vec{a}(t) = \begin{pmatrix} \sin(2t) \\ e^t \\ \cos(2t) \end{pmatrix} \qquad \text{b) } \vec{a}(t) = \begin{pmatrix} e^{-t} \cos t \\ e^{-t} \sin t \\ t \end{pmatrix}
\]

<|ref|>equation<|/ref|><|det|>[[114, 204, 140, 221]]<|/det|>
a)

<|ref|>equation<|/ref|><|det|>[[124, 222, 639, 290]]<|/det|>
\[
\vec{\dot{a}}(t) = \begin{pmatrix} 2 \cdot \cos(2t) \\ e^t \\ -2 \cdot \sin(2t) \end{pmatrix}; \quad \vec{\ddot{a}}(t) = \begin{pmatrix} -4 \cdot \sin(2t) \\ e^t \\ -4 \cdot \cos(2t) \end{pmatrix}
\]

<|ref|>equation<|/ref|><|det|>[[114, 293, 140, 310]]<|/det|>
b)

<|ref|>equation<|/ref|><|det|>[[114, 312, 780, 450]]<|/det|>
\[
\begin{align*}
\vec{\dot{a}}(t) &= \begin{pmatrix} -e^{-t} \cdot \cos t - \sin t \cdot e^{-t} \\ -e^{-t} \cdot \sin t + \cos t \cdot e^{-t} \\ 1 \end{pmatrix} = \begin{pmatrix} -(\sin t + \cos t) \cdot e^{-t} \\ -(\sin t - \cos t) \cdot e^{-t} \\ 1 \end{pmatrix} \\
\vec{\ddot{a}}(t) &= \begin{pmatrix} -(\cos t - \sin t) \cdot e^{-t} + e^{-t} (\sin t + \cos t) \\ -(\cos t + \sin t) \cdot e^{-t} + e^{-t} (\sin t - \cos t) \\ 0 \end{pmatrix} = 2 \cdot e^{-t} \begin{pmatrix} \sin t \\ -\cos t \\ 0 \end{pmatrix}
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[114, 463, 585, 481]]<|/det|>
## 5. Ableitungen von Skalar- und Vektorprodukten 

<|ref|>text<|/ref|><|det|>[[114, 480, 678, 498]]<|/det|>
Gegeben seien die folgenden parameterabhängigen Vektoren: 

<|ref|>equation<|/ref|><|det|>[[114, 496, 512, 543]]<|/det|>
\[
\vec{a}(t) = \begin{pmatrix} t^2 \\ t^3 \end{pmatrix}, \vec{b}(t) = \begin{pmatrix} 2 \cos t \\ 2 \sin t \end{pmatrix}, \vec{c}(t) = \begin{pmatrix} e^{-t} \\ e^{-t} \end{pmatrix}.
\]

<|ref|>text<|/ref|><|det|>[[114, 542, 857, 577]]<|/det|>
Bestimmen Sie die 1. Ableitung der folgenden Skalar- und Vektorprodukte mit Hilfe der entsprechenden Produktregel: 

<|ref|>equation<|/ref|><|det|>[[114, 575, 692, 597]]<|/det|>
a) \(\langle \vec{a}, \vec{b} \rangle\) b) \(\langle \vec{b}, \vec{c} \rangle\) c) \(\vec{a} \times \vec{b}\) d) \(\vec{a} \times \vec{c}\)

<|ref|>equation<|/ref|><|det|>[[114, 611, 140, 628]]<|/det|>
a)

<|ref|>equation<|/ref|><|det|>[[114, 633, 850, 750]]<|/det|>
\[
\begin{align*}
\frac{d}{dt} (\vec{a} \cdot \vec{b}) &= \dot{\vec{a}} \cdot \vec{b} + \vec{a} \cdot \dot{\vec{b}} = \begin{pmatrix} 1 \\ 2t \\ 3t^2 \end{pmatrix} \cdot \begin{pmatrix} 2 \cdot \cos t \\ 2 \cdot \sin t \\ t^2 \end{pmatrix} + \begin{pmatrix} t \\ t^2 \\ t^3 \end{pmatrix} \cdot \begin{pmatrix} -2 \cdot \sin t \\ 2 \cdot \cos t \\ 2t \end{pmatrix} = \\
&= 2 \cdot \cos t + 4t \cdot \sin t + 3t^4 - 2t \cdot \sin t + 2t^2 \cdot \cos t + 2t^4 = \\
&= 5t^4 + 2t \cdot \sin t + 2(1 + t^2) \cdot \cos t
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[114, 750, 572, 797]]<|/det|>
b) \(\frac{d}{dt} (\vec{b} \cdot \vec{c}) = \dot{\vec{b}} \cdot \vec{c} + \vec{b} \cdot \dot{\vec{c}} = 3t^2 - 4 \cdot e^{-t} \cdot \sin t\)