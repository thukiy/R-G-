<|ref|>sub_title<|/ref|><|det|>[[115, 166, 490, 202]]<|/det|>
# Übungsblatt DGL 2 

<|ref|>text<|/ref|><|det|>[[576, 179, 880, 196]]<|/det|>
Computational and Data Science 

<|ref|>text<|/ref|><|det|>[[757, 199, 884, 216]]<|/det|>
BSc HS2024 

<|ref|>sub_title<|/ref|><|det|>[[115, 232, 272, 261]]<|/det|>
## Lösungen 

<|ref|>text<|/ref|><|det|>[[752, 240, 884, 258]]<|/det|>
Mathematik 3 

<|ref|>sub_title<|/ref|><|det|>[[115, 287, 211, 305]]<|/det|>
### Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 303, 816, 339]]<|/det|>
- Sie kennen die Begriffe Richtungsvektorfeld, stabile und instabile statische Lösung, Attraktor und Repellor sowie ihre wichtigsten Eigenschaften. 

<|ref|>text<|/ref|><|det|>[[115, 337, 785, 355]]<|/det|>
- Sie können die statischen Lösungen einer DGL 1. Ordnung berechnen. 

<|ref|>text<|/ref|><|det|>[[115, 353, 828, 387]]<|/det|>
- Sie können das Richtungsvektorfeld einer DGL 1. Ordnung in Komponenten angeben, von Hand skizzieren und mit Python plotten. 

<|ref|>text<|/ref|><|det|>[[115, 386, 845, 436]]<|/det|>
- Sie können anhand der Skizze des Richtungsvektorfeldes beurteilen, ob eine statische Lösung ein Attraktor, ein Repellor, stabil oder instabil ist. Sie können des Weiteren beurteilen, ob die DGL elementar integrierbar oder autonom ist. 

<|ref|>sub_title<|/ref|><|det|>[[115, 467, 512, 486]]<|/det|>
## 1. Aussagen über Richtungsvektorfelder 

<|ref|>text<|/ref|><|det|>[[115, 492, 683, 510]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[115, 508, 880, 712]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Jede DGL hat ein Richtungsvektorfeld.</td><td></td><td>X</td></tr><tr><td>b) Mit Hilfe des Richtungsvektorfeldes kann man eine DGL 1. Ordnung lösen.</td><td></td><td>X</td></tr><tr><td>c) Mit Hilfe des Richtungsvektorfeldes kann man eine DGL 1. Ordnun g visualisieren.</td><td>X</td><td></td></tr><tr><td>d) Die Vektoren des Richtungsvektorfeldes sind an jedem Punkt Einheitsvektoren.</td><td>X</td><td></td></tr><tr><td>e) Die Graphen der Lösungen einer DGL 1. Ordnung stehen an jedem Punkt senkrecht auf dem Richtungsvektorfeld.</td><td></td><td>X</td></tr><tr><td>f) Anhand des Richtungsvektorfeldes einer DGL 1. Ordnung kann man die Stabilität ihrer statischen Lösungen beurteilen.</td><td>X</td><td></td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[115, 727, 519, 745]]<|/det|>
## 2. Skizzieren von Richtungsvektorfeldern 

<|ref|>text<|/ref|><|det|>[[115, 744, 870, 828]]<|/det|>
Bestimmen Sie die statischen Lösungen der angegebenen DGL sowie die Komponenten des Richtungsvektorfeldes. Skizzieren Sie das Richtungsvektorfeld von Hand. Geben Sie bei jeder statischen Lösung an, ob es sich um einen Attraktor, Repellor oder keines von beidem handelt. Welche der statischen Lösungen sind stabil? 

<|ref|>text<|/ref|><|det|>[[115, 826, 222, 844]]<|/det|>
a) \(y' = 0\) 

<|ref|>text<|/ref|><|det|>[[115, 843, 197, 861]]<|/det|>
d) \(y' = y\) 

<|ref|>text<|/ref|><|det|>[[115, 860, 206, 878]]<|/det|>
g) \(y' = |x|\) 

<|ref|>text<|/ref|><|det|>[[115, 877, 295, 896]]<|/det|>
j) \(y' = (2 - y) \cdot (1 - y)\) 

<|ref|>text<|/ref|><|det|>[[375, 826, 450, 844]]<|/det|>
b) \(y' = 1\) 

<|ref|>text<|/ref|><|det|>[[375, 843, 456, 861]]<|/det|>
e) \(y' = x\) 

<|ref|>text<|/ref|><|det|>[[375, 860, 490, 878]]<|/det|>
h) \(y' = 1 - y\) 

<|ref|>text<|/ref|><|det|>[[375, 877, 520, 896]]<|/det|>
k) \(y' = y^2 - y - 2\) 

<|ref|>text<|/ref|><|det|>[[635, 826, 719, 844]]<|/det|>
c) \(y' = -1\) 

<|ref|>text<|/ref|><|det|>[[635, 843, 720, 861]]<|/det|>
f) \(y' = |y|\) 

<|ref|>text<|/ref|><|det|>[[635, 860, 736, 878]]<|/det|>
i) \(y' = 2 - y\) 

<|ref|>text<|/ref|><|det|>[[635, 876, 785, 896]]<|/det|>
l) \(y' = |y| \cdot (y + 1)\) 

<|ref|>text<|/ref|><|det|>[[115, 910, 794, 929]]<|/det|>
Für statische Lösungen muss folgende Bedingung erfüllt sein: \(y' = 0 = f(x, y)\).