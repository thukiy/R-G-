# 6. Ableitung von Termen mit Beträgen 

Wir berechnen jeweils die Ableitung der gegebenen Funktion $f$ mit Hilfe geeigneter Ableitungsregeln.
a) Für alle $x \in \mathbb{R} \backslash\{0\}$ sei
$f(x)=|x|=\operatorname{sgn}(x) \cdot x$.
Mit Hilfe der Produktregel erhalten wir für $x \in \mathbb{R} \backslash\{0\}$ die Ableitung

$$
\underline{\underline{f^{\prime}(x)}}=\operatorname{sgn}^{\prime}(x) \cdot x+\operatorname{sgn}(x) \cdot x^{\prime}=0 \cdot x+\operatorname{sgn}(x) \cdot 1=\underline{\underline{\operatorname{sgn}(x)}}
$$

b) Für alle $x \in \mathbb{R} \backslash\{0\}$ sei
$f(x)=\sqrt{|x|}$.
Mit Hilfe der Wurzelregel und (39) erhalten wir für $x \in \mathbb{R} \backslash\{0\}$ die Ableitung

$$
\underline{\underline{f^{\prime}(x)}}=\frac{|x|^{\prime}}{2 \sqrt{|x|}}=\underline{\underline{\frac{\operatorname{sgn}(x)}{2 \sqrt{|x|}}}}
$$

c) Für alle $x \in \mathbb{R} \backslash\{0\}$ sei
$f(x)=\frac{1}{1+|x|}$.
Mit Hilfe der Reziproken-Regel und (39) erhalten wir für $x \in \mathbb{R} \backslash\{0\}$ die Ableitung

$$
\underline{\underline{f^{\prime}(x)}}=-\frac{(1+|x|)^{\prime}}{(1+|x|)^{2}}=-\frac{0+\operatorname{sgn}(x)}{(1+|x|)^{2}}=-\frac{\operatorname{sgn}(x)}{(1+|x|)^{2}}
$$

d) Für alle $x \in \mathbb{R}$ sei
$f(x)=\left|x^{3}\right|=\operatorname{sgn}\left(x^{3}\right) \cdot x^{3}=\operatorname{sgn}(x) \cdot x^{3}$.
Für die Berechnung der Ableitung von $f$ betrachten wir die Fälle $x \neq 0$ und $x=0$ getrennt.
Fall 1: $x \neq 0$. Mit Hilfe der Produkt-Regel erhalten wir

$$
f^{\prime}(x)=\operatorname{sgn}^{\prime}(x) \cdot x^{3}+\operatorname{sgn}(x) \cdot\left(x^{3}\right)^{\prime}=0 \cdot x^{3}+\operatorname{sgn}(x) \cdot 3 x^{2}=\operatorname{sgn}(x) \cdot 3 x^{2}
$$

Fall 2: $x=0$. Wir betrachten die einseitigen Grenzwerte

$$
\begin{aligned}
& \lim _{x \searrow 0} f^{\prime}(x)=\lim _{x \searrow 0}\left(\operatorname{sgn}(x) \cdot 3 x^{2}\right)=+1 \cdot 3 \cdot 0^{2}=0=\operatorname{sgn}(0) \cdot 3 \cdot 0^{2}=0 \\
& \lim _{x \nearrow 0} f^{\prime}(x)=\lim _{x \nearrow 0}\left(\operatorname{sgn}(x) \cdot 3 x^{2}\right)=-1 \cdot 3 \cdot 0^{2}=0=\operatorname{sgn}(0) \cdot 3 \cdot 0^{2}=0
\end{aligned}
$$

Demnach macht die Ableitung bei $x=0$ keinen Sprung.
Somit erhalten wir die Ableitung

$$
\underline{\underline{f^{\prime}(x)}=\operatorname{sgn}(x) \cdot 3 x^{2}} \quad \text { für alle } \quad x \in \mathbb{R}
$$