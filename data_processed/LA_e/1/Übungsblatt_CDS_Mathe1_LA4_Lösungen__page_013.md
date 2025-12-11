<|ref|>equation<|/ref|><|det|>[[176, 82, 457, 120]]<|/det|>
\[3x_3 - x_4 = 4 \Rightarrow x_3 = \frac{4 + x_4}{3}\]

<|ref|>equation<|/ref|><|det|>[[120, 120, 642, 156]]<|/det|>
\[2x_1 + x_2 + 2x_4 = 6 \Rightarrow x_1 = \frac{6 - x_2 - 2x_4}{2} = 3 - \frac{x_2}{2} - x_4\]

<|ref|>sub_title<|/ref|><|det|>[[114, 156, 444, 175]]<|/det|>
## 2. Variante: Gauß-Jordan-Verfahren 

<|ref|>table<|/ref|><|det|>[[115, 174, 878, 285]]<|/det|>
<table><tr><td></td><td>[2]</td><td>1</td><td>0</td><td>2</td><td>6</td></tr><tr><td>2</td><td>4</td><td>2</td><td>3</td><td>3</td><td>16</td></tr><tr><td>-1</td><td>-2</td><td>-1</td><td>6</td><td>-4</td><td>2</td></tr><tr><td>-4</td><td>-8</td><td>-4</td><td>9</td><td>-11</td><td>-12</td></tr><tr><td>1</td><td>2</td><td>1</td><td>-3</td><td>3</td><td>2</td></tr></table>

<|ref|>table<|/ref|><|det|>[[464, 174, 661, 285]]<|/det|>
<table><tr><td></td><td>[2]</td><td>1</td></tr><tr><td>0</td><td>[3]</td><td>-1</td></tr><tr><td>0</td><td>0</td><td>6</td></tr><tr><td>0</td><td>9</td><td>-3</td></tr><tr><td>0</td><td>-3</td><td>1</td></tr></table>

<|ref|>table<|/ref|><|det|>[[697, 174, 880, 285]]<|/det|>
<table><tr><td></td><td>[2]</td><td>1</td><tr><td>0</td><td>[3]</td><td>-1</td></tr><tr><td>0</td><td>00</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>0<td>0</td><td>0</td></td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0<td>0</td></td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>0<td>0</td></td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr></tr></table>

<|ref|>table<|/ref|><|det|>[[114, 291, 550, 344]]<|/det|>
<table><tr><td></td><td>[2]</td><td>1</td><td>0</td></tr><tr><td>0</td><td>[3]</td><td>-1</td><td>4</td></tr><tr><td>0</td><td>0</td><td>[3]</td><td>-1</td></tr><tr><td>0</td><td>0<td>0</td><td>0</td></td></tr><tr><td>0</td><td>0</td><td>0<td>0</td></td></tr><tr><td>0</td><td>0</td><td>0<td>0</td></td></tr></table>

<|ref|>text<|/ref|><|det|>[[114, 348, 277, 366]]<|/det|>
Rang und Defekt: 

<|ref|>equation<|/ref|><|det|>[[114, 364, 400, 382]]<|/det|>
\[n_R = 2, n_D = n_V - n_R = 4 - 2 = 2.\]

<|ref|>text<|/ref|><|det|>[[114, 380, 593, 398]]<|/det|>
Pivot-Variablen: \(x_1\) und \(x_3\), freie Parameter: \(x_2\) und \(x_4\). 

<|ref|>text<|/ref|><|det|>[[114, 396, 720, 414]]<|/det|>
Es ergibt sich durch Einsetzen in die 2. und 1. Zeile der Stufenform: 

<|ref|>equation<|/ref|><|det|>[[174, 415, 637, 455]]<|/det|>
\[x_3 - \frac{1}{3} \cdot x_4 = \frac{4}{3} \Rightarrow x_3 = \frac{4}{3} + \frac{x_4}{3} = \frac{4 + x_4}{3}\]

