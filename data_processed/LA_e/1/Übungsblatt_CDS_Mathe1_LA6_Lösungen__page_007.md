<|ref|>text<|/ref|><|det|>[[117, 82, 310, 100]]<|/det|>
Die Diskriminante ist 

<|ref|>equation<|/ref|><|det|>[[117, 108, 590, 128]]<|/det|>
\[D = b^2 - 4 \cdot a \cdot c = 3^2 - 4 \cdot 2 \cdot (-2) = 9 + 16 = 25 > 0.\]

<|ref|>text<|/ref|><|det|>[[117, 137, 768, 156]]<|/det|>
Mit Hilfe der Mitternachtsformel für quadratische Gleichungen erhalten wir 

<|ref|>equation<|/ref|><|det|>[[117, 162, 478, 201]]<|/det|>
\[s_{1,2} = \frac{-b \pm \sqrt{D}}{2a} = \frac{-3 \pm \sqrt{25}}{2 \cdot 2} = \frac{-3 \pm 5}{4}.\]

<|ref|>text<|/ref|><|det|>[[117, 205, 666, 223]]<|/det|>
Die quadratische Gleichung hat somit die zwei reellen Lösungen 

<|ref|>equation<|/ref|><|det|>[[255, 228, 740, 265]]<|/det|>
\[s_1 = \frac{-3 - 5}{4} = \frac{-8}{4} = -2 \quad \text{und} \quad s_2 = \frac{-3 + 5}{4} = \frac{2}{4} = \frac{1}{2}.\]

<|ref|>text<|/ref|><|det|>[[117, 270, 592, 288]]<|/det|>
Wir betrachten die Fälle \(s = -2\) und \(s = 1/2\) getrennt. 

<|ref|>text<|/ref|><|det|>[[117, 291, 636, 310]]<|/det|>
**Fall 1:** \(s = -2\): In diesem Fall betrachten wir die Gleichung 

<|ref|>equation<|/ref|><|det|>[[437, 319, 592, 337]]<|/det|>
\[\sin(x) = s = -2.\]

<|ref|>text<|/ref|><|det|>[[117, 345, 872, 365]]<|/det|>
Weil für alle \(x \in \mathbb{R}\) gilt \(\sin(x) \in [-1, 1]\), finden wir in diesem Fall keine Lösung für \(x\). 

<|ref|>text<|/ref|><|det|>[[117, 366, 640, 385]]<|/det|>
**Fall 2:** \(s = 1/2\): In diesem Fall betrachten wir die Gleichung 

<|ref|>equation<|/ref|><|det|>[[440, 392, 583, 426]]<|/det|>
\[\sin(x) = s = \frac{1}{2}.\]

<|ref|>text<|/ref|><|det|>[[145, 432, 825, 451]]<|/det|>
Die Gleichung und Nebenbedingung sind demnach genau dann erfüllt, wenn gilt 

<|ref|>equation<|/ref|><|det|>[[228, 457, 783, 536]]<|/det|>
\[x \in \left( \left\{ \frac{\pi}{6} + k \cdot 2\pi \mid k \in \mathbb{Z} \right\} \cup \left\{ \frac{5\pi}{6} + k \cdot 2\pi \mid k \in \mathbb{Z} 
\right\} \right) \cap [0, 2\pi[ \quad \Leftrightarrow \quad x \in \left\{ \frac{\pi}{6} + 0 \right\} \cup \left\{ \frac{5\pi}{6} + 0 \right\}.\]

<|ref|>text<|/ref|><|det|>[[117, 540, 456, 558]]<|/det|>
Daraus erhalten wir die Lösungsmenge 

<|ref|>equation<|/ref|><|det|>[[424, 565, 570, 604]]<|/det|>
\[\mathbb{L} = \left\{ \frac{\pi}{6}, \frac{5\pi}{6} \right\}.\]

<|ref|>text<|/ref|><|det|>[[117, 625, 680, 644]]<|/det|>
## 6. Trigonometrische Gleichungen mit Python/Sympy lösen 

<|ref|>text<|/ref|><|det|>[[117, 642, 835, 661]]<|/det|>
Lösen Sie die trigonometrischen Gleichungen aus Aufgabe 5 mit Python/Sympy. 

<|ref|>text<|/ref|><|det|>[[117, 660, 150, 677]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[117, 675, 400, 692]]<|/det|>
# Python initialisieren 

<|ref|>text<|/ref|><|det|>[[117, 692, 355, 709]]<|/det|>
import sympy as sp; 

<|ref|>text<|/ref|><|det|>[[117, 708, 468, 725]]<|/det|>
import IPython.display as dp; 

<|ref|>text<|/ref|><|det|>[[117, 724, 395, 740]]<|/det|>
# Python konfigurieren 

<|ref|>text<|/ref|><|det|>[[117, 740, 350, 757]]<|/det|>
x= sp.symbols('x'); 

<|ref|>text<|/ref|><|det|>[[117, 757, 275, 773]]<|/det|>
# Berechnung 

<|ref|>text<|/ref|><|det|>[[117, 773, 433, 790]]<|/det|>
L=sp.solve(sp.sin(2*x), x); 

<|ref|>text<|/ref|><|det|>[[117, 789, 234, 805]]<|/det|>
# Ausgabe 

<|ref|>text<|/ref|><|det|>[[117, 805, 288, 822]]<|/det|>
dp.display(L); 

<|ref|>text<|/ref|><|det|>[[117, 821, 177, 838]]<|/det|>
b) - f) 

<|ref|>text<|/ref|><|det|>[[117, 837, 835, 872]]<|/det|>
analog zu a) – sehr wichtig: die Gleichung muss so umgestellt sein, dass auf der rechten Seite 0 steht