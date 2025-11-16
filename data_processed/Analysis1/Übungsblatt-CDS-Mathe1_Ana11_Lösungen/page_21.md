f) Wir erhalten

$$
\begin{aligned}
\underline{I} & =\int_{u}^{-v}\left(2 w u-6 v w^{2}+1\right) \mathrm{d} w=\left.\left[u w^{2}-2 v w^{3}+w\right]\right|_{w=u} ^{w=-v} \\
& =u \cdot(-v)^{2}-2 v \cdot(-v)^{3}-v-u \cdot u^{2}+2 v \cdot u^{3}-u=u v^{2}+2 v^{4}-v-u^{3}+2 v u^{3}-u \\
& =\underline{2 v^{4}+2 u^{3} v-u^{3}+u v^{2}-u-v .}
\end{aligned}
$$

# 13. Aufleitung von eigentlichen Exponentialfunktionen 

Wir berechnen die folgenden unbestimmten Integrale durch elementares Aufleiten.
a) Wir erhalten

$$
\underline{F(x)}=\int \mathrm{e}^{x} \mathrm{~d} x=\underline{\underline{e}^{x}+c}
$$

b) Wir erhalten

$$
\underline{F(x)}=\int 2^{x} \mathrm{~d} x=\underline{\frac{1}{\ln (2)} \cdot 2^{x}+c}
$$

c) Wir zeigen zwei Varianten, um diese Teilaufgabe zu lösen.

Variante 1: Durch elementares Aufleiten erhalten wir

$$
\underline{F(x)}=\int \mathrm{e}^{-x} \mathrm{~d} x=-\mathrm{e}^{-x}+c=\underline{c-\mathrm{e}^{-x}}
$$

Variante 2: Durch Umformen des Integranden und elementares Aufleiten erhalten wir

$$
\begin{aligned}
\underline{F(x)} & =\int \mathrm{e}^{-x} \mathrm{~d} x=\int \frac{1}{\mathrm{e}^{x}} \mathrm{~d} x=\int\left(\frac{1}{\mathrm{e}}\right)^{x} \mathrm{~d} x=\frac{1}{\ln \left(\frac{1}{\mathrm{e}}\right)} \cdot\left(\frac{1}{\mathrm{e}}\right)^{x}+c=\frac{1}{-\ln (\mathrm{e})} \cdot \frac{1}{\mathrm{e}^{x}}+c \\
& =\frac{1}{-1} \cdot \mathrm{e}^{-x}+c=\underline{c-\mathrm{e}^{-x}}
\end{aligned}
$$

d) Wir zeigen zwei Varianten, um diese Teilaufgabe zu lösen.

Variante 1: Durch elementares Aufleiten erhalten wir

$$
\underline{F(x)}=\int 2^{-x} \mathrm{~d} x=-\frac{1}{\ln (2)} \cdot 2^{-x}+c=\underline{c-\frac{1}{\ln (2)} \cdot 2^{-x}}
$$

Variante 2: Durch Umformen des Integranden und elementares Aufleiten erhalten wir

$$
\begin{aligned}
\underline{F(x)} & =\int 2^{-x} \mathrm{~d} x=\int \frac{1}{2^{x}} \mathrm{~d} x=\int\left(\frac{1}{2}\right)^{x} \mathrm{~d} x=\frac{1}{\ln \left(\frac{1}{2}\right)} \cdot\left(\frac{1}{2}\right)^{x}+c=\frac{1}{-\ln (2)} \cdot \frac{1}{2^{x}}+c \\
& =-\frac{1}{\ln (2)} \cdot 2^{-x}+c=\underline{c-\frac{1}{\ln (2)} \cdot 2^{-x}}
\end{aligned}
$$