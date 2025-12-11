<|ref|>equation<|/ref|><|det|>[[120, 85, 565, 128]]<|/det|>
\[
\nu_d = \frac{1}{2\pi} \cdot \omega_d = \frac{1}{2\pi} \cdot \sqrt{\omega_0^2 - \delta^2} = \frac{1}{2\pi} \cdot \sqrt{\frac{1}{LC} - \frac{R^2}{4L^2}}
\]

<|ref|>equation<|/ref|><|det|>[[145, 131, 738, 180]]<|/det|>
\[
\approx \frac{1}{2\pi} \cdot \sqrt{\frac{1}{1.80 \cdot 10^{-2} \text{ H} \cdot 1.41 \cdot 10^{-4} \text{ F}}} = \frac{1}{4} \cdot \frac{(10.0 \Omega)^2}{(1.80 \cdot 10^{-2} \text{ H})^2} \approx \frac{89.6 \text{ Hz}}{}
\]

<|ref|>text<|/ref|><|det|>[[115, 178, 485, 197]]<|/det|>
und für die Resonanzfrequenz ergibt sich 

<|ref|>equation<|/ref|><|det|>[[115, 197, 777, 240]]<|/det|>
\[
\frac{\nu_{\perp}}{2\pi} = \frac{1}{2\pi} \cdot \omega_{\perp} = \frac{1}{2\pi} \cdot \sqrt{\omega_0^2-2\delta^2} = \frac{1}{2\pi} \cdot \sqrt{\frac{11}{LC} - 2 \cdot \frac{R^2}{4L^2}} = \frac{1}{2\pi} \cdot \sqrt{\frac{1}{LC}- \frac{R^2}{2L^2}}
\]

<|ref|>equation<|/ref|><|det|>[[135, 243, 737, 288]]<|/det|>
\[
\approx \frac{1}{2\pi} \cdot \sqrt{ \frac{1}{1.80 \cdot 10^{-2} \text{ H} 1.41 \cdot 10^{-4} \text{ F}} - \frac{(10.0 \Omega)^2}{2 \cdot (1.80 \cdot 10^{-2} \text{ H})^2}} \approx \frac{77.9 \text{ Hz}}{}
\]

<|ref|>sub_title<|/ref|><|det|>[[115, 307, 545, 326]]<|/det|>
4. Erzwungene mechanische Schwingung → 

<|ref|>text<|/ref|><|det|>[[115, 324, 864, 410]]<|/det|>
Ein schwach gedämpftes schwingungsfähiges mechanisches System mit dem Dämpfungsfaktor \(\delta\) und der Eigen- bzw. Resonanzfrequenz \(\omega_0\) (des ungedämpften Systems) wird von aussen durch eine periodische Kraft mit derselben Kreisfrequenz \(\omega_0\) zu erzwungenen Schwingungen angeregt. Lösen Sie die Schwingungsgleichung \(\ddot{x} + 2\delta\dot{x} + \omega_0^2 x = a \cdot \cos(\omega_0 t)\) mit \(\delta < \omega_0\) für die ABs \(x(0) = 0\), \(\dot{x}(0) = 0\). 

<|ref|>text<|/ref|><|det|>[[118, 424, 520, 443]]<|/det|>
Wir lösen zunächst die zugehörige homogene Dgl 

<|ref|>equation<|/ref|><|det|>[[157, 452, 350, 472]]<|/det|>
\[
\ddot{x} + 2\delta\dot{x} + \omega_0^2 x \equiv 0
\]

<|ref|>text<|/ref|><|det|>[[118, 481, 866, 518]]<|/det|>
durch den Lösungsansatz (Exponentialansatz) \(x = e^{\lambda t}\), \(\dot{x} = \lambda \cdot e^{\lambda t}\) und \(\ddot{x} = \lambda^2 \cdot e^{\lambda t}\) und erhalten die Gleichung 

<|ref|>equation<|/ref|><|det|>[[157, 526, 485, 548]]<|/det|>
\[
\lambda^2 \cdot e^{\lambda t} + 2\delta\lambda \cdot e^{\lambda t} + \omega_0^2 \cdot e^{\lambda t} = 0
\]

<|ref|>text<|/ref|><|det|>[[118, 558, 747, 577]]<|/det|>
Division durch \(e^{\lambda t} \neq 0\) führt schließlich zu der charakteristischen Gleichung 

<|ref|>equation<|/ref|><|det|>[[157, 586, 350, 607]]<|/det|>
\[
\lambda^2 + 2\delta\lambda + \omega_0^2 = 0
\]

<|ref|>text<|/ref|><|det|>[[115, 617, 866, 652]]<|/det|>
Diese besitzt bei der vorausgesetzten schwachen Dämpfung (\(\delta < \omega_0\)) konjugiert komplexe Lösungen: 

<|ref|>equation<|/ref|><|det|>[[157, 660, 875, 718]]<|/det|>
\[
\lambda_{1/2} = -\delta \pm \sqrt{\delta^2 - \omega_0^2} = -\delta \pm \sqrt{-(\omega_0^2 - \delta^2)} = -\delta \pm \sqrt{-\omega_0^2} = -\delta \pm \mathrm{j} \omega_d \\
< 0 \qquad \omega_d^2 > 0
\]

<|ref|>text<|/ref|><|det|>[[118, 728, 650, 747]]<|/det|>
Wir erhalten somit eine gedämpfte Schwingung mit der Gleichung 

<|ref|>equation<|/ref|><|det|>[[157, 757, 822, 786]]<|/det|>
\[
x_0(t) = e^{-\delta t} [C_1 \cdot \sin(\omega_d t) + C_2 \cdot \cos(\omega_d t)] \quad \text{mit} \quad \omega_d = \sqrt{\omega_0^2 - \delta^2}
\]

<|ref|>text<|/ref|><|det|>[[115, 787, 741, 821]]<|/det|>
Eine partikuläre Lösung \(x_p\) der inhomogenen DGL erhält man mit dem Lösungsansatz 

<|ref|>equation<|/ref|><|det|>[[118, 820, 440, 838]]<|/det|>
\[
x_p = A \cdot \sin(\omega_0 t) + B \cdot \cos(\omega_0 t)
\]