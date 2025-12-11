<|ref|>text<|/ref|><|det|>[[120, 83, 820, 115]]<|/det|>
Übergang von der Zufallsvariablen \(X\) zur standardnormalverteilten Zufallsvariablen \(U = \frac{X - \mu}{\sigma} = \frac{X - 80}{0,03}\) 

<|ref|>text<|/ref|><|det|>[[120, 128, 607, 147]]<|/det|>
a) \(x_u \le X \le x_o\) Der Durchmesser liegt im Toleranzbereich (Bild K-9): 

<|ref|>equation<|/ref|><|det|>[[140, 150, 876, 230]]<|/det|>
\[ 
\begin{align*} 
P(x_u \le X \le x_o) &= P(79,91 \le X \le 80,06) = P\left(\frac{79,91 - 80}{0,03} \le U \le \frac{80,06 - 80}{0,03}\right) = P(-3 \le U \le 2) = \\
&= \Phi(2) - \Phi(-3) = \Phi(2) - [1 - \Phi(3)] = \Phi(2) - 1 + \Phi(3) = \Phi(2) + \Phi(3) - 1 = \\
&= 0,9772 + 0,9987 - 1 = 0,9759 \approx 97,6\% 
\end{align*} 
\]

<|ref|>text<|/ref|><|det|>[[139, 247, 872, 275]]<|/det|>
Folgerung: Mit einer hohen Wahrscheinlichkeit von rund 97,6% sind die Bohrungen qualitätsgerecht, liegen also im vorgegebenen Toleranzbereich. 

<|ref|>text<|/ref|><|det|>[[120, 280, 595, 299]]<|/det|>
b) \(X < x_u\) Der Durchmesser fällt zu klein aus (Nachbohrung): 

<|ref|>equation<|/ref|><|det|>[[144, 304, 880, 365]]<|/det|>
\[ 
\begin{align*} 
P(X < x_u) &= P(X < 79,91) = P\left(U < \frac{79,91 - 80}{0,03}\right) = P(U < -3) = \Phi(-3) = 1 - \Phi(3) = \\
&= 1 - 0,9987 = 0,0013 \cong 0,13\% 
\end{align*} 
\]

<|ref|>text<|/ref|><|det|>[[139, 378, 583, 395]]<|/det|>
Folgerung: Eine Nachbohrung wird äußerst selten nötig sein! 

<|ref|>text<|/ref|><|det|>[[120, 403, 580, 422]]<|/det|>
c) \(X > x_o\) Der Durchmesser fällt zu groß aus (Ausschussware): 

<|ref|>equation<|/ref|><|det|>[[144, 427, 875, 487]]<|/det|>
\[ 
\begin{align*} 
P(X > x_o) &= P(X > 80,06) = P\left(U > \frac{80,06 - 80}{0,03}\right) = P(U > 2) = 1 - P(U \le 2) = 1 - \Phi(2) = \\
&= 1 - 0,9772 = 0,0228 \approx 2,3\% 
\end{align*} 
\]

<|ref|>text<|/ref|><|det|>[[139, 499, 580, 514]]<|/det|>
Bei einer Serienproduktion beträgt der Ausschussanteil rund 2,3%. 

<|ref|>sub_title<|/ref|><|det|>[[117, 534, 296, 552]]<|/det|>
## 12. Weinabfüllung 

<|ref|>text<|/ref|><|det|>[[117, 551, 877, 620]]<|/det|>
In einem Weingut wird auf einer automatischen Abfüllanlage Wein in 0,75-Liter-Flaschen gefüllt. Das Abfüllvolumen X kann dabei nach den Angaben des Herstellers als eine normalverteilte Zufallsvariable mit dem Mittelwert \(m = 0,75\) l = 750 cm³ und der Standardabweichung \(\sigma = 20\) cm³ angenommen werden: 

<|ref|>text<|/ref|><|det|>[[117, 618, 830, 653]]<|/det|>
a) Wie gross ist die Wahrscheinlichkeit dafür, dass eine abgefüllte Weinflasche weniger als 730 cm³ Wein enthält? 

<|ref|>text<|/ref|><|det|>[[117, 651, 844, 686]]<|/det|>
b) Berechnen Sie die Wahrscheinlichkeit, dass das abgefüllte Weinvolumen vom Sollwert (Mittelwert) um maximal 2% (nach oben bzw. unten) abweicht. 

<|ref|>equation<|/ref|><|det|>[[117, 702, 330, 738]]<|/det|>
\[ U = \frac{X - \mu}{\sigma} = \frac{X - 750}{20} \]

<|ref|>equation<|/ref|><|det|>[[117, 748, 875, 767]]<|/det|>
\[ a) P(X < 730) = P(U < -1) = \phi(-1) = 1 - \phi(1) = 1 - 0,8413 = 0,1587 \approx 15,9\% \]

<|ref|>equation<|/ref|><|det|>[[117, 776, 707, 795]]<|/det|>
\[ b) \text{Abweichung: } 2\% \text{ von } 750 \text{ cm}^3 = 15 \text{ cm}^3 \Rightarrow 735 \le X \le 765 \]

<|ref|>equation<|/ref|><|det|>[[154, 805, 740, 846]]<|/det|>
\[ 
\begin{align*} 
P(735 \le X \le 765) &= P(-0,75 \le U \le 0,75) = 2 \cdot \phi(0,75) - 1 = \\
&= 2 \cdot 0,7734 - 1 = 0,5468 \approx 54,7\% 
\end{align*} 
\]