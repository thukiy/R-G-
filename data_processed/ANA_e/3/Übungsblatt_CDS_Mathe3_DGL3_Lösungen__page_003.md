<|ref|>text<|/ref|><|det|>[[114, 81, 390, 100]]<|/det|>
Statische Lösungen: \(y_s(x) = 0\). 

<|ref|>text<|/ref|><|det|>[[114, 98, 857, 117]]<|/det|>
Nicht statische Lösungen mit der Methode der Trennung der Variablen bestimmen: 

<|ref|>equation<|/ref|><|det|>[[114, 116, 714, 404]]<|/det|>
\[
\begin{align*}
& y' = x^2 \cdot y^3 \quad |: y^3 \\
& \frac{1}{y^3} \cdot y' = x^2 \quad | \int \dots dx \\
& \int \frac{1}{y^3} \cdot y' dx = \int \frac{1}{y^3} dy = \int x^2 dx \\
& -\frac{1}{2y^2} = \frac{1}{3} x^3 + c \quad | \cdot (-2) \\
& \frac{1}{y^2} = -\frac{2}{3} x^3 - 2c = C - \frac{2}{3} x^3 \quad | \text{rez}(\dots) \\
& y^2 = \frac{1}{C - \frac{2}{3} x^3} \quad | \pm \sqrt{\dots} \\
& y(x) = \pm \sqrt{\frac{1}{C - \frac{2}{3} x^3}} = \pm \frac{1}{\sqrt{C - \frac{2}{3} x^3}} \quad c, C \in \mathbb{R}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 405, 583, 425]]<|/det|>
Reelle Lösungen existisieren genau dann, wenn gilt 

<|ref|>equation<|/ref|><|det|>[[114, 423, 595, 586]]<|/det|>
\[
\begin{align*}
& C - \frac{2}{3} x^3 > 0 \quad | + \frac{2}{3} x^3 \\
& \Leftrightarrow \quad C > \frac{2}{3} x^3 \quad | \cdot \frac{3}{2} \\
& \Leftrightarrow \quad \frac{3}{2} C > x^3 \quad | \sqrt[3]{ \dots } \\
& \Leftrightarrow \quad \sqrt[3]{\frac{3}{2} C} > x.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 585, 857, 604]]<|/det|>
Allgemeine Lösung durch Kombination der statischen und nicht statischen Lösung: 

<|ref|>equation<|/ref|><|det|>[[119, 617, 647, 692]]<|/det|>
\[
y(x) = \begin{cases} 0 & \text{für } x \in \mathbb{R} \\ \pm \frac{1}{\sqrt{C - \frac{2}{3} x^2}} & \text{für } x \in ]-\infty, \sqrt[3]{\frac{3}{2} C} \mid \text{mit } C \in \mathbb{R}. \end{cases}
\]

<|ref|>text<|/ref|><|det|>[[114, 697, 144, 714]]<|/det|>
e) 

<|ref|>text<|/ref|><|det|>[[114, 712, 415, 731]]<|/det|>
Statische Lösungen gibt es nicht. 

<|ref|>text<|/ref|><|det|>[[114, 729, 857, 748]]<|/det|>
Nicht statische Lösungen mit der Methode der Trennung der Variab len bestimmen: 

<|ref|>equation<|/ref|><|det|>[[114, 746, 780, 905]]<|/det|>
\[
\begin{align*}
& y' = 1 \cdot (1 + y^2) \quad | : (1 + y^2) \\
& \frac{1}{1 + y^2} \cdot y' = 1 \quad | \int \dots dx \\
& \Leftrightarrow \int \frac{1}{1 + y^2} \cdot y' dx = \int \frac{1}{1 + y^2} dy = \int 1 dx \\
& \Leftrightarrow \arctan(y) = x + c \quad | \tan(\dots) \\
& \Leftrightarrow y(x) = \tan(x + c) = \tan(x - C) \quad c, C \in \mathbb{R}
\end{align*}
\]

<|ref|>text<|/ref|><|det|> [[114, 907, 583, 926]]<|/det|>
Reelle Lösungen existisieren genau dann, wenn gilt