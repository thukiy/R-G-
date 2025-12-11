<|ref|>sub_title<|/ref|><|det|>[[110, 67, 440, 85]]<|/det|>
## 10. Ableitung von Area-Funktionen 

<|ref|>text<|/ref|><|det|>[[108, 85, 895, 120]]<|/det|>
Wir verwenden die Ketten-Regel, um jeweils die *Ableitung* der folgenden *Funktionen* aus der *Ableitung* der *Umkehrfunktion* zu bestimmen. 

<|ref|>text<|/ref|><|det|>[[122, 125, 308, 143]]<|/det|>
a) Für alle \(z \in \mathbb{R}\) gilt 

<|ref|>equation<|/ref|><|det|>[[447, 155, 922, 175]]<|/det|>
\[ \text{arsinh}(\sinh(z)) = z \qquad (70) \]

<|ref|>text<|/ref|><|det|>[[150, 188, 195, 203]]<|/det|>
und 

<|ref|>equation<|/ref|><|det|>[[421, 216, 922, 245]]<|/det|>
\[ \cosh(z) = \sqrt{1 + \sinh^2(z)}. \qquad (71) \]

<|ref|>text<|/ref|><|det|>[[150, 255, 815, 273]]<|/det|>
Durch beidseitiges *Ableiten* von (70) mit Hilfe der *Ketten-Regel* erhalten wir 

<|ref|>equation<|/ref|><|det|>[[195, 285, 922, 386]]<|/det|>
\[ \begin{align*} \text{arsinh}'\big(\sinh(z)\big) \cdot \sinh'(z) &= z' \tag{72} \\ \Rightarrow \quad \text{arsinh}'\big(\sinh(z)\big) \cdot \cosh(z) &= 1 \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \quad | : \cosh(z) \tag{73} \\ \Rightarrow \quad \text{arsinh}'\big(\sinh(z)\bigg) &= \frac{1}{\cosh(z)} = \frac{1}{\sqrt{1 + \sinh^2(z)}}. \tag{74} \end{align*} \]

<|ref|>text<|/ref|><|det|>[[150, 400, 922, 435]]<|/det|>
Durch die Substitution \(x := \sinh(z)\) erhalten wir für alle \(x \in \mathbb{R}\) die *Areasinus-Hyperbolicus-Ableitung* 

<|ref|>equation<|/ref|><|det|>[[434, 444, 922, 485]]<|/det|>
\[ \text{arsinh}'(x) = \frac{1}{\sqrt{1 + x^2}}. \qquad (75) \]

<|ref|>text<|/ref|><|det|>[[120, 506, 328, 526]]<|/det|>
b) Für alle \(z \in \mathbb{R}_0^+\) gilt 

<|ref|>equation<|/ref|><|det|>[[444, 538, 922, 557]]<|/det|>
\[ \text{arcosh}(\cosh(z)) = z \qquad (76) \]

<|ref|>text<|/ref|><|det|>[[150, 571, 195, 586]]<|/det|>
und 

<|ref|>equation<|/ref|><|det|>[[351, 597, 922, 626]]<|/det|>
\[ \sinh(z) > 0 \Rightarrow \sinh(z) = \sqrt{\cosh^2(z) - 1}. \qquad (77) \]

<|ref|>text<|/ref|><|det|>[[150, 637, 815, 655]]<|/det|>
Durch beidseitiges *Ableiten* von (76) mit Hilfe der *Ketten-Regel* erhalten wir 

<|ref|>equation<|/ref|><|det|>[[243, 667, 922, 686]]<|/det|>
\[ \text{arcosh}'\big(\cosh(z)\big) \cdot \cosh'(z) = z' \qquad (78) \]

<|ref|>equation<|/ref|><|det|>[[189, 697, 922, 725]]<|/det|>
\[ \Rightarrow \quad \text{arcosh}'\big(\cosh(z)\big) \cdot \sinh(z) = 1 \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \quad |: \sinh(z) \qquad (79) \]

<|ref|>equation<|/ref|><|det|>[[189, 735, 922, 780]]<|/det|>
\[ \Rightarrow \quad \text{arcosh}'\big(\cosh(2z)\big) = \frac{1}{\sinh(z)} = \frac{1}{\sqrt{\cosh^2(z) - 1}}. \qquad (80) \]

<|ref|>text<|/ref|><|det|>[[150, 792, 922, 827]]<|/det|>
Durch die Substitution \(x := \cosh(z)\) erhalten wir für alle \(x \in [1, \infty[\) die *Areacosinus-Hyperbolicus-Ableitung* 

<|ref|>equation<|/ref|><|det|>[[434, 837, 922, 875]]<|/det|>
\[ \text{arcosh}'(x) = \frac{1}{\sqrt{x^2 - 1}}. \qquad (81) \]