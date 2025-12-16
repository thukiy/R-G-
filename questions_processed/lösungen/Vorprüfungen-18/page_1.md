<|ref|>text<|/ref|><|det|>[[20, 20, 820, 66]]<|/det|>
3) d) \(P(A_1|B) = \frac{P(B|A_1) \cdot P(A_1)}{P(B)}\) ... Saq von Beyes 

<|ref|>equation<|/ref|><|det|>[[132, 85, 700, 123]]<|/det|>
\[P(B) \text{ über totale Wahrscheinlichkeit}\]

<|ref|>equation<|/ref|><|det|>[[132, 120, 515, 167]]<|/det|>
\[P(B) = \sum_{k=1}^{3} P(B|A_k) \cdot P(A_k)\]

<|ref|>equation<|/ref|><|det|>[[132, 189, 737, 230]]<|/det|>
\[P(A_1|B) = \frac{0,1 \cdot 0,25}{0,1 \cdot 0,25 + 0,3 \cdot 0,3 + 0,5 \cdot 0,45} = 0,074 \approx 7,4\%\]

<|ref|>text<|/ref|><|det|>[[75, 281, 816, 315]]<|/det|>
e) Glücksrad : Binomialverteilung liegt vor 

<|ref|>equation<|/ref|><|det|>[[160, 317, 730, 355]]<|/det|>
\[P(r) = \frac{1}{6} \quad p(r) = \frac{1}{6} \quad n = 10\]

<|ref|>equation<|/ref|><|det|>[[129, 370, 620, 415]]<|/det|>
\[P(X=x) = \binom{n}{x} \cdot p^x \cdot (1-p)^{n-x}\]

<|ref|>equation<|/ref|><|det|>[[129, 412, 625, 460]]<|/det|>
\[P(X \ge 2) = \sum_{k=2}^{10} \binom{n}{k} \cdot p^k \cdot (1-p)^{n-k}\]

<|ref|>equation<|/ref|><|det|>[[255, 472, 960, 504]]<|/det|>
\[= 1 - P(X \le 1) = 1 - \binom{8}{1} \cdot p^1 \cdot (1-p)^8 - \binom{8}{2} \cdot p^2 \cdot (1-p)^7\]

<|ref|>equation<|/ref|><|det|>[[255, 512, 585, 543]]<|/det|>
\[= 1 - 4845 = 0,5155\]