<|ref|>sub_title<|/ref|><|det|>[[114, 81, 770, 135]]<|/det|>
4. Linearkombinationen von Vektoren mit Python/Numpy berechnen
Berechnen Sie die Linearkombinationen von Vektoren aus Aufgabe 3 mit
Python/Numpy. 

<|ref|>text<|/ref|><|det|>[[114, 148, 405, 475]]<|/det|>
# Python initialisieren:
import numpy as np;
# Parameter:
u=np.array([2,-1]);
v=np.array([-3,3]);
w=np.array([1,1/2]);
# Berechnungen:
a=u+v;
b=4*w;
c=u-1/3*v;
d= 2*u-2*w;
e=2*u+v+u;
f=2*(v+3*w);
# Ausgabe:
print('a=',a);
print('b=',b);
print('c=',c);
print('d=',d);
print('e=',e);
print('f=',f); 

<|ref|>sub_title<|/ref|><|det|>[[114, 488, 770, 541]]<|/det|>
5. Linearkombinationen von Vektoren mit Python/Sympy berechnen
Berechnen Sie die Linearkombinationen von Vektoren aus Aufgabe
Python/Sympy. 

<|ref|>text<|/ref|><|det|>[[114, 555, 469, 912]]<|/det|>
# Python initialisieren:
import sympy as sp;
import IPython.display as dp;
# Parameter:
u=sp.Matrix([[2],[-1]]);
v=sp.Matrix([[3],[3]]);
w=sp.Matrix([[1],[1/2]]);
sp.init_printing();
# Berechnungen:
a=u+v
b=4*w;
c=u-1/3*v;
d= 2*u - 2*w;
e=2*u+v+u;
f=2*(v+3*w);

# Ausgabe:
dp.display(a);
dp.display(b);
dp.display(c);
dp.display(d);
dp.display(e);
dp.display(f);