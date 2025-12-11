<|ref|>text<|/ref|><|det|>[[120, 83, 310, 97]]<|/det|>
Wir betrachten die Ereignisse 

<|ref|>text<|/ref|><|det|>[[163, 105, 368, 121]]<|/det|>
\(T\): Treffer und \(\bar{T}\): Fehlschuss 

<|ref|>text<|/ref|><|det|>[[120, 128, 872, 170]]<|/det|>
mit den Wahrscheinlichkeiten \(P(T) = p = 0,3\) und \(P(\bar{T}) = 1 - P(T) = 1 - 0,3 = 0,7\). Das Ergebnis eines Versuches (Treffer oder Fehlschuss) ist dabei unabhängig vom Ergebnis des vorangegangenen Schussversuches (stochastisch unabhängige Ereignisse). 

<|ref|>text<|/ref|><|det|>[[120, 177, 710, 193]]<|/det|>
a) Der *Multiplikationssatz* (\(\rightarrow\) FS: Kap. XV.3.2) liefert für das Ereignis \(TTT\) (\(= 3\) Treffer): 

<|ref|>equation<|/ref|><|det|>[[163, 200, 777, 216]]<|/det|>
\[P(3 \text{ Treffer}) = P(TT) = P(T) \cdot P(T) \cdot P(T) = 0,3 \cdot 0,3 \cdot 0,3 = 0,3^3 = 0,027 \cong 2,7\%\]

<|ref|>text<|/ref|><|det|>[[120, 228, 733, 243]]<|/det|>
b) Drei mögliche Ereignisse (Fehlschuss beim 1. bzw. 2. bzw. 3. Versuch): \(\bar{T}T\bar{T}\), \(T\bar{T}T\), \(T\bar{T}\bar{T}\). 

<|ref|>equation<|/ref|><|det|>[[163, 249, 856, 290]]<|/det|>
\[P(2 \text{ Treffer}) = P(\bar{T}T\bar{T}) + P(T\bar{T}T) + P(TT\bar{T}) = 0,7 \cdot 0,3 \cdot 0,3 + 0,3 \cdot 0,7 \cdot 0,3 + 0,3 \cdot 0,3 \cdot 0,7 = 3(0,7 \cdot 0,3^2) = 0,189 \cong 18,9\%\]

<|ref|>text<|/ref|><|det|>[[120, 300, 750, 316]]<|/det|>
c) \(P(\text{mindestens } 2 \text{ Treffer}) = P(2 \text{ Treffer}) + P(3 \text{ Treffer}) = 0,189 + 0,027 = 0,216 \cong 21,6\%\) 

<|ref|>text<|/ref|><|det|>[[144, 318, 485, 333]]<|/det|>
(unter Berücksichtigung der Ergebnisse aus a) und b)) 

<|ref|>text<|/ref|><|det|>[[120, 343, 870, 395]]<|/det|>
d) Der Bogenschütze muss *mindestens* \(n\) Schüsse abgeben, um die Scheibe *wenigstens einmal* mit einer Wahrscheinlichkeit von 90% zu treffen (\(n\) ist dabei zunächst noch unbekannt). Mit \(p(i)\) bezeichnen wir die Wahrscheinlichkeit, dass der Schütze die Scheibe *erstmals* beim \(i\)-ten Schuss trifft (\(i = 1, 2, \ldots, n\); alle vorangegangenen Schüsse sind *Fehlschüsse*). Dabei gilt: 

<|ref|>equation<|/ref|><|det|>[[163, 400, 725, 465]]<|/det|>
\[p(1) = 0,3; \quad p(2) = 0,7 \cdot 0,3 = 0,3 \cdot 0,7^1; \quad p(3) = 0,7 \cdot 0,7 \cdot 0,3 = 0,3 \cdot 0.7^2; \\ \ldots; \quad p(n) = \frac{0,7 \cdot 0,7 \ldots 0,7 \cdot 0,3}{n-1} \cdot 0,3 = 0,3 \cdot 0,7^{n-1}\]

<|ref|>text<|/ref|><|det|>[[140, 471, 592, 487]]<|/det|>
Die ganzzahlige Unbekannte \(n\) genügt dann der folgenden Bedingung: 

<|ref|>equation<|/ref|><|det|>[[163, 491, 875, 595]]<|/det|>
\[p(1) + p(2) + p(3) + \ldots + p(n) = 0,3 + 0,3 \cdot 0,7^1 + 0,3 \cdot 0,7^2 + \ldots + 0,3 \cdot 0,7^{n-1} = \\ = 0,3(1 + 0,7^1 + 0,7^2 + \ldots + 0,7^{n-1}) = 0,3 \cdot \frac{0,7^n - 1}{0,7 - 1} = \frac{0,3(0,7^n - 1)}{-0,3} = 1 - 0,7^n = 0,9 \Rightarrow \\ \text{geometrische Reihe} (\rightarrow \text{FS: Kap. I.3.3}) \\ 0,7^n = 0,1 \mid \ln \Rightarrow \ln 0,7^n = \ln 0,1 \Rightarrow n \cdot \ln 0,7 = \ln 0,1 \Rightarrow n = \frac{\ln 0,1}{\ln 0,7} = 6,4557\]

<|ref|>text<|/ref|><|det|>[[120, 604, 880, 645]]<|/det|>
Da \(n\) ganzzahlig sein muss (\(n = \text{Anzahl der abgegebenen Schüsse}\)), lautet die Lösung \(n = 7\). D.h. der Schütze muss *mindestens* 7 Schüsse abgeben, um mit einer Wahrscheinlichkeit von 90% *wenigstens einmal* die Scheibe zu treffen. 

<|ref|>sub_title<|/ref|><|det|>[[117, 672, 290, 689]]<|/det|>
## 7. Kugeln in Urne 

<|ref|>text<|/ref|><|det|>[[117, 688, 880, 737]]<|/det|>
In einer Urne befinden sich 4 weisse (W) und 6 schwarze (S) Kugeln. Eine Kugel wird zufällig entnommen und dafür eine der anderen Farbe wieder hineingelegt. Dann wird der Urne eine weitere Kugel entnommen. Bestimmen Sie mit Hilfe des Ereignisbaumes die Wahrscheinlichkeit, dass 

<|ref|>text<|/ref|><|det|>[[117, 755, 470, 772]]<|/det|>
a) die zuletzt gezogene Kugel weiß ist, 

<|ref|>text<|/ref|><|det|>[[117, 770, 718, 788]]<|/det|>
b) man bei beiden Ziehungen jeweils Kugeln gleicher Farbe erhält, 

<|ref|>text<|/ref|><|det|>[[117, 786, 820, 821]]<|/det|>
c) beide Kugeln weiss sind, wenn bekannt ist, dass die gezogenen Kugeln die gleiche Farbe haben.