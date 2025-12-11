<|ref|>text<|/ref|><|det|>[[45, 10, 333, 40]]<|/det|>
wähle \(v(t) = c \cdot e^{a^2k \cdot t}\) 

<|ref|>equation<|/ref|><|det|>[[144, 45, 480, 80]]<|/det|>
\[w(x) = c_1 e^{\sqrt{k}x} + c_2 e^{-\sqrt{k}x}\]

<|ref|>equation<|/ref|><|det|>[[144, 93, 475, 118]]<|/det|>
\[C, C_1, C_2 \quad \text{Sind Konstanten}\]

<|ref|>text<|/ref|><|det|>[[122, 128, 490, 156]]<|/det|>
\(\rightarrow\) für \(k < 0\) ist \(\sqrt{k}\) imaginar 

<|ref|>text<|/ref|><|det|>[[45, 189, 505, 214]]<|/det|>
beispiele RB: \(u(0, t) = u(L, t) = 0\) 

<|ref|>equation<|/ref|><|det|>[[100, 220, 715, 252]]<|/det|>
\[0 = w(0) = w(L) = c_1 + c_2 = c_1 e^{\sqrt{k}L} + c_2 e^{-\sqrt{k}L}\]

<|ref|>equation<|/ref|><|det|>[[100, 265, 470, 290]]<|/det|>
\[\text{aus } 0 = c_1 + c_2 : \quad c_1 = -c_2\]

<|ref|>equation<|/ref|><|det|>[[100, 295, 395, 328]]<|/det|>
\[\Rightarrow 0 = c_1 (e^{\sqrt{k}L} - e^{-\sqrt{k}L})\]

<|ref|>equation<|/ref|><|det|>[[100, 337, 440, 366]]<|/det|>
\[\text{mit } \sinh(x) = \frac{1}{2} (e^x - e^{-x}) :\]

<|ref|>equation<|/ref|><|det|>[[164, 380, 395, 406]]<|/det|>
\[0 = 2c_1 \sinh(\sqrt{k}L)\]

<|ref|>text<|/ref|><|det|>[[105, 437, 285, 461]]<|/det|>
1. Fall: \(k > 0\) 

<|ref|>equation<|/ref|><|det|>[[214, 475, 450, 500]]<|/det|>
\[c_1 = 0 \quad \rightarrow \quad c_2 = 0\]

<|ref|>text<|/ref|><|det|>[[184, 512, 890, 538]]<|/det|>
\(\Rightarrow w(x) = 0\) und \(v(t) = 0\), entpricht der triviaten Lösung 

<|ref|>text<|/ref|><|det|>[[105, 570, 280, 594]]<|/det|>
2. Fall: \(k < 0\) 

<|ref|>equation<|/ref|><|det|>[[144, 604, 671, 630]]<|/det|>
\[w(x) = \tilde{c}_1 \sin(\sqrt{k}L x) + \tilde{c}_2 \cos(\sqrt{k}L x)\]

<|ref|>equation<|/ref|><|det|>[[100, 636, 905, 800]]<|/det|>
\[w(x) = c_1 e^{\sqrt{k} x} + c_2 e^{-\sqrt{k} x} \\
= c_1 e^{i\sqrt{k} x} + c_2 e^{-i\sqrt{k} x} \\
= c_1 [\cos(\sqrt{k} x) + i \sin(-\sqrt{k} x)] + c_2 [\cos(-\sqrt{k} x) + i \sin(-\sqrt{k} x)] \\
= \cos(\sqrt{k} x) \cdot (c_1 + c_2) + \sin(\sqrt{k} x) (ic_1 - ic_2)\]

<|ref|>equation<|/ref|><|det|>[[100, 815, 380, 846]]<|/det|>
\[\text{mit } RB: w(0) = 0 = \tilde{c}_2\]

<|ref|>equation<|/ref|><|det|>[[214, 855, 456, 880]]<|/det|>
\[w(L) = 0\]

<|ref|>equation<|/ref|><|det|>[[284, 890, 456, 916]]<|/det|>
\[= \sin(\sqrt{k}L) \tilde{c}_1\]

<|ref|>equation<|/ref|><|det|>[[208, 930, 565, 955]]<|/det|>
\[\rightarrow \sqrt{k} L = n\pi \quad n \in \mathbb{N}\]