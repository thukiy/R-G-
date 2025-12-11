<|ref|>text<|/ref|><|det|>[[122, 66, 405, 85]]<|/det|>
d) Wir betrachten die Funktion 

<|ref|>equation<|/ref|><|det|>[[150, 90, 297, 125]]<|/det|>
\[f(x) = \frac{1}{1 + e^{-x}}.\]

<|ref|>text<|/ref|><|det|>[[150, 128, 533, 147]]<|/det|>
Mit Hilfe der Reziproken-Regel erhalten wir 

<|ref|>equation<|/ref|><|det|>[[150, 152, 747, 250]]<|/det|>
\[ 
\begin{align*} 
f'(x) &= -\frac{(1 + e^{-x})'}{(1 + e^{-x})^2} = -\frac{0 - e^{-x}}{(1 + e^{-x})^2} = \frac{e^{-x}}{(1 + e^{-x})^2} = \frac{e^{2x} \cdot e^{-x}}{e^{2x} \cdot (1 + e^{-x})^2} \\
&= \frac{e^{2x-x}}{(e^x)^2 \cdot (1 + e^{-x})^2} = \frac{e^x}{(e^x \cdot (1 + e^{-x}))^2} = \frac{e^x}{(e^x + 1)^2}. 
\end{align*} 
\]

<|ref|>text<|/ref|><|det|>[[122, 263, 404, 282]]<|/det|>
e) Wir betrachten die Funktion 

<|ref|>equation<|/ref|><|det|>[[150, 288, 420, 312]]<|/det|>
\[f(x) = \ln^{\ln(x)}(x) = (\ln(x))^{\ln(x)}.\]

<|ref|>text<|/ref|><|det|>[[150, 317, 540, 336]]<|/det|>
Mit Hilfe der Exponential-Regel erhalten wir 

<|ref|>equation<|/ref|><|det|>[[150, 341, 801, 425]]<|/det|>
\[ 
\begin{align*} 
f'(x) &= \left(\ln'(x) \cdot \ln(\ln(x)) + \ln'(x) \cdot \frac{\ln(x)}{\ln(x)}\right) \cdot \ln^{\ln(x)}(x) \\
&= \left(\frac{1}{x} \cdot \ln(\ln(x)) + \frac{1}{x} \cdot 1\right) \cdot \ln^{\ln(x)}(x) = \frac{1}{x} \cdot \left(\ln(\ln(x)) + 1\right) \cdot \ln^{\ln(x)}(x). 
\end{align*} 
\]

<|ref|>text<|/ref|><|det|>[[122, 437, 405, 456]]<|/det|>
f) Wir betrachten die Funktion 

<|ref|>equation<|/ref|><|det|>[[150, 461, 290, 503]]<|/det|>
\[f(x) = \frac{2^{-\sqrt{|x|}}}{\ln(2)}.\]

<|ref|>text<|/ref|><|det|>[[150, 508, 494, 526]]<|/det|>
Mit Hilfe der Ketten-Regel erhalten wir 

<|ref|>equation<|/ref|><|det|>[[150, 531, 902, 625]]<|/det|>
\[ 
\begin{align*} 
f'(x) &= \frac{1}{\ln(2)} \cdot \left(-\sqrt{|x|}\right)' \cdot \ln(2) \cdot 2^{-\sqrt{|x|}} = -\frac{1}{2 \cdot \sqrt{|x|}} \cdot |x|' \cdot 2^{-\sqrt{|x|}} = -\frac{\operatorname{sgn}(x)}{2 \cdot \sqrt{|x|}} \cdot 2^{-\sqrt{|x|}} \\
&= -\frac{\operatorname{sgn}(x)}{\sqrt{|x|}} \cdot 2^{-\sqrt{|x|}-1}. 
\end{align*} 
\]

<|ref|>sub_title<|/ref|><|det|>[[107, 647, 606, 666]]<|/det|>
9. Diverse Ableitungen berechnen mit Python/Sympy 

<|ref|>text<|/ref|><|det|>[[107, 665, 912, 701]]<|/det|>
Wir berechnen die Ableitungen aus Aufgabe 8 mit Python/Sympy. Dazu implementieren wir den folgenden Code, den wir für jede Teilaufgabe modifizieren. 

<|ref|>text<|/ref|><|det|>[[107, 706, 444, 920]]<|/det|>
# Python initialisieren:
import IPython.display as dp;
import sympy as sp;
# Python konfigurieren:
sp.init_printing();
x=sp.symbols('x',real=True);
# Parameter:
f=...;
# Berechnungen:
fs=sp.simplify(sp.diff(f,x));
# Ausgabe:
dp.display(f);
dp.display(fs);