<|ref|>equation<|/ref|><|det|>[[257, 88, 590, 128]]<|/det|>
\[ (x - C) \in \mathbb{R} \setminus \left\{ \pm \frac{\pi}{2}, \pm \frac{3\pi}{2}, \pm \frac{5\pi}{2}, \dots \right\} \]

<|ref|>equation<|/ref|><|det|>[[119, 132, 590, 174]]<|/det|>
\[ \Leftrightarrow \quad x \in \mathbb{R} \setminus \left\{ C \pm \frac{\pi}{2}, C \pm \frac{3\pi}{2}, C \pm \frac{5\pi}{2}, \dots \right\}. \]

<|ref|>text<|/ref|><|det|>[[115, 176, 608, 195]]<|/det|>
Es ergeben sich die folgenden allgemeinen Lösungen: 

<|ref|>equation<|/ref|><|det|>[[119, 195, 737, 234]]<|/det|>
\[ y(x) = \tan(x - C) \text{ für } x \in \mathbb{R} \setminus \left\{ C \pm \frac{\pi}2, C \pm \frac{3\pi}2, C \pm \frac{5\pi}2, \dots \right\} \quad \text{mit } C \in \mathbb{R}. \]

<|ref|>text<|/ref|><|det|>[[115, 238, 142, 257]]<|/det|>
f) 

<|ref|>text<|/ref|><|det|>[[115, 255, 305, 274]]<|/det|>
Statische Lösungen: 

<|ref|>equation<|/ref|><|det|>[[407, 276, 565, 296]]<|/det|>
\[ 0 = x^2 \cdot (3y_s + 1) \]

<|ref|>equation<|/ref|><|det|>[[249, 305, 730, 324]]<|/det|>
\[ \Leftrightarrow \quad 0 = 3y_s + 1 \quad | - 1 \]

<|ref|>equation<|/ref|><|det|>[[249, 335, 728, 353]]<|/det|>
\[ \Leftrightarrow \quad -1 = 3y_s \quad | : 3. \]

<|ref|>text<|/ref|><|det|>[[123, 361, 630, 380]]<|/det|>
Daraus erhalten wir genau eine statische Lösung, nämlich 

<|ref|>equation<|/ref|><|det|>[[430, 386, 549, 419]]<|/det|>
\[ y_s(x) = -\frac{1}{3}. \]

<|ref|>text<|/ref|><|det|>[[115, 420, 857, 440]]<|/det|>
Nicht statische Lösungen mit der Methode der Trennung der Variablen bestimmen: 

<|ref|>equation<|/ref|><|det|>[[409, 440, 780, 460]]<|/det|>
\[ y' = x^2 \cdot (3y + 1) \quad | : (3y + 1) \]

<|ref|>equation<|/ref|><|det|>[[131, 492, 775, 532]]<|/det|>
\[ \Leftrightarrow \quad \frac{1}{3y + 1} \cdot y' = x^2 \quad | \int \dots dx \]

<|ref|>equation<|/ref|><|det|>[[131, 535, 525, 575]]<|/det|>
\[ \Leftrightarrow \quad \int \frac{1}{3y + 1} \cdot y' dx = \int \frac{1}{3y + 1} dy = \int x^2 dx \]

<|ref|>equation<|/ref|><|det|>[[131, 577, 722, 611]]<|/det|>
\[ \Leftrightarrow \quad \frac{1}{3} \ln(|3y + 1|) = \frac{1}{3} x^3 + c \quad | \cdot 3 \]

<|ref|>equation<|/ref|><|det|>[[131, 614, 722, 639]]<|/det|>
\[ \Leftrightarrow \quad \ln(|3y + 1|) = x^3 + 3c \quad | e^{\dots} \]

<|ref|>equation<|/ref|><|det|>[[131, 642, 590, 666]]<|/det|>
\[ \Leftrightarrow \quad |3y + 1| = e^{x^3 + 3c} = e^{x^3} \cdot e^{3c} \]

<|ref|>equation<|/ref|><|det|>[[131, 670, 504, 694]]<|/det|>
\[ \Leftrightarrow \quad |3y + 1| = C_1 \cdot e^{x^3} \]

<|ref|>equation<|/ref|><|det|>[[131, 697, 730, 722]]<|/det|>
\[ \Leftrightarrow \quad 3y + 1 = \pm C_1 \cdot e^{x^3} = C_2 \cdot e^{x^3} \quad | - 1 \]

<|ref|>equation<|/ref|><|det|>[[131, 727, 722, 751]]<|/det|>
\[ \Leftrightarrow \quad 3y = C_2 \cdot e^{x^3} - 1 \quad | : 3 \]

<|ref|>equation<|/ref|><|det|>[[131, 754, 675, 789]]<|/det|>
\[ \Leftrightarrow \quad y(x) = \frac{C_2}{3} \cdot e^{x^3} - \frac{1}{3} = C_3 \cdot e^{x^3} - \frac{1}{3} \]

<|ref|>text<|/ref|><|det|>[[119, 792, 547, 812]]<|/det|>
für \(x \in \mathbb{R}\) mit \(c \in \mathbb{R}\), \(C_1 \in \mathbb{R}^+\) und \(C_2, C_3 \in \mathbb{R} \setminus \{0\}\). 

<|ref|>text<|/ref|><|det|>[[115, 811, 857, 831]]<|/det|>
Allgemeine Lösung durch Kombination der statischen und nicht statischen Lösung: 

<|ref|>equation<|/ref|><|det|>[[119, 830, 417, 866]]<|/det|>
\[ y(x) = C \cdot e^{x^3} - \frac{1}{3} \quad \text{mit } C \in \mathbb{R}. \]