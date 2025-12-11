<|ref|>text<|/ref|><|det|>[[114, 83, 140, 101]]<|/det|>
9) 

<|ref|>equation<|/ref|><|det|>[[166, 100, 740, 135]]<|/det|>
\[x^2 y' = y(x - y) = xy - y^2 \Rightarrow y' = \frac{xy - y^2}{x^2} = \frac{y}{x} - \frac{y^2}{x^2} = \left(\frac{y}{x}\right) - \left(\frac{y}{x}\right)^2\]

<|ref|>text<|/ref|><|det|>[[122, 140, 875, 157]]<|/det|>
Sie lässt sich also durch die folgende Substitution in eine durch „Trennung der Variablen“ lösbare Dgl überführen: 

<|ref|>equation<|/ref|><|det|>[[166, 163, 830, 188]]<|/det|>
\[u = \frac{y}{x}, \quad y = xu \Rightarrow y' = 1 \cdot u + u' \cdot x = u + xu' \quad (\text{Ableitung mit der Produktregel})\]

<|ref|>equation<|/ref|><|det|>[[166, 195, 850, 230]]<|/det|>
\[y' = \left(\frac{y}{x}\right) - \left(\frac{y}{x^2}\right)^2 \Rightarrow u + xu' = u - u^2 \Rightarrow xu' = x \cdot \frac{du}{dx} = -u^2 \Rightarrow \frac{du}{u^2} = -\frac{dx}{x}\]

<|ref|>text<|/ref|><|det|>[[122, 237, 560, 252]]<|/det|>
Integration beider Seiten führt zur Lösung für die Hilfsvariable \(u\): 

<|ref|>equation<|/ref|><|det|>[[166, 258, 845, 339]]<|/det|>
\[\int \frac{du}{u^2} = -\int \frac{dx}{x} \Rightarrow \int u^{-2} du = -\int \frac{dx}{x} \Rightarrow \frac{u^{-1}}{-1} = -\frac{1}{u} = -\ln|x| + C \quad (-1) \Rightarrow \frac{1}{u} = \ln|x| - C \Rightarrow u = \frac{1}{\ln|x| - C} \quad (\text{nach Kehrwertbildung})\]

<|ref|>text<|/ref|><|det|>[[122, 344, 501, 360]]<|/det|>
Durch Rücksubstitution erhalten wir die gesuchte Lösung: 

<|ref|>equation<|/ref|><|det|>[[166, 366, 579, 400]]<|/det|>
\[y = xu = x \cdot \frac{1}{\ln|x| - C} = \frac{x}{\ln|x| - C} \quad (\text{mit } C \in \mathbb{R})\]

<|ref|>text<|/ref|><|det|>[[114, 400, 140, 417]]<|/det|>
h) 

<|ref|>equation<|/ref|><|det|>[[166, 421, 785, 458]]<|/det|>
\[y' = \frac{4x^2 + y^2}{xy} = \frac{4x^2}{xy} + \frac{y^2}{xy} = \frac{4x}{y} + \frac{y}{x} = 4 \left(\frac{x}{y}\right) + \left(\frac{y}{x}\right) = 4 \left(\frac{y}{x}\right)^{-1} + \left(\frac{y}{x}\right)\]

<|ref|>text<|/ref|><|det|>[[117, 466, 555, 483]]<|/det|>
darstellen (x/y ist der Kehrwert von y/x). Die Substitution 

<|ref|>equation<|/ref|><|det|>[[166, 490, 877, 520]]<|/det|>
\[u = \frac{y}{x}, \quad y = xu \Rightarrow \quad y' = 1 \cdot u + u' \cdot x = u + xu'  \quad (\text{Ableitung mit der Produktregel})\]

<|ref|>text<|/ref|><|det|>[[117, 527, 671, 544]]<|/det|>
führt dann zu einer Dgl, die sich durch „Trennung der Variablen“ lösen lässt: 

<|ref|>equation<|/ref|><|det|>[[166, 550, 820, 587]]<|/det|>
\[y' = 4 \left(\frac{y}{x}\right)^{-1} + \left(\left(\frac{y}{x}\right)\right) \Rightarrow u + xu' = 4u^{-1} + u = \frac{4}{u} + u \Rightarrow xu' = \frac{4}{u} \Rightarrow\]

<|ref|>equation<|/ref|><|det|>[[166, 597, 750, 632]]<|/det|>
\[xu' = x \cdot \frac{du}{dx} = \frac{4}{u} \Rightarrow u du = \frac{4}{x} dx \Rightarrow \int u du = 4 \cdot \int \frac{1}{x} dx \Rightarrow\]

<|ref|>equation<|/ref|><|det|>[[166, 639, 865, 673]]<|/det|>
\[\frac{1}{2} u^2 = 4 (\ln|x| + \ln|C|) \Rightarrow \frac{1}{2} u^2 = 4 \cdot \ln|Cx| \quad \cdot 2 \Rightarrow u^2 = 8 \cdot \ln|Cx| \Rightarrow\]

<|ref|>equation<|/ref|><|det|>[[166, 680, 707, 708]]<|/det|>
\[u = \pm \sqrt{8 \cdot \ln|Cx|} = \pm 2 \cdot \sqrt{2 \cdot \ln|Cx|} \quad (\text{Rechenregel: R1})\]

<|ref|>text<|/ref|><|det|>[[117, 715, 685, 732]]<|/det|>
Durch Rücksubstitution erhalten wir schließlich die allgemeine Lösung der Dgl: 

<|ref|>equation<|/ref|><|det|>[[166, 740, 411, 767]]<|/det|>
\[y = xu = \pm 2x \cdot \sqrt{2 \cdot \ln|Cx|}\]

<|ref|>sub_title<|/ref|><|det|>[[117, 785, 410, 802]]<|/det|>
## 3. AWP mit separierbarer DGL 

<|ref|>text<|/ref|><|det|>[[117, 801, 716, 819]]<|/det|>
Lösen Sie mit Hilfe der Trennung der Variablen das folgende AWP. 

<|ref|>text<|/ref|><|det|>[[117, 818, 608, 839]]<|/det|>
a) DGL: \(y' - xy^2 = x\); Anfangsbedingung: \(y(0) = 1\). 

<|ref|>text<|/ref|><|det|>[[117, 837, 615, 861]]<|/det|>
b) DGL: \(y' - 2\sqrt{y} = 0\); Anfangsbedingung: \(y(2) = 9\). 

<|ref|>text<|/ref|><|det|>[[117, 859, 645, 882]]<|/det|>
c) DGL: \(y' = (1 + x + y)^2\); Anfangsbedingung: \(y(0) = 2\).