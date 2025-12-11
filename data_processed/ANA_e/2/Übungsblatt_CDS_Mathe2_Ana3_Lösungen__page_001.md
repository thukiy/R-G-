<|ref|>title<|/ref|><|det|>[[115, 183, 476, 216]]<|/det|>
Übungsblatt Ana 3 

<|ref|>text<|/ref|><|det|>[[578, 196, 881, 231]]<|/det|>
Computational and Data Science
FS2024 

<|ref|>text<|/ref|><|det|>[[115, 250, 270, 277]]<|/det|>
Lösungen 

<|ref|>text<|/ref|><|det|>[[750, 258, 880, 275]]<|/det|>
Mathematik 2 

<|ref|>text<|/ref|><|det|>[[115, 303, 210, 320]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 320, 852, 354]]<|/det|>
- Sie kennen die Begriffe Integral, Stammfunktion, partielle Integration und deren wichtigste Eigenschaften. 

<|ref|>text<|/ref|><|det|>[[115, 353, 855, 386]]<|/det|>
- Sie können die partielle Integration anwenden, um bestimmte und unbestimmte Integrale zu berechnen. 

<|ref|>text<|/ref|><|det|>[[115, 386, 852, 419]]<|/det|>
- Sie können bestimmte Integrale näherungsweise auf eine vorgegebene Anzahl Dezimalstellen mit Python/Numpy berechnen. 

<|ref|>sub_title<|/ref|><|det|>[[115, 452, 480, 469]]<|/det|>
1. Aussagen über partielle Integration 

<|ref|>text<|/ref|><|det|>[[115, 468, 679, 485]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[115, 483, 878, 670]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Die Methode der partiellen Integration basiert auf der Produktregel der Differentialrechnung.</td><td>X</td><td></td></tr><tr><td>b) Mit Hilfe der partiellen Integration kann jedes Produkt von 2 Funktionen integriert werden.</td><td></td><td>X</td></tr><tr><td>c) Um ein Produkt von 2 Funktionen mit partieller Integration integrieren zu können, muss man mindestens einen der Faktoren allein integrieren können.</td><td>X</td><td></td></tr><tr><td>d) Mit Hilfe der partiellen Integration kann das Integral einer beliebigen differentierbaren Funktion f(x) auf die Berechnung des Integrals von x · f'(x) zurückgeführt werden und umgekehrt.</td><td>X</td><td></td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[115, 686, 660, 703]]<|/det|>
2. Stammfunktionen mit partieller Integration bestimmen 

<|ref|>text<|/ref|><|det|>[[115, 702, 866, 735]]<|/det|>
Berechnen Sie die folgenden unbestimmten Integrale mit der Methode der partiellen Integration. 

<|ref|>equation<|/ref|><|det|>[[115, 734, 633, 826]]<|/det|>
\[
\begin{align*}
a) \int x e^x dx & \qquad b) \int x^2 e^x dx \\
c) \int x \sin x dx & \qquad d) \int x \cos x dx \\
e) \int x^2 \sin x dx & \qquad f) \int x^2 \cos x dx \\
g) \int (\sin x)^2 dx & \qquad h) \int (\cos x)^2 dx \\
i) \int (\sinh x)^2 dx & \qquad j) \int (\cosh x)^2 dx
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[115, 840, 761, 890]]<|/det|>
\[
\begin{align*}
a) \quad & \quad \int \downarrow \uparrow \\
F(x) = \int x \cdot e^x dx = x e^x - \int 1 \cdot e^x dx = x e^x - e^x + c = (x - 1) e^x + c.
\end{align*}
\]