<|ref|>sub_title<|/ref|><|det|>[[24, 11, 592, 64]]<|/det|>
# Stetigkeit einer Funktion 

<|ref|>text<|/ref|><|det|>[[24, 90, 990, 196]]<|/det|>
Def: Eine in \(x_0\) und einer gewissen Umgebung von \(x_0\) definierte Funktion \(y = f(x)\) heisst stetig an der Stelle \(x_0\), wenn der Grenzwert von \(f(x)\) an \(x_0\) vorhanden ist und mit dem Funktionswert übereinstimmt: 

<|ref|>equation<|/ref|><|det|>[[92, 207, 325, 245]]<|/det|>
\[ \lim_{x \to x_0} f(x) = f(x_0) \]

<|ref|>text<|/ref|><|det|>[[24, 265, 110, 293]]<|/det|>
Bsp: 

<|ref|>equation<|/ref|><|det|>[[92, 263, 300, 293]]<|/det|>
\[ \bullet f(x) = x^2 \quad f: \mathbb{R} \to \mathbb{R} \]

<|ref|>equation<|/ref|><|det|>[[165, 304, 675, 350]]<|/det|>
\[ f(1) = 1 \quad \lim_{x \to 1} f(x) = 1 = f(1) \]

<|ref|>text<|/ref|><|det|>[[165, 345, 475, 375]]<|/det|>
⇒ ist auf ganz \(\mathbb{R}\) stetig 

<|ref|>equation<|/ref|><|det|>[[92, 375, 610, 419]]<|/det|>
\[ \bullet f(x) = \frac{1}{1-x} \quad f: \mathbb{R} \setminus \{1\} \to \mathbb{R} \]

<|ref|>text<|/ref|><|det|>[[165, 423, 866, 490]]<|/det|>
⇒ \(f(x)\) ist an \(x = 1\) nicht stetig, da nicht definiert an dieser Stelle (Definitionslücke) 

<|ref|>equation<|/ref|><|det|>[[92, 494, 580, 595]]<|/det|>
\[ \bullet f(x) = \begin{cases} 1 & x > 0 \\ 0 & < 0 \end{cases} \]

<|ref|>text<|/ref|><|det|>[[165, 576, 580, 610]]<|/det|>
⇒ \(f(x)\) ist an \(x = 0\) nicht stetig 

<|ref|>text<|/ref|><|det|>[[24, 636, 700, 666]]<|/det|>
Unstetigkeitsstellen: • Lücken im Definitionsbereich 

<|ref|>text<|/ref|><|det|>[[300, 677, 555, 703]]<|/det|>
• endliche Sprünge 

<|ref|>text<|/ref|><|det|>[[300, 715, 456, 740]]<|/det|>
• Polstellen 

<|ref|>text<|/ref|><|det|>[[24, 765, 830, 802]]<|/det|>
Bsp: 
\[ \bullet f(x) = \frac{x^2 - 1}{x + 1} \quad \text{bei } x_0 = -1 \text{ Definitionslücke} \] 

<|ref|>equation<|/ref|><|det|>[[165, 803, 928, 850]]<|/det|>
\[ \lim_{x \to -1} \frac{x^2 - 1}{x + 1} = \lim_{x \to -1} \frac{(x+1)(x-1)}{x+1} = \lim_{x \to -1} (x-1) = -2 \]

<|ref|>text<|/ref|><|det|>[[175, 867, 857, 897]]<|/det|>
Beheben der dicke: Funktionswert = Grenzwert 

<|ref|>equation<|/ref|><|det|>[[191, 900, 930, 975]]<|/det|>
\[ g(x) = \begin{cases} \frac{x^2 - 1}{x + 1} & x \neq -1 \\ -2 & x = -1 \end{cases} \quad \Rightarrow g(x) \text{ ist stetig} \]