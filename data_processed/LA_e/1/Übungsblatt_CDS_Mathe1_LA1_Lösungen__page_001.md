<|ref|>title<|/ref|><|det|>[[108, 155, 485, 196]]<|/det|>
# Übungsblatt LA 1 

<|ref|>text<|/ref|><|det|>[[570, 157, 928, 196]]<|/det|>
Computational and Data Science BSc
HS 2023 

<|ref|>text<|/ref|><|det|>[[108, 234, 255, 261]]<|/det|>
Lösungen 

<|ref|>text<|/ref|><|det|>[[781, 241, 923, 260]]<|/det|>
Mathematik 1 

<|ref|>sub_title<|/ref|><|det|>[[108, 289, 422, 309]]<|/det|>
## 1. Aussagen über Python/Numpy 

<|ref|>table<|/ref|><|det|>[[108, 316, 920, 500]]<|/det|>
<table><tr><td>Welche der folgenden Aussagen sind wahr und welche falsch?</td><td>wahr</td><td>falsch</td></tr><tr><td>a) Python/Numpy wurde speziell für den Unterricht an Schulen entwickelt.</td><td>○</td><td>●</td></tr><tr><td>b) Python/Numpy ist die Abkürzung von "Numerical Python".</td><td>●</td><td>○</td></tr><tr><td>c) Python/Numpy ist ein CAS (Computer-Algebra-Systeme).</td><td>○</td><td>●</td></tr><tr><td>d) Die Kernkompetenzen von Python/Numpy sind Numerik, Datenverarbeitung und Datenvisualisierung.</td><td>●</td><td>○</td></tr><tr><td>e) Python/Numpy ist für die gängigen Betriebssysteme Windows, Mac und Linux erhältlich.</td><td>●</td><td>○</td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[108, 550, 675, 568]]<|/det|>
## 2. Terme mit Hilfe von Python/Numpy numerisch auswerten 

<|ref|>text<|/ref|><|det|>[[108, 567, 920, 603]]<|/det|>
Wir werten jeweils den Term mit Python/Numpy numerisch aus. Dazu implementieren wir den folgenden Code, den wir für jede Teilaufgabe ergänzen. 

<|ref|>text<|/ref|><|det|>[[108, 609, 386, 675]]<|/det|>
# Python initialisieren:
import numpy as np;
# Berechnungen:
... 

<|ref|>text<|/ref|><|det|>[[120, 695, 330, 713]]<|/det|>
a) 45.6³ durch 45.6**3 

<|ref|>text<|/ref|><|det|>[[120, 719, 340, 740]]<|/det|>
b) \(\sqrt{3}\) durch np.sqrt(3) 

<|ref|>text<|/ref|><|det|>[[120, 745, 320, 766]]<|/det|>
c) \(\sqrt[5]{2}\) durch 2**(1/5) 

<|ref|>text<|/ref|><|det|>[[120, 771, 472, 792]]<|/det|>
d) \(\sqrt[7]{5.654 \cdot 10^{24}}\) durch 5.654e24**(1/7) 

<|ref|>text<|/ref|><|det|>[[120, 797, 370, 819]]<|/det|>
e) 44.5⁵ durch 44.5**(5/9) 

<|ref|>text<|/ref|><|det|>[[120, 826, 308, 846]]<|/det|>
f) 4π durch 4*np.pi 

<|ref|>text<|/ref|><|det|>[[120, 852, 435, 873]]<|/det|>
g) \(\sin(5\pi/4)\) durch \(\sin(5*np.pi/4)\) 

<|ref|>text<|/ref|><|det|>[[120, 878, 477, 899]]<|/det|>
h) \(\cot(-3\pi/5)\) durch \(1/\tan(-3*np.pi/5)\) 

<|ref|>text<|/ref|><|det|>[[536, 695, 864, 715]]<|/det|>
i) \(\tan(77^\circ)\) durch \(\tan(77*np.pi/180)\) 

<|ref|>text<|/ref|><|det|>[[536, 721, 898, 741]]<|/det|>
j) \(\arccos(-0.45)\) durch np.arccos(-0.45) 

<|ref|>text<|/ref|><|det|>[[536, 747, 888, 767]]<|/det|>
k) \(\operatorname{arccot}(34.1)\) durch np.arctan(1/34.1) 

<|ref|>text<|/ref|><|det|>[[536, 773, 797, 793]]<|/det|>
l) \(e^{-3.34}\) durch np.exp(-3.34) 

<|ref|>text<|/ref|><|det|>[[528, 800, 723, 820]]<|/det|>
m) e durch np.exp(1) 

<|ref|>text<|/ref|><|det|>[[528, 826, 810, 846]]<|/det|>
n) \(\ln(13.2)\) durch np.log(13.2) 

<|ref|>text<|/ref|><|det|>[[528, 852, 935, 873]]<|/det|>
o) \(\log_{10}(23'456)\) durch np.log(23)/np.log(10) 

<|ref|>text<|/ref|><|det|>[[528, 878, 916, 899]]<|/det|>
p) \(\log_{2}(69.6)\) durch np.log(69.6)/np.log(2)