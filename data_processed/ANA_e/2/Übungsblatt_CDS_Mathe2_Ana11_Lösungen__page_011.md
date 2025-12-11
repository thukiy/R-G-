<|ref|>image<|/ref|><|det|>[[120, 81, 620, 306]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[115, 306, 150, 323]]<|/det|>
e) 

<|ref|>text<|/ref|><|det|>[[115, 322, 395, 340]]<|/det|>
Code für b) (a), c), d) analog): 

<|ref|>text<|/ref|><|det|>[[115, 339, 410, 356]]<|/det|>
# Python initialisieren: 

<|ref|>text<|/ref|><|det|>[[115, 355, 494, 372]]<|/det|>
import matplotlib.pyplot as pl; 

<|ref|>text<|/ref|><|det|>[[115, 371, 350, 388]]<|/det|>
import numpy as np; 

<|ref|>text<|/ref|><|det|>[[115, 387, 270, 404]]<|/det|>
# Parameter: 

<|ref|>text<|/ref|><|det|>[[115, 403, 844, 437]]<|/det|>
x_0=-6; x_E=6; y_0=-3; y_E=3; #Intervalle auf x- und y-Achse
festlegen 

<|ref|>text<|/ref|><|det|>[[115, 436, 748, 454]]<|/det|>
N_x=13; N_y=9; #Anzahl Intervalle auf x- und y-Achse 

<|ref|>text<|/ref|><|det|>[[115, 452, 808, 486]]<|/det|>
sc=16; # für Skalierung beim Quiverplot (findet umgekehrt statt 1/sc) 

<|ref|>text<|/ref|><|det|>[[115, 485, 412, 502]]<|/det|>
lw=0.005; # Linienstärke 

<|ref|>text<|/ref|><|det|>[[115, 501, 199, 518]]<|/det|>
fig=1; 

<|ref|>text<|/ref|><|det|>[[115, 517, 281, 534]]<|/det|>
# Funktionen: 

<|ref|>text<|/ref|><|det|>[[115, 533, 310, 550]]<|/det|>
def v(x,y): 

<|ref|>text<|/ref|><|det|>[[525, 532, 808, 550]]<|/det|>
# Vektorfeld definieren 

<|ref|>text<|/ref|><|det|>[[215, 549, 515, 566]]<|/det|>
v_x=x/((x**2+y**2)**0.5); 

<|ref|>text<|/ref|><|det|>[[215, 565, 515, 582]]<|/det|>
v_y=y/((x**2+y**2)**0.5); 

<|ref|>text<|/ref|><|det|>[[216, 581, 400, 598]]<|/det|>
return v_x,v_y; 

<|ref|>text<|/ref|><|det|>[[115, 597, 220, 614]]<|/det|>
# Daten: 

<|ref|>text<|/ref|><|det|>[[115, 613, 856, 646]]<|/det|>
x_data=np.linspace(x_0,x_E,N_x); # Generieren von Punkten auf x-Achse 

<|ref|>text<|/ref|><|det|>[[115, 645, 856, 679]]<|/det|>
y_data=np.linspace(y_0,y_E,N_y); # Generieren von Punkten auf y-Achse 

<|ref|>text<|/ref|><|det|>[[115, 678, 844, 711]]<|/det|>
[x_grid,y_grid]=np.meshgrid(x_data,y_data); # Generieren von Punktepaaren (x,y) 

<|ref|>text<|/ref|><|det|>[[115, 710, 797, 747]]<|/det|>
[v_x_grid,v_y_grid]=v(x_grid,y_grid); # Vektoren für die jeweiligen (x,y) bestimmen 

<|ref|>text<|/ref|><|det|>[[115, 745, 210, 761]]<|/det|>
# Plot: 

<|ref|>text<|/ref|><|det|>[[115, 761, 301, 778]]<|/det|>
pl.figure(fig); 

<|ref|>text<|/ref|><|det|>[[115, 777, 855, 810]]<|/det|>
pl.quiver(x_grid,y_grid,v_x_grid,v_y_grid,scale=sc,width=lw); # Plot eines Vektorfeldes 

<|ref|>text<|/ref|><|det|>[[115, 809, 856, 843]]<|/det|>
pl.xlabel('x'); pl.yscale('y'); # x- und y-Achsenbeschriftung
pl.grid('on'); # Gitter wird angezeigt 

<|ref|>text<|/ref|><|det|>[[115, 842, 820, 874]]<|/det|>
pl.axis('image'); # Achse wird entsprechend dem Datenlimit skaliert