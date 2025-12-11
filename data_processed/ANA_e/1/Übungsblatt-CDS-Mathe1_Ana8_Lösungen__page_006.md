<|ref|>sub_title<|/ref|><|det|>[[75, 66, 444, 84]]<|/det|>
## 6. Ableitung von Termen mit Beträgen 

<|ref|>text<|/ref|><|det|>[[75, 83, 890, 118]]<|/det|>
Wir berechnen jeweils die *Ableitung* der gegebenen *Funktion* \(f\) mit Hilfe geeigneter *Ableitungsregeln*. 

<|ref|>text<|/ref|><|det|>[[91, 120, 320, 140]]<|/det|>
a) Für alle \(x \in \mathbb{R} \setminus \{0\}\) sei 

<|ref|>equation<|/ref|><|det|>[[119, 152, 888, 171]]<|/det|>
\[f(x) = |x| = \operatorname{sgn}(x) \cdot x. \qquad (38)\]

<|ref|>text<|/ref|><|det|>[[119, 181, 699, 201]]<|/det|>
Mit Hilfe der *Produktregel* erhalten wir für \(x \in \mathbb{R} \setminus \{0\}\) die *Ableitung* 

<|ref|>equation<|/ref|><|det|>[[119, 212, 888, 240]]<|/det|>
\[\frac{f'(x)}{=} = \operatorname{sgn}'(x) \cdot x + \operatorname{sgn}(x) \cdot x' = 0 \cdot x + \operatorname{sgn}(x) \cdot 1 = \operatorname{sgn}(x). \qquad (39)\]

<|ref|>text<|/ref|><|det|>[[91, 255, 320, 275]]<|/det|>
b) Für alle \(x \in \mathbb{R} \setminus \{0\}\) sei 

<|ref|>text<|/ref|><|det|>[[119, 285, 888, 316]]<|/det|>
\(f(x) = \sqrt{|x|}\). \qquad (40) 

<|ref|>text<|/ref|><|det|>[[119, 320, 767, 340]]<|/det|>
Mit Hilfe der *Wurzelregel* und (39) erhalten wir für \(x \in \mathbb{R} \setminus \{0\}\) die *Ablieitung* 

<|ref|>equation<|/ref|><|det|>[[119, 351, 888, 395]]<|/det|>
\[\frac{f'(x)}{=} = \frac{|x|'}{2\sqrt{|x|}} = \frac{\operatorname{sgn}(x)}{2\sqrt{|x|}}. \qquad (41)\]

<|ref|>text<|/ref|><|det|>[[91, 412, 330, 433]]<|/det|>
c) Für alle \(x \in \mathbb{R} \setminus \{0\}\) sei 

<|ref|>sub_title<|/ref|><|det|>[[91, 575, 280, 594]]<|/det|>
## d) Für alle \(x \in \mathbb{R}\) sei 

<|ref|>equation<|/ref|><|det|>[[119, 567, 888, 576]]<|/det|>
\[f'(x) = -\frac{(1 + |x|)'}{(1 + |x|)^2} = -\frac{0 + \operatorname{sgn}(x)}{(1 + |x|)^2} = -\frac{\operatorname{sgn}(x)}{(1 + |x|)^2}. \qquad (43)\]

<|ref|>text<|/ref|><|det|>[[91, 610, 280, 629]]<|/det|>
 

<|ref|>equation<|/ref|><|det|>[[119, 616, 888, 638]]<|/det|>
\[f(x) = |x^3| = \operatorname{sgn}(x^3) \cdot x^3 = \operatorname{sgn}(x) \cdot x^3. \qquad (44)\]

<|ref|>text<|/ref|><|det|>[[119, 648, 888, 667]]<|/det|>
Für die Berechnung der *Ableitung* von \(f\) betrachten wir die Fälle \(x \neq 0\) und \(x = 0\) getrennt. 

<|ref|>text<|/ref|><|det|>[[119, 670, 599, 690]]<|/det|>
**Fall 1:** \(x \neq 0\). Mit Hilfe der *Produkt-Regel* erhalten wir 

<|ref|>equation<|/ref|><|det|>[[147, 699, 888, 722]]<|/det|>
\[f'(x) = \operatorname{sgn}'(x) \cdot x^3 + \operatorname{sgn}(x) \cdot (x^3)' = 0 \cdot x^3 + \operatorname{sgn}(x) \cdot 3x^2 = \operatorname{sgn}(x) \cdot 3x^2. \qquad (45)\]

<|ref|>text<|/ref|><|det|>[[119, 733, 616, 752]]<|/det|>
**Fall 2:** \(x = 0\). Wir betrachten die *einseitigen Grenzwerte* 

<|ref|>equation<|/ref|><|det|>[[147, 761, 888, 787]]<|/det|>
\[\lim_{x \searrow 0} f'(x) = \lim_{x \searrow 0} (\operatorname{sgn}(x) \cdot 3x^2) = +1 \cdot 3 \cdot 0^2 = 0 = \operatorname{sgn}(0) \cdot 3 \cdot 0^2 = 0 \qquad (46)\]

<|ref|>equation<|/ref|><|det|>[[147, 795, 888, 822]]<|/det|>
\[\lim_{x \nearrow 0} f'(x) = \lim_{x \nearrow 0} (\operatorname{sgn}(x) \cdot 3x^2) = -1 \cdot 3 \cdot 0^2 = 0 = \operatorname{sgn}'(0) \cdot 3 \cdot 0^2 = 0. \qquad (47)\]

<|ref|>text<|/ref|><|det|>[[119, 833, 633, 853]]<|/det|>
Demnach macht die *Ableitung* bei \(x = 0\) keinen Sprung. 

<|ref|>text<|/ref|><|det|>[[119, 858, 407, 876]]<|/det|>
Somit erhalten wir die *Ableitung* 

<|ref|>equation<|/ref|><|det|>[[119, 888, 888, 910]]<|/det|>
\[f'(x) = \operatorname{sgn}(x) \cdot 3x^2 \quad \text{für alle} \quad x \in \mathbb{R}. \qquad (48)\]