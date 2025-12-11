<|ref|>equation<|/ref|><|det|>[[140, 65, 852, 240]]<|/det|>
\[
\begin{align*}
&= \sqrt{3} \lim_{n \to \infty} \sum_{k=1}^{n} \left( \frac{1}{\sqrt{2}} \right)^k = \sqrt{3} \lim_{n \to \infty} G_{(1;n)} \left( \frac{1}{\sqrt{2}} \right) = \sqrt{3} \lim_{n \to \infty} \frac{\frac{1}{\sqrt{2}} - \left( \frac{1}{\sqrt{2}} \right)^{n+1}}{1 - \frac{1}{\sqrt{2}}} \\
&= \sqrt{3} \lim_{n \to \infty} \frac{\frac{2}{\sqrt{2}} - \left( \frac{1}{\sqrt{2}} \sqrt{2} \right)^{n+1}}{1 - \frac{1}{\sqrt{2}}} = \sqrt{3} \cdot \frac{\frac{1}{\sqrt{2}} - 0}{1 - \frac{1}{\sqrt{2}}} = \sqrt{3} \cdot 1 - \frac{\frac{1}{\sqrt{2}}}{\sqrt{2}} = \sqrt{3} \cdot \frac{\sqrt{2} \cdot \frac{1}{\sqrt{2}}}{\sqrt{2} \cdot \left( 1 - \frac{1}{\sqrt{2}} \right)} \\
&= \sqrt{3} \cdot \frac{1}{\sqrt{2} - \frac{\sqrt{2}}{\sqrt{2}}} = \frac{\sqrt{3}}{\sqrt{2} - 1} \approx 4.182.
\end{align*}
\]  

<|ref|>text<|/ref|><|det|>[[91, 252, 622, 272]]<|/det|>
f) Mit Hilfe der geometrischen Summen-Formel erhalten wir  

<|ref|>equation<|/ref|><|det|>[[115, 278, 884, 380]]<|/det|>
\[
\begin{align*}
L &= \sum_{k=0}^{\infty} \sqrt{\frac{3^k}{2}} = \lim_{n \to \infty} \sum_{k=0}^{n} \sqrt{\frac{3^k}{2}} = \lim_{n \to \infin} \sum_{k=0}^{n} \sqrt{\frac{3^k}{2} = \lim_{n \to \infin} \frac{1}{\sqrt{2}} \sum_{k=0}^{n} \left(\sqrt{3}\right)^k} \\
&= \frac{1}{\sqrt{2}} \lim_{n \to \infty} G_{(0;n)} \left(\sqrt{3}\right) = \frac{1}{\sqrt{2}} \lim_{n \to \infty} \frac{1 - \left(\sqrt{3}\right)^{n+1}}{1 - \sqrt{3}}.
\end{align*}
\]  

<|ref|>text<|/ref|><|det|>[[118, 384, 887, 439]]<|/det|>
Die geometrische Reihe ist offensichtlich divergent, denn \(\sqrt{3} > 1\) und für \(n \to \infty\) gilt somit
\[
\left(\sqrt{3}\right)^{n+1} \to \infty.
\]  

<|ref|>sub_title<|/ref|><|det|>[[76, 464, 450, 483]]<|/det|>
17. Aussagen über geometrische Reihen 

<|ref|>text<|/ref|><|det|>[[76, 483, 819, 503]]<|/det|>
Es seien \(m \in \mathbb{N}\) und \(x \in \mathbb{R} \setminus \{0, 1\}\). Wir betrachten die allgemeine geometrische Reihe 

<|ref|>equation<|/ref|><|det|>[[445, 510, 886, 555]]<|/det|>
\[
\sum_{k=m}^{\infty} x^k. \qquad (75)
\]

<|ref|>table<|/ref|><|det|>[[76, 565, 888, 774]]<|/det|>
<table><tr><td>Welche der folgenden Aussagen sind wahr und welche falsch?</td><td>wahr</td><td>falsch</td></tr><tr><td>a) Für \(x > 1\) divergiert die geometrische Reihe in jedem Fall.</td><td>●</td><td>○</td></tr><tr><td>b) Für \(x < 1\) konvergiert die geometrische Reihe in jedem Fall.</td><td>○</td><td>●</td></tr><tr><td>c) Für \(x = 2\) konvergiert die geometrische Reihe gegen \(\infty\).</td><td>○</td><td>●</td></tr><tr><td>d) Für \(x = 0.5\) und \(m = 0\) konvergiert die geometrische Reihe gegen 2.</td><td>●</td><td>○</td></tr><tr><td>e) Um zu beurteilen, ob die geometrische Reihe konvergiert, muss man so-wohl \(x\) als auch \(m\) kennen.</td><td>○</td><td>●</td></tr><tr><td>f) Um den Grenzwert der geometrischen Reihe (falls ein solcher existiert) berechnen zu können, muss man sowohl \(x\) als auch \(m\) kennen.</td><td>●</td><td>○</td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[76, 796, 330, 814]]<|/det|>
18. Springender Basketball 

<|ref|>text<|/ref|><|det|>[[76, 813, 887, 883]]<|/det|>
Ein Basketball fällt aus einer Höhe von 20 m frei auf den Boden und springt immer wieder von diesem auf. Bei jedem Aufspringen erreicht er 4/9 der Höhe aus welcher er unmittelbar davor heruntergefallen ist. Die Fallhöhen bilden somit eine geometrische Folge, rekursiv definiert durch 

<|ref|>equation<|/ref|><|det|>[[255, 887, 884, 923]]<|/det|>
\[
H_0 := 20 \text{ m und } H_{k+1} := \frac{4}{9} H_k \text{ für alle } k \in \mathbb{N}_0. \qquad (76)
\]