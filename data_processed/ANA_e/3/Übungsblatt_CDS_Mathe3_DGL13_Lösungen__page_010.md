<|ref|>text<|/ref|><|det|>[[15, 0, 75, 35]]<|/det|>
A2 

<|ref|>equation<|/ref|><|det|>[[15, 30, 857, 150]]<|/det|>
\[
\text{Wellengel.} \quad U_{tt} = \Delta U \qquad U(\vec{x}, t) \\
\frac{\partial^2 U(\vec{x}, t)}{\partial t^2} = \frac{\partial^2 U(\vec{x}, t)}{\partial x_1^2} + \frac{\partial^2 U(\vec{x}, t)}{\partial x_2^2}
\]

<|ref|>text<|/ref|><|det|>[[15, 165, 100, 213]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[15, 186, 989, 320]]<|/det|>
\[
\text{Formationsinstate: } U(\vec{x}, t) = e^{ik \vec{x} \cdot \vec{U}(\vec{x})} \\
\text{Einsteffen: } -k^2 e^{ik \vec{x} \cdot \vec{U}(\vec{x})} = e^{ik \vec{x} \cdot \left[ \frac{\partial^2 U(\vec{x})}{\partial x_1^2} + \frac{\partial^2 U(\vec{x})}{\partial x_2^2} \right]}
\]

<|ref|>equation<|/ref|><|det|>[[40, 330, 625, 380]]<|/det|>
\[
\Rightarrow -k^2 U(\vec{x}) = \Delta U(\vec{x})
\]

<|ref|>equation<|/ref|><|det|>[[7, 390, 970, 470]]<|/det|>
\[
b) \quad \frac{\partial^2 U(\vec{x})}{\partial x_1^2} \frac{\partial^2 U(\vec{x})}{\partial x_2^2} + k^2 \cdot U(\vec{x}) = 0 \quad \text{PDE}
\]

<|ref|>equation<|/ref|><|det|>[[81, 495, 952, 592]]<|/det|>
\[
U(x_1, 0) = U(x_1, 5) = U(0, x_2) = U(a, x_2) = 0 \quad \text{TC} \\
\text{nutze: } k^2 = k_{x_1}^2 + k_{x_2}^2
\]

<|ref|>equation<|/ref|><|det|>[[50, 608, 602, 650]]<|/det|>
\[
\text{Abwette: } U(\vec{x}) = v(x_1) \cdot w(x_2)
\]

<|ref|>equation<|/ref|><|det|>[[50, 658, 395, 696]]<|/det|>
\[
\text{Einsteffen mit PDE: }
\]

<|ref|>equation<|/ref|><|det|>[[55, 702, 896, 747]]<|/det|>
\[
w(x_2) \cdot v'(x_1) + v(x_1) \cdot w'(x_2) + k^2 v(x_1) \cdot w(x_2) = 0
\]

<|ref|>equation<|/ref|><|det|>[[61, 760, 950, 869]]<|/det|>
\[
\begin{align*}
\frac{v'(x_1)}{v(x_1)} + \frac{w'(x_2)}{w(x_2)} + k^2 &= 0 \quad \text{und} \\
&= k_{x_1}^2 + k_{x_2}^2
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[40, 880, 777, 970]]<|/det|>
\[
\begin{align*}
- k \frac{v''(x_1)}{v(x_1)} &= - k^2 \frac{1}{x_1} \quad \text{und} \\
&= - k_{x_2}^2 \frac{2}{x_2}
\end{align*}
\]