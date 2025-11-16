\# Parameter:
$f=(x+1) * 2 * * x ;$
Gemäss Ausgabe erhalten wir die Ableitung
$\underline{f^{\prime}(s)=2^{x} \cdot((x+1) \cdot \ln (2)+1)}$.
f) Wir modifizieren den Code.
\# Parameter:
$f=(x+1) * 3 * *(-x * * 2)$;
Gemäss Ausgabe erhalten wir die Ableitung
$\underline{f^{\prime}(x)=3^{-x^{2}} \cdot(-x \cdot(x+1) \cdot \ln (9)+1)}$.

# 8. Diverse Ableitungen 

Wir berechnen jeweils die Ableitung der angegebenen Funktion.
a) Wir betrachten die Funktion
$f(x)=5^{x^{3}-\sqrt{x}+7}$.
Mit Hilfe der Ketten-Regel erhalten wir
$\underline{f^{\prime}(x)}=\left(x^{3}-\sqrt{x}+7\right)^{\prime} \cdot \ln (5) \cdot 5^{x^{3}-\sqrt{x}+7}=\underbrace{\left(3 x^{2}-\frac{1}{2 \sqrt{x}}\right) \cdot \ln (5) \cdot 5^{x^{3}-\sqrt{x}+7}}_{\text {. }}$
b) Wir betrachten die Funktion
$f(x)=\log _{2}\left(9 x^{2}-4\right)$.
Mit Hilfe der Ketten-Regel erhalten wir

$$
\begin{aligned}
\underline{f^{\prime}(x)} & =\left(9 x^{2}-4\right)^{\prime} \cdot \log _{2}^{\prime}\left(9 x^{2}-4\right)=\left(9 \cdot 2 x^{2-1}-0\right) \cdot \frac{1}{\ln (2) \cdot\left(9 x^{2}-4\right)} \\
& =\underline{\frac{18 x}{\ln (2) \cdot\left(9 x^{2}-4\right)}}
\end{aligned}
$$

c) Wir betrachten die Funktion

$$
\begin{aligned}
f(x) & =\sqrt[4]{\ln \left(x^{256}\right)}=\sqrt[4]{\ln \left(|x|^{256}\right)}=\sqrt[4]{256 \cdot \ln (|x|)}=\sqrt[4]{256} \cdot \sqrt[4]{\ln (|x|)}=4 \cdot \sqrt[4]{\ln (|x|)} \\
& =4 \cdot(\ln (|x|))^{\frac{1}{4}}
\end{aligned}
$$

Mit Hilfe der Ketten-Regel erhalten wir
$\underline{f^{\prime}(x)}=4 \cdot \frac{1}{4} \cdot(\ln (|x|))^{\frac{1}{4}-1} \cdot(\ln (|x|))^{\prime}=(\ln (|x|))^{-\frac{3}{4}} \cdot \frac{1}{x}=\frac{1}{x \cdot \sqrt[4]{\ln ^{3}(|x|)}}$.