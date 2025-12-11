<|ref|>text<|/ref|><|det|>[[114, 81, 144, 100]]<|/det|>
h) 

<|ref|>equation<|/ref|><|det|>[[114, 98, 610, 170]]<|/det|>
\[ \mathbf{u} \cdot \mathbf{v}^T = \begin{bmatrix} 0 \\ 2 \\ -4 \end{bmatrix} \cdot \begin{bmatrix} 1 & 3 & -3 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 0 \\ 2 & 6 & -6 \\ -4 & -12 & 12 \end{bmatrix}. \]

<|ref|>text<|/ref|><|det|>[[114, 173, 137, 192]]<|/det|>
i) 

<|ref|>equation<|/ref|><|det|>[[114, 190, 500, 253]]<|/det|>
\[ B^T \cdot \mathbf{v} = \begin{bmatrix} 3 & 1 & 5 \\ 4 & 2 & 6 \end{bmatrix} \cdot \begin{bmatrix} 1 \\ 3 \\ -3 \end{bmatrix} = \begin{bmatrix} -9 \\ -8 \end{bmatrix}. \]

<|ref|>text<|/ref|><|det|>[[114, 256, 137, 275]]<|/det|>
j) 

<|ref|>equation<|/ref|><|det|>[[114, 273, 677, 341]]<|/det|>
\[ \mathbf{v}^T \cdot B = \begin{bmatrix} 1 & 3 & -3 \end{bmatrix} \cdot \begin{bmatrix} 3 & 4 \\ 1 & 2 \\ 5 & 6 \end{bmatrix} = \begin{bmatrix} -9 & -8 \end{bmatrix} = (B^T \cdot \mathbf{v})^T. \]

<|ref|>sub_title<|/ref|><|det|>[[114, 357, 518, 375]]<|/det|>
## 7. Matrizen berechnen mit Python/Numpy 

<|ref|>text<|/ref|><|det|>[[114, 373, 678, 392]]<|/det|>
Berechnen Sie die Matrizen aus Aufgabe 7 mit Python/Numpy. 

<|ref|>text<|/ref|><|det|>[[114, 405, 320, 422]]<|/det|>
# Initialisieren: 

<|ref|>text<|/ref|><|det|>[[114, 422, 348, 440]]<|/det|>
import numpy as np; 

<|ref|>text<|/ref|><|det|>[[114, 439, 263, 456]]<|/det|>
# Parameter: 

<|ref|>text<|/ref|><|det|>[[114, 455, 611, 472]]<|/det|>
A=np.array([[4,-3,2],[6,2,5],[-1,-2,3]]); 

<|ref|>text<|/ref|><|det|>[[114, 470, 501, 488]]<|/det|>
B=np.array([[3,4],[1,2],[5,6]]); 

<|ref|>text<|/ref|><|det|>[[114, 487, 444, 504]]<|/det|>
u=np.array([[0],[2],[-4]]); 

<|ref|>text<|/ref|><|det|>[[114, 503, 430, 520]]<|/det|>
v=np.array([[1],[3],[-3]]); 

<|ref|>text<|/ref|><|det|>[[114, 519, 300, 536]]<|/det|>
# Berechnungen: 

<|ref|>text<|/ref|><|det|>[[114, 536, 192, 552]]<|/det|>
C=A@B; 

<|ref|>text<|/ref|><|det|>[[114, 551, 410, 568]]<|/det|>
# D=B@A; nicht definiert 

<|ref|>text<|/ref|><|det|>[[114, 568, 192, 584]]<|/det|>
E=A@u; 

<|ref|>text<|/ref|><|det|>[[114, 584, 192, 600]]<|/det|>
F=A@A; 

<|ref|>text<|/ref|><|det|>[[114, 600, 410, 617]]<|/det|>
# G=B@B; nicht definiert 

<|ref|>text<|/ref|><|det|>[[114, 616, 212, 632]]<|/det|>
H=v.T@u; 

<|ref|>text<|/ref|><|det|>[[114, 632, 410, 649]]<|/det|>
# J=v@u; nicht definiert 

<|ref|>text<|/ref|><|det|>[[114, 648, 216, 664]]<|/det|>
K=u@v.T; 

<|ref|>text<|/ref|><|det|>[[114, 664, 216, 680]]<|/det|>
L=B.T@v; 

<|ref|>text<|/ref|><|det|>[[114, 680, 216, 696]]<|/det|>
M=v.T@B; 

<|ref|>text<|/ref|><|det|>[[114, 696, 239, 713]]<|/det|>
# Ausgabe: 

<|ref|>text<|/ref|><|det|>[[114, 712, 300, 729]]<|/det|>
print('C=',C); 

<|ref|>text<|/ref|><|det|>[[114, 728, 575, 746]]<|/det|>
print('D kann nicht gebildet werden'); 

<|ref|>text<|/ref|><|det|>[[114, 745, 300, 762]]<|/det|>
print('E=',E); 

<|ref|>text<|/ref|><|det|>[[114, 761, 300, 778]]<|/det|>
print('F=',F); 

<|ref|>text<|/ref|><|det|>[[114, 777, 586, 795]]<|/det|>
print('G kann nicht gebildet werden'); 

<|ref|>text<|/ref|><|det|>[[114, 794, 300, 811]]<|/det|>
print('H=',H); 

<|ref|>text<|/ref|><|det|>[[114, 810, 586, 828]]<|/det|>
print('J kann nicht gebildet werden'); 

<|ref|>text<|/ref|><|det|>[[114, 827, 300, 844]]<|/det|>
print('K=',K); 

<|ref|>text<|/ref|><|det|>[[114, 843, 300, 860]]<|/det|>
print('L=',L); 

<|ref|>text<|/ref|><|det|>[[114, 859, 300, 876]]<|/det|>
print('M=',M);