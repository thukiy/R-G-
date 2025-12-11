<|ref|>sub_title<|/ref|><|det|>[[33, 15, 770, 68]]<|/det|>
Integralrechnung – Anwendung 

<|ref|>text<|/ref|><|det|>[[50, 90, 501, 118]]<|/det|>
bisher : • Berechnung von Flächen 

<|ref|>text<|/ref|><|det|>[[177, 130, 686, 158]]<|/det|>
• Berechnung Volumen von Rotationswörtern 

<|ref|>sub_title<|/ref|><|det|>[[23, 188, 435, 215]]<|/det|>
Bogenlänge einer ebenen Kurve 

<|ref|>image<|/ref|><|det|>[[88, 227, 400, 386]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[515, 247, 910, 272]]<|/det|>
gesucht : dünge von f(x) zwischen 

<|ref|>equation<|/ref|><|det|>[[627, 287, 816, 310]]<|/det|>
\(x = a\) und \(x = b\)

<|ref|>text<|/ref|><|det|>[[44, 404, 840, 432]]<|/det|>
→ Annäherung von Bogen PQ durch Tangente f(x) in P ergibt 

<|ref|>text<|/ref|><|det|>[[102, 443, 380, 468]]<|/det|>
Geradenabschnitt PQ' 

<|ref|>text<|/ref|><|det|>[[44, 479, 615, 508]]<|/det|>
→ Pythagoras : (ds)² = (dx)² + (dy)² 

<|ref|>equation<|/ref|><|det|>[[390, 512, 888, 625]]<|/det|>
\[ 
\begin{align*}
ds^2 &= (dx)^2 + (dy)^2 \\
&= (dx)^2 + (dy)^2 \cdot \frac{(dx)^2}{(dx)^2} \\
&= (dx)^2 \cdot (1 + \frac{(dy)^2}{(dx)^2}) \\
&= (\frac{dy}{dx})^2 = (y'(x))^2 = (f'(x))^2
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[150, 612, 481, 642]]<|/det|>
\(\Rightarrow ds = dx \sqrt{1 + (f'(x))^2}\)

<|ref|>text<|/ref|><|det|>[[44, 670, 571, 707]]<|/det|>
→ Bogenlänge : \(s = a\sqrt{1 + (f'(x))^2} dx\) 

<|ref|>text<|/ref|><|det|>[[23, 752, 790, 781]]<|/det|>
Bsp : • dünge zwischen \(x=3\) und \(x=8\) von \(f(x) = \frac{2}{3}\sqrt{x^3}\) 

<|ref|>equation<|/ref|><|det|>[[186, 787, 485, 820]]<|/det|>
\(f' = \frac{2}{3} \cdot \frac{3}{2} \cdot x^{1/2} = \sqrt{x}\)

<|ref|>equation<|/ref|><|det|>[[186, 825, 840, 899]]<|/det|>
\[ 
\begin{align*}
s &= \frac{8}{3} \sqrt{1 + (\sqrt{x})^2} dx = \frac{8}{3} \int \sqrt{1 + x} dx = \frac{8}{3} \int (1 + x)^{1/2} \\
&= \left[ \frac{2}{3} (1 + x)^{3/2} \right]_3^8 = \frac{2}{3} \left[ 27 - 8 \right] = \frac{38}{3}
\end{align*}
\]