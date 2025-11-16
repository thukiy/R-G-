In expliziter Form erhalten wir daraus

$$
H_{k}=\left(\frac{4}{9}\right)^{k} H_{0} \approx\left(\frac{4}{9}\right)^{k} \cdot 20 \mathrm{~m} \text { für alle } k \in \mathbb{N}_{0}
$$

a) Wir suchen die Distanz $\Delta s$, welche der Basketball (nach oben und unten zusammengezählt) insgesamt zurücklegt, bevor er am Boden liegen bleibt. Dabei müssen wir berücksichtigen, dass der Basketball über die Anfangshöhe $H_{0}$ nur hinunterfällt, während er über alle anderen Höhen $H_{k}$ für $k \in \mathbb{N}^{+}$vor dem Hinunterfallen auch aufsteigen muss. Mit Hilfe der geometrischen Summen-Formel erhalten wir daher

$$
\begin{aligned}
\underline{\Delta s} & =H_{0}+\sum_{k=1}^{\infty} 2 H_{k}=H_{0}+\lim _{n \rightarrow \infty} \sum_{k=1}^{n} 2 H_{k}=H_{0}+\lim _{n \rightarrow \infty} \sum_{k=1}^{n} 2 \cdot\left(\frac{4}{9}\right)^{k} \cdot H_{0} \\
& =H_{0}+2 H_{0} \lim _{n \rightarrow \infty} \sum_{k=1}^{n}\left(\frac{4}{9}\right)^{k}=H_{0}+2 H_{0} \lim _{n \rightarrow \infty} G_{(1 ; n)}\left(\frac{4}{9}\right)=H_{0}+2 H_{0} \lim _{n \rightarrow \infty} \frac{\frac{4}{9}-\left(\frac{4}{9}\right)^{n+1}}{1-\frac{4}{9}} \\
& =H_{0}+2 H_{0} \cdot \frac{\frac{4}{9}-0}{1-\frac{4}{9}}=H_{0}+2 H_{0} \cdot \frac{\frac{4}{9}}{\frac{5}{9}}=H_{0}+2 H_{0} \cdot \frac{4}{9} \cdot \frac{9}{5}=H_{0}\left(1+\frac{8}{5}\right) \\
& =\frac{13}{5} H_{0} \approx \frac{13}{5} \cdot 20 \mathrm{~m}=\underline{52 \mathrm{~m}}
\end{aligned}
$$

b) Es sei $g \approx 10 \mathrm{~m} / \mathrm{s}^{2}$ die Fallbeschleunigung. Gemäss den klassischen Fallgesetzen aus der Physik sind Fallhöhe $H$ und Fallzeit $T$ verknüpft durch die Beziehung

$$
\begin{array}{rlrl} 
& H & =\frac{g}{2} T^{2} & \left\lvert\, \begin{array}{l}
\cdot \frac{2}{g}
\end{array}\right. \\
\Leftrightarrow & \frac{2}{g} H & =T^{2} & \mid \sqrt{\ldots}
\end{array}
$$

Daraus erhalten wir

$$
T=\sqrt{\frac{2 H}{g}}=\sqrt{\frac{2}{g}} \sqrt{H}
$$

Durch Einsetzen der Folgeglieder aus (77) in (79) erhalten wir die ebenfalls geometrische Folge der Fallzeiten, welche explizit gegeben ist durch

$$
\begin{aligned}
T_{k} & =\sqrt{\frac{2}{g}} \sqrt{H_{k}}=\sqrt{\frac{2}{g}} \sqrt{\left(\frac{4}{9}\right)^{k} H_{0}}=\sqrt{\frac{2}{g}} \sqrt{\left(\frac{4}{9}\right)^{k}} \sqrt{H_{0}}=\left(\sqrt{\frac{4}{9}}\right)^{k} \sqrt{\frac{2}{g}} \sqrt{H_{0}} \\
& =\left(\frac{2}{3}\right)^{k} \sqrt{\frac{2 H_{0}}{g}}=\left(\frac{2}{3}\right)^{k} T_{0} \text { für alle } k \in \mathbb{N} .
\end{aligned}
$$

Wir suchen die Dauer $\Delta t$ vom Zeitpunkt des Fallenlassens bis der Basketball auf dem Boden liegen bleibt. Dabei müssen wir berücksichtigen, dass der Basketball für den ersten Fall über die Höhe $H_{0}$ die Zeit $T_{0}$ benötigt, während die Dauer des Aufstieges und Falles über alle anderen Höhen $H_{k}$ für $k \in \mathbb{N}$ jeweils $2 T_{k}$ beträgt. Mit Hilfe der geometrischen Summen-Formel erhalten wir daher
$\underline{\Delta t}=T_{0}+\sum_{k=1}^{\infty} 2 T_{k}=T_{0}+\lim _{n \rightarrow \infty} \sum_{k=1}^{n} 2 T_{k}=T_{0}+\lim _{n \rightarrow \infty} \sum_{k=1}^{n} 2\left(\frac{2}{3}\right)^{k} T_{0}$