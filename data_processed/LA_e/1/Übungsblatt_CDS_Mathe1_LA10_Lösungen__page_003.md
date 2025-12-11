<|ref|>equation<|/ref|><|det|>[[115, 83, 499, 163]]<|/det|>
\[
\begin{array}{c|cc}
v_{\perp} = v - v_{\parallel} = & 1 & -0.5 \\
2 & 0.5 & 1.5 \\
3 & -0.5 & 3.5 \\
4 & 0.5 & 3.5
\end{array}
\]

<|ref|>sub_title<|/ref|><|det|>[[115, 184, 666, 203]]<|/det|>
3. Orthogonalprojektionen mit Python/Numpy berechnen 

<|ref|>text<|/ref|><|det|>[[115, 201, 808, 220]]<|/det|>
Berechnen Sie die Orthogonalprojektionen aus Aufgabe 2 mit Python/Numpy. 

<|ref|>text<|/ref|><|det|>[[115, 235, 144, 252]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[115, 250, 410, 267]]<|/det|>
# Python initialisieren: 

<|ref|>text<|/ref|><|det|>[[115, 267, 348, 284]]<|/det|>
import numpy as np; 

<|ref|>text<|/ref|><|det|>[[115, 283, 264, 299]]<|/det|>
# Parameter: 

<|ref|>text<|/ref|><|det|>[[115, 299, 562, 316]]<|/det|>
v=np.array([2,3]); w=np.array([6,0]); 

<|ref|>text<|/ref|><|det|>[[115, 315, 280, 331]]<|/det|>
# Funktionen: 

<|ref|>text<|/ref|><|det|>[[115, 330, 562, 348]]<|/det|>
v_parallel=np.dot(v,w)/np.dot(w,w)*w; 

<|ref|>text<|/ref|><|det|>[[115, 347, 303, 364]]<|/det|>
# Berechnungen: 

<|ref|>text<|/ref|><|det|>[[115, 363, 420, 380]]<|/det|>
v_senkrecht=v-v_parallel; 

<|ref|>text<|/ref|><|det|>[[115, 380, 240, 396]]<|/det|>
# Ausgabe: 

<|ref|>text<|/ref|><|det|>[[115, 395, 540, 412]]<|/det|>
print('v_parallel = ', v_parallel); 

<|ref|>text<|/ref|><|det|>[[115, 411, 562, 428]]<|/det|>
print('v_senkrecht = ', v_senkrecht); 

<|ref|>text<|/ref|><|det|>[[115, 444, 337, 462]]<|/det|>
Aufgaben b) - f) analog. 

<|ref|>sub_title<|/ref|><|det|>[[115, 477, 660, 495]]<|/det|>
4. Orthogonalprojektionen mit Python/Sympy berechnen 

<|ref|>text<|/ref|><|det|>[[115, 494, 805, 512]]<|/det|>
Berechnen Sie die Orthogonalprojektionen aus Aufgabe 2 mit PythoN/Sympy. 

<|ref|>text<|/ref|><|det|>[[115, 528, 144, 545]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[115, 543, 312, 560]]<|/det|>
# Initialisieren 

<|ref|>text<|/ref|><|det|>[[115, 560, 348, 577]]<|/det|>
import sympy as sp; 

<|ref|>text<|/ref|><|det|>[[115, 576, 469, 593]]<|/det|>
import IPython.display as dp; 

<|ref|>text<|/ref|><|det|>[[115, 592, 344, 609]]<|/det|>
sp.init_printing(); 

<|ref|>text<|/ref|><|det|>[[115, 608, 255, 625]]<|/det|>
# Parameter 

<|ref|>text<|/ref|><|det|>[[115, 624, 586, 641]]<|/det|>
v=sp.Matrix([2,3]); w=sp.Matrix([6,0]); 

<|ref|>text<|/ref|><|det|>[[115, 640, 293, 657]]<|/det|>
# Berechnungen 

<|ref|>text<|/ref|><|det|>[[115, 656, 515, 673]]<|/det|>
v_parallel=(v.dot(w)/w.dot(w))*w; 

<|ref|>text<|/ref|><|det|>[[115, 672, 410, 689]]<|/det|>
v_senkrecht=v-v_parallel 

<|ref|>text<|/ref|><|det|>[[115, 688, 231, 705]]<|/det|>
# Ausgabe 

<|ref|>text<|/ref|><|det|>[[115, 704, 395, 721]]<|/det|>
dp.display(v_parallel); 

<|ref|>text<|/ref|><|det|>[[115, 720, 408, 737]]<|/det|>
dp.display(v_senkrecht); 

<|ref|>text<|/ref|><|det|>[[115, 752, 337, 771]]<|/det|>
Aufgaben b) - f) analog.