<|ref|>equation<|/ref|><|det|>[[115, 81, 500, 116]]<|/det|>
\[
\frac{M_g}{g} = \rho_g \cdot V_g = \pi \cdot C^2 \cdot \rho_g \cdot \left( H \cdot (x_1 - x_a) - \frac{x_1^2}{2} \right).
\]

<|ref|>sub_title<|/ref|><|det|>[[115, 137, 571, 155]]<|/det|>
3. Volumen durch Integration des Querschnitts 

<|ref|>text<|/ref|><|det|>[[115, 153, 875, 205]]<|/det|>
Gegeben sei ein Körper, deren Grundfläche ein Kreis sei und der im Querschnitt aus
gleichseitigen Dreiecken besteht (siehe Skizze). Bestimmen Sie das Volumen des
Körpers durch Integration des Querschnitts. 

<|ref|>image<|/ref|><|det|>[[290, 205, 710, 415]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[115, 433, 872, 470]]<|/det|>
Wir bestimmen die Fläche der gleichseitigen Dreiecke, die eine Seitenlänge von s(x)
und eine Höhe h(x) haben, unter Zuhilfenahme des Satzes von Pythagoras. 

<|ref|>text<|/ref|><|det|>[[115, 467, 395, 486]]<|/det|>
Für den Kreis gilt: \(x^2 + y^2 = a^2\) 

<|ref|>text<|/ref|><|det|>[[115, 484, 636, 505]]<|/det|>
Für die Seitenlänge ergibt sich: \(s(x) = 2 \cdot y = 2 \cdot \sqrt{a^2 - x^2}\) 

<|ref|>text<|/ref|><|det|>[[115, 504, 686, 540]]<|/det|>
Für die Höhe ergibt sich: \(h(x) = \sqrt{(s(x))^2 - \left(\frac{1}{2}s(x)\right)^2} = \frac{\sqrt{3}}{2} \cdot s(x)\) 

<|ref|>text<|/ref|><|det|>[[115, 540, 610, 558]]<|/det|>
Dreick­sfläche (0,5 mal Grundseite mal Höhe) ist somit: 

<|ref|>equation<|/ref|><|det|>[[122, 558, 732, 593]]<|/det|>
\[
A(x) = \frac{\sqrt{3}}{4} \cdot s^2(x) = \frac{\sqrt{3}}{4} \cdot \left( 2 \cdot \sqrt{a^2 - x^2} \right)^2 = \frac{\sqrt{3}}{4} \cdot 4 \cdot (a^2 - x^2) = \sqrt{3} \cdot (a^2 - x^2)
\]

<|ref|>text<|/ref|><|det|>[[115, 591, 500, 609]]<|/det|>
Durch Integration ergibt sich das Volumen 

<|ref|>equation<|/ref|><|det|>[[115, 608, 744, 718]]<|/det|>
\[
\begin{align*}
\frac{V}{g} &= \int_{-a}^{a} A(x) \, \mathrm{d}x = 2 \int_{0}^{a} A(x) \, \mathrm{d}x = 2 \int_{0}^{0} \sqrt{3} \cdot (a^2 - x^2) \, \mathrm{d}x = 2 \cdot \sqrt{3} \int_{0}^{a} (a^2 - x^2) \, \mathrm{d}x \\
&= 2 \cdot \sqrt{3} \cdot \left[ a^2 \cdot x - \frac{1}{3} \cdot x^3 \right]_{0}^{a} = 2 \cdot \sqrt{3} \cdot \left( a^2 \cdot a - \frac{1}{3} \cdot a^3 - 0 + 0 \right) \\
&= 2 \cdot \sqrt{3} \cdot \left( a^3 - \frac{1}{3} \cdot a^3 \right) = 2 \cdot \sqrt{3} \cdot a^3 \cdot \left( 1 - \frac{1}{3} \right) = 2 \cdot \sqrt{3} \cdot a^3 \frac{2}{3} = \frac{4}{3} \cdot \sqrt{3} \cdot a^3.
\end{align*}
\]