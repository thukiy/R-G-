<|ref|>text<|/ref|><|det|>[[115, 84, 142, 100]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[115, 99, 848, 115]]<|/det|>
Unter Verwendung von Polarkoordinaten transformiert sich der Integrand wie folgt (x = r · cos φ, y = r · sin φ): 

<|ref|>equation<|/ref|><|det|>[[161, 121, 528, 137]]<|/det|>
\[z = f(x; y) = 1 + x + y = 1 + r \cdot \cos \varphi + r \cdot \sin \varphi\]

<|ref|>text<|/ref|><|det|>[[115, 144, 760, 159]]<|/det|>
Das Flächenelement \(dA\) lautet in Polarkoordinaten \(dA = r \, dr \, d\varphi\), die Integrationsgrenzen sind (sie) 

<|ref|>equation<|/ref|><|det|>[[161, 166, 415, 181]]<|/det|>
\[r\text{-Integration:} \quad \text{von } r = 0 \text{ bis } r = 1\]

<|ref|>equation<|/ref|><|det|>[[161, 188, 437, 203]]<|/det|>
\[\varphi\text{-Integration:} \quad \text{von } \varphi = 0 \text{ bis } \varphi = 2\pi\]

<|ref|>text<|/ref|><|det|>[[115, 207, 197, 221]]<|/det|>
Damit gilt: 

<|ref|>equation<|/ref|><|det|>[[161, 227, 664, 304]]<|/det|>
\[I = \iint_{(A)} (1 + x + y) \, dA = \int_{\varphi=0}^{2\pi} \int_{r=0}^{1} (1 + r \cdot \cos \varphi + r \cdot \sin \varphi) \, r \, dr \, d\varphi = \\ = \int_{\varphi=0}^{2\pi} \int_{r=0}^{1}(r + r^2 \cdot \cos \varphi + r^2 \cdot \sin \varphi) \, dr \, d\varphi\]

<|ref|>text<|/ref|><|det|>[[115, 341, 422, 356]]<|/det|>
Wir integrieren zunächst nach \(r\), dann nach \(\varphi\). 

<|ref|>text<|/ref|><|det|>[[115, 366, 400, 381]]<|/det|>
Innere Integration (nach der Variablen \(r\)) 

<|ref|>equation<|/ref|><|det|>[[161, 388, 750, 472]]<|/det|>
\[\int_{r=0}^{1} (r + r^2 \cdot \cos \varphi + r^2 \cdot \sin\varphi) \, dr = \left[ \frac{1}{2} r^2 + \frac{1}{3} r^3 \cdot \cos\varphi + \frac{1}{3} r^3 \cdot \sin\varphi \right]_{r=0}^{1} = \\ = \frac{1}{2} + \frac{1}{3} \cdot \cos\varphi + \frac{1}{3} \cdot \sin\varphi - 0 - 0 - 0 = \frac{1}{2} + \frac{1}{3} \cdot \sin\varphi + \frac{1}{3} \cdot \sin\varphi\]

<|ref|>text<|/ref|><|det|>[[115, 472, 415, 488]]<|/det|>
Äußere Integration (nach der Variablen \(\varphi\)) 

<|ref|>equation<|/ref|><|det|>[[161, 495, 768, 590]]<|/det|>
\[I = \int_{\varphi=0}^{2\pi} \left( \frac{1}{2} + \frac{1}{3} \cdot \cos \varphi + \frac{1}{3} \cdot \sin \varphi \right) \, d\varphi = \left[ \frac{1}{2} \varphi + \frac{1}{3} \cdot \sin \varphi - \frac{1}{3} \cdot \cos \varphi \right]_{0}^{2\pi} = \\ = \pi + \frac{1}{3} \cdot \sin(2\pi) - \frac{1}{3} \cdot \cos(2\pi) - 0 - \frac{1}{3} \cdot \sin 0 + \frac{1}{3} \cdot \cos 0 = \pi - \frac{1}{3} + \frac{1}{3} = \pi\]

<|ref|>text<|/ref|><|det|>[[115, 597, 242, 612]]<|/det|>
Ergebnis: \(I = \pi\) 

<|ref|>text<|/ref|><|det|>[[115, 612, 144, 628]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[115, 630, 866, 671]]<|/det|>
\(I = \iint_A (3\sqrt{x^2 + y^2} + 4) \, dA\), wobei der Integrationsbereich der angegebene Kreisring sein soll. 

<|ref|>image<|/ref|><|det|>[[120, 672, 344, 824]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[115, 826, 807, 842]]<|/det|>
Die Transformationsgleichungen für den Übergang von kartesischen Koordinaten zu Polarkoordinaten lauten: 

<|ref|>equation<|/ref|><|det|>[[161, 847, 495, 863]]<|/det|>
\[x = r \cdot \cos \varphi, \quad y = r \cdot \sin \varphi, \quad dA = r \, dr \, d\varphi\]

<|ref|>text<|/ref|><|det|>[[115, 869, 608, 884]]<|/det|>
Die Integrationsgrenzen des kreisringförmigen Integrationsbereiches sind (sie) 

<|ref|>equation<|/ref|><|det|>[[161, 890, 426, 906]]<|/det|>
\[r\text{-Integration:} \quad \text{von } r = \text{1 bis } r = 3\]

<|ref|>equation<|/ref|><|det|>[[161, 911, 440, 927]]<|/det|>
\[\varphi\text{-Integration:} \quad \text{von } \varphi=0 \text{ bis } \varphi=2\pi\]