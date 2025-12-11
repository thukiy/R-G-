<|ref|>sub_title<|/ref|><|det|>[[25, 10, 490, 43]]<|/det|>
## Methode der Charakteristiken 

<|ref|>text<|/ref|><|det|>[[45, 53, 950, 85]]<|/det|>
- für lineare PDGL 1. Ordnung, die homogen oder inhomogen sein kann 

<|ref|>text<|/ref|><|det|>[[45, 90, 830, 121]]<|/det|>
- häufig für Transportgleichungen verwendet (Verkehrsdynamik, 

<|ref|>text<|/ref|><|det|>[[68, 128, 365, 157]]<|/det|>
Ausbreitung von Gasen) 

<|ref|>text<|/ref|><|det|>[[20, 180, 456, 220]]<|/det|>
**Bsp:** \(\frac{du(\vec{x}, t)}{dt} + \langle \vec{a}, \nabla u(\vec{x}, t) \rangle = 0\) 

<|ref|>text<|/ref|><|det|>[[115, 223, 608, 255]]<|/det|>
\(\vec{a}, \vec{x} \in \mathbb{R}^n, t \in \mathbb{R}, u: \mathbb{R}^n \times \mathbb{R} \to \mathbb{R}\) 

<|ref|>text<|/ref|><|det|>[[115, 262, 375, 290]]<|/det|>
AB: \(u(\vec{x}, 0) = q(\vec{x})\) 

<|ref|>text<|/ref|><|det|>[[100, 300, 920, 333]]<|/det|>
→ eine Seite der PDGL entspricht der Richtungsabbildung von \(u\) 

<|ref|>text<|/ref|><|det|>[[145, 338, 500, 370]]<|/det|>
in Richtung \((a_1 \dots a_n \ 1)^T\) 

<|ref|>text<|/ref|><|det|>[[145, 377, 415, 408]]<|/det|>
Richtungsabbildung: 

<|ref|>text<|/ref|><|det|>[[195, 415, 672, 444]]<|/det|>
von \(f(\vec{x})\) in Richtung \(\vec{a}\) : \(\langle \nabla f(\vec{x}), \vec{a} \rangle\) 

<|ref|>equation<|/ref|><|det|>[[195, 447, 500, 533]]<|/det|>
\[ \mathbb{L} \propto \begin{pmatrix} \frac{\partial u}{\partial x_1} \\ \vdots \\ \frac{\partial u}{\partial x_n} \end{pmatrix}, \begin{pmatrix} a_1 \\ \vdots \\ a_n \\ 1 \end{pmatrix} \]

<|ref|>text<|/ref|><|det|>[[100, 567, 425, 595]]<|/det|>
→ definiere \(w: \mathbb{R} \to \mathbb{R}\) 

<|ref|>equation<|/ref|><|det|>[[195, 604, 480, 630]]<|/det|>
\[ w(s) = u(\vec{x} + s\vec{a}, t + s) \]

<|ref|>equation<|/ref|><|det|>[[195, 633, 920, 720]]<|/det|>
\[ \mathbb{L} w'(s) = \frac{\partial w}{\partial s} = \frac{\partial w}{\partial x_1} \frac{\partial x_1}{\partial s} + \frac{\partial w}{\partial x_2} \frac{\partial x_2}{\partial s} + \dots + \frac{\partial w}{\partial x_n} \frac{\partial x_n}{\partial s} \\ = a_1 \frac{\partial u(\vec{x} + s\vec{a}, t + s)}{\partial x_1} + \dots + a_n \frac{\partial u(\vec{x} + s\vec{a}, t + s)}{\delta x_n} + 1 \cdot \frac{\partial u(\vec{x} + s\vec{a}, t + s)}{\dot{s}} = 0 \]

<|ref|>text<|/ref|><|det|>[[100, 740, 920, 770]]<|/det|>
→ \(w'(s) = 0\) und \(w(s)\) ist konstant, d.h. wir können als Argument 

<|ref|>text<|/ref|><|det|>[[145, 778, 930, 808]]<|/det|>
von \(w\) einen beliebigen Wert einsehen und erhalten immer denselben 

<|ref|>text<|/ref|><|det|>[[145, 817, 320, 842]]<|/det|>
Funktionswert 

<|ref|>equation<|/ref|><|det|>[[100, 853, 572, 920]]<|/det|>
\[ \begin{aligned} \mathbb{L} u(\vec{x}, t) &= w(0) = w(-t) = u(\vec{x} - t\vec{a}, 0) \\ &= q(\vec{x} - t\vec{a}) \end{aligned} \]

<|ref|>text<|/ref|><|det|>[[100, 930, 955, 959]]<|/det|>
→ zum Zeitpunkt \(t = 0\) wird ein Funktionswert an Stelle \(\vec{y}\) mit Geschw. 

<|ref|>text<|/ref|><|det|>[[145, 967, 550, 995]]<|/det|>
\(|\vec{a}|\) in Richtung \(\vec{a}\) transportiert: