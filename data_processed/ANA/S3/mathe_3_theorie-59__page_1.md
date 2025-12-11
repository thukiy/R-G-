<|ref|>sub_title<|/ref|><|det|>[[24, 17, 525, 45]]<|/det|>
b) Es liegt eine p-periodische Funktion 

<|ref|>equation<|/ref|><|det|>[[108, 54, 950, 115]]<|/det|>
\[ f(x) = f(x+p), \quad f: \mathbb{R} \to \mathbb{R} \text{ vor, die auf } ]x_0, x_0+p[ \text{ stäuben sie sich } \text{differenzierbar ist. Die Fourier-Reihe } u_f \text{ ist } \]

<|ref|>equation<|/ref|><|det|>[[137, 120, 650, 160]]<|/det|>
\[ \frac{a_0}{2} + \sum_{k=1}^{\infty} \left[ a_k \cos\left(\frac{2\pi k}{p} \cdot x\right) + b_k \sin\left(\frac{2\pi k}{p} \cdot x\right) \right] \]

<|ref|>equation<|/ref|><|det|>[[137, 177, 390, 217]]<|/det|>
\[ a_0 = \frac{2}{p} \sum_{x_0}^{x_0+p} f(x) \, dx \]

<|ref|>equation<|/ref|><|det|>[[137, 220, 528, 260]]<|/det|>
\[ a_k = \frac{2}{p} \sum_{x_0}^{x_0+p}f(x) \cdot \cos\left(\frac{2\pi k}{p} \cdot x\right) \, dx \]

<|ref|>equation<|/ref|><|det|>[[137, 260, 520, 300]]<|/det|>
\[ b_k = \frac{2}{p} \sum_{x_0}^{x_0 + p} f(x) \cdot \sin\left(\frac{2\pi k}{p} \cdot x\right) \, dx \]

### Nicht-periodische Signale 

<|ref|>text<|/ref|><|det|>[[30, 377, 580, 405]]<|/det|>
1. \(f: \mathbb{R} \to \mathbb{C}\) sei nicht periodische Funktion 

<|ref|>text<|/ref|><|det|>[[88, 416, 644, 444]]<|/det|>
\(f\) kann in keine Fourier-Reihe entwickelt werden 

<|ref|>text<|/ref|><|det|>[[30, 455, 692, 483]]<|/det|>
2. \(f: [t_0, t_1] \to \mathbb{C}\) kann periodisch erweitert werden 

<|ref|>text<|/ref|><|det|>[[88, 493, 955, 520]]<|/det|>
Es gelten dieselben Aussagen/Bedingungen wie für periodische Funktionen 

<|ref|>text<|/ref|><|det|>[[24, 550, 440, 577]]<|/det|>
**Bsp:** \(f: [0; 2] \to \mathbb{R}\) 

<|ref|>equation<|/ref|><|det|>[[360, 550, 450, 572]]<|/det|>
\[ f(t) = t \]

<|ref|>image<|/ref|><|det|>[[100, 580, 757, 770]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[88, 779, 965, 848]]<|/det|>
Einleitung mit Periode 4, keine Sprünge, gerade: reine cos-Reihe
Einleitung mit Periode 8, keine Sprünge, ungeade: reine sin-Reihe 

<|ref|>text<|/ref|><|det|>[[108, 857, 465, 885]]<|/det|>
→ Vermeidung von Sprüngen 

<|ref|>text<|/ref|><|det|>[[108, 895, 437, 922]]<|/det|>
→ möglichst kurze Periode 

<|ref|>text<|/ref|><|det|>[[108, 933, 590, 961]]<|/det|>
→ wenn möglich: Symmetrie herstellen