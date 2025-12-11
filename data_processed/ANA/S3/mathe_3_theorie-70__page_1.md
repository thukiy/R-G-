<|ref|>sub_title<|/ref|><|det|>[[25, 11, 319, 46]]<|/det|>
## Lösungsmethoden 

<|ref|>sub_title<|/ref|><|det|>[[25, 50, 327, 82]]<|/det|>
### Separationsansatz 

<|ref|>text<|/ref|><|det|>[[45, 91, 380, 118]]<|/det|>
- auch Bernoulli - Ansatz 

<|ref|>text<|/ref|><|det|>[[45, 130, 825, 160]]<|/det|>
- typischerweise für lineare PDGLs, Trennung der Variabeln 

<|ref|>text<|/ref|><|det|>[[25, 186, 450, 214]]<|/det|>
Wir beachten konkrete Beispiel: 

<|ref|>text<|/ref|><|det|>[[50, 225, 902, 293]]<|/det|>
Diffusionsgleichung in 1D mit AWP, auch wärmelösungsgleichung genannt 

<|ref|>equation<|/ref|><|det|>[[105, 299, 400, 335]]<|/det|>
\[ \frac{\partial u(x,t)}{\partial t} - a^2 \frac{\partial^2 u(x,t)}{\partial x^2} = 0 \]

<|ref|>text<|/ref|><|det|>[[105, 340, 431, 370]]<|/det|>
AB: \(u(x,0) = \sin(\frac{\pi}{L} \cdot x)\) 

<|ref|>text<|/ref|><|det|>[[105, 377, 456, 408]]<|/det|>
RB: \(u(0,t) = u(L,t) = 0\) 

<|ref|>equation<|/ref|><|det|>[[105, 414, 426, 444]]<|/det|>
\[ (x,t) \in [0,L] \times [0,\infty[ \]

<|ref|>text<|/ref|><|det|>[[45, 454, 911, 560]]<|/det|>
→ Modelle für 1D Stab, denen Abkühlung beschrieben wird, wobei die Stabenden (bei \(x=0\) und \(x=L\)) auf gleicher Temperatur sind über die gesamte Zeit 

<|ref|>text<|/ref|><|det|>[[45, 568, 600, 597]]<|/det|>
→ Lösungsansatz: \(u(x,t) = v(t) \cdot w(x)\) 

<|ref|>sub_title<|/ref|><|det|>[[470, 604, 765, 633]]<|/det|>
### Trennung der Variabeln 

<|ref|>text<|/ref|><|det|>[[45, 643, 360, 670]]<|/det|>
→ Insekten in PDGL: 

<|ref|>equation<|/ref|><|det|>[[105, 680, 525, 710]]<|/det|>
\[ v'(t) \cdot w(x) - a^2 \cdot v(t) \cdot w''(x) = 0 \]

<|ref|>text<|/ref|><|det|>[[105, 718, 440, 748]]<|/det|>
für \(v(t) \neq 0\), \(w(x) \neq 0\): 

<|ref|>equation<|/ref|><|det|>[[159, 752, 469, 789]]<|/det|>
\[ \frac{v'(t)}{v(t)} = a^2 \frac{w''(x)}{w(x)} = \text{konst.} \]

<|ref|>text<|/ref|><|det|>[[115, 799, 900, 825]]<|/det|>
→ muss konstant sein, da eine Seite von \(t\) und rechte von \(x\) 

<|ref|>text<|/ref|><|det|>[[159, 835, 755, 864]]<|/det|>
abhängig und beide denselben Wert haben sollen 

<|ref|>text<|/ref|><|det|>[[115, 873, 480, 900]]<|/det|>
→ wähle \(a^2k\) als konstante 

<|ref|>equation<|/ref|><|det|>[[199, 911, 650, 939]]<|/det|>
\[ v'(t) = a^2k \cdot v(t), \quad w''(x) = k \cdot w(x) \]

<|ref|>text<|/ref|><|det|>[[115, 949, 920, 978]]<|/det|>
→ es liegen DGL, die mit Exponentialansatz gelöst werden können