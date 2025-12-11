<|ref|>text<|/ref|><|det|>[[30, 16, 230, 44]]<|/det|>
Rächenregel : 

<|ref|>equation<|/ref|><|det|>[[60, 55, 410, 81]]<|/det|>
\[P(\mu - \delta \le X \le \mu + \delta) \approx 0,68\]

<|ref|>equation<|/ref|><|det|>[[60, 93, 455, 119]]<|/det|>
\[P(\mu - 2\delta \le X \le \mu + 2\delta) \approx 0,95\]

<|ref|>equation<|/ref|><|det|>[[60, 131, 465, 157]]<|/det|>
\[P(\mu - 3\delta \le X \le \mu + 3\delta) \approx 0,997\]

<|ref|>image<|/ref|><|det|>[[530, 15, 866, 170]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[30, 189, 650, 214]]<|/det|>
Standardisierung ergibt Standardnormalverteilung 

<|ref|>equation<|/ref|><|det|>[[20, 227, 440, 252]]<|/det|>
\[\rightarrow \mu = 0 \quad \text{und} \quad \delta^2 = 1 \Rightarrow \delta = 1\]

<|ref|>text<|/ref|><|det|>[[100, 264, 562, 290]]<|/det|>
\(\rightarrow\) wird durch Transformation erzielt : 

<|ref|>equation<|/ref|><|det|>[[150, 295, 270, 328]]<|/det|>
\[U = \frac{x-\mu}{\delta}\]

<|ref|>equation<|/ref|><|det|>[[100, 331, 536, 365]]<|/det|>
\[\rightarrow \text{Dichte Funktion } \varphi(u) = \frac{1}{2\pi} e^{-\frac{1}{2}u^2}\]

<|ref|>equation<|/ref|><|det|>[[100, 377, 748, 405]]<|/det|>
\[\rightarrow \text{Verteilungsfunktion } \phi(u) = P(U \le u) = -\omega^2 \varphi(t) \, dt\]

<|ref|>equation<|/ref|><|det|>[[20, 436, 260, 460]]<|/det|>
\[\rightarrow \varphi(u) = \varphi(-u)\]

<|ref|>equation<|/ref|><|det|>[[80, 472, 285, 497]]<|/det|>
\[\phi(-u) = 1 - \phi(u)\]

<|ref|>text<|/ref|><|det|>[[20, 530, 955, 558]]<|/det|>
\(\rightarrow\) Werte der Verteilungsfunktion sind tabelliert, sind nur für \(u > 0\) gegeben 

<|ref|>text<|/ref|><|det|>[[20, 590, 610, 616]]<|/det|>
\(\rightarrow\) wenn nicht standardisierte Variable vorliegt : 

<|ref|>equation<|/ref|><|det|>[[80, 620, 510, 653]]<|/det|>
\[P(X \le x) = F(x) = \Phi\left(\frac{x-\mu}{\delta}\right) = \Phi(u)\]

<|ref|>equation<|/ref|><|det|>[[100, 663, 430, 688]]<|/det|>
\[\rightarrow P(a \le X \le b) = F(b) - F(b)\]

<|ref|>equation<|/ref|><|det|>[[150, 696, 600, 753]]<|/det|>
\[= \Phi\left(\frac{b-\mu}{\delta}\right) - \Phi\left(\frac{a-\mu}{\delta}\right) = \Phi(b^*) - \Phi(a^*)\]

<|ref|>equation<|/ref|><|det|>[[100, 780, 630, 805]]<|/det|>
\[\rightarrow P(|X - \mu| \le k\delta) = P(\mu - k\delta \le X \le \mu + k\delta + \mu)\]

<|ref|>equation<|/ref|><|det|>[[150, 816, 425, 841]]<|/det|>
\[= F(\mu + k\delta) - F(\mu - k\delta)\]

<|ref|>equation<|/ref|><|det|>[[150, 853, 592, 878]]<|/det|>
\[= \Phi(k) - \Phi(-k) = \Phi(k) - [1 - \Phi(k)]\]

<|ref|>equation<|/ref|><|det|>[[150, 890, 325, 915]]<|/det|>
\[= 2 \cdot \Phi(k) - 1\]