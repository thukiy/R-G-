<|ref|>title<|/ref|><|det|>[[115, 183, 476, 217]]<|/det|>
Übungsblatt Ana 2 

<|ref|>text<|/ref|><|det|>[[578, 196, 880, 232]]<|/det|>
Computational and Data Science
FS2024 

<|ref|>text<|/ref|><|det|>[[115, 250, 270, 278]]<|/det|>
Lösungen 

<|ref|>text<|/ref|><|det|>[[750, 258, 880, 275]]<|/det|>
Mathematik 2 

<|ref|>text<|/ref|><|det|>[[115, 303, 210, 320]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 320, 789, 354]]<|/det|>
- Sie kennen die Begriffe Integral, Stammfunktion, Substitution und deren wichtigste Eigenschaften. 

<|ref|>text<|/ref|><|det|>[[115, 353, 789, 387]]<|/det|>
- Sie können die Methode der Substitution anwenden, um bestimmte und unbestimmte Integrale zu berechnen. 

<|ref|>text<|/ref|><|det|>[[115, 386, 852, 420]]<|/det|>
- Sie können bestimmte Integrale näherungsweise auf eine vorgegebene Anzahl Dezimalstellen mit Python/Numpy berechnen. 

<|ref|>sub_title<|/ref|><|det|>[[115, 451, 380, 469]]<|/det|>
1. Aussagen über Integrale 

<|ref|>text<|/ref|><|det|>[[115, 468, 680, 485]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[115, 483, 880, 737]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Für \(f: \mathbb{R} \to \mathbb{R}\) gilt: existiert zu f eine Stammfunktion, so ist diese eindeutig.</td><td></td><td>X</td></tr><tr><td>b) Für die integrierbaren Funktionen \(f, g: \mathbb{R} \to \mathbb{R}\) gilt: \(\int f(x)dx + \int g(x)dx = \int (f(x) + g(x))dx\).</td><td>X</td><td></td></tr><tr><td>c) Für die integrierbaren Funktionen \(f, g: \mathbb{R} \to R\) gilt: \(\int f(x)dx \cdot \int g(x)dx = \int (f(x) \cdot g(x))dx\).</td><td></td><td>X</td></tr><tr><td>d) Für die integrierbaren Funktionen \(f, g: \mathbb{R} \to g(x)dx\).</td><td>X</td><td></td></tr><tr><td>e) Für die integrierbare Funktion \(f: \mathbb{R} \to \mathbb{R}\) gilt: \(\int_a^b f(x)dx = 0 \implies f(x) = 0 \forall x \in [a, b]\).</td><td></td><td>X</td></tr><tr><td>f) Für die integrierbare Funktion \(f: \mathbb{R} \to \mathbb{R} \text{ gilt: } a < b \implies \int_a^b f(x)dx \le \int_a^b |f(x)|dx\).</td><td>X</td><td></td></tr></table>