<|ref|>text<|/ref|><|det|>[[120, 83, 300, 98]]<|/det|>
Unter Berücksichtigung von  

<|ref|>equation<|/ref|><|det|>[[163, 102, 618, 145]]<|/det|>
\[x^{2} + y^{2} = r^{2}\cdot \cos^{2}\phi +r^{2}\cdot \sin^{2}\phi = r^{2}(\cos^{2}\phi +\sin^{2}\phi) = r^{2}\]  

<|ref|>text<|/ref|><|det|>[[118, 150, 518, 166]]<|/det|>
transformiert sich der Integrand des Doppelintegrals wie folgt:  

<|ref|>equation<|/ref|><|det|>[[163, 170, 581, 194]]<|/det|>
\[z = f(x;y) = 3\cdot \sqrt{x^{2} + y^{2}} +4 = 3\cdot \sqrt{r^{2}} +4 = 3r + 4\]  

<|ref|>text<|/ref|><|det|>[[118, 200, 472, 216]]<|/det|>
Das Doppelintegral \(I\) lautet damit in Polarkoordinaten:  

<|ref|>equation<|/ref|><|det|>[[163, 222, 800, 273]]<|/det|>
\[I = \iint_{(A)}(3\cdot \sqrt{x^{2} + y^{2}} +4)dA = \int_{\phi = 0}^{2\pi}\int_{r = 1}^{3}(3r + 4)rdrd\phi = \int_{\phi = 0}^{2\pi}\int_{r = 1}^{2\pi}(3r^{2} + 4)rdrd\phi\]  

<|ref|>text<|/ref|><|det|>[[118, 279, 672, 295]]<|/det|>
Die Auswertung erfolgt in der üblichen Weise (erst nach \(r\) , dann nach \(\phi\) integrieren).  

<|ref|>text<|/ref|><|det|>[[118, 296, 401, 310]]<|/det|>
Innere Integration (nach der Variablen \(r\) )  

<|ref|>equation<|/ref|><|det|>[[160, 316, 610, 360]]<|/det|>
\[\int_{r = 1}^{3}(3r^{2} + 4r)d r = \left[r^{3} + 2r^{2}\right]_{r = 1}^{3} = 27 + 18 - 1 - 2 = 42\]  

<|ref|>text<|/ref|><|det|>[[118, 363, 410, 378]]<|/det|>
Äußere Integration (nach der Variablen \(\phi\) )  

<|ref|>equation<|/ref|><|det|>[[160, 384, 629, 430]]<|/det|>
\[I = \int_{\phi = 0}^{2\pi}42d\phi = 42\cdot \int_{0}^{2\pi}1d\phi = 42[\phi ]_{0}^{2\pi} = 42(2\pi -0) = 84\pi\]  

<|ref|>text<|/ref|><|det|>[[118, 440, 256, 455]]<|/det|>
Ergebnis: \(I = 84\pi\)  

<|ref|>sub_title<|/ref|><|det|>[[116, 472, 270, 489]]<|/det|>
## 7. Schwerpunkt  

<|ref|>text<|/ref|><|det|>[[116, 488, 860, 523]]<|/det|>
Bestimmen Sie den Flächenschwerpunkt S des skizzierten Kreisringausschnitts mit Innenradius \(r_1 = 2\) und Aussenradius \(r_2 = 6\) .  

<|ref|>image<|/ref|><|det|>[[315, 526, 680, 680]]<|/det|>  

<|ref|>text<|/ref|><|det|>[[116, 679, 700, 694]]<|/det|>
Der Integrationsbereich für die Berechnung des Flächenschwerpunktes \(S = (x_S; y_S)\) lautet:  

<|ref|>text<|/ref|><|det|>[[160, 701, 415, 716]]<|/det|>
\(r\) - Integration: von \(r = 2\) bis \(r = 6\)  

<|ref|>text<|/ref|><|det|>[[160, 724, 422, 740]]<|/det|>
\(\phi\) - Integration: von \(\phi = 0\) bis \(\phi = \pi\)  

<|ref|>text<|/ref|><|det|>[[116, 747, 763, 763]]<|/det|>
Der benötigte Flächeninhalt \(A\) lässt sich elementar berechnen (als Differenz zweier Halbkreisflächen):  

<|ref|>equation<|/ref|><|det|>[[160, 768, 675, 798]]<|/det|>
\[A = \frac{1}{2} (\pi r_2^2 -\pi r_1^2) = \frac{1}{2}\pi (r_2^2 -r_1^2) = \frac{1}{2}\pi (36 - 4) = 16\pi = 50,2655\]  

<|ref|>text<|/ref|><|det|>[[116, 802, 866, 830]]<|/det|>
Wegen der Spiegelsymmetrie der Fläche liegt der Schwerpunkt auf der \(y\) - Achse. Somit ist \(x_S = 0\) . Die Ordinate \(y_S\) berechnen wir mit dem folgenden Doppelintegral:  

<|ref|>equation<|/ref|><|det|>[[160, 837, 528, 884]]<|/det|>
\[y_S = \frac{1}{A}\cdot \iint_{(A)}y dA = \frac{1}{16\pi}\cdot \int_{\phi = 0}^{2\pi}\int_{r = 2}^{6}r^2\cdot \sin \phi dr d\phi\]