<|ref|>text<|/ref|><|det|>[[114, 82, 141, 100]]<|/det|>
c) 

<|ref|>equation<|/ref|><|det|>[[120, 100, 880, 320]]<|/det|>
\[
\begin{align*}
\frac{d}{dt} (\vec{a} \times \vec{b}) &= \dot{\vec{a}} \times \vec{b} + \vec{a} \times \dot{\vec{b}} = \begin{pmatrix} 1 \\ 2t \\ 3t^2 \end{pmatrix} \times \begin{pmatrix} 2 \cdot \cos t \\ 2 \cdot \sin t \\ t^2 \end{pmatrix} + \begin{pmatrix} t \\ t^2 \\ t^3 \end{pmatrix} \times \begin{pmatrix} -2 \cdot \sin t \\ 2 \cdot \cos t \\ 2t \end{pmatrix} = \\
&= \begin{pmatrix} 2t^3 - 6t^2 \cdot \sin t \\ 6t^2 \cdot \cos t - t^2 \\ 2 \cdot \sin t - 4t \cdot \cos t \end{pmatrix} + \begin{pmatrix} 2t^3 - 2t^3 \cdot \cos t \\ -2t^3 \cdot \sin t - 2t^2 \\ 2t \cdot \cos t + 2t^2 \cdot \sin t \end{pmatrix} = \\
&= \begin{pmatrix} 4t^3 - 6t^2 \cdot \sin t - 2t^3 \cdot \cos t \\ -3t^2 - 2t^3 \cdot \sin t + 6t^2 \cdot \cos t \\ 2(1 + t^2) \cdot \sin t - 2t \cdot \cos t \end{pmatrix}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 319, 141, 337]]<|/det|>
d) 

<|ref|>equation<|/ref|><|det|>[[120, 340, 696, 410]]<|/det|>
\[
\frac{d}{dt} (\vec{a} \times \vec{c}) = \dot{\vec{a}} \times \vec{c} + \vec{a} \times \dot{\vec{c}} = \begin{pmatrix} 3t^2 + (t^3 - 3t^2) \cdot e^{-t} \\ -2t - (t^3 - 3t^2) \cdot e^{-t} \\ (1 - 3t + t^2) \cdot e^{-t} \end{pmatrix}
\]

<|ref|>sub_title<|/ref|><|det|>[[114, 425, 260, 444]]<|/det|>
6. Bogenlänge 

<|ref|>text<|/ref|><|det|>[[114, 441, 636, 460]]<|/det|>
Berechnen Sie die Bogenlänge der folgenden Funktionen. 

<|ref|>equation<|/ref|><|det|>[[114, 460, 875, 515]]<|/det|>
\[
\text{a) } \gamma: [0, a] \to \mathbb{R}^3, \gamma(t) = t \begin{pmatrix} \cos t \\ \sin t \\ 1 \end{pmatrix}. \qquad \text{b) } \gamma: [0, 4\pi] \to \mathbb{R}^3, \gamma(t) = \begin{pmatrix} -t \cos t + \sin t \\ \cos t + t \sin t \\ \frac{t^2}{4} \end{pmatrix}
\]

<|ref|>text<|/ref|><|det|>[[114, 515, 144, 533]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[114, 531, 567, 550]]<|/det|>
Für die Ableitung erhält man mit Hilfe der Produktregel 

<|ref|>equation<|/ref|><|det|>[[211, 560, 650, 617]]<|/det|>
\[
\dot{\gamma}(t) = \begin{pmatrix} \cos t \\ \sin t \\ 1 \end{pmatrix} + t \begin{pmatrix} -\sin t \\ \cos t \\ 0 \end{pmatrix} = \begin{pmatrix} \cos t - t \sin t \\ \sin t + t \cos t \\ 1 \end{pmatrix}.
\]

<|ref|>text<|/ref|><|det|>[[120, 620, 373, 639]]<|/det|>
Die Kurve hat damit die Länge 

<|ref|>equation<|/ref|><|det|>[[227, 649, 735, 880]]<|/det|>
\[
\begin{align*}
L &= \int_0^a \|\dot{\gamma}(t)\| \, dt = \int_0^a \|(\cos t - t \sin t, \sin t + t \cos t, 1)^\top\| \, dt \\
&= \int_0^a \sqrt{(\cos t - t \sin t)^2 + (\sin t + t \cos t)^2 + 1} \, dt \\
&= \int_0^a \sqrt{(1 + t^2)(\sin^2 t + \cos^2 t) + 1} \, dt = \int_0^a \sqrt{2 + t^2} \, dt \\
&= \sqrt{2} \int_0^a \sqrt{1 + (t/\sqrt{2})^2} \, dt
\end{align*}
\]