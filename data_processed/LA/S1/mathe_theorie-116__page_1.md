<|ref|>text<|/ref|><|det|>[[25, 10, 841, 42]]<|/det|>
→ die dünge des Vektors ist durch Skalprodukt definiert : 

<|ref|>equation<|/ref|><|det|>[[95, 45, 456, 160]]<|/det|>
\[
\begin{align*}
|\vec{v}| &= \sqrt{v_1^2 + v_2^2 + \cdots + v_n^2} \\
&= \sqrt{<\vec{v}, \vec{v}>} \\
|\vec{v}|^2 &= <\vec{v}, \vec{v}>
\end{align*}
\]

<|ref|>image<|/ref|><|det|>[[544, 45, 880, 191]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[540, 168, 877, 197]]<|/det|>
Pythagoras : \(|\vec{v}|^2 = v_1^2 + v_2^2\) 

<|ref|>text<|/ref|><|det|>[[18, 225, 644, 255]]<|/det|>
geometrische Interpretation des Skalprodukts : 

<|ref|>equation<|/ref|><|det|>[[48, 264, 777, 370]]<|/det|>
\[
\begin{align*}
\langle \vec{v}, \vec{w} \rangle &= |\vec{v}| \cdot |\vec{w}| \cdot \cos \alpha & v, w \in \mathbb{R}^n \\
\alpha &= \angle (\vec{v}, \vec{w}) \\
0 &\le \alpha \le \pi
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[25, 383, 981, 452]]<|/det|>
→ Skalprodukt entspricht der dünge von \(\vec{v}\) multipliziert mit derselben Projektion von \(\vec{w}\) auf \(\vec{v}\) 

<|ref|>image<|/ref|><|det|>[[179, 455, 400, 562]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[25, 597, 970, 625]]<|/det|>
→ Winkel zwischen \(\Delta\) Vektoren kann mit Skalprodukt bestimmt werden : 

<|ref|>equation<|/ref|><|det|>[[128, 627, 339, 666]]<|/det|>
\[
\cos \alpha = \frac{\langle \vec{v}, \vec{w} \rangle}{|\vec{v}| \cdot |\vec{w}|}
\]

<|ref|>equation<|/ref|><|det|>[[100, 688, 500, 760]]<|/det|>
\[
\begin{align*}
0 < \alpha < \frac{\pi}{2} &: \langle \vec{v}, \vec{w} \rangle > 0 \\
\frac{\pi}{2} < \alpha < \pi &: \langle \vec{v}, \vec{w} \rangle < 0
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[25, 792, 950, 821]]<|/det|>
→ \(\Delta\) Vektoren sind orthogonal (senkrecht) aufeinander, wenn gilt : 

<|ref|>equation<|/ref|><|det|>[[80, 828, 450, 960]]<|/det|>
\[
\begin{align*}
\langle \vec{v}, \vec{w} \rangle = 0 & \quad \vec{v}, \vec{w} \neq 0 \\
\Leftrightarrow \alpha = \frac{\pi}{2} & \Leftrightarrow \vec{v} \perp \vec{w} \\
\Rightarrow \langle \vec{v}, \vec{w} \rangle = |\vec{v}| \cdot |\vec{w}| \cdot \cos \alpha = 0 & \Leftrightarrow \cos \alpha = 0 \\
\alpha = \frac{\pi}{2}
\end{align*}
\]