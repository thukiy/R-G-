<|ref|>text<|/ref|><|det|>[[117, 85, 624, 101]]<|/det|>
(Transformationsgleichungen: \(y = r \cdot \sin \varphi\) , Flächenelement \(dA = r \, dr \, d\varphi\))  

<|ref|>text<|/ref|><|det|>[[117, 111, 399, 127]]<|/det|>
Innere Integration (nach der Variablen \(r\) )  

<|ref|>equation<|/ref|><|det|>[[160, 135, 715, 216]]<|/det|>
\[\int_{r = 2}^{6}r^{2}\cdot \sin \phi d r = \sin \phi \cdot \int_{r = 2}^{6}r^{2}d r = \sin \phi \left[\frac{1}{3} r^{3}\right]_{r = 2}^{6} = \frac{1}{3}\cdot \sin \phi \left[r^{3}\right]_{r = 2}^{6} =\] \[\qquad = \frac{1}{3}\cdot \sin \phi (216 - 8) = \frac{208}{3}\cdot \sin \phi\]  

<|ref|>text<|/ref|><|det|>[[117, 216, 410, 232]]<|/det|>
Außere Integration (nach der Variablen \(\phi\) )  

<|ref|>equation<|/ref|><|det|>[[157, 240, 866, 290]]<|/det|>
\[y_{s} = \frac{1}{16\pi}\cdot \frac{208}{3}\cdot \int_{\phi = 0}^{\pi}\sin \phi d\phi = \frac{13}{3\pi}\left[-\cos \phi \right]_{0}^{\pi} = \frac{13}{3\pi}\left(-\cos \pi +\cos 0\right) = \frac{13}{3\pi}\left(1 + 1\right) = \frac{26}{3\pi} = 2,7587\]  

<|ref|>text<|/ref|><|det|>[[116, 298, 327, 314]]<|/det|>
Schwerpunkt: \(S = (0; 2,7587)\)  

<|ref|>sub_title<|/ref|><|det|>[[116, 328, 461, 346]]<|/det|>
## 8. Volumen zylinderförmiger Körper  

<|ref|>text<|/ref|><|det|>[[115, 346, 847, 401]]<|/det|>
Berechnen Sie das Volumen \(V\) des Körpers, der durch einen in der xy- Ebene gelegenen kreisförmigen Boden mit Radius \(r = 1\) und einen Deckel mit der Fläche \(z = e^{x^{2} + y^{2}}\) gebildet wird.  

<|ref|>image<|/ref|><|det|>[[405, 404, 597, 536]]<|/det|>  

<|ref|>text<|/ref|><|det|>[[117, 550, 868, 603]]<|/det|>
Wir verwenden Polarkoordinaten (wegen der Kreis- bzw. Rotationssymmetrie). Der kreisförmige „Boden“ liefert den Integrationsbereich \(1: 0 \leq r \leq 1, 0 \leq \phi \leq 2\pi\) . Die Rotationsfläche bildet den „Deckel“ des zylindrischen Körpers, ihre Gleichung in Polarkoordinaten erhalten wir wie folgt (Transformationsgleichungen: \(x = r \cdot \cos \phi , y = r \cdot \sin \phi\) ):  

<|ref|>equation<|/ref|><|det|>[[161, 610, 790, 650]]<|/det|>
\[x^{2} + y^{2} = r^{2}\cdot \cos^{2}\phi +r^{2}\cdot \sin^{2}\phi = r^{2}\left(\cos^{2}\phi +\sin^{2}\phi\right) = r^{2}\Rightarrow z = \mathrm{e}^{x^{2} + y^{2}} = \mathrm{e}^{r^{2}}\]  

<|ref|>text<|/ref|><|det|>[[118, 655, 621, 672]]<|/det|>
(unter Verwendung des „trigonometrischen Pythagoras“ \(\sin^{2}\phi +\cos^{2}\phi = 1\) )  

<|ref|>text<|/ref|><|det|>[[118, 676, 357, 691]]<|/det|>
Damit gilt für das gesuchte Volumen:  

<|ref|>equation<|/ref|><|det|>[[161, 699, 676, 747]]<|/det|>
\[V = \iint_{(\mathrm{A})}z d A = \int_{\phi = 0}^{2\pi}\int_{r = 0}^{1}\mathrm{e}^{r^{2}}\cdot r d r d\phi \quad (\mathrm{Flächenelement} d A = r d r d\phi)\]  

<|ref|>text<|/ref|><|det|>[[118, 761, 400, 776]]<|/det|>
Innere Integration (nach der Variablen \(r\) )  

<|ref|>text<|/ref|><|det|>[[118, 781, 538, 796]]<|/det|>
Wir lösen das innere Integral mit Hilfe der folgenden Substitution:  

<|ref|>equation<|/ref|><|det|>[[161, 802, 775, 840]]<|/det|>
\[u = r^{2},\quad \frac{d u}{d r} = 2r,\quad d r = \frac{d u}{2r},\quad \mathrm{Grenzen}\subset \mathrm{unten:}r = 0\Rightarrow u = 0\]  

<|ref|>equation<|/ref|><|det|>[[161, 852, 822, 896]]<|/det|>
\[\int_{r = 0}^{1}\mathrm{e}^{r^{2}}\cdot r d\tau = \int_{u = 0}^{1}\mathrm{e}^{u}\cdot \frac{d u}{2\pi} = \frac{1}{2}\cdot \int_{u = 0}^{1}\mathrm{e}^{u}d u = \frac{1}{2}\left[\mathrm{e}^{u}\right]_{u = 0}^{1} = \frac{1}{2}\left(\mathrm{e}^{1} - \mathrm{e}^{0}\right) = \frac{1}{2}\left(\mathrm{e} - 1\right)\]