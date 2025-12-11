<|ref|>equation<|/ref|><|det|>[[217, 83, 666, 200]]<|/det|>
\[
\begin{align*}
s &= \frac{1}{2} \int_0^{\pi/2} \sin((j+k)x) + \sin((j-k)x) \, \mathrm{d}x \\
&= -\frac{1}{2} \left[ \frac{\cos((j+k)x)}{j+k} + \frac{\cos((j-k)x)}{j-k} \right]_{0}^{\pi/2} \\
&= -\frac{1}{2} \left( \frac{c_+ - 1}{j+k} + \frac{c_- - 1}{j-k} \right), \quad c_\pm = \cos((j \pm k)\pi/2)
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[122, 206, 390, 224]]<|/det|>
(zweiter Term entfällt für \(j = k\)) 

<|ref|>equation<|/ref|><|det|>[[122, 232, 480, 251]]<|/det|>
\[
\cos(\ell\pi/2) \in \{-1, 0, 1\} \quad \leadsto \quad \text{mehrere Fälle}
\]

<|ref|>text<|/ref|><|det|>[[122, 254, 636, 273]]<|/det|>
■ \(j = k\): orthogonal, falls \(c_+ = 1\), d.h. \(j + k = 4m\) \(m \in \mathbb{N}_0\) 

<|ref|>text<|/ref|><|det|>[[122, 273, 783, 308]]<|/det|>
■ \(j \neq k \land c_+ = 1\): orthogonal, falls ebenfalls \(c_- = 1\), d.h. \(j + k = 4m_1\) und \(j - k = 4m_2\) \(m_1 \in \mathbb{N}, m_2 \in \mathbb{Z}\) 

<|ref|>text<|/ref|><|det|>[[122, 304, 352, 321]]<|/det|>
\(s \neq 0\) in den anderen Fällen 

<|ref|>text<|/ref|><|det|>[[122, 334, 720, 353]]<|/det|>
■ \(j \neq k \land c_+ = 0 \implies j + k \text{ ungerade} \implies j - k \text{ ungerade und}\) 

<|ref|>equation<|/ref|><|det|>[[253, 360, 652, 396]]<|/det|>
\[
c_- = 0, \quad s = \frac{1}{2} \frac{(j-k) + (j+k)}{j^2 - k^2} = \frac{j}{j^2 - k^2} \neq 0
\]

<|ref|>text<|/ref|><|det|>[[122, 402, 630, 421]]<|/det|>
■ \(j \neq k \land c_+ = -1 \implies j + k = 2+4m\) und \(s = 0\) falls 

<|ref|>text<|/ref|><|det|>[[145, 420, 637, 456]]<|/det|>
(i) \(c_- = -1\) und \(j + k = -(j-k)\) (Widerspruch zu \(j > 0\)) oder 

<|ref|>text<|/ref|><|det|>[[145, 456, 760, 490]]<|/det|>
(ii) \(c_- = 0\) und \(j + k = 2(k-j)\) bzw. \(k = 3j\) (Widerspruch zu \(j + k = 2\)) 

<|ref|>equation<|/ref|><|det|>[[115, 508, 767, 753]]<|/det|>
\[
\begin{align*}
S &= -\frac{1}{2} \left( \frac{c_+ - 1}{i+k} + \frac{c_- - 1}{j-k} \right) \quad c_\pm = \cos((j \pm k)\frac{\sqrt{2}}{2}) \\
&= -\frac{1}{2} \left( \frac{c_+ (j-k) - j+k}{j^2 - k^2} + \frac{c_- (j+k) - j-k}{j^2 - k^2} \right) \\
&= -\frac{1}{2} \left( \frac{c_+ (j+k) + c_- (j+k) - 2j}{j^2 - k^2} \right) \\
&= -\frac{1}{3} \left( \frac{c_+ (j-k) + c_- (j+k) - 2j}{j^2 - k^3} \right)
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[164, 755, 390, 775]]<|/det|>
Da \(j = k: 2j = 4m\) bzw. \(j = 2m\).

<|ref|>text<|/ref|><|det|>[[115, 784, 844, 820]]<|/det|>
Im Folgenden betrachten wir die Fälle \(j \neq k\), hier kann \(c_+\) nur die Werte -1, = und +1
annehmen, es müssen also 3 Fälle unterschieden werden.