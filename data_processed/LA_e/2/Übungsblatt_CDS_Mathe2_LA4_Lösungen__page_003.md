<|ref|>sub_title<|/ref|><|det|>[[115, 81, 520, 100]]<|/det|>
3. Matrizen berechnen mit Python/Numpy 

<|ref|>text<|/ref|><|det|>[[115, 98, 737, 118]]<|/det|>
Berechnen Sie die Matrizen aus Aufgabe 2a) – d) mit Python/Numpy. 

<|ref|>text<|/ref|><|det|>[[115, 131, 325, 149]]<|/det|>
# Initialisieren: 

<|ref|>text<|/ref|><|det|>[[115, 149, 350, 166]]<|/det|>
import numpy as np; 

<|ref|>text<|/ref|><|det|>[[115, 165, 267, 182]]<|/det|>
# Parameter: 

<|ref|>text<|/ref|><|det|>[[115, 181, 504, 199]]<|/det|>
A=np.array([[1,3,-1],[4,-2,8]]); 

<|ref|>text<|/ref|><|det|>[[115, 197, 504, 215]]<|/det|>
B=np.array([[−3,9,3],[−6,6,3]]); 

<|ref|>text<|/ref|><|det|>[[115, 214, 304, 231]]<|/det|>
# Berechnungen: 

<|ref|>text<|/ref|><|det|>[[115, 230, 200, 247]]<|/det|>
C=A+B; 

<|ref|>text<|/ref|><|det|>[[115, 246, 206, 263]]<|/det|>
E=-2*A; 

<|ref|>text<|/ref|><|det|>[[115, 262, 240, 279]]<|/det|>
F=(1/3)*B; 

<|ref|>text<|/ref|><|det|>[[115, 278, 220, 295]]<|/det|>
G=2*B-A; 

<|ref|>text<|/ref|><|det|>[[115, 294, 241, 311]]<|/det|>
# Ausgabe: 

<|ref|>text<|/ref|><|det|>[[115, 310, 290, 327]]<|/det|>
print('C=',C); 

<|ref|>text<|/ref|><|det|>[[115, 326, 288, 343]]<|/det|>
print('E=',E); 

<|ref|>text<|/ref|><|det|>[[115, 342, 288, 359]]<|/det|>
print('F=',F); 

<|ref|>text<|/ref|><|det|>[[115, 358, 288, 375]]<|/det|>
print('G=',G); 

<|ref|>sub_title<|/ref|><|det|>[[115, 390, 366, 409]]<|/det|>
4. Produkte von Matrizen 

<|ref|>text<|/ref|><|det|>[[115, 407, 374, 425]]<|/det|>
Gegeben seien die Matrizen 

<|ref|>equation<|/ref|><|det|>[[115, 421, 405, 458]]<|/det|>
\[A = \begin{pmatrix} 2 & 4 \\ 3 & 1 \end{pmatrix} \text{ und } B = \begin{pmatrix} -1 & 4 \\ 2 & -3 \end{pmatrix}.\]

<|ref|>text<|/ref|><|det|>[[115, 460, 590, 479]]<|/det|>
Berechnen Sie die jeweiligen Produkte der Matrizen. 

<|ref|>equation<|/ref|><|det|>[[115, 477, 794, 496]]<|/det|>
a) \(C = A \cdot B\) b) \(C = B \cdot A\) c) \(C = A \cdot E\) d) \(C = E \cdot A\)

<|ref|>text<|/ref|><|det|>[[115, 510, 150, 528]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[123, 530, 880, 641]]<|/det|>
\[ \underline{C} = A \cdot B = \begin{bmatrix} 2 \cdot (-1) + 4 \cdot 2 & 2 \cdot 4 + 4 \cdot (-3) \\ 3 \cdot (-1) + 1 \cdot 2 & 3 \cdot 4 + 1 \cdot (-3) \end{bmatrix} = \begin{bmatrix} -2 + 8 & 8 - 12 \\ -3 + 2 & 12 - 3 \end{bmatrix} \\ = \begin{bmatrix} 6 & -4 \\ -1 & 9 \end{bmatrix}. \]

<|ref|>text<|/ref|><|det|>[[115, 645, 150, 663]]<|/det|>
b) 

<|ref|>equation<|/ref|><|det|>[[119, 666, 880, 715]]<|/det|>
\[ \underline{C} = B \cdot A = \begin{bmatrix} (-1) \cdot 2 + 4 \cdot 3 & (-1) \cdot 4 + 4 \cdot 1 \\ 2 \cdot 2 + (-3) \cdot 3 & 2 \cdot 4 + (-3) \cdot 1 \end{bmatrix} = \begin{bmatrix} -2 + 12 & -4 + 4 \\ 4 - 9 & 8 - 3 \end{bmatrix} \\ = \begin{bmatrix} 10 & 0 \\ -5 & 5 \end{bmatrix} \neq A \cdot B. \]

<|ref|>text<|/ref|><|det|>[[115, 785, 150, 803]]<|/det|>
c) 

<|ref|>equation<|/ref|><|det|>[[123, 807, 880, 856]]<|/det|>
\[ \underline{C} = A \cdot \mathbb{1} = \begin{bmatrix} 2 \cdot 1 + 4 \cdot 0 & 2 \cdot 0 + 4 \cdot 1 \\ 3 \cdot 1 + 1 \cdot 0 & 3 \cdot 0 + 1 \cdot 1 \end{bmatrix} = \begin{bmatrix} 2 + 0 & 0 + 4 \\ 3 + 0 & 0 + 1 \end{bmatrix} = \begin{bmatrix} 2 & 4 \\ 3 & 1 \end{bmatrix} = \underline{A}. \]

<|ref|>text<|/ref|><|det|>[[115, 852, 150, 870]]<|/det|>
d) 

<|ref|>equation<|/ref|><|det|>[[123, 871, 880, 920]]<|/det|>
\[ \underline{C} = \mathbb{1} \cdot A = \begin{bmatrix} 1 \cdot 2 + 0 \cdot 3 & 1 \cdot 4 + 0 \cdot 1 \\ 0 \cdot 2 + 1 \cdot 3 & 0 \cdot 4 + 1 \cdot 1 \end{bmatrix} = \begin{bmatrix} 2 + \underline{0} & 4 + \underline{0} \\ 0 + \underline{3} & 0 + \underline{1} \end{bmatrix} = \begin{bmatrix} 2 & 4 \\ 3 & 0 \end{bmatrix} = \underline{A}. \]