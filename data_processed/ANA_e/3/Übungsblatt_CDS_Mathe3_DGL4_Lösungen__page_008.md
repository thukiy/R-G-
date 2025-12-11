<|ref|>text<|/ref|><|det|>[[114, 81, 825, 117]]<|/det|>
Da die Spannung jedoch nicht konstant ist, sondern zeitabhängig, gibt es keine statischen Lösungen. 

<|ref|>sub_title<|/ref|><|det|>[[114, 131, 245, 149]]<|/det|>
Python Code: 

<|ref|>text<|/ref|><|det|>[[114, 147, 820, 560]]<|/det|>
# Initialisieren
import numpy as np;
import matplotlib.pyplot as plt;
# Parameter
R=4; C=15*10**(-3);
t_0=0; t_E=1; N_t=21; # Anfangs- und Endzeitpunkt; Anzahl Punkte auf t-Achse
U_0=0; U_E=12; N_U=15; fig=1; # Anfangs- und Endspannungswert, Anzahl Punkte
# Funktionen
def U(t): u=12*(t-t_0); return u;
def f(t,U_C): u=(1/(R*C))*(U(t)-U_C); return u;
def v(t,U_C): v_t=0*t+1; v_U_C=f(t,U_C); return v_t, v_U_C;
# Daten
t_data=np.linspace(t_0,t_E,N_t);
U_C_data=np.linspace(U_0,U_E,N_U);
[t_grid,U_C_grid]=np.meshgrid(t_data,U_C_data); # Pärchen (t,U)
[v_t_grid,v_U_C_grid]=v(t_grid,U_C_grid);
# Plot
pl.figure(fig);
pl.quiver(t_grid*1000,U_C_grid,v_t_grid*1000,v_U_C_grid, angles='xy', scale=25000, width=0.004);
pl.xlabel('ms'); pl.ylabel('V'); pl.grid('on'); 

<|ref|>image<|/ref|><|det|>[[120, 570, 688, 872]]<|/det|>