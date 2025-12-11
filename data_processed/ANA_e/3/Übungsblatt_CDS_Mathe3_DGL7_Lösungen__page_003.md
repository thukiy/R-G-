<|ref|>equation<|/ref|><|det|>[[114, 80, 428, 118]]<|/det|>
\[
\underline{\delta} = \frac{R}{2L} \approx \frac{1.20 \Omega}{2 \cdot 1.50 \cdot 10^{-2} \text{ H}} \approx \frac{40.0}{s}.
\]

<|ref|>text<|/ref|><|det|>[[114, 137, 495, 156]]<|/det|>
Da \(\delta < \omega_0\), liegt schwache Dämpfung vor. 

<|ref|>text<|/ref|><|det|>[[114, 155, 144, 172]]<|/det|>
c) 

<|ref|>text<|/ref|><|det|>[[114, 170, 471, 189]]<|/det|>
Das System schwingt mit der Frequenz 

<|ref|>equation<|/ref|><|det|>[[114, 188, 680, 272]]<|/det|>
\[
\begin{align*}
\nu_d &= \frac{1}{2\pi} \cdot \omega_d = \frac{1}{2\pi} \cdot \sqrt{\omega_0^2 - \delta^2} = \frac{1}{2\pi} \cdot \sqrt{\frac{1}{LC} - \frac{R^2}{4L^2}} \\
&\approx \frac{1}{2\pi} \cdot \sqrt{\frac{1}{1.50 \cdot 10^{-2} \text{ H} \cdot 1.68 \cdot 10^{-4} \text{ F}}} - \frac{(1.20 \Omega)^2}{4 \cdot (1.50 \cdot 10^{-2} \text{ H})^2} \approx \frac{100 \text{ Hz}}{}
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[114, 286, 808, 305]]<|/det|>
4. Lösen von AWP von freien gedämpften harmonischen Schwingungen 

<|ref|>text<|/ref|><|det|>[[114, 304, 835, 339]]<|/det|>
Bestimmen Sie die Lösung des gegebenen AWP und bestimmen Sie die Lösung
sowohl in Sinus-Cosinus-Form als auch in Sinus-Phasen-Form. 

<|ref|>equation<|/ref|><|det|>[[114, 345, 660, 364]]<|/det|>
a) DGL: \(\ddot{x} + 4\dot{x} + 29x = 0\) b) DGL: \(\ddot{x} + \dot{x} + 2x = 0\)

<|ref|>equation<|/ref|><|det|>[[134, 363, 590, 400]]<|/det|>
\[
\text{AB: } x(0) = 1 \qquad \text{AB: } x(0) = 0 \\
\dot{x}(0) = -2. \qquad \dot{x}(0) = 3.
\]

<|ref|>text<|/ref|><|det|>[[114, 412, 144, 429]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[120, 430, 640, 450]]<|/det|>
\[
\lambda_{1/2} = -2 \pm 5j; \quad x = e^{-2t} [C_1 \cdot \sin (5t) + C_2 \cdot \cos (5t)];
\]

<|ref|>equation<|/ref|><|det|>[[120, 455, 666, 475]]<|/det|>
\[
\dot{x} = e^{-2t} [- (2C_1 + 5C_2) \cdot \sin (5t) + (5C_1 - 2C_2) \cdot \cos (5t)]
\]

<|ref|>equation<|/ref|><|det|>[[120, 482, 389, 501]]<|/det|>
\[
Lösung: x(t) = e^{-2t} \cdot \cos (5t)
\]

<|ref|>text<|/ref|><|det|>[[114, 500, 144, 517]]<|/det|>
b) 

<|ref|>equation<|/ref|><|det|>[[114, 515, 802, 580]]<|/det|>
\[
\begin{align*}
\lambda_{1/2} &= -\frac{1}{2} \pm \frac{1}{2} \sqrt{7}j; \quad x = e^{-\frac{1}{2}t} \left[ C_1 \cdot \sin \left( \frac{1}{2} \sqrt{7} t \right) + C_2 \cdot \cos \left( \frac{1}{2} \sqrt{7} t \right) \right]; \\
\dot{x} &= e^{-\frac{1}{2}t} \left[ -\frac{1}{2} (C_1 + \sqrt{7} C_2) \cdot \sin \left( \frac{1}{2} \sqrt{7} \right) + \frac{1}{2} (\sqrt{7} C_1 - C_2) \cdot \cos \left( \frac{1}{2} \sqrt{7} \right) \right]
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[120, 598, 506, 633]]<|/det|>
\[
Lösung: x(t) = \frac{6}{7} \sqrt{7} \cdot e^{-\frac{1}{2}t} \cdot \sin \left( \frac{1}{2} \sqrt{7} T \right)
\]

<|ref|>sub_title<|/ref|><|det|>[[114, 652, 723, 670]]<|/det|>
5. Aussagen über freie gedämpfte harmonische Schwingungen 

<|ref|>text<|/ref|><|det|>[[114, 669, 763, 704]]<|/det|>
Gegeben sei das folgende AWP der freien ungedämpften harmonischen
Schwingung: 

<|ref|>equation<|/ref|><|det|>[[114, 702, 315, 720]]<|/det|>
DGL: \(\ddot{x} + 6\dot{x} + 9x = 0\)

<|ref|>equation<|/ref|><|det|>[[114, 719, 238, 737]]<|/det|>
AB: \(x(3) = 5\)

<|ref|>equation<|/ref|><|det|>[[152, 737, 241, 755]]<|/det|>
\(\dot{x}(3) = 0\).

<|ref|>text<|/ref|><|det|>[[114, 760, 680, 779]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[114, 777, 878, 912]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Das AWP beschreibt ein schwach gedämpftes System.</td><td></td><td>X</td></tr><tr><td>b) Die Lösung des AWP verläuft durch den Punkt (5;-5).</td><td></td><td>X</td></tr><tr><td>c) Die Lösung des AWP hat ein lokales Maximum bei t = 3.</td><td>X</td><td></td></tr><tr><td>d) Die Lösung des AWP ist periodisch.</td><td></td><td>X</td></tr><tr><td>e) Für die Lösung des AWP gilt: lim t→∞ x(t) = 0.</td><td>X</td><td></td></tr><tr><td>f) Für die Lösung des AWP gilt: lim t→∞ x(t) = 0.<td>X</td><td></td></td></tr></table>