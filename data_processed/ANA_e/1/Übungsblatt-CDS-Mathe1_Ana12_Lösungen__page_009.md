<|ref|>equation<|/ref|><|det|>[[152, 64, 920, 150]]<|/det|>
\[
\begin{align*}
B(x) &= \frac{L(x)}{2} = \frac{x}{2} \tag{90} \\
H(x) &= \frac{V}{L(x)B(x)} = \frac{V}{x \cdot \frac{x}{2}} = \frac{2V}{x^2} \tag{91} \\
A(x) &= 2L(x) \cdot B(x) + 2L(x) \cdot H(x) + 2B(x) \cdot H(x) \\
&= 2 \cdot x \cdot \frac{x}{2} + 2 \cdot x \cdot \frac{2V}{x^2} + 2 \cdot \frac{x}{2} \cdot \frac{2V}{x^2} = x^2 + \frac{4V}{x} + \frac{2V}{x} = x^2 + \frac{6V}{x}. \tag{92}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[152, 216, 920, 252]]<|/det|>
Die Kanten eines Quaders sind immer positiv, d.h. \(L \ge 0\). Weil in (91) und (92) die
unabhängige Variable \(x\) im Nenner steht, muss sogar gelten 

<|ref|>equation<|/ref|><|det|>[[485, 260, 920, 277]]<|/det|>
\[
x = L > 0. \tag{93}
\]

<|ref|>text<|/ref|><|det|>[[152, 285, 888, 303]]<|/det|>
Wir suchen somit das globale Minimum der Funktion \(A(x)\) auf dem offenen Intervall 

<|ref|>equation<|/ref|><|det|>[[479, 310, 920, 329]]<|/det|>
\[
I := ]0, \infty[. \tag{94}
\]

<|ref|>text<|/ref|><|det|>[[152, 337, 610, 355]]<|/det|>
Dabei gehen wir gemäss den folgenden Schritten vor. 

<|ref|>text<|/ref|><|det|>[[152, 359, 593, 377]]<|/det|>
S1 Kritische Stellen: Die Ableitung von \(A(x)\) ist 

<|ref|>equation<|/ref|><|det|>[[193, 383, 920, 419]]<|/det|>
\[
A'(x) = 2x^{2-1} + (-1) \cdot \frac{6V}{x^{1+1}} = 2x - \frac{6V}{x^2}. \tag{95}
\]

<|ref|>text<|/ref|><|det|>[[193, 422, 802, 440]]<|/det|>
Wir bestimmen die kritischen Stellen von \(A(x)\). Für diese muss gelten 

<|ref|>equation<|/ref|><|det|>[[485, 446, 920, 483]]<|/det|>
\[
0 = A'(x) = 2x - \frac{6V}{x^2} \quad \left| + \frac{6V}{x^2} \right. \tag{96}
\]

<|ref|>equation<|/ref|><|det|>[[279, 490, 920, 528]]<|/det|>
\[
\Leftrightarrow \qquad \frac{6V}{x^2} = 2x \qquad \left| \cdot \frac{x^2}{2} \right. \tag{97}
\]

<|ref|>equation<|/ref|><|det|>[[279, 534, 920, 572]]<|/det|>
\[
\Leftrightarrow \qquad \frac{6V}{x^2}\cdot \frac{x^2}{2} = 3V = x^3 \qquad \left| \sqrt[3]{\cdots} \right. \tag{98}
\]

<|ref|>text<|/ref|><|det|>[[193, 576, 765, 594]]<|/det|>
Daraus erhalten wir genau eine kritische Stelle von \(A(x)\), nämlich 

<|ref|>equation<|/ref|><|det|>[[485, 600, 920, 621]]<|/det|>
\[
x_1 = \sqrt[3]{3V}. \tag{99}
\]

<|ref|>text<|/ref|><|det|>[[193, 630, 650, 648]]<|/det|>
Ferner berechnen wir gemäss (89) bis (92) die Werte 

<|ref|>equation<|/ref|><|det|>[[197, 655, 920, 678]]<|/det|>
\[
L_1 = L(x_1) = x_1 = \sqrt[3]{3V} \approx \sqrt[3]{3 \cdot 9.00 \text{ dm}^3} = \sqrt[3]{27 \text{ dm}^3} = 3.00 \text{ dm} = 30.0 \text{ cm} \quad (100)
\]

<|ref|>equation<|/ref|><|det|>[[197, 686, 920, 722]]<|/det|>
\[
B_1 = B(x_1) = \frac{x_1}{2} = \frac{L}{2} \approx \frac{1}{2} \cdot 3.00 \text{ dm} = 1.50 \text{ dm} = 15.0 \text{ cm} \quad (101)
\]

<|ref|>equation<|/ref|><|det|>[[193, 728, 920, 767]]<|/det|>
\[
H_1 = H(x_1) = \frac{2V}{x_1^2} = \frac{2V}{L^2} \approx 2 \cdot \frac{9.00 \text{ dm}^3}{(3.00 \text{ dm})^2} = 2.00 \text{ dm} = 20.0 \text{ cm} \quad (102)
\]

<|ref|>equation<|/ref|><|det|>[[197, 775, 920, 811]]<|/det|>
\[
A_1 = A(x_1) = x_1^2 + \frac{6V}{x_1} \approx (3.00 \text{ dm})^2 + \frac{6 \cdot 9.00 \text{ dm}^3}{3.00 \text{ dm}} = 27.0 \text{ dm}^2. \quad (103)
\]

<|ref|>text<|/ref|><|det|>[[152, 817, 824, 835]]<|/det|>
S2 Rand stellen: Das offene Intervall I hat keine Randstellen, es gilt jedoch 

<|ref|>equation<|/ref|><|det|>[[193, 840, 920, 875]]<|/det|>
\[
A(x) = x^2 + \frac{6V}{x} \xrightarrow{x \to 0} \infty \quad \text{und} \quad A(x) = x^2 + \frac{6V}{x} \xrightarrow{x\to\infty} \infty. \quad (104)
\]

<|ref|>text<|/ref|><|det|>[[193, 880, 920, 914]]<|/det|>
Die Oberfläche der Kiste ist demnach gegen beide Grenzen des Intervalls I nach oben
unbeschränkt.