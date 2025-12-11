<|ref|>text<|/ref|><|det|>[[119, 83, 875, 137]]<|/det|>
Die Urne enthält stets 10 Kugeln, nach der 1. Ziehung somit entweder 3 weiße und 7 schwarze Kugeln (wenn zunächst eine *weiße* Kugel gezogen wurde) oder je 5 weiße und schwarze Kugeln (wenn zunächst eine *schwarze* Kugel gezogen wurde). 

<|ref|>text<|/ref|><|det|>[[119, 137, 469, 156]]<|/det|>
Aus dem Ereignisbaum in Bild A-22 folgt: 

<|ref|>equation<|/ref|><|det|>[[119, 163, 525, 227]]<|/det|>
\[
\begin{align*}
\text{a)} \quad P(W) &= P(WW) + P(SW) = \\
&= \frac{4}{10} \cdot \frac{3}{10} + \frac{6}{10} \cdot \frac{5}{10} = \frac{42}{100} = 0,42
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[119, 239, 525, 302]]<|/det|>
\[
\begin{align*}
\text{b)} \quad P(WW \cup SS) &= P(WW) + P(SS) = \\
&= \frac{4}{10} \cdot \frac{3}{10}+ \frac{6}{10} \cdot \frac{5}{10} = \frac {42}{100} = 0,42
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[120, 313, 400, 347]]<|/det|>
\[
\text{c)} \quad P(WW) = \frac{4}{10} \cdot \frac{3}{10} = \frac{12}{100}
\]

<|ref|>equation<|/ref|><|det|>[[157, 353, 470, 393]]<|/det|>
\[
P = \frac{P(WW)}{P(WW \cup SS)} = \frac{12/100}{42/100} = \frac{2}{7}
\]

<|ref|>image<|/ref|><|det|>[[660, 138, 875, 355]]<|/det|>
 

<|ref|>sub_title<|/ref|><|det|>[[114, 411, 339, 429]]<|/det|>
## 8. Rohrleitungssystem 

<|ref|>text<|/ref|><|det|>[[114, 427, 877, 512]]<|/det|>
Das Rohrleitungssystem einer Erdölraffinerie besitze 500 Flanschverbindungen, von denen jede Verbindung aus zwei Einzelflanschen vom Typ F1 und F2 sowie einem Dichtungsring zwischen ihnen besteht. Es ist bekannt, dass 1% der Flansche vom Typ F1 und 1,5% derjenigen vom Typ F2 ungenügende Qualität haben. Ferner ist bei 2% der Dichtringe mangelnde Dichtungseigenschaft zu erwarten. 

<|ref|>text<|/ref|><|det|>[[114, 510, 875, 546]]<|/det|>
Wie viele absolut einwandfreie (d.h. ohne jeglichen Mangel) Flanschverbindungen im Rohrleitungssystem können wir erwarten? 

<|ref|>text<|/ref|><|det|>[[119, 560, 825, 614]]<|/det|>
Damit eine Flanschverbindung als absolut einwandfrei (Ereignis A) bezeichnet werden kann, müssen sowohl Einzelflansche als auch der Dichtungsring dieser Verbindung mangelfrei sein. 

<|ref|>equation<|/ref|><|det|>[[159, 627, 655, 646]]<|/det|>
\[
A_1 : \text{Ereignis, dass der Flansch vom Typ F1 einwandfrei ist.}
\]

<|ref|>equation<|/ref|><|det|>[[159, 649, 655, 668]]<|/det|>
\[
A_2 : \text{Ereignis, dass der Flansch vom Typ F2 einwandfrei ist.}
\]

<|ref|>equation<|/ref|><|det|>[[159, 671, 603, 690]]<|/det|>
\[
A_3 : \text{Ereignis, dass der Dichtungsring einwandfrei ist.}
\]

<|ref|>text<|/ref|><|det|>[[119, 703, 825, 738]]<|/det|>
Das Ereignis A, dass eine Flanschverbindung komplett einwandfrei ist, entspricht dem Durchschnitt aller drei Ereignisse: 

<|ref|>equation<|/ref|><|det|>[[159, 752, 308, 770]]<|/det|>
\[
A = A_1 \cap A_2 \cap A_3
\]

<|ref|>text<|/ref|><|det|>[[119, 784, 736, 803]]<|/det|>
Die Wahrscheinlichkeit für das Eintreten des Ereignisses A ist nach (9.26): 

<|ref|>equation<|/ref|><|det|>[[159, 816, 561, 836]]<|/det|>
\[
P(A) = P(A_1 \cap A_2 \cap A_3) = P(A_1) \cdot P(A_2) \cdot P(A_3)
\]

<|ref|>text<|/ref|><|det|>[[119, 840, 546, 859]]<|/det|>
Wahrscheinlichkeit für einwandfreien Flansch F1: 

<|ref|>equation<|/ref|><|det|>[[164, 871, 490, 892]]<|/det|>
\[
P(A_1) = 1 - P(\overline{A_1}) = 1 - 0,01 = 0,99
\]