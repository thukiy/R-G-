<|ref|>text<|/ref|><|det|>[[122, 84, 688, 103]]<|/det|>
Damit haben wir die kritischen Stellen von \(f\) gefunden, diese sind 

<|ref|>equation<|/ref|><|det|>[[195, 112, 803, 134]]<|/det|>
\[P_1 := (0; -1), \quad P_2 := (0; 1), \quad P_3 := (-\sqrt{3}; 0) \quad \text{und} \quad P_4 := (\sqrt{3}; 0).\]

<|ref|>text<|/ref|><|det|>[[122, 146, 880, 200]]<|/det|>
Für die weitere Untersuchung der kritischen Stellen \(P_k = (x_k; y_k)\) mit \(k \in \{1, \ldots 4\}\) betrachten wir die zweiten, partiellen Ableitungen von \(f\) an diesen Stellen. Wir stellen die Ergebnisse in der folgenden Tabelle zusammen. 

<|ref|>table<|/ref|><|det|>[[165, 210, 802, 327]]<|/det|>
<table><tr><td>k</td><td>xk</td><td>yk</td><td>zk</td><td>fx,x</td><td>fy,y</td><td>fx,y</td><td>det(∇²f)</td><td>Typ:</td></tr><tr><td>1</td><td>0</td><td>-1</td><td>10</td><td>-2 &lt; 0</td><td>-6 &lt; 0</td><td>0</td><td>+12 &gt; 0</td><td>lok. Maximum</td></tr><tr><td>2</td><td>0</td><td>+1</td><td>6</td><td>+2 &gt; 0</td><td>+6 &gt; 0</td><td>0</td><td>+12 &gt; 0</td><td>lok. Minimum</td></tr><tr><td>3</td><td>-√3</td><td>0</td><td>8</td><td>0</td><td>0</td><td>-2√3</td><td>-12 &lt; 0</td><td>Sattel-Punkt</td></tr><tr><td>4</td><td>+√3</td><td>0</td><td>8</td><td>0</td><td>0</td><td>+2√3</td><td>-12 &lt; 0</td><td>Sattel-PunKt</td></tr></table>

<|ref|>text<|/ref|><|det|>[[115, 330, 145, 347]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[115, 345, 515, 363]]<|/det|>
Gradient und Hesse-Matrix ergeben sich zu 

<|ref|>equation<|/ref|><|det|>[[117, 362, 880, 406]]<|/det|>
\[\nabla f = \begin{bmatrix} f_{,x} \\ f_{,y} \end{bmatrix} = \begin{bmatrix} 6xy \\ 3x^2 + 3y^2 - 27 \end{bmatrix} \quad \text{und} \quad \nabla^2 f = \begin{bmatrix} f_{,x,x} & f_{,x,y} \\ f_{,y,x} & f_{,y,y} \end{bmatrix} = \begin{bmatrix} 6y & 6x \\ 6x & 6y \end{bmatrix}\]

<|ref|>text<|/ref|><|det|>[[115, 404, 420, 422]]<|/det|>
Für kritische Stellen muss gelten 

<|ref|>equation<|/ref|><|det|>[[117, 421, 720, 475]]<|/det|>
\[\nabla f = 0 \Leftrightarrow \begin{cases} 6xy = 0 \\ 3x^2 + 3y^2 - 27 = 0 \end{cases} \Leftrightarrow \begin{cases} \text{I:} & xy = 0 \\ \text{II:} & x^2 + y^2 - 9 = 0. \end{cases}\]

<|ref|>text<|/ref|><|det|>[[115, 478, 713, 497]]<|/det|>
Aus Gleichung I folgt, dass entweder x = 0 oder y = 0 gelten muss. 

<|ref|>text<|/ref|><|det|>[[115, 496, 455, 515]]<|/det|>
Fall 1: \(x = 0\). Aus der Gleichung II 

<|ref|>equation<|/ref|><|det|>[[362, 527, 733, 550]]<|/det|>
\[y^2 - 9 = 0 \Leftrightarrow y^2 = 9 \Leftrightarrow y \in \{-3, 3\}.\]

<|ref|>text<|/ref|><|det|>[[115, 562, 454, 581]]<|/det|>
Fall 2: \(y = 0\). Aus der Gleichung II 

<|ref|>equation<|/ref|><|det|>[[357, 593, 737, 615]]<|/det|>
\[x^2 - 9 = 0 \Leftrightarrow x^2 = 9 \Leftrightarrow x \in \{-3, 3\}.\]

<|ref|>text<|/ref|><|det|>[[115, 631, 739, 651]]<|/det|>
Damit haben wir die kritischen Stellen von \(f\) gefunden, diese sünd 

<|ref|>equation<|/ref|><|det|>[[216, 664, 848, 686]]<|/det|>
\[P_1 := (0; -3), \quad P_2 := (0; 3), \quad P_3 := (-3; 0) \quad \text{und} \quad P_4 := (3; 0).\]

<|ref|>text<|/ref|><|det|>[[122, 688, 880, 741]]<|/det|>
Für die weitere Untersuchung der kritischen Stellen \(P_k = (x_k ; y_k)\) mit \(k \in \{1, \ldots 4\}\) betrachten wir eine zweiten, partiellen Ableitungen von \(f\) an diesen Stellen. Wir stellen die Ergebnisse im folgenden Tabelle zusammen. 

<|ref|>table<|/ref|><|det|>[[165, 752, 792, 865]]<|/det|>
<table><tr><td>k</td><td>xk</td><td>yk</td><td>zk</td><td>f_x,x</td><td>f_y,y</td><td>f_x,y</td><td>det(∇²f)</td><td>Typ:</td></tr><tr><td>1</td><tr><td>2</td><td>0</td><td>-3</td><td>58</td><td>-18 &lt; 0</td><td>-18 &lt; 0</td><td>0</td><td>+324 &gt; 0</td><td>lok. Maximum</td></tr><tr><td>3</td><td>-3</td><td>0</td><td>-50</td><td>+18 &gt; 0</td><td>+18 &gt; 0</td><td>0</td><td>+324 &gt; 0</td><td>lok. Minimum</td></tr><tr><td>4</td><td>+3</td><td>0</td><td>4</td><td>0</td><td>0</td><td>-18</td><td>-324 &lt; 0</td><td>Sattel-Punkt</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>0</td><td>+18</td><td>-324 &lt; 0</td><td>Sattel-Punkt</td><td></td></tr></tr></table>