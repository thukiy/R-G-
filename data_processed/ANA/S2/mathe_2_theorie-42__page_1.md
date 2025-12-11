<|ref|>sub_title<|/ref|><|det|>[[30, 15, 339, 57]]<|/det|>
# Hesse-Matrix 

<|ref|>text<|/ref|><|det|>[[24, 70, 715, 97]]<|/det|>
Def: \(f: D \subseteq \mathbb{R}^n \to \mathbb{R}\) sei mind. 2 mal partielle differenzierbar. 

<|ref|>text<|/ref|><|det|>[[100, 111, 430, 135]]<|/det|>
Die Hesse-Matrix ergibt sich zu 

<|ref|>equation<|/ref|><|det|>[[110, 139, 540, 214]]<|/det|>
\[H_f(\vec{x}) = \nabla^2 f(\vec{x}) = \begin{pmatrix} \frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} \\ \frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} \end{pmatrix}\]

<|ref|>text<|/ref|><|det|>[[45, 226, 808, 253]]<|/det|>
→ mit Satz von Schwarz: Hesse Matrix ist symmetrisch, d.h. \(H_f = H_f^T\) 

<|ref|>text<|/ref|><|det|>[[45, 266, 590, 291]]<|/det|>
→ Gradient (eine Ableitung) ergibt einen Velor 

<|ref|>text<|/ref|><|det|>[[45, 305, 411, 330]]<|/det|>
→ Hesse-Matrix \(\hat{\equiv}\) 2. Ableitung 

<|ref|>text<|/ref|><|det|>[[110, 344, 848, 410]]<|/det|>
⇝ bei Funktion, die von 1 Variabeln abhängt, ist 2. Ableitung
hinreichende Bedingung für Identifikation von Extremstellen 

<|ref|>sub_title<|/ref|><|det|>[[20, 443, 252, 468]]<|/det|>
## Richtungsabteilung 

<|ref|>image<|/ref|><|det|>[[33, 483, 380, 730]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[433, 483, 911, 508]]<|/det|>
bisher: partielle Ableitung von \(f: \mathbb{R}^n \to \mathbb{R}\) 

<|ref|>text<|/ref|><|det|>[[567, 525, 959, 551]]<|/det|>
⇝ diese geben Steigung entlang der 

<|ref|>text<|/ref|><|det|>[[567, 564, 875, 589]]<|/det|>
Achsen (also \(x_1, x_2 \ldots\)) an 

<|ref|>text<|/ref|><|det|>[[433, 600, 880, 626]]<|/det|>
jetzt: Steigung entlang einer beliebigen 

<|ref|>text<|/ref|><|det|>[[567, 639, 900, 665]]<|/det|>
Richtung → Richtungsabteilung 

<|ref|>text<|/ref|><|det|>[[24, 774, 675, 801]]<|/det|>
Def: Gegeben: \(f: \mathbb{R}^n \to \mathbb{R}\) und Richtung \(\hat{e}\) mit \(|\hat{e}| = 1\) 

<|ref|>text<|/ref|><|det|>[[106, 816, 272, 839]]<|/det|>
Der Grenzwert 

<|ref|>equation<|/ref|><|det|>[[106, 844, 655, 880]]<|/det|>
\[\frac{\partial f}{\partial \hat{e}} (\vec{x}_0) = \lim_{t \to 0} \left( \frac{f(\vec{x}_0 + t \cdot \hat{e}) - f(\vec{x}_0)}{t} \right) = \frac{d}{dt} f(\vec{x}_0 + t \cdot \hat{e}) \big|_{t=0}\]

<|ref|>text<|/ref|><|det|>[[106, 892, 710, 918]]<|/det|>
heisst Richtungsabteilung von \(f\) an \(\vec{x}_0\) in Richtung \(\hat{e}\)