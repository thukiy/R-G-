<|ref|>title<|/ref|><|det|>[[115, 183, 500, 216]]<|/det|>
Übungsblatt 11 Ana 

<|ref|>text<|/ref|><|det|>[[576, 196, 880, 231]]<|/det|>
Computational and Data Science
FS2024 

<|ref|>text<|/ref|><|det|>[[115, 250, 270, 277]]<|/det|>
Lösungen 

<|ref|>text<|/ref|><|det|>[[750, 258, 880, 275]]<|/det|>
Mathematik 2 

<|ref|>text<|/ref|><|det|>[[115, 303, 210, 320]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 320, 800, 386]]<|/det|>
- Sie kennen die Begriffe Kurve, Spur, Geschwindigkeits-/Tangentenvektor, Beschleunigungsvektor, Tangenteneinheitsvektor, Hauptnormalenvektor, Binormalenvektor, Parametrisierung, Bogenlänge, Vektorfeld, Kurven-/Linienintegral und deren wichtigste Eigenschaften. 

<|ref|>text<|/ref|><|det|>[[115, 386, 742, 403]]<|/det|>
- Sie können die Spur einer parametrisierten Kurve in 2D skizzieren. 

<|ref|>text<|/ref|><|det|>[[115, 403, 530, 419]]<|/det|>
- Sie können ein Vektorfeld in 2D skizzieren. 

<|ref|>text<|/ref|><|det|>[[115, 419, 610, 436]]<|/det|>
- Sie können die Bogenlänge einer Kurve berechnen. 

<|ref|>text<|/ref|><|det|>[[115, 436, 490, 453]]<|/det|>
- Sie können Linienintegrale berechnen. 

<|ref|>sub_title<|/ref|><|det|>[[115, 485, 515, 502]]<|/det|>
1. Aussagen über parametrisierte Kurven 

<|ref|>text<|/ref|><|det|>[[115, 501, 680, 518]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[115, 516, 878, 671]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Eine parametrisierte Kurve kann durch \(\vec{r}: \mathbb{R} \to \mathbb{R}^n\) dargestellt werden.</td><td>X</td><td></td></tr><tr><td>b) Eine parametrisierte Kurve ist stets injektiv.</td><td></td><td>X</td></tr><tr><td>c) Eine parametrisierte Kurve ist für \(n \ge 2\) niemals surjektiv.</td><td>X</td><td></td></tr><tr><td>d) Haben zwei parametrisierte Kurven dieselbe Spur, dann haben sie auch dieselbe Geschwindigkeit.</td><td></td><td>X</td></tr><tr><td>e) Haben zwei parametrisierte Kurven dieselbe Spur, dann sie auch denselben Tangenteneinheitsvektor.</td><td></td><td>X</td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[115, 686, 469, 703]]<|/det|>
2. Spur von parametrisierten Kurven 

<|ref|>text<|/ref|><|det|>[[115, 702, 843, 720]]<|/det|>
Skizzieren Sie jeweils die Spur der Kurve für einen geeigneten Bereich von \(t \in \mathbb{R}\). 

<|ref|>equation<|/ref|><|det|>[[115, 718, 785, 754]]<|/det|>
\[ \text{a) } \vec{r}(t) = \left( \frac{1 + 2t}{3 - t} \right) \quad \text{b) } \vec{r}(t) = \left( \frac{t}{\sin t} \right) \quad \text{c) } \vec{r}(t) = \left( \frac{\sin t}{t} \right) \]

<|ref|>equation<|/ref|><|det|>[[115, 752, 829, 790]]<|/det|>
\[ \text{d) } \vec{r}(t) = \left( \frac{2 \cos t}{2 \sin t} \right) \quad \text{e) } \vec{r}(t) = \left( \frac{\cosh t}{\sinh t} \right) \quad \text{f) } \vec{r}(t) = \left( \frac{2 - \frac{t}{2\pi} \cos t}{2 - \frac{t}{2\pi} \sin t} \right) \]

<|ref|>text<|/ref|><|det|>[[115, 790, 696, 808]]<|/det|>
g) Plotten Sie die Spur der Kurven aus a) - f) mit Python/Numpy.