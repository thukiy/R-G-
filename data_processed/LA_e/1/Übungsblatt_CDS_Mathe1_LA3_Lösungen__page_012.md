<|ref|>text<|/ref|><|det|>[[113, 81, 880, 234]]<|/det|>
b=np.array([3,0,1]); pr_L=1; # Berechnungen L=np.linalg.solve(A,b); # Ausgabe print('L=',L); → „normale“ Ausgabe print(f"L={np.array2string(L,precision=pr_L)}"); → Ausgabe mittels eines f-strings; über precision werden die Nachkommastellen vorgegeben 

<|ref|>text<|/ref|><|det|>[[113, 264, 870, 536]]<|/det|>
b) Lösung für Aufgabe 3a)
Mit Sympy:
# Initialisieren
import sympy as sp;
import IPython.display as dp;
# Parameter
G=sp.Matrix([[2,-1,1],[-1,2,7]]); → Koeffizienten vor den Variablen
und auch rechte Seite wird eingegeben
# Berechnungen
H=G.reef(); → reduzierte Stufenform (Gauß-Jordan) wird
berechnet
# Ausgabe
dp.display(G,H); → zuerst werden die Koeffizienten des linearen
Gleichungssystem angezeigt, anschliessend
die reduzierte Stufenform und die rechte Spalte
gibt die Lösung an 

<|ref|>text<|/ref|><|det|>[[113, 546, 707, 713]]<|/det|>
Lösung für Aufgabe 5a) (b) und c) analog).
# Initialisieren
import sympy as sp;
import IPython.display as dp;
#Parameter
G=sp.Matrix([[2,-3,1,3],[-1,3,-2,0],[3,-1,5,1]]);
# Berechnungen
H=G.reef();
# Ausgabe
dp.display(G,H);