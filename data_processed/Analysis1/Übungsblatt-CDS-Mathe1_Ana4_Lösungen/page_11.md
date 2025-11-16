# 13. Martingale Strategie 

Als Martingale bezeichnet man folgende Strategie, um beim Roulette zu gewinnen.
§1 Es wird nur auf einfache Chancen gesetzt (z.B. Rot und Schwarz), das heisst, der gesetzte Betrag geht bei jedem Spiel entweder als gesamtes verloren oder wird im Gewinnfall durch die Bank verdoppelt.
§2 Nach jedem Verlust wird der Einsatz verdoppelt.
a) Der erste Einsatz betrage $E_{0}:=1 \mathrm{CHF}$ und jeder weitere Einsatz sei die Verdoppelung des jeweils unmittelbar Vorangegangenen, das heisst
$E_{k}=2 \cdot E_{k-1}=2 \cdot 2 \cdot E_{k-2}=\ldots=2^{k} \cdot E_{k-k}=2^{k} \cdot E_{0}$.
Der Gesamtverlust nach acht verlorenen Spielen beträgt demnach

$$
\begin{aligned}
\underline{V_{7}} & =\sum_{k=0}^{7} E_{k}=\sum_{k=0}^{7} 2^{k} \cdot E_{0}=E_{0} \sum_{k=0}^{7} 2^{k}=E_{0} \cdot G_{(0 ; 7)}(2)=E_{0} \cdot \frac{2^{0}-2^{8}}{1-2}=E_{0} \cdot \frac{1-256}{-1} \\
& =1 \mathrm{CHF} \cdot 255=\underline{255 \mathrm{CHF}}
\end{aligned}
$$

b) Wenn das neunte Spiel nach acht verlorenen Spielen gewonnen wird und der erste Einsatz einen Franken betrug, dann erhält der Spieler einen Gesamtgewinn von
$\underline{G}=E_{8}-V_{7}=2^{8} \cdot E_{0}-V_{7}=256 \cdot 1 \mathrm{CHF}-255 \mathrm{CHF}=\underline{1 \mathrm{CHF}}$.
c) Es sei $n \in \mathbb{N}^{*}$. Der Gesamtverlust nach $n$ verlorenen Spielen beträgt demnach

$$
\begin{aligned}
V_{n-1} & =\sum_{k=0}^{n-1} E_{k}=\sum_{k=0}^{n-1} 2^{k} \cdot E_{0}=E_{0} \sum_{k=0}^{n-1} 2^{k}=E_{0} \cdot G_{(0 ; n-1)}(2)=E_{0} \cdot \frac{2^{0}-2^{n}}{1-2}=E_{0} \cdot \frac{1-2^{n}}{-1} \\
& =\left(2^{n}-1\right) \cdot E_{0}
\end{aligned}
$$

Wird das Spiel $n+1$ gewonnen, dann beträgt der Gesamtgewinn
$\underline{G}=E_{n}-V_{n-1}=2^{n} \cdot E_{0}-\left(2^{n}-1\right) \cdot E_{0}=2^{n} \cdot E_{0}-2^{n} \cdot E_{0}+E_{0}=\underline{E_{0}>0}$.
Unabhängig von der Höhe des ersten Einsatzes gewinnt der Spieler nach $n$ verlorenen Spielen und einem gewonnenen Spiel $n+1$ insgesamt gerade den Betrag $E_{0}$.

## 14. Aussagen über eine spezielle Summe

Es sei $0<z<1$ und $n \in \mathbb{N}$. Wir betrachten die Summe

$$
S_{n}=\sum_{k=0}^{n} \frac{(-1)^{k+1}}{(1+z)^{k}}
$$

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) Es gilt $S_{0}<0$. | $\bullet$ | $\bigcirc$ |
| b) Es gibt ein $x \in \mathbb{R}$, so dass $S_{n}=-G_{(0 ; n)}(x)$ für alle $n \in \mathbb{N}^{+}$. | $\bullet$ | $\bigcirc$ |
| c) Für alle $n \in \mathbb{N}^{+}$gilt $S_{n+1}>S_{n}$. | $\bigcirc$ | $\bullet$ |
| d) Für alle $n \in \mathbb{N}^{+}$gilt $S_{n}<0$. | $\bullet$ | $\bigcirc$ |
| e) Ist $z \in \mathbb{Q}$, dann folgt $S_{n} \in \mathbb{Q}$ für alle $n \in \mathbb{N}$. | $\bullet$ | $\bigcirc$ |
| f) Für sehr grosse $n \in \mathbb{N}^{+}$gilt $S_{n} \approx-\frac{1+z}{2+z}$. | $\bullet$ | $\bigcirc$ |