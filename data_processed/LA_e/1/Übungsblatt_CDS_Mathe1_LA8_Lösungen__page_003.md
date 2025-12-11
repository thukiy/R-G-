<|ref|>text<|/ref|><|det|>[[114, 83, 145, 101]]<|/det|>
g) 

<|ref|>equation<|/ref|><|det|>[[124, 100, 787, 170]]<|/det|>
\[ \left\langle \begin{bmatrix} \cos(\varphi) \\ \sin(\varphi) \\ 1 \end{bmatrix}, \begin{bmatrix} \cos(\varphi) \\ \sin(\varphi) \\ -1 \end{bmatrix} \right\rangle = \cos(\varphi) \cdot \cos(\varphi) + \sin(\varphi) \cdot \sin(\varphi) + 1 \cdot (-1) \]

<|ref|>equation<|/ref|><|det|>[[380, 185, 720, 207]]<|/det|>
\[ = \cos^2(\varphi) + \sin^2(\varphi) - 1 = 1 - 1 = \underline{0}. \]

<|ref|>text<|/ref|><|det|>[[114, 207, 145, 225]]<|/det|>
h) 

<|ref|>equation<|/ref|><|det|>[[124, 223, 808, 292]]<|/det|>
\[ \left\langle \begin{bmatrix} \cos(\varphi) \\ \sin( \varphi) \\ 1 \end{bmatrix}, \begin{bmatrix} -\sin(\varphi) \\ \cos(\varphi) \\ 1 \end{bmatrix} \right\rangle = \cos(\varphi) \cdot \left( -\sin(\varphi) \right) + \sin(\varphi) \cdot \cos(\varphi) + 1 \cdot 1 \]

<|ref|>equation<|/ref|><|det|>[[395, 308, 880, 330]]<|/det|>
\[ = -\cos(\varphi) \cdot \sin(\varphi) + \cos(\varphi) \cdot \sin(\varphi) + 1 = 0 + 1 = \underline{1}. \]

<|ref|>text<|/ref|><|det|>[[114, 330, 140, 348]]<|/det|>
i) 

<|ref|>equation<|/ref|><|det|>[[124, 346, 875, 420]]<|/det|>
\[ \left\langle \begin{bmatrix} 2^x \\ 3^x \\ 1 \end{bmatrix}, \begin{bmatrix} 2^{-x} \\ 3^x \\ -9^x \end{bmatrix} \right\rangle = 2^x \cdot 2^{-x} + 3^x \cdot 3^x - 1 \cdot 9^x = 2^{x-x} + 3^{x+x} - 9^x = 2^0 + 3^{2x} - (3^2)^x \]

<|ref|>equation<|/ref|><|det|>[[315, 427, 565, 449]]<|/det|>
\[ = 1 + 3^{2x} - 3^{2x} = 1 + 0 = \underline{1}. \]

<|ref|>text<|/ref|><|det|>[[114, 464, 570, 483]]<|/det|>
3. Skalarprodukt mit Python/Numpy berechnen 

<|ref|>text<|/ref|><|det|>[[114, 481, 787, 500]]<|/det|>
Berechnen Sie die Skalarprodukte aus Aufgabe 2a) – f) mit Python/Numpy. 

<|ref|>text<|/ref|><|det|>[[114, 515, 145, 532]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[114, 530, 408, 548]]<|/det|>
# Python initialisieren: 

<|ref|>text<|/ref|><|det|>[[114, 547, 348, 565]]<|/det|>
import numpy as np; 

<|ref|>text<|/ref|><|det|>[[114, 564, 260, 580]]<|/det|>
# Parameter: 

<|ref|>text<|/ref|><|det|>[[114, 579, 333, 597]]<|/det|>
v=np.array([1,2]); 

<|ref|>text<|/ref|><|det|>[[114, 596, 333, 613]]<|/det|>
w=np.array([3,4]); 

<|ref|>text<|/ref|><|det|>[[114, 612, 301, 629]]<|/det|>
# Berechnungen: 

<|ref|>text<|/ref|><|det|>[[114, 628, 298, 645]]<|/det|>
sp=np.dot(v,w); 

<|ref|>text<|/ref|><|det|>[[114, 644, 240, 661]]<|/det|>
# Ausgabe: 

<|ref|>text<|/ref|><|det|>[[114, 660, 469, 678]]<|/det|>
print('Skalarprodukt = ',sp); 

<|ref|>text<|/ref|><|det|>[[114, 692, 375, 711]]<|/det|>
b) – f) analog zu Aufgabe a). 

<|ref|>text<|/ref|><|det|>[[114, 725, 567, 744]]<|/det|>
4. Skalarprodukt mit Python/Sympy berechnen 

<|ref|>text<|/ref|><|det|>[[114, 742, 731, 761]]<|/det|>
Berechnen Sie die Skalarprodukte aus Aufgabe 2 mit Python/Sympy. 

<|ref|>text<|/ref|><|det|>[[114, 776, 145, 794]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[114, 792, 408, 810]]<|/det|>
# Python initialisieren: 

<|ref|>text<|/ref|><|det|>[[114, 809, 348, 826]]<|/det|>
import sympy as sp; 

<|ref|>text<|/ref|><|det|>[[114, 825, 469, 842]]<|/det|>
import IPython.display as dp; 

<|ref|>text<|/ref|><|det|>[[114, 841, 260, 858]]<|/det|>
# Parameter: 

<|ref|>text<|/ref|><|det|>[[114, 857, 345, 875]]<|/det|>
sp.init_printing(); 

<|ref|>text<|/ref|><|det|>[[114, 874, 345, 891]]<|/det|>
v=sp.Matrix([1,2]); 

<|ref|>text<|/ref|><|det|>[[114, 890, 345, 907]]<|/det|>
w=sp.Matrix([3,4]); 

<|ref|>text<|/ref|><|det|>[[114, 906, 300, 923]]<|/det|>
# Berechnungen: