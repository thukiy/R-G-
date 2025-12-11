<|ref|>sub_title<|/ref|><|det|>[[114, 99, 320, 116]]<|/det|>
## 3. Qualitätskontrolle 

<|ref|>text<|/ref|><|det|>[[114, 115, 884, 166]]<|/det|>
In einer Lieferung von 10 Glühbirnen vom gleichen Typ befinden sich 2 defekte. Zu Kontrollzwecken werden 3 Glühbirnen zufällig entnommen. Die Zufallsvariable X beschreibe die Anzahl der dabei erhaltenen defekten Glühbirnen. 

<|ref|>text<|/ref|><|det|>[[114, 165, 620, 183]]<|/det|>
a) Bestimmen Sie die Verteilung der Zufallsvariablen X. 

<|ref|>text<|/ref|><|det|>[[114, 181, 884, 216]]<|/det|>
b) Wie gross ist die Wahrscheinlichkeit, dass sich in einer solchen Stichprobe genau eine defekte Glühbirne befindet? 

<|ref|>text<|/ref|><|det|>[[120, 229, 879, 248]]<|/det|>
a) Anzahl der möglichen Stichproben (Kombinationen 3. Ordnung ohne Wiederholung): 

<|ref|>equation<|/ref|><|det|>[[160, 249, 400, 290]]<|/det|>
\[C(10; 3) = \binom{10}{3} = 120\]

<|ref|>text<|/ref|><|det|>[[160, 285, 808, 323]]<|/det|>
\(X = 0\) Nur einwandfreie Glühbirnen (3 aus 8): \(C(8; 3) = \binom{8}{3} = 56\) 

<|ref|>text<|/ref|><|det|>[[250, 323, 657, 342]]<|/det|>
Somit: \(P(X = 0) = f(0) = 56/120 = 7/15\) 

<|ref|>text<|/ref|><|det|>[[160, 352, 733, 375]]<|/det|>
\(X = 1\) 1 defekte (aus 2) und 2 einwandfreie Glühbirnen (aus 8): 

<|ref|>equation<|/ref|><|det|>[[250, 375, 702, 418]]<|/det|>
\[C(2; 1) \cdot C(8; 2) = \binom{2}{1} \cdot \binom{8}{2} = 2 \cdot 28 = 56\]

<|ref|>text<|/ref|><|det|>[[250, 426, 657, 446]]<|/det|>
Somit: \(P(X = 1) = f(1) = 56/120 = 7/15\) 

<|ref|>text<|/ref|><|det|>[[160 447, 733, 468]]<|/det|>
\(X = 2\) 2 defekte (aus 2) und 1 einwandfreie Glühbirne (aus 8): 

<|ref|>equation<|/ref|><|det|>[[240, 470, 678, 514]]<|/det|>
\[C(2; 2) \cdot C(8; 1) = \binom{2}{2} \cdot \binom{8}{1} = 1 \cdot 8 = 8\]

<|ref|>text<|/ref|><|det|>[[240, 520, 642, 540]]<|/det|>
Somit: \(P(X = 2) = f(2) = 8/120 = 1/15\) 

<|ref|>text<|/ref|><|det|>[[160, 560, 333, 590]]<|/det|>
Verteilungstabelle: 

<|ref|>table<|/ref|><|det|>[[352, 555, 642, 609]]<|/det|>
<table><tr><td>\(x_i\)</td><td>0</td><td>1</td><td>2</td></tr><tr><td>\(f(x_i)\)</td><td>7/15</td><td>7/15</td><td>1/15</td></tr></table>

<|ref|>text<|/ref|><|det|>[[120, 620, 405, 640]]<|/det|>
b) \(P(X = 1) = f(1) = 7/15\) 

<|ref|>sub_title<|/ref|><|det|>[[114, 657, 211, 674]]<|/det|>
## 4. Würfel 

<|ref|>text<|/ref|><|det|>[[114, 674, 884, 758]]<|/det|>
Ein Würfel werde so oft geworfen, bis entweder eine 6 erscheint oder viermal nacheinander keine 6 erscheint. Die Zufallsgrösse X sei die Anzahl der benötigten Würfe. Welche Werte kann X annehmen, und mit welchen Wahrscheinlichkeiten ist das der Fall? Man skizziere die Verteilungsfunktion von X und gebe sie in mathematischer Schreibweise an. 

<|ref|>text<|/ref|><|det|>[[114, 772, 884, 840]]<|/det|>
Da wenigstens einmal gewürfelt wird, ist der kleinste Wert, den die Zufallsgrösse X annehmen kann, \(x_1 = 1\). Wenn viermal nacheinander keine 6 erscheint, ist das Spiel beendet. Demzufolge ist der grösste Wert, den die Zufallsgrösse realisieren kann, \(x_4 = 4\): 

<|ref|>text<|/ref|><|det|>[[114, 839, 884, 923]]<|/det|>
Die Zufallsgrösse X kann also nur die Werte \(x_1 = 1\), \(x_2 = 2\), \(x_3 = 3\) und \(x_4 = 4\) annehmen. Andere Werte sind nicht möglich, X ist eine diskrete Zufallsgrösse. Kommen wir nun zu den Wahrscheinlichkeiten (die dann als Sprunghöhen im Bild der Verteilungsfunktion einzutragen sind). Wird beim ersten Wurf eine 6 geworfen, dann realisiert die Zufallsgrösse den Wert \(x_1 = 1\) mit der Wahrscheinlichkeit