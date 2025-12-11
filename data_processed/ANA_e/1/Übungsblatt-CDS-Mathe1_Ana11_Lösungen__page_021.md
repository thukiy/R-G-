<|ref|>text<|/ref|><|det|>[[123, 66, 270, 85]]<|/det|>
f) Wir erhalten 

<|ref|>equation<|/ref|><|det|>[[150, 96, 920, 191]]<|/det|>
\[
\begin{align*}
I &= \int_u^{-v} (2wu - 6vw^2 + 1) \, \mathrm{d}w = \left[ uw^2 - 2vw^3 + w \right]_{w=u}^{w=-v} \\
&= u \cdot (-v)^2 - 2v \cdot (-v)^3 - v - u \cdot u^2 + 2v \cdot u^3 - u = uv^2 + 2v^4 - v - u^3 + 2vu^3 - u \\
&= 2v^4 + 2u^3v - u^3 + uv^2 - u - v.
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[107, 221, 611, 240]]<|/det|>
13. Aufleitung von eigentlichen Exponentialfunktionen 

<|ref|>text<|/ref|><|det|>[[107, 238, 816, 257]]<|/det|>
Wir berechnen die folgenden unbestimmten Integrale durch elementares Aufleiten. 

<|ref|>text<|/ref|><|det|>[[121, 262, 270, 281]]<|/det|>
a) Wir erhalten 

<|ref|>equation<|/ref|><|det|>[[150, 293, 920, 330]]<|/det|>
\[
\frac{F(x)}{x} = \int e^x \, \mathrm{d}x = \frac{e^x + c}{\ln(2)}. \quad (52)
\]

<|ref|>text<|/ref|><|det|>[[121, 343, 270, 362]]<|/det|>
b) Wir erhalten 

<|ref|>equation<|/ref|><|det|>[[150, 372, 920, 415]]<|/det|>
\[
\frac{F(x)}{x} = \int 2^x \, \mathrm{d}x = \frac{1}{\ln(2)} \cdot 2^x + c. \quad (53)
\]

<|ref|>text<|/ref|><|det|>[[121, 432, 655, 451]]<|/det|>
c) Wir zeigen zwei Varianten, um diese Teilaufgabe zu lösen. 

<|ref|>text<|/ref|><|det|>[[150, 455, 622, 473]]<|/det|>
Variante 1: Durch elementares Aufleiten erhalten wir 

<|ref|>equation<|/ref|><|det|>[[170, 485, 920, 521]]<|/det|>
\[
\frac{F(x)}{x} = \int e^{-x} \, \mathrm{d}x = -e^{-x} + c = c - e^{-x}. \quad (54)
\]

<|ref|>text<|/ref|><|det|>[[150, 532, 900, 551]]<|/det|>
Variante 2: Durch Umformen des Integranden und elementares Aufleiten erhalten wir 

<|ref|>equation<|/ref|><|det|>[[170, 561, 920, 641]]<|/det|>
\[
\begin{align*}
F(x) &= \int e^{-x} \, \mathrm{d}x = \int \frac{1}{e^x} \, \mathrm{d}x = \int \left(\frac{1}{e}\right)^x \, \mathrm{d}x = \frac{1}{\ln\left(\frac{1}{e}\right)} \cdot \left(\frac{1}{e}\right)^x + c = \frac{1}{-\ln(e)} \cdot \frac{1}{e^x} + c \\
&= \frac{1}{-1} \cdot e^{-x} + c = \frac{c - e^{-x}}{e}. \tag{55}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[121, 655, 655, 673]]<|/det|>
d) Wir zeigen zwei Varianten, um diese Teilaufgabe zu lösen. 

<|ref|>text</td><td>Variante 1: Durch elementares Aufleiten erhalten wir</td></tr></table> 

<|ref|>equation<|/ref|><|det|>[[170, 707, 911, 746]]<|/det|>
\[
\frac{F(x)}{x} = \int 2^{-x} \, \mathrm{d}x = -\frac{1}{\ln(2)} \cdot 2^{-x} + c = c - \frac{1}{\ln(2)} \cdot 2^{-x}. \quad (56)
\]

<|ref|>text<|/ref|><|det|>[[150, 764, 900, 783]]<|/det|>
Variante 2: Durch Umformen des Integranden und elementares Aufleithen erhalten wir 

<|ref|>equation<|/ref|><|det|>[[170, 793, 911, 878]]<|/det|>
\[
\begin{align*} \frac{F(x)}{x} &= \int 2^{-x} \, \mathrm{d}x = \int \frac{1}{2^x} \, \mathrm{d}x = \int \left(\frac{1}{2}\right)^x \, \mathrm{d}x = \frac{1}{\ln\left(\frac12\right)} \cdot \left(\frac{1}{2}\right)^x + c = \frac{1}{-\ln(2)} \cdot \frac{1}{2^x} + c \\ &= -\frac{1}{\ln(2)} \cdot 2^{-x} + c = \frac{1}{\ln(2)} \cdot 2^{-x}. \end{align*}
\]