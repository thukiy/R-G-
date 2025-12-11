<|ref|>sub_title<|/ref|><|det|>[[75, 66, 587, 85]]<|/det|>
## 3. Skriptvorlage für Berechnungen mit Python/Numpy 

<|ref|>text<|/ref|><|det|>[[75, 84, 888, 120]]<|/det|>
Wir betrachten den folgenden Code für Python/Numpy zur Berechnung der *Hypotenuse* eines *rechtswinkligen Dreiecks* aus den beiden *Katheten* \(a \approx 12.3\) cm und \(b \approx 8.14\) cm. 

<|ref|>text<|/ref|><|det|>[[75, 127, 418, 255]]<|/det|>
# Python initialisieren:
import numpy as np;
# Parameter:
a=12.3; b=8.14; pr=3; ME='cm';
# Berechnungen:
c=np.sqrt(a**2+b**2);
# Ausgabe:
print(__file__); 

<|ref|>text<|/ref|><|det|>[[75, 275, 504, 323]]<|/det|>
print(f"Seite a = {a:#.{pr}g} {ME}"); print(f"Seite b = {b:#.{pr}g} {ME}"); print(f"Seite c = {c:#.{pr}g} {ME}"); 

<|ref|>text<|/ref|><|det|>[[90, 363, 890, 422]]<|/det|>
a) Wir implementieren den Code in Python/Numpy, speichern Sie das Skript unter einem ge-eigneten Dateinamen und führen es aus. Gemäss Output beträgt die *Länge* der *Hypotenuse* des *Dreiecks* 

<|ref|>equation<|/ref|><|det|>[[118, 428, 257, 446]]<|/det|>
\[c \approx 14.7 \text{ cm.} (1)\]

<|ref|>text<|/ref|><|det|>[[90, 468, 844, 487]]<|/det|>
b) Die Zeile print(__file__); bewirkt die Ausgabe des Dateinamens der Skript-Datei. 

<|ref|>text<|/ref|><|det|>[[90, 494, 880, 530]]<|/det|>
c) Wir variieren den Wert des Parameters pr und beobachten die Wirkung dieser Variationen. Offensichtlich ist pr jeweils gerade die Anzahl Dezimalstellen im ausgegebenen Wert. 

<|ref|>text<|/ref|><|det|>[[90, 545, 850, 563]]<|/det|>
d) Wir modifizieren den Code für die *Katheten* mit *Längen* \(a \approx 0.85\) km und \(b \approx 234\) m. 

<|ref|>text<|/ref|><|det|>[[118, 571, 397, 600]]<|/det|>
# Python initialisieren:
import numpy as np;
# Parameter:
a=0.85e3; pr_a=2; sc_a=1.0e-3; ME_a='km'; \ 
b=234.; pr_b=3; sc_b=1.0; ME_b='m'; \ 
pr_c=2; sc_c=1.0e-3; ME_c='km'; \ 

<|ref|>text<|/ref|><|det|>[[118, 666, 360, 695]]<|/det|>
# Berechnungen:
c=np.sqrt(a**2+b**2);
# Ausgabe:
 print(__file__);
 print(f"Seite a = {a*sc_a:#.{pr_a}g} {ME_a}"); 
 print(f"Seite b = {b*sc_b:#.{pr_b}g} {ME_b}"); 
 print(f"Seite c = {c*sc_c:#.{pr_c}g} {ME_c}"); 

<|ref|>text<|/ref|><|det|>[[118, 805, 797, 823]]<|/det|>
Gemäss Output beträgt die *Länge* der *Hypotenuse* des *Dreies* in diesem Fall 

<|ref|>equation<|/ref|><|det|>[[118, 838, 230, 856]]<|/det|>
\[c \approx 0.88 \text{ km.}\]