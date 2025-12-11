<|ref|>text<|/ref|><|det|>[[114, 83, 144, 100]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[119, 99, 600, 135]]<|/det|>
Die Funktion \(f\) ist ungerade, daher sind die Koeffizienten \(a_k = 0, k = 0, 1, 2, \ldots\) 

<|ref|>text<|/ref|><|det|>[[119, 136, 592, 155]]<|/det|>
Zur Bestimmung der Koeffizienten \(b_k\) berechnen wir zunächst 

<|ref|>equation<|/ref|><|det|>[[119, 160, 600, 260]]<|/det|>
\[
\begin{align*}
\cos(x) \sin(kx) &= \frac{1}{4i} (\mathrm{e}^{\mathrm{i}x} + \mathrm{e}^{-\mathrm{i}x})(\mathrm{e}^{\mathrm{i}kx} - \mathrm{e}^{-\mathrm{i}kx}) \\
&= \frac{1}{4i} (\mathrm{e}^{\mathrm{i}(k+1)x} - \mathrm{e}^{-\mathrm{i}(k-1)x} + \mathrm{e}^{\mathrm{i}(k-1)x} - \mathrm{e}^{-\mathrm{i}(k+1)x}) \\
&= \frac{1}{2} (\sin((k+1)x) + \sin((k-1)x)).
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[119, 264, 405, 283]]<|/det|>
Nun ergibt sich für \(k \ge 2\) die Formel 

<|ref|>equation<|/ref|><|det|>[[169, 290, 550, 487]]<|/det|>
\[
\begin{align*}
b_k &= \frac{1}{\pi} \int_0^\pi x (\sin((k+1)x) + \sin((k-1)x)) \, \mathrm{d}x \\
&= \frac{1}{\pi} \left[ \frac{\sin((k+1)x)}{(k+1)^2} - \frac{x \cos((k+1)x)}{k+1} \right. \\
&\qquad \left. + \frac{\sin((k-1)x)}{(k-1)^2} - \frac{x \cos((k-1)x)}{k-1} \right]^\pi_0 \\
&= -\frac{(-1)^{k+1}}{k+1} - \frac{(-1)^{k-1}}{k-1} \\
&= (-1)^k \frac{2k}{k^2-1}.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[119, 489, 300, 506]]<|/det|>
Für \(k = 1\) erhalten wir 

<|ref|>equation<|/ref|><|det|>[[226, 515, 490, 696]]<|/det|>
\[
\begin{align*}
b_1 &= \frac{2}{\pi} \int_0^\pi x \cos(x) \sin(x) \, \mathrm{d}x \\
&= \frac{1}{\pi} \int_0^\pi x \sin(2x) \, \mathrm{d}x \\
&= \frac{1}{\pi} \left[ \frac{ \sin(2x)}{4} - \frac{x \cos(2x)}{2} \right]_0^\pi \\
&= -\frac{1}{2}.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[119, 713, 377, 731]]<|/det|>
Damit haben wir die Fourierreihe 

<|ref|>equation<|/ref|><|det|>[[208, 738, 512, 788]]<|/det|>
\[
\left(-\frac{1}{2} \sin(x) + \sum_{k=2}^{\infty} \frac{(-1)^k}{k^2-1} \sin(kx)\right)
\]

<|ref|>text<|/ref|><|det|>[[119, 797, 202, 815]]<|/det|>
gefunden. 

<|ref|>text<|/ref|><|det|>[[114, 816, 150, 834]]<|/det|>
b) 

<|ref|>equation<|/ref|><|det|>[[123, 837, 658, 895]]<|/det|>
\[
a_0 = \frac{1}{\pi} \cdot \int_0^{2\pi} (2\pi x - x^2) \, dx = \frac{1}{\pi} \left[ \pi x^2 - \frac{1}{3} x^3 \right]_0^{2\pi} = \frac{4}{3} \pi^2
\]