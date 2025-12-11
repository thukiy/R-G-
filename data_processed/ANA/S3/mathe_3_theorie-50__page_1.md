<|ref|>equation<|/ref|><|det|>[[88, 30, 490, 65]]<|/det|>
\[<p, q> = -\pi \int p(x) \cdot q^*(x) \, dx\]

<|ref|>text<|/ref|><|det|>[[625, 35, 980, 78]]<|/det|>
* konjugiert komplex
→ Imaginarität ändert Vorzeichen 

<|ref|>equation<|/ref|><|det|>[[260, 71, 504, 98]]<|/det|>
\[L^2 - \text{Skalarprodukt}\]

<|ref|>text<|/ref|><|det|>[[25, 150, 576, 177]]<|/det|>
→ trig. Momente sind paarweise orthogonale 

<|ref|>equation<|/ref|><|det|>[[88, 180, 476, 216]]<|/det|>
\[<e^{ijx}, e^{ikx}> = -\pi \int e^{i(j-k)x} \, dx\]

<|ref|>equation<|/ref|><|det|>[[78, 235, 545, 323]]<|/det|>
\[= \begin{cases} -\pi \int 1 \, dx & j = k \\ \left[ \frac{-i}{j-k} e^{i(j-k)x} \right]_{-\pi}^{\pi} = 0 & j \neq k \end{cases}\]

<|ref|>text<|/ref|><|det|>[[360, 323, 550, 363]]<|/det|>
da trig. Momenträg- periodisch 

<|ref|>text<|/ref|><|det|>[[25, 397, 675, 425]]<|/det|>
→ Transformation auf beliebige Periode \(T\) möglich: 

<|ref|>equation<|/ref|><|det|>[[110, 428, 207, 459]]<|/det|>
\[\frac{t}{T} = \frac{x}{2\pi}\]

<|ref|>text<|/ref|><|det|>[[25, 488, 647, 524]]<|/det|>
Orthonormalbasis: \(\psi_k = \frac{1}{\sqrt{2\pi}} e^{ikx}\) \(k \in \mathbb{Z}\) 

<|ref|>equation<|/ref|><|det|>[[315, 526, 655, 598]]<|/det|>
\[< \psi_k, \psi_j> = \begin{cases} 1 & j = k \\ 0 & j \neq k \end{cases}\]

<|ref|>text<|/ref|><|det|>[[25, 620, 570, 655]]<|/det|>
→ reellwertig: \(\sqrt{\frac{2}{\pi}} \sin(kx), \sqrt{\frac{2}{\pi}} \cos(kx)\) 

<|ref|>equation<|/ref|><|det|>[[241, 657, 816, 691]]<|/det|>
\[\frac{2}{\pi} \cdot \sqrt{\sin(jx) \sin(kx)} \, dx = \frac{2}{\pi} \cdot \sqrt{\cos(jx) \cos(kx)} \, dx\]

<|ref|>equation<|/ref|><|det|>[[241, 695, 562, 795]]<|/det|>
\[= \begin{cases} 1 & j = k \\ 0 & j \neq k \text{ } \end{cases}\]

<|ref|>equation<|/ref|><|det|>[[241, 777, 562, 810]]<|/det|>
\[\frac{2}{\pi} \cdot \sqrt{\sin(jx) cos(kx)} \, dx = 0\]

<|ref|>equation<|/ref|><|det|>[[60, 832, 490, 875]]<|/det|>
\[|p|_L^2 = \sqrt{<p, p>} = \sqrt{-\pi \int |p(x)|^2 \, dx}\]

<|ref|>equation<|/ref|><|det|>[[30, 884, 770, 925]]<|/det|>
\[ \text{Absand im quadr. Mittel } |p-q|_L^2 = \left(-\pi \int |p(x) - q(x)|^2 \, dx\right)^{1/2} \]

<|ref|>equation<|/ref|><|det|>[[30, 943, 770, 984]]<|/det|>
\[ \text{Absand von } f \text{ zu trig. Polynom } q = \sum_{k=-n}^{n} q_k \psi_k \quad \psi_k \in \mathbb{C} \]