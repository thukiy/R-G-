<|ref|>text<|/ref|><|det|>[[179, 10, 899, 80]]<|/det|>
b) es befinden sich jeweils \(n_1, n_2, \dots, n_k\) gleiche Elemente unter \(n\) Elementen: 

<|ref|>equation<|/ref|><|det|>[[265, 75, 760, 156]]<|/det|>
\[P(n; n_1, \dots, n_k) = \frac{n!}{n_1! \cdot n_2! \cdot \dots \cdot n_k!}\]

<|ref|>equation<|/ref|><|det|>[[265, 128, 755, 156]]<|/det|>
\[n_1 + n_2 + \dots + n_k = n \quad k \le n\]

<|ref|>text<|/ref|><|det|>[[20, 184, 680, 214]]<|/det|>
Bsp: 6 Kugeln: 3 weiss, 2 grau, 1 schwarz 

<|ref|>equation<|/ref|><|det|>[[181, 223, 675, 250]]<|/det|>
\[n = 6 \quad n_1 = 3 \quad n_2 = 2 \quad n_3 = 1\]

<|ref|>equation<|/ref|><|det|>[[145, 255, 848, 299]]<|/det|>
\[P(6; 1, 2, 3) = \frac{6!}{1! \cdot 2! \cdot 3!} = \frac{3! \cdot 4 \cdot 5 \cdot 6}{1 \cdot 2 \cdot 3!} = \frac{24 \cdot 5 \cdot 6}{2} = 60\]

<|ref|>equation<|/ref|><|det|>[[30, 320, 490, 391]]<|/det|>
\[(n+1)! = n! (n+1) \quad n \in \mathbb{N}\]

<|ref|>text<|/ref|><|det|>[[30, 435, 360, 466]]<|/det|>
Auswahlprobleme 

<|ref|>sub_title<|/ref|><|det|>[[50, 476, 319, 508]]<|/det|>
## Kombinationen 

<|ref|>text<|/ref|><|det|>[[100, 516, 940, 625]]<|/det|>
Um mit \(n\) Kugeln, von denen \(k\) gezogen werden und die Reihenfolge wird nicht berücksichtigt. Die \(k\) Kugeln bilden eine Kombination. 

<|ref|>text<|/ref|><|det|>[[160, 633, 820, 667]]<|/det|>
a) ohne Zurücklegen / ohne Wiederholung: 

<|ref|>text<|/ref|><|det|>[[220, 671, 878, 703]]<|/det|>
jede Kugeln kann nur 1 mal gezogen werden 

<|ref|>text<|/ref|><|det|>[[220, 707, 925, 797]]<|/det|>
Anzahl Kombinationen \(C(n; k) = \binom{n}{k}\) \(k \le n\)

<|ref|>equation<|/ref|><|det|>[[590, 737, 925, 792]]<|/det|>
\[= \frac{n!}{k! (n-k)!} \quad \text{Binomialkoeffizient}\]

<|ref|>text<|/ref|><|det|>[[160, 825, 744, 860]]<|/det|>
b) mit Zurücklagen / Wiederholung: 

<|ref|>text<|/ref|><|det|>[[220, 864, 920, 955]]<|/det|>
jede Kugel kann mehrmals gezogen werden

\[C_w(n; k) = \binom{n+k-1}{k} = \frac{(n+k-1)!}{k!(n-1)!} \quad k > n\]

<|ref|>text<|/ref|><|det|>[[781, 928, 925, 955]]<|/det|>
ist möglich