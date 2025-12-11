<|ref|>text<|/ref|><|det|>[[114, 85, 140, 101]]<|/det|>
c) 

<|ref|>equation<|/ref|><|det|>[[114, 95, 330, 170]]<|/det|>
\[
\mathbf{f}(t) = \begin{cases} a^2 - t^2 |t| \le a \\ 0 |t| > a \end{cases}
\]

<|ref|>text<|/ref|><|det|>[[114, 185, 144, 201]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[114, 207, 880, 297]]<|/det|>
\[
\begin{align*}
F(\omega) &= \int_{-\infty}^{\infty} f(t) \cdot \mathrm{e}^{-\mathrm{i}\omega t} \, \mathrm{d}t = \int_{-T}^{T} A \cdot \mathrm{e}^{-\mathrm{i}\omega t} \, \mathrm{d}t = A \cdot \left[ \mathrm{e}^{-\mathrm{i}\omega t} \right]_{-T}^{T} = -A \cdot \left( \mathrm{e}^{-\mathrm{i}\omega T} - \mathrm{e}^{\mathrm{i}\omega T} \right) \\
&= \frac{2A}{\omega} \cdot \frac{\mathrm{e}^{\mathrm{i}\omega T} - \mathrm{e}^{-\mathrm{i}\omega T}}{2\mathrm{i}} = \frac{2A}{\omega} \cdot \sin(\omega T).
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 298, 144, 314]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[114, 313, 515, 330]]<|/det|>
Mit Hilfe von partieller Integration ergibt sich 

<|ref|>equation<|/ref|><|det|>[[114, 328, 880, 585]]<|/det|>
\[
\begin{align*}
F(\omega) &= \int_{-\infty}^{\infty}f(t) \cdot \mathrm{e}^{-\mathrm{i}\omega t} \, \mathrm{d} t = \int_{-T}^{T} A \cdot \left( 1 - \frac{|t|}{T} \right) \cdot \mathrm{e}^{-\mathrm{i}\omega t} \, \mathrm{d} \\
&= \left[ A \cdot \left( 1 - \frac{|t|}{T} \right) - \frac{1}{-\mathrm{i}\omega} \cdot \mathrm{e}^{-\mathrm{i}\omega t} \right]_{-T}^{T} - \int_{-T}^{T} A \cdot \left( 0 - \frac{\mathrm{sgn}(t)}{T} \right) \cdot \frac{1}{-\mathrm{i}\omega} \cdot \mathrm{e}^{-\mathrm{iw}t} \, \mathrm{d} \\
&= 0 - \frac{A}{\mathrm{i}\omega T} \int_{-T}^{T} \mathrm{sgn}(t) \cdot \mathrm{e}^{-\mathrm{iw}t} \, \mathrm{d} t = \frac{A}{\mathrm{i}\omega T} \cdot \left( \int_{-T}^{0} \mathrm{e}^{-\mathrm{iw}t} \, \mathrm{d} t - \int_{0}^{T} \mathrm{e}^{-\mathrm{iw}t} \, \mathrm{d} t \right) \\
&= \frac{A}{\mathrm{i}\omega T} \cdot \left( \frac{1}{-\mathrm{i}\omega} \cdot \left[ \mathrm{e}^{-\mathrm{iw}t} \right]_{-T}^{0} - \frac{1}{-\mathrm{i}\omega} \cdot \left[ \mathrm{e}^{- \mathrm{iw}t} \right]_{0}^{T} \right) = \frac{A}{\omega^2 T} \cdot \left( 1 - \mathrm{e}^{\mathrm{iw}T} + 1 - \mathrm{e}^{-\mathrm{iw}T} \right) \\
&= \frac{2A}{\omega^2 T} \cdot \left( 1 - \frac{\mathrm{e}^{\mathrm{iw}T} + \mathrm{e}^{-\mathrm{iw}T}}{2} \right) = \frac{2A}{\omega^2 T} \cdot \left( 1 -  \cos(\omega T) \right).
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 586, 144, 602]]<|/det|>
c) 

<|ref|>equation<|/ref|><|det|>[[120, 607, 802, 685]]<|/det|>
\[
F(\omega) = \int_{-a}^{a} (a^2 - t^2) \cdot \mathrm{e}^{-\mathrm{j}\omega t} \, dt = a^2 \cdot \int_{-a}^{a} \mathrm{e}^{-\mathrm{j}\omega t} \, dt - \int_{-a}^{a} t^2 \cdot \mathrm{e}^{-\mathrm{j}\omega t} \, dt = a^2 I_1 - I_2
\]

<|ref|>text<|/ref|><|det|>[[120, 690, 417, 707]]<|/det|>
Auswertung der Integrale \(I_1\) und \(I_2\): 

<|ref|>equation<|/ref|><|det|>[[120, 714, 825, 897]]<|/det|>
\[
\begin{align*}
I_1 &= \left[ \frac{\mathrm{e}^{-\mathrm{j}\omega t}}{-\mathrm{j}\omega} \right]_{-a}^{a} = \frac{\mathrm{e}^{\mathrm{j}\omega a} - \mathrm{e}^{-\mathrm{j}\omega a}}{\mathrm{j}\omega} = \frac{2 \cdot \sin(\omega a)}{\omega} && \text{(Integral: } 312 \text{ mit } a = -\mathrm{j}\omega\text{)} \\
I_2 &= \left[ \frac{(-\omega^2 t^2 + \mathrm{j} 2\omega t + 2) \cdot \mathrm{e}^{-\mathrm{j}\omega t}}{(-\mathrm{j}\omega)^3} \right]_{-a}^{a} = \\
&= \frac{\omega^2 a^2 (\mathrm{e}^{\mathrm{j}\omega a} - \mathrm{e}^{-\mathrm{j}\omega} a) + \mathrm{j} 2\omega a (\mathrm{e}^{\mathrm{j}\omega a} + \mathrm{e}^{-\mathrm{j}\omega a}) - 2 (\mathrm{e}^{\mathrm{j}\omega a} - \mathrm{e}^{-\mathrm{j} \omega a})}{\mathrm{j}\omega^3} = \\
&= \frac{2a^2 \cdot \sin(\omega a)}{\omega} + \frac{4a \cdot \cos(\omega a)}{\omega^2} - \frac{4 \cdot \sin(\omega a)}{\omega^3} && \text{(Integral: } 314 \text{ mit } a = -\mathrm{j}\omega\text{)} \\
\end{align*}
\]