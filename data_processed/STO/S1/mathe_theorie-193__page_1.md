<|ref|>sub_title<|/ref|><|det|>[[25, 7, 460, 42]]<|/det|>
Standardnormalverteilung 

<|ref|>text<|/ref|><|det|>[[52, 51, 852, 82]]<|/det|>
Standardisierung wird durchgeführt, d.h. \(\mu = 0\) und \(z^2 = 1 = z\) 

<|ref|>equation<|/ref|><|det|>[[72, 88, 900, 128]]<|/det|>
\[ \rightarrow U = \frac{x - \mu}{z} \quad (\mu \text{ & } z \text{ sind weite aus ursprünglichen Verteilungen}) \]

<|ref|>text<|/ref|><|det|>[[72, 147, 500, 175]]<|/det|>
→ Dichte Funktion ergibt sich zu 

<|ref|>equation<|/ref|><|det|>[[128, 180, 644, 220]]<|/det|>
\[ \varphi(u) = \frac{1}{\sqrt{2\pi}} \cdot e^{-\frac{1}{2} u^2} \quad -\infty < u < \infty \]

<|ref|>text<|/ref|><|det|>[[128, 245, 415, 272]]<|/det|>
Verteilungsfunktion : 

<|ref|>equation<|/ref|><|det|>[[136, 275, 615, 313]]<|/det|>
\[ \varphi(u) = P(U \le u) = \frac{1}{\sqrt{2\pi}} \cdot e^{-\frac{1}2 u^2} \quad dt \]

<|ref|>equation<|/ref|><|det|>[[72, 343, 722, 373]]<|/det|>
\[ \rightarrow \varphi(u) = \varphi(-u), \text{ d.h. } \varphi \text{ ist achsensymmetrisch} \]

<|ref|>equation<|/ref|><|det|>[[144, 381, 440, 410]]<|/det|>
\[ \rightarrow \varphi(-u) = 1 - \varphi(u) \]

<|ref|>equation<|/ref|><|det|>[[72, 419, 585, 453]]<|/det|>
\[ \rightarrow \varphi(u) \text{ ist normiert: } -\infty \int \varphi(u) \, du = 1 \]

<|ref|>text<|/ref|><|det|>[[72, 480, 970, 550]]<|/det|>
→ Weite der Verteilungsfunktion \(\varphi(u)\) liegen in tobellorischer Form vor, allerdings muß für \(u > 0\) : \(\varphi(-u) = 1 - \varphi(u)\) 

<|ref|>image<|/ref|><|det|>[[181, 562, 640, 717]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[52, 733, 450, 764]]<|/det|>
Gegeben ist \(X\) mit \(\mu\) und \(z^2\) 

<|ref|>equation<|/ref|><|det|>[[56, 768, 546, 802]]<|/det|>
\[ 1) \quad P(X \le x) = F(x) = \varphi\left(\frac{x - \mu}{z}\right) = \varphi(u) \]

<|ref|>equation<|/ref|><|det|>[[56, 807, 784, 841]]<|/det|>
\[ 2) \quad P(X \ge x) = 1 - P(X \le x) = 1 - \varphi\left(\frac{x - \mu}{z}\right) = 1 - \varphi(u) \]

<|ref|>equation<|/ref|><|det|>[[56, 846, 940, 880]]<|/det|>
\[ 3) \quad P(a \le X \le b) = F(b) - F(a) = \varphi\left(\frac{b - \mu}{z}\right) - \varphi\left(\frac{a - \mu}{z}\right) = \varphi(b^*) - \varphi(a^*) \]

<|ref|>equation<|/ref|><|det|>[[56, 925, 884, 998]]<|/det|>
\[ 4) \quad P(|X - \mu| \le kz) = P(\mu - kz \le X \le \mu + kz) = \varphi(k) - \varphi(-k) \\ = 2 \cdot \varphi(k) - 1 \]