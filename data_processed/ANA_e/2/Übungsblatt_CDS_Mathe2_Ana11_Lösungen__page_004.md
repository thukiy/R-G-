<|ref|>text<|/ref|><|det|>[[114, 81, 135, 100]]<|/det|>
f) 

<|ref|>image<|/ref|><|det|>[[114, 115, 688, 450]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[114, 455, 145, 473]]<|/det|>
g) 

<|ref|>text<|/ref|><|det|>[[114, 470, 184, 488]]<|/det|>
Für a): 

<|ref|>text<|/ref|><|det|>[[114, 486, 405, 503]]<|/det|>
# Python initialisieren: 

<|ref|>text<|/ref|><|det|>[[114, 502, 494, 520]]<|/det|>
import matplotlib.pyplot as pl; 

<|ref|>text<|/ref|><|det|>[[114, 519, 345, 536]]<|/det|>
import numpy as np; 

<|ref|>text<|/ref|><|det|>[[114, 534, 264, 551]]<|/det|>
# Parameter: 

<|ref|>text<|/ref|><|det|>[[114, 550, 576, 568]]<|/det|>
t_0=0; t_E=2*np.pi; N=41; lw=3; fig=1; 

<|ref|>text<|/ref|><|det|>[[114, 567, 280, 584]]<|/det|>
# Funktionen: 

<|ref|>text<|/ref|><|det|>[[114, 583, 770, 600]]<|/det|>
def gamma(t): # Definition der parametrisierten Kurve 

<|ref|>text<|/ref|><|det|>[[114, 598, 277, 656]]<|/det|>
x=1+2*t;
y=3-t;
return x,y; 

<|ref|>text<|/ref|><|det|>[[114, 650, 214, 666]]<|/det|>
# Daten: 

<|ref|>text<|/ref|><|det|>[[114, 665, 480, 682]]<|/det|>
t_data=np.linspace(t_0,t_E,N); 

<|ref|>text<|/ref|><|det|>[[114, 680, 480, 698]]<|/det|>
[x_data,y_data]=gamma(t_data); 

<|ref|>text<|/ref|><|det|>[[114, 696, 204, 713]]<|/det|>
# Plot: 

<|ref|>text<|/ref|><|det|>[[114, 712, 336, 730]]<|/det|>
fh=pl.figure(fig); 

<|ref|>text<|/ref|><|det|>[[114, 728, 550, 746]]<|/det|>
pl.plot(x_data,y_data,linewidth=lw); 

<|ref|>text<|/ref|><|det|>[[114, 744, 500, 762]]<|/det|>
pl.xlabel('x'); pl.ylabel('y'); 

<|ref|>text<|/ref|><|det|>[[114, 760, 504, 778]]<|/det|>
pl.grid('on'); pl.axis('image'); 

<|ref|>text<|/ref|><|det|>[[144, 777, 330, 796]]<|/det|>
➔ analog für b) - f) 

<|ref|>sub_title<|/ref|><|det|>[[114, 810, 610, 829]]<|/det|>
3. Geschwindigkeits- und Tangenteneinheitsvektor 

<|ref|>text<|/ref|><|det|>[[114, 827, 816, 862]]<|/det|>
Berechnen Sie jeweils den Tangenteneinheitsvektor und skizzieren Sie diesen entlang der Spur. 

<|ref|>equation<|/ref|><|det|>[[114, 858, 839, 895]]<|/det|>
\[
\text{a) } \ddot{\gamma}(t) = \left( \frac{2t-3}{2-t} \right) \qquad \text{b) } \ddot{\gamma}(t) = \left( \frac{3\cos t - 3}{3\sin t + 1} \right) \qquad \text{c) } \ddot{\gamma}(t) = \left( \frac{3\cos t + 2}{2\sin t + 1} \right)
\]