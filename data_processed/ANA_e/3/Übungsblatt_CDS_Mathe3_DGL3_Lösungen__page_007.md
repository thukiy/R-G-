<|ref|>equation<|/ref|><|det|>[[357, 81, 675, 110]]<|/det|>
\[y' = 1 \cdot 2 \sqrt{y} \quad \left| : (2 \sqrt{y}) \right.\]

<|ref|>equation<|/ref|><|det|>[[117, 115, 690, 155]]<|/det|>
\[\Leftrightarrow \quad \frac{1}{2 \sqrt{y}} \cdot y' = 1 \quad \left| \int_{2}^{x} \ldots dx \right.\]

<|ref|>equation<|/ref|><|det|>[[117, 159, 476, 199]]<|/det|>
\[\Rightarrow \quad \int_{2}^{x} \frac{1}{2 \sqrt{y}} \cdot y' dx = \int_{2}^{x} 1 dx\]

<|ref|>equation<|/ref|><|det|>[[117, 202, 476, 243]]<|/det|>
\[\Leftrightarrow \quad \int_{9}^{y} \frac{1}{2 \sqrt{y}} dy = \int_{2}^{x} 1 dx\]

<|ref|>equation<|/ref|><|det|>[[117, 'y' = \sqrt{y} - \sqrt{9} = \left[ x \right]_{2}^{x} = x - 2 \quad \left| + 3 \right.\]

<|ref|>equation<|/ref|><|det|>[[117, 285, 650, 305]]<|/det|>
\[\Leftrightarrow \quad \sqrt{y} = x + 1 \quad \left| (\ldots)^2 \right.\]

<|ref|>equation<|/ref|><|det|>[[117, 310, 636, 339]]<|/det|>
\[\Rightarrow \quad y(x) = (x + 1)^2. \quad \left[ \star \right]\]

<|ref|>text<|/ref|><|det|>[[114, 333, 785, 368]]<|/det|>
Die letzte Umformung stellt keine Äquivalenzumformung dar. Sie ist jedoch umkehrbar, wenn gilt 

<|ref|>equation<|/ref|><|det|>[[297, 367, 567, 387]]<|/det|>
\[x + 1 \ge 0 \quad \left| -1 \right.\]

<|ref|>equation<|/ref|><|det|>[[117, 395, 352, 415]]<|/det|>
\[\Leftrightarrow \quad x \ge -1.\]

<|ref|>text<|/ref|><|det|>[[114, 415, 732, 435]]<|/det|>
Aus der nicht statischen Lösung (*) erhält man die Lösung des AWP: 

<|ref|>equation<|/ref|><|det|>[[120, 435, 451, 457]]<|/det|>
\[y(x) = (x + 1)^2 \quad \text{für } x \in [-1, \infty[.\]

<|ref|>text<|/ref|><|det|>[[114, 462, 144, 480]]<|/det|>
c) 

<|ref|>equation<|/ref|><|det|>[[162, 485, 692, 504]]<|/det|>
\[u = 1 + x + y, \quad u' = 0 + 1 + y' = 1 + y' \quad \Rightarrow \quad y' = u' - 1 \quad \Rightarrow\]

<|ref|>equation<|/ref|><|det|>[[162, 512, 816, 545]]<|/det|>
\[y' = (1 + x + y)^2 \quad \Rightarrow \quad u' - 1 = u^2 \quad \Rightarrow \quad u' = \frac{du}{dx} = 1 + u^2 \quad \Rightarrow \quad \frac{du}{1 + u^2} = dx\]

<|ref|>text<|/ref|><|det|>[[114, 551, 725, 568]]<|/det|>
Nach der bereits vorgenommenen Trennung der Variablen werden beide Seiten integriert: 

<|ref|>equation<|/ref|><|det|>[[162, 574, 670, 608]]<|/det|>
\[\int \frac{du}{1 + u^2} = \int 1 \, dx \quad \Rightarrow \quad \arctan u = x + C \quad \Rightarrow \quad u = \tan (x + C)\]

<|ref|>text<|/ref|><|det|>[[114, 614, 587, 630]]<|/det|>
Durch Rücksubstitution erhalten wir die gesuchte allgemeine Lösung: 

<|ref|>equation<|/ref|><|det|>[[162, 637, 632, 655]]<|/det|>
\[u = 1 + x + y = \tan (x + C) \quad \Rightarrow \quad y = \tan (x + C) - x - 1\]

<|ref|>text<|/ref|><|det|>[[114, 661, 603, 679]]<|/det|>
Aus dem Anfangswert \(y(0) = 2\) bestimmen wir die spezielle Lösung: 

<|ref|>equation<|/ref|><|det|>[[162, 685, 880, 704]]<|/det|>
\[y(0) = 2 \quad \Rightarrow \quad \tan C - 1 = 2 \quad \Rightarrow \quad \tan C = 3 \quad \Rightarrow \quad C = \arctan 3 = 1,2490 \quad (\text{Bogenmaß!})\]

<|ref|>text<|/ref|><|det|>[[114, 710, 408, 728]]<|/det|>
Lösung: \(y = \tan (x + 1,2490) - x - 1\)