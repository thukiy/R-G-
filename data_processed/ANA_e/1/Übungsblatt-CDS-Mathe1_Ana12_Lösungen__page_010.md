<|ref|>text<|/ref|><|det|>[[117, 65, 888, 85]]<|/det|>
S3 Kandidatenvergl eich: Wir stellen die Ergebnisse in der folgenden Tabelle zusammen. 

<|ref|>table<|/ref|><|det|>[[194, 93, 810, 151]]<|/det|>
<table><tr><td>k</td><td>xk</td><td>Lk</td><td>Bk</td><td>Hk</td><td>Ak</td><td>Typ</td></tr><tr><td>1</td><td>30.0 cm</td><td>30.0 cm</td><td>15.0 cm</td><td>20.0 cm</td><td>27.0 dm²</td><td>globales Minimum</td></tr></table>

<|ref|>text<|/ref|><|det|>[[117, 162, 678, 181]]<|/det|>
Die Oberfläche der Kiste ist also genau dann minimal, wenn gilt 

<|ref|>equation<|/ref|><|det|>[[286, 192, 888, 210]]<|/det|>
\[L \approx 30.0 \text{ cm}, \quad B \approx 15.0 \text{ cm} \quad \text{und} \quad H \approx 20.0 \text{ cm}. \quad (106)\]

<|ref|>text<|/ref|><|det|>[[88, 231, 888, 284]]<|/det|>
b) Wir betrachten eine zylinderförmige Konservendose mit Radius R und Höhe H. Aus der Elementargeometrie wissen wir, dass Oberfläche und Volumen eines Kreiszylinders berechnet werden können durch 

<|ref|>equation<|/ref|><|det|>[[327, 294, 888, 313]]<|/det|>
\[A = 2\pi R^2 + 2\pi RH \quad \text{bzw.} \quad V = \pi R^2 H. \quad (107)\]

<|ref|>text<|/ref|><|det|>[[117, 325, 888, 343]]<|/det|>
Wenn die gesuchte Konservendose genau einen Liter fassen soll, dann muss demnach gelten 

<|ref|>equation<|/ref|><|det|>[[117, 353, 888, 373]]<|/det|>
\[V = \pi R^2 H = 1.001 = 1.00 \text{ dm}^3. \quad (108)\]

<|ref|>text<|/ref|><|det|>[[117, 384, 822, 403]]<|/det|>
Zunächst formulieren wir die Aufgabe als Optimierungsproblem. Dazu wählen wir 

<|ref|>equation<|/ref|><|det|>[[125, 412, 888, 454]]<|/det|>
\[x := R \quad (\text{unabhängige Variable}) \quad (109)\]
\[A := 2\pi R^2 + 2\pi RH \equiv \text{Oberfläche der Dose} \quad (\text{zu optimierende Variable}).\]

<|ref|>text<|/ref|><|det|>[[117, 463, 888, 499]]<|/det|>
Wir drücken nun sämtliche Variablen des Problems durch die unabhängige Variable x aus.
Mit Hilfe von (108) erhalten wir 

<|ref|>equation<|/ref|><|det|>[[117, 509, 888, 530]]<|/det|>
\[R(x) = x \quad (110)\]

<|ref|>equation<|/ref|><|det|>[[117, 537, 888, 577]]<|/det|>
\[H(x) = \frac{V}{\pi R^2(x)} = \frac{V}{\pi x^2} \quad (111)\]

<|ref|>equation<|/ref|><|det|>[[117, 579, 888, 617]]<|/det|>
\[A(x) = 2\pi R^2(x) + 2\pi R(x)H(x) = 2\pi x^2 + 2\pi x \frac{V}{\pi x^2} = 2\pi x^2 + \frac{2V}{x}. \quad (112)\]

<|ref|>text<|/ref|><|det|>[[117, 623, 888, 660]]<|/det|>
Der Radius eines Kreiszylinders ist immer positiv, d.h. \(R \ge 0\). Weil in (111) und (112) die unabhängige Variable x im Nenner steht, muss sogar gelten 

<|ref|>equation<|/ref|><|det|>[[450, 671, 888, 689]]<|/det|>
\[x = R > 0. \quad (113)\]

<|ref|>text<|/ref|><|det|>[[117, 701, 857, 720]]<|/det|>
Wir suchen somit das globale Minimum der Funktion \(A(x)\) auf dem offenen Intervall 

<|ref|>equation<|/ref|><|det|>[[446, 730, 888, 750]]<|/det|>
\[I := ]0, \infty[. \quad (114)\]

<|ref|>text<|/ref|><|det|>[[117, 760, 580, 779]]<|/det|>
Dabei gehen wir gemäss den folgenden Schritten vor. 

<|ref|>text<|/ref|><|det|>[[117, 783, 561, 802]]<|/det|>
S1 Kritische Stellen: Die Ableitung von \(A(x)\) ist 

<|ref|>equation<|/ref|><|det|>[[160, 810, 888, 847]]<|/det|>
\[A'(x) = 2\pi \cdot 2x^{2-1} + (-1) \cdot \frac{2V}{x^{1+1}} = 4\pi x - \frac{2V}{x^2}. \quad (115)\]

<|ref|>text<|/ref|><|det|>[[160, 853, 770, 873]]<|/det|>
Wir bestimmen die kritischen Stellen von \(A(x)\). Für diese muss gelten 

<|ref|>equation<|/ref|><|det|>[[409, 881, 888, 919]]<|/det|>
\[0 = A'(x) = 4\pi x - \frac{2V}{x^2} \quad \left| + \frac{2V}{x^2} \right. \quad (116)\]