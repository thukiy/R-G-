<|ref|>title<|/ref|><|det|>[[115, 183, 476, 217]]<|/det|>
Übungsblatt Ana 4 

<|ref|>text<|/ref|><|det|>[[579, 196, 880, 232]]<|/det|>
Computational and Data Science
FS2024 

<|ref|>text<|/ref|><|det|>[[115, 250, 270, 278]]<|/det|>
Lösungen 

<|ref|>text<|/ref|><|det|>[[750, 258, 880, 275]]<|/det|>
Mathematik 2 

<|ref|>text<|/ref|><|det|>[[115, 304, 210, 321]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 321, 765, 355]]<|/det|>
- Sie kennen den Begriff uneigentliches Integral und dessen wichtigste Eigenschaften. 

<|ref|>text<|/ref|><|det|>[[115, 354, 770, 389]]<|/det|>
- Sie können die Existenz eines uneigentlichen Integrals beurteilen und gegebenenfalls seinen Wert berechnen. 

<|ref|>sub_title<|/ref|><|det|>[[115, 419, 515, 437]]<|/det|>
1. Aussagen über uneigentliche Integrale 

<|ref|>text<|/ref|><|det|>[[115, 436, 680, 454]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[115, 451, 880, 635]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Alle uneigentlichen Integrale müssen über eine Grenzwertbildung bestimmt werden.</td><td>X</td><td></td></tr><tr><td>b) Alle uneigentlichen Integrale erkennt man daran, dass mindestens eine der Grenzen \(-\infty\) oder \(\infty\) ist.</td><td></td><td>X</td></tr><tr><td>c) Falls das uneigentliche Integral \(I = \int_{0}^{\infty} f(x) dx\) existiert, dann gilt: \(I = \lim_{t \to \infty} \int_{0}^{t} f(x) dx\).</td><td>X</td><td></td></tr><tr><td>d) Falls der Grenzwert \(I = \lim_{t \to \infty} \int_{0}^{t} \frac{f(x)}{x} dx\) konvergiert, dann gilt: \(I = \int_{0}^{\infty} \frac{f(x)}{x} dx\).</td><td>X</td><td></td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[115, 650, 366, 667]]<|/det|>
2. Uneigentliche Integrale 

<|ref|>text<|/ref|><|det|>[[115, 666, 704, 684]]<|/det|>
Berechnen Sie, sofern möglich, den Wert der folgenden Integrale. 

<|ref|>equation<|/ref|><|det|>[[115, 682, 755, 762]]<|/det|>
\[
\begin{align*}
a) \int_{0}^{\infty} e^{-x} dx & \qquad b) \int_{0}^{\infty} 2^{-x} dx & \qquad c) \int_{1}^{\infty} \frac{1}{x} dx \\
d) \int_{1}^{\infty} \frac{1}{x^2} dx & \qquad e) \int_{0}^{1} \frac{1}{x} dx & \qquad f) \int_{0}^{1} \frac{1}{\sqrt{x}} dx \\
g) \int_{-\infty}^{\infty} e^{-|x|} dx & \qquad h) \int_{-\infty}^{\infty} \frac{1}{x^2} dx & \qquad i) \int_{-\infty}^{\infty} \frac{1}{1+x^2} dx
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 775, 144, 792]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[120, 790, 880, 829]]<|/det|>
\[
\frac{I}{I} = \int_{0}^{\infty} e^{-x} dx = \lim_{s \to \infty} \int_{0}^{s} e^{-x} dx = \lim_{s \to \infty} \left[ -e^{-x} \right]_{0}^{s} = \lim_{s \to \infty} \left( -e^{-s} + e^{-0} \right) = 0 + 1 = \frac{1}{e}.
\]