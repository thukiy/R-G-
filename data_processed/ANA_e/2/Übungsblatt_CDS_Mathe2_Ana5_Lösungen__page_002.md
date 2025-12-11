<|ref|>text<|/ref|><|det|>[[114, 81, 880, 120]]<|/det|>
a) Wie gross muss H gewählt werden, damit die Vase das Volumen \(V_0\) fassen kann?
b) Welche Masse hat die leere Vase, wenn sie aus Glas der Dichte \(p_g\) gefertigt ist? 

<|ref|>image<|/ref|><|det|>[[161, 133, 835, 333]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[114, 346, 150, 364]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[114, 362, 592, 381]]<|/det|>
Das Innenvolumen der Vase ergibt sich allgemein zu 

<|ref|>equation<|/ref|><|det|>[[114, 379, 707, 455]]<|/det|>
\[
\begin{align*}
V_i &= \pi \int_{x_i}^{H} f_i^2(x) \, \mathrm{d}x = \pi \int_{x_i}^{H} C^2 \cdot \left( \sqrt{x-x_i} \right)^2 \, \mathrm{d}x = \pi \cdot C^2 \int_{x_i}^{H} (x-x_i) \, \mathrm{d}x \\
&= \pi \cdot C^2 \cdot \frac{1}{2} \cdot \left[ (x-x_i)^2 \right] \bigg|_{x_i}^{H} = \frac{\pi \cdot C^2}{2} \cdot \left( (H-x_i)^2 - 0 \right) = \frac{\pi \cdot C^2}{2} \cdot (H-x_i)^2
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 453, 583, 472]]<|/det|>
Die Vase soll das vorgegebene Volumen \(V_0\) fassen: 

<|ref|>equation<|/ref|><|det|>[[114, 473, 550, 580]]<|/det|>
\[
\begin{align*}
V_0 &= V_i = \frac{\pi \cdot C^2}{2} \cdot (H - x_i)^2 \quad & \left| \cdot \frac{2}{\pi \cdot C^2} \right. \\
&= \frac{2}{\pi \cdot C^2} \cdot V_0 = (H - x_i)^2 \quad & \left| \sqrt{\dots} \right. \\
&= \sqrt{\frac{2}{\pi \cdot C^2}} \cdot V_0 = |H - x_i| = H - x_i \quad & \left| + x_i \right. \\
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 579, 410, 598]]<|/det|>
Somit erhalten wir für die Höhe: 

<|ref|>equation<|/ref|><|det|>[[114, 597, 447, 636]]<|/det|>
\[
\frac{H}{x} = x_i + \sqrt{\frac{2}{\pi \cdot C^2}} \cdot V_0 - x_i + \frac{1}{C} \cdot \sqrt{\frac{2}{\pi}} \cdot V_0.
\]

<|ref|>text<|/ref|><|det|>[[114, 639, 150, 657]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[114, 654, 863, 691]]<|/det|>
Um das Glasvolumen der Vase zu bestimmen, berechnen wir auch das sogenannte
Aussenvolumen \(V_a\) und ziehen von diesem anschliessend das Innenvolumen \(V_i\) ab: 

<|ref|>equation<|/ref|><|det|>[[114, 689, 770, 895]]<|/det|>
\[
\begin{align*}
V_a &= \pi \int_0^H f_a^2(x) \, \mathrm{d}x = \pi \int_0^H C^2 \cdot \left( \sqrt{x-x_a} \right)^2 \, \mathrm{d}x = \pi \cdot C^2 \cdot \int_0^H (x-x_a) \, \mathrm{d}x \\
&= \pi \cdot C^2 \cdot \frac 1 2 \cdot \left[ (x-x_a)^2 \right] \bigg|_0^H = \frac{\pi \cdot C^2}{2} \cdot \left( (x-x_a)^2 - (0-x_a)^2 \right) \\
&= \frac{\pi \cdot C^2}{2} \cdot \left( H^2 - 2 \cdot H \cdot x_a + x_a^2 - x_a^3 \right) = \frac{\pi \cdot C^2}{2} \cdot \left( H^3 - 2 \cdot H \cdot x_a \right) \\
V_g &= V_a - V_i = \frac{\pi \cdot C^2}{2} \cdot \left( H - 2 \cdot H \cdot x_a \right) - \frac{\pi \cdot C^2}{2} \cdot (H - x_i) \\
&= \frac{\pi \cdot C^2}{2} \cdot \left(H^2 - 2 \cdot H \cdot x_a - H^2 + 2 \cdot H \cdot x_i - x_i^2 \right) = \frac{\pi \cdot C^2}{2} \cdot \frac{1}{2} \cdot \left( 2 \cdot H \cdot (x_i - x_a) - x_i^2 \right) \\
&= \pi \cdot C^2 \cdot \left( H \cdot (x_i - x_a) - \frac{x_i^2}{2} \right).
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 895, 473, 914]]<|/det|>
Jetzt können wir die Masse bestimmen: