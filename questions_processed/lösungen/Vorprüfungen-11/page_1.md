<|ref|>text<|/ref|><|det|>[[24, 7, 789, 50]]<|/det|>
3) c) Orthogonal- Projektion : \((\frac{5}{1})\) auf \((\frac{1}{3})\) 

<|ref|>text<|/ref|><|det|>[[137, 66, 550, 103]]<|/det|>
import numpy as np; 

<|ref|>text<|/ref|><|det|>[[137, 103, 960, 140]]<|/det|>
v = np.array([5, 3, 1]) ; w = np.array([1, 2, 3]) ; 

<|ref|>text<|/ref|><|det|>[[137, 142, 933, 180]]<|/det|>
v - parallell = np.dot(v, w) / np.dot(w, w) * w; 

<|ref|>text<|/ref|><|det|>[[137, 183, 655, 220]]<|/det|>
v - senkrecht = v - v - parallell; 

<|ref|>text<|/ref|><|det|>[[137, 222, 339, 260]]<|/det|>
print(...); 

<|ref|>text<|/ref|><|det|>[[44, 296, 500, 338]]<|/det|>
d) q: P₁(5, 1, 2) \(\vec{a} = (\frac{1}{2})\) 

<|ref|>text<|/ref|><|det|>[[107, 337, 512, 375]]<|/det|>
E: P₀(2, 1, 8) \(\vec{n} = (\frac{2}{3})\) 

<|ref|>text<|/ref|><|det|>[[107, 397, 870, 435]]<|/det|>
\(\langle \vec{n}, \vec{a} \rangle = \langle (\frac{1}{2}), (\frac{1}{2}) \rangle = -3 + 3 + 2 = 2 \Rightarrow q \neq E\) 

<|ref|>text<|/ref|><|det|>[[125, 440, 920, 475]]<|/det|>
\(\vec{a}\) nicht senkrecht zu \(\vec{n}\), d.h. q ist nicht parallell zu 

<|ref|>text<|/ref|><|det|>[[125, 480, 660, 513]]<|/det|>
Ebene und q liegt nicht in de Ebene 

<|ref|>text<|/ref|><|det|>[[147, 518, 707, 551]]<|/det|>
→ q schneidet E → Schnittpunkt : 

<|ref|>equation<|/ref|><|det|>[[105, 570, 940, 630]]<|/det|>
\[G = \vec{n} + \frac{\langle \vec{n}, \vec{n} \rangle - \langle \vec{n}, \vec{a} \rangle}{\langle \vec{n}, \vec{a} \rangle} \cdot \vec{a} = (\frac{5}{2}) + \frac{\langle (\frac{1}{2}), (\frac{1}{2}) \rangle - \langle (\frac{1}{2}), \frac{5}{2} \rangle}{\frac{1}{2}} \cdot (\frac{1}{2})\]

<|ref|>equation<|/ref|><|det|>[[145, 635, 910, 678]]<|/det|>
\[= (\frac{5}{2}) + \frac{9 - Q}{2} \cdot (\frac{1}{2}) = (\frac{5}{2}) + \frac{9}{2} \cdot (\frac{3}{2}) = (\frac{5}{2}) + (\frac{18.5}{4.5}) = (\frac{18.5}{5.5})\]

<|ref|>text<|/ref|><|det|>[[117, 690, 655, 725]]<|/det|>
⇒ Schnittpunkt S (18, 5; 5, 5; 11) 

<|ref|>equation<|/ref|><|det|>[[110, 744, 810, 800]]<|/det|>
\[\sin \varphi = \frac{|\langle \vec{n}, \vec{a} \rangle|}{\|\vec{n}\| \cdot \|\vec{a}\|} = \frac{12}{\sqrt{11} \cdot \sqrt{14}} = \frac{2}{\sqrt{154}}\]

<|ref|>equation<|/ref|><|det|>[[160, 805, 822, 843]]<|/det|>
\[\varphi = \arcsin \left( \frac{2}{\sqrt{154}} \right) = 9,2744 \ldots \approx 9,27^\circ\]