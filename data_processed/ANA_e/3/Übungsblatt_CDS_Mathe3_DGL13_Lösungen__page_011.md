<|ref|>equation<|/ref|><|det|>[[35, 0, 777, 118]]<|/det|>
\[
\begin{align*}
\text{IV}(x_1) &= C_1 \cdot e^{\sqrt{-k_{x_1}^2} x_1} + C_2 \cdot e^{-\sqrt{-k_{x_1}^2} x_1} \\
\text{WI}(x_2) &= C_3 e^{\sqrt{-k_{x_2}^2} x_2} + C_4 e^{-\sqrt{-k_{x_2}^2} x_2}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[5, 140, 700, 185]]<|/det|>
Invertible IIC: \(U(x_1, 0) = U(x_1, b) = 0\) 

<|ref|>equation<|/ref|><|det|>[[117, 205, 890, 640]]<|/det|>
\[
\begin{align*}
C_3 + C_4 &= 0 \Leftrightarrow C_3 = -C_4 \\
\text{WI}(b) &= C_3 \left[ e^{\sqrt{-k_{x_2}^2} b} - e^{-\sqrt{-k_{x_2}^2} b} \right] = 0 \\
e^{\sqrt{-k_{x_2}^2} b} &= e^{-\sqrt{-k_{x_2}^2} b} \\
e^{2\sqrt{-k_{x_2}^2} b} &= 1 \\
e^{2\sqrt{-k_{x_2}^2} b} &= 2\pi i \cdot n \\
b &= \frac{2\pi i n}{2\sqrt{-k_{x_2}^2}} = \frac{\pi i n}{k_{x_2} \cdot \sqrt{-1}} = \frac{\pi n}{k_{x_2}} \\
k_{x_2} &= \frac{\pi n}{b}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[10, 656, 722, 700]]<|/det|>
Invertible IIC: \(U(0, x_2) = U(a, x_2) = 0\) 

<|ref|>equation<|/ref|><|det|>[[195, 710, 930, 970]]<|/det|>
\[
\begin{align*}
C_1 + C_2 &= 0 \quad \Leftrightarrow \quad C_1 = -C_2 \\
v(a) &= C_1 \cdot \left[ e^{\sqrt{-k_{x_1}^2} a} - e^{-\sqrt{-k_{x_1}^2} a} \right] = 0 \\
e^{\sqrt{-k_{x_1}^2} a} &= e^{-\sqrt{-k_{x_1}^2} a} \\
e^{2\sqrt{-k_{x_1}^2} a} &= 1 \quad \text{(Segment = 0)} \\
2\sqrt{-k_{x_1}^2} a &= 2\pi i \cdot m
\end{align*}
\]