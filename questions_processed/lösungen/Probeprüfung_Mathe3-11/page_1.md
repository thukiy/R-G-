<|ref|>text<|/ref|><|det|>[[30, 12, 512, 45]]<|/det|>
5) \(f(t)\) bestimmen: \(m = \frac{4y}{x} = \frac{24}{t}\) 

<|ref|>text<|/ref|><|det|>[[90, 52, 620, 81]]<|/det|>
\(y = mx + q\) (allegenweine lineare Funktion) 

<|ref|>text<|/ref|><|det|>[[90, 90, 728, 119]]<|/det|>
hier: \(q = 0\), da Funktion durch ursprung verläuft 

<|ref|>equation<|/ref|><|det|>[[90, 124, 515, 159]]<|/det|>
\[ \rightarrow f(t) = \frac{24}{t} \cdot t \quad t \in [-\frac{1}{2}; \frac{1}{2}] \]

<|ref|>text<|/ref|><|det|>[[90, 168, 963, 197]]<|/det|>
Funktion ist ungeordet und kann durch eine Sinusreihe dargestellt werden, 

<|ref|>text<|/ref|><|det|>[[90, 205, 500, 234]]<|/det|>
d.h. \(a_n = 0\), Peride \(p = T\) 

<|ref|>equation<|/ref|><|det|>[[90, 240, 888, 400]]<|/det|>
\[ \begin{aligned} b &= \frac{2}{T} \cdot \frac{T^2}{-T^2} \cdot \frac{24}{t} \cdot t \cdot \sin\left(\frac{24t}{T} \cdot t\right) \, dt \\ &= \frac{44}{T^2} \left[ t \cdot \left(- \cos\left(\frac{24t}{T} \cdot t\right) \right) \cdot \frac{T^2}{-T^2} - \frac{T^2}{-T^2} \left[ \left(-\cos\left(\frac{24t}{T} \cdot t\right) \right) \right] \cdot \frac{T^2}{-T^2} \, dt \right] \\ &= \frac{44}{T^2} \left[ -\frac{1}{2} \cdot \cos\left(\frac{24t}{T} \cdot \frac{T}{2}\right) \cdot \frac{T^2}{-T^2} - \frac{1}{2} \cdot \cos\left(\frac{24t}{T} - \frac{T}{2}\right) \cdot \frac{T^2}{-T^3} \right] + \left[ \frac{T^2}{4T^2} \cdot \sin\left(\frac{24t}{T} \cdot t\right) \right] \cdot \frac{T^2}{-T^2} \\ &= \frac{44}{T^2} \left[ -\frac{T^2}{2T^2} \cdot \cos\left(7t\right) + \frac{T^2}{4T^2} \cdot \sin\left(\frac{7t}{2}\right) - \frac{T^2}{4T^2} \cdot \sin\left(\frac{2t}{T} \cdot \left(-\frac{T}{2}\right)\right) \right] \\ &= \frac{44}{T^2} \left[ -\frac{T^2}{\frac{2T^2}{2T^2}} \cdot \cos\left(7t\right) = -\frac{24}{T^2} \cdot (-1)^k = \frac{24}{T^2} \cdot (-1)^{k+1} = b_k \right] \end{aligned} \]

<|ref|>equation<|/ref|><|det|>[[90, 408, 878, 450]]<|/det|>
\[ f(t) = \sum_{k=1}^{8} b_k \cdot \sin\left(\frac{24t}{T} \cdot t\right) \]

<|ref|>equation<|/ref|><|det|>[[130, 450, 550, 490]]<|/det|>
\[ = \sum_{k=1}^{8} \frac{24}{T^2} \cdot (-1)^{k+1} \cdot \sin\left(\frac{24t}{T} \cdot t\right) = \sum_{k=1}^{8} \frac{24}{T^2} (-1)^{k+1} \cdot \sin\left(\frac{24t}{T}\right) \]