<|ref|>title<|/ref|><|det|>[[115, 165, 456, 201]]<|/det|>
# Übungsblatt LA 6 

<|ref|>text<|/ref|><|det|>[[572, 179, 880, 216]]<|/det|>
Computational and Data Science
BSc HS2023 

<|ref|>text<|/ref|><|det|>[[115, 233, 270, 261]]<|/det|>
## Lösungen 

<|ref|>text<|/ref|><|det|>[[752, 240, 880, 258]]<|/det|>
Mathematik 1 

<|ref|>text<|/ref|><|det|>[[115, 287, 210, 305]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 303, 803, 355]]<|/det|>
- Sie kennen die Begriffe Sinus-, Cosinus-, Tangens-, Cotangensfunktion, Steigung, Additionstheorem, Multiplikationstheorem und trigonometrische Gleichung und deren wichtigste Eigenschaften. 

<|ref|>text<|/ref|><|det|>[[115, 353, 816, 387]]<|/det|>
- Sie können die Additions- und Multiplikationstheoreme für trigonometrische Funktionen anwenden. 

<|ref|>text<|/ref|><|det|>[[115, 386, 585, 404]]<|/det|>
- Sie können trigonometrische Gleichungen lösen. 

<|ref|>text<|/ref|><|det|>[[115, 402, 748, 421]]<|/det|>
- Sie können trigonometrische Gleichungen mit Python/Sympy lösen. 

<|ref|>sub_title<|/ref|><|det|>[[115, 451, 574, 469]]<|/det|>
### 1. Aussagen über trigonometrische Funktionen 

<|ref|>text<|/ref|><|det|>[[115, 467, 680, 485]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[115, 483, 880, 572]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Für alle \(x, y \in \mathbb{R}\) gilt: \(\sin(x + y) = \sin x \cdot \cos y + \cos x \cdot \sin y\).</td><td>X</td><td></td></tr><tr><td>b) Für alle \(x, y \in \mathbb{R}\) gilt: \(\cos(x + y) = \cos x \cdot \cos y + \sin x \cdot \sin y\).</td><td></td><td>X</td></tr><tr><td>c) Für alle \(x, y \in \mathbb{R}\) gilt: \(\tan(x - y) = \tan x \cdot \cot y - \cot x \cdot \tan y\).</td><td></td><td>X</td></tr><tr><td>d) Für alle \(\varphi \in \mathbb{R}\) gilt: \(\sin(2\varphi) = 2 \sin \varphi\).</td><td></td><td>X</td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[115, 587, 377, 604]]<|/det|>
### 2. Multiplikationstheoreme 

<|ref|>text<|/ref|><|det|>[[115, 603, 850, 638]]<|/det|>
Leiten Sie die folgenden Multiplikationsformeln mit Hilfe der Additionstheoreme für Sinus- und Cosinusfunktionen her. 

<|ref|>equation<|/ref|><|det|>[[115, 636, 750, 675]]<|/det|>
\[
\begin{align*}
a) \sin(2\alpha) &= 2 \sin \alpha \cdot \cos \alpha \\
b) \cos(2\alpha) &= \cos^2 \alpha - \sin^2 \alpha \\
c) \sin(3\alpha) &= 3 \sin \alpha - 4 \sin^3 \alpha \\
d) \cos(3\alpha) &= 4 \cos^3 \alpha - 3 \cos \alpha
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 688, 825, 722]]<|/det|>
Wir leiten mit Hilfe der Additionstheoreme für Sinus- und Cosinusfunktionen die Multiplikationstheoreme her. 

<|ref|>text<|/ref|><|det|>[[115, 722, 145, 739]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[115, 737, 702, 755]]<|/det|>
Mit Hilfe des Additionstheorems für die Sinusfunktion erhalten wir 

<|ref|>equation<|/ref|><|det|>[[119, 754, 832, 778]]<|/det|>
\[
\sin(2 \cdot \alpha) = \sin(\alpha + \alpha) = \sin(\alpha) \cdot \cos(\alpha) + \cos(\alpha) \cdot \sin(\alpha) = 2 \cdot \sin(\alpha) \cdot \cos(\alpha).
\]

<|ref|>text<|/ref|><|det|>[[115, 780, 145, 797]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[115, 796, 725, 814]]<|/det|>
Mit Hilfe des Additionstheorems für die Cosinusfunktion erhalten wir 

<|ref|>equation<|/ref|><|det|>[[119, 813, 830, 838]]<|/det|>
\[
\cos(2 \cdot \alpha) = \cos(\alpha + \alpha) = \cos(\alpha) \cdot \cos(\alpha) - \sin(\alpha) \cdot \sin(\alpha) = \cos^2(\alpha) - \sin^2(\alpha).
\]

<|ref|>text<|/ref|><|det|>[[115, 841, 780, 859]]<|/det|>
Mit Hilfe des trigonometrischen Pythagoras \(\sin^2\alpha + \cos^2\alpha = 1\) erhalten wir 

<|ref|>equation<|/ref|><|det|>[[119, 857, 790, 881]]<|/det|>
\[
\cos(2 \cdot \alpha) = \cos^2(\alpha) - \sin^2(\alpha) = 1 - \sin^2(\alpha) - \sin^2(\alpha) = 1 - 2 \cdot \sin^2(\alpha)
\]

<|ref|>equation<|/ref|><|det|>[[119, 896, 816, 922]]<|/det|>
\[
\cos(2 \cdot \alpha) = \cos^2(\beta) - \sin^2(\beta) = \cos^2(\alpha) - (1 - \cos^2(\alpha)) = 2 \cdot \cos^2(\alpha) - 1
\]