<|ref|>equation<|/ref|><|det|>[[149, 87, 810, 177]]<|/det|>
\[
\begin{align*}
&= \frac{4A}{T^2} \cdot \left( \frac{T^2}{4\pi^2 k^2} \cdot \sin\left(\frac{2\pi k}{T} \cdot T\right) - \frac{T}{2\pi k} \cdot T \cdot \cos\left(\frac{2\pi k}{T} \cdot T\right) - 0 + 0 \right) \\
&= \frac{A}{\pi^2 k^2} \cdot \sin(2\pi k) - \frac{2A}{\pi k} \cdot \cos(2\pi k) = \frac{A}{\pi^2 k^2} \cdot 0 - \frac{2A}{\pi k} \cdot 1 = -\frac{2A}{\pi k}.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[124, 184, 630, 203]]<|/det|>
Die reelle Fourier-Entwicklung des Signals ist daher 

<|ref|>equation<|/ref|><|det|>[[124, 213, 662, 266]]<|/det|>
\[
x_n(t) = \sum_{k=1}^{n} b_k \cdot \sin\left(\frac{2\pi k}{T} t\right) = -\frac{2A}{\pi} \sum_{k=1}^{n} \frac{1}{k} \cdot \sin\left(\frac{2\pi k}{T} t\right).
\]

<|ref|>text<|/ref|><|det|>[[114, 277, 145, 294]]<|/det|>
d) 

<|ref|>text<|/ref|><|det|>[[114, 291, 850, 310]]<|/det|>
Es liegt negative Parität vor, deshalb können wir eine reine Sinusreihe verwenden. 

<|ref|>equation<|/ref|><|det|>[[175, 317, 805, 373]]<|/det|>
\[
x(t) = \begin{cases} \frac{A}{4} \cdot t & |t \in [0, T/4] \\ 2A - \frac{A}{4} \cdot t & |t \in [T/4, T/2] \end{cases} = \begin{cases} \frac{4A}{T} t & |t \in [0, T/4] \\ 2A - \tfrac{4A}{T} t & |t \in [T/4, T/2] \end{cases}.
\]

<|ref|>text<|/ref|><|det|>[[130, 383, 571, 401]]<|/det|>
Für die reellen Fourier-Koeffizienten erhalten wir 

<|ref|>equation<|/ref|><|det|>[[130, 415, 196, 432]]<|/det|>
\(a_0 = 0\)

<|ref|>equation<|/ref|><|det|>[[130, 442, 196, 459]]<|/det|>
\(a_k = 0\)

<|ref|>equation<|/ref|><|det|>[[130, 468, 870, 675]]<|/det|>
\[
\begin{align*}
b_k &= \frac{2}{T} \int_T x(t) \cdot \sin\left(\frac{2\pi k}{T} t\right) dt = \frac{2}{T} \int_0^T x(t) \cdot \sin\left(\frac{2\pi k}{T} t\right)
dt \\
&= \frac{2}{T} \cdot 2 \int_0^{\frac{T}{2}} x(t) \cdot \sin\left(\frac{2\pi k}{T} t\right)\ dt = \frac{4}{T} \int_0^{\frac{T}{2}} x(t) \cdot \sin\left(\left(\frac{2\pi k}{T} t\right)\right) dt \\
&= \frac{4}{T} \left(\int_0^{\frac{T}{4}} \frac{4A}{T} t \cdot \sin\left(\frac{2\pi k}{T} t\right) dt + \int_{\frac{T}{4}}^{\frac{T}{2}} \left(2A - \frac{4A}{T} t\right) \cdot \sin\left(\frac{2\pi k}{T} t\right) dt\right) \\
&= \frac{16A}{T^2} \int_0^{\frac{T}{4}} t \cdot \sin\left(\frac{2\pi k}{T} t\right) dt - \frac{8A}{T} \int_{\frac{T}{4}}^{\frac{T}{2}} \sin\left(\frac{2\pi k}{T} t\right) dt - \frac{T}{T^2} \int_{\frac{T}{4}}^{\frac{T}{2}} t \cdot \sin\left(\frac{2\pi k}{T} t\right)dt \\
&= \frac{16A}{T^2} \int_0^{\frac{T^2}{4}} t \cdot \sin\left(\frac{2\pi k}{T} t \right) dt - \frac{8A}{T} \int_{\frac{T}{4}}^{\left(\frac{T}{2}\right)} \sin\left(\frac{2\pi k}{T} t\right) dt - \frac{\frac{T^2}{4}}{T^2} \int_{\frac{T}{4}}^{\frac{T^2}{2}} t \cdot \sin\left(\frac{2\pi k}{T} t \right)
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[130, 686, 371, 704]]<|/det|>
Die einzelnen Integrale sind 

<|ref|>equation<|/ref|><|det|>[[130, 714, 816, 895]]<|/det|>
\[
\begin{align*}
I_1 &= \int_0^{\frac{T}{4}} t \cdot \sin\left(\frac{3\pi k}{T} t\right) dt = \left[\frac{T^2}{4\pi^2 k^2} \cdot \sin\left(\left(\frac{2\pi k}{T} t\right)\cdot \frac{T}{2\pi k}\right) - \frac{T}{2\pi k} \cdot \frac{T}{4} \cdot \cos\left(\frac{2\pi k}{T} \cdot \frac{T}{4}\right)\right]_{0}^{\frac{T}{4}} \\
&= \frac{T^2}{4\pi^2 k^2} \cdot \sin\left(2\pi k \cdot \frac{T}{4}\right) - \frac{T}{2\pi k} \cdot \frac{T}{4}\cdot \cos\left(2\pi k \cdot \frac{T}{4}\right) - 0 + 0 \\
&= \frac{T^2}{4\pi^2 k^2} \cdot \frac{\sin\left(\pi k\right)}{2} - \frac{T^2}{8\pi k} \cdot \cos\left(\frac{\pi k}{2}\right)
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[117, 846, 581, 899]]<|/det|>
\[
I_2 = \int_{\frac{T}{4}}^{\frac{T}{2}} \sin\left(\frac{3\pi k}{T} t\right) dt = -\frac{T}{2\pi k} \cdot \left[\cos\left(\frac{2\pi k}{T} t\right)\right]_{\frac{T}{4}}^{\frac{T}{2}}
\]