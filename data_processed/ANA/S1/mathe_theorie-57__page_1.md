<|ref|>sub_title<|/ref|><|det|>[[18, 10, 777, 66]]<|/det|>
# Ableitung Exponentialfunktion 

<|ref|>equation<|/ref|><|det|>[[48, 87, 405, 118]]<|/det|>
\[f(x) = a^x \quad f'(x) = 2\]

<|ref|>text<|/ref|><|det|>[[20, 128, 330, 156]]<|/det|>
mit Differentialquotient : 

<|ref|>equation<|/ref|><|det|>[[48, 156, 860, 298]]<|/det|>
\[f'(x) = \lim_{\Delta x \to 0} \frac{f(x + \Delta x) - f(x)}{\Delta x} = \lim_{\Delta x \to 0} \frac{a^{x+\Delta x} - a^x}{\Delta x} = \lim_{\Delta x \to 0} \frac{a^x \cdot a^{\Delta x} - a^x}{\Delta x} = \lim_{\Delta x \to 1} \frac{a^x \cdot a^{\Delta x} - a^x}{\Delta x} \quad \text{und} \quad f(x) = \lim_{\Delta x \to 0} \frac{a^x \cdot (a^{\Delta x} - 1)}{\Delta x} = a^x \cdot \lim_{\Delta x \to 0} \frac{a^{\Delta x} - 1}{\Delta x} = a^x \cdot z_a = z_a \cdot f(x)\]

<|ref|>text<|/ref|><|det|>[[20, 305, 485, 333]]<|/det|>
Näherungswelle für \(z_a\) bestimmen : 

<|ref|>equation<|/ref|><|det|>[[48, 335, 655, 405]]<|/det|>
\[a = 2 : z_2 = \lim_{\Delta x \to 0} \frac{2^{\Delta x} - 1}{\Delta x} \approx \frac{2^{0,001} - 1}{0,001} \approx 0,69\]

<|ref|>equation<|/ref|><|det|>[[48, 405, 370, 435]]<|/det|>
\[\rightarrow (2^x)^2 \approx 0,69 \cdot 2^x\]

<|ref|>equation<|/ref|><|det|>[[48, 435, 620, 495]]<|/det|>
\[a = 3 : z_3 = \lim_{\Delta x \to 0} \frac{3^{\Delta x} - 1}{\Delta x} \approx \frac{3^{0,001} - 1}{0,001} \approx 1,1\]

<|ref|>equation<|/ref|><|det|>[[48, 495, 390, 525]]<|/det|>
\[\rightarrow (3^x)' = 1,1 \cdot 3^x\]

<|ref|>text<|/ref|><|det|>[[48, 520, 661, 550]]<|/det|>
\(\rightarrow\) es gibt eine Basis \(a\), für die gilt : 

<|ref|>equation<|/ref|><|det|>[[150, 553, 310, 584]]<|/det|>
\[(a^x)' = a^x\]

<|ref|>text<|/ref|><|det|>[[170, 595, 866, 625]]<|/det|>
\(\rightarrow\) dies ist die Eulersche Zahl (nach Leonard Euler) 

<|ref|>equation<|/ref|><|det|>[[230, 636, 559, 661]]<|/det|>
\[e = 2,7182 \ldots \quad \in \mathbb{R} \setminus \mathbb{Q}\]

<|ref|>text<|/ref|><|det|>[[20, 694, 715, 722]]<|/det|>
natürliche Exponential - und logarithmusfunktion : 

<|ref|>equation<|/ref|><|det|>[[48, 730, 208, 760]]<|/det|>
\[f : \mathbb{R} \to \mathbb{R}^+\]

<|ref|>equation<|/ref|><|det|>[[48, 768, 189, 799]]<|/det|>
\[f(x) = e^x\]

<|ref|>equation<|/ref|><|det|>[[48, 808, 192, 839]]<|/det|>
\[f'(x) = e^x\]

<|ref|>equation<|/ref|><|det|>[[100, 847, 741, 955]]<|/det|>
\[\begin{align*}
\text{Umkehrfunktion von } f(x) &= e^x : \quad x = \log_e y \\
&= \ln y \\
&= f^{-1}(y)
\end{align*}\]