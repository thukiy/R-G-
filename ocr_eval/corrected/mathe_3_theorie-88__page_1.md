<|ref|>sub_title<|/ref|><|det|>[[33, 14, 357, 43]]<|/det|>
## Diskrete Verteilungen 

<|ref|>sub_title<|/ref|><|det|>[[45, 55, 265, 81]]<|/det|>
### • Gleichverteilung 

<|ref|>text<|/ref|><|det|>[[108, 92, 664, 118]]<|/det|>
jede Ausgang hat dieselbe wahrscheinlichkeit 

<|ref|>equation<|/ref|><|det|>[[160, 123, 550, 240]]<|/det|>
\[
f(x) = \begin{cases} \text{pi} = \frac{1}{m} & \text{i} = 1 \dots m \\ 0 & \text{sonst} \end{cases} \\
E(x) = \frac{1}{m} \sum_{i} x_i
\]

<|ref|>sub_title<|/ref|><|det|>[[45, 264, 682, 291]]<|/det|>
### • Benutze-Verteilung : nur 2 Auszüge möglich 

<|ref|>text<|/ref|><|det|>[[115, 300, 610, 327]]<|/det|>
ergbenis A mit wahrscheinlichkeit p 

<|ref|>equation<|/ref|><|det|>[[160, 332, 660, 490]]<|/det|>
\[
\begin{align*}
" & \quad \tilde{A} & " & \quad " & \quad " & \quad (1-p) \\
f(x) = \begin{cases} 1-p & x=0 \\ p & x=1 \\ 0 & \text{sonst} \end{cases} \\
E(x) = p & \delta^2 = p-p^2
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[75, 495, 936, 523]]<|/det|>
→ Grundlage für Binomial-, Poisson- und hypergeometrische Verteilung 

<|ref|>sub_title<|/ref|><|det|>[[45, 548, 936, 576]]<|/det|>
### Binomialverteilung : n-maliges Durchführen eines Bernoulli Experiments

<|ref|>equation<|/ref|><|det|>[[160, 581, 660, 698]]<|/det|>
\[
f(x) = \begin{cases} (\frac{n}{x}) \cdot p^x \cdot (1-p)^{n-x} & x = 1 \dots n \\ 0 & \text{sonst} \end{cases} \\
E(x) = n \cdot p & \delta^2 = n \cdot p \cdot (1-p)
\]

<|ref|>text<|/ref|><|det|>[[75, 704, 450, 730]]<|/det|>
→ Ziehen mit zurücklegen 

<|ref|>sub_title<|/ref|><|det|>[[45, 756, 493, 785]]<|/det|>
### Hypergeometrische Verteilung 

<|ref|>text<|/ref|><|det|>[[75, 795, 920, 863]]<|/det|>
→ Ziehen ohne zurücklegen : p ändert sich bei jeder Ziehung, Reihenfolge nicht relevant 

<|ref|>text<|/ref|><|det|>[[100, 875, 940, 939]]<|/det|>
• n Elemente aus N Elementen, wobei x die gewünschte Eigenschaft haben und die restlichen (n-x) nicht