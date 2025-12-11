<|ref|>sub_title<|/ref|><|det|>[[108, 66, 653, 85]]<|/det|>
10. Aussagen über verallgemeinerte Exponentialfunktionen 

<|ref|>table<|/ref|><|det|>[[108, 94, 920, 310]]<|/det|>
<table><tr><td>Welche der folgenden Aussagen sind wahr und welche falsch?</td><td>wahr</td><td>falsch</td></tr><tr><td>a) Verallgemeinerte Exponentialfunktionen beschreiben jeweils die Beziehung zwischen zwei Grössen in vielen Anwendungen aus Alltag, Naturwissenschaft, Technik und Wirtschaft.</td><td>●</td><td>○</td></tr><tr><td>b) Verallgemeinerte Exponentialfunktionen sind immer injektiv.</td><td>●</td><td>○</td></tr><tr><td>c) Verallgemeinerte Exponentialfunktionen sind immer strikt monoton.</td><td>●</td><td>○</td></tr><tr><td>d) Jede verallgemeinerte Exponentialfunktion hat eine Umkehrfunktion, sofern man die Zielmenge geschickt wählt.</td><td>●</td><td>○</td></tr><tr><td>e) Jede eigentliche Exponentialfunktion ist auch eine verallgemeinerte Exponentialfunktion.</td><td>●</td><td>○</td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[108, 377, 699, 395]]<|/det|>
11. Eigenschaften von verallgemeinerten Exponentialfunktionen 

<|ref|>text<|/ref|><|det|>[[108, 393, 920, 429]]<|/det|>
Seien \(a \in \mathbb{R}^+ \setminus \{1\}\), \(\Sigma \in \mathbb{R} \setminus \{0\}\), \(x_0 \in \mathbb{R}\), \(y_0 \in \mathbb{R} \setminus \{0\}\) und \(f\) die verallgemeinerte Exponentialfunktion 

<|ref|>equation<|/ref|><|det|>[[395, 441, 920, 489]]<|/det|>
\[f : \mathbb{R} \to \mathbb{R} \quad (48) \\ x \mapsto f(x) := y_0 \cdot a^{\frac{x-x_0}{\Sigma}}. \]

<|ref|>text<|/ref|><|det|>[[108, 499, 692, 518]]<|/det|>
Wir beweisen die folgenden Eigenschaften von \(f\) für alle \(x, \Delta x \in \mathbb{R}\). 

<|ref|>text<|/ref|><|det|>[[122, 523, 220, 542]]<|/det|>
a) Es gilt 

<|ref|>equation<|/ref|><|det|>[[150, 553, 920, 585]]<|/det|>
\[\frac{f(x_0)}{x_0} = y_0 \cdot a^{\frac{x_0-x_0}{\Sigma}} = y_0 \cdot a^{\frac{0}{\Sigma}} = y_0 \cdot a^0 = y_0 \cdot 1 = y_0. \quad (49)\]

<|ref|>text<|/ref|><|det|>[[122, 601, 317, 620]]<|/det|>
b) Für alle \(x \in \mathbb{R}\) gilt 

<|ref|>equation<|/ref|><|det|>[[150, 630, 920, 696]]<|/det|>
\[\begin{aligned} \frac{f(x + \Sigma)}{x + \Sigma} &= y_0 \cdot a^{\frac{x + \Sigma - x_0}{\Sigma}} = y_0 \cdot a^{\frac{\Sigma}{\Sigma} + \frac{x - x_0}{\Sigma}} = y_0 \cdot a^{\frac{\Sigma}{\Delta \Sigma}} \cdot a^{\frac{x - x_0}{\Sigma}} = y_0 \cdot a^1 \cdot a^{\frac{x - x_0}{\Sigma}} = a \cdot y_0 \cdot a^{\frac{x - x_0}{\Sigma}} \\ &= a \cdot f(x). \end{aligned} \quad (50)\]

<|ref|>text<|/ref|><|det|>[[122, 715, 317, 734]]<|/det|>
c) Für alle \(x \in \mathbb{R}\) gilt 

<|ref|>equation<|/ref|><|det|>[[1500, 744, 920, 825]]<|/det|>
\[\begin{aligned} \frac{f(x - \Sigma)}{x - \Sigma} &= y_0 \cdot a^{\frac{x - \Sigma - x_0}{\Sigma}} = y_0 \cdot a^{\frac{-\Sigma}{\Sigma} + \frac{x - x_0}{\Sigma}} = y_0 \\ &= \frac{1}{a} \cdot y_0 \cdot a^{\frac{x - x_0}{\Sigma}} = \frac{f(x)}{a}. \end{aligned} \quad (51)\]

<|ref|>text<|/ref|><|det|>[[122, 843, 352, 862]]<|/det|>
d) Für alle \(x, \Delta x \in \mathbb{R}\) gilt 

<|ref|>equation<|/ref|><|det|>[[150, 872, 920, 905]]<|/det|>
\[\frac{f(x + \Delta x)}{x + \Delta x} = y_0 \cdot a^{\frac{x + \Delta x - x_0}{\Sigma}} = y_0 \cdot a^{\frac{\Delta x}{\Sigma} + \frac{x - x_0}{\Sigma}} = y_0 \quad a^{\frac{\Delta x}{\Sigma}} \cdot a^{\frac{x - x_0}{\Sigma}} = a^{\frac{\Delta x}{\Sigma}} \cdot f(x). \quad (52)\]