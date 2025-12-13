<|ref|>text<|/ref|><|det|>[[25, 10, 333, 42]]<|/det|>
Bsp: \(\int \frac{x}{\sqrt{1-x^2}} \, dx\) 

<|ref|>equation<|/ref|><|det|>[[160, 68, 683, 98]]<|/det|>
\[f(q(x)) = \sqrt{1-x^2} \quad q(x) = 1-x^2 = z\]

<|ref|>equation<|/ref|><|det|>[[160, 103, 714, 140]]<|/det|>
\[q'(x) = \frac{dq(x)}{dx} = \frac{dz}{dx} = -2x \quad \iff \quad dx = -\frac{dz}{2x}\]

<|ref|>equation<|/ref|><|det|>[[160, 142, 560, 210]]<|/det|>
\[\rightarrow \int \frac{x}{\sqrt{z}} \cdot \left(-\frac{dz}{2x}\right) = -\frac{1}{2} \int \frac{1}{\sqrt{z}} \, dz\]

<|ref|>equation<|/ref|><|det|>[[220, 207, 880, 238]]<|/det|>
\[= -\frac{1}{2} \cdot 2z^{1/2} + c = -z^{1/2} + c = -\sqrt{z} + c = -\sqrt{1-x^2} + c\]

<|ref|>equation<|/ref|><|det|>[[160, 260, 671, 296]]<|/det|>
\[\int \frac{1}{1+(\ln x)^2} \cdot \frac{1}{x} \, dx = \int \frac{1}{x+x \cdot (\ln x)^2} \, dx\]

<|ref|>equation<|/ref|><|det|>[[160, 324, 682, 355]]<|/det|>
\[f(q(x)) = 1+(\ln x)^2 \quad q(x) = \ln x = z\]

<|ref|>equation<|/ref|><|det|>[[160, 358, 707, 395]]<|/det|>
\[q'(x) = \frac{dq(x)}{dx} = \left(\frac{dz}{dx}\right) = \frac{1}{x} \quad \iff \quad dx = x \cdot dz\]

<|ref|>equation<|/ref|><|det|>[[160, 398, 647, 432]]<|/det|>
\[\rightarrow \int \frac{1}{1+z^2} \cdot \frac{1}{x} \cdot x \cdot dz = \int \frac{1}{1+z^2} \, dz\]

<|ref|>equation<|/ref|><|det|>[[228, 440, 680, 466]]<|/det|>
\[= \text{arc tan } z + c = \text{arc tan } (\ln x) + c\]

<|ref|>sub_title<|/ref|><|det|>[[20, 518, 327, 545]]<|/det|>
## Numerische Integration 

<|ref|>text<|/ref|><|det|>[[55, 558, 728, 588]]<|/det|>
Teilweise Integration in geschlossener Form nicht möglich 

<|ref|>text<|/ref|><|det|>[[55, 593, 610, 627]]<|/det|>
2. B. \(\int e^{-x^2} \, dt\) nicht analytisch lösbar 

<|ref|>sub_title<|/ref|><|det|>[[25, 656, 201, 683]]<|/det|>
## Trapeziformel 

<|ref|>text<|/ref|><|det|>[[45, 695, 901, 765]]<|/det|>
\(f: \mathbb{R} \to \mathbb{R}\), Integrationsiniveau: \(a \le x \le b\) zulege \([a,b]\) in \(n\) gleich
grosse Teiliniveaule de Lange \(h = \frac{b-a}{n}\) 

<|ref|>text<|/ref|><|det|>[[75, 793, 780, 858]]<|/det|>
→ Stärkstellen: \(x_0 = a\), \(x_1 = x_0 + h\), \(x_2 = x_0 + 2h\) ...
\(x_n = b\) 

<|ref|>text<|/ref|><|det|>[[75, 868, 770, 897]]<|/det|>
→ Funktionswelt an Stärkstelle: \(f(x_n)\) heisst Stärkwert 

<|ref|>equation<|/ref|><|det|>[[125, 908, 625, 935]]<|/det|>
\[y_n = f(x_n) = f(x_0 + h \cdot n) \quad k = 0 \ldots n\]