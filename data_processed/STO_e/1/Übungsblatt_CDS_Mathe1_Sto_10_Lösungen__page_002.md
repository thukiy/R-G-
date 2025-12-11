<|ref|>equation<|/ref|><|det|>[[115, 81, 454, 113]]<|/det|>
a) \(f(x) = \frac{1}{16}x + b\) (0 ≤ x ≤ 4),

<|ref|>equation<|/ref|><|det|>[[115, 111, 395, 133]]<|/det|>
b) \(f(x) = c\) (a ≤ x ≤ b),

<|ref|>equation<|/ref|><|det|>[[115, 131, 460, 152]]<|/det|>
c) \(f(x) = a(1 + x)\) (-1 ≤ x ≤ 1).

<|ref|>text<|/ref|><|det|>[[115, 150, 577, 169]]<|/det|>
Ausserhalb der angegebenen Intervalle gilt f(x) = 0. 

<|ref|>equation<|/ref|><|det|>[[120, 183, 732, 234]]<|/det|>
a) \[\int_{0}^{4} \left( \frac{1}{16} x + b \right) dx = \left[ \frac{1}{32} x^2 + bx \right]_{0}^{4} = \frac{1}{2} + 4b = 1 \Rightarrow b = \frac{1}{8}\]

<|ref|>equation<|/ref|><|det|>[[120, 245, 640, 293]]<|/det|>
b) \(c \cdot \int_{a}^{b} 1 dx = c \left[ x \right]_{a}^{b} = c(b - a) = 1 \Rightarrow c = \frac{1}{b - a}\)

<|ref|>equation<|/ref|><|det|>[[120, 306, 700, 355]]<|/det|>
c) \(a \cdot \int_{-1}^{1} (1 + x) dx = a \left[ x + \frac{1}{2} x^2 \right]_{-1}^{1} = 2a = 1 \Rightarrow a = \frac{1}{2}\)

<|ref|>title<|/ref|><|det|>[[115, 375, 678, 393]]<|/det|>
3. Wahrscheinlichkeiten mittels Dichtefunktion bestimmen 

<|ref|>text<|/ref|><|det|>[[115, 392, 610, 409]]<|/det|>
Eine stetige Zufallsvariable X besitzt die Dichtefunktion 

<|ref|>equation<|/ref|><|det|>[[115, 408, 430, 463]]<|/det|>
\[f(x) = \begin{cases} kx & 0 \le x \le 10 \\ \text{für} & \text{alle übrigen } x \end{cases}\]

<|ref|>text<|/ref|><|det|>[[115, 473, 445, 491]]<|/det|>
a) Bestimmen Sie den Parameter k. 

<|ref|>text<|/ref|><|det|>[[115, 490, 610, 508]]<|/det|>
b) Berechnen Sie die folgenden Wahrscheinlichkeiten: 

<|ref|>equation<|/ref|><|det|>[[144, 507, 551, 525]]<|/det|>
\[P(X \le -2), P(1 \le X \le 2), P(X \ge 5), P(3 \le X \le 8).\]

<|ref|>equation<|/ref|><|det|>[[120, 540, 595, 592]]<|/det|>
a) \[\int_{0}^{10} kx dx = \left[ \frac{1}{2} kx^2 \right]_{0}^{10} = 50k = 1 \Rightarrow k = \frac{1}{50}\]

<|ref|>equation<|/ref|><|det|>[[120, 593, 792, 650]]<|/det|>
b) Verteilungsfunktion: \(F(x) = \frac{1}{50} \cdot \int_{0}^{x} u \, du = \frac{1}{100} \left[ u^2 \right]_{0}^{x} = \frac{1}{100} x^2 = 0,01x^2\) (0 ≤ x ≤ 10)

<|ref|>equation<|/ref|><|det|>[[150, 655, 785, 673]]<|/det|>
\[P(X \le -2) = 0; \quad P(1 \le X \le 2) = F(2) - F(1) = 0,04 - 0,01 = 0,03\]

<|ref|>equation<|/ref|><|det|>[[150, 680, 660, 698]]<|/det|>
\[P(X \ge 5) = 1 - P(X \le 5) = 1 - F(5) = 1 - 0,25 = 0,75\]

<|ref|>equation<|/ref|><|det|>[[150, 705, 603, 723]]<|/det|>
\[P(3 \le X \le 8) = F(8) - F(3) = 0,64 - 0,09 = 0,55\]

<|ref|>title<|/ref|><|det|>[[115, 740, 661, 758]]<|/det|>
4. Dichtefunktion einer gegebenen Verteilungsfunktion II 

<|ref|>text<|/ref|><|det|>[[115, 757, 880, 791]]<|/det|>
Die Lebensdauer T eines bestimmten elektronischen Bauelements sei eine stetige Zufallsvariable mit der Verteilungsfunktion 

<|ref|>equation<|/ref|><|det|>[[115, 790, 615, 811]]<|/det|>
\[F(t) = 1 - (1 + 0,2t) \cdot e^{-0,2t} \quad (t \ge 0; \text{ sonst } F(t) = 0).\]

<|ref|>text<|/ref|><|det|>[[115, 809, 590, 827]]<|/det|>
a) Bestimmen Sie die zugehörige Dichtefunktion f(t). 

<|ref|>text<|/ref|><|det|>[[115, 826, 602, 844]]<|/det|>
b) Berechnen Sie die Wahrscheinlichkeit P(1 ≤ T ≤ 5). 

<|ref|>equation<|/ref|><|det|>[[120, 860, 872, 882]]<|/det|>
a) \(f(t) = F'(t) = -[0,2 \cdot e^{-0,2t} + e^{-0,2t} \cdot (-0,2)(1 + 0,2t)] = 0,04t \cdot e^{-0,2t}\)

<|ref|>equation<|/ref|><|det|>[[120, 902, 725, 921]]<|/det|>
b) \(P(1 \le T \le 5) = F(5) - F(1) = 0,2642 - 0,0175 = 0,2467\)