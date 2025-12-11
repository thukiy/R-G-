<|ref|>sub_title<|/ref|><|det|>[[20, 12, 350, 45]]<|/det|>
Anwendung auf DGL 

<|ref|>text<|/ref|><|det|>[[55, 54, 692, 82]]<|/det|>
f(t) heisst auch Originalfunktion, F(t) Bildfunktion 

<|ref|>text<|/ref|><|det|>[[110, 92, 536, 120]]<|/det|>
f(t) ⇌ F(t) F(t) ⇌ f(t) 

<|ref|>text<|/ref|><|det|>[[186, 131, 450, 156]]<|/det|>
Korrespondenzzeichen 

<|ref|>text<|/ref|><|det|>[[55, 187, 365, 214]]<|/det|>
→ a·f(t) ⇌ a·F(t) 

<|ref|>text<|/ref|><|det|>[[55, 225, 450, 252]]<|/det|>
→ f(t) + g(t) ⇌ F(t) + G(t) 

<|ref|>text<|/ref|><|det|>[[55, 262, 556, 289]]<|/det|>
→ a·f(t) + b·g(t) ⇌ a·F(t) + b·G(t) 

<|ref|>sub_title<|/ref|><|det|>[[20, 316, 560, 348]]<|/det|>
Ableitung der Fouriertransformation : 

<|ref|>text<|/ref|><|det|>[[55, 356, 530, 384]]<|/det|>
f(t) ⇌ F(t) → f'(t) ⇌ iwF(t) 

<|ref|>text<|/ref|><|det|>[[20, 437, 393, 465]]<|/det|>
Bsp: 
\(\ddot{x} + 4\dot{x} - 5x = 2(t) \cdot e^{-7t}\) 

<|ref|>text<|/ref|><|det|>[[110, 495, 220, 517]]<|/det|>
x ⇌ X 

<|ref|>text<|/ref|><|det|>[[110, 530, 250, 552]]<|/det|>
\(\ddot{x} \leftrightarrow iwX\) 

<|ref|>text<|/ref|><|det|>[[110, 565, 270, 590]]<|/det|>
\(\ddot{x} \leftrightarrow -w^2X\) 

<|ref|>text<|/ref|><|det|>[[110, 600, 590, 660]]<|/det|>
\(\delta(t): \text{ Sprungfunktion} = \begin{cases} 0 & t < 0 \\ 1 & t \geq 0 \end{cases}\) 

<|ref|>text<|/ref|><|det|>[[110, 770, 803, 808]]<|/det|>
\(\delta(t) \cdot e^{-7t} \leftrightarrow \frac{1}{iw + 7}\) (aus Tabelle, z.B. Papula) 

<|ref|>text<|/ref|><|det|>[[110, 835, 357, 860]]<|/det|>
Einsetzen in DGL: 

<|ref|>equation<|/ref|><|det|>[[130, 866, 465, 906]]<|/det|>
\[-w^2X + 4iwX - 5X = \frac{1}{iw + 7}\]

<|ref|>text<|/ref|><|det|>[[130, 903, 721, 940]]<|/det|>
\(X = \frac{1}{(iw + 7)(-w^2 + 4iw - 5)}\) das im Regensraum