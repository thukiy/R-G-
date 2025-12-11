<|ref|>sub_title<|/ref|><|det|>[[114, 82, 701, 99]]<|/det|>
4. Eigenwerte und -vektoren mit Python/Numpy bestimmmen 

<|ref|>text<|/ref|><|det|>[[114, 99, 828, 116]]<|/det|>
Berechnen Sie die Eigenwerte und -vektoren aus Aufgabe 3 mit Python/Numpy. 

<|ref|>text<|/ref|><|det|>[[114, 133, 775, 293]]<|/det|>
a)
# Python initialisieren:
import numpy as np;
# Parameter:
A=np.array([[2,0],[0,3]]);
# Berechnungen:
EW,EV=np.linalg.eig(A); # EW=Eigenwert, EV=Eigenvektor
# Ausgabe:
print('Eigenwerte =',EW);
print('Eigenvektoren =',EV); 

<|ref|>text<|/ref|><|det|>[[114, 310, 240, 328]]<|/det|>
b) – f) analog 

<|ref|>sub_title<|/ref|><|det|>[[114, 343, 701, 360]]<|/det|>
5. Eigenwerte und -vektoren mit Python/Sympy bestimmmen 

<|ref|>text<|/ref|><|det|>[[114, 360, 825, 377]]<|/det|>
Berechnen Sie die Eigenwerte und -vektoren aus Aufgabe 2 mit Python/Sympy. 

<|ref|>text<|/ref|><|det|>[[114, 394, 450, 700]]<|/det|>
a)
# Python initialisieren:
import IPython.display as dp;
import sympy as sp;
# Python konfigurieren:
sp.init_printing(),
# Parameter:
A=sp.Matrix([[2,0],[0,3]]);
# Berechnungen:
[EV,EW]=A.diagonalize(); # EV=Eigenvektoren in Matrixform; EW (Eigenwerte)=Einträge in Hauptdiagonale
ew=A.eigenvals(); # Eigenwert und dessen Multiplizität
ev=A.eigenvects(); #Eigenwert, Multiplizität und zugehöriger Eigenvektor
# Ausgabe:
dp.display(EV);
dp.display(EW);
dp.display(ew);
dp.display(ev); 

<|ref|>text<|/ref|><|det|>[[114, 717, 240, 735]]<|/det|>
b) – f) analog 

<|ref|>sub_title<|/ref|><|det|>[[114, 750, 661, 766]]<|/det|>
6. Eigenwerte/-vektoren zu quadrirtier/invertierter Matrix 

<|ref|>text<|/ref|><|det|>[[114, 767, 685, 784]]<|/det|>
Gegeben sei ein Eigenvektor \(\vec{v}\) zum Eigenwert \(\lambda\) einer Matrix A. 

<|ref|>text<|/ref|><|det|>[[114, 784, 755, 801]]<|/det|>
a) Ist \(\vec{v}\) auch Eigenvektor von A²? Und falls ja, zu welchem Eigenwert? 

<|ref|>text<|/ref|><|det|>[[114, 801, 868, 835]]<|/det|>
b) Wenn A zudem invertierbar sei, ist dann \(\vec{v}\) auch ein Eigenvektor zu A⁻¹? Und falls ja, zu welchem Eigenwert?