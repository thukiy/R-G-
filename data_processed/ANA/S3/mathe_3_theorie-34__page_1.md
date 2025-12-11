<|ref|>equation<|/ref|><|det|>[[160, 8, 600, 40]]<|/det|>
\[y_1(x) = e^{(-8 + i\omega)x}, \quad y_2(x) = e^{(-8 - i\omega)x}\]

<|ref|>equation<|/ref|><|det|>[[160, 45, 560, 80]]<|/det|>
\[y(x) = C_1 \cdot e^{-8x + i\omega x} + C_2 \cdot e^{-8x - i\omega x}\]

<|ref|>equation<|/ref|><|det|>[[220, 85, 561, 118]]<|/det|>
\[= e^{-8x} (C_1 \cdot e^{i\omega x} + C_2 \cdot e^{-i\omega x})\]

<|ref|>equation<|/ref|><|det|>[[220, 123, 928, 191]]<|/det|>
\[= e^{-8x} [C_1 \cdot (\cos(\omega x) + i \cdot \sin(\omega x)) + C_2 \cdot (\cos(-\omega x) + i \cdot \sin(-\omega x))] = \cos(\omega x) = -\sin(\omega x)\]

<|ref|>equation<|/ref|><|det|>[[220, 199, 780, 255]]<|/det|>
\[= e^{-8x} \cdot [\cos(\omega x) \cdot (C_1 + C_2) + i \cdot \sin(\omega x) (C_1 - C_2)] = A = B\]

<|ref|>equation<|/ref|><|det|>[[220, 275, 592, 310]]<|/det|>
\[= e^{-8x} \cdot (A \cos(\omega x) + B \sin(\omega x))\]

<|ref|>text<|/ref|><|det|>[[28, 344, 320, 370]]<|/det|>
**Bsp:** \(y'' + 4y' + 4y = 0\) 

<|ref|>equation<|/ref|><|det|>[[120, 375, 345, 405]]<|/det|>
\[Ansatz: y = e^{\lambda x}\]

<|ref|>equation<|/ref|><|det|>[[115, 415, 308, 440]]<|/det|>
\[\lambda^2 + 4\lambda + 4 = 0\]

<|ref|>equation<|/ref|><|det|>[[115, 445, 375, 477]]<|/det|>
\[\lambda_{1/2} = \frac{-4 \pm \sqrt{16 - 4 \cdot 4}}{2} = -2\]

<|ref|>equation<|/ref|><|det|>[[115, 490, 388, 515]]<|/det|>
\[\Rightarrow y(x) = (C_1 + C_2 \cdot x) \cdot e^{-2x}\]

<|ref|>equation<|/ref|><|det|>[[100, 550, 343, 576]]<|/det|>
\[\cdot y'' + 6y' + 45y = 0\]

<|ref|>equation<|/ref|><|det|>[[120, 586, 345, 611]]<|/det|>
\[\lambda^2 + 6\lambda + 45 = 0\]

<|ref|>equation<|/ref|><|det|>[[120, 616, 595, 650]]<|/det|>
\[\lambda_{1/2} = \frac{-6 \pm \sqrt{36 - 4 \cdot 45}}{2} = \frac{-6 \pm \sqrt{-144}}{2} = -3 \pm i \cdot 6\]

<|ref|>equation<|/ref|><|det|>[[120, 660, 320, 686]]<|/det|>
\[\delta = 3 \quad \omega = 6\]

<|ref|>equation<|/ref|><|det|>[[120, 695, 558, 725]]<|/det|>
\[y(x) = e^{-3x} \cdot (A \cdot \cos(6x) + B \cdot \sin(6x))\]