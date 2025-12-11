<|ref|>sub_title<|/ref|><|det|>[[30, 13, 270, 43]]<|/det|>
Fourier-Reihe 

<|ref|>text<|/ref|><|det|>[[30, 55, 930, 88]]<|/det|>
a) \(2\pi\)-periodische Funktion \(f: \mathbb{R} \to \mathbb{R}\), die auf \([-T; T]\) integrierbar ist, 

<|ref|>text<|/ref|><|det|>[[78, 93, 744, 121]]<|/det|>
kann durch trigonometrische Reihe dargestellt werden. 

<|ref|>text<|/ref|><|det|>[[78, 130, 384, 156]]<|/det|>
Dies ist die Fourier-Reihe 

<|ref|>text<|/ref|><|det|>[[78, 190, 330, 215]]<|/det|>
- reelle Darstellung : 

<|ref|>equation<|/ref|><|det|>[[111, 220, 702, 260]]<|/det|>
\[ \frac{a_0}{2} + \sum_{k=1}^{\infty} \left[ a_k \cos(kx) + b_k \cdot \sin(kx) \right] \quad k \in \mathbb{N} \]

<|ref|>equation<|/ref|><|det|>[[111, 280, 339, 312]]<|/det|>
\[ a_0 = \frac{1}{T} - \pi f(x) \, dx \]

<|ref|>equation<|/ref|><|det|>[[111, 316, 440, 349]]<|/det|>
\[ a_k = \frac{1}{T} - \pi f(x) \cos(kx) \, dx \]

<|ref|>equation<|/ref|><|det|>[[111, 353, 425, 386]]<|/det|>
\[ b_k = \frac{1}{T} - \pi f(x) \sin(kx) \, dx \]

<|ref|>text<|/ref|><|det|>[[111, 399, 613, 425]]<|/det|>
→ \(a_k\) & \(b_k\) heissen Fourier-Koeffizienten 

<|ref|>text<|/ref|><|det|>[[78, 455, 384, 481]]<|/det|>
- komplexe Darstellung : 

<|ref|>equation<|/ref|><|det|>[[131, 485, 300, 525]]<|/det|>
\[ \sum_{k=-\infty}^{\infty} c_k e^{ikx} \]

<|ref|>equation<|/ref|><|det|>[[131, 540, 590, 580]]<|/det|>
\[ c_k = \frac{1}{2\pi} - \pi f(x) e^{-ikx} \, dx \quad k \in \mathbb{Z} \]

<|ref|>text<|/ref|><|det|>[[82, 608, 810, 636]]<|/det|>
dauermenhäng reelle und komplexe Fourier-Koeffizienten : 

<|ref|>equation<|/ref|><|det|>[[131, 644, 535, 675]]<|/det|>
\[ a_0 = 2c_0 \quad a_k = c_k + c_{-k} \]

<|ref|>equation<|/ref|><|det|>[[351, 682, 536, 707]]<|/det|>
\[ b_k = i(c_k - c_{-k}) \]

<|ref|>text<|/ref|><|det|>[[288, 722, 350, 744]]<|/det|>
bzw. 

<|ref|>equation<|/ref|><|det|>[[131, 752, 559, 784]]<|/det|>
\[ c_0 = \frac{1}{2} a_0 \quad c_k = \frac{1}{2} (a_k - ib_k) \]

<|ref|>equation<|/ref|><|det|>[[351, 789, 560, 821]]<|/det|>
\[ c_{-k} = \frac{1}{2} (a_k + ib_k) \]