<|ref|>equation<|/ref|><|det|>[[117, 84, 830, 290]]<|/det|>
\[
\begin{align*}
a_k &= \frac{2}{T} \int_T x(t) \cdot \cos\left(\frac{2\pi k}{T} t\right) dt = \frac{2}{T} \cdot 2 \int_0^{\frac{T}{4}} A \cdot \cos\left(\frac{2\pi k}{T} t\right) dt \\
&= \frac{4A}{T} \int_0^{\frac{T}{4}} \cos\left(\frac{2\pi k}{T} t\right) dt = \frac{A}{T} \cdot \frac{T}{2\pi k} \cdot \left[ \sin\left(\frac{2\pi k}{T} t\right) \right]_0^{\frac{T}{4}} \\
&= \frac{2A}{\pi k} \cdot \left( \sin\left(\frac{2\pi k}{T} \cdot \frac{T}{4}\right) - \sin\left(\frac{2\pi k}{T} \cdot 0\right) \right) = \frac{2A}{\pi k} \cdot \left( \sin\left(\frac{\pi k}{2}\right) - \sin(0) \right) \\
&= \frac{2A}{\pi k} \cdot \left( \frac{1}{2} \cdot \left( (-1)^k - 1 \right) \cdot (-1)^{\frac{k+1}{2}} - 0 \right) = \frac{A}{\pi} \cdot \frac{\left((-1)^k - 1\right) \cdot (-1)^{\frac{k+1}{2}}}{k}
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[121, 298, 193, 315]]<|/det|>
\(b_k = 0\).

<|ref|>text<|/ref|><|det|>[[121, 328, 625, 348]]<|/det|>
Die reelle Fourier-Entwicklung des Signals ist daher 

<|ref|>equation<|/ref|><|det|>[[121, 358, 700, 470]]<|/det|>
\[
\begin{align*}
x_n(t) &= \frac{a_0}{2} + \sum_{k=1}^{n} a_k \cdot \cos\left(\frac{2\pi k}{T} t\right) \\
&= \frac{A}{2} + \frac{A}{\pi} \sum_{k=1}^{n} \frac{\left((-1)^k - 1\right) \cdot (-1)^{\frac{1}{2}} \cdot \cos\left(\frac{2\pi k}{T} t\right)}{k}.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 475, 145, 492]]<|/det|>
c) 

<|ref|>text<|/ref|><|det|>[[115, 490, 852, 525]]<|/det|>
Es liegt negative Parität vor, deshalb können wir eine reine Sinusreihe verwenden.
Es gilt ausserdem für \(t \in ]0, T[\) 

<|ref|>equation<|/ref|><|det|>[[365, 525, 715, 561]]<|/det|>
\[
x(t) = \frac{2A}{T} \cdot (t - 0) - A = \frac{2A}{T} t - A.
\]

<|ref|>text<|/ref|><|det|>[[124, 570, 608, 589]]<|/det|>
Für die reellen Fourier-Koeffizienten erhalten wir 

<|ref|>equation<|/ref|><|det|>[[124, 602, 200, 620]]<|/det|>
\(a_0 = 0\)

<|ref|>equation<|/ref|><|det|>[[124, 633, 195, 650]]<|/det|>
\(a_k = 0\)

<|ref|>equation<|/ref|><|det|>[[124, 653, 783, 700]]<|/det|>
\[
b_k = \frac{2}{T} \int_T x(t) \cdot \sin\left(\frac{2\pi k}{T} t\right) dt = \frac{2}{\frac{T}{2}} \int_0^T \left(\frac{2A}{T} t - A\right) \cdot \sin\left(\frac{2\pi k}{T} t\right) dt
\]

<|ref|>equation<|/ref|><|det|>[[124, 704, 512, 750]]<|/det|>
\[
= \frac{2A}{T} \int_0^T \left(\frac{2}{T} t - 1\right) \cdot \sin\left(\frac{2\pi k}{T} t\right)dt
\]

<|ref|>equation<|/ref|><|det|>[[124, 754, 675, 800]]<|/det|>
\[
= \frac{2A}{T} \int_0^t \frac{2}{T} t \cdot \sin\left(\frac{2\pi k}{T} t\right) dt - \frac{2A}{T} \int_0^T \sin\left(\frac{2\pi k}{T} t\right) dt
\]

<|ref|>text<|/ref|><|det|>[[124, 804, 456, 850]]<|/det|>
\[
= \frac{4A}{T^2} \int_0^T t \cdot \sin\left(\frac{2\pi k}{T} t\right) dt = 0
\]

<|ref|>equation<|/ref|><|det|>[[124, 853, 696, 900]]<|/det|>
\[
= \frac{4A}{T^2} \cdot \left[ \frac{T^2}{4\pi^2 k^2} \cdot \sin\left(\frac{2\pi k}{T} t\right) - \frac{T}{2\pi k} \cdot t \cdot \cos\left(\frac{2\pi k}{T} t\right) \right]_0^T
\]