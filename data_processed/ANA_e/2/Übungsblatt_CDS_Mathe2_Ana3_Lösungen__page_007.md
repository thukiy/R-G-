<|ref|>text<|/ref|><|det|>[[115, 84, 144, 100]]<|/det|>
c) 

<|ref|>text<|/ref|><|det|>[[115, 99, 293, 116]]<|/det|>
mittels Substitution 

<|ref|>equation<|/ref|><|det|>[[120, 123, 350, 142]]<|/det|>
\[
u(r) := r^2 \Rightarrow u'(r) = 2r.
\]

<|ref|>equation<|/ref|><|det|>[[120, 144, 541, 181]]<|/det|>
\[
\frac{du}{dr} = 2r \Leftrightarrow du = 2r dr \Leftrightarrow dr = \frac{du}{2r} = \frac{1}{2r} du
\]

<|ref|>text<|/ref|><|det|>[[120, 191, 216, 207]]<|/det|>
und somit 

<|ref|>equation<|/ref|><|det|>[[120, 218, 780, 405]]<|/det|>
\[
\begin{align*}
F(r) &= \int r^3 \cos(r^2) \, dr = \int u \cdot r \cdot \cos(u) \cdot \frac{1}{2r} \, du = \frac{1}{2} \int u \cdot \cos(u) \, du \\
&= \frac{1}{2} \cdot \left( u \cdot \sin(u) - \int 1 \cdot \sin(u) \, du \right) = \frac{1}{2} \cdot \left( u \cdot \sin(u) + \int \sin(u) \, du \right) \\
&= \frac{1}{2} \cdot \left( u \cdot \sin(1) - (-1) \cdot \cos(u) + \tilde{c} \right) = \frac{1}{2} \cdot \left( u \cdot u \cdot \sin(u) + \cos(u) \right) + c \\
&= \frac{1}{2} \cdot \left( r^2 \cdot \sin(r^2) + \cos(r^2) \right) + c.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 406, 144, 423]]<|/det|>
d) 

<|ref|>text<|/ref|><|det|>[[115, 424, 780, 451]]<|/det|>
Wir zerlegen den Integrand \(f(x) = \frac{x}{\cos^2 x}\) wie folgt in ein Produkt aus zwei Faktoren \(u\) und \(v'\): 

<|ref|>equation<|/ref|><|det|>[[161, 452, 430, 504]]<|/det|>
\[
f(x) = \frac{x}{\cos^2 x} = x \cdot \frac{1}{\cos^2 x} = u v'
\]

<|ref|>text<|/ref|><|det|>[[115, 507, 880, 546]]<|/det|>
**Begründung:** Diese Zerlegung hat Aussicht auf Erfolg, da \(v' = \frac{1}{\cos^2 x}\) bekanntlich die *Ableitung* von \(\tan x\) ist.
Mit der gewählten Zerlegung 

<|ref|>equation<|/ref|><|det|>[[161, 552, 565, 584]]<|/det|>
\[
u = x, \quad v' = \frac{1}{\cos^2 x} \quad \text{und damit} \quad u' = 1, \quad v = \tan x
\]

<|ref|>text<|/ref|><|det|>[[115, 591, 480, 606]]<|/det|>
führt die *partielle Integration* zu folgendem Ergebnis: 

<|ref|>equation<|/ref|><|det|>[[161, 612, 870, 710]]<|/det|>
\[
\begin{align*}
I &= \int \frac{x}{\cos^2 x} \, dx = \int x \cdot \frac{1}{\cos^2 x} \, dx = \int u v' \, dx = u v - \int u' v \, dx = x \cdot \tan x - \int 1 \cdot \tan x \, dx = \\
&= x \cdot \tan x - \int \tan x \, dx = x \cdot \tan x - I_1 \\
I_1
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 712, 880, 750]]<|/det|>
Das „Hilfsintegral“ \(I_1\) ist zwar *kein* Grundintegral, lässt sich aber durch eine *Substitution* leicht lösen, wenn man die
trigonometricische Beziehung \(\tan x = \frac{\sin x}{\cos x}\) beachtet: 

<|ref|>equation<|/ref|><|det|>[[161, 757, 373, 789]]<|/det|>
\[
I_1 = \int \tan x \, dx = \int \frac{\sin x}{\cos x} \, dx
\]

<|ref|>text<|/ref|><|det|>[[115, 795, 880, 823]]<|/det|>
Im Zähler steht – vom Vorzeichen abgesehen – die *Ableitung* des Nenners, das Integral \(I_1\) ist daher durch die *Substitution* \(u = \cos x\) wie folgt lösbar 

<|ref|>equation<|/ref|><|det|>[[161, 830, 460, 861]]<|/det|>
\[
u = \cos x, \quad \frac{du}{dx} = -\sin x, \quad dx = \frac{du}{-\sin x}
\]

<|ref|>equation<|/ref|><|det|>[[161, 867, 856, 900]]<|/det|>
\[
I_1 = \int \tan x \, dx = \int (\frac{\sin x}{\cos x}) \, dx = \int \frac{\sin x}{u} \cdot \frac{du}{-\sin x} = -\int \frac{1}{u} \, du = -\ln |u| + C = -\ln |\cos x| + C
\]