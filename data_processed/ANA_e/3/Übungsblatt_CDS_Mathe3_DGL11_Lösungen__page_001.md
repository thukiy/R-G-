<|ref|>title<|/ref|><|det|>[[115, 165, 507, 201]]<|/det|>
# Übungsblatt DGL 11 

<|ref|>text<|/ref|><|det|>[[576, 179, 880, 196]]<|/det|>
Computational and Data Science 

<|ref|>text<|/ref|><|det|>[[755, 199, 880, 215]]<|/det|>
BSc HS2024 

<|ref|>sub_title<|/ref|><|det|>[[115, 232, 270, 260]]<|/det|>
## Lösungen 

<|ref|>text<|/ref|><|det|>[[750, 241, 880, 258]]<|/det|>
Mathematik 3 

<|ref|>text<|/ref|><|det|>[[115, 287, 210, 304]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 303, 852, 338]]<|/det|>
- Sie kennen die Begriffe Fourier-Transformation und -Rücktransformation sowie deren wichtigste Eigenschaften. 

<|ref|>text<|/ref|><|det|>[[115, 337, 827, 354]]<|/det|>
- Sie können die Fourier-Transformation einer einfachen Funktion bestimmen. 

<|ref|>text<|/ref|><|det|>[[115, 353, 875, 386]]<|/det|>
- Sie können mit Hilfe einer Transformationstabelle die Fourier-Rücktransformation durchführen. 

<|ref|>text<|/ref|><|det|>[[115, 386, 875, 419]]<|/det|>
- Sie können mit Hilfe der Fourier-Transformation einfache lineare DGL 1. Ordnung lösen. 

<|ref|>sub_title<|/ref|><|det|>[[115, 451, 736, 470]]<|/det|>
### 1. Aussagen über Fourier-Entwicklungen und -Transformationen 

<|ref|>text<|/ref|><|det|>[[115, 476, 680, 494]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[115, 491, 880, 715]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Die Fourier-Transformierte \(F(\omega)\) kann aus physikalischer Sicht als Spektrum interpretiert werden.</td><td>X</td><td></td></tr><tr><td>b) Jede Funktion der Form \(f: \mathbb{R} \to \mathbb{R}\) hat eine Fourier-Transformierte.</td><td></td><td>X</td></tr><tr><td>c) Nur periodische Funktionen der Form \(f: \mathbb{R} \to \mathbb{R}\) haben eine Fourier-Transformierte.</td><td></td><td>X</td></tr><tr><td>d) Die Bildfunktion einer konstanten Funktion ist konstant.</td><td></td><td>X</td></tr><tr><td>e) Gilt \(f(t) \circ \text{-}\bullet F(\omega)\), dann folgt \(2f(t) \circ \text{-}\bullet 2F(\omega)\).</td><td>X</td><td></td></tr><tr><td>f) Gilt \(f(t) \circ \text{-}\bullet F(\omega)\) und \(g(t) \circ \text{-}\bullet G(\omega)\), dann folgt \(F(\omega) + G(\omega) \circ \text{-}\bullet f(t) + g(t)\).</td><td>X</td><td></td></tr><tr><td>g) Mit Hilfe der Fourier-Transformation lässt sich jede lineare DGL einfach lösen.</td><td></td><td>X</td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[115, 730, 392, 747]]<|/det|>
### 2. Fourier-Transformationen 

<|ref|>text<|/ref|><|det|>[[115, 747, 780, 765]]<|/det|>
Berechnen Sie für die angegeben Funktionen die Fourier-Transformierten. 

<|ref|>equation<|/ref|><|det|>[[115, 765, 343, 825]]<|/det|>
\[ \text{a)} \quad f(t) = \begin{cases} A \mid t \in [-T, T] \\ 0 \mid \text{sonst} \end{cases} \]

<|ref|>equation<|/ref|><|det|>[[115, 825, 390, 904]]<|/det|>
\[ \text{b)} \quad f(t) = \begin{cases} A \left(1 - \frac{|t|}{T}\right) \mid t \in [-T, T] \\ 0 \mid \text{sonST} \end{cases} \]