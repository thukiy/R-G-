<|ref|>text<|/ref|><|det|>[[118, 87, 383, 103]]<|/det|>
Es gilt: \(z_{xy} = z_{yx}\) (Satz von Schwarz). 

<|ref|>text<|/ref|><|det|>[[118, 110, 878, 138]]<|/det|>
\(z_{yy}\) erhalten wir, indem wir \(z_y\) mit Hilfe der Ketten- oder Quotientenregel partiell nach \(y\) differenzieren. Wir verwenden hier die Kettenregel: 

<|ref|>equation<|/ref|><|det|>[[161, 144, 707, 180]]<|/det|>
\[z_y = \frac{2}{2y - x^2} = 2 \frac{(2y - x^2)^{-1}}{u} = 2u^{-1} \quad \text{mit} \quad u = 2y - x^2 \quad \text{und} \quad \frac{\partial u}{\partial y} = 2\]

<|ref|>equation<|/ref|><|det|>[[161, 191, 690, 226]]<|/det|>
\[z_{yy} = \frac{\partial z_y}{\partial y} = \frac{\partial z_y}{\partial u} \cdot \frac{\partial u}{\partial y} = 2(-1 \cdot u^{-2}) \cdot 2 = -4u^{-2} = -\frac{4}{u^2} = -\frac{4}{(2y - x^2)^2}\]

<|ref|>text<|/ref|><|det|>[[118, 230, 147, 247]]<|/det|>
c) 

<|ref|>equation<|/ref|><|det|>[[118, 247, 739, 290]]<|/det|>
\[z_x = \frac{1}{2\sqrt{x^2 - 2xy}} \cdot (2x - 2y) = \frac{x - y}{\sqrt{x^2 - 2xy}}; \quad z_y = -\frac{x}{\sqrt{x^2 - 2xy}};\]

<|ref|>equation<|/ref|><|det|>[[118, 299, 625, 344]]<|/det|>
\[z_{xx} = \frac{1 \cdot \sqrt{x^2 - 2xy} - \frac{1}{2\sqrt{x^2 - 2xy}} \cdot (2(x - 2y)(x - y))}{x^2 - 2xy} =\]

<|ref|>equation<|/ref|><|det|>[[118, 359, 580, 404]]<|/det|>
\[= \frac{(x^2 - 2xy) - (x - y)^2}{(x^2 - 2xy) \sqrt{x^2 - 2xy}} = -\frac{y^2}{\sqrt{(x^2 - 2xy)^3}};\]

<|ref|>equation<|/ref|><|det|>[[118, 408, 586, 453]]<|/det|>
\[z_{yy} = -\frac{x^2}{\sqrt{(x^2 - 2xy)^3}}; \quad z_{xy} = z_{yx} = \frac{xy}{\sqrt{(x^2 - 2xy)^3}}\]

<|ref|>sub_title<|/ref|><|det|>[[118, 473, 472, 491]]<|/det|>
## 4. Ableitungen in Funktion einsetzen 

<|ref|>text<|/ref|><|det|>[[118, 490, 878, 560]]<|/det|>
a) Zeigen Sie, dass die Funktion \(z = f(x, y) = xy + x \cdot \ln\left(\frac{y}{x}\right)\), mit \(x > 0\) und \(y > 0\), die Gleichung \(xz_x + yz_y = xy + z\) (bzw. in anderer Schreibweise: \(x \frac{\partial f}{\partial x} + y \frac{\partial f}{\partial y} = xy + z\)) erfüllt. 

<|ref|>text<|/ref|><|det|>[[118, 558, 855, 606]]<|/det|>
b) Zeigen Sie, dass die Funktion \(f(x, t) = e^{-\pi^2 a^2 t} \cdot \sin(\pi x), a \in \mathbb{R}\) eine Lösung der Gleichung \(a^2 \cdot f_{xx} = f_t\) (andere Schreibweise: \(a^2 \cdot \frac{\partial^2 f}{\partial x^2} = \frac{\partial f}{\partial t}\)) ist. 

<|ref|>text<|/ref|><|det|>[[118, 621, 147, 638]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[118, 636, 880, 670]]<|/det|>
Die Funktion wird vor dem Differenzieren unter Verwendung der Rechenregel \(\ln\left(\frac{a}{b}\right) = \ln a - \ln b\) in eine günstigere Gestalt gebracht: 

<|ref|>equation<|/ref|><|det|>[[161, 675, 827, 705]]<|/det|>
\[z = xy + x \cdot \ln\left(\frac{y}{x}\right) = xy + x (\ln y - \ln x) = xy + x \cdot \ln y - x \cdot \ln x = x (y + \ln y) - x \cdot \ln x\]

<|ref|>text<|/ref|><|det|>[[118, 708, 720, 723]]<|/det|>
Gliedweises partielles Differenzieren nach \(x\) unter Verwendung der Produktregel liefert dann: 

<|ref|>equation<|/ref|><|det|>[[161, 730, 861, 777]]<|/det|>
\[z = x \frac{(y + \ln y) - x \cdot \ln x}{x} = x \frac{(y + \ln y) - (uv)}{u} \quad \text{mit} \quad u = x, \quad v = \ln x \quad \text{und} \quad u_x = 1, \quad v_x = \frac{1}{x}\]

<|ref|>equation<|/ref|><|det|>[[161, 778, 794, 805]]<|/det|>
\[z_x = 1 \frac{(y + \ln y) - (u_x v + v_x u)}{x} = y + \ln y - \left(1 \cdot \ln x + \frac{1}{x} \cdot \frac{u}{x}\right) = y + \ln y - \ln x - 1\]

<|ref|>text<|/ref|><|det|>[[118, 807, 551, 821]]<|/det|>
Die partielle Ableitung nach \(y\) lässt sich besonders einfach bilden: 

<|ref|>equation<|/ref|><|det|>[[161, 828, 628, 864]]<|/det|>
\[z = x \frac{(y + \ln y) - x \ln x}{x} \Rightarrow z_y = x \left(1 + \frac{1}{y}\right) - 0 = x + \frac{x}{y}\]

<|ref|>text<|/ref|><|det|>[[161, 860, 373, 872]]<|/det|>
konst. Faktor konst. Summand