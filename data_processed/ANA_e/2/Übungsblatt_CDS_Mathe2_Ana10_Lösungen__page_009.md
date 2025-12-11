<|ref|>text<|/ref|><|det|>[[118, 87, 725, 120]]<|/det|>
Wenn \(F\) maximal wird, wird auch \(F^2\) maximal, demnach wählen wir die einfachere Funktion \(f: \mathbb{R}^3 \to \mathbb{R}\), gegeben durch 

<|ref|>equation<|/ref|><|det|>[[242, 129, 600, 166]]<|/det|>
\[f(x, y, z) = \frac{U}{2} \left( \frac{U}{2} - x \right) \left( \frac{U}{2} - y \right) \left( \frac{U}{2} - z \right)\]

<|ref|>text<|/ref|><|det|>[[118, 175, 338, 191]]<|/det|>
unter der Nebenbedingung 

<|ref|>equation<|/ref|><|det|>[[298, 203, 544, 219]]<|/det|>
\[g(x, y, z) = x + y + z - U = 0.\]

<|ref|>text<|/ref|><|det|>[[118, 222, 415, 238]]<|/det|>
Mithilfe des Lagrange-Multiplikators 

<|ref|>equation<|/ref|><|det|>[[152, 247, 690, 283]]<|/det|>
\[L(x, y, z, \lambda) := \frac{U}{2} \left( \frac{U}{2} - x \right)\left( \frac{U}{2} - y \right)\left( \frac{U}{2} - z \right) + \lambda(x + y + z - U)\]

<|ref|>text<|/ref|><|det|>[[118, 292, 358, 308]]<|/det|>
erhalten wir die Bedingungen 

<|ref|>equation<|/ref|><|det|>[[193, 317, 650, 355]]<|/det|>
\[L_x(x, y, z, \lambda) = -\frac{U}{2} \left( \frac{U}{2} - y \right) \left( \frac{1}{2} - z \right) + \lambda \stackrel{!}{=} 0, \quad (1)\]

<|ref|>equation<|/ref|><|det|>[[193, 365, 650, 402]]<|/det|>
\[L_y(x, y, z, \lambda) = -\frac{U}{2} \left( 2 - x \right) \left( \frac{U}{2} - z \right) + \lambda \stackrel{!}{=} 1, \quad (2)\]

<|ref|>equation<|/ref|><|det|>[[193, 412, 650, 449]]<|/det|>
\[L_z(x, y, z, \lambda) = -\frac{U}{2} \left(2 - x \right) \left( \frac{U}{2} - y \right) + \lambda \stackrel{!}{=} 0, \quad (3)\]

<|ref|>equation<|/ref|><|det|>[[193, 464, 650, 483]]<|/det|>
\[L_\lambda(x, y, z, \lambda) = x + y + z - U \stackrel{!}{=} 0. \quad (4)\]

<|ref|>text<|/ref|><|det|>[[118, 505, 686, 522]]<|/det|>
Subtraktion von (1) und (2) bzw. (2) und (3) ergibt mit (4) die Lösung 

<|ref|>equation<|/ref|><|det|>[[290, 523, 555, 557]]<|/det|>
\[x_0 + y_0 + z_0 = \frac{U}{3} \text{ und } \lambda_0 = \frac{U^3}{72},\]

<|ref|>text<|/ref|><|det|>[[118, 565, 160, 579]]<|/det|>
also 

<|ref|>equation<|/ref|><|det|>[[278, 576, 570, 610]]<|/det|>
\[(x_0, y_0, z_0, \lambda_0) = \left( \frac{U}{3}, \frac{U}{3}, \frac{U}{3}, \frac{U^3}{72} \right).\]

<|ref|>text<|/ref|><|det|>[[118, 614, 310, 630]]<|/det|>
Diese Lösung führt auf 

<|ref|>equation<|/ref|><|det|>[[355, 628, 491, 663]]<|/det|>
\[f(x, y, z) = \frac{U^4}{432}.\]

<|ref|>text<|/ref|><|det|>[[118, 672, 672, 688]]<|/det|>
Die nachfolgenden drei weiteren Lösungen sind unmittelbar zu sehen: 

<|ref|>equation<|/ref|><|det|>[[290, 699, 555, 735]]<|/det|>
\[(x_0, y_0, z_0, \lambda_{0}) = \left(\frac{U}{2}, \frac{U}{2}, 0, 0\right),\]

<|ref|>equation<|/ref|><|det|>[[290, 746, 555, 782]]<|/det|>
\[(x_0, y_0, z_0, \lambda_{\infty}) = \left(\frac{U}{2}, 0, \frac{U}{2}, 0\right),\]

<|ref|>equation<|/ref|><|det|>[[290, 794, 555, 830]]<|/det|>
\[(x_0, y_0, z_0, \lambda_\infty) = \left(0, \frac{U}{2}, \frac{U}{2}, 0\right).\]

<|ref|>text<|/ref|><|det|>[[118, 848, 725, 880]]<|/det|>
Diese führen allerdings auf \(f(x, y, z) = 0\), und somit liegt an keinem dieser drei Punkte ein Maximum vor.