<|ref|>equation<|/ref|><|det|>[[120, -2, 880, 504]]<|/det|>
\[x_1 + \frac{1}{2} \cdot x_2 + x_4 = 3 \Rightarrow x_1 = 3 - \frac{x_2}{2} - x_4.\]

<|ref|>text<|/ref|><|det|>[[114, 505, 144, 523]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[114, 521, 460, 540]]<|/det|>
Mit Hilfe des Gauß-Jordan-Verfahrens 

<|ref|>table<|/ref|><|det|>[[120, 538, 820, 620]]<|/det|>
<table><tr><td></td><td>[2]</td><td>3</td><td>-1</td><td>-3</td><td></td><td>[2]</td><td>3</td><td>-1</td><td>-3</td></tr><tr><td>-1</td><td>-2</td><td>1</td><td>5</td><td>7</td><td>⇔</td><td>0</td><td>4</td><td>4</td><td>4</td></tr><tr><td></td><td>0</td><td>2</td><td>2</td><td>p</td><td></td><td>0</td><td>2</td><td>2</td><td>p</td></tr></table>

<|ref|>table<|/ref|><|det|>[[464, 538, 760, 620]]<|/det|>
<table><tr><td></td><td>[2]</td><td>3</td></tr><tr><td>0</td><td>[1]</td><td>1</td></tr><tr><td>0</td><td>0</td><td>2</td></tr><tr><td>0</td><td>0</td><td>2</td></tr></table>

<|ref|>table<|/ref|><|det|>[[137, 624, 833, 692]]<|/det|>
<table><tr><td>3</td><td>[2]</td><td>3</td><td>-1</td><td>-3</td><td></td></tr><tr><td>⇔</td><td>0</td><td>[1]</td><td>1</td><td>1</td><td>⇔</td></tr><tr><td></td><td>0</td><td>0</td><td>0</td><td>p - 2</td><td></td></tr></table>

<|ref|>table<|/ref|><|det|>[[464, 624, 830, 692]]<|/det|>
<table><tr><td></td><td>[2]</td><td>0</td><td>-4</td><td>-6</td><td></td></tr><tr><td></td><td>0</td><td>[1]</td><td>1</td><td>1</td><td>⇔</td><td>0</td><td>[1]</td><td>1</td></tr><tr><td></td><td>0</td><td>0</td><td>0</td><td>p - 2<td></td><td>0</td><td>0</td><td>0</td></td></tr></table>

<|ref|>text<|/ref|><|det|>[[114, 696, 277, 714]]<|/det|>
Rang und Defekt: 

<|ref|>equation<|/ref|><|det|>[[114, 712, 395, 730]]<|/det|>
\[n_R = 2, n_D = n_V - n_R = -3 - 2 = 1.\]

<|ref|>text<|/ref|><|det|>[[114, 728, 515, 747]]<|/det|>
Pivot-Variablen: \(x\) und \(y\), freier Parameter: \(z\). 

<|ref|>text<|/ref|><|det|>[[114, 754, 234, 772]]<|/det|>
1. Fall: \(p \neq 2\) 

<|ref|>text<|/ref|><|det|>[[114, 770, 789, 807]]<|/det|>
Die Verträglichkeit in der dritten Zeile ist nicht erfüllt und somit gibt es keine Lösungen, d. h. \(L = \emptyset\). 

<|ref|>text<|/ref|><|det|>[[114, 812, 234, 831]]<|/det|>
2. Fall: \(p = 2\) 

<|ref|>text<|/ref|><|det|>[[114, 829, 473, 847]]<|/det|>
Die reduzierte Stufenform ergibt sich zu 

<|ref|>table<|/ref|><|det|>[[120, 851, 730, 920]]<|/det|>
<table><tr><td></td><td>[1]</td><td>0</td><td>-2</td><td>-3</td><td></td><td>[1]</td><td>0</td><td>-2</td><td>-3</td></tr><tr><td>0</td><td>[1]</td><td>1</td><td>1</td><td>1</td><td>⇔</td><td>0</td><td>[1]</td></tr><tr><td>0</td><td>0</td><td>0</td><td>2 - 2</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>