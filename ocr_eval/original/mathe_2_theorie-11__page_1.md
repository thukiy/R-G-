<|ref|>image<|/ref|><|det|>[[90, 12, 833, 220]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[70, 226, 900, 255]]<|/det|>
→ Flächen des Breite h unter der Kurve f(x) werden durch Trapeze 
angenähert 

<|ref|>equation<|/ref|><|det|>[[120, 263, 900, 420]]<|/det|>
\[
\begin{align*}
y_0 \quad A_1 \quad y_1 \quad A_1 &= h \cdot y_1 + \frac{1}{2} \cdot h \cdot (y_0 - y_1) = h \cdot y_1 + \frac{1}{2} h \cdot y_0 - \frac{1}{2} h \cdot y_1 \\
&= \frac{1}{2} h \cdot (y_1 + y_0) \\
&\to A_n = \frac{1}{2} h \cdot (y_{n-1} + y_n)
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[108, 437, 900, 710]]<|/det|>
\[
\begin{align*}
a \int f(x) \, dx &\approx A_1 + A_2 + \ldots + A_n \\
&= \frac{1}{2} h (y_0 + y_1) + \frac{1}{2} h (y_1 + y_2) + \ldots + \frac{1}{2} h (y_{n-1} + y_n) \\
&= \frac{1}{2} h (y_0 + y_1 + y_1 + y_2 + y_2 + \ldots + y_{n-1} + y_{n-1} + y_n) \\
&= \frac{1}{2} h \left( y_0 + 2y_1 + 2y_2 + \ldots + 2y_{n-1} + y_n \right) \\
&= \frac{1}{2} h \left( y_0 + y_n + 2 \cdot (y_1 + y_2 + \ldots + y_{n-1}) \right) \\
&= \frac{1}{2} h \left( y_0 \right) + h \cdot \Sigma_1 \\
&= \frac{1}{2} h \left( \Sigma_1 + h \cdot \Sigma_2 \right)
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[15, 728, 620, 760]]<|/det|>
\[
Bsp: \quad \int_0^1 e^{-x^2} \, dx \quad n = 5 \quad \to \quad h = 0,2
\]

<|ref|>equation<|/ref|><|det|>[[156, 770, 911, 802]]<|/det|>
\[
\int_0^1 e^{-x^2} \, dx \approx \frac{1}{2} h \Sigma_1 + h \Sigma_2 = 0,7444
\]

<|ref|>table<|/ref|><|det|>[[156, 810, 320, 970]]<|/det|>
<table><tr><td>\(x_n\)</td><td>\(y_n\)</td></tr><tr><td>0</td><td>1</td></tr><tr><td>0,2</td><td>0,9608</td></tr><tr><td>0,4</td><td>0,8521</td></tr><tr><td>0,6</td><td>0,6977</td></tr><tr><td>0,8</td><td>0,5273</td></tr><tr><td>1</td><td>0,3679</td></tr></table>

<|ref|>equation<|/ref|><|det|>[[450, 800, 911, 828]]<|/det|>
\[
\int_0^1 e^{-x^2} \, dx \sim \frac{1}{2} h \Sigma_1 + h \Sigma_2 = \quad 0,7444
\]

<|ref|>equation<|/ref|><|det|>[[450, 835, 710, 857]]<|/det|>
\[
\text{exakter Welt : } 0,7468
\]

<|ref|>text<|/ref|><|det|>[[450, 870, 680, 888]]<|/det|>
8 # Initialisieren 

<|ref|>text<|/ref|><|det|>[[450, 886, 737, 904]]<|/det|>
9 import numpy as np; 

<|ref|>text<|/ref|><|det|>[[450, 902, 661, 920]]<|/det|>
10 # Berechnung 

<|ref|>text<|/ref|><|det|>[[450, 918, 740, 936]]<|/det|>
11 x=np.linspace(0,1,5); 

<|ref|>text<|/ref|><|det|>[[450, 934, 821, 952]]<|/det|>
12 I=np.trapz(np.e**(-x**2),x); 

<|ref|>text<|/ref|><|det|>[[450, 950, 625, 968]]<|/det|>
13 # Ausgabe 

<|ref|>text<|/ref|><|det|>[[450, 966, 795, 986]]<|/det|>
14 print("I=",np.round(I,5));