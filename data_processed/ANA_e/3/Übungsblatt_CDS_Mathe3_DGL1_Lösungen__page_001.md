<|ref|>sub_title<|/ref|><|det|>[[115, 166, 485, 202]]<|/det|>
# Übungsblatt DGL 1 

<|ref|>text<|/ref|><|det|>[[575, 179, 880, 196]]<|/det|>
Computational and Data Science 

<|ref|>text<|/ref|><|det|>[[757, 199, 880, 216]]<|/det|>
BSc HS2024 

<|ref|>sub_title<|/ref|><|det|>[[115, 232, 270, 261]]<|/det|>
## Lösungen 

<|ref|>text<|/ref|><|det|>[[752, 241, 880, 258]]<|/det|>
Mathematik 3 

<|ref|>text<|/ref|><|det|>[[115, 287, 210, 305]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 303, 855, 354]]<|/det|>
- Sie kennen die Begriffe gewöhnliche Differentialgleichung, Ordnung, analytisch isolierbar, elementar integrierbar, autonom, linear, linear homogen und separierbar und können diese erklären und auf konkrete Beispiele anwenden. 

<|ref|>text<|/ref|><|det|>[[115, 352, 850, 370]]<|/det|>
- Sie kennen die Abkürzungen DGL, ODE, AWP, IVP und IC und ihre Bedeutung. 

<|ref|>text<|/ref|><|det|>[[115, 368, 870, 419]]<|/det|>
- Sie können bestimmen, ob eine DGL 1. Ordnung analytisch isolierbar, elementar integrierbar, autonom, linear, linear homogen, linear mit konstanten Koeffizienten oder separierbar ist. 

<|ref|>text<|/ref|><|det|>[[115, 418, 870, 453]]<|/det|>
- Sie können überprüfen, ob eine gegebene Funktion eine gegebene DGL oder ein AWP 1. Ordnung löst. 

<|ref|>sub_title<|/ref|><|det|>[[115, 484, 519, 503]]<|/det|>
## 1. Aussagen über Differentialgleichungen 

<|ref|>text<|/ref|><|det|>[[115, 501, 680, 519]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[115, 516, 880, 653]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Die Lösung einer Differentialgleichung – angenommen es existiert eine Lösung – ist in jedem Fall eine reelle Zahl.</td><td></td><td>X</td></tr><tr><td>b) Jede Differentialgleichung hat entweder keine oder genaue eine Lösung.</td><td></td><td>X</td></tr><tr><td>c) Ein Anfangswertproblem hat meistens unendlich viele Lösungen.</td><td></td><td>X</td></tr><tr><td>d) Eine Differentialgleichung kann sowohl linear inhomogen als auch autonom sein.</td><td>X</td><td></td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[115, 668, 476, 686]]<|/det|>
## 2. Klassifikation von DGL 1. Ordnung 

<|ref|>text<|/ref|><|det|>[[115, 684, 725, 752]]<|/det|>
a) \(y' = 0\) b) \(y' = 2\) c) \(y' = 3x\) d) \(y' = y\) e) \(y' + 2y = 0\) f) \(y' y = -3\) g) \(y' - 3y + x = 0\) h) \(4y' = 3x + 5x^2y\) i) \(4xy' = 3x^2y + 20xy\) j) \(4xy' = 3x^2y^2 + 20xy^2\) k) \(\sin(y) + y' + \sin(x) = \sqrt{y}\) l) \(\sin(y') + y + \sin(x) = \sqrt{y'}\) 

<|ref|>text<|/ref|><|det|>[[115, 760, 714, 780]]<|/det|>
Klassifizieren Sie die obigen DGL gemäss den folgenden Kriterien: 

<|ref|>table<|/ref|><|det|>[[115, 782, 907, 925]]<|/det|>
<table><tr><td></td><td>a)</td><td>b)</td><td>c)</td><td>d)</td><td>e)</td><td>f)</td><td>g)</td><td>h)</td><td>i)</td><td>j)</td><td>k)</td><td>l)</td></tr><tr><td>Analytisch isolierbar</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>Elementar integrierbar</td><td>X</td><td>X</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Autonom</td><td>X</td><td>X</td><td></td><td>X</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Linear</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><tr><td>Linear homogen</td><td>X</td><td></td><td>X</td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>Linear mit konst. Koeffizienten</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td>X<td></td><td></td><td></td><td></td><td></td></tr><tr><td>separierbar</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td></td><td>X</td><td>X</td><td></td><td></td></tr></tr></table>