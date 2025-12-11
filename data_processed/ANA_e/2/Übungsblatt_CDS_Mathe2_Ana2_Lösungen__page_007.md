<|ref|>text<|/ref|><|det|>[[114, 81, 135, 99]]<|/det|>
f) 

<|ref|>equation<|/ref|><|det|>[[119, 102, 644, 168]]<|/det|>
\[
\begin{align*}
u(x) & := -x^2 \Rightarrow u'(x) = -2x \\
\frac{du}{dx} & = -2x \Leftrightarrow du = -2x dx \Leftrightarrow dx = \frac{du}{-2x} = -\frac{1}{2x} du
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[124, 177, 225, 195]]<|/det|>
und somit 

<|ref|>equation<|/ref|><|det|>[[124, 202, 872, 300]]<|/det|>
\[
\begin{align*}
I &= \int_{0}^{10} 5x e^{-x^2} \, dx = 5 \int_{u(0)}^{u(10)} x e^u \cdot \frac{1}{-2x} \, du = -\frac{5}{2} \int_{0}^{-100} e^u \, du = -\frac{5}{2} \cdot \left[ e^u \right]_{0}^{-100} \\
&= -\frac{5}{2} \cdot \left( e^{-100} - e^0 \right) = \frac{5}{2} \left( 1 - e^{-100} \right).
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[114, 312, 520, 330]]<|/det|>
5. Integrale mit Python/Numpy berechnen 

<|ref|>text<|/ref|><|det|>[[114, 328, 785, 364]]<|/det|>
Berechnen Sie die folgenden bestimmten Integrale mit dem Befehl trapz in Python/Numpy. 

<|ref|>equation<|/ref|><|det|>[[114, 361, 631, 437]]<|/det|>
\[
\begin{align*}
a) \int_{0}^{\pi} \sin x \, dx & \qquad b) \int_{2}^{5} \frac{1+x}{1-x} \, dx \\
c) \int_{-2}^{0} 3^x \, dx & \qquad d) \int_{2}^{100} \frac{\sin x}{1+3x} \, dx \\
e) \int_{0.01}^{1} \log_2 x \, dx & \qquad f) \int_{2}^{3} \log_5 x \, dx
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 453, 145, 470]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[114, 468, 312, 485]]<|/det|>
# Initialisieren 

<|ref|>text<|/ref|><|det|>[[114, 485, 350, 502]]<|/det|>
import numpy as np; 

<|ref|>text<|/ref|><|det|>[[114, 501, 494, 518]]<|/det|>
import matplotlib.pyplot as pl; 

<|ref|>text<|/ref|><|det|>[[114, 517, 255, 533]]<|/det|>
# Parameter 

<|ref|>text<|/ref|><|det|>[[114, 532, 538, 565]]<|/det|>
x_0=0; x_E=np.pi; n=7; N=10; fig=1;
def f(x): y=np.sin(x); return y; 

<|ref|>text<|/ref|><|det|>[[114, 565, 290, 581]]<|/det|>
# Berechnungen 

<|ref|>text<|/ref|><|det|>[[114, 581, 365, 597]]<|/det|>
for k in range (0,n): 

<|ref|>text<|/ref|><|det|>[[162, 597, 526, 613]]<|/det|>
x_data=np.linspace(x_0, x_E, N); 

<|ref|>text<|/ref|><|det|>[[162, 612, 365, 628]]<|/det|>
f_data=f(x_data); 

<|ref|>text<|/ref|><|det|>[[162, 628, 323, 644]]<|/det|>
# Integration 

<|ref|>text<|/ref|><|det|>[[162, 644, 480, 660]]<|/det|>
I=np.trapz(f_data, x_data); 

<|ref|>text<|/ref|><|det|>[[162, 660, 336, 676]]<|/det|>
print('I=',I); 

<|ref|>text<|/ref|><|det|>[[162, 676, 240, 691]]<|/det|>
N=2*N; 

<|ref|>text<|/ref|><|det|>[[114, 692, 234, 708]]<|/det|>
# Ausgabe 

<|ref|>text<|/ref|><|det|>[[114, 708, 504, 725]]<|/det|>
print('Integral: I=',f"{I:.3}"); 

<|ref|>text<|/ref|><|det|>[[114, 725, 195, 740]]<|/det|>
# Plot 

<|ref|>text<|/ref|><|det|>[[114, 740, 338, 757]]<|/det|>
fh=pl.figure(fig); 

<|ref|>text<|/ref|><|det|>[[114, 757, 400, 773]]<|/det|>
pl.plot(x_data,f_data); 

<|ref|>text<|/ref|><|det|>[[114, 773, 499, 789]]<|/det|>
pl.xlabel('x'); pl.ylabel('y'); 

<|ref|>text<|/ref|><|det|>[[114, 789, 504, 806]]<|/det|>
pl.grid('on'); pl.axis('image'); 

<|ref|>text<|/ref|><|det|>[[114, 823, 433, 841]]<|/det|>
Es ergibt sich als Integralwert I = 2. 

<|ref|>text<|/ref|><|det|>[[114, 841, 177, 857]]<|/det|>
b) - f) 

<|ref|>text<|/ref|><|det|>[[114, 856, 875, 890]]<|/det|>
Code analog zu a) ausführen, jedoch Funktion und Start- und Endwert anpassen und Intervallunterteilung „ausprobieren“. 

<|ref|>table<|/ref|><|det|>[[114, 888, 880, 927]]<|/det|>
<table><tr><td>b)</td><td>c)</td><td>d)</td><td>e)</td><td>f)</td></tr><tr><td>I = -5,77</td><td>I = 0,809</td><td>I = -0,0171</td><td>I = -1,36</td><td>I = 2,58</td></tr></table>