<|ref|>image<|/ref|><|det|>[[114, 84, 675, 375]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[114, 389, 149, 405]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[114, 404, 852, 423]]<|/det|>
Es liegt negative Parität vor, deshalb können wir eine reine Sinusreihe verwenden. 

<|ref|>equation<|/ref|><|det|>[[122, 425, 195, 444]]<|/det|>
\(a_0 = 0\)

<|ref|>equation<|/ref|><|det|>[[122, 456, 195, 475]]<|/det|>
\(a_k = 0\)

<|ref|>equation<|/ref|><|det|>[[122, 485, 737, 525]]<|/det|>
\[b_k = \frac{2}{T} \int_T x(t) \cdot \sin\left(\frac{2\pi k}{T} t\right) dt = \frac{2}{T} \cdot 2 \int_0^{\frac{T}{2}} A \cdot \sin\left(\frac{2\pi k}{T} t\right) dt\]

<|ref|>equation<|/ref|><|det|>[[122, 536, 880, 696]]<|/det|>
\[= \frac{4A}{T} \int_0^{\frac{T}{2}} \sin\left(\frac{2\pi k}{T} t\right) dt = \frac{A}{T} \cdot \frac{T}{2\pi k} \cdot (-1) \cdot \left[ \cos\left(\frac{2\pi k}{T} t\right) \right]_0^{\frac{T}{2}}\]

<|ref|>equation<|/ref|><|det|>[[122, 698, 592, 739]]<|/det|>
\[= \frac{2A}{\pi k} \cdot \left( \cos\left(\frac{2\pi k}{T} \cdot \frac{T}{2}\right) - \cos\left(\frac{2\pi k}{T} \cdot 0\right) \right) = -\frac{2A}{\pi k} \cdot (\cos(\pi k) - \cos(0))\]

<|ref|>equation<|/ref|><|det|>[[122, 700, 555, 740]]<|/det|>
\[= \frac{2A}{\pi k} \cdot \left( (-1)^k - 1 \right) = \frac{2A}{\pi} \cdot \frac{1 - (-1)^k}{k}.\]

<|ref|>text<|/ref|><|det|>[[122, 745, 650, 765]]<|/det|>
Die reelle Fourier-Entwicklung des Signals ist daher 

<|ref|>equation<|/ref|><|det|>[[122, 768, 750, 787]]<|/det|>
\[x_n(t) = \sum_{k=1}^{n} b_k \cdot \sin\left(\frac{2\pi k}{T} t\right) = \frac{2A}{\pi} \sum_{k=1}^{n} \frac{1 - (-1)^k}{k} \cdot \sin\left(\frac{2\pi k}{T} t\right).\]

<|ref|>text<|/ref|><|det|>[[114, 789, 149, 805]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[114, 803, 867, 822]]<|/det|>
Es liegt positive Parität vor, deshalb können wir eine reine Cosinusreihe verwenden. 

<|ref|>equation<|/ref|><|det|>[[122, 821, 880, 910]]<|/det|>
\[a_0 = \frac{2}{T} \int_T x(t) dt = \frac{2}{T} \cdot 2 \int_0^{\pi} A dt = \frac{4A}{T} \int_0^{\pi} \frac{1}{T} dt = \frac{4A}{T} \cdot \left[ t \right]_0^{\pi} = \frac{4A}{T} \cdot \left( \frac{T}{4} - 0 \right)\]

<|ref|>equation<|/ref|><|det|>[[122, 872, 290, 910]]<|/det|>
\[= \frac{4A}{T} \cdot \frac{T}{4} = A\]