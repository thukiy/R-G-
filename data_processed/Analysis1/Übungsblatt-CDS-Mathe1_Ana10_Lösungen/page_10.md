c) Für alle $z \in \mathbb{R}$ gilt

$$
\operatorname{artanh}(\tanh (z))=z
$$

Durch beidseitiges Ableiten von (82) mit Hilfe der Ketten-Regel erhalten wir

$$
\begin{aligned}
& \operatorname{artanh}^{\prime}(\tanh (z)) \cdot \tanh ^{\prime}(z)=z^{\prime} \\
& \Rightarrow \quad \operatorname{artanh}^{\prime}(\tanh (z)) \cdot\left(1-\tanh ^{2}(z)\right)=1 \quad \mid:\left(1-\tanh ^{2}(z)\right) \\
& \Rightarrow \quad \operatorname{artanh}^{\prime}(\tanh (z))=\frac{1}{1-\tanh ^{2}(z)} .
\end{aligned}
$$

Durch die Substitution $x:=\tanh (z)$ erhalten wir für alle $x \in]-1,1[$ die Areatangens-Hyperbolicus-Ableitung

$$
\underline{\operatorname{artanh}^{\prime}(x)=\frac{1}{1-x^{2}}}
$$

d) Für alle $z \in \mathbb{R} \backslash\{0\}$ gilt

$$
\operatorname{arcoth}(\operatorname{coth}(z))=z
$$

Durch beidseitiges Ableiten von (87) mit Hilfe der Ketten-Regel erhalten wir

$$
\begin{aligned}
& \operatorname{arcoth}^{\prime}(\operatorname{coth}(z)) \cdot \operatorname{coth}^{\prime}(z)=z^{\prime} \\
& \Rightarrow \quad \operatorname{arcoth}^{\prime}(\operatorname{coth}(z)) \cdot\left(1-\operatorname{coth}^{2}(z)\right)=1 \quad \mid:\left(1-\operatorname{coth}^{2}(z)\right) \\
& \Rightarrow \quad \operatorname{arcoth}^{\prime}(\operatorname{coth}(z))=\frac{1}{1-\operatorname{coth}^{2}(z)} .
\end{aligned}
$$

Durch die Substitution $x:=\operatorname{coth}(z)$ erhalten wir für alle $x \in \mathbb{R} \backslash]-1,1[$ die Areacotangens-Hyperbolicus-Ableitung

$$
\underline{\operatorname{arcoth}^{\prime}(x)=\frac{1}{1-x^{2}}}
$$

# 11. Diverse Ableitungen berechnen 

Wir berechnen jeweils die Ableitung der angegebenen Funktion.
a) Wir betrachten die Funktion

$$
f(x)=\frac{x^{6}}{3}-\frac{x^{15}}{5}-\mathrm{e}^{14}
$$

Mit Hilfe der Summen-Regel, der Faktor-Regel und der Monom-Ableitung erhalten wir

$$
\underline{f^{\prime}(x)}=\frac{1}{3} \cdot 6 x^{6-1}-\frac{1}{5} \cdot 15 x^{15-1}-0=2 x^{5}-3 x^{14}=\underline{x^{5} \cdot\left(2-3 x^{9}\right)}
$$