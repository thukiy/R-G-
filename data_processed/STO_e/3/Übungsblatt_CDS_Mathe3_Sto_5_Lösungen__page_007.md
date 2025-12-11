<|ref|>table<|/ref|><|det|>[[117, 80, 700, 282]]<|/det|>
<table><tr><td>X (Be-stellung)</td><td>\(y_{1}\) (Sonnenschein)</td><td>\(y_{2}\) (Bewölkung oder Regen)</td><td>\(\sum_{k=1}^{2}\)</td></tr><tr><td>\(x_{1}\) (Kaffee und Kuchen)</td><td>\(P_{11} = P_{1e} \cdot P_{e1}\) \(= 0,60 \cdot 0,30\) \(= 0,18\) \(P_{21} = P_{2e} \cdot P_{e1}\) \(= 0,40 \cdot 0,30\) \(= 0,12\)</td><td>\(P_{12} = P_{1e} \cdot P_{e2}\) \(= 0,60 \cdot 0,70\) \(= 0,42\) \(P_{22} = P_{2e} \cdot P_{e2}\) \(= 0,40 \cdot 0,70\) \(= 0,28\)</td><td>\(P_{1e} = 0,60\) \(P_{2e} = 0,40\)</td></tr><tr><td>\(x_{2}\) (Eis)</td><td></td><td></td><td></td></tr><tr><td>\(\sum_{j=1}^{2}\)</td><td>\(P_{e1} = 0,30\)</td><td>\(P_{e2} = 0,70\)</td><td>1</td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[114, 299, 530, 317]]<|/det|>
## 8. Stetige 2-dimensionale Zufallsvariable II 

<|ref|>text<|/ref|><|det|>[[114, 316, 812, 350]]<|/det|>
Die stochastisch unabhängigen stetigen Zufallsvariablen X und Y besitzen die folgenden Dichtefunktionen: 

<|ref|>equation<|/ref|><|det|>[[345, 349, 649, 387]]<|/det|>
\[f_1(x) = \frac{1}{4}(x + 1), \quad 0 \le x \le 2\]

<|ref|>equation<|/ref|><|det|>[[360, 387, 633, 425]]<|/det|>
\[f_2(y) = y + \frac{1}{2}, \quad 0 \le y \le 1\]

<|ref|>text<|/ref|><|det|>[[114, 424, 595, 442]]<|/det|>
(im übrigen Bereich verschwinden beide Funktionen). 

<|ref|>text<|/ref|><|det|>[[114, 440, 763, 459]]<|/det|>
a) Bestimmen Sie die Dichtefunktion f(x,y) der gemeinsamen Verteilung. 

<|ref|>text<|/ref|><|det|>[[114, 457, 775, 475]]<|/det|>
b) Wie lautet die Verteilungsfunktion F(x,y) der gemeinsamen Verteilung? 

<|ref|>text<|/ref|><|det|>[[114, 474, 690, 492]]<|/det|>
c) Berechnen Sie die Wahrscheinlichkeit P(0 ≤ X ≤ 1; 0 ≤ Y ≤ 1). 

<|ref|>equation<|/ref|><|det|>[[114, 508, 790, 551]]<|/det|>
\[a) \quad f(x; y) = f_1(x) \cdot f_2(y) = \frac{1}{4}(x + 1) \left( y + \frac{1}{2} \right) = \frac{1}{8}(x + 1)(2y + 1)\]

<|ref|>equation<|/ref|><|det|>[[114, 551, 827, 595]]<|/det|>
\[b) \quad F(x; y) = \int_{u=0}^{x} \int_{v=0}^{y} f(u; v) \, dv \, du = \frac{1}{8} \cdot \int_{u=0}^{x} \int_{v=0}^{y} (u + 1)(2v + 1) \, dv \, du =\]

<|ref|>equation<|/ref|><|det|>[[224, 620, 872, 664]]<|/det|>
\[= \frac{1}{8} \cdot \int_{0}^{x} (u + 1) \, du \cdot \int_{0}^{y} (2v + 1) \, dv = \frac{1}{8} \left[ \frac{1}{2} u^2 + u \right]_{0}^{x} \cdot \left[ v^2 + v \right]_{0}^{y} =\]

<|ref|>equation<|/ref|><|det|>[[224, 675, 714, 718]]<|/det|>
\[= \frac{1}{8} \left( \frac{1}{2} x^2 + x \right) (y^2 + y) = \frac{1}{16} (x^2 + 2x) (y^2 + y)\]

<|ref|>equation<|/ref|><|det|>[[114, 720, 684, 757]]<|/det|>
\[c) \quad P(0 \le X \le 1; 0 \le Y \le 1) = F(1; 1) = \frac{1}{16} \cdot 3 \cdot 2 = \frac{3}{8}\]

<|ref|>sub_title<|/ref|><|det|>[[114, 776, 546, 794]]<|/det|>
## 9. Diskrete 2-dimensionale Zufallsvariable III 

<|ref|>text<|/ref|><|det|>[[114, 793, 825, 828]]<|/det|>
Die diskreten Zufallsvariablen X und Y mit den folgenden Verteilungsfunktionen sind stochastisch unabhängig: 

<|ref|>table<|/ref|><|det|>[[117, 835, 700, 901]]<|/det|>
<table><tr><td>\(x_{i}\)</td><td>1</td><td>2</td><td>3</td><td>\(y_{k}\)</td><td>5</td><td>10</td><td>15</td></tr><tr><td>\(f_{1}(x_{i})\)</td><td>0,5</td><td>0,3</td><td>0,2</td><td>\(f_{2}(y_{k})\)</td><td>0,15</td><td>0,6</td><td>0,25</td></tr></table>

<|ref|>text<|/ref|><|det|>[[114, 904, 512, 922]]<|/det|>
Bestimmen Sie die gemeinsame Verteilung.