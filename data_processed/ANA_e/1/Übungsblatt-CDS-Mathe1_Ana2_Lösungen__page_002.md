<|ref|>text<|/ref|><|det|>[[90, 66, 186, 85]]<|/det|>
c) Es gilt 

<|ref|>equation<|/ref|><|det|>[[315, 95, 888, 120]]<|/det|>
\[
\frac{f(5)}{5} = 4 \cdot 5 = \frac{20}{5} \quad \text{und} \quad \frac{f(9)}{9} = 4 \cdot 9 = \frac{36}{5}. \quad (5)
\]

<|ref|>text<|/ref|><|det|>[[90, 140, 446, 158]]<|/det|>
d) Durch Einsetzen von (5) erhalten wir 

<|ref|>equation<|/ref|><|det|>[[344, 170, 888, 195]]<|/det|>
\[
f(\{5, 9\}) = \{f(5), f(9)\} = \{20, 36\}. \quad (6)
\]

<|ref|>text<|/ref|><|det|>[[90, 215, 456, 234]]<|/det|>
e) Für die Bildmenge der Funktion \(f\) gilt 

<|ref|>equation<|/ref|><|det|>[[220, 245, 888, 304]]<|/det|>
\[
\begin{align*}
\frac{f(A)}{A} &= f(\{1, 3, 5, 7, 9, 11\}) = \{f(1), f(3), f(5), f(7), f(9), f(11)\} \\
&= \{4, 12, 20, 28, 36, 44\}.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[90, 328, 890, 365]]<|/det|>
f) Als alternative Zielmenge für die Funktion \(f\) taugt jede Menge \(\tilde{B}\), welche die Bildmenge \(f(A)\) aus (7) als Teilmenge enthält. Algebraisch ausgedrückt muss für \(\tilde{B}\) also gelten 

<|ref|>equation<|/ref|><|det|>[[453, 375, 888, 396]]<|/det|>
\[
f(A) \subseteq \tilde{B}. \qquad (8)
\]

<|ref|>text<|/ref|><|det|>[[117, 408, 890, 446]]<|/det|>
Die kleinste Menge \(\tilde{B}_{\text{min}}\) und die grösste reelle Zahlen-Menge \(\tilde{B}_{\text{max}}\), welche die Bedingung
(8) erfüllen sind 

<|ref|>equation<|/ref|><|det|>[[266, 457, 888, 481]]<|/det|>
\[
\tilde{B}_{\text{min}} = f(A) = \{4, 12, 20, 28, 36, 44\} \quad \text{und} \quad \tilde{B}_{\text{max}} = \mathbb{R}. \quad (9)
\]

<|ref|>text<|/ref|><|det|>[[90, 501, 890, 555]]<|/det|>
g) Wir suchen eine Funktion \(g\), welche \(B\) als Definitionsmenge und \(A\) als Zielmenge hat,
d.h. eine Funktion des Typs \(g: B \to A\). Dazu müssen wir eine Zuordnungsvorschrift \(g(x)\)
finden, welche jedem \(x \in B\) auf eindeutige Weise ein \(g(x) \in A\) zuordnet. 

<|ref|>text<|/ref|><|det|>[[117, 558, 890, 594]]<|/det|>
Variante 1: Die einfachste Möglichkeit ist die Wahl einer auf \(B\) konstanten Funktion mit
Funktionswert in \(A\). Es gilt \(7 \in A\), somit wäre ein Beispiel 

<|ref|>equation<|/ref|><|det|>[[431, 606, 888, 648]]<|/det|>
\[
\begin{align*}
g : B \to A \\
x \mapsto g(x) := 7.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[117, 663, 890, 715]]<|/det|>
Variante 2: Eine weitere Möglichkeit ist \(g\) auf dem Bild von \(f\) als Umkehrung von \(f\) zu
definieren und dann auf alle weiteren Elemente von \(B\) konstant fortzusetzen. Somit
wäre ein Beispiel 

<|ref|>equation<|/ref|><|det|>[[360, 728, 888, 800]]<|/det|>
\[
\begin{align*}
g : B \to A \\
x \mapsto g (x) := \begin{cases} x/4 & | x/4 \in A \\ 11 & | x/4 \notin A. \end{cases} \tag{11}
\end{align*}
\]