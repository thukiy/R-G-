<|ref|>title<|/ref|><|det|>[[115, 183, 476, 217]]<|/det|>
Übungsblatt 9 Ana 

<|ref|>text<|/ref|><|det|>[[577, 196, 880, 231]]<|/det|>
Computational and Data Science
FS2024 

<|ref|>text<|/ref|><|det|>[[115, 250, 270, 277]]<|/det|>
Lösungen 

<|ref|>text<|/ref|><|det|>[[750, 256, 880, 274]]<|/det|>
Mathematik 2 

<|ref|>text<|/ref|><|det|>[[115, 303, 210, 320]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 319, 875, 353]]<|/det|>
- Sie kennen die Begriffe partielle Ableitung, Tangentialebene, Gradient, totales Differential, Satz von Schwarz, Hesse-Matrix und deren wichtigste Eigenschaften. 

<|ref|>text<|/ref|><|det|>[[115, 353, 830, 386]]<|/det|>
- Sie können die partiellen Ableitungen von Funktionen in mehreren Variablen berechnen. 

<|ref|>text<|/ref|><|det|>[[115, 386, 839, 403]]<|/det|>
- Sie können die Tangentialebene in einem Punkt an ein Skalarfeld bestimmen. 

<|ref|>text<|/ref|><|det|>[[115, 403, 830, 436]]<|/det|>
- Sie können den Gradienten, das totale Differential und die Hesse-Matrix von Skalarfeldern bestimmen. 

<|ref|>sub_title<|/ref|><|det|>[[115, 468, 494, 486]]<|/det|>
1. Aussagen über partielle Ableitungen 

<|ref|>text<|/ref|><|det|>[[115, 485, 333, 503]]<|/det|>
Gegeben sei \(f: \mathbb{R}^n \to \mathbb{R}\). 

<|ref|>text<|/ref|><|det|>[[115, 502, 680, 519]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[115, 517, 880, 737]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Unter einer partiellen Ableitung von f versteht man die Ableitung nach einer der n Variablen, wobei die anderen Variablen wie Konstanten betrachtet werden.</td><td>X</td><td></td></tr><tr><td>b) Die partiellen Ableitungen können mit Hilfe des Differenzquotienten bestimmt werden.</td><td>X</td><td></td></tr><tr><td>c) Die Rechenregeln für Ableitungen von einer Funktion in einer Variablen gelten auch für partielle Ableitungen von Funktionen in mehreren Variablen.</td><td>X</td><td></td></tr><tr><td>d) Jede in einem Punkt P differenzierbare Funktion f ist dort partiell differenzierbar.</td><td>X</td><td></td></tr><tr><td>e) Aus der Existenz von \(grad(f(\vec{x}))\) folgt: die Tangentialebene an f ist in \(\vec{x}\) berechenbar.</td><td>X</td><td></td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[115, 752, 624, 770]]<|/det|>
2. Ableitungswerte von Funktionen in zwei Variablen 

<|ref|>text<|/ref|><|det|>[[115, 769, 790, 803]]<|/det|>
Bestimmen Sie für die nachfolgenden Funktionen die partiellen Ableitungen allgemein und an den gegebenen Stellen \((x_0, y_0)\). 

<|ref|>equation<|/ref|><|det|>[[115, 803, 515, 824]]<|/det|>
a) \(f(x, y) = \sqrt{2x + 3xy + 4y}, (x_0, y_0) = (1; 1)\)

<|ref|>equation<|/ref|><|det|>[[115, 822, 510, 842]]<|/det|>
b) \(f(x, y) = \cos(e^{xy} + xy), (x_0, y_0) = (0; 1)\)

<|ref|>equation<|/ref|><|det|>[[115, 840, 400, 859]]<|/det|>
c) \(f(x, y) = x^{2y}, (x_0, y_0) = (2; 1)\)

<|ref|>text<|/ref|><|det|>[[115, 857, 795, 876]]<|/det|>
Bestimmen Sie für die nachfolgenden Funktionen die partiellen Ableitun gen. 

<|ref|>equation<|/ref|><|det|>[[115, 874, 360, 892]]<|/det|>
d) \(z = f(x, y) = (2x - 3y^2)^5\)

<|ref|>equation<|/ref|><|det|>[[115, 890, 440, 910]]<|/det|>
e) \(z = f(x, y) = (x^3 - y^2) \cdot \cosh(xy)\)

<|ref|>equation<|/ref|><|det|>[[115, 908, 370, 927]]<|/det|>
f) \(z = f(x, y) = \ln(2x + e^{3y})\)