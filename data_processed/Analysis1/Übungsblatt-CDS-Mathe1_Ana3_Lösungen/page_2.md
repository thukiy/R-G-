c) Aufgrund unserer Ergebnisse aus Teilaufgabe a) vermuten wir, dass die Folge $a_{n}$ nach oben beschränkt ist durch die obere Schranke $a_{\mathrm{O}}:=2$. Für alle $n \in \mathbb{N}$ gilt offensichtlich
$\underline{\underline{a_{n}}}=\frac{2 n}{n+1} \leq \frac{2 n+2}{n+1}=\frac{2(n+1)}{n+1}=\underline{\underline{2=a_{\mathrm{O}}}}$
d) Durch gleichnamig machen und Subtrahieren der Brüche erhalten wir die Abschätzung

$$
\begin{aligned}
& \underline{\underline{a_{n+1}-a_{n}}}=\frac{2(n+1)}{(n+1)+1}-\frac{2 n}{n+1}=\frac{2 n+2}{n+2}-\frac{2 n}{n+1}=\frac{(2 n+2)(n+1)-2 n(n+2)}{(n+2)(n+1)} \\
& =\frac{2 n^{2}+2 n+2 n+2-2 n^{2}-4 n}{(n+2)(n+1)}=\frac{2}{(n+2)(n+1)} \geq \underline{\underline{0}}
\end{aligned}
$$

e) Durch Ausklammern in Zähler und Nenner eines Faktors $n$ und Kürzen in (1) finden wir den Grenzwert

$$
a_{n}=\frac{2 n}{n+1}=\frac{n \cdot 2}{n \cdot\left(\frac{n}{n}+\frac{1}{n}\right)}=\frac{2}{\frac{n}{n}+\frac{1}{n}}=\frac{2}{1+\frac{1}{n}} \xrightarrow{n \rightarrow \infty} \frac{2}{1+0}=2
$$

Die Folge $a_{n}$ konvergiert demnach gegen den Grenzwert $\underline{a=2}$.
f) Wir berechnen die Folge $D_{n}$ der Abweichungen (Betrag der Differenz) der Folge $a_{n}$ zum Grenzwert $a=2$ aus Teilaufgabe e). Durch gleichnamig machen und Subtrahieren der Brüche erhalten wir die Abschätzung

$$
\begin{aligned}
\underline{\underline{D_{n}}} & =\left|a-a_{n}\right|=\left|2-\frac{2 n}{n+1}\right|=\left|\frac{2(n+1)-2 n}{n+1}\right|=\left|\frac{2 n+2-2 n}{n+1}\right|=\left|\frac{2}{n+1}\right| \\
& =\frac{2}{\underline{n+1}} \xrightarrow{n \rightarrow \infty} 0
\end{aligned}
$$

Die Folge $D_{n}$ konvergiert erwartungsgemäss gegen den Grenzwert $\underline{D=0}$.
g) Wir suchen ein $N \in \mathbb{N}$, so dass für alle $n \geq N$ das Folgeglied $a_{n}$ nicht weiter vom Grenzwert $a=2$ aus Teilaufgabe e) entfernt ist als die Vorgabe $\varepsilon=1 / 1^{\prime} 000^{\prime} 000$. Dazu betrachten wir den Ausdruck für die Abweichung aus Teilaufgabe f). Gemäss (8) muss gelten

$$
\begin{aligned}
D_{N}=\left|a-a_{N}\right| & \leq \varepsilon \\
\Leftrightarrow & \frac{2}{N+1} & \leq \frac{1}{1^{\prime} 000^{\prime} 000} \\
\Leftrightarrow & \frac{N+1}{2} & \geq 1^{\prime} 000^{\prime} 000 \\
\Leftrightarrow & N+1 & \geq 2^{\prime} 000^{\prime} 000
\end{aligned} \quad \left\lvert\, \begin{aligned}
& \frac{1}{(\ldots)} \\
& \mid \cdot 2 \\
& \mid-1
\end{aligned}
$$

Daraus erhalten wir die Bedingung

$$
N \geq 2^{\prime} 000^{\prime} 000-1=1^{\prime} 999^{\prime} 999
$$

Das kleinste $N \in \mathbb{N}$, welches diese Bedingung erfüllt ist offensichtlich $\underline{N=1^{\prime} 999^{\prime} 999}$.