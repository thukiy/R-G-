<|ref|>sub_title<|/ref|><|det|>[[33, 10, 512, 45]]<|/det|>
# Partielle Differentialgleichungen 

<|ref|>sub_title<|/ref|><|det|>[[25, 50, 250, 83]]<|/det|>
## Klassifizierung 

<|ref|>text<|/ref|><|det|>[[25, 85, 644, 120]]<|/det|>
Def: Gegeben sei \(\vec{F} : D \times \mathbb{R} \times \mathbb{R}^n \times \ldots \times \mathbb{R}^n \to \mathbb{R}^m\) 

<|ref|>text<|/ref|><|det|>[[108, 127, 888, 161]]<|/det|>
mit \(u(x) : D \subseteq \mathbb{R}^n \to \mathbb{R}\). Dann nennt man eine Gleichung der Form 

<|ref|>equation<|/ref|><|det|>[[50, 163, 750, 205]]<|/det|>
\[ \vec{F}(x, u(x), \frac{du(x)}{dx}, \ldots, \frac{du(x)}{dx}, \frac{d^2u(x)}{dx^2}, \frac{d^3u(x)}{dx^3}, \ldots, \frac{d^n u(x)}{dx^n}) = 0 \]

<|ref|>text<|/ref|><|det|>[[108, 208, 799, 237]]<|/det|>
eine partielle Differentialgleichung (PDGL) k-ter Ordnung 

<|ref|>text<|/ref|><|det|>[[80, 243, 620, 272]]<|/det|>
→ \(K\) ist die höchste vorkommende Ableitung 

<|ref|>text<|/ref|><|det|>[[25, 302, 739, 331]]<|/det|>
Bsp: PDGL 1. Ordnung, linear homogen (Transportgel.) 

<|ref|>equation<|/ref|><|det|>[[125, 333, 480, 375]]<|/det|>
\[ \frac{du(x)}{dt} + <\vec{a}, \nabla_x u(x, t)> \]

<|ref|>equation<|/ref|><|det|>[[125, 375, 515, 416]]<|/det|>
\[ = \frac{du(x)}{dt} + \sum_{i=1}^n a_i \cdot \frac{du(x)}{dx_i} = 0 \]

<|ref|>equation<|/ref|><|det|>[[125, 428, 561, 461]]<|/det|>
\[ u : \mathbb{R}^n \times \mathbb{R} \to \mathbb{R}, \quad \vec{x} = \left( \frac{x_1}{x_n} \right) \in \mathbb{R}^n \]

<|ref|>equation<|/ref|><|det|>[[125, 472, 350, 496]]<|/det|>
\[ t \in \mathbb{R}^+, \quad \vec{a} \in \mathbb{R}^n \]

<|ref|>text<|/ref|><|det|>[[25, 531, 400, 558]]<|/det|>
- Navier-Steokes-Gleichungen 

<|ref|>text<|/ref|><|det|>[[50, 568, 329, 595]]<|/det|>
(4 PDGL, 2. Ordnung) 

<|ref|>text<|/ref|><|det|>[[50, 606, 636, 636]]<|/det|>
→ Grundgleichungen der Störmungsmechanik 

<|ref|>equation<|/ref|><|det|>[[50, 638, 568, 710]]<|/det|>
\[ \frac{\partial \vec{v}}{\partial t} + <\vec{a}, \nabla_x \vec{v} > \vec{a} - \Delta_x \vec{v} = -\nabla_x p \quad (*) \]

<|ref|>equation<|/ref|><|det|>[[268, 685, 410, 708]]<|/det|>
\[ \text{div } \vec{a} = 0 \]

<|ref|>text<|/ref|><|det|>[[50, 740, 268, 769]]<|/det|>
\(p(x, t)\): Druck 

<|ref|>text<|/ref|><|det|>[[50, 777, 644, 806]]<|/det|>
\(\vec{a} : \mathbb{R}^3 \times \mathbb{R} \to \mathbb{R}^3\) (inkompressible Störmung) 

<|ref|>equation<|/ref|><|det|>[[50, 828, 540, 952]]<|/det|>
\[ \begin{aligned} \text{div } \vec{v} &= <\nabla, \vec{v}> & \vec{v} &= \left( \frac{v_1}{v_n} \right) \\ &= <\left( \frac{\partial x_1}{\partial x_n} \right), \left( \frac{v_1}{v_n} \right)> \\ \Delta \vec{v} &= <\nabla, \nabla> \vec{v} \end{aligned} \]