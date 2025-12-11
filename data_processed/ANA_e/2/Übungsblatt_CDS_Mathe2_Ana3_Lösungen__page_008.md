<|ref|>text<|/ref|><|det|>[[117, 88, 523, 103]]<|/det|>
Für das vorgegebene Integral \(I\) erhalten wir damit die Lösung 

<|ref|>equation<|/ref|><|det|>[[160, 110, 841, 160]]<|/det|>
\[
I = \int \frac{x}{\cos^2 x} \, dx = x \cdot \tan x - I_1 = x \cdot \tan x - (-\ln |\cos x| + C) = x \cdot \tan x + \ln |\cos x| - C = \\
= x \cdot \tan x + \ln |\cos x| + C^* \quad (C^* = -C)
\]

<|ref|>text<|/ref|><|det|>[[117, 161, 877, 202]]<|/det|>
Wir „verifizieren“ das Ergebnis, indem wir zeigen, dass die 1. Ableitung des unbestimmten Integrals zum Integranden führt. Dabei verwenden wir in der angedeuteten Weise die Produktregel (1. Summand) und die Kettenregel (2. Summand): 

<|ref|>equation<|/ref|><|det|>[[160, 208, 530, 245]]<|/det|>
\[
I = x \cdot \tan x + \ln |\cos x| + C^* = u v + \ln |t| + C^* \\
u \quad v \quad t
\]

<|ref|>equation<|/ref|><|det|>[[160, 253, 880, 285]]<|/det|>
\[
I' = u' v + v' u + \frac{1}{t} \cdot t' = 1 \cdot \tan x + \frac{1}{\cos^2 x} \cdot x + \frac{1}{\cos x} \cdot (-\sin x) = \tan x + \frac{x}{\cos^2 x} - \tan x = \frac{x}{\cos^2 x}
\]

<|ref|>text<|/ref|><|det|>[[117, 290, 593, 304]]<|/det|>
(unter Verwendung der trigonometrischen Beziehung \(\sin x / \cos x = \tan x\)) 

<|ref|>text<|/ref|><|det|>[[117, 307, 145, 323]]<|/det|>
e) 

<|ref|>text<|/ref|><|det|>[[117, 323, 858, 338]]<|/det|>
Die Substitution \(u = 1 + e^x\) führt zu einer Vereinfachung im Nenner des Integranden. Somit gilt (versuchsweise): 

<|ref|>equation<|/ref|><|det|>[[163, 344, 426, 373]]<|/det|>
\[
u = 1 + e^x, \quad \frac{du}{dx} = e^x, \quad dx = \frac{du}{e^x}
\]

<|ref|>text<|/ref|><|det|>[[117, 379, 370, 394]]<|/det|>
Durchführung der Integralsubstitution: 

<|ref|>equation<|/ref|><|det|>[[163, 400, 595, 434]]<|/det|>
\[
I = \int \frac{e^{2x}}{1 + e^x} \, dx = \int \frac{e^{2x} \cdot du}{u \cdot e^x} = \int \frac{e^x \cdot e^x \cdot du}{u \cdot e^x} = \int \frac{e^x}{u} \, du
\]

<|ref|>text<|/ref|><|det|>[[117, 440, 875, 468]]<|/det|>
Um die alte Variable \(x\) vollständig aus dem Integral zu entfernen, lösen wir die Substitutionsgleichung \(u = 1 + e^x\) nach \(e^x\) auf und setzen den gefundenen Ausdruck \(e^x = u - 1\) ein. Das Integral \(I\) lässt sich jetzt leicht lösen: 

<|ref|>equation<|/ref|><|det|>[[163, 473, 621, 506]]<|/det|>
\[
I = \int \frac{e^x}{u} \, du = \int \frac{u - 1}{u} \, du = \int \left(1 - \frac{1}{u}\right) \, du = u - \ln |u| + C
\]

<|ref|>text<|/ref|><|det|>[[117, 512, 593, 527]]<|/det|>
Nach der Rücksubstitution \(u = 1 + e^x\) erhält man die folgende Lösung: 

<|ref|>equation<|/ref|><|det|>[[163, 533, 824, 565]]<|/det|>
\[
I = \int \frac{e^{2x}}{1 + e^{x}} \, dx = (1 + e^x) - \ln |1 + e^x| + C = e^x - \ln (1 + e^x) + C^* \quad (C^* = 1 + C)
\]

<|ref|>text<|/ref|><|det|>[[117, 581, 144, 597]]<|/det|>
f) 

<|ref|>text<|/ref|><|det|>[[117, 599, 825, 631]]<|/det|>
Mit der naheliegenden Substitution \(u = \ln x\), \(\frac{du}{dx} = \frac{1}{x}\), \(dx = x \, du\) erreichen wir unser Ziel: 

<|ref|>equation<|/ref|><|det|>[[163, 635, 614, 668]]<|/det|>
\[
I = \int \frac{(\ln x)^3}{x} \, dx = \int \frac{u^3}{x} \cdot x \, du = \int u^3 \, du = \frac{1}{4} u^4 + C
\]

<|ref|>text<|/ref|><|det|>[[117, 675, 688, 690]]<|/det|>
Die Lösung lautet somit nach vollzogener Rücksubstitution \(u = \ln x\) wie folgt: 

<|ref|>equation<|/ref|><|det|>[[163, 698, 437, 735]]<|/det|>
\[
I = \int \frac{(\ln x)^3}{x^2} \, dx = \frac{1}{4} (\ln x)^4 + C
\]

<|ref|>sub_title<|/ref|><|det|>[[117, 753, 410, 770]]<|/det|>
5. Aufleiten mit Python/Sympy 

<|ref|>text<|/ref|><|det|>[[117, 770, 805, 788]]<|/det|>
Berechnen Sie die unbestimmten Integrale aus Aufgabe 4 mit Python/Sympy. 

<|ref|>text<|/ref|><|det|>[[117, 803, 144, 819]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[117, 819, 407, 835]]<|/det|>
# Python initialisieren: 

<|ref|>text<|/ref|><|det|>[[117, 835, 465, 851]]<|/det|>
import IPython.display as dp; 

<|ref|>text<|/ref|><|det|>[[117, 851, 346, 866]]<|/det|>
import sympy as sp; 

<|ref|>text<|/ref|><|det|>[[117, 866, 346, 882]]<|/det|>
sp.init_printing(); 

<|ref|>text<|/ref|><|det|>[[117, 882, 240, 897]]<|/det|>
# Symbole: 

<|ref|>text<|/ref|><|det|>[[117, 898, 333, 913]]<|/det|>
x=sp.symbols('x');