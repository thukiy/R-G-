<|ref|>text<|/ref|><|det|>[[120, 84, 685, 121]]<|/det|>
Aus den Randbedingungen \(u(0, y) = u(1, y) = 0\) folgt \(V(0) = V(1) = 0\). Wir erhalten: 

<|ref|>equation<|/ref|><|det|>[[171, 139, 636, 245]]<|/det|>
\[
\begin{align*}
V(0) &= (a_1 + a_2) = 0 \Rightarrow a_1 = -a_2 \\
V(1) &= a_1 \exp(\sqrt{k}) - a_1 \exp(-\sqrt{k}) = 0 \\
&\Rightarrow \exp(\sqrt{k}) = \exp(-\sqrt{k}) \Rightarrow \exp(2\sqrt{k}) = 1 \\
&\Rightarrow 2\sqrt{k} = 2\pi in \Rightarrow k = -\pi^2 n^2, n \in \mathbb{N}.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[120, 260, 230, 278]]<|/det|>
So sind mit 

<|ref|>equation<|/ref|><|det|>[[120, 293, 664, 333]]<|/det|>
\[
W_n(y) = \tilde{d}_n(\exp(\pi ny) + \exp(-\pi ny)) = 2\tilde{d}_n \cosh(\pi ny)
\]

<|ref|>text<|/ref|><|det|>[[120, 316, 163, 333]]<|/det|>
und 

<|ref|>equation<|/ref|><|det|>[[151, 348, 656, 370]]<|/det|>
\[
V_n(x) = \tilde{c}_n(\exp(i\pi nx) - \exp(-i\pi nx)) = 2\tilde{c}_n \sin(\pi nx)
\]

<|ref|>text<|/ref|><|det|>[[120, 383, 419, 402]]<|/det|>
die zugehörigen Lösungen durch 

<|ref|>equation<|/ref|><|det|>[[232, 415, 576, 466]]<|/det|>
\[
u(x, t) = \sum_{n=1}^{\infty} c_n \sin(\pi nx) \cosh(\pi ny)
\]

<|ref|>text<|/ref|><|det|>[[120, 479, 207, 497]]<|/det|>
gegeben. 

<|ref|>text<|/ref|><|det|>[[120, 505, 685, 542]]<|/det|>
Die Koeffizienten \(c_n\) sind noch aus der Bedingung \(u(x, 1) = x\) zu bestimmen, d. h. 

<|ref|>equation<|/ref|><|det|>[[209, 555, 598, 629]]<|/det|>
\[
\begin{align*}
u(x, 1) &= \sum_{n_1}^{\infty} c_n \sin(\pi nx) \cosh(\pi n) \\
&= \sin(3\pi x) \cosh(3\pi) - 2 \sin(\pi x).
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[120, 651, 688, 707]]<|/det|>
Durch Koeffizientenvergleich erhalten wir \(c_1 = -2\cosh(\pi)\),
\(c_3 = 1\) und \(c_n = 0\) für alle \(n \in \mathbb{N} \setminus \{1, 3\}\). Damit ergibt sich
insgesamt die Lösung 

<|ref|>equation<|/ref|><|det|>[[124, 720, 684, 757]]<|/det|>
\[
u(x, t) = -\frac{2}{\cosh \pi} \sin(\pi x) \cosh(\pi y) + \sin(3\pi x) \cosh(3\pi y).
\]