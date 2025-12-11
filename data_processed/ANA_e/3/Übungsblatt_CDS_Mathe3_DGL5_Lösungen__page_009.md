<|ref|>sub_title<|/ref|><|det|>[[115, 83, 141, 100]]<|/det|>
b) 

<|ref|>sub_title<|/ref|><|det|>[[115, 99, 231, 117]]<|/det|>
Aufgabe 6a: 

<|ref|>text<|/ref|><|det|>[[115, 115, 459, 133]]<|/det|>
# Python initialisieren 

<|ref|>text<|/ref|><|det|>[[115, 131, 468, 149]]<|/det|>
import IPython.display as dp; 

<|ref|>text<|/ref|><|det|>[[115, 148, 350, 165]]<|/det|>
import sympy as sp; 

<|ref|>text<|/ref|><|det|>[[115, 164, 390, 181]]<|/det|>
# Python konfigurieren 

<|ref|>text<|/ref|><|det|>[[115, 180, 375, 197]]<|/det|>
# sp.init_printing(); 

<|ref|>text<|/ref|><|det|>[[115, 196, 340, 213]]<|/det|>
x=sp.symbols('x'); 

<|ref|>text<|/ref|><|det|>[[115, 212, 355, 229]]<|/det|>
y=sp.Function('y'); 

<|ref|>text<|/ref|><|det|>[[115, 228, 256, 245]]<|/det|>
# Parameter 

<|ref|>text<|/ref|><|det|>[[115, 244, 590, 262]]<|/det|>
a=1; b=4; c=5; x_0=0; y_0=sp.pi; v_0=0; 

<|ref|>text<|/ref|><|det|>[[115, 261, 293, 278]]<|/det|>
# Berechnungen 

<|ref|>text<|/ref|><|det|>[[115, 277, 612, 294]]<|/det|>
l=a*y(x).diff(x,2)+b*y(x).diff(x)+c*y(x); 

<|ref|>text<|/ref|><|det|>[[115, 293, 181, 309]]<|/det|>
#r=0; 

<|ref|>text<|/ref|><|det|>[[115, 308, 866, 344]]<|/det|>
L=sp.dsolve(l,y(x),ics={y(x_0):y_0,y(x).diff(x).subs(x,x_0):v_0}); 

<|ref|>text<|/ref|><|det|>[[115, 342, 234, 359]]<|/det|>
# Ausgabe 

<|ref|>text<|/ref|><|det|>[[115, 358, 288, 375]]<|/det|>
dp.display(L); 

<|ref|>text<|/ref|><|det|>[[145, 390, 832, 425]]<|/det|>
➔ Aufgaben 6b – d analog, die Parameter a, b, c, x_0, y_0 und v_0 müssen verändert eingegeben werden