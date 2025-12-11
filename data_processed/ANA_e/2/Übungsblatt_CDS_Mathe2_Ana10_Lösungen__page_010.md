<|ref|>text<|/ref|><|det|>[[115, 85, 140, 100]]<|/det|>
c) 

<|ref|>text<|/ref|><|det|>[[115, 99, 728, 117]]<|/det|>
Es seien a, b, c die Kantenlängen. Dann lautet die Nebenbedingung 

<|ref|>equation<|/ref|><|det|>[[172, 120, 671, 158]]<|/det|>
\[
g(a, b, c) = \underbrace{2}_{\text{Geld}} \cdot \underbrace{4(a + b + c)}_{\text{Holz}} + \underbrace{3}_{\text{Geld}} \cdot \underbrace{2(ab + bc + ac)}_{\text{Stoff}} - \underbrace{50}_{\text{Geld}} = 0.
\]

<|ref|>text<|/ref|><|det|>[[120, 168, 210, 184]]<|/det|>
Damit gilt 

<|ref|>equation<|/ref|><|det|>[[289, 181, 555, 252]]<|/det|>
\[
\text{grad } g(a, b, c) = \begin{cases} 8 + 6b + 6c \\ 8 + 6a + 6c \\ 8 + 6a + 6b \end{cases}.
\]

<|ref|>text<|/ref|><|det|>[[120, 258, 206, 273]]<|/det|>
Weiter ist 

<|ref|>equation<|/ref|><|det|>[[359, 272, 485, 290]]<|/det|>
\[
f(a, b, c) = abc.
\]

<|ref|>text<|/ref|><|det|>[[120, 296, 303, 311]]<|/det|>
Nun ermitteln wir aus 

<|ref|>equation<|/ref|><|det|>[[176, 320, 670, 391]]<|/det|>
\[
\text{grad } f(a, b, c) + \lambda \text{grad } g(a, b, c) = \begin{cases} bc + \lambda(8 + 6b + 6c) \\ ac + \lambda(8 + 6a + 6c) \\ ab + \lambda(8 + 6a + 6b) \end{cases} \stackrel{!}{=} 0
\]

<|ref|>text<|/ref|><|det|>[[120, 393, 725, 424]]<|/det|>
die Werte \(a, b, c \in \mathbb{R}_+\). Wir subtrahieren die 2. Zeile von der 1. Zeile und erhalten 

<|ref|>equation<|/ref|><|det|>[[345, 426, 544, 443]]<|/det|>
\[
bc - ac + \lambda(6b - 6a) = 0
\]

<|ref|>equation<|/ref|><|det|>[[306, 459, 512, 477]]<|/det|>
\[
\iff (b - a)(c + 6\lambda) = 0
\]

<|ref|>equation<|/ref|><|det|>[[306, 481, 526, 516]]<|/det|>
\[
\iff \begin{cases} a = b \text{ oder } \lambda = -\frac{c}{6} \\ \end{cases}
\]

<|ref|>text<|/ref|><|det|>[[120, 522, 725, 553]]<|/det|>
Auf ähnliche Art und Weise (2. Zeile - 3. Zeile, 1. Zeile - 3. Zeile) bekommen wir 

<|ref|>equation<|/ref|><|det|>[[330, 550, 512, 630]]<|/det|>
\[
\begin{array}{l} b = c \text{ oder } \lambda = -\frac{a}{6}; \\ a = c \text{ oder } \lambda = -\frac{b}{6}. \end{array}
\]

<|ref|>text<|/ref|><|det|>[[120, 631, 546, 647]]<|/det|>
Es liegen jetzt verschiedene Fallunterscheidungen vor: 

<|ref|>text<|/ref|><|det|>[[127, 654, 720, 696]]<|/det|>
i) \(a = b\) und \(\lambda = -\frac{a}{6} = -\frac{b}{6}\). Daraus ergibt sich ein Widerspruch. Denn aus
\(ab + \lambda(8 + 6a + 6b) = 0\) resultiert 

<|ref|>equation<|/ref|><|det|>[[225, 707, 644, 740]]<|/det|>
\[
a^2 + \left(-\frac{a}{6}\right)(8 + 12a) = 0 \iff a = 0 \text{ oder } a = -\frac{8}{6}.
\]

<|ref|>text<|/ref|><|det|>[[120, 755, 715, 789]]<|/det|>
ii) \(b = c\) und \(\lambda = -\frac{b}{6} = -\frac{c}{6}\). Daraus ergibt sich ein analoger Widerspruch. 

<|ref|>text<|/ref|><|det|>[[120, 789, 718, 819]]<|/det|>
iii) \(a = c\) und \(\lambda = -\frac{a}{6} = -\frac{c}{6}\). Daraus ergibt sich ein analoger Widespruch.