<|ref|>text<|/ref|><|det|>[[118, 81, 170, 108]]<|/det|>
A1 

<|ref|>text<|/ref|><|det|>[[118, 96, 720, 170]]<|/det|>
a) \(<\vec{v}, \vec{v}_x> \vec{v} = <\begin{pmatrix} u_1 \\ u_2 \\ u_3 \end{pmatrix}, \begin{pmatrix} \frac{\partial u_1}{\partial x_1} \\ \frac{\partial u_2}{\partial x_2} \\ \frac{\partial u_3}{\partial x_3} \end{pmatrix} > \begin{pmatrix} u_1 \\ u_2 \\ u_3 \end{pmatrix}\) 

<|ref|>equation<|/ref|><|det|>[[155, 180, 580, 250]]<|/det|>
\[ = (u_1 \frac{\partial}{\partial x_1} + u_2 \frac{\partial}{\partial x_2} + u_3 \frac{\partial}{\partial x_3}) \begin{pmatrix} u_1 \\ u_2 \\ u_3 \end{pmatrix} \]

<|ref|>equation<|/ref|><|det|>[[155, 255, 860, 401]]<|/det|>
\[ = \begin{pmatrix} u_1 \frac{\partial u_1}{\partial x_1} + u_2 \frac{\partial u_2}{\partial x_2} + u_3 \frac{\partial u_3}{\partial x_3} \\ u_1 \frac{\partial u_2}{\partial x_1} + u_2 \frac{\partial u_3}{\partial x_2} + u_3 \frac{\partial u_1}{\partial x_3} \\ u_1 \frac{\partial u_3}{\partial x_1} + u_2 \frac{\partial u_1}{\partial x_2} + u_3 \frac{\partial u_2}{\partial x_3} \end{pmatrix} = (\sum_{i=1}^{3} u_i \frac{\partial u_i}{\partial x_i})_{j=1..3} \]

<|ref|>text<|/ref|><|det|>[[118, 405, 777, 440]]<|/det|>
b) \(\Delta x \vec{v}\): da \(\vec{v}\) ein Wellenpaket ist, gibt nicht: 

<|ref|>equation<|/ref|><|det|>[[459, 447, 875, 500]]<|/det|>
\[ \Delta v = \text{div} (\text{grad } v) \]

<|ref|>equation<|/ref|><|det|>[[456, 496, 875, 520]]<|/det|>
\[ \rightarrow \text{von } \text{pür } \text{Wellenpaket } \text{gültig} \]

<|ref|>text<|/ref|><|det|>[[160, 515, 770, 550]]<|/det|>
Hier: rot(rot\(\vec{v}\)) = grad(div\(\vec{v}\)) - \(\Delta \vec{v}\) 

<|ref|>equation<|/ref|><|det|>[[256, 552, 712, 585]]<|/det|>
\[ \Delta \vec{v} = \text{grad} (\text{div } \vec{v}) - \text{rot} (\text{rot } \vec{v}) \]

<|ref|>equation<|/ref|><|det|>[[120, 585, 375, 627]]<|/det|>
\[ \text{div}(\vec{v}) = <\vec{v}, \vec{v}> \]

<|ref|>equation<|/ref|><|det|>[[120, 625, 350, 661]]<|/det|>
\[ \text{rot}(\vec{v}) = \vec{v} \times \vec{v} \]

<|ref|>equation<|/ref|><|det|>[[120, 660, 880, 799]]<|/det|>
\[ \Rightarrow \Delta \vec{v} = \vec{v} < \vec{v}, \vec{v} > - \vec{v} \times (\vec{v} \times \vec{v}) \] \[ \text{umsetzt: } \vec{v} < \vec{v}, \vec{v} > = \begin{pmatrix} \frac{\partial \varphi_{x1}}{\partial x_2} \\ \frac{\partial \varphi_{x2}}{\partial x_2} \\ \frac{\partial \varphi_{x3}}{\partial x_3} \end{pmatrix} < \begin{pmatrix} \frac{\partial \varphi_{x1}}{\partial x_1} \\ \frac{\partial \varphi_{x2}}{\partial x_1} \\ \frac{\partial \varphi_{x3}}{\partial x_1} \end{pmatrix}, \begin{pmatrix} u_1 \\ u_2 \\ u_3 \end{pmatrix} > \]