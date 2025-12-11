<|ref|>image<|/ref|><|det|>[[120, 81, 875, 504]]<|/det|>
 

<|ref|>sub_title<|/ref|><|det|>[[114, 519, 625, 538]]<|/det|>
## 3. Richtungsvektorfelder mit Python/Numpy plotten I 

<|ref|>text<|/ref|><|det|>[[114, 536, 315, 555]]<|/det|>
Gegeben sei die DGL 

<|ref|>equation<|/ref|><|det|>[[114, 553, 430, 575]]<|/det|>
\[y' = f(x, y) \text{ mit } f(x, y) = 1 - y^2.\]

<|ref|>text<|/ref|><|det|>[[114, 572, 835, 608]]<|/det|>
In der Datei `RVF_Blatt2_A3.py` ist der Python/Numpy Code gegeben, um das Richtungsvektorfeld dieser DGL zu plotten. 

<|ref|>text<|/ref|><|det|>[[114, 606, 857, 658]]<|/det|>
a) Bestimmen Sie die statischen Lösungen dieser DGL und skizzieren Sie das Richtungsvektorfeld von Hand. Vergleichen Sie das Ergebnis mit dem Plot, den Sie mittels der Datei `RVF_Blatt2_A3.py` erhalten. 

<|ref|>text<|/ref|><|det|>[[114, 656, 870, 709]]<|/det|>
b) Studieren Sie den Code – Sie sollten verstehen, welche Auswirkungen die Befehle jeder Zeile haben. Nehmen Sie hierfür unter Umständen das Internet zur Hilfe. Setzen Sie sich definitiv mit dem Befehl `pl.quiver` auseinander. 

<|ref|>text<|/ref|><|det|>[[114, 707, 850, 742]]<|/det|>
c) Welche Bedeutung hat der Parameter `sc`? Variieren Sie hierzu am besten den Wert dieses Parameters. 

<|ref|>text<|/ref|><|det|>[[114, 741, 861, 793]]<|/det|>
d) Weshalb ist es wichtig, die statischen Lösungen der DGL zu kennen, bevor man den Python/Numpy Code zum Plotten des Richtungsvektorfeldes schreibt/verwendet? 

<|ref|>text<|/ref|><|det|>[[114, 809, 145, 826]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[114, 824, 864, 876]]<|/det|>
Zur Bestimmung der statischen Lösung muss gelten: \(0 = 1 - y^2 = (1-y)(1+y)\). Als Lösungen erhält man somit \(y_{s1}(x) = -1\) (Repellor und instabile Lösung) und \(y_{s2}(x) = 1\) (Attraktor und stabile Lösung).