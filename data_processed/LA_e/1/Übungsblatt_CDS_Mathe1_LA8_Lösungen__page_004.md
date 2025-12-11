<|ref|>text<|/ref|><|det|>[[115, 81, 262, 98]]<|/det|>
sp=v.dot(w); 

<|ref|>text<|/ref|><|det|>[[115, 98, 245, 114]]<|/det|>
# Ausgabe: 

<|ref|>text<|/ref|><|det|>[[115, 114, 300, 131]]<|/det|>
dp.display(sp); 

<|ref|>text<|/ref|><|det|>[[115, 146, 377, 164]]<|/det|>
b) - f) analog zu Aufgabe a). 

<|ref|>text<|/ref|><|det|>[[115, 180, 145, 197]]<|/det|>
g) 

<|ref|>text<|/ref|><|det|>[[115, 196, 408, 213]]<|/det|>
# Python initialisieren: 

<|ref|>text<|/ref|><|det|>[[115, 213, 350, 229]]<|/det|>
import sympy as sp; 

<|ref|>text<|/ref|><|det|>[[115, 229, 468, 245]]<|/det|>
import IPython.display as dp; 

<|ref|>text<|/ref|><|det|>[[115, 245, 265, 261]]<|/det|>
# Parameter: 

<|ref|>text<|/ref|><|det|>[[115, 261, 344, 278]]<|/det|>
sp.init_printing(); 

<|ref|>text<|/ref|><|det|>[[115, 278, 406, 294]]<|/det|>
phi = sp.symbols('phi'); 

<|ref|>text<|/ref|><|det|>[[115, 294, 610, 310]]<|/det|>
v=sp.Matrix([sp.cos(phi),sp.sin(phi),1]); 

<|ref|>text<|/ref|><|det|>[[115, 310, 622, 326]]<|/det|>
w=sp.Matrix([sp.cos(phi),sp.sin(phi),-1]); 

<|ref|>text<|/ref|><|det|>[[115, 326, 310, 342]]<|/det|>
# Berechnungen: 

<|ref|>text<|/ref|><|det|>[[115, 342, 664, 359]]<|/det|>
Skalar=sp.trigsimp(v.dot(w)); # Vereinfachung 

<|ref|>text<|/ref|><|det|>[[115, 359, 448, 374]]<|/det|>
trigonometricischer Ausdrücke 

<|ref|>text<|/ref|><|det|>[[115, 374, 245, 390]]<|/det|>
# Ausgabe: 

<|ref|>text<|/ref|><|det|>[[115, 390, 350, 407]]<|/det|>
dp.display(Skalar); 

<|ref|>text<|/ref|><|det|>[[115, 423, 145, 440]]<|/det|>
h) 

<|ref|>text<|/ref|><|det|>[[115, 440, 234, 457]]<|/det|>
analog zu g) 

<|ref|>text<|/ref|><|det|>[[115, 472, 135, 489]]<|/det|>
i) 

<|ref|>text<|/ref|><|det|>[[115, 488, 408, 504]]<|/det|>
# Python initialisieren: 

<|ref|>text<|/ref|><|det|>[[115, 504, 350, 520]]<|/det|>
import sympy as sp; 

<|ref|>text<|/ref|><|det|>[[115, 520, 468, 536]]<|/det|>
import IPython.display as dp; 

<|ref|>text<|/ref|><|det|>[[115, 536, 265, 552]]<|/det|>
# Parameter: 

<|ref|>text<|/ref|><|det|>[[115, 552, 344, 569]]<|/det|>
sp.init_printing(); 

<|ref|>text<|/ref|><|det|>[[115, 569, 350, 585]]<|/det|>
x = sp.symbols('x'); 

<|ref|>text<|/ref|><|det|>[[115, 585, 450, 601]]<|/det|>
v=sp.Matrix([2**x,3**x,1]); 

<|ref|>text<|/ref|><|det|>[[115, 601, 551, 617]]<|/det|>
w=sp.Matrix([2**(-x),3**x,-(9**x)]); 

<|ref|>text<|/ref|><|det|>[[115, 617, 310, 633]]<|/det|>
# Berechnungen: 

<|ref|>text<|/ref|><|det|>[[115, 633, 468, 649]]<|/det|>
Skalar=sp.simplify(v.dot(w)); 

<|ref|>text<|/ref|><|det|>[[115, 649, 245, 665]]<|/det|>
# Ausgabe: 

<|ref|>text<|/ref|><|det|>[[115, 665, 350, 682]]<|/det|>
dp.display(Skalar); 

<|ref|>sub_title<|/ref|><|det|>[[115, 698, 475, 716]]<|/det|>
5. Eigenschaften des Skalarprodukts 

<|ref|>text<|/ref|><|det|>[[115, 716, 802, 749]]<|/det|>
Beweisen Sie die folgenden Eigenschaften des Skalarprodukts für \(a \in \mathbb{R}\) und beliebige Vektoren \(\vec{u}, \vec{v}, \vec{w} \in \mathbb{R}^n\) mit \(n \in \mathbb{N}\). 

<|ref|>text<|/ref|><|det|>[[115, 748, 316, 766]]<|/det|>
a) \(\langle a \cdot \vec{v}, \vec{w} \rangle = a \cdot \langle \vec{v}, \vec{w} \rangle\) 

<|ref|>text<|/ref|><|det|>[[115, 765, 268, 783]]<|/det|>
b) \(\langle \vec{u} + \vec{v}, \vec{w} \rangle = \langle \vec{u}, \vec{w} \rangle + \langle \vec{v}, \vec{w} \rangle\) 

<|ref|>text<|/ref|><|det|>[[0, 0, 0, 0]]<|/det|>
c) \(\langle \vec{w}, \vec{v} \rangle = \langle \vec{v}, \vec{w} \rangle\) 

<|ref|>text<|/ref|><|det|>[[500, 765, 608, 783]]<|/det|>
d) \(\langle \vec{v}, \vec{v} \rangle \geq 0\) 

<|ref|>text<|/ref|><|det|>[[115, 783, 315, 800]]<|/det|>
e) \(\langle \vec{v}, \vec{v} \rangle = 0 \iff \vec{v} = 0\) 

<|ref|>text<|/ref|><|det|>[[500, 783, 860, 800]]<|/det|>
f) \(\langle \vec{v} + \vec{w}, \vec{v} + \vec{w} \rangle = |\vec{v}|^2 + |\vec{w}|^2 + 2 \cdot \langle \vec{v}, \vec{w} \rangle\) 

<|ref|>text<|/ref|>