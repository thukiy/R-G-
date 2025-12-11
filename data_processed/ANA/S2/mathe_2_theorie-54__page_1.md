<|ref|>text<|/ref|><|det|>[[20, 13, 555, 42]]<|/det|>
Bsp: \(f: \mathbb{R}^2 \to \mathbb{R}\) \(f(x, y) = x^2 + y^2\) 

<|ref|>equation<|/ref|><|det|>[[130, 45, 520, 78]]<|/det|>
\[ \vec{v}: \mathbb{R}^2 \to \mathbb{R}^2 \quad \vec{v}(x, y) = (-\vec{x}) \]

<|ref|>equation<|/ref|><|det|>[[130, 85, 754, 118]]<|/det|>
\[ \vec{v}(t) = \left( \frac{\cos t}{t} \right) \quad t \in [0, 2\pi] \quad \vec{v}(t) = \left( \frac{-\sin t}{\cos t} \right) \]

<|ref|>text<|/ref|><|det|>[[130, 149, 451, 175]]<|/det|>
Schaares Kurvenintegrale: 

<|ref|>equation<|/ref|><|det|>[[140, 181, 775, 240]]<|/det|>
\[ \begin{aligned} \frac{2\pi}{\omega} \int f(\vec{v}(t)) \cdot |\vec{v}(t)| \, dt &= \frac{2\pi}{\omega} \int (\cos^2 t + \sin^2 t) \cdot \sqrt{(-\sin t)^2 + \cos^2 t} \, dt \\ &= \frac{2\pi}{\omega} \int 1 \, dt = [t] \frac{2\pi}{\omega} = 2\pi \end{aligned} \]

<|ref|>text<|/ref|><|det|>[[130, 266, 475, 291]]<|/det|>
velobrieëles Kurvenintegrale: 

<|ref|>equation<|/ref|><|det|>[[140, 297, 925, 330]]<|/det|>
\[ \frac{2\pi}{\omega} < \left( \frac{-\sin t}{\cos t} \right), \left( \frac{-\sin t}{\cos t} \right) > dt = \frac{2\pi}{\omega} \int (\sin^2 t + \cos^2 t) \, dt = \frac{2\pi}{\omega} \int 1 \, dt = 2\pi \]

<|ref|>text<|/ref|><|det|>[[20, 386, 955, 490]]<|/det|>
Def: Velbortfeld \(\vec{v}\) heisst konsekativ oder Polenklaffeld /gradientenfeld, wenn
\(\int \vec{v} \cdot d\vec{s} >\) nun von Anfangs- und Endpunkt aber nicht von dem Weg abhängig. 

<|ref|>text<|/ref|><|det|>[[70, 519, 750, 546]]<|/det|>
→ für konsekatives Vektorfeld \(\vec{v}\) gibt es ein Skaarfeld 

<|ref|>equation<|/ref|><|det|>[[130, 553, 787, 680]]<|/det|>
\[ \begin{aligned} f: D \subseteq \mathbb{R}^m \to \mathbb{R} \quad \text{mit} \quad \vec{v}f = \vec{v} \\ \Rightarrow \frac{\partial f}{\partial x_1} = v_1, \quad \frac{\partial f}{\partial x_2} = v_2 \quad \ldots \quad \frac{\partial f}{\partial x_m} = v_m, \quad \vec{v} = \left( \begin{array}{c} v_1 \\ \vdots \\ v_m \end{array} \right) \\ \Rightarrow f \text{ heisst Polenklauf von } \vec{v} \text{ bau. Stammfunktion von } \vec{v} \\ \Rightarrow \int \vec{v} \cdot d\vec{s} > = f(\vec{v}(b)) - f(\vec{v}(a)) \end{aligned} \]

<|ref|>equation<|/ref|><|det|>[[70, 686, 704, 712]]<|/det|>
\[ \text{mit } \vec{v}: [a, b] \to D \subseteq \mathbb{R}^m, \quad \vec{v}: D \subseteq \mathbb{R}^m \to \mathbb{R}^m \]

<|ref|>equation<|/ref|><|det|>[[70, 750, 320, 787]]<|/det|>
\[ \Rightarrow \oint \vec{v} \cdot d\vec{s} > = 0 \]