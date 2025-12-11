<|ref|>sub_title<|/ref|><|det|>[[25, 15, 339, 44]]<|/det|>
## Fourier transformation 

<|ref|>text<|/ref|><|det|>[[60, 56, 490, 84]]<|/det|>
periodische Funktion \(f(x) = f(x+p)\) 

<|ref|>text<|/ref|><|det|>[[60, 88, 732, 123]]<|/det|>
→ \(\frac{2\pi}{p} = \omega\) kann als Grundfrequenz aufgefasst werden 

<|ref|>text<|/ref|><|det|>[[60, 131, 946, 202]]<|/det|>
→ die sin- und cos-Funktionen haben verschiedene Amplituden an und bei
und Frequenzen \(\omega_n\), die Vielfache der Grundfrequenz \(\omega\) sind: \(\omega_n = k \cdot \omega\) 

<|ref|>text<|/ref|><|det|>[[60, 208, 949, 275]]<|/det|>
→ Signal \(f(x)\) ist überlagerung unendlicher Anzahl harmonischer sin- bzw.
cos-Schwingungen 

<|ref|>text<|/ref|><|det|>[[60, 283, 930, 312]]<|/det|>
→ das periodische Signal besitzt ein disurtes Spektrum von Frequenzen \(\omega_n\) 

<|ref|>image<|/ref|><|det|>[[36, 344, 480, 450]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[40, 468, 540, 488]]<|/det|>
Kippschwingung/Sägezahnfunktion als Fourier-Reihe: 

<|ref|>equation<|/ref|><|det|>[[40, 495, 550, 530]]<|/det|>
\[f(t) = \frac{A}{2} - \frac{A}{\pi} \left[ \sin(\omega_0 t) + \frac{1}{2} \sin(2\omega_0 t) + \frac{1}{3} \sin(3\omega_0 t) + \ldots \right]\]

<|ref|>image<|/ref|><|det|>[[550, 343, 955, 512]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[570, 518, 789, 537]]<|/det|>
(Amplituden-)Spektrum 

<|ref|>text<|/ref|><|det|>[[30, 569, 960, 636]]<|/det|>
Frage: Kann auch ein nicht-periodisches Signal spektral verlegt werden, also
durch überlagerung von sin- und cos-Funktionen dargestellt werden? 

<|ref|>text<|/ref|><|det|>[[30, 664, 936, 691]]<|/det|>
→ \(f(x)\), was auf \(x_0, x_0 + p\) gegeben ist, kann periodisch fortgesetzt werden 

<|ref|>text<|/ref|><|det|>[[100, 700, 725, 728]]<|/det|>
⇛ \(p \to \infty\) exibt gewünscht nicht periodische Funktion 

<|ref|>text<|/ref|><|det|>[[30, 740, 440, 767]]<|/det|>
→ für periodische Funktionen gibt: 

<|ref|>equation<|/ref|><|det|>[[90, 772, 545, 810]]<|/det|>
\[\Delta \omega = \omega_{n+1} - \omega_n = \frac{2\pi(k+1)}{p} - \frac{2\pi k}{p} = \frac{2\pi}{p}\]

<|ref|>text<|/ref|><|det|>[[100, 816, 440, 842]]<|/det|>
⇛ für \(p \to \infty\): \(\Delta \omega \to 0\) 

<|ref|>text<|/ref|><|det|>[[60, 854, 936, 920]]<|/det|>
→ für nicht-periodische Funktion ergibt sich ein kontinuierliches Spektrum
aller Frequenzen 

<|ref|>equation<|/ref|><|det|>[[30, 940, 560, 985]]<|/det|>
\[\Rightarrow f(x) = \sum_{k=-\infty}^{\infty} \left[ \frac{2}{p} x_0^{k+p} f(t) \cdot e^{-i \frac{2\pi}{p} kt} \right] dt \quad \text{et} \quad i \frac{2\pi}{p} x\]