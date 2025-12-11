<|ref|>text<|/ref|><|det|>[[20, 15, 852, 45]]<|/det|>
Bsp: Herstellung von Holzbrettern die dünge 10 m, \(z^2 = 10 \, \text{cm}^2\). 

<|ref|>text<|/ref|><|det|>[[108, 55, 833, 85]]<|/det|>
Wie gross ist die Wahrscheinlichkeit, dass Abweichungen 

<|ref|>text<|/ref|><|det|>[[108, 90, 355, 120]]<|/det|>
> 9 cm auftreten? 

<|ref|>equation<|/ref|><|det|>[[108, 145, 592, 180]]<|/det|>
\[P(1 \times -1000 | > 9) \leq \frac{10}{9^2} = \frac{10}{81} \approx 0,123\]

<|ref|>sub_title<|/ref|><|det|>[[30, 222, 707, 253]]<|/det|>
## Zentraler Grenzwertsatz (dindeberg & devy) 

<|ref|>text<|/ref|><|det|>[[57, 263, 940, 293]]<|/det|>
Satz: \(X_1 \ldots X_n\) seien stochastisch unabhängig und normalverteilt mit 

<|ref|>text<|/ref|><|det|>[[160, 300, 797, 330]]<|/det|>
Mittelwerte \(\mu_1 \ldots \mu_n\) und Variation \(\sigma_1^2 \ldots \sigma_n^2\) 

<|ref|>text<|/ref|><|det|>[[160, 336, 930, 377]]<|/det|>
Dann ist die Summe \(Z = \sum_{i=1}^n X_i\) ebenfalls normalverteilt mit 

<|ref|>text<|/ref|><|det|>[[160, 377, 540, 415]]<|/det|>
\(\mu_Z = \sum_{i=1}^n \mu_i\) und \(\sigma_Z^2 = \sum_{i=1}^n \sigma_i^2\) 

<|ref|>text<|/ref|><|det|>[[100, 435, 958, 500]]<|/det|>
→ Haben die Xi denselben Mittelwert \(\mu_i = \mu\) und Variation \(\sigma_i^2 = \sigma^2\), dann gilt: \(\mu_Z = n \cdot \mu\), \(\sigma_Z^2 = n \cdot \sigma^2\) 

<|ref|>text<|/ref|><|det|>[[57, 530, 812, 560]]<|/det|>
bei Anwendungen: Verteilung der Xi unbelangt oder nicht 

<|ref|>text<|/ref|><|det|>[[320, 567, 490, 595]]<|/det|>
normalverteilt 

<|ref|>text<|/ref|><|det|>[[332, 595, 728, 636]]<|/det|>
\(\rightarrow\) Verteilung \(\sum_{i=1}^n X_i\) unbelangt 

<|ref|>sub_title<|/ref|><|det|>[[30, 664, 370, 693]]<|/det|>
## Zentraler Grenzwertsatz 

<|ref|>text<|/ref|><|det|>[[57, 703, 940, 773]]<|/det|>
\(X_1 \ldots X_n\) seien stochastisch unabhängig, die derselben Verteilungsfunktion mit \(\mu\) und \(\sigma^2\) genügen. Man bildet standardisierte Zufallsvariable 

<|ref|>equation<|/ref|><|det|>[[120, 780, 370, 820]]<|/det|>
\[U_n = \frac{X_1 + \ldots + X_n - n\mu}{\sigma \sqrt{n}}\]

<|ref|>text<|/ref|><|det|>[[57, 832, 655, 870]]<|/det|>
Dann gilt \(\lim_{n \to \infty} F_n(u) = \Phi(u) = \frac{1}{\sqrt{2\pi}} \cdot e^{-\frac{1}{2}u^2}\) 

<|ref|>text<|/ref|><|det|>[[57, 894, 886, 920]]<|/det|>
→ \(U_n\) ist für hinreichend grosses \(n\) annähernd standardnormalverteilt 

<|ref|>text<|/ref|><|det|>[[120, 925, 832, 959]]<|/det|>
\(\rightarrow Z_n = \sum_{i=1}^n X_i\) ist annähernd standardnormalverteilt mit 

<|ref|>equation<|/ref|><|det|>[[160, 965, 560, 992]]<|/det|>
\[E(Z_n) = n\mu \text{ und } Var(Z_n) = n\sigma^2\]