<|ref|>sub_title<|/ref|><|det|>[[114, 81, 450, 100]]<|/det|>
## 4. Komplexe Fourier-Koeffizienten 

<|ref|>text<|/ref|><|det|>[[114, 99, 808, 118]]<|/det|>
Bestimmen Sie die komplexen Fourier-Koeffizienten der Funktion f, die durch 

<|ref|>equation<|/ref|><|det|>[[114, 115, 327, 152]]<|/det|>
\[f(x) = \begin{cases} 0, & -\pi < x \le 0 \\ e^{ix}, & 0 < x \le \pi \end{cases}\]

<|ref|>text<|/ref|><|det|>[[114, 150, 234, 167]]<|/det|>
gegeben ist. 

<|ref|>text<|/ref|><|det|>[[221, 182, 276, 198]]<|/det|>
Es ist 

<|ref|>equation<|/ref|><|det|>[[258, 207, 465, 312]]<|/det|>
\[c_k = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(x) e^{-ikx} \, dx \\
= \frac{1}{2\pi} \int_{0}^{\pi} e^{i(1-k)x} \, dx.\]

<|ref|>text<|/ref|><|det|>[[122, 318, 485, 336]]<|/det|>
Für \(k = 1\) ist \(c_1 = 1/2\). Für \(k \neq 1\) erhalten wir 

<|ref|>equation<|/ref|><|det|>[[264, 342, 460, 458]]<|/det|>
\[c_k = \frac{1}{2\pi} \left[ \frac{e^{i(1-k)x}}{i(1-k)} \right]_{0}^{\pi} \\
= \frac{1}{2\pi} \frac{e^{i(1-k)\pi} - 1}{i(1-k)} \\
= -\frac{i}{2\pi} \frac{(-1)^{k-1} - 1}{1-k}.\]

<|ref|>text<|/ref|><|det|>[[122, 462, 460, 480]]<|/det|>
Damit ist \(c_k = 0\) für \(k\) ungerade, \(k \neq 1\) und 

<|ref|>equation<|/ref|><|det|>[[255, 486, 472, 521]]<|/det|>
\[c_k = \frac{i}{\pi(1-k)}, \quad k \text{ gerade.}\]

<|ref|>text<|/ref|><|det|>[[122, 527, 325, 544]]<|/det|>
Die Fourierreihe ist durch 

<|ref|>equation<|/ref|><|det|>[[232, 549, 491, 593]]<|/det|>
\[\left(\frac{1}{2} e^{ix} + \sum_{k=-\infty}^{\infty} \frac{i}{\pi(1-2k)} e^{2ikx}\right)\]

<|ref|>text<|/ref|><|det|>[[122, 600, 202, 616]]<|/det|>
gegeben. 

<|ref|>sub_title<|/ref|><|det|>[[114, 634, 343, 651]]<|/det|>
## 5. Reelle Fourier-Reihe 

<|ref|>text<|/ref|><|det|>[[114, 650, 370, 668]]<|/det|>
Entwickeln Sie die Funktion 

<|ref|>text<|/ref|><|det|>[[114, 668, 388, 686]]<|/det|>
a) \(f(x) = x \cos x, x \in ]-\pi, \pi[\) 

<|ref|>text<|/ref|><|det|>[[114, 685, 411, 703]]<|/det|>
b) \(f(x) = x(2\pi - x), 0 \le x \le 2\pi\) 

<|ref|>text<|/ref|><|det|>[[114, 702, 355, 720]]<|/det|>
c) \(f(x) = |x|, -\pi \le x \le \pi\) 

<|ref|>text<|/ref|><|det|>[[114, 719, 450, 736]]<|/det|>
in eine Fourier-Reihe in reeller Form.