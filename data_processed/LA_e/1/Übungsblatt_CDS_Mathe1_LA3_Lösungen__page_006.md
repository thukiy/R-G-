<|ref|>text<|/ref|><|det|>[[115, 81, 390, 100]]<|/det|>
a*5 min + b*15 min = 480 min 

<|ref|>text<|/ref|><|det|>[[115, 114, 400, 133]]<|/det|>
Mit Hilfe des Gauß-Verfahrens: 

<|ref|>table<|/ref|><|det|>[[120, 133, 784, 228]]<|/det|>
<table><tr><td>18 min</td><td>6.0 min</td><td>480 min</td><td>3</td><td>1</td><td>80</td><td>3</td><td>1</td><td>96</td><td>3</td><td>1</td><td>80</td><td>3</td><td>1</td><td>96</td></tr><tr><td>5.0 min</td><td>15 min</td><td>480 min</td><td>1</td><td>3</td><td>96</td><td>1</td><td>3</td><td>1</td><td>80</td><td>1</td><td>3</td><td>1</td><td>80</td><td>1</td><td>-208</td></tr><tr><td>[1]</td><td>3</td><td>96</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0</td><td>[1]</td><td>26</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td><td></td><td></td><td></td><td></td></td></tr></tr></table>

<|ref|>text<|/ref|><|det|>[[120, 235, 433, 252]]<|/det|>
Durch **Rückwärtseinsetzen** erhalten wir 

<|ref|>equation<|/ref|><|det|>[[253, 257, 435, 275]]<|/det|>
\[1 \cdot b = 26 \Rightarrow b = 26\]

<|ref|>equation<|/ref|><|det|>[[200, 278, 715, 296]]<|/det|>
\[1 \cdot a + 3 \cdot b = 21 \Rightarrow a = 96 - 3 \cdot b = 96 - 3 \cdot 26 = 96 - 78 = 18.\]

<|ref|>text<|/ref|><|det|>[[115, 311, 468, 330]]<|/det|>
Mit Hilfe des Gauß-Jordan-Verfahrens: 

<|ref|>table<|/ref|><|det|>[[120, 330, 789, 425]]<|/det|>
<table><tr><td>18 min</td><td>6.0 min</td><td>480 min<td>3</td><td>1</td><td>80</td><td>3</td><td>1</td><td>96</td><td>1</td><td>3</td><td>96</td><td>1</td><td>80</td><td>3</td><td>1</td><td>96</td></td></tr><tr><td>5.0 min</td><td>15 min</td><td>480 min<td>1</td><td>3</td><td>96</td><td>1</td><td>3</td><td>1</td><td>96</td><td>1</td><td>3</td><td>1</td><td>96</td><td>1</td></td></tr><tr><td>3</td><td>[1]</td><td>3</td><td>96</td><td>[1]</td><td>0</td><td>18</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><tr><td>0</td><td>[1]</td><td>26</td><td></td><td>0</td><td>[1]</td><td>26</td><td></td><td></td><td></td><td></td></tr></tr></table>

<|ref|>text<|/ref|><|det|>[[115, 441, 725, 460]]<|/det|>
## 5. Eindeutig lösbare lineare Gleichungssysteme für 3 Variablen 

<|ref|>text<|/ref|><|det|>[[115, 459, 847, 494]]<|/det|>
Bringen Sie die linearen Gleichungssysteme in ein Gauß-Schema und bestimmen Sie die Lösung mit Hilfe des Gauß- oder Gauß-Jordan-Verfahrens. 

<|ref|>equation<|/ref|><|det|>[[115, 492, 551, 543]]<|/det|>
\[a) 2x - 3y + z = 3 \quad b) 2x + z = 6y \\
-x + 3y - 2z = 0 \quad 6x + 3y = 2 + 2z \\
3x - y + 5z = 1 \quad 2x + 3y + 1 = 3z\]

<|ref|>text<|/ref|><|det|>[[115, 558, 148, 575]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[120, 572, 572, 590]]<|/det|>
**Variante 1:** Wir wenden das Gauss-Verfahren an. Es gilt 

<|ref|>table<|/ref|><|det|>[[144, 595, 690, 770]]<|/det|>
<table><tr><td>2 -3</td><td>1</td><td>3</td><td>-1</td><td>3</td><td>-2</td><td>0</td><td>[1]</td><td>-3</td><td>2</td><td>0</td></tr><tr><td>-1</td><td>3</td><td>-2</td><td>0</td><td>2</td><td>-3</td><td>1</td><td>3</td><td>2</td><td>-3</td><td>1</td></tr><tr><td>3</td><td>-1</td><td>5</td><td>1</td><td>3</td><td>-1</td><td>5</td><td>1</td><td>3</td><td>-1<td>5</td></td></tr><tr><td>[1]</td><td>-3</td><td>2</td><td>0</td><td>[1]</td><td>-3</td><td>2</td><td>0<td>[1]</td><td>-3</td><td>2</td></td></tr><tr><td>0</td><td>3</td><td>-3</td><td>3</td><td>0</td><td>[1]</td><td>-1</td><td>1</td><td>0</td><td>[1]</td><td>-1</td></tr><tr><td>0</td><td>8</td><td>-1</td><td>1</td><td>8</td><td>0</td><td>8</td><td>-1</td><td>1</td><td>0</td><td>7</td></tr><tr><td>[1]</td><td>-3</td><td>2</td><td>0</td><td>0</td><td>[1]</td><td>-3</td><td>2</td><td>0</td><td>[1]<td>-3</td></td></tr><tr><td>0</td><td>[1]</td><td>-1</td><td>1</td><td>0</td><td>0</td><td>[1]</td><td>-1</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>[1]</td><td>-1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>7</td><td>-7</td></tr></table>

<|ref|>text<|/ref|><|det|>[[144, 801, 435, 819]]<|/det|>
Durch **Rückwärtseinsetzen** finden wir 

<|ref|>equation<|/ref|><|det|>[[430, 825, 495, 841]]<|/det|>
\[z = -1\]

<|ref|>equation<|/ref|><|det|>[[310, 845, 605, 863]]<|/det|>
\[y - z = 1 \Rightarrow y = 1 + z = 1 - 1 = 0\]

<|ref|>equation<|/ref|><|det|>[[261, 865, 686, 884]]<|/det|>
\[x - 3y + 2z = 0 \Rightarrow x = 3y - 2z = 3 \cdot 0 - 2(-1) = 2.\]