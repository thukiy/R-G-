$$
\begin{aligned}
& =\sqrt{3} \lim _{n \rightarrow \infty} \sum_{k=1}^{n}\left(\frac{1}{\sqrt{2}}\right)^{k}=\sqrt{3} \lim _{n \rightarrow \infty} G_{(1 ; n)}\left(\frac{1}{\sqrt{2}}\right)=\sqrt{3} \lim _{n \rightarrow \infty} \frac{\frac{1}{\sqrt{2}}-\left(\frac{1}{\sqrt{2}}\right)^{n+1}}{1-\frac{1}{\sqrt{2}}} \\
& =\sqrt{3} \lim _{n \rightarrow \infty} \frac{\frac{1}{\sqrt{2}}-\frac{1}{(\sqrt{2})^{n+1}}}{1-\frac{1}{\sqrt{2}}}=\sqrt{3} \cdot \frac{\frac{1}{\sqrt{2}}-0}{1-\frac{1}{\sqrt{2}}}=\sqrt{3} \cdot \frac{\frac{1}{\sqrt{2}}}{1-\frac{1}{\sqrt{2}}}=\sqrt{3} \cdot \frac{\sqrt{2} \cdot \frac{1}{\sqrt{2}}}{\sqrt{2} \cdot\left(1-\frac{1}{\sqrt{2}}\right)} \\
& =\sqrt{3} \cdot \frac{1}{\sqrt{2}-\frac{\sqrt{2}}{\sqrt{2}}}=\underline{\frac{\sqrt{3}}{\sqrt{2}-1} \approx 4.182}
\end{aligned}
$$

f) Mit Hilfe der geometrischen Summen-Formel erhalten wir

$$
\begin{aligned}
\underline{I}_{2} & =\sum_{k=0}^{\infty} \sqrt{\frac{3^{k}}{2}}=\lim _{n \rightarrow \infty} \sum_{k=0}^{n} \sqrt{\frac{3^{k}}{2}}=\lim _{n \rightarrow \infty} \sum_{k=0}^{n} \frac{\sqrt{3^{k}}}{\sqrt{2}}=\lim _{n \rightarrow \infty} \frac{1}{\sqrt{2}} \sum_{k=0}^{n}(\sqrt{3})^{k} \\
& =\frac{1}{\sqrt{2}} \lim _{n \rightarrow \infty} G_{(0 ; n)}(\sqrt{3})=\frac{1}{\sqrt{2}} \lim _{n \rightarrow \infty} \frac{1-(\sqrt{3})^{n+1}}{1-\sqrt{3}}
\end{aligned}
$$

Die geometrische Reihe ist offensichtlich divergent, denn $\sqrt{3}>1$ und für $n \rightarrow \infty$ gilt somit $(\sqrt{3})^{n+1} \rightarrow \infty$.

# 17. Aussagen über geometrische Reihen 

Es seien $m \in \mathbb{N}$ und $x \in \mathbb{R} \backslash\{0,1\}$. Wir betrachten die allgemeine geometrische Reihe

$$
\sum_{k=m}^{\infty} x^{k}
$$

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) Für $x>1$ divergiert die geometrische Reihe in jedem Fall. | $\bullet$ | $\bigcirc$ |
| b) Für $x<1$ konvergiert die geometrische Reihe in jedem Fall. | $\bigcirc$ | $\bullet$ |
| c) Für $x=2$ konvergiert die geometrische Reihe gegen $\infty$. | $\bigcirc$ | $\bullet$ |
| d) Für $x=0.5$ und $m=0$ konvergiert die geometrische Reihe gegen 2. | $\bullet$ | $\bigcirc$ |
| e) Um zu beurteilen, ob die geometrische Reihe konvergiert, muss man so- <br> wohl $x$ als auch $m$ kennen. | $\bigcirc$ | $\bullet$ |
| f) Um den Grenzwert der geometrischen Reihe (falls ein solcher existiert) <br> berechnen zu können, muss man sowohl $x$ als auch $m$ kennen. | $\bullet$ | $\bigcirc$ |

## 18. Springender Basketball

Ein Basketball fällt aus einer Höhe von 20 m frei auf den Boden und springt immer wieder von diesem auf. Bei jedem Aufspringen erreicht er $4 / 9$ der Höhe aus welcher er unmittelbar davor heruntergefallen ist. Die Fallhöhen bilden somit eine geometrische Folge, rekursiv definiert durch

$$
H_{0}:=20 \mathrm{~m} \quad \text { und } \quad H_{k+1}:=\frac{4}{9} H_{k} \quad \text { für alle } \quad k \in \mathbb{N}_{0} .
$$