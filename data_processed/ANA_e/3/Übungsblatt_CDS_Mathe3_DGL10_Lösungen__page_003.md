<|ref|>image<|/ref|><|det|>[[117, 82, 640, 240]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[120, 241, 603, 260]]<|/det|>
Für die reellen Fourier-Koeffizienten erhalten wir 

<|ref|>equation<|/ref|><|det|>[[120, 270, 880, 555]]<|/det|>
\[
\begin{align*}
a_0 &= \frac{2}{T} \int_T \text{PE}_{(T,+)}[f](t) \, \mathrm{d}t = \frac{2}{2\pi} \int_{-\pi}^{\pi} t^2 \, \mathrm{d}t = \frac{1}{\pi} \cdot \frac{1}{3} \cdot \left[ t^3 \right]_{-\pi}^{\pi} = \frac{1}{3\pi} \cdot \left( \pi^3 - (-\pi)^3 \right) \\
&= \frac{1}{3\pi} \cdot 2\pi^3 = \frac{2}{3}\pi^2 \\
a_k &= \frac{2}{T} \int_T \text{PE}_{(T, +)}[f](t) \cos\left(\frac{2\pi k}{T} t\right) \, \mathrm{d}t = \frac{2}{2\pi} \int_{-\pi}^\pi t^2 \cos\left(\frac{2\pi k}{2\pi} t\right) \, \mathrm{d}t \\
&= \frac{1}{\pi} \cdot 2 \int_0^\pi t^2 \cdot \cos(k t) \, \mathrm{d}t = \frac{2}{\pi} \cdot \left[ \left( \frac{t^2}{k} - \frac{2}{k^3} \right) \cdot \sin(k t) + \frac{2t}{k^2} \cdot \cos(k t) \right]_{0}^{\pi} \\
&= \frac{2}{\pi} \cdot \left( \left( \frac{\pi^2}{k} - \frac{2}{k^3} \right) \sin(k \pi) + \frac{2\pi}{k^2} \cdot \cos(k \pi) - 0 - 0 \right) = \frac{2}{\pi} \cdot \frac{2\pi}{k^2} \cdot \cos(k \pi) \\
&= \frac{4}{k^2} \cdot \cos(k \pi) = 4 \frac{(-1)^k}{k^2}
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[127, 555, 201, 572]]<|/det|>
\(b_k = 0\).

<|ref|>text<|/ref|><|det|>[[127, 587, 525, 605]]<|/det|>
Die reelle Fourier-Entwicklung ist daher 

<|ref|>equation<|/ref|><|det|>[[127, 616, 715, 666]]<|/det|>
\[
f_n(t) = \frac{a_0}{2} + \sum_{k=1}^{n} a_k \cdot \cos\left(\frac{2\pi k}{T} t\right) = \frac{\pi^2}{3} + 4 \sum_{k=1}^{n} \frac{(-1)^k}{k^2} \cdot \cos(k t)
\]

<|ref|>text<|/ref|><|det|>[[127, 678, 445, 697]]<|/det|>
und auf dem Intervall \([- \pi, \pi]\) gilt 

<|ref|>equation<|/ref|><|det|>[[127, 710, 561, 760]]<|/det|>
\[
\frac{f(t)}{=} \lim_{n \to \infty} f_n(t) = \frac{\pi^2}{3} + 4 \sum_{k=2}^{\infty} \frac{(-1)^k}{k^2} \cdot \cos(k t).
\]

<|ref|>text<|/ref|><|det|>[[114, 767, 144, 784]]<|/det|>
c) 

<|ref|>equation<|/ref|><|det|>[[345, 783, 680, 832]]<|/det|>
\[
f(0) = \frac{\pi^2}{3} + 4 \sum_{k=0}^{\infty} \frac{(-1)^k}{k^2} \cdot \cos (k \cdot 0)
\]

<|ref|>equation<|/ref|><|det|>[[225, 840, 816, 890]]<|/det|>
\[
\Leftrightarrow \qquad 0^2 = \frac{\pi^2}{3} + 4 \sum_{k=1}^{\infty} \frac{(-1)^k}{k^2} \cdot 1 \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \quad \vdots \quad 4
\]