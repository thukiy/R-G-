<|ref|>sub_title<|/ref|><|det|>[[114, 81, 568, 100]]<|/det|>
## 7. Trigonometrische Zahlen mit Python/Numpy 

<|ref|>text<|/ref|><|det|>[[114, 99, 780, 117]]<|/det|>
Berechnen Sie die Konversionen aus Aufgabe 5 und 6 mit Python/Numpy. 

<|ref|>text<|/ref|><|det|>[[114, 131, 250, 149]]<|/det|>
für Aufgabe 5: 

<|ref|>text<|/ref|><|det|>[[114, 148, 315, 164]]<|/det|>
# Initialisieren 

<|ref|>text<|/ref|><|det|>[[114, 164, 348, 181]]<|/det|>
import numpy as np; 

<|ref|>text<|/ref|><|det|>[[114, 181, 260, 196]]<|/det|>
# Parameter 

<|ref|>text<|/ref|><|det|>[[114, 196, 325, 213]]<|/det|>
r=4; phi=np.pi/2; 

<|ref|>text<|/ref|><|det|>[[114, 213, 270, 229]]<|/det|>
# Berechnung 

<|ref|>text<|/ref|><|det|>[[114, 229, 515, 246]]<|/det|>
z=r*(np.cos(phi)+1j*np.sin(phi)); 

<|ref|>text<|/ref|><|det|>[[114, 245, 234, 261]]<|/det|>
# Ausgabe 

<|ref|>text<|/ref|><|det|>[[114, 260, 410, 277]]<|/det|>
print('z=', f"{z:#.3}"); 

<|ref|>text<|/ref|><|det|>[[114, 293, 250, 310]]<|/det|>
für Aufgabe 6: 

<|ref|>text<|/ref|><|det|>[[114, 309, 315, 326]]<|/det|>
# Initialisieren 

<|ref|>text<|/ref|><|det|>[[114, 326, 348, 342]]<|/det|>
import numpy as np; 

<|ref|>text<|/ref|><|det|>[[114, 342, 260, 358]]<|/det|>
# Parameter 

<|ref|>text<|/ref|><|det|>[[114, 358, 170, 374]]<|/det|>
z=3; 

<|ref|>text<|/ref|><|det|>[[114, 374, 270, 390]]<|/det|>
# Berechnung 

<|ref|>text<|/ref|><|det|>[[114, 390, 469, 407]]<|/det|>
r=np.abs(z); phi=np.angle(z); 

<|ref|>text<|/ref|><|det|>[[114, 406, 234, 422]]<|/det|>
# Ausgabe 

<|ref|>text<|/ref|><|det|>[[114, 421, 648, 439]]<|/det|>
print('z=', z, '=', r, '*cis(', phi/np.pi, 'pi)'); 

<|ref|>sub_title<|/ref|><|det|>[[114, 455, 547, 472]]<|/det|>
## 8. Aussagen über quadratische Gleichungen 

<|ref|>text<|/ref|><|det|>[[114, 471, 590, 489]]<|/det|>
Gegeben sei die allgemeine quadratische Gleichung 

<|ref|>equation<|/ref|><|det|>[[114, 488, 494, 505]]<|/det|>
\[ax^2 + bx + c = 0 \text{ mit } a, b, c \in \mathbb{R} \text{ und } a \neq 0.\]

<|ref|>text<|/ref|><|det|>[[114, 504, 680, 522]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[114, 520, 880, 743]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Die Koeffizienten a,b,c können so gewählt werden, dass es keine Lösung in ℝ gibt.</td><td>X</td><td></td></tr><tr><td>b) Die Koeffizienten a,b,c können so gewählt werden, dass es keine Lösung in ℂ gibt.</td><td></td><td>X</td></tr><tr><td>c) Für jede Wahl der Koeffizienten a,b,c liegen zwei verschiedene Lösungen in ℂ vor.</td><td></td><td>X</td></tr><tr><td>d) Die Koeffizienten a,b,c können so gewählt werden, dass x₁ = 1 und x₂ = i die beiden Lösungen sind.</td><td></td><td>X</td></tr><tr><td>e) Gibt es 2 Lösungen x₁ und x₂, dann gilt entweder x₂ = x₁* oder x₁, x₂ ∈ ℝ.</td><td>X</td><td></td></tr><tr><td>f) Die Anzahl der Lösungen kann anhand der Diskriminante beurteilt werden.</td><td>X</td><td></td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[114, 758, 401, 776]]<|/det|>
## 9. Quadratische Gleichungen 

<|ref|>text<|/ref|><|det|>[[114, 775, 795, 810]]<|/det|>
Bestimmen Sie die Lösungen der quadratischen Gleichung in ℂ mit Hilfe der Mitternachtsformel. 

<|ref|>equation<|/ref|><|det|>[[114, 809, 815, 845]]<|/det|>
\[
\begin{align*}
a) x^2 + 1 &= 0 && b) x^2 - 10x + 74 &= 0 && c) 2x^2 + 4 &= x \\
d) 3t^2 &= -30t - 507 && e) w = 2 + w^2 && f) s(s + 1) = 2s^2 + 1
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 860, 145, 876]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[114, 875, 280, 893]]<|/det|>
\[
a = 1, b = 0, c = 1
\]

<|ref|>equation<|/ref|><|det|>[[114, 891, 407, 910]]<|/det|>
Diskriminante: D = b² - 4ac = -4

<|ref|>equation<|/ref|><|det|>[[114, 908, 393, 927]]<|/det|>
Es ergeben sich die Lösungen

<|ref|>text<|/ref|><|det|>[[114, 926, 508, 943]]<|/det|>