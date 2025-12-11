<|ref|>text<|/ref|><|det|>[[115, 81, 260, 98]]<|/det|>
# Parameter: 

<|ref|>text<|/ref|><|det|>[[115, 98, 275, 115]]<|/det|>
f=x/(1+x**4); 

<|ref|>text<|/ref|><|det|>[[115, 115, 300, 132]]<|/det|>
# Berechnungen: 

<|ref|>text<|/ref|><|det|>[[115, 131, 517, 149]]<|/det|>
F=sp.simplify(sp.integrate(f,x)); 

<|ref|>text<|/ref|><|det|>[[115, 148, 240, 164]]<|/det|>
# Ausgabe: 

<|ref|>text<|/ref|><|det|>[[115, 164, 288, 181]]<|/det|>
dp.display(f); 

<|ref|>text<|/ref|><|det|>[[115, 180, 288, 197]]<|/det|>
dp.display(F); 

<|ref|>text<|/ref|><|det|>[[115, 196, 222, 213]]<|/det|>
b), c), e), f) 

<|ref|>text<|/ref|><|det|>[[115, 212, 760, 230]]<|/det|>
analog zu a), jedoch Funktion f und nach Bedarf die Symbole anpassen 

<|ref|>text<|/ref|><|det|>[[115, 228, 844, 263]]<|/det|>
→ die Stammfunktion bei d) am besten mit WolframAlpha überprüfen – Lösung in Python nicht korrekt 

<|ref|>sub_title<|/ref|><|det|>[[115, 277, 400, 295]]<|/det|>
## 6. Fläche des Einheitskreises 

<|ref|>text<|/ref|><|det|>[[115, 294, 840, 345]]<|/det|>
Berechnen Sie die Fläche des Einheitskreises durch Integration, indem Sie einen geeigneten Teil des Kreisbogens als Graph einer Funktion auffassen und diesen integrieren. 

<|ref|>text<|/ref|><|det|>[[115, 344, 576, 362]]<|/det|>
Hinweis: Verwenden Sie die Substitution x = sin(u). 

<|ref|>text<|/ref|><|det|>[[115, 376, 790, 412]]<|/det|>
Wir wählen einen Viertelkreis, der im 1. Quadranten des kartesischen Koordinatensystems liegt, um die Fläche des Einheitskreises zu bestimmen. 

<|ref|>image<|/ref|><|det|>[[115, 412, 545, 639]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[115, 656, 485, 675]]<|/det|>
Für die Punkte auf dem Einheitskreis gilt: 

<|ref|>equation<|/ref|><|det|>[[306, 676, 710, 700]]<|/det|>
\[1 = x^2 + y^2 = x^2 + f^2(x) \quad \begin{vmatrix} -x^2 \\ \sqrt{\ldots} \end{vmatrix}\]

<|ref|>equation<|/ref|><|det|>[[120, 710, 707, 735]]<|/det|>
\[\Leftrightarrow \quad 1 - x^2 = f^2(x) \quad \begin{vmatrix} \sqrt{\ldots} \end{vmatrix}\]

<|ref|>equation<|/ref|><|det|>[[115, 744, 275, 767]]<|/det|>
\[f(x) = \sqrt{1 - x^2}.\]

<|ref|>text<|/ref|><|det|>[[115, 770, 844, 805]]<|/det|>
Die Fläche des Einheitskreises entspricht 4 mal der grün markierten Fläche in der obigen Abbildung: 

<|ref|>equation<|/ref|><|det|>[[120, 808, 544, 849]]<|/det|>
\[A_K = 4 \cdot A = 4 \int_0^1 f(x) \, dx = 4 \int_0^1 \sqrt{1 - x^2} \, dx.\]

<|ref|>text<|/ref|><|det|>[[115, 850, 715, 869]]<|/det|>
Um das Integral zu lösen, wählen wir die Methode der Substitution. 

<|ref|>equation<|/ref|><|det|>[[120, 868, 480, 888]]<|/det|>
\[x := \sin(u) \quad \begin{vmatrix} (\ldots)' \end{vmatrix}\]

<|ref|>equation<|/ref|><|det|>[[120, 898, 490, 919]]<|/det|>
\[1 = \cos(u) \cdot u' \quad \begin{vmatrix} : \cos(u). \end{vmatrix}\]