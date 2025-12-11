<|ref|>equation<|/ref|><|det|>[[119, 81, 392, 115]]<|/det|>
\[y' = \boxed{\cdot} \cdot \sinh \left(\frac{x}{c}\right) \cdot \frac{1}{\boxed{\cdot}} = \sinh \left(\frac{x}{c}\right)\]

<|ref|>equation<|/ref|><|det|>[[119, 120, 702, 185]]<|/det|>
\[ \begin{aligned} 1 + (y')^2 &= 1 + \sinh^2 \left(\frac{x}{c}\right) = \cosh^2 \left(\frac{x}{c}\right) \Rightarrow \sqrt{1 + (y')^2} = \cosh \left(\frac{x}{c}\right) \\ y \cdot \sqrt{1 + (y')^2} &= c \cdot \cosh \left(\frac{x}{c}\right) \cdot \cosh \left(\frac{x}{c}\right) = c \cdot \cosh^2 \left(\frac{x}{c}\right) \end{aligned} \]

<|ref|>text<|/ref|><|det|>[[115, 180, 735, 201]]<|/det|>
Berechnung des Integrals (siehe Übungsblatt 3 Analysis Aufgabe 2j): 

<|ref|>equation<|/ref|><|det|>[[115, 202, 840, 264]]<|/det|>
\[ M_x = 2\pi \cdot \int_a^b y \cdot \sqrt{1 + (y')^2} \, dx = 2\pi c \cdot 2 \cdot \int_0^c \cosh^2 \left(\frac{x}{c}\right) \, dx = 4\pi c \left[ \frac{x}{2} + \frac{\sinh \left(\frac{2x}{c}\right)}{4/c} \right]_0^c = \]

<|ref|>equation<|/ref|><|det|>[[139, 303, 895, 410]]<|/det|>
\[ \begin{aligned} &= 4\pi c \left[ \frac{x}{2} + \frac{c}{4} \cdot \sinh \left(\frac{2x}{c}\right) \right]_0^c = 4\pi c \left( \frac{c}{2} + \frac{c}{4} \cdot \sinh 2 - 0 - \frac{c}{4} \cdot \sinh 0 \right) = 4\pi c \left( \frac{c}{2} + \frac{c}{2} \cdot \sinh 2 \right) = \\ &= 4\pi c \cdot \frac{c}{2} \left( 1 + \frac{1}{2} \cdot \sinh 2 \right) = 2\pi c^2 \cdot 2,8134 = 5,6268\pi c^2 = 17,6771 \cdot c^2 \end{aligned} \]