<|ref|>sub_title<|/ref|><|det|>[[114, 81, 860, 101]]<|/det|>
4. Anfangsbedingungen der freien ungedämpften harmonischen Schwingung 

<|ref|>text<|/ref|><|det|>[[114, 99, 850, 135]]<|/det|>
Sei \(\omega > 0\) und \(x_0, v_0 \in \mathbb{R}\). Gegeben sei das folgende AWP der freien ungedämpften harmonischen Schwingung 

<|ref|>equation<|/ref|><|det|>[[114, 133, 283, 151]]<|/det|>
\[
\text{DGL: } \ddot{x} + \omega^2 x = 0
\]

<|ref|>equation<|/ref|><|det|>[[114, 150, 252, 169]]<|/det|>
\[
\text{AB: } x(t_0) = x_0
\]

<|ref|>equation<|/ref|><|det|>[[152, 168, 257, 186]]<|/det|>
\[
\dot{x}(t_0) = v_0.
\]

<|ref|>text<|/ref|><|det|>[[114, 184, 533, 202]]<|/det|>
a) Wie müssen \(C, S \in \mathbb{R}\) gewählt werden, damit 

<|ref|>equation<|/ref|><|det|>[[144, 201, 785, 220]]<|/det|>
\[
x(t) := C \cdot \cos(\omega(t - t_0)) + S \cdot \sin(\omega(t - t_0)) \text{ eine Lösung des AWP ist?}
\]

<|ref|>text<|/ref|><|det|>[[114, 219, 852, 254]]<|/det|>
b) Wie müssen \(A, \varphi_0 \in \mathbb{R}\) gewählt werden, damit \(x(t) := A \cdot \sin(\omega(t - t_0) + \varphi_0)\) eine Lösung des AWP ist? 

<|ref|>text<|/ref|><|det|>[[114, 252, 850, 288]]<|/det|>
c) Welche Zusammenhänge bestehen zwischen den Parameterpaaren (C,S) und (A,φ₀)? 

<|ref|>text<|/ref|><|det|>[[144, 285, 850, 321]]<|/det|>
Hinweis: Verwenden Sie die Argumentfunktion, die von den komplexen Zahlen bekannt ist, um \(\varphi_0\) durch C und S auszudrücken. 

<|ref|>text<|/ref|><|det|>[[114, 336, 144, 353]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[114, 351, 327, 369]]<|/det|>
Ableiten des Ansatzes: 

<|ref|>equation<|/ref|><|det|>[[114, 367, 639, 415]]<|/det|>
\[
\begin{align*}
\dot{x}(t) &= C \cdot (-\omega) \cdot \sin(\omega \cdot (t - t_0)) + S \cdot \omega \cdot \cos(\omega \cdot (t - t_0)) \\
&= \omega S \cdot \cos(\omega \cdot (t - t_0)) - \omega C \cdot \sin(\omega \cdot (t - t_0)).
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 415, 300, 433]]<|/det|>
Einsetzen der ABs: 

<|ref|>equation<|/ref|><|det|>[[114, 431, 825, 480]]<|/det|>
\[
\begin{align*}
x_0 &= x(t_0) = C \cdot \cos(\omega \cdot (t_0 - t_0)) + S \cdot \sin(\omega \cdot (t_0 - t_0)) = C \cdot \cos(0) + S \cdot \sin(0) \\
&= C \cdot 1 + S \cdot 0 = C
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[114, 487, 875, 534]]<|/det|>
\[
\begin{align*}
v_0 &= \dot{x}(t_0) = \omega S \cdot \cos(\omega \cdot (t_0 - t_0)) - \omega C \cdot \sin(\omega \cdot (t_0 - t_0)) = \omega S \cdot \cos(0) - \omega C \cdot \sin(0) \\
&= \omega S \cdot 1 + \omega C \cdot 0 = \omega S.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[114, 533, 377, 560]]<|/det|>
Es ergibt sich: \(C = x_0, S = \frac{v_0}{\omega}\). 

<|ref|>text<|/ref|><|det|>[[114, 558, 144, 575]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[114, 574, 333, 592]]<|/det|>
Ableitung des Ansatzes 

<|ref|>equation<|/ref|><|det|>[[114, 590, 690, 611]]<|/det|>
\[
\dot{x}(t) = A \cdot \omega \cdot \cos(\omega \cdot (t - t_0) + \varphi_0) = \omega A \cdot \cos(\omega \cdot (t - t_0) + \varphi_1)
\]

<|ref|>text<|/ref|><|det|>[[114, 611, 300, 628]]<|/det|>
Einsetzen der ABs: 

<|ref|>equation<|/ref|><|det|>[[114, 627, 757, 648]]<|/det|>
\[
x_0 = x(t_0) = A \cdot \sin(\omega \cdot (t_0 - t_0) + \varphi_0) = A \cdot \sin(0 + \varphi_0) = A \cdot \sin(\varphi_0)
\]

<|ref|>equation<|/ref|><|det|>[[114, 655, 805, 677]]<|/det|>
\[
v_0 = \dot{x}(t_0) = \omega A \cdot \cos(\omega \cdot (t_0 - t_0) + \varphi_1) = \omega A \cdot \cos(0 + \varphi_0) = \omega A \cdot \cos(\varphi_0)
\]

<|ref|>text<|/ref|><|det|>[[114, 676, 608, 695]]<|/det|>
Wir erhalten somit das nicht-lineare Gleichungssystem 

<|ref|>equation<|/ref|><|det|>[[122, 696, 345, 722]]<|/det|>
I: \(A \cdot \sin(\varphi_0) = x_0\)

<|ref|>equation<|/ref|><|det|>[[114, 725, 348, 763]]<|/det|>
II: \(A \cdot \cos(\varphi_0) = \frac{v_0}{\omega}\)

<|ref|>text<|/ref|><|det|>[[114, 765, 530, 784]]<|/det|>
Zur Lösung verwenden wir die komplexe Zahl 

<|ref|>equation<|/ref|><|det|>[[114, 783, 680, 818]]<|/det|>
\[
z := A \cdot \cos(\varphi_0) = A \cdot \cos(\varphi_0) + i \cdot A \cdot \sin(\varphi_0) = \frac{v_0}{\omega} + i \cdot x_0
\]

<|ref|>text<|/ref|><|det|>[[114, 817, 244, 835]]<|/det|>
Es ergibt sich