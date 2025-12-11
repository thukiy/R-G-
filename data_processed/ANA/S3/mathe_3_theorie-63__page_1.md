<|ref|>text<|/ref|><|det|>[[24, 15, 375, 42]]<|/det|>
Bsp: døg im "Realraum" i 

<|ref|>text<|/ref|><|det|>[[191, 54, 400, 78]]<|/det|>
Rückharmonformation 

<|ref|>equation<|/ref|><|det|>[[191, 85, 560, 118]]<|/det|>
\[x(t) = \frac{1}{2\pi} \cdot \omega f X(\omega) e^{i\omega t} d\omega\]

<|ref|>equation<|/ref|><|det|>[[191, 120, 560, 153]]<|/det|>
\[= \frac{1}{2\pi} \cdot \omega f \frac{e^{i\omega t}}{(i\omega + \tau)(-i\omega^2 + 4i\omega - 5)} d\omega\]

<|ref|>text<|/ref|><|det|>[[191, 170, 490, 194]]<|/det|>
dies ist eine partikuläre døg 

<|ref|>text<|/ref|><|det|>[[105, 225, 712, 248]]<|/det|>
→ AB oder RB können nicht berücksichtigt werden 

<|ref|>table_caption<|/ref|><|det|>[[105, 296, 325, 305]]<|/det|>
Tabelle 1: Exponentielle Fourier-Transformationen 

<|ref|>text<|/ref|><|det|>[[105, 307, 210, 316]]<|/det|>
Hinweis: a > 0, b > 0 

<|ref|>text<|/ref|><|det|>[[105, 316, 470, 332]]<|/det|>
Bei den Korrespondenzen Nr. 15 bis Nr. 23 handelt es sich um die Fourier-Transformationen sog. „verallgemeinerter“ Funktionen (Distributionen). 

<|ref|>table<|/ref|><|det|>[[105, 336, 470, 600]]<|/det|>
<table><tr><td>Originalfunktion f(t)</td><td>Bildfunktion F(ω)</td></tr><tr><td>o(t - a) - o(t - b) =</td><td></td></tr><tr><td>\(= \begin{cases} 1 & a \le t \le b \\ 0 & \text{alle übrigen } t \end{cases}\)</td><td>j \(\cdot \frac{e^{-jb\omega} - e^{-ja\omega}}{\omega}\)</td></tr><tr><td>(mit a &lt; b)</td><td></td></tr><tr><td>o(t + a) - o(t - a) =</td><td></td></tr><tr><td>\(= \begin{cases} 1 & |t| \le a \\ 0 & \text{alle übrigen } t \end{cases}\)</td><td>2 \(\cdot \sin (a\omega)\)</td></tr><tr><td>o(t + a) - o(t) =</td><td></td></tr><tr><td>\(= \begin{cases} 1 & -a \le t \le 0 \\ 0 & \text{alle übrigen } t \end{cases}\)</td><td>\(j \cdot \frac{1 - e^{ja\omega}}{\omega}\)</td></tr><tr><td>o(t) - o(t - a) =</td><td></td></tr><tr><td>\(= \begin{cases}\text{1} & 0 \le t \le a \\ 0 & \text{alle übrigen } t \end{cases} \quad j \cdot \frac{e^{-ja\omega} - 1}{\omega}\)</td><td></td></tr><tr><td>\(= \begin{cases} a - |t| & |t| \le a \\ 0 & \text{alle übrigen }t \end{cases} \quad \frac{2[1 - \cos (a\omega)]}{\omega^2}\)</td><td></td></tr><tr><td>\(= \begin{cases} 1 & \frac{\pi}{a} \cdot e^{-a|\omega|} \\ 0 & \text{alle übrigen } t \end{cases} \quad \frac{\pi}{a} \cdot e^{-a|\omega|}\)</td><td></td></tr></table>

<|ref|>table_caption<|/ref|><|det|>[[520, 291, 707, 300]]<|/det|>
Tabelle 2: Fourier-Sinus-Transformationen 

<|ref|>text<|/ref|><|det|>[[520, 303, 633, 312]]<|/det|>
Hinweis: a &gt; 0, b &gt; 0 

