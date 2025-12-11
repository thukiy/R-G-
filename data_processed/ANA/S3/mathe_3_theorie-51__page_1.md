<|ref|>equation<|/ref|><|det|>[[68, 12, 833, 130]]<|/det|>
\[
\begin{align*}
|f - q|^2_{L^2} &= <f - q, f - q> \tag{keine } q_k \text{-Abhängigkeit} \\
&= |f|^2_{L^2} - \sum_{k=-n}^{n} |<f, \varphi_k>|^2_{L^2} + \sum_{k=-n}^{n} |q_k - <f, \varphi_k>|^2_{L^2}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[191, 130, 680, 159]]<|/det|>
Abstand minimale, wenn \(q_k = <f, \varphi_k>\) 

<|ref|>text<|/ref|><|det|>[[25, 202, 570, 234]]<|/det|>
Fourierpolynom zu einer Funktion \(f\) : 

<|ref|>equation<|/ref|><|det|>[[50, 238, 530, 280]]<|/det|>
\[
p(x) = \sum_{k=-n}^{n} c_k e^{ikx} \quad x \in \mathbb{R}
\]

<|ref|>equation<|/ref|><|det|>[[50, 293, 626, 331]]<|/det|>
\[
\text{Fourierkoeffizienten } c_k = \frac{1}{2\pi} - \pi \int f(x) e^{-ikx} \, dx
\]

<|ref|>text<|/ref|><|det|>[[25, 375, 336, 405]]<|/det|>
reelles Fourier-Polynom 

<|ref|>equation<|/ref|><|det|>[[50, 410, 533, 451]]<|/det|>
\[
p_n(x) = \sum_{k=1}^{n} (a_k \cos(kx) + b_k \sin(kx))
\]

<|ref|>equation<|/ref|><|det|>[[50, 465, 440, 505]]<|/det|>
\[
a_0 = \frac{1}{\pi} - \pi \int f(x) \, dx \quad x \in \mathbb{R}
\]

<|ref|>equation<|/ref|><|det|>[[50, 510, 375, 549]]<|/det|>
\[
a_k = \frac{1}{\pi} - \pi \int f(x) \cos(kx) \, dx
\]

<|ref|>equation<|/ref|><|det|>[[50, 553, 370, 592]]<|/det|>
\[
b_k = \frac{1}{\pi} - \pi \int f(x) \sin(kx) \, dx
\]

<|ref|>equation<|/ref|><|det|>[[50, 607, 633, 670]]<|/det|>
\[
\begin{align*}
a_0 &= c_0 \quad &a_k &= c_k + c_{-k} \quad &b_k &= i(c_k - c_{-k}) \\
c_k &= \frac{a_k - ib_k}{2} \quad &c_{-k} &= \frac{a_k + ib_k}{2}
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[50, 700, 530, 730]]<|/det|>
\[\rightarrow f \text{ ist eine gerade Funktion: } b_k = 0\]

<|ref|>equation<|/ref|><|det|>[[50, 737, 530, 767]]<|/det|>
\[\rightarrow f \text{ ist eine ungeade Funktion: } a_k = 0\]

<|ref|>text<|/ref|><|det|>[[50, 796, 310, 824]]<|/det|>
Hilfreiche Formeln : 

<|ref|>equation<|/ref|><|det|>[[70, 833, 520, 860]]<|/det|>
\[
\sin(k \cdot \pi) = 0 \quad k \in \mathbb{N}
\]

<|ref|>equation<|/ref|><|det|>[[70, 870, 290, 900]]<|/det|>
\[
\cos(k \cdot \pi) = (-1)^k
\]

<|ref|>equation<|/ref|><|det|>[[70, 904, 480, 937]]<|/det|>
\[
\sin(k \cdot \frac{\pi}{2}) = \frac{1}{2} \left[ (-1)^k - 1 \right] \cdot (-1)^{\frac{k+1}{2}}
\]

<|ref|>equation<|/ref|><|det|>[[70, 944, 460, 977]]<|/det|>
\[
\cos(k \cdot \frac{\pi}{2}) = \frac{1}{2} \cdot \left[ (-1)^k - 1 \right] \cdot (-1)^{\frac{\pi}{2}}
\]