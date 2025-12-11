<|ref|>text<|/ref|><|det|>[[114, 83, 875, 120]]<|/det|>
Die Niveauflächen sind also Sphären in 3D um den Mittelpunkt (0;0;0) mit Radius \(\sqrt{L}\) mit der Gleichung 

<|ref|>equation<|/ref|><|det|>[[114, 118, 280, 140]]<|/det|>
\[z = \sqrt{L - x^2 - y^2}.\]

<|ref|>text<|/ref|><|det|>[[114, 139, 144, 156]]<|/det|>
c) 

<|ref|>text<|/ref|><|det|>[[114, 154, 528, 173]]<|/det|>
Die Niveaufläche zum Niveau L ergibt sich zu 

<|ref|>equation<|/ref|><|det|>[[114, 171, 333, 191]]<|/det|>
\[L = f(x, y, z) = x^2 + y^2.\]

<|ref|>text<|/ref|><|det|>[[114, 189, 875, 242]]<|/det|>
Für die Variable z gibt es keine Einschränkung, somit entsprechen die Niveauflächen von f dem Mantel von Zylindern in 3D, wobei die Symmetrieachse des Zylinders die z-Achse ist. Für den Radius des Zylinders ergibt sich \(\sqrt{L}\). 

<|ref|>sub_title<|/ref|><|det|>[[114, 256, 666, 275]]<|/det|>
## 6. Funktionsgraphen und Höhenlinien mit Python/Numpy 

<|ref|>text<|/ref|><|det|>[[114, 273, 787, 308]]<|/det|>
Plotten Sie sowohl die Funktion als auch die Höhenlinien der angegebenen Funktionen mit Python/Numpy. 

<|ref|>equation<|/ref|><|det|>[[114, 305, 808, 362]]<|/det|>
\[
\begin{align*}
a) f(x, y) &= \frac{x}{2} && b) f(x, y) &= \frac{y}{2} && c) f(x, y) &= \frac{x+y}{2} \\
d) f(x, y) &= \frac{x \cdot y}{4} && e) f(x, y) &= \frac{x^2 + y^2}{2} && f) f(x, y) &= \frac{6 \cdot \sin(xy)}{1+x^2+y^2}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 375, 144, 392]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[114, 390, 407, 407]]<|/det|>
# Python initialisieren: 

<|ref|>text<|/ref|><|det|>[[114, 406, 495, 423]]<|/det|>
import matplotlib.pyplot as pl; 

<|ref|>text<|/ref|><|det|>[[114, 421, 515, 439]]<|/det|>
from mpl_toolkits import mplot3d; 

<|ref|>text<|/ref|><|det|>[[114, 438, 340, 455]]<|/det|>
import numpy as np; 

<|ref|>text<|/ref|><|det|>[[114, 455, 264, 471]]<|/det|>
# Parameter: 

<|ref|>text<|/ref|><|det|>[[114, 470, 469, 488]]<|/det|>
x_0=-2; x_E=2; y_0=-2; y_E=2; 

<|ref|>text<|/ref|><|det|>[[114, 486, 792, 504]]<|/det|>
N_x=401; N_y=401; # Anzahl Intervalle für x- bzw y-Achse 

<|ref|>text<|/ref|><|det|>[[114, 502, 490, 520]]<|/det|>
N_g=10; N_l=31; # Schrittweite 

<|ref|>text<|/ref|><|det|>[[114, 519, 819, 552]]<|/det|>
az=70; el=25; # Drehwinkel gegenüber z-Achse (azimuth) und gegenüber xy-Ebene 

<|ref|>text<|/ref|><|det|>[[114, 551, 195, 568]]<|/det|>
fig=1; 

<|ref|>text<|/ref|><|det|>[[114, 567, 275, 584]]<|/det|>
# Funktionen: 

<|ref|>text<|/ref|><|det|>[[114, 583, 456, 601]]<|/det|>
def f(x,y): z=x/2; return z; 

<|ref|>text<|/ref|><|det|>[[114, 600, 219, 616]]<|/det|>
# Daten: 

<|ref|>text<|/ref|><|det|>[[114, 615, 771, 649]]<|/det|>
x_data=np.linspace(x_0, x_E, N_x); # Punkte auf x-Achse erzeugen 

<|ref|>text<|/ref|><|det|>[[114, 647, 771, 681]]<|/det|>
y_data=np.linspace(y_0, y_E, N_y); # Punkte auf y-Achse erzeugen 

<|ref|>text<|/ref|><|det|>[[114, 679, 820, 714]]<|/det|>
[x_grid, y_grid]=np.meshgrid(x_data, y_data); # Pärchen mit allen x- und y-Werten 

<|ref|>text<|/ref|><|det|>[[114, 712, 760, 730]]<|/det|>
z_grid=f(x_grid, y_grid); # Funktionswerte der Pärchen 

<|ref|>text<|/ref|><|det|>[[114, 728, 275, 745]]<|/det|>
# Graph-Plot: 

<|ref|>text<|/ref|><|det|>[[114, 744, 647, 762]]<|/det|>
pl.figure(fig); ax=pl.axes(projection='3d'); 

<|ref|>text<|/ref|><|det|>[[114, 760, 850, 795]]<|/det|>
ax.plot_surface(x_grid, y_grid, z_grid, rstride=N_g, cstride=N_g, cmap='rainbow'); ax.view_init(el, az); 

<|ref|>text<|/ref|><|det|>[[114, 793, 830, 828]]<|/det|>
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z'); ax.set_box_aspect((np.ptp(x_grid), np.ptp(y_grid), np.ptp(z_grid))); 

<|ref|>text<|/ref|><|det|>[[114, 826, 325, 843]]<|/det|>
pl.title('3D Darstellung'); 

<|ref|>text<|/ref|><|det|>[[114, 842, 346, 859]]<|/det|>
# Höhenlinien-Plot: 

<|ref|>text<|/ref|><|det|>[[114, 858, 463, 875]]<|/det|>
fig=fig+1; fh=pl.figure(fig); 

<|ref|>text<|/ref|><|det|>[[114, 874, 562, 892]]<|/det|>
pl.contour(x_grid, y_grid, z_grid, N_l); 

<|ref|>text<|/ref|><|det|>[[114, 890, 504, 908]]<|/det|>
pl.xlabel('x'); pl.ylabel('y');