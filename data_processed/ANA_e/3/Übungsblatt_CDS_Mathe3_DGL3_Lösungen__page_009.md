<|ref|>text<|/ref|><|det|>[[114, 81, 144, 99]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[114, 98, 870, 133]]<|/det|>
Die DGL ist 1. Ordnung, analytisch isolierbar, autonom, linear inhomogen mit
konstanten Koeffizienten und separierbar. Für die statischen Lösungen muss gelten: 

<|ref|>equation<|/ref|><|det|>[[120, 135, 545, 170]]<|/det|>
\[0 = -\frac{1}{RC} \cdot U_C + \frac{1}{RC} \cdot U = -\frac{1}{RC} \cdot (U_C - U).\]

<|ref|>text<|/ref|><|det|>[[114, 170, 580, 189]]<|/det|>
Es ergibt sich somit als statische Lösung: \(U = 12V\). 

<|ref|>text<|/ref|><|det|>[[114, 203, 245, 220]]<|/det|>
Python Code: 

<|ref|>text<|/ref|><|det|>[[120, 223, 390, 238]]<|/det|>
# Python initialisieren: 

<|ref|>text<|/ref|><|det|>[[120, 239, 468, 255]]<|/det|>
import matplotlib.pyplot as pl; 

<|ref|>text<|/ref|><|det|>[[120, 255, 339, 271]]<|/det|>
import numpy as np; 

<|ref|>text<|/ref|><|det|>[[120, 271, 257, 286]]<|/det|>
# Parameter: 

<|ref|>text<|/ref|><|det|>[[120, 286, 411, 301]]<|/det|>
R=4.00; C=15.0e-3; U=12.0; 

<|ref|>text<|/ref|><|det|>[[120, 301, 485, 317]]<|/det|>
t_a=0; t_b=0.4; U_a=0; U_b=16.0; 

<|ref|>text<|/ref|><|det|>[[120, 316, 699, 332]]<|/det|>
N_t=17; N_U=17; sc_t=1e3; sc=2.5e4; aw=0.004; fig=1; 

<|ref|>text<|/ref|><|det|>[[120, 332, 270, 347]]<|/det|>
# Funktionen: 

<|ref|>text<|/ref|><|det|>[[120, 347, 567, 363]]<|/det|>
def f(t, U_C): s=(U-U_C)/(R*C); return s; 

<|ref|>text<|/ref|><|det|>[[120, 363, 270, 378]]<|/det|>
def v(t, U_C): 

<|ref|>text<|/ref|><|det|>[[215, 378, 325, 394]]<|/det|>
v_t=0*t+1; 

<|ref|>text<|/ref|><|det|>[[215, 394, 380, 410]]<|/det|>
v_U_C=f(t, U_C); 

<|ref|>text<|/ref|><|det|>[[215, 410, 400, 426]]<|/det|>
return v_t, v_U_C; 

<|ref|>text<|/ref|><|det|>[[120, 426, 216, 441]]<|/det|>
# Daten: 

<|ref|>text<|/ref|><|det|>[[120, 441, 475, 457]]<|/det|>
t_data=np.linspace(t_a, t_b, N_t); 

<|ref|>text<|/ref|><|det|>[[120, 456, 499, 472]]<|/det|>
U_C_data=np.linspace(U_a, U_b, N_U); 

<|ref|>text<|/ref|><|det|>[[120, 472, 642, 488]]<|/det|>
[t_grid, U_C_grid]=np.meshgrid(t_data, U_C_data); 

<|ref|>text<|/ref|><|det|>[[120, 487, 576, 504]]<|/det|>
[v_t_grid, v_U_C_grid]=v(t_grid, U_C_grid); 

<|ref|>text<|/ref|><|det|>[[120, 504, 205, 519]]<|/det|>
# Plot: 

<|ref|>text<|/ref|><|det|>[[120, 519, 325, 535]]<|/det|>
fh=pl.figure(fig); 

<|ref|>text<|/ref|><|det|>[[120, 534, 742, 565]]<|/det|>
pl.quiver(t_grid*sc_t, U_C_grid, v_t_grid*sc_t, v_U_C_grid,
angles='xy', scale=sc_width=aw); 

<|ref|>text<|/ref|><|det|>[[120, 564, 808, 581]]<|/det|>
pl.xlabel('$t[\mathrm{mm}][\mathrm{ms}]\$'); pl.ylabel('$U_C[\mathrm{mm}][\mathrm{V}]\$'); 

<|ref|>text<|/ref|><|det|>[[120, 580, 280, 596]]<|/det|>
pl.grid('on');