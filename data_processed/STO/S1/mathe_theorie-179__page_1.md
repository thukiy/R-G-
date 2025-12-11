<|ref|>text<|/ref|><|det|>[[40, 10, 777, 88]]<|/det|>
→ 2 hat selbe Einheit wie μ, kann von Vorteil sein;
0 ist durchschnittliche Abweichung, 

<|ref|>text<|/ref|><|det|>[[20, 106, 425, 135]]<|/det|>
andere Schreibweise für \(x^2\): 

<|ref|>equation<|/ref|><|det|>[[55, 145, 860, 300]]<|/det|>
\[
\begin{align*}
x^2 &= E((x-\mu)^2) = E(x^2 - 2x\mu + \mu^2) \\
&= E(x^2) - 2\mu \cdot E(x) + \mu^2 \cdot E(1) \\
&= E(x^2) - 2\mu^2 + \mu^2 = E(x^2) - \mu^2 = E(x^2) - [E(x)]^2
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[133, 304, 480, 332]]<|/det|>
Varianzverschiebungssatz 

<|ref|>text<|/ref|><|det|>[[15, 361, 630, 469]]<|/det|>
Bsp:  • Wur mit 3 w und 2s kugeln
3-mal ziehen mit zurücklegen
\(X =\) Anzahl des kugeln 

<|ref|>text<|/ref|><|det|>[[175, 497, 320, 525]]<|/det|>
Verteilung 

<|ref|>table<|/ref|><|det|>[[175, 530, 707, 630]]<|/det|>
<table><tr><td>\(x_i\)</td><td>0</td><td>1</td><td>2</td><td>3</td></tr><tr><td>\(f(x_i)\)</td><td>\(\frac{34}{125}\)</td><td>\(\frac{54}{125}\)</td><td>\(\frac{36}{125}\)</td><td>\(\frac{8}{125}\)</td></tr><tr><td></td><td>(\(\frac{3}{5}\))<sup>3</sup></td><td>3·\(\frac{5}{9}\)·(\(\frac{3}{5}\))<sup>2</sup></td><td>3·(\(\frac{3}{5}\))<sup>2</sup>·\(\frac{5}{9}\)</td><td>(\(\frac{3}{5}\))<sup>3</sup></td></tr></table>

<|ref|>equation<|/ref|><|det|>[[155, 667, 730, 771]]<|/det|>
\[
\begin{align*}
E(X) &= \sum_{i=1}^{4} x_i \cdot f(x_i) = 1 \cdot \frac{54}{125} + 2 \cdot \frac{36}{125} + 3 \cdot \frac{8}{125} \\
&= \frac{54 + 72 + 24}{125} = \frac{150}{125} = \frac{6}{5}
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[148, 785, 833, 900]]<|/det|>
\[
\begin{align*}
Var(X) &= \sigma^2 = \sum_{i=1}^{4} (x_i - \mu)^2 \cdot f(x_i) \\
&= \left(-\frac{6}{5}\right)^2 \cdot \frac{33}{125} + \left(-\frac{1}{5}\right)^2 \cdot \frac{54}{125} + \left(\frac{4}{5}\right)^2 \cdot \frac{36}{125} + \left(\frac{9}{5}\right)^2 \cdot \frac{8}{125} \\
&= \frac{18}{25} = 0,72
\end{align*}
\]