<|ref|>table<|/ref|><|det|>[[520, 316, 878, 600]]<|/det|>
<table><tr><td>Originalfunktion f(t)</td><td>Bildufunkion F2(ω)</td></tr><tr><td>o(t) - o(t - a) =</td><td></td></tr><tr><tr><td>(1) \(= \begin{cases} 1 & 0 \le t \le a \\ 0 & \text{alle übrige } t \end{cases} \quad \frac{1 - \cos (a\omega)}{\omega}\)</td><td></td></tr><tr><td>(2) \(\frac{1}{t}\)</td><td>\(\frac{\pi}{2}\)</td></tr><tr><td>(3) \(\frac{1}{\sqrt{t}}\)</td><td>\(\sqrt{\frac{\pi}{2\omega}}\)</td></tr><tr><td>(4) \(\frac{t}{a^2 + t^2}\)</td><td>\(\frac{\pi}{2} \cdot e^{-a\omega}\)</td></tr><tr><td>(5) \(e^{-at}\)</td><td>\(\frac{\omega}{a^2 + \omega^2}\)</td></tr><tr><td>(6) \(t \cdot e^{-at}\)</td><td>\(\frac{2a\omega}{(a^2 + \omega^2)^2}\)</td></tr><tr><td>(7) \(t \cdot e^{-at^2}\)</td><td>\(\frac{1}{4a} \cdot \sqrt{\frac{\pi}{a}} \cdot \omega \cdot e^{-\frac{a^2}{4a}}\)</td></tr><tr><td>(8) \(\frac{\sin (at)}{t}\)</td><td>\(\frac{1}{2} \cdot \ln \left| \frac{a + \omega}{a - \omega} \right|\)</td></tr><tr><td>(9) \(e^{-bt} \cdot \sin (at)\)</td><td>\(\frac{b}{2} \left[ \frac{1}{b^2 + (a - \omega)^2} - \frac{1}{b^2 + (a + \omega)^2} \right]\)</td></tr><tr><td>(10) \(\frac{e^{-bt} \cdot \sin (at)}{t}\)</td><td>\(\frac{1}{4} \cdot \ln \left( \frac{b^2 + (\omega + a)^2}{b^2 + (\omega - a)^2} \right)\)</td></tr></table>

<|ref|>table_caption<|/ref|><|det|>[[520, 611, 714, 620]]<|/det|>
Tabelle 3: Fourier-Kosinus-Transformationen 

<|ref|>text<|/ref|><|det|>[[520, 622, 633, 631]]<|/det|>
Hinweis: a &gt; 0, b &gt; 1 

<|ref|>table<|/ref|><|det|>[[520, 635, 878, 960]]<|/det|>
<table><tr><td>Originalfunktion f(t)</td><td>Bildfunktion Fc(ω)</td></tr><tr><td>o(t) - o(t - a) =</td><td>\(\frac{\sin (a\omega)}{\omega}\)</td></tr><tr><td>(1) \(= \begin{cases} 1 & 0 \le t & \le a \\ 0 & \text{alle übrigen } t \end{cases}\quad \frac{1}{2\omega}\)</td><td></td></tr><tr><td>(2) \(\frac{1}{\sqrt{t}}\)</td><td>\(\frac{\pi}{2\omega}\)</td></tr><tr><td>(3) \(\frac{1}{a^2 + t^2}\)</td><td>\(\frac{\pi}{2a} \cdot e^{-a\omega}\)</td></tr><tr><td>(4) \(e^{-at}\)</td><td>\(\frac{a}{a^2 + \omega^2}\)</td></tr><tr><td>(5) \(t \cdot e^{-at}\)</td><td>\(\frac{a^2 - \omega^2}{(a^2 + \omega^2)^2}\)</td></tr><tr><td>(6) \(e^{-at^2}\)</td><td>\(\frac{1}{2} \sqrt{\frac{\pi}{a}} \cdot e^{-\frac{a^2}{4a}}\)</td></tr><tr><td>(7) \(\frac{\sin (at)}{t}\)</td><td>\(\begin{cases} \pi/2 & \omega < a \\ \pi/4 & \text{für } \omega = a \\ 0 & \omega > a \end{cases}\)</td></tr><tr><td>(8) \(e^{-bt} \cdot \sin (at)\)</td><td>\(\frac{1}{2} \left[ \frac{a + \omega}{b^2 + (a + \omega)^2} + \frac{a - \omega}{b^2 + (a - \omega)^2} \right]\)</td></tr><tr><td>(9) \(e^{-bt} \cdot \cos (at)\)</td><td>\(\frac{b}{2} \left[ \frac{1}{a^2 + (a - \omega)^2} + \frac{1}{b^2 + (a + \omega)^2} \right] \)</td></tr><tr><td>(10) \(\frac{\sin (at^2)}{t}\)</td><td>\(\frac{1}{2} \sqrt{\frac{\pi}{2a}} \left[ \cos \left( \frac{\omega^2}{4a} \right) - \sin \left( \frac{\omega^2}{4a} \right) \right]\)</td></tr><tr><td>(11) \(\cos (at^2)\)</td><td>\(\frac{1}{2} \sqrt{\frac{\pi}{2a}} [\cos \left( \frac{\omega^2}{4a} \right) + \sin \left( \frac{\omega^2}{4a} \right)]\)</td></tr></table>