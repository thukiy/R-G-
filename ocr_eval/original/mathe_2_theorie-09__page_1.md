<|ref|>sub_title<|/ref|><|det|>[[40, 18, 300, 57]]<|/det|>
# Substitution 

<|ref|>text<|/ref|><|det|>[[24, 71, 520, 99]]<|/det|>
Umkehrung des Kleintreegel der Differentiation 

<|ref|>equation<|/ref|><|det|>[[50, 106, 346, 137]]<|/det|>
\[ [f(g(x))]' = f'(g(x)) \cdot g'(x) \]

<|ref|>text<|/ref|><|det|>[[30, 149, 270, 177]]<|/det|>
* Substitutionstreegel 

<|ref|>text<|/ref|><|det|>[[72, 189, 945, 254]]<|/det|>
\(f: \mathbb{R} \to \mathbb{R}\) sei integrierbar, habe Stammfunktion \(F: \mathbb{R} \to \mathbb{R}\), \(g: \mathbb{R} \to \mathbb{R}\) sei differenzierbar. Dann gilt: 

<|ref|>equation<|/ref|><|det|>[[90, 263, 800, 297]]<|/det|>
\[ \int f(g(x)) \cdot g'(x) \, dx = \int f(z) \, dz = F(z) + c = F(g(x)) + c \]

<|ref|>equation<|/ref|><|det|>[[90, 300, 950, 338]]<|/det|>
\[ x = a^b f(g(x)) \cdot g'(x) \, dx = \int_{z = g(a)}^{g(b)} f(z) \, dz = [F(z)]_{g(a)}^{g(b)} = F(g(b)) - F(g(a)) \]

<|ref|>text<|/ref|><|det|>[[30, 365, 963, 392]]<|/det|>
→ wichtig: beim Substitiieren müssen Integrationsgrenzen neu berechnet werden 

<|ref|>text<|/ref|><|det|>[[30, 401, 870, 429]]<|/det|>
→ formal: "Glemen" des zusammengesetzen Funktion, Substitution 

<|ref|>text<|/ref|><|det|>[[197, 441, 810, 468]]<|/det|>
durchführen, integrieren, eventuell Rücksubstitutionen 

<|ref|>text<|/ref|><|det|>[[20, 500, 395, 529]]<|/det|>
Bsp: 
\[ \int \cos(x^2) \cdot 2x \, dx \] 

<|ref|>equation<|/ref|><|det|>[[160, 555, 596, 580]]<|/det|>
\[ f(g(x)) = \cos(x^2) \quad g(x) = x^2 = z \]

<|ref|>equation<|/ref|><|det|>[[160, 586, 656, 621]]<|/det|>
\[ g'(x) = \frac{dg(x)}{dx} = \frac{dz}{dx} = 2x \quad \iff \quad dx = \frac{dz}{2x} \]

<|ref|>text<|/ref|><|det|>[[160, 634, 463, 659]]<|/det|>
Substitution durchführen: 

<|ref|>equation<|/ref|><|det|>[[160, 666, 916, 703]]<|/det|>
\[ \int \cos z \cdot 2x \frac{dz}{2x} = \int \cos z \, dz = \sin z + c = \sin x^2 + c \]

<|ref|>equation<|/ref|><|det|>[[120, 728, 400, 760]]<|/det|>
\[ \int e^{\sin x} \cdot \cos x \, dx \]

<|ref|>equation<|/ref|><|det|>[[160, 785, 350, 818]]<|/det|>
\[ f(g(x)) = e^{\sin x} \]

<|ref|>equation<|/ref|><|det|>[[170, 832, 384, 857]]<|/det|>
\[ g(x) = \sin x = z \]

<|ref|>equation<|/ref|><|det|>[[170, 863, 707, 900]]<|/det|>
\[ g'(x) = \frac{dg(x)}{dx} = \left. \frac{dz}{dx} \right. = \cos x \quad \iff \quad dx = \frac{dz}{\cos x} \]

<|ref|>equation<|/ref|><|det|>[[160, 904, 597, 940]]<|/det|>
\[ \rightarrow \int e^z \cdot \cos x \frac{dz}{\cos x} = \int e^z \, dz \]

<|ref|>equation<|/ref|><|det|>[[230, 945, 512, 978]]<|/det|>
\[ = e^z + c = e^{\sin x} + c \]