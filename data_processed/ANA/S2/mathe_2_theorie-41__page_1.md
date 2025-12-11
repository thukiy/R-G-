<|ref|>text<|/ref|><|det|>[[24, 15, 718, 42]]<|/det|>
Def: \(f: \mathbb{D} \subseteq \mathbb{R}^n \to \mathbb{R}\) sei mind. 2 mal partielle differenzierbar. 

<|ref|>text<|/ref|><|det|>[[100, 56, 432, 79]]<|/det|>
Die Hesse-Matrix ergibt sich zu 

<|ref|>equation<|/ref|><|det|>[[102, 81, 540, 157]]<|/det|>
\[H_f(\vec{x}) = \nabla^2 f(\vec{x}) = \begin{pmatrix} \frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots \\ \frac{\partial^2 f}{\partial x_1 \partial x_3} & \frac{\partial^2 f}{\partial x_2^2} & \cdots \\ \frac{\partial^2 f}{\partial x_2 \partial x_3} & \frac{\partial^2 f}{\partial x_3^2} & \cdots \end{pmatrix}\]

<|ref|>text<|/ref|><|det|>[[42, 170, 810, 197]]<|/det|>
→ mit Satz von Schwarz: Hesse Matrix ist symmetrisch, d.h. \(H_f = H_f^T\) 

<|ref|>text<|/ref|><|det|>[[42, 209, 592, 234]]<|/det|>
→ Gradient (esste Ableitung) ergibt einen Velour 

<|ref|>text<|/ref|><|det|>[[42, 247, 408, 272]]<|/det|>
→ Hesse- Matrix ⇌ 2. Ableitung 

<|ref|>text<|/ref|><|det|>[[110, 286, 850, 351]]<|/det|>
⇝ bei Funktion, die von 1 Variabeln abhängt, ist 2. Ableitung
hinreichende Bedingung für Identifikation von Extremstellen 

<|ref|>sub_title<|/ref|><|det|>[[24, 384, 254, 410]]<|/det|>
## Richtungsabteilung 

<|ref|>image<|/ref|><|det|>[[35, 424, 375, 667]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[430, 425, 916, 450]]<|/det|>
bisher: partielle Ableitung von \(f: \mathbb{R}^n \to \mathbb{R}\) 

<|ref|>text<|/ref|><|det|>[[520, 464, 960, 490]]<|/det|>
⇝ diese geben Steigung entlang der 

<|ref|>text<|/ref|><|det|>[[568, 503, 875, 528]]<|/det|>
Achsen (also \(x_1, x_2\)...) an 

<|ref|>text<|/ref|><|det|>[[430, 541, 886, 567]]<|/det|>
jeht: Steigung entlang einer beliebigen 

<|ref|>text<|/ref|><|det|>[[520, 580, 900, 606]]<|/det|>
Richtung → Richtungsabteilung 

<|ref|>text<|/ref|><|det|>[[24, 714, 680, 740]]<|/det|>
Def: Gegeben: \(f: \mathbb{R}^n \to \mathbb{R}\) und Richtung \(\hat{e}\) mit \(|\hat{e}| = 1\) 

<|ref|>text<|/ref|><|det|>[[102, 755, 275, 779]]<|/det|>
Der Grenzwert 

<|ref|>equation<|/ref|><|det|>[[108, 784, 655, 824]]<|/det|>
\[\frac{d\hat{f}}{d\hat{e}} (\vec{x}_0) = \lim_{\hat{e} \to 0} \left( \frac{f(\vec{x}_0 + \hat{e} \cdot \vec{e}) - f(\vec{x}_0)}{\hat{e}} \right) = \frac{d}{d\hat{e}} f(\vec{x}_0 + \hat{e} \cdot \vec{e}) \big|_{\hat{e} = 0}\]

<|ref|>text<|/ref|><|det|>[[102, 833, 710, 859]]<|/det|>
heisst Richtungsabteilung von \(f\) an \(\vec{x}_0\) in Richtung \(\hat{e}\) 

<|ref|>text<|/ref|><|det|>[[24, 880, 597, 918]]<|/det|>
einfachere Darsleitung: \(\frac{d\hat{f}(\vec{x}_0)}{d\hat{e}} = \langle \text{grad } f(\vec{x}_0), \hat{e} \rangle\)