<|ref|>equation<|/ref|><|det|>[[118, 85, 880, 170]]<|/det|>
\[
\begin{align*}
F(\omega) &= a^2 I_1 - I_2 = \frac{2a^2 \cdot \sin(\omega a)}{\omega} - \frac{2a^2 \cdot \sin(\omega a)}{\omega} - \underbrace{4a \cdot \cos(\omega a)}_{\omega^2} + \underbrace{4 \cdot \sin(\omega a)}_{\omega^3} = \\
&= \frac{4[\sin(\omega a) - a\omega \cdot \cos(\omega a)]}{\omega^3}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 174, 207, 192]]<|/det|>
Integrale: 

<|ref|>equation<|/ref|><|det|>[[114, 213, 544, 300]]<|/det|>
\[
\begin{align*}
(312) \quad & \int e^{ax} dx = \frac{1}{a} \cdot e^{ax} \\
(314) \quad & \int x^2 \cdot e^{ax} dx = \left( \frac{a^2 x^2 - 2ax + 2}{a^3} \right) \cdot e^{ax}
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[114, 315, 468, 333]]<|/det|>
3. Fourier-Transformation einer DGL 

<|ref|>text<|/ref|><|det|>[[114, 332, 456, 350]]<|/det|>
Gegeben sei die Differentialgleichung 

<|ref|>equation<|/ref|><|det|>[[114, 348, 300, 367]]<|/det|>
\[
\dot{x} = 2x + \sigma(t) \cdot e^{-3t}.
\]

<|ref|>text<|/ref|><|det|>[[114, 365, 765, 384]]<|/det|>
Berechnen Sie die Lösung der DGL mit Hilfe der Fourier-Transformation. 

<|ref|>text<|/ref|><|det|>[[118, 398, 640, 417]]<|/det|>
Mit Hilfe einer Fourier-Transformationstabelle finden wir 

<|ref|>equation<|/ref|><|det|>[[114, 430, 312, 521]]<|/det|>
\[
\begin{align*}
x & \circ \bullet X \\
i & \circ \bullet i\omega X \\
\sigma(t) & \circ \bullet \frac{1}{i\omega + 3}.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 536, 272, 554]]<|/det|>
Einsetzen ergibt: 

<|ref|>equation<|/ref|><|det|>[[114, 553, 771, 628]]<|/det|>
\[
\begin{align*}
i\omega X &= 2X + \frac{1}{3 + i\omega} \quad \Big| - 2X \\
\iff i\omega X - 2X &= (i\omega - 2) \cdot X = \frac{1}{i\omega + 3} \quad \Big| : (i\omega - 2)
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 630, 300, 648]]<|/det|>
Daraus erhalten wir 

<|ref|>equation<|/ref|><|det|>[[114, 656, 520, 693]]<|/det|>
\[
X(\omega) = \frac{1}{i\omega - 2} \cdot \frac{1}{i\omega + 3} = \frac{1}{(i\omega - 2) \cdot (i\omega + 3)}.
\]

<|ref|>text<|/ref|><|det|>[[114, 693, 325, 711]]<|/det|>
Als Lösung ergibt sich: 

<|ref|>equation<|/ref|><|det|>[[118, 717, 600, 762]]<|/det|>
\[
\frac{1}{2\pi} \int_{-\infty}^{\infty} X(\omega) \cdot e^{i\omega t} d\omega = \frac{1}{2\pi} \int_{-\infty}^{\infty} \frac{e^{i\omega t}}{(i\omega - 2) \cdot (i\omega + 3)} d\omega
\]

<|ref|>sub_title<|/ref|><|det|>[[114, 781, 411, 799]]<|/det|>
4. Fourier-Rücktransformation 

<|ref|>text<|/ref|><|det|>[[114, 797, 841, 832]]<|/det|>
Bestimmen Sie zu den angegebenen Bildunktionen durch Rücktransformation die
Originalfunktion. 

<|ref|>equation<|/ref|><|det|>[[114, 830, 571, 858]]<|/det|>
a) \(F(\omega) = \frac{5}{(2+i\omega)^2}\) b) \(F(\omega) = \cos(5\omega)\)

<|ref|>equation<|/ref|><|det|>[[114, 856, 310, 885]]<|/det|>
c) \(F(\omega) = \frac{2}{5+i\omega} - \frac{3}{2+i\omega}\)