<|ref|>sub_title<|/ref|><|det|>[[118, 83, 410, 102]]<|/det|>
Partielle Ableitungen 2. Ordnung 

<|ref|>equation<|/ref|><|det|>[[174, 111, 884, 285]]<|/det|>
\[
\begin{align*}
z_{xx} &= \frac{\partial}{\partial x} z_x = \frac{\partial}{\partial x} [e^y - y \cdot e^x] = 0 - y \cdot e^x = -y \cdot e^x \\
z_{xy} &= \frac{\partial}{\partial y} z_x = \frac{\partial}{\partial y} [e^y - y \cdot e^x] = e^y - 1 \cdot e^x = e^y - e^x \\
z_{yx} &= \frac{\partial}{\partial x} z_y = \frac{\partial}{\partial x} [x \cdot e^y - e^x] = 1 \cdot e^y - e^x = e^y - e^x \\
z_{yy} &= \frac{\partial}{\partial y} z_y = \frac{\partial}{\partial y} [x \cdot e^y - e^x] = x \cdot e^y - 0 = x \cdot e^y
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[118, 285, 152, 303]]<|/det|>
b) 

<|ref|>sub_title<|/ref|><|det|>[[118, 302, 410, 320]]<|/det|>
Partielle Ableitungen 1. Ordnung 

<|ref|>text<|/ref|><|det|>[[118, 325, 456, 344]]<|/det|>
Wir verwenden wie folgt die Kettenregel: 

<|ref|>equation<|/ref|><|det|>[[174, 352, 839, 491]]<|/det|>
\[
\begin{align*}
z &= \ln \left( 2y - x^2 \right) = \ln u \quad \text{mit} \quad u = 2y - x^2 \quad \text{und} \quad \frac{\partial u}{\partial x} = -2x, \quad \frac{\partial u}{\partial y} = 2 \\
z_x &= \frac{\partial z}{\partial x} = \frac{\partial z}{\partial u} \cdot \frac{\partial u}{\partial x} = \frac{1}{u} \cdot (-2x) = -\frac{2x}{u} = -\frac{2x}{2y - x^2} \\
z_y &= \frac{\partial z}{\partial y} = \frac{\partial z}{\partial u} \cdot \frac{\partial u}{\gamma y} = \frac{1}{u} \cdot 2 = \frac{2}{u} = \frac{2}{2y - x^2}
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[118, 493, 365, 510]]<|/det|>
Partielle Ableitungen 2. Ordnung 

<|ref|>text<|/ref|><|det|>[[118, 514, 748, 531]]<|/det|>
\(z_{xx}\) erhalten wir, indem wir \(z_x\) mit Hilfe der Quotientenregel partiell nach \(x\) differenzieren: 

<|ref|>equation<|/ref|><|det|>[[168, 536, 884, 618]]<|/det|>
\[
\begin{align*}
z_x &= \frac{-2x}{2y - x^2} = \frac{u}{v} \quad \text{mit} \quad u = -2x, \quad v = 2y - x^2 \quad \text{und} \quad u_x = -2, \quad v_x = -2x \\
z_{xx} &= \frac{\partial z_x}{\partial x} = \frac{u_x v - v_x u}{v^2} = \frac{-2(2y - x^2) - (-2x)(-2x)}{(2y - x^2)^2} = \frac{-4y + 2x^2 - 4x^2}{(2y - x^2)^2} = \frac{-2x^2 - 4y}{(2y - x^2)^2}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[118, 623, 760, 640]]<|/det|>
\(z_{xy}\) erhält man aus \(z_x\) durch partielles Differenzieren nach \(y\). Wir benötigen die Kettenregel: 

<|ref|>equation<|/ref|><|det|>[[168, 645, 790, 730]]<|/det|>
\[
\begin{align*}
z_x &= \frac{-2x}{2y-x^2} = -2x(2y-x^2)^{-1} = -2x \cdot u^{-1} \quad \text{mit} \quad u = 2y - x^2 \text{ und } \frac{\partial u}{\partial y} = 2 \\
z_{xy} &= \frac{\partial z_x}{\partial y} = \frac{\partial z_x}{\partial u} \cdot \frac{\partial u}{\partial y} = -2x(-1 \cdot u^{-2}) \cdot 2 = 4x \cdot u^{-2} = \frac{4x}{u^2} = \frac{4x}{(2y-x^2)^2}
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[118, 730, 880, 759]]<|/det|>
Alternative: Sie differenzieren nach der Quotientenregel, wobei der Zähler eine konstante, d.h. von der Variablen \(y\) unabhängige Funktion ist. 

<|ref|>text<|/ref|><|det|>[[118, 765, 880, 794]]<|/det|>
\(z_{yx}\) erhalten wir, indem wir \(z_y\) mit Hilfe der Quotienten- oder Kettenregel partiell nach \(x\) differenzieren. Wir wollen an dieser Stelle die Quotientenregel verwenden: 

<|ref|>equation<|/ref|><|det|>[[162, 799, 714, 832]]<|/det|>
\[
z_y = \frac{2}{2y - x^2} = \frac{u}{v} \quad \textmit \quad u = 2, \quad v = 2y - x^2 \quad \textund \quad u_x = 0, \quad v_x = -2x
\]

<|ref|>equation<|/ref|><|det|>[[162, 839, 640, 874]]<|/det|>
\[
z_{yx} = \frac{\partial z_y}{\partial x} = \frac{u_x v - v_x u}{v^2} \quad = \frac{0(2y - x^2) - (-2x) \cdot 2}{(2y - x^2)^2} = \frac{4x}{(2y - x^2)^2}
\]