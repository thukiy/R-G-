<|ref|>text<|/ref|><|det|>[[114, 81, 480, 100]]<|/det|>
d) Bestimmen Sie die Lösung des AWP 

<|ref|>text<|/ref|><|det|>[[144, 97, 277, 125]]<|/det|>
DGL: \(y' = \frac{y}{2\sqrt{x}}\) 

<|ref|>text<|/ref|><|det|>[[144, 123, 275, 142]]<|/det|>
AB: \(y(4) = 3\). 

<|ref|>text<|/ref|><|det|>[[114, 156, 145, 173]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[114, 171, 816, 190]]<|/det|>
- Zuerst statische Lösungen bestimmen: es gibt genau eine, nämlich \(y_s(x) = 0\). 

<|ref|>text<|/ref|><|det|>[[114, 188, 856, 224]]<|/det|>
- Dann nicht statische Lösungen bestimmen mittels der Methode der Trennung der Variablen. Für \(y \neq y_s\) erhalten wir 

<|ref|>equation<|/ref|><|det|>[[345, 225, 690, 245]]<|/det|>
\[y' = m(x) \cdot y \quad | : y\]

<|ref|>equation<|/ref|><|det|>[[144, 250, 736, 290]]<|/det|>
\[\Leftrightarrow \quad \frac{1}{y} \cdot y' = m(x) \quad | \int \ldots dx\]

<|ref|>equation<|/ref|><|det|>[[144, 293, 470, 331]]<|/det|>
\[\Leftrightarrow \quad \int \frac{1}{y} \cdot y' \, dx = \int \frac{1}{y} \, dy = \int m(x) \, dx\]

<|ref|>equation<|/ref|><|det|>[[144, 333, 686, 353]]<|/det|>
\[\Leftrightarrow \quad \ln(|y|) = M(x) + c \quad | e^{-c} \]

<|ref|>equation<|/ref|><|det|>[[144, 357, 630, 377]]<|/det|>
\[\Leftrightarrow \quad |y| = e^{M(x) + c} = e^{M(x)} \cdot e^c = C_1 \cdot e^{M(x)}\]

<|ref|>equation<|/ref|><|det|>[[144, 383, 570, 403]]<|/det|>
\[\Leftrightarrow \quad y(x) = \pm C_1 \cdot e^{M(x)} = C_2 \cdot e^{M(x)}\]

<|ref|>text<|/ref|><|det|>[[117, 409, 500, 428]]<|/det|>
für \(x \in \mathbb{R}\) mit \(c \in \mathbb{R}\), \(C_1 \in \mathbb{R}^+\) und \(C_2 \in \mathbb{R} \setminus \{0\}\). 

<|ref|>text<|/ref|><|det|>[[114, 427, 820, 480]]<|/det|>
- Allgemeine Lösung durch Kombination der statischen mit der nicht statischen Lösung: \(y(x) = C \cdot e^{M(x)}\) mit \(C \in \mathbb{R}\) und \(M(x)\) sei eine Stammfunktion von \(m(x)\). 

<|ref|>text<|/ref|><|det|>[[114, 478, 460, 497]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[114, 480, 460, 498]]<|/det|>
- Spezielle statische Lösung: \(y_s(x) = 0\). 

<|ref|>text<|/ref|><|det|>[[114, 496, 870, 530]]<|/det|>
- Spezielle nicht statische Lösung mittels Trennung der Variablen. Für \(y \neq y_s\) erhalten wir 

<|ref|>text<|/ref|><|det|>[[114, 570, 145, 587]]<|/det|>
⇔ 

<|ref|>equation<|/ref|><|det|>[[144, 530, 696, 570]]<|/det|>
\[\Leftrightarrow \quad \frac{1}{y} \cdot y' \quad | : y\]

<|ref|>equation<|/ref|><|det|>[[144, 575, 696, 614]]<|/det|>
\[\Leftrightarrow \quad \int_{x_0}^{x} \frac{1}{y} \cdot y' \, dx = \int_{y_0}^{y} \frac{1}{y} \, dy = \int_{x_0}^{x} m(x) \, dx\]

<|ref|>text<|/ref|><|det|>[[114, 618, 145, 636]]<|/det|>
⇔ 

<|ref|>equation<|/ref|><|det|>[[144, 610, 680, 650]]<|/det|>
\[\Leftrightarrow \quad \ln\left(\frac{y}{y_0}\right) = M(x) - M(x_0) \quad | e^{-c}\]

<|ref|>text<|/ref|><|det|>[[114, 654, 145, 672]]<|/det|>
⇔ 

<|ref|>equation<|/ref|><|det|>[[144, 653, 640, 692]]<|/det|>
\[\Leftrightarrow \quad \frac{y}{y_0} = e^{M(x) - M(x_0)} \quad | \cdot y_0\]

<|ref|>text<|/ref|><|det|>[[114, 732, 145, 750]]<|/det|>
⇔ 

<|ref|>equation<|/ref|><|det|>[[144, 696, 550, 735]]<|/det|>
\[\Leftrightarrow \quad y(x) = y_0 \cdot e^{M(x) - M(x_0)}.\]

<|ref|>text<|/ref|><|det|>[[114, 752, 856, 806]]<|/det|>
- Lösung des AWP durch Kombination der speziellen statischen mit der speziellen nicht statischen Lösung zu \(y(x) = y_0 \cdot e^{M(x) - M(x_0)}\), wobei \(M(x)\) eine Stammfunktion von \(m(x)\) sei. 

<|ref|>text<|/ref|><|det|>[[114, 805, 145, 823]]<|/det|>
c) 

<|ref|>text<|/ref|><|det|>[[114, 821, 875, 896]]<|/det|>
Für die DGL \(y' = \cos(x) \cdot y\) gilt: \(m(x) = \cos x\). Somit ist die allgemeine Stammfunktion von \(m(x)\): \(M(x) = \int m(x) \, dx = \int \cos x \, dx = \sin x + c\). Durch Einsetzen in die allgemeine Lösung aus a) und der Wahl \(c = 0\) erhalten wir die allgemeine Lösung \(y(x) = C \cdot e^{M(x)} = C \cdot e^{\sin x}\).