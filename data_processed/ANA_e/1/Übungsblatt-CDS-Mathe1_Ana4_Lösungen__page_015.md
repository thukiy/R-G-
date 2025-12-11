<|ref|>text<|/ref|><|det|>[[107, 66, 446, 85]]<|/det|>
In expliziter Form erhalten wir daraus 

<|ref|>equation<|/ref|><|det|>[[312, 90, 922, 130]]<|/det|>
\[
H_k = \left( \frac{4}{9} \right)^k H_0 \approx \left( \frac{4}{9} \right)^k \cdot 20 \text{ m für alle } k \in \mathbb{N}_0. \quad (77)
\]

<|ref|>text<|/ref|><|det|>[[121, 142, 922, 230]]<|/det|>
a) Wir suchen die Distanz \(\Delta s\), welche der Basketball (nach oben und unten zusammengezählt) insgesamt zurücklegt, bevor er am Boden liegen bleibt. Dabei müssen wir berücksichtigen, dass der Basketball über die Anfangshöhe \(H_0\) nur hinunterfällt, während er über alle anderen Höhen \(H_k\) für \(k \in \mathbb{N}^+\) vor dem Hinunterfallen auch aufsteigen muss. Mit Hilfe der geometrischen Summen-Formel erhalten wir daher 

<|ref|>equation<|/ref|><|det|>[[149, 234, 922, 424]]<|/det|>
\[
\begin{align*}
\Delta s &= H_0 + \sum_{k=1}^{\infty} 2H_k = H_0 + \lim_{n \to \infty} \sum_{k=1}^{n} 2H_k = H_0 + \lim_{n \to \infty} 2 \cdot \left( \frac{4}{9} \right)^k \cdot H_0 \\
&= H_0 + 2H_0 \lim_{n \to \infty} \sum_{k=1}^{n} \left( \frac{4}{9} \right)^k = H_0 + 2H_0 \lim_{n \to \infty} G_{(1;n)} \left( \frac{4}{9} \right) = H_0 + 2H_0 \lim_{n \to \infty} \frac{\frac{4}{9} - \left( \frac{4}{9} \right)^{n+1}}{1 - \frac{4}{9}} \\
&= H_0 + 2H_0 \cdot \frac{\frac{4}{9} - 0}{1 - \frac{4}{9}} = H_0 + 2H_0 \cdot \frac{\frac{4}{9}}{5} = H_0 + 2H_0 \cdot \frac{4}{9} \cdot \frac{9}{5} = H_0 \left( 1 + \frac{8}{5} \right) \\
&= \frac{13}{5} H_0 \approx \frac{13}{5} \cdot 20 \text{ m} = 52 \text{ m}. \tag{78}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[121, 432, 922, 468]]<|/det|>
b) Es sei \(g \approx 10 \text{ m/s}^2\) die Fallbeschleunigung. Gemäss den klassischen Fallgesetzen aus der Physik sind Fallhöhe \(H\) und Fallzeit \(T\) verknüpft durch die Beziehung 

<|ref|>equation<|/ref|><|det|>[[540, 472, 920, 511]]<|/det|>
\[
H = \frac{g}{2} T^2 \qquad \left| \frac{2}{g} \right. \quad (79)
\]

<|ref|>equation<|/ref|><|det|>[[296, 516, 920, 555]]<|/det|>
\[
\Leftrightarrow \qquad \frac{2}{g} H = T^2 \qquad \left| \sqrt{\cdots} \right. \quad (80)
\]

<|ref|>text<|/ref|><|det|>[[149, 559, 330, 575]]<|/det|>
Daraus erhalten wir 

<|ref|>equation<|/ref|><|det|>[[430, 580, 920, 625]]<|/det|>
\[
T = \sqrt{\frac{2H}{g}} = \sqrt{\frac{2}{g}} \sqrt{H}. \quad (81)
\]

<|ref|>text<|/ref|><|det|>[[149, 631, 922, 668]]<|/det|>
Durch Einsetzen der Folgeglieder aus (77) in (79) erhalten wir die ebenfalls geometrische
Folge der Fallzeiten, welche explizit gegeben ist durch 

<|ref|>equation<|/ref|><|det|>[[149, 673, 920, 774]]<|/det|>
\[
\begin{align*}
T_k &= \sqrt{\frac{2}{g}} \sqrt{H_k} = \sqrt{\frac{2}{g}} \sqrt{\left( \frac{4}{9} \right)^k H_0} = \sqrt{\frac{2}{g}} \sqrt{\left( \frac{1}{9} \right)^k \sqrt{H_0}} = \left( \sqrt{\frac{4}{9}} \right)^k \sqrt{\frac{2}{g}} \sqrt{H_0} \\
&= \left( \frac{2}{3} \right)^k \sqrt{\frac{2H_0}{g}} = \left( \frac{2}{3} \right)^k T_0 \text{ für alle } k \in \mathbb{N}. \tag{82}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[149, 783, 922, 869]]<|/det|>
Wir suchen die Dauer \(\Delta t\) vom Zeitpunkt des Fallenlassens bis der Basketball auf dem
Boden liegen bleibt. Dabei müssen wir berücksichtigen, dass der Basketball für den ersten
Fall über die Höhe \(H_0\) die Zeit \(T_0\) benötigt, während die Dauer des Aufstieges und Falles
über alle anderen Höhen \(H_k\) für \(k \in \mathbb{N}\) jeweils \(2T_k\) beträgt. Mit Hilfe der geometrischen
Summen-Formel erhalten wir daher 

<|ref|>equation<|/ref|><|det|>[[149, 873, 712, 920]]<|/det|>
\[
\Delta t = T_0 + \sum_{k=1}^{\infty} 2T_k = T_0 + \lim_{n \to \infty} \sum_{k=1}^{2n} 2T_k = T_0 + \lim_{n \to \infty} 2 \left( \frac{2}{3} \right)^k T_0
\]