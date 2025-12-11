<|ref|>sub_title<|/ref|><|det|>[[114, 81, 300, 100]]<|/det|>
## 8. Kurvenintegrale 

<|ref|>text<|/ref|><|det|>[[114, 98, 770, 117]]<|/det|>
Bestimmen Sie die folgenden skalaren bzw. vektoriellen Kurvenintegrale: 

<|ref|>equation<|/ref|><|det|>[[114, 115, 592, 160]]<|/det|>
\[
\text{a) } \ddot{\gamma} : [0,2\pi] \to \mathbb{R}^3, \ddot{\gamma}(t) = \begin{pmatrix} \cos t \\ \sin t \\ t \end{pmatrix}, f(x, y, z) = x^2 + yz.
\]

<|ref|>equation<|/ref|><|det|>[[114, 158, 761, 195]]<|/det|>
\[
\text{b) } \ddot{\gamma} \text{ ist die Verbindungsstrecke von } (0;0) \text{ nach } (1;1) \text{ und } \ddot{v}(x,y) = \begin{pmatrix} 2y \\ e^x \end{pmatrix}.
\]

<|ref|>text<|/ref|><|det|>[[114, 208, 144, 224]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[124, 222, 373, 240]]<|/det|>
Für diese Kurve erhalten wir 

<|ref|>equation<|/ref|><|det|>[[196, 252, 767, 277]]<|/det|>
\[
\dot{\gamma}(t) = (-\sin t, \cos t, 1)^\top, \quad \|\dot{\gamma}(t)\| = \sqrt{\sin^2 t + \cos^2 t + 1} = \sqrt{2},
\]

<|ref|>text<|/ref|><|det|>[[124, 291, 350, 309]]<|/det|>
und damit für das Integral 

<|ref|>equation<|/ref|><|det|>[[125, 320, 839, 415]]<|/det|>
\[
\begin{align*}
\int_{\gamma} f \, \mathrm{d}s &= \int_{0}^{2\pi} f(\gamma(t)) \|\dot{\gamma}(t)\| \, \mathrm{d}t = \int_{0}^{2\pi} f(\cos t, \sin t, t) \sqrt{2} \, \mathrm{d}t \\
&= \sqrt{2} \int_{0}^{2\pi} \cos^2 t + t \sin t \, \mathrm{d}t = \sqrt{2} \left( \pi - t \cos t \bigg|_{0}^{2\pi} + \int_{0}^{2\pi} \cos t \, \mathrm{d}t \right) = -\sqrt{2\pi}.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 420, 144, 437]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[114, 434, 757, 473]]<|/det|>
Die direkte Verbindungsstrecke ist gegeben durch \(\gamma(t) = (t, t)^\top\), \(t \in [0, 1]\).
Das Kurvenintegral berechnet sich dann zu 

<|ref|>equation<|/ref|><|det|>[[243, 485, 712, 572]]<|/det|>
\[
\begin{align*}
\int_{\gamma} \mathbf{v} \cdot \mathrm{d}s &= \int_{0}^{1} (\mathbf{v}(\gamma(t)), \dot{\gamma}(t)) \, \mathrm{d}t = \int_{0}^{1} \begin{pmatrix} 2t \\ \mathbf{e}^t \end{pmatrix}^\top \begin{pmatrix} 1 \\ 1 \end{pmatrix} \, \mathrm{d}t \\
&= \int_{0}^{1} (2t + \mathbf{e}^t) \, \mathrm{d}t = 1 + \mathbf{e} - 1 = \mathbf{e}.
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[114, 588, 315, 606]]<|/det|>
## 9. Kurvenintegrale II 

<|ref|>text<|/ref|><|det|>[[114, 604, 707, 624]]<|/det|>
Gegeben seien die Vektorfelder \(\ddot{v}\): \(\mathbb{R}^2 \to \mathbb{R}^2\) und \(\ddot{w}\): \(\mathbb{R}^2 \to \mathbb{R}^2\) durch 

<|ref|>equation<|/ref|><|det|>[[114, 622, 494, 660]]<|/det|>
\[
\ddot{v}(x, y) = \begin{pmatrix} x^2 - y \\ x + y^2 \end{pmatrix} \text{ und } \ddot{w}(x, y) = \begin{pmatrix} x + y^2 \\ 2xy \end{pmatrix}.
\]

<|ref|>text<|/ref|><|det|>[[114, 658, 848, 695]]<|/det|>
Berechnen Sie sowohl für \(\ddot{v}\) als auch für \(\ddot{w}\) jeweils das Kurvenintegral von A=(0;1)
nach B=(1;2) 

<|ref|>text<|/ref|><|det|>[[114, 694, 427, 712]]<|/det|>
a) längs der Verbindungsgeraden 

<|ref|>text<|/ref|><|det|>[[114, 710, 857, 745]]<|/det|>
b) längs des Streckenzugs bestehend aus den Strecken von A nach (1;1) und von (1;1) nach B, 

<|ref|>text<|/ref|><|det|>[[114, 743, 418, 762]]<|/det|>
c) längs der Parabel \(y = x^2 + 1\). 

<|ref|>text<|/ref|><|det|>[[120, 777, 875, 853]]<|/det|>
Wir bezeichnen mit \(\gamma_1\) die direkte Verbindungsstrecke von \(A\) und \(B\), mit \(\gamma_2\) den Streckenzug, bestehend aus \(\gamma_{2,1}\) von \(A\) nach \((1, 1)^\top\), gefolgt von \(\gamma_{2,2}\) von \((1, 1)^\top\) nach \(B\) und mit \(\gamma_3\) die Verbindungskurve von \(A\) nach \(B\) entlang der Parabel \(y = x^2 + 1\). Wir wählen die folgenden Parametrisierungen: 

<|ref|>equation<|/ref|><|det|>[[120, 854, 490, 875]]<|/det|>
\[
\text{(a) } \gamma_1 : [0, 1] \to \mathbb{R}^2, \quad \gamma_1(t) = (t, 1 + t)^\top
\]

<|ref|>equation<|/ref|><|det|>[[120, 874, 872, 896]]<|/det|>
\[
\text{(b) } \gamma_{2,1} : [0, 1] \to \mathbb{R}^2, \quad \gamma_{2,1}(t) = (t, 1)^\top \text{ und } \gamma_{2,2} : [0, 1] \to \mathbb{R}^2, \quad \text{und } \gamma_{2,2}(t) = (1, 1 + t)^\top
\]

<|ref|>equation<|/ref|><|det|>[[120, 894, 495, 916]]<|/det|>
\[
\text{(c) } \gamma_3 : [0, 1] \to \mathbb{R}^2, \quad \gamma(3)(t) = (t, t^2 + 1)^\top
\]