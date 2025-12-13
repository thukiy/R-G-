<|ref|>sub_title<|/ref|><|det|>[[33, 15, 456, 60]]<|/det|>
# Partielle Integration 

<|ref|>text<|/ref|><|det|>[[55, 72, 600, 99]]<|/det|>
Umkehrung der Produktregel der Differentiation 

<|ref|>equation<|/ref|><|det|>[[55, 108, 551, 135]]<|/det|>
\[ [u(x) \cdot v(x)]' = u'(x) \cdot v(x) + u(x) \cdot v'(x) \]

<|ref|>equation<|/ref|><|det|>[[50, 145, 710, 211]]<|/det|>
\[ \int [u(x) \cdot v(x)]' \, dx = \int u'(x) \cdot v(x) \, dx + \int u(x) \cdot v'(x) \, dx \]

<|ref|>equation<|/ref|><|det|>[[35, 222, 652, 252]]<|/det|>
\[ \rightarrow \int u'(x) \cdot v(x) \, dx = u(x) \cdot v(x) - \int u(x) \cdot v'(x) \, dx \]

<|ref|>equation<|/ref|><|det|>[J]<|/ref|><|det|>[[20, 281, 820, 333]]<|/det|>
\[ \text{Bsp:} \quad \circ \int x \cdot e^x \, dx = x \cdot e^x - \int e^x \cdot 1 \, dx = x \cdot e^x - e^x + c \]

<|ref|>text<|/ref|><|det|>[[150, 344, 810, 413]]<|/det|>
→ nun sinnvoll, wenn Restintegral einfacher au lösen ist
als Anfangsintegral 

<|ref|>text<|/ref|><|det|>[[20, 440, 533, 469]]<|/det|>
## Sonderfall: 
\[ u(x) = x \quad u'(x) = 1 \] 

<|ref|>equation<|/ref|><|det|>[[65, 478, 588, 507]]<|/det|>
\[ \int v(x) \cdot 1 \, dx = v(x) \cdot x - \int v'(x) \cdot x \, dx \]

<|ref|>equation<|/ref|><|det|>[[20, 534, 777, 602]]<|/det|>
\[ \text{Bsp:} \quad \circ \int \ln x \, dx = \ln x \cdot x - \int \frac{1}{x} \cdot x \, dx = x \cdot \ln x - \int 1 \, dx \]

<|ref|>equation<|/ref|><|det|>[[120, 630, 930, 837]]<|/det|>
\[ \begin{align*} \circ \int x \cdot \ln x \, dx &= \int x \cdot \ln x \, dx = \int x \cdot \ln x \, dx = \int x \cdot \ln x - \int 1 \, dx \\ &= x \cdot \ln x - x + c \\ \circ \int x \cdot \ln x \, dx &= \int x \cdot \int 1 \, dx = \int x \cdot \ln x \, dx = \int x \cdot 1 \, dx \\ &= x \cdot \ln x - x + c \\ \circ x^2 \cdot \ln x \, dx &= \int x^2 \cdot \ln x \, dx = \int x^2 \cdot 1 \, dx = x^2 \cdot \ln x - \int 1 \, dx \\ &= 2 \cdot \ln 2 - \int 1 \, dx = 2 \cdot \ln 2 - (1 \cdot 4 - 1 \cdot 1) \\ &= 2 \cdot \ln 2 - 3 \cdot 1 \\ &= 2 \cdot \ln 2 - 3 \cdot 1 \\ &= \ln 2 \cdot \ln 2 - 3 \cdot 1 \\ &= \ln^2 2 - 3 \cdot 1 \\ &= \ln^2 2 - 1 \cdot 3 \\ &= \ln^2 2 - 3 \cdot 1 \\ &= \ln 2 \cdot \ln^2 2 - 3 \cdot 1 \\ &= \ln^2 \cdot \ln^2 2 - 3 \cdot 1 \\ &= \frac{\ln^2 2 \cdot \ln^2 2 - 3 \cdot 1}{\ln^2 2} \\ &= \frac{\ln^2 2 \cdot \ln^2 2 - \ln^2 2}{\ln^2 2} \\ &= \frac{\ln^2 2 \cdot 1}{\ln^2 2} \\ &= \frac{\ln^2 \cdot 1}{\ln^2 2} \\ &= \frac{\ln^3 2}{\ln^2 2} \\ &= \frac{\ln^3 2}{\ln 2} \\ &= \frac{\ln^3 2}{\ln 2} \\ \end{align*} \]

<|ref|>equation<|/ref|><|det|>[[120, 870, 978, 940]]<|/det|>
\[ \begin{align*} \circ \int x^2 \cdot \cos x \, dx &= \int x^2 \cdot \cos x \, dx = \int x^2 \cdot 1 \, dx = x^2 - \int 1 \, dx \\ &= x^2 \cdot \cos x - \int 2x \cdot \sin x \, dx \\ &= x^2 \cdot \cos x - \int 2x \sin x \, dx \\ &= x^2 \cdot \cos x - \int 1 \cdot 2x \sin x \, dx \\ &= x^2 \cdot \cos x - 2x \cdot \int \sin x \, dx \\ &= x^2 \cdot \cos x - 2x (- \cos x) \\ &= x^2 \cdot \cos x + 2x \cos x \\ &= x^2 \cdot \cos x + 2x \cos x \\ &= \cos x \cdot \cos x + 2x \cos x \\ &= \cos^2 x + 2x \cos x \\ &= \cos^2 x + 2x (\cos x - 1) \\ &= \cos^2 x + 2x \cos x - 2x \\ &= \cos^2 x + 2x \cos x - 2x \\ \end{align*} \]