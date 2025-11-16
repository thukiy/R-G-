# 10. Ableitung von Area-Funktionen 

Wir verwenden die Ketten-Regel, um jeweils die Ableitung der folgenden Funktionen aus der Ableitung der Umkehrfunktion zu bestimmen.
a) Für alle $z \in \mathbb{R}$ gilt

$$
\operatorname{arsinh}(\sinh (z))=z
$$

und

$$
\cosh (z)=\sqrt{1+\sinh ^{2}(z)}
$$

Durch beidseitiges Ableiten von (70) mit Hilfe der Ketten-Regel erhalten wir

$$
\begin{aligned}
& \operatorname{arsinh}^{\prime}(\sinh (z)) \cdot \sinh ^{\prime}(z)=z^{\prime} \\
& \Rightarrow \quad \operatorname{arsinh}^{\prime}(\sinh (z)) \cdot \cosh (z)=1 \quad \mid: \cosh (z) \\
& \Rightarrow \quad \operatorname{arsinh}^{\prime}(\sinh (z))=\frac{1}{\cosh (z)}=\frac{1}{\sqrt{1+\sinh ^{2}(z)}}
\end{aligned}
$$

Durch die Substitution $x:=\sinh (z)$ erhalten wir für alle $x \in \mathbb{R}$ die Areasinus-HyperbolicusAbleitung

$$
\underline{\operatorname{arsinh}^{\prime}(x)=\frac{1}{\sqrt{1+x^{2}}}}
$$

b) Für alle $z \in \mathbb{R}_{0}^{+}$gilt

$$
\operatorname{arcosh}(\cosh (z))=z
$$

und

$$
\sinh (z)>0 \Rightarrow \sinh (z)=\sqrt{\cosh ^{2}(z)-1}
$$

Durch beidseitiges Ableiten von (76) mit Hilfe der Ketten-Regel erhalten wir

$$
\begin{aligned}
& \operatorname{arcosh}^{\prime}(\cosh (z)) \cdot \cosh ^{\prime}(z)=z^{\prime} \\
& \Rightarrow \quad \operatorname{arcosh}^{\prime}(\cosh (z)) \cdot \sinh (z)=1 \quad \mid: \sinh (z) \\
& \Rightarrow \quad \operatorname{arcosh}^{\prime}(\cosh (z))=\frac{1}{\sinh (z)}=\frac{1}{\sqrt{\cosh ^{2}(z)-1}}
\end{aligned}
$$

Durch die Substitution $x:=\cosh (z)$ erhalten wir für alle $x \in[1, \infty[$ die AreacosinusHyperbolicus-Ableitung

$$
\underline{\operatorname{arcosh}^{\prime}(x)=\frac{1}{\sqrt{x^{2}-1}}}
$$