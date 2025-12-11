<|ref|>text<|/ref|><|det|>[[90, 65, 890, 103]]<|/det|>
c) Aufgrund unserer Ergebnisse aus Teilaufgabe a) vermuten wir, dass die Folge \(a_n\) nach oben beschränkt ist durch die obere Schranke \(a_0 := 2\). Für alle \(n \in \mathbb{N}\) gilt offensichtlich 

<|ref|>equation<|/ref|><|det|>[[117, 112, 888, 152]]<|/det|>
\[ \frac{a_n}{n} = \frac{2n}{n+1} \le \frac{2n+2}{n+1} = \frac{2(n+1)}{n+1} = 2 = a_0. \qquad (5) \]

<|ref|>text<|/ref|><|det|>[[90, 163, 867, 183]]<|/det|>
d) Durch gleichnamig machen und Subtrahieren der Brüche erhalten wir die Abschätzung 

<|ref|>equation<|/ref|><|det|>[[117, 191, 888, 281]]<|/det|>
\[ \begin{aligned} \frac{a_{n+1} - a_n}{n} &= \frac{2(n+1)}{(n+1)+1} - \frac{2n}{n+1} = \frac{2n+2}{n+2} - \frac{2n}{n+1} = \frac{(2n+2)(n+1) - 2n(n+2)}{(n+2)(n+1)} \\ &= \frac{2n^2 + 2n + 2n + 2 - 2n^2 - 4n}{(n+2)(n+1)} = \frac{2}{(n+2)(n+1)} \ge \frac{0_e}{2}. \end{aligned} \qquad (6) \]

<|ref|>text<|/ref|><|det|>[[90, 290, 890, 327]]<|/det|>
e) Durch Ausklammern in Zähler und Nenner eines Faktors \(n\) und Kürzen in (1) finden wir den Grenzwert 

<|ref|>equation<|/ref|><|det|>[[117, 333, 888, 373]]<|/det|>
\[ a_n = \frac{2n}{n+1} = \frac{n \cdot 2}{n \cdot \left(\frac{n}{n} + \frac{1}{n}\right)} = \frac{2}{\frac{n}{n} + \frac{1}{n}} = \frac{2}{1 + \frac{1}{n}} \xrightarrow{n \to \infty} \frac{2}{1+0} = 2. \qquad (7) \]

<|ref|>text<|/ref|><|det|>[[117, 381, 660, 401]]<|/det|>
Die Folge \(a_n\) konvergiert demnach gegen den Grenzwert \(a = 2\). 

<|ref|>text<|/ref|><|det|>[[90, 411, 888, 466]]<|/det|>
f) Wir berechnen die Folge \(D_n\) der Abweichungen (Betrag der Differenz) der Folge \(a_n\) zum Grenzwert \(a = 2\) aus Teilaufgabe e). Durch gleichnamig machen und Subtrahieren der Brüche erhalten wir die Abschätzung 

<|ref|>equation<|/ref|><|det|>[[117, 475, 888, 561]]<|/det|>
\[ \begin{aligned} \frac{D_n}{n} &= \left|a - a_n\right| = \left|2 - \frac{2n}{n+1}\right| = \left|\frac{2(n+1) - 2n}{n+1}\right| = \left|\frac{2n+2 - 2n}{n+1}\right| = \left|\frac{2}{n+1}\right| \\ &= \frac{2}{\frac{n+1}{n}} \xrightarrow{n \to \infty} 0. \end{aligned} \qquad (8) \]

<|ref|>text<|/ref|><|det|>[[117, 574, 750, 594]]<|/det|>
Die Folge \(D_n\) konvergiert erwartungsgemäss gegen den Grenzwert \(D = 0\). 

<|ref|>text<|/ref|><|det|>[[90, 604, 890, 658]]<|/det|>
g) Wir suchen ein \(N \in \mathbb{N}\), so dass für alle \(n \ge N\) das Folgeglied \(a_n\) nicht weiter vom Grenzwert \(a = 2\) aus Teilaufgabe e) entfernt ist als die Vorgabe \(\varepsilon = 1/1'000'000\). Dazu betrachten wir den Ausdruck für die Abweichung aus Teilaufgabe f). Gemäss (8) muss gelten 

<|ref|>equation<|/ref|><|det|>[[363, 668, 888, 808]]<|/det|>
\[ \begin{aligned} D_N &= \left|a - a_N\right| \le \varepsilon \\ &\Leftrightarrow \frac{2}{N+1} \le \frac{1}{1'000'000} \quad \left| \frac{1}{(\ldots)} \right. \\ &\Leftrightarrow \frac{N+1}{2} \ge 1'000'000 \quad \left| \cdot 2 \right. \\ &\Leftrightarrow N+1 \ge 2'000'000 \quad \left| -1 \right. \end{aligned} \qquad (9) \qquad (10) \qquad (11) \qquad (12) \]

<|ref|>text<|/ref|><|det|>[[117, 817, 426, 836]]<|/det|>
Daraus erhalten wir die Bedingung 

<|ref|>equation<|/ref|><|det|>[[366, 848, 888, 868]]<|/det|>
\[ N \ge 2'000'000 - 1 = 1'999'999. \qquad (13) \]

<|ref|>text<|/ref|><|det|>[[117, 880, 845, 899]]<|/det|>
Das kleinste \(N \in \mathbb{N}\), welches diese Bedingung erfüllt ist offensichtlich \(N = 1'999'999\).