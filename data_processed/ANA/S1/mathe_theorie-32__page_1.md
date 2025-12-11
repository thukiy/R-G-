<|ref|>text<|/ref|><|det|>[[135, 10, 730, 42]]<|/det|>
- Summe der ersten \(n\) natürlichen Zahlen : 

<|ref|>equation<|/ref|><|det|>[[177, 44, 530, 120]]<|/det|>
\[ \sum_{k=1}^{n} k = \sum_{k=1}^{n} (n+1-k) \]

<|ref|>equation<|/ref|><|det|>[[257, 100, 536, 141]]<|/det|>
\[ = \sum_{k=1}^{n} (n+1) - \sum_{k=1}^{n} k \]

<|ref|>equation<|/ref|><|det|>[[257, 159, 633, 201]]<|/det|>
\[ = (n+1)(n+1-1) - \sum_{k=1}^{n} k = \]

<|ref|>equation<|/ref|><|det|>[[177, 216, 444, 259]]<|/det|>
\[ 2 \cdot \sum_{k=1}^{n} k = (n+1) \cdot n \]

<|ref|>equation<|/ref|><|det|>[[217, 270, 490, 316]]<|/det|>
\[ \sum_{k=1}^{n} k = \frac{1}{2} (n+1) \cdot n \]

<|ref|>text<|/ref|><|det|>[[545, 281, 900, 308]]<|/det|>
Artikelmethische Summe / 

<|ref|>text<|/ref|><|det|>[[545, 317, 920, 347]]<|/det|>
Gaussische Summenformel 

<|ref|>text<|/ref|><|det|>[[185, 380, 510, 408]]<|/det|>
- Geometrische Summe 

<|ref|>equation<|/ref|><|det|>[[210, 408, 957, 485]]<|/det|>
\[ \begin{align*} G_{m,n}(x) &= \sum_{k=m}^{n} (x)^k = x^m + x^{m+1} + \dots + x^n = \frac{x^m - x^{n+1}}{1-x} \\ m,n \in \mathbb{N}, \quad x \in \mathbb{R} \setminus \{0; 1\} \end{align*} \]

<|ref|>text<|/ref|><|det|>[[24, 510, 90, 541]]<|/det|>
Bsp.: 

<|ref|>equation<|/ref|><|det|>[[130, 500, 816, 560]]<|/det|>
\[ \sum_{k=1}^{n} \left( \frac{1}{2} \right)^k = \frac{\left( \frac{1}{2} \right) - \left( \frac{1}{2} \right)^{10}}{1 - \frac{1}{2}} = \frac{\frac{1}{2} - \frac{1}{2^{10}}}{1 - \frac{1}{2}} = 2 \cdot \left( \frac{1}{2} - \frac{1}{2^{10}} \right) = 1 - \frac{1}{2^{3}} \]

<|ref|>text<|/ref|><|det|>[[170, 576, 715, 606]]<|/det|>
→ typische Anwendung : Rentnerrechnung 

<|ref|>sub_title<|/ref|><|det|>[[36, 655, 220, 700]]<|/det|>
# Reihen 

<|ref|>text<|/ref|><|det|>[[25, 712, 355, 740]]<|/det|>
- Partial- / Teilsumme : 

<|ref|>equation<|/ref|><|det|>[[70, 749, 440, 785]]<|/det|>
\[ a_n \text{ sei Folge } \text{reeller zahlen} \]

<|ref|>equation<|/ref|><|det|>[[70, 784, 550, 830]]<|/det|>
\[ S_n := \sum_{k=1}^{n} a_k \text{ heisst Partialsumme} \]

<|ref|>text<|/ref|><|det|>[[70, 850, 692, 880]]<|/det|>
Die einzelnen \(S_n\) bilden auch eine Folge : \((S_n)\). 

<|ref|>text<|/ref|><|det|>[[70, 900, 725, 940]]<|/det|>
→ Die unendliche Summe \(\sum_{k=1}^{\infty} a_k\) heisst Reihe. 

<|ref|>text<|/ref|><|det|>[[140, 944, 975, 979]]<|/det|>
↪ Die Reihe konvergiert gegen ein \(s \in \mathbb{R}\), wenn gilt: \(\lim_{n \to \infty} S_n = s\)