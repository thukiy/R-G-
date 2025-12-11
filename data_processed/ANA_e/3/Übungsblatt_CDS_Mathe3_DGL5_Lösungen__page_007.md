<|ref|>equation<|/ref|><|det|>[[115, 80, 365, 113]]<|/det|>
\[
B = S = \frac{v_0 + \delta y_0}{\omega_d} = \frac{0 + 2\pi}{1} = 2\pi
\]

<|ref|>text<|/ref|><|det|>[[115, 110, 285, 128]]<|/det|>
Lösung des AWP: 

<|ref|>equation<|/ref|><|det|>[[122, 130, 727, 242]]<|/det|>
\[
\begin{align*}
y(x) &= \mathrm{e}^{-\delta \cdot (x-x_0)} \left( C \cdot \cos\left(\omega_d \left(x-x_0\right)\right) + S \cdot \sin\left(\omega_d \left(x-x_0\right)\right) \right) \\
&= \mathrm{e}^{-2 \cdot (x-0)} \left( \pi \cdot \cos\left(1 \cdot (x-0)\right) + 2\pi \cdot \sin\left(1 \cdot (x-0)\right) \right) \\
&= \pi \mathrm{e}^{-2x} \left( \cos(x) + 2 \sin(x) \right).
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[115, 243, 240, 267]]<|/det|>
\[
\lim_{x \to \infty} y(x) = 0.
\]

<|ref|>text<|/ref|><|det|>[[115, 282, 145, 298]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[115, 298, 570, 316]]<|/det|>
Charakteristisches Polynom: \(p(\lambda) = \lambda^2 + 20\lambda + 64\) 

<|ref|>text<|/ref|><|det|>[[115, 315, 357, 332]]<|/det|>
Diskriminante: \(D = 144 > 0\) 

<|ref|>text<|/ref|><|det|>[[115, 332, 415, 349]]<|/det|>
Es existieren 2 reelle Nullstellen: 

<|ref|>equation<|/ref|><|det|>[[115, 352, 720, 455]]<|/det|>
\[
\begin{align*}
\lambda_{1,2} &= \frac{-b \pm \sqrt{D}}{2 \cdot a} = \frac{-20 \pm \sqrt{144}}{2 \cdot 1} = \frac{-20 \pm 12}{2} \\
\lambda_{1} &= \frac{-20 - 12}{2} = \frac{-32}{2} = -16 \quad \text{und} \quad \lambda_{2} = \frac{-20 + 12}{2} = \frac{-8}{2} = -4
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 425, 320, 443]]<|/det|>
Reelle Basislösungen: 

<|ref|>equation<|/ref|><|det|>[[122, 444, 825, 468]]<|/det|>
\[
y_1(x) = \mathrm{e}^{\lambda_1(x-x_0)} = \mathrm{e}^{-16 \cdot (x-x_0)} \quad \text{und} \quad y_2(x) = \mathrm{e}^{\lambda_2(x-x_0)} = \mathrm{e}^{-4 \cdot (x-x_0)}
\]

<|ref|>text<|/ref|><|det|>[[115, 470, 281, 488]]<|/det|>
Lösung des AWP: 

<|ref|>equation<|/ref|><|det|>[[115, 490, 525, 530]]<|/det|>
\[
C_1 = \frac{\lambda_2 \cdot y_0 - v_0}{\lambda_2 - \lambda_1} = \frac{-4 \cdot 0 - 2}{-4 - (-16)} = \frac{-2}{12} = -\frac{1}{6}
\]

<|ref|>equation<|/ref|><|det|>[[115, 536, 520, 576]]<|/det|>
\[
C_2 = \frac{v_0 - \lambda_1 \cdot y_0}{\lambda_2 - \lambda_1} = \frac{2 - (-16) \cdot 0}{-4 - (-16)} = \frac{2}{12} = \frac{1}{6}.
\]

<|ref|>equation<|/ref|><|det|>[[115, 575, 688, 614]]<|/det|>
\[
\frac{y(x)}{y(0)} = C_1 \cdot y_1(x) + C_2 \cdot y_2(x) = -\frac{1}{6} \cdot \mathrm{e}^{-16 \cdot (x-0)} + \frac{1}{6} \cdot \mathrm{e}^{-4 \cdot (x-0)}
\]

<|ref|>equation<|/ref|><|det|>[[115, 620, 355, 661]]<|/det|>
\[
= \frac{1}{6} \left( \mathrm{e}^{-4x} - \mathrm{e}^{-16x} \right).
\]

<|ref|>equation<|/ref|><|det|>[[115, 661, 595, 700]]<|/det|>
\[
\lim_{x \to \infty} y(x) = \lim_{x \to \infty} \frac{1}{6} \left( \mathrm{e}^{-4x} - \mathbf{e}^{-16x} \right) = \frac{1}{6} (0 - 0) = \underline{0}.
\]

<|ref|>text<|/ref|><|det|>[[115, 716, 145, 732]]<|/det|>
c) 

<|ref|>text<|/ref|><|det|>[[115, 732, 555, 750]]<|/det|>
Charakteristisches Polynom: \(p(\lambda) = 4\lambda^2 - 4\lambda + 1\) 

<|ref|>text<|/ref|><|det|>[[115, 749, 301, 765]]<|/det|>
Diskriminante: \(D = 0\) 

<|ref|>text<|/ref|><|det|>[[115, 765, 444, 783]]<|/det|>
Es existiert 1 reelle Nullstelle: \(\lambda = \frac{1}{2}\). 

<|ref|>text<|/ref|><|det|>[[115, 782, 320, 799]]<|/det|>
Reelle Basislösungen: 

<|ref|>equation<|/ref|><|det|>[[115, 797, 395, 821]]<|/det|>
\[
y_1(x) = \mathrm{e}^{\lambda(x-x_0)} = \mathrm{e}^{0.5 \cdot (x-x_0)}
\]

<|ref|>equation<|/ref|><|det|>[[115, 830, 592, 856]]<|/det|>
\[
y_2(x) = (x - x_0) \cdot \mathrm{e}^{\lambda(x-x_0)} = (x - x_0) \cdot \mathrm{e}^{0.5 \cdot (x-x_0)}
\]

<|ref|>text<|/ref|><|det|>[[115, 855, 281, 872]]<|/det|>
Lösung des AWP: