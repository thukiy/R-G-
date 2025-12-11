<|ref|>equation<|/ref|><|det|>[[80, 19, 725, 234]]<|/det|>
\[
\begin{align*}
w(y) &= 0 \\
c_3 e^{\sqrt{-\pi^2 n^2}}, 0 &= c_4 e^{-\sqrt{-\pi^2 n^2}}, 0 \\
c_3 &= c_4 \\
\Rightarrow w(y) &= c_3 [e^{\sqrt{-\pi^2 n^2} y} + e^{-\sqrt{-\pi^2 n^2} y}]
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[30, 264, 900, 640]]<|/det|>
\[
\begin{align*}
&\Rightarrow \text{unable estimate } w(y) = c_3 e^{\sqrt{-k}y} + c_4 e^{-\sqrt{-k}y} \\
&\qquad \quad \rightarrow w(y) = 2c_3 \cosh(k \pi y) \\
&\qquad \quad \rightarrow v_n(x) = c_1 [e^{i \pi n x} - e^{-i \pi n x}] \\
&\qquad \quad = c_1 [\cos(k \pi n x) + i \sin(k \pi n x) \\
&\qquad \quad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \quad - \cos(k \pi n x) - i \sin(k \pi n x)] \\
&\qquad \quad = c_1 [e^{i k \pi n x} \sin(k \pi n x)]
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[20, 640, 970, 789]]<|/det|>
\[
\Rightarrow u(x, y) = v(x) \cdot w(y) = \sum_{n=1}^{\infty} c_{1n} \sin(n\pi x) \cdot \tilde{c}_{3n} \cosh(n\pi y) \\
= \sum_{n=1}^{\infty} C_n \sin(n\pi x) \cosh(n\pi y)
\]

<|ref|>equation<|/ref|><|det|>[[6, 803, 770, 975]]<|/det|>
\[
C \text{ mittels } IC \text{ bestimmen!}
\\
U(x, 1) = \sin(3\pi x) \cosh(3\pi) - 2 \sin(\pi x)
\\
= \sum_{n=1}^{\infty} C_n \sin(n\pi x) \coth(n\pi)
\]