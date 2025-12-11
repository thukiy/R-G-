<|ref|>sub_title<|/ref|><|det|>[[114, 98, 799, 117]]<|/det|>
5. Erwartungswert, Varianz, Standardabweichung stetiger Verteilungen 

<|ref|>text<|/ref|><|det|>[[114, 115, 829, 152]]<|/det|>
Die stetige Zufallsvariable X besitze die jeweils angegebene Dichtefunktion f(x).
Berechnen Sie den Mittelwert μ, die Varianz σ² und die Standardabweichung σ. 

<|ref|>text<|/ref|><|det|>[[114, 151, 397, 169]]<|/det|>
a) f(x) = const. = c (a ≤ x ≤ b) 

<|ref|>text<|/ref|><|det|>[[114, 167, 417, 185]]<|/det|>
b) f(x) = mx (0 ≤ x ≤ 10; m ∈ ℝ) 

<|ref|>equation<|/ref|><|det|>[[114, 200, 880, 832]]<|/det|>
\[
\begin{align*}
\text{a) Normierung: } \int_a^b c \, dx &= c \left[ x \right]_a^b = c (b - a) = 1 \quad \Rightarrow \quad c = \frac{1}{b - a} \\
\mu &= \frac{1}{b - a} \cdot \int_a^b x \, dx = \frac{1}{2(b - a)} \left[ x^2 \right]_a^b = \frac{b^2 - a^2}{2(b - a)} = \frac{(b + a)(b - a)}{2(b - a)} = \frac{1}{2}(a + b) \\
E(X^2) &= \frac{1}{b - a} \cdot \int_a^b x^2 \, dx = \frac{1}{3(b - a)} \left[ x^3 \right]_a^b = \frac{b^3 - a^3}{3(b - a)} = \\
&= \frac{(b - a)(a^2 + ab + b^2)}{3(b - a)} = \frac{1}{3}(a^2 + ab + b^2) \\
\text{NR: } (b^3 - a^3) : (b - a) &= a^2 + ab + b^2 \quad \text{(Polynomdivision)} \\
\sigma^2 &= E(X^2) - \mu^2 = \frac{1}{3}(a^2 + ab + b^2) - \frac{1}{4}(a + b)^2 = \\
&= \frac{4(a^2 + ab + b^2) - 3(a^2 + 2ab + b^2)}{12} = \\
&= \frac{4a^2 + 4ab + 4b^2 - 3a^2 - 6ab - 3b^2}{12} = \frac{a^2 - 2ab + b^2}{12} = \frac{1}{12}(a - b)^2 \\
\sigma &= 0.2887(b - a)
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[114, 614, 744, 833]]<|/det|>
\[
\begin{align*}
\text{b) Normierung: } \int_0^{10} m x \, dx &= \left[ \frac{1}{2} m x^2 \right]_0^{10} = 50m = 1 \quad \Rightarrow \quad m = \frac{1}{50} \\
\mu &= \int_0^{10} x \cdot \frac{1}{50} x \, dx = \frac{1}{50} \cdot \int_0^{10} x^2 \, dx = \frac{1}{150} \left[ x^3 \right]_0^{10} = \frac{20}{3} \\
E(X^2) &= \int_0^{10} x^2 \cdot \frac{1}{50} x \, dx = \frac{1}{50}\cdot \int_0^{10} x^3 \, dx = \frac{1}{200} \left[ x^4 \right]_0^{10} = 50 \\
\sigma^2 &= E(X^2) - \mu^2 = 50 - \frac{400}{9} = \frac{50}{9} = 5.5556; \quad \sigma = 2.3570
\end{align*}
\]