<|ref|>sub_title<|/ref|><|det|>[[114, 81, 360, 99]]<|/det|>
## 3. Regressionsanalyse II 

<|ref|>text<|/ref|><|det|>[[114, 98, 830, 135]]<|/det|>
Bestimmen Sie nach der Gaußschen Methode der kleinsten Quadrate diejenige Exponentialfunktion vom Typ \(y = a \cdot e^{bx}\), die sich den vier Messpunkten 

<|ref|>table<|/ref|><|det|>[[114, 140, 664, 196]]<|/det|>
<table><tr><td>i</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>xi</td><td>0</td><td>1</td><td>2</td><td>3</td></tr><tr><td>yi</td><td>5,1</td><td>1,75</td><td>1,08</td><td>0,71</td></tr></table>

<|ref|>text<|/ref|><|det|>[[114, 202, 444, 220]]<|/det|>
in optimaler Weise anpasst (a &gt; 0). 

<|ref|>text<|/ref|><|det|>[[114, 218, 880, 303]]<|/det|>
Hinweis: Die Exponentialfunktion wird in der halblogarithmischen Darstellung durch die Gerade dargestellt \(v = cu + d\) (\(u = x, v = \ln y\), \(c = b\) und \(d = \ln a\)). Dabei geht der Punkt \(P_i(x_i, y_i)\) in den Punkt \(Q_i(u_i, v_i)\) über. Man bestimme daher zunächst die zu den Punkten \(Q_i\) gehörende Ausgleichgerade und daraus dann die Parameter \(a\) und \(b\) der Exponentialfunktion. 

<|ref|>image<|/ref|><|det|>[[124, 323, 400, 601]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[124, 593, 250, 610]]<|/det|>
\(v = cu + d\) 

<|ref|>table<|/ref|><|det|>[[124, 616, 576, 765]]<|/det|>
<table><tr><td>i</td><td>\(u_i = x_i\)</td><td>\(v_i = \ln y_i\)</td><td>\(u_i^2\)</td><td>\(u_i v_i\)</td></tr><tr><td>1</td><td>0</td><td>1,629 241</td><td>0</td><td>0</td></tr><tr><td>2</td><td>1</td><td>0,559 616</td><td>1</td><td>0,559 616</td></tr><tr><td>3</td><td>2</td><td>0,076 961</td><td>4</td><td>0,153 922</td></tr><tr><td>4</td><td>3</td><td>-0,342 490</td><td>9</td><td>-1,027 471</td></tr><tr><td>∑</td><td>6</td><td>1,923 328</td><td>14</td><td>-0,313 933</td></tr></table>

<|ref|>equation<|/ref|><|det|>[[124, 772, 411, 825]]<|/det|>
\[ \overline{u} = \frac{1}{4} \cdot \sum_{1}^{4} u_i = \frac{1}{4} \cdot 6 = 1,5 \]

<|ref|>equation<|/ref|><|det|>[[124, 825, 533, 870]]<|/det|>
\[ \overline{v} = \frac{1}{4} \cdot \sum_{1}^{4} v_i = \frac{1}{4} \cdot 1,923 328 = 0,480 832 \]