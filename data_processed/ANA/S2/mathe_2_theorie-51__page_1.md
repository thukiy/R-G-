<|ref|>image<|/ref|><|det|>[[45, 12, 333, 230]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[25, 266, 610, 293]]<|/det|>
Bogenlänge (Lennen wir schon von Integration) : 

<|ref|>equation<|/ref|><|det|>[[60, 299, 825, 333]]<|/det|>
\[s = \int_a^b \sqrt{1 + y'(x)^2} \, dx \quad \text{Paramehüsierung : } (f(x))\]

<|ref|>equation<|/ref|><|det|>[[60, 339, 512, 373]]<|/det|>
\[s(y(t)) = \int_a^b \sqrt{\dot{x}_1(t)^2 + \ldots + \dot{x}_m(t)^2} \, dt\]

<|ref|>text<|/ref|><|det|>[[20, 404, 515, 431]]<|/det|>
häufig verwendete Paramehüsierungen : 

<|ref|>text<|/ref|><|det|>[[45, 441, 230, 467]]<|/det|>
- Kreis im \(\mathbb{R}^2\) 

<|ref|>equation<|/ref|><|det|>[[70, 465, 888, 600]]<|/det|>
\[ \begin{aligned} \vec{\gamma}(t) &= \vec{m} + \begin{pmatrix} r \cdot \cos t \\ r \cdot \sin t \end{pmatrix} \\ &= \vec{m} + r \begin{pmatrix} \cos(\omega t) \\ \sin(\omega t) \end{pmatrix} \end{aligned} \quad \begin{aligned} \vec{m} : \text{Nullpunkt} \\ r : \text{Radius} \\ t = [0, 2\pi] \end{aligned} \quad \text{T : Periodendauer} \quad \omega = \frac{2\pi}{t} : \text{Kreislegung} \]

<|ref|>text<|/ref|><|det|>[[45, 618, 550, 645]]<|/det|>
- Graph eine Funktion \(f: [x_0, x_E] \to \mathbb{R}\) 

<|ref|>equation<|/ref|><|det|>[[82, 652, 255, 703]]<|/det|>
\[ \vec{\gamma}(t) = \begin{pmatrix} t \\ f(t) \end{pmatrix} \]

<|ref|>text<|/ref|><|det|>[[20, 732, 528, 763]]<|/det|>
Bsp : \(f(t) = \begin{pmatrix} r \cos t \\ r \sin t \end{pmatrix}\) \(t \in [0, 2\pi]\) 

<|ref|>equation<|/ref|><|det|>[[147, 768, 610, 899]]<|/det|>
\[ \begin{aligned} s(\vec{\gamma}) &= \frac{2\pi}{t} \sqrt{(-r \sin t)^2 + (r \cos t)^2} \quad \text{dt} \\ &= r^2 \sin^2 t + r^2 \cos^2 t \\ &= r^2 (\sin^2 t + \cos^2 t) = r^2 \\ &= \frac{2\pi}{t} r \, \text{dt} = r [t]_0^{2\pi} = 2\pi r \end{aligned} \]