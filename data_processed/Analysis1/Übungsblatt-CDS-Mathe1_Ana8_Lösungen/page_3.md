# 3. Konsequenzen der Produkt-Regel 

Mit Hilfe der Produktregel der Differentialrechnung lassen sich einige weitere, nützliche Regeln herleiten.
a) Es sei $f$ eine Funktion der Form

$$
f(x)=a(x) \cdot b(x) \cdot c(x)=a(x) \cdot(b(x) \cdot c(x))
$$

Gemäss Produktregel gilt

$$
\begin{aligned}
\underline{\underline{f^{\prime}(x)}} & =a^{\prime}(x) \cdot(b(x) \cdot c(x))+a(x) \cdot(b(x) \cdot c(x))^{\prime} \\
& =a^{\prime}(x) \cdot b(x) \cdot c(x)+a(x) \cdot\left(b^{\prime}(x) \cdot c(x)+b(x) \cdot c^{\prime}(x)\right) \\
& =\underline{\underline{a^{\prime}(x)} \cdot b(x) \cdot c(x)+a(x) \cdot b^{\prime}(x) \cdot c(x)+a(x) \cdot b(x) \cdot c^{\prime}(x)} .
\end{aligned}
$$

b) Es sei $f$ eine Funktion der Form

$$
f(x)=h^{2}(x)=h(x) \cdot h(x)
$$

Mit Hilfe der Produktregel erhalten wir die Quadratregel, d.h.

$$
\underline{\underline{f^{\prime}(x)}}=h^{\prime}(x) \cdot h(x)+h(x) \cdot h^{\prime}(x)=\underline{\underline{2 \cdot h(x) \cdot h^{\prime}(x)}}
$$

c) Es sei $f$ eine Funktion der Form

$$
f(x)=\sqrt{h(x)}
$$

Durch Umformen, beidseitig Ableiten und Anwenden der Quadratregel aus Teilaufgabe b) erhalten wir

$$
\begin{aligned}
& f(x)=\sqrt{h(x)} \quad \mid(\ldots)^{2} \\
& \Rightarrow \quad f^{2}(x)=h(x) \quad \mid(\ldots)^{\prime} \\
& \Rightarrow \quad 2 \cdot f(x) \cdot f^{\prime}(x)=h^{\prime}(x) \quad \mid:(2 f(x)) .
\end{aligned}
$$

Es gilt also die Wurzelregel, d.h.

$$
\underline{\underline{f^{\prime}(x)}}=\frac{h^{\prime}(x)}{2 f(x)}=\underline{\underline{h^{\prime}(x)}} .
$$

d) Es sei $f$ eine Funktion der Form

$$
f(x)=\frac{1}{h(x)}
$$

Durch Umformen, beidseitig Ableiten und Anwenden der Produkt-Regel erhalten wir

$$
f(x)=\frac{1}{h(x)} \quad \mid \cdot h(x)
$$