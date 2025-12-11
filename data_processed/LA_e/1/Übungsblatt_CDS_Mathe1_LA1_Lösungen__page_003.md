<|ref|>sub_title<|/ref|><|det|>[[107, 66, 420, 85]]<|/det|>
4. Aussagen über Python/Sympy 

<|ref|>table<|/ref|><|det|>[[107, 95, 920, 277]]<|/det|>
<table><tr><td>Welche der folgenden Aussagen sind wahr und welche falsch?</td><td>wahr</td><td>falsch</td></tr><tr><td>a) Python/Sympy wurde speziell für den Unterricht an Schulen entwickelt.</td><td>○</td><td>●</td></tr><tr><td>b) Python/Sympy ist die Abkürzung von "Symbolic Python".</td><td>●</td><td>○</td></tr><tr><td>c) Python/Sympy ist ein CAS (Computer-Algebra-Systeme).</td><td>●</td><td>○</td></tr><tr><td>d) Die Kernkompetenzen von Python/Sympy sind Numerik, Datenverarbeitung und Datenvisualisierung.</td><td>○</td><td>●</td></tr><tr><td>e) Python/Sympy ist für die gängigen Betriebssysteme Windows, Mac und Linux erhältlich.</td><td>●</td><td>○</td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[107, 319, 504, 337]]<|/det|>
5. Elementare Algebra mit Python/Sympy 

<|ref|>text<|/ref|><|det|>[[107, 336, 593, 354]]<|/det|>
Wir betrachten den folgenden Code für Python/Sympy. 

<|ref|>text<|/ref|><|det|>[[107, 359, 390, 374]]<|/det|>
# Python initialisieren: 

<|ref|>text<|/ref|><|det|>[[107, 374, 446, 390]]<|/det|>
import IPython.display as dp; 

<|ref|>text<|/ref|><|det|>[[107, 391, 333, 406]]<|/det|>
import sympy as sp; 

<|ref|>text<|/ref|><|det|>[[107, 406, 377, 422]]<|/det|>
# Python konfigurieren: 

<|ref|>text<|/ref|><|det|>[[107, 422, 330, 437]]<|/det|>
sp.init_printing(); 

<|ref|>text<|/ref|><|det|>[[107, 437, 410, 453]]<|/det|>
x, y, z=sp.symbols('x, y, z'); 

<|ref|>text<|/ref|><|det|>[[107, 453, 250, 468]]<|/det|>
# Parameter: 

<|ref|>text<|/ref|><|det|>[[107, 469, 480, 485]]<|/det|>
p=x**x**2*(x**2-4)*(x**2-2*x-15); 

<|ref|>text<|/ref|><|det|>[[107, 486, 283, 501]]<|/det|>
# Berechnungen: 

<|ref|>text<|/ref|><|det|>[[107, 501, 283, 517]]<|/det|>
f=sp.expand(p); 

<|ref|>text<|/ref|><|det|>[[107, 517, 283, 533]]<|/det|>
g=sp.factor(p); 

<|ref|>text<|/ref|><|det|>[[107, 533, 310, 549]]<|/det|>
h=sp.simplify(p); 

<|ref|>text<|/ref|><|det|>[[107, 550, 230, 566]]<|/det|>
# Ausgabe: 

<|ref|>text<|/ref|><|det|>[[107, 566, 270, 582]]<|/det|>
dp.display(f); 

<|ref|>text<|/ref|><|det|>[[107, 582, 270, 598]]<|/det|>
dp.display(g); 

<|ref|>text<|/ref|><|det|>[[107, 598, 270, 614]]<|/det|>
dp.display(h); 

<|ref|>text<|/ref|><|det|>[[117, 624, 920, 659]]<|/det|>
a) Wir implementieren den Code in Python/Sympy und führen ihn aus. Im Output erhalten wir die Terme 

<|ref|>equation<|/ref|><|det|>[[182, 665, 920, 684]]<|/det|>
\[60 x^3 + 8 x^4 - 19 x^5 - 2 x^6 + x^7 \quad (3)\]

<|ref|>equation<|/ref|><|det|>[[150, 692, 920, 712]]<|/det|>
\[(-5 + x)(-2 + x) x^3 (2 + x) (3 + x) \quad (4)\]

<|ref|>equation<|/ref|><|det|>[[206, 718, 920, 738]]<|/det|>
\[x^3 (-4 - x^2) (-15 - 2x + x^2) \quad (5)\]

<|ref|>equation<|/ref|><|det|>[[202, 745, 920, 765]]<|/det|>
\[(-5 + x) x^3 (3 + x) (-4 + x^2). \quad (6)\]

<|ref|>text<|/ref|><|det|>[[117, 774, 920, 809]]<|/det|>
b) Wir fassen die Wirkungen der drei Befehle expand, factor und simplify in einer Tabelle zusammen. 

<|ref|>table<|/ref|><|det|>[[150, 813, 536, 919]]<|/det|>
<table><tr><td>Befehl</td><td>Wirkung</td></tr><tr><td>expand</td><td>Vollständiges Ausmultiplizieren</td></tr><tr><td>factor</td><td>Vollständiges Faktorisieren</td></tr><tr><td>simplify</td><td>Einfaches Vereinfachen</td></tr></table>