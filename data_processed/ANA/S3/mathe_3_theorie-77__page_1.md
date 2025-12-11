<|ref|>equation<|/ref|><|det|>[[196, 15, 562, 85]]<|/det|>
\[
\begin{align*}
u(\vec{y}, 0) &= q(\vec{y}) = q(\vec{y} + t\vec{a} - t\vec{a}) \\
&= u(\vec{y} + t\vec{a}, t)
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[102, 92, 785, 121]]<|/det|>
→ PDGLs werden auf gewöhnliche DGLs zurückgeführt 

<|ref|>equation<|/ref|><|det|>[[50, 145, 768, 255]]<|/det|>
\[
\begin{align*}
\text{allegemein} : & \langle \vec{a}(\vec{x}, u(\vec{x})), \nabla u(\vec{x}) \rangle + b(\vec{x}, u(\vec{x})) > = 0 \quad \text{(*)} \\
& \text{mit } \vec{a} : \mathbb{R}^n \times \mathbb{R} \to \mathbb{R}^n, \quad b : \mathbb{R}^n \times \mathbb{R} \to \mathbb{R} \\
& u : \mathbb{R}^n \to \mathbb{R}, \quad x \in \mathbb{R}^n
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[82, 284, 956, 312]]<|/det|>
PDGL ist quasilinear, da a & b nicht linear von u abhängen können 

<|ref|>equation<|/ref|><|det|>[[82, 337, 597, 470]]<|/det|>
\[
\begin{align*}
\text{Einführung einer Kurve } \vec{R} : & D \subseteq \mathbb{R} \to \mathbb{R}^n \\
\text{auf dämonzphunktion } u : & w(s) = u(\vec{R}(s)) \\
w'(s) = \frac{du}{ds} = \frac{du}{ds} = \frac{\partial u}{\partial s} \frac{ds}{ds} + \ldots + \frac{\partial u}{\partial s} \frac{ds}{ds} \\
&= < \vec{R}'(s), \nabla u(\vec{R}(s)) >
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[82, 510, 625, 615]]<|/det|>
\[
\begin{align*}
\text{Vgl mit PDGL (*)} : \\
w'(s) = & < \vec{R}'(s), \nabla u(\vec{R}(s)) > = -b(\vec{x}, u(\vec{x})) \\
& = \vec{a}(\vec{x}, \vec{a}(\vec{x})) = \vec{a}(\vec{R}(s), w(s))
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[78, 645, 675, 672]]<|/det|>
→ es ergibt sich das System gewöhnlicher DGLs : 

<|ref|>equation<|/ref|><|det|>[[138, 678, 411, 750]]<|/det|>
\[
\begin{align*}
\vec{R}'(s) &= \vec{a}(\vec{R}(s), w(s)) \\
w'(s) &= -b(\vec{R}(s), w(s))
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[138, 760, 765, 789]]<|/det|>
Die dämonigen \(k_1 \ldots k_n\), \(w\) heissen Charakteristiken 

<|ref|>text<|/ref|><|det|>[[138, 815, 888, 880]]<|/det|>
Mit Hilfe von AB wie \(w(0) = u(\vec{R}(0))\) ist das der PDGL entlang einer Charakteristik eindeutig bestimmt.