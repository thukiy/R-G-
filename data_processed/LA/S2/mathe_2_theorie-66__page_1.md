<|ref|>text<|/ref|><|det|>[[20, 12, 621, 50]]<|/det|>
Bsp : 
\[\frac{z_1}{z_2} = \frac{2e^{i\frac{\pi}{6}}}{3e^{i\frac{3\pi}{6}}} = \frac{2}{3} \cdot e^{i(\frac{\pi}{6} - \frac{3\pi}{6})} = \frac{2}{3} \cdot e^{-i\frac{2\pi}{6}}\] 

<|ref|>equation<|/ref|><|det|>[[210, 63, 580, 95]]<|/det|>
\[= \frac{2}{3} \cdot (\cos(-\frac{2}{6}\pi) + i \cdot \sin(-\frac{2}{6}\pi))\]

<|ref|>equation<|/ref|><|det|>[[210, 102, 636, 135]]<|/det|>
\[= \frac{2}{3} \cdot (-\frac{1}{2} \sqrt{3} + i \cdot \frac{1}{2}) = -\frac{1}{3} \sqrt{3} + \frac{1}{3} i\]

<|ref|>text<|/ref|><|det|>[[20, 170, 207, 195]]<|/det|>
Bemelwungen : 

<|ref|>equation<|/ref|><|det|>[[48, 205, 425, 234]]<|/det|>
\[\cdot |e^{i\varphi}| = \sqrt{\cos^2\varphi + \sin^2\varphi} = 1\]

<|ref|>equation<|/ref|><|det|>[[48, 241, 567, 273]]<|/det|>
\[\cdot e^{i0} = e^{i \cdot 2k\pi} = 1 \quad k \in \mathbb{Z}\]

<|ref|>equation<|/ref|><|det|>[[48, 280, 211, 310]]<|/det|>
\[\cdot e^{i\pi} = -1\]

<|ref|>text<|/ref|><|det|>[[20, 345, 155, 369]]<|/det|>
Polenzieen 

<|ref|>text<|/ref|><|det|>[[50, 383, 835, 411]]<|/det|>
Berechnungen von \(z^n\) bisher aufwendig, mit Exponentialform einfacher 

<|ref|>text<|/ref|><|det|>[[20, 440, 480, 470]]<|/det|>
Bsp : 
\[z = 2 + 2i \quad z^{12} = ?\]

<|ref|>equation<|/ref|><|det|>[[155, 480, 355, 508]]<|/det|>
\[|r| = \sqrt{8} = 2\sqrt{2}\]

<|ref|>equation<|/ref|><|det|>[[155, 513, 590, 550]]<|/det|>
\[\varphi = \frac{\pi}{4} \quad z \text{ liegt im Quadranten}\]

<|ref|>equation<|/ref|><|det|>[[155, 552, 340, 585]]<|/det|>
\[z = 2\sqrt{2} e^{i\frac{\pi}{4}}\]

<|ref|>equation<|/ref|><|det|>[[210, 590, 899, 666]]<|/det|>
\[\begin{align*}
&\rightarrow z^{12} = (2\sqrt{2} e^{i\frac{\pi}{4}})^{12} \\
&= (2\sqrt{2})^{12} (e^{i\frac{\pi}{4}})^{12} \\
&= 8^6 \cdot e^{i \cdot 3\pi - 2\pi} \\
&= 8^6 \cdot e^{i\pi} \\
&= -8^6
\end{align*}\]

<|ref|>text<|/ref|><|det|>[[20, 699, 328, 723]]<|/det|>
Radizieren (Wurzel ziehen) 

<|ref|>equation<|/ref|><|det|>[[48, 735, 576, 767]]<|/det|>
\[z^3 = w, \text{ wobei } w \text{ eine komplexe Zahl sei}\]

<|ref|>equation<|/ref|><|det|>[[48, 775, 320, 804]]<|/det|>
\[z^3 = w = -3 + \sqrt{3} i\]

<|ref|>equation<|/ref|><|det|>[[115, 816, 860, 848]]<|/det|>
\[|w| = \sqrt{9+3} = \sqrt{12} \quad \varphi = \arg(z) = \frac{5}{6}\pi \quad (2. Quadrant)\]

<|ref|>equation<|/ref|><|det|>[[115, 850, 619, 886]]<|/det|>
\[w = \sqrt{12} \cdot e^{i(\frac{5}{6}\pi + 2k\pi)} = z^3 \quad |\frac{3}{2}|\]

<|ref|>equation<|/ref|><|det|>[[48, 888, 690, 921]]<|/det|>
\[z_k = (12^{1/2})^{1/3} \cdot (e^{i(\frac{5}{6}\pi + 2k\pi)})^{1/3} = 12^{1/6} \cdot e^{i(\frac{5}{6}\pi + \frac{5}{6}k\pi)}\]

<|ref|>equation<|/ref|><|det|>[[48, 925, 570, 960]]<|/det|>
\[z_0 = 12^{1/6} \cdot e^{i\frac{5}{6}\pi} \quad z_1 = 12^{1/6} \cdot e^{i\frac{7}{6}\pi}\]

<|ref|>equation<|/ref|><|det|>[[48, 963, 732, 998]]<|/det|>
\[z_2 = 12^{1/6} \cdot e^{i\frac{23}{6}\pi} \quad z_3 = z_0, \quad z_4 = z_1, \quad z_5 = z_2 \quad \dots\]