<|ref|>sub_title<|/ref|><|det|>[[115, 166, 485, 202]]<|/det|>
# Übungsblatt DGL 9 

<|ref|>text<|/ref|><|det|>[[574, 179, 880, 196]]<|/det|>
Computational and Data Science 

<|ref|>text<|/ref|><|det|>[[755, 199, 880, 215]]<|/det|>
BSc HS2024 

<|ref|>sub_title<|/ref|><|det|>[[115, 232, 270, 261]]<|/det|>
## Lösungen 

<|ref|>text<|/ref|><|det|>[[750, 240, 880, 257]]<|/det|>
Mathematik 3 

<|ref|>text<|/ref|><|det|>[[115, 287, 210, 304]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 303, 844, 354]]<|/det|>
- Sie kennen die Begriffe trigonometrisches Monom/Polynom, \(L^2\)-Skalarprodukt, Orthonormalbasis, Fourier-Polynom, reelle/komplexe Fourier-Koeffizienten, Fourier-Reihe und Fourier-Entwicklung sowie deren wichtigste Eigenschaften. 

<|ref|>text<|/ref|><|det|>[[115, 353, 816, 387]]<|/det|>
- Sie kennen die Zusammenhänge zwischen komplexen und reellen Fourier-Koeffizienten und können diese anwenden. 

<|ref|>text<|/ref|><|det|>[[115, 386, 770, 420]]<|/det|>
- Sie können die Parität einer periodischen Funktion ausnutzen, um die Berechnung der Fourier-Koeffizienten zu vereinfachen. 

<|ref|>text<|/ref|><|det|>[[115, 419, 735, 436]]<|/det|>
- Sie können einfache Funktionen in eine Fourier-Reihe entwickeln. 

<|ref|>sub_title<|/ref|><|det|>[[115, 467, 785, 487]]<|/det|>
## 1. Aussagen über erzwungen gedämpfte harmonische Schwingungen 

<|ref|>text<|/ref|><|det|>[[115, 492, 680, 510]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[115, 508, 880, 662]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Jede periodische Funktion \(f: \mathbb{R} \to \mathbb{R}\) besitzt eine Fourier-Entwicklung.</td><td>X</td><td></td></tr><tr><td>b) Jede periodische Funktion \(f: \mathbb{R} \to \mathbb{R}\) kann exakt durch eine Fourier-Reihe dargestellt werden.</td><td></td><td>X</td></tr><tr><td>c) Die Fourier-Entwicklung einer ungeraden periodischen Funktion \(f: \mathbb{R} \to \mathbb{R}\) ist eine reine Sinusentwicklung.</td><td>X</td><td></td></tr><tr><td>d) Die Fourier-Entwicklung einer geraden periodischen Funktion \(f: \mathbb{R} \to \mathbb{R}\) ist eine reinen Sinusentwicklung.</td><td></td><td>X</td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[115, 677, 285, 695]]<|/det|>
## 2. Orthogonalität 

<|ref|>text<|/ref|><|det|>[[115, 694, 850, 736]]<|/det|>
Welche Paare der Funktionen \(\cos(kx)\), \(\sin(jx)\), \(k \in \mathbb{N}_0\), \(j \in \mathbb{N}\) sind auf dem Intervall \([0, \frac{\pi}{2}]\) orthogonal? 

<|ref|>equation<|/ref|><|det|>[[120, 753, 605, 770]]<|/det|>
\[ \text{Additionstheorem } \sin(\alpha \pm \beta) = \sin \alpha \cos \beta \pm \cos \alpha \sin \beta \quad \leadsto \]

<|ref|>equation<|/ref|><|det|>[[275, 781, 601, 812]]<|/det|>
\[ \sin \alpha \cos \beta = \frac{1}{2} (\sin(\alpha + \beta) + \sin(\alpha - \beta))\]

<|ref|>equation<|/ref|><|det|>[[120, 821, 640, 846]]<|/det|>
\[ \text{Einsetzen in das Skalarprodukt } s = \int_0^{\pi/2} \sin(jx) \cos(kx) \, dx \quad \leadsto \]