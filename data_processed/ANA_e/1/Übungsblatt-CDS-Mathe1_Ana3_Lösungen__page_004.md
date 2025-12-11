<|ref|>text<|/ref|><|det|>[[91, 65, 890, 102]]<|/det|>
f) Jede monotone und beschränkte Folge ist gemäss Theorie konvergent. Es kann daher keine Folge geben, welche sowohl monoton steigend und beschränkt als auch divergent ist. 

<|ref|>sub_title<|/ref|><|det|>[[75, 128, 500, 148]]<|/det|>
5. Aussagen über die Konvergenz von Folgen 

<|ref|>table<|/ref|><|det|>[[75, 155, 888, 344]]<|/det|>
<table><tr><td>Welche der folgenden Aussagen sind wahr und welche falsch?</td><td>wahr</td><td>falsch</td></tr><tr><td>a) Jede konvergente, reelle Zahlenfolge ist nach unten beschränkt.</td><td>●</td><td>○</td></tr><tr><td>b) Jede konvergente, monotone, reelle Zahlenfolge ist streng monoton.</td><td>○</td><td>●</td></tr><tr><td>c) Die Folge \(a_n := n - n^3\) konvergiert gegen \(-\infty\).</td><td>○</td><td>●</td></tr><tr><td>d) Ist eine reelle Zahlenfolge streng monoton und beschränkt, dann ist sie konvergent.</td><td>●</td><td>○</td></tr><tr><td>e) Gilt für alle Folgeglieder \(a_n\) einer reellen Zahlenfolge dass \(0 < a_n < \frac{1}{n^3}\), dann konvergiert \(a_n\) gegen Null.</td><td>●</td><td>○</td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[75, 392, 454, 410]]<|/det|>
6. Konvergenzverhalten und Grenzwerte 

<|ref|>text<|/ref|><|det|>[[75, 408, 888, 446]]<|/det|>
Wir bestimmen in jeder Teilaufgabe, ob die gegebene Folge divergiert oder konvergiert und berechnen in letzterem Fall den Grenzwert. 

<|ref|>text<|/ref|><|det|>[[91, 450, 343, 469]]<|/det|>
a) Wir betrachten die Folge 

<|ref|>equation<|/ref|><|det|>[[443, 477, 888, 514]]<|/det|>
\[a_n := \frac{3}{n+2}. \qquad (18)\]

<|ref|>text<|/ref|><|det|>[[117, 522, 740, 542]]<|/det|>
Wir zeigen zwei Varianten, um das Verhalten der Folge zu untersuchen. 

<|ref|>text<|/ref|><|det|>[[117, 545, 888, 581]]<|/det|>
**Variante 1:** Durch Ausklammern in Zähler und Nenner eines Faktors \(n\) und Kürzen erhalten wir 

<|ref|>equation<|/ref|><|det|>[[142, 586, 888, 631]]<|/det|>
\[a_n = \frac{3}{n+2} = \frac{n \cdot \frac{3}{n}}{n \cdot \left(\frac{n}{n} + \frac{2}{n}\right)} = \frac{\frac{3}{n}}{1 + \frac{2}{n}} \xrightarrow{n \to \infty} \frac{0}{1+0} = 0. \qquad (19)\]

<|ref|>text<|/ref|><|det|>[[117, 640, 388, 659]]<|/det|>
**Variante 2:** Offensichtlich gilt 

<|ref|>equation<|/ref|><|det|>[[481, 672, 888, 692]]<|/det|>
\[0 \le a_n \qquad (20)\]

<|ref|>text<|/ref|><|det|>[[142, 703, 714, 722]]<|/det|>
und durch Abschätzen nach oben erhalten wir für alle \(n \ge 1\), dass 

<|ref|>equation<|/ref|><|det|>[[142, 732, 888, 770]]<|/det|>
\[a_n = \frac{3}{n+2} \le \frac{3}{n} = 3 \cdot \frac{1}{n} \xrightarrow{n \to \infty} 3 \cdot 0 = 0. \qquad (21)\]

<|ref|>text<|/ref|><|det|>[[117, 780, 635, 799]]<|/det|>
Die Folge konvergiert demnach gegen den Grenzwert \(a = 0\). 

<|ref|>text<|/ref|><|det|>[[91, 810, 494, 829]]<|/det|>
b) Durch Abschätzen nach unten erhalten wir 

<|ref|>equation<|/ref|><|det|>[[117, 839, 888, 877]]<|/det|>
\[a_n := \frac{n+2}{3} \ge \frac{n}{3} = \frac{1}{3} \cdot n \xrightarrow{n \to \infty} \infty. \qquad (22)\]

<|ref|>text<|/ref|><|det|>[[117, 884, 700, 903]]<|/det|>
Die Folge ist offenbar nach oben unbeschränkt und somit divergent.