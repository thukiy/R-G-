<|ref|>text<|/ref|><|det|>[[114, 85, 140, 100]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[114, 100, 365, 117]]<|/det|>
mittels partieller Integration 

<|ref|>equation<|/ref|><|det|>[[127, 120, 785, 317]]<|/det|>
\[
\begin{align*}
F(t) &= \int \mathrm{e}^{at} \cdot \sin(\omega t) \, \mathrm{d}t = \frac{1}{a} \cdot \mathrm{e}^{at} \cdot \sin(\omega t) - \frac{\omega}{a} \int \mathrm{e}^{at} \cdot \cos(\omega t) \, \mathrm{d}t \\
&= \frac{1}{a} \cdot \mathrm{e}^{at} \cdot \sin (\omega t) - \frac{\omega}{a} \cdot \left( \frac{1}{a} \cdot \mathrm{e}^{at} \cdot \cos(\omega t) - \frac{\omega}{a} \int \mathrm{e}^{at}(\cdot - 1) \cdot \sin(\omega t) \, \mathrm{d}t \right) \\
&= \frac{1}{a} \cdot \mathrm{e}^{at} \cdot (\sin(\omega t) - \frac{\omega}{a^2} \cdot \mathrm{e}^{at} \cdot \cos(\omega t) - \left( \frac{\omega^2}{a^2} \int \mathrm{e}^{at} \cdot \sin(\omega t) \, \mathrm{dt} \right) \\
&= \mathrm{e}^{at} \cdot \left( \frac{1}{a} \cdot \sin(\omega t) - \frac{\omega}{a^2} \cdot \cos(\omega t) \right) - \frac{\omega^2}{a^2} \cdot F(t).
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[125, 323, 234, 341]]<|/det|>
Es gilt also 

<|ref|>equation<|/ref|><|det|>[[153, 350, 840, 490]]<|/det|>
\[
\begin{align*}
F(t) &= \mathrm{e}^{at} \cdot \left( \frac{1}{a} \sin(\omega t) - \frac{\omega}{a^2} \cdot \mathrm{cos}(\omega t) \right) - \frac{\omega^2}{a^2} \left. F(t) \right| + \frac{\omega^2}{a^2} \cdot F(t) \\
F(t) + \frac{\omega^2}{a^2} \cdot F(t) &= \mathrm{e}^{at} \cdot \left( \frac{1}{2} \sin(\omega t) - \frac{\omega}{a^2} \cdot (\cos(\omega t)) \right) \\
\left( 1 + \frac{\omega^2}{a^2} \right) \cdot F(t) &= \mathrm{e}^{at} \cdot \left( \frac{\omega}{a} \sin(\omega t) - \frac{\omega}{a^2} (\cos(\omega t)) \right) \quad \left| \cdot \left( 1 + \frac{\omega^2}{a^2} \right) \right|.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[135, 498, 317, 515]]<|/det|>
Daraus erhalten wir 

<|ref|>equation<|/ref|><|det|>[[135, 524, 870, 620]]<|/det|>
\[
\begin{align*}
F(t) &= \frac{\mathrm{e}^{at} \cdot \left( \frac{1}{a} \cdot (\sin(\omega t) - \frac{\omega}{a^2} ) \cdot \cos(\omega t) \right)}{(1 + \frac{\omega^2}{a^2})} + c = \frac{\mathrm{e}^{at} \cdot \left( \frac{1}{a^2} \cdot (\sin(\omega t) - \frac{\omega}{a^2} - \cos(\omega t)) \right) \cdot a^2}{(1 + \frac{\omega^2}{a^2})} + c \\
&= \frac{\mathrm{e}^{at} \cdot (a \cdot \sin(\omega t) - \omega \cdot \cos(\omega t))}{a^2 + \omega^2} + c.
\end{align*}
\]