<|ref|>equation<|/ref|><|det|>[[111, 0, 560, 45]]<|/det|>
\[w(s) = \sum_{3} e^{-\frac{1}{2}(k_1^2 + k_2^2)}\]

<|ref|>text<|/ref|><|det|>[[61, 52, 991, 170]]<|/det|>
**Angenommen:** \((x_0, y_0, u(x_0, y_0)) \to (x(t), y(t), u(t))\)

\[
- \to (t_1, -t_2^2), e^{-\frac{t_2^2}{2}} \quad \text{aus I.C}
\]

<|ref|>equation<|/ref|><|det|>[[75, 179, 980, 300]]<|/det|>
\[
\begin{pmatrix}
k_1(s) \\
k_2(s) \\
w(s)
\end{pmatrix}
\text{soll auf dieser Stellungskurve liegen}
\]

<|ref|>equation<|/ref|><|det|>[[40, 310, 856, 650]]<|/det|>
\[
\begin{align*}
& \Rightarrow C_1 e^s = t \quad \xrightarrow{s=0} \quad C_1 = t \\
& C_2 e^s = -t^2 \quad \xrightarrow{s=0} \quad C_2 = -C_1^2 = -t^2 \\
& \tilde{C}_3 e^{-\frac{1}{2}(k_1^2 + k_2^2)} = e^{-\frac{1}{2}t^2} \\
& \tilde{C}_3 e^{-\frac{1}{2}(t^2 + t^4)} = e^{-\frac{1}{2}t^2} \\
& \tilde{C}_4 e^{-\frac{1}{2}t^4} = 1 \\
& \tilde{C}_3 e^{\frac{1}{2}t^4} = 1
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[30, 686, 900, 888]]<|/det|>
\[
\begin{align*}
& \Rightarrow x = k_1(s) = C_1 e^s = t, e^s \iff e^s = \frac{x}{t} \\
& y = k_2(s) = C_2 e^s = -t^2, e^s \\
& \qquad = -t^2, \frac{x}{t} = -x, t \iff t = -\frac{y}{x}
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[20, 874, 595, 930]]<|/det|>
\[
\Rightarrow u(x,y) = e^{\frac{1}{2}(\frac{y}{x})^4} e^{-\frac{1}{2}(x^2 + y^2)}
\]