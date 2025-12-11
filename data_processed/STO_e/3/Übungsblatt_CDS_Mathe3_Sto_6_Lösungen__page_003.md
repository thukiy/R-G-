<|ref|>text<|/ref|><|det|>[[120, 85, 629, 104]]<|/det|>
a) *Additionssatz* für Mittelwerte bzw. Varianzen verwenden: 

<|ref|>equation<|/ref|><|det|>[[157, 117, 644, 137]]<|/det|>
\[
\mu = \mu_1 + \mu_2 + \mu_3 = (200 + 120 + 180) \Omega = 500 \Omega
\]

<|ref|>equation<|/ref|><|det|>[[157, 147, 720, 170]]<|/det|>
\[
\sigma^2 = \sigma_1^2 + \sigma_2^2 + \sigma_3^2 = (4 + 1 + 4) \Omega^2 = 9 \Omega^2; \quad \sigma = 3 \Omega
\]

<|ref|>text<|/ref|><|det|>[[120, 183, 875, 203]]<|/det|>
b) Übergang von der Zufallsvariablen \(R\) zur standardnormalverteilten Zufallsvariablen \(U\): 

<|ref|>equation<|/ref|><|det|>[[157, 206, 616, 245]]<|/det|>
\[
U = \frac{R - \mu}{\sigma} = \frac{R - 500}{3} \quad \Rightarrow \quad |R - 500| = 3 |U|
\]

<|ref|>equation<|/ref|><|det|>[[157, 251, 625, 273]]<|/det|>
\[
|R - 500| \le c \quad \Rightarrow \quad 3 |U| \le c \quad \Rightarrow \quad |U| \le c/3
\]

<|ref|>equation<|/ref|><|det|>[[157, 278, 755, 315]]<|/det|>
\[
P(|R - 500| \le c) = P\left(|U| \le \frac{c}{3}\right) = 2 \cdot \phi\left(\frac{c}{3}\right) - 1 = 0,95 \quad \Rightarrow
\]

<|ref|>equation<|/ref|><|det|>[[157, 316, 660, 350]]<|/det|>
\[
\phi\left(\frac{c}{3}\right) = 0,975 \quad \Rightarrow \quad \frac{c}{3} = u_{0,975} = 1,960 \quad c = 5,88
\]

<|ref|>equation<|/ref|><|det|>[[157, 352, 477, 371]]<|/det|>
\[
Lösung: 494,12 \Omega \le R \le 505,88 \Omega
\]

<|ref|>sub_title<|/ref|><|det|>[[114, 388, 285, 406]]<|/det|>
5. Transformator 

<|ref|>text<|/ref|><|det|>[[114, 405, 825, 460]]<|/det|>
Der Kern eines Transformators wird schichtweise aus Blechen der Dicke X und
Zwischenlagen der Dicke Y aufgebaut. X und Y seien dabei normalverteilte
Zufallsgrössen mit den folgenden Parametern (Kennwerten): 

<|ref|>equation<|/ref|><|det|>[[114, 457, 450, 475]]<|/det|>
\[
X: E(X) = \mu_X = 0,6 \text{ mm}, \sigma_X = 0,03 \text{ mm}
\]

<|ref|>equation<|/ref|><|det|>[[114, 473, 465, 492]]<|/det|>
\[
Y: E(Y) = \mu_Y = 0,05 \text{ mm}, \sigma_Y = 0,01 \text{ mm}
\]

<|ref|>text<|/ref|><|det|>[[114, 490, 833, 558]]<|/det|>
Der Kern bestehe aus insgesamt 100 Blechen und somit 99 Zwischenlagen. Die
einzelnen Schichtdicken werden dabei als völlig unabhängig voneinander
angesehen. Bestimmen Sie die Wahrscheinlichkeitsverteilung der Dicke Z
des Transformatorkerns. 

<|ref|>image<|/ref|><|det|>[[315, 556, 680, 720]]<|/det|>