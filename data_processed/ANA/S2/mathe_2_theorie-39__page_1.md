<|ref|>sub_title<|/ref|><|det|>[[25, 11, 280, 40]]<|/det|>
## Totales Differencial 

<|ref|>text<|/ref|><|det|>[[50, 52, 610, 79]]<|/det|>
Verwendung des Gradienten für Tangenkalebene : 

<|ref|>equation<|/ref|><|det|>[[55, 85, 666, 120]]<|/det|>
\[z = f(x_0, y_0) + \frac{\partial z}{\partial x} f(x_0, y_0) \cdot (x - x_0) + \frac{\partial z}{\partial y} f(x_0, y_0) \cdot (y - y_0)\]

<|ref|>equation<|/ref|><|det|>[[80, 124, 476, 180]]<|/det|>
\[= f(x_0, y_0) + \langle \nabla f(x_0, y_0), \left( \frac{x - x_0}{y - y_0} \right) \rangle\]

<|ref|>equation<|/ref|><|det|>[[70, 186, 533, 234]]<|/det|>
\[\rightarrow f(x, y) - f(x_0, y_0) \approx \langle \nabla f(x_0, y_0), \Delta \vec{r} \rangle\]

<|ref|>equation<|/ref|><|det|>[[259, 245, 533, 272]]<|/det|>
\[\Delta f \approx \langle \nabla f(x_0, y_0), \Delta \vec{\tau} \rangle\]

<|ref|>equation<|/ref|><|det|>[[290, 280, 700, 314]]<|/det|>
\[= \frac{\partial z}{\partial x} f(x_0, y_0) \Delta x + \frac{\partial z}{\partial y} f(x_0, y_0)  \Delta y\]

<|ref|>text<|/ref|><|det|>[[111, 343, 550, 370]]<|/det|>
es ergibt sich das totale Differential : 

<|ref|>equation<|/ref|><|det|>[[130, 375, 450, 411]]<|/det|>
\[df(x, y) = \frac{\partial z}{\partial x} dx + \frac{\partial z}{\partial y} dy\]

<|ref|>text<|/ref|><|det|>[[20, 440, 945, 508]]<|/det|>
→ wie ändelt sich z bei geängfügige Änderung von x & y (Verschreibung findet auf Tangenkalebene statt) 

<|ref|>text<|/ref|><|det|>[[20, 519, 930, 586]]<|/det|>
→ es wird linearisierung der Funktion durchgeführt : gekrümmte Fläche f wird durch Tangenkalebene approximiert 

<|ref|>text<|/ref|><|det|>[[20, 597, 848, 666]]<|/det|>
→ Anwendung :
• Fehlerfortpflanzung
• nicht lineare Gleichungssysteme (Flugsteuerung) 

<|ref|>text<|/ref|><|det|>[[25, 696, 266, 721]]<|/det|>
in n Dimensionen : 

<|ref|>equation<|/ref|><|det|>[[30, 725, 430, 760]]<|/det|>
\[df(\vec{x}) = \frac{\partial f(\vec{x})}{\partial x_1} dx_1 + \ldots + \frac{\partial f(\vec{x})}{\partial x_n} dx_n\]

<|ref|>equation<|/ref|><|det|>[[35, 771, 290, 799]]<|/det|>
\[\vec{x} \in \mathbb{R}^n, \quad f : \mathbb{R}^n \to \mathbb{R}\]

<|ref|>text<|/ref|><|det|>[[25, 833, 280, 858]]<|/det|>
andere ausgedrückt : 

<|ref|>equation<|/ref|><|det|>[[35, 866, 465, 911]]<|/det|>
\[\lim_{\Delta \vec{r} \to 0} \frac{|f(\vec{x} + \Delta \vec{r}) - f(\vec{x}) - \langle \nabla f(\vec{x}), \Delta \vec{r} \rangle|}{\lvert \Delta \vec{r} \rvert} = 0\]