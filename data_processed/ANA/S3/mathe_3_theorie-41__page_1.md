<|ref|>text<|/ref|><|det|>[[230, 15, 737, 42]]<|/det|>
→ es liegt starke Dämpfung vor (Kriechfalle) 

<|ref|>text<|/ref|><|det|>[[28, 72, 938, 116]]<|/det|>
spezielle Lösungen: (betrachte AB, einnere das DGL 2. Ordnung: \(y(x) = C_1 e^{\lambda_1 x} + C_2 e^{\lambda_2 x}\)) 

<|ref|>text<|/ref|><|det|>[[28, 130, 583, 160]]<|/det|>
1) \(x(0) = A\) und \(\dot{x}(0) = 0\), d.h. \(t_0 = 0\) 

<|ref|>equation<|/ref|><|det|>[[92, 170, 423, 196]]<|/det|>
\[x(0) = C_1 + C_2 = A \iff\]

<|ref|>equation<|/ref|><|det|>[[92, 204, 415, 232]]<|/det|>
\[\dot{x}(t) = \lambda_1 C_1 e^{\lambda_1 t} + \lambda_2 C_2 e^{\lambda_2 t}\]

<|ref|>equation<|/ref|><|det|>[[92, 243, 370, 269]]<|/det|>
\[\dot{x}(0) = \lambda_1 C_1 + \lambda_2 C_2 = 0\]

<|ref|>text<|/ref|><|det|>[[92, 303, 397, 328]]<|/det|>
Einsetzen von \(C_2 = A - C_1\): 

<|ref|>equation<|/ref|><|det|>[[107, 340, 595, 365]]<|/det|>
\[\lambda_1 C_1 + \lambda_2 (A - C_1) = \lambda_1 C_1 + \lambda_2 A - \lambda_2 C_1 = 0\]

<|ref|>equation<|/ref|><|det|>[[107, 377, 360, 403]]<|/det|>
\[C_1 (\lambda_1 - \lambda_2) = -\lambda_2 A\]

<|ref|>equation<|/ref|><|det|>[[107, 410, 238, 443]]<|/det|>
\[C_1 = -\frac{\lambda_2 A}{\lambda_1 - \lambda_2}\]

<|ref|>equation<|/ref|><|det|>[[107, 450, 512, 485]]<|/det|>
\[C_2 = A - \left(-\frac{\lambda_2 A}{\lambda_1 - \lambda_2}\right) = \frac{(\lambda_1 + \lambda_2) A + \lambda_2 A}{\lambda_1 - \lambda_2} = \frac{\lambda_1 A}{\lambda_1 - \lambda_2}\]

<|ref|>equation<|/ref|><|det|>[[92, 515, 345, 540]]<|/det|>
\[\Rightarrow \text{das für AWP:}\]

<|ref|>equation<|/ref|><|det|>[[167, 545, 555, 579]]<|/det|>
\[x(t) = -\frac{\lambda_2 A}{\lambda_1 - \lambda_2} \cdot e^{\lambda_1 t} + \frac{\lambda_1 A}{\lambda_1 - \lambda_2} \cdot e^{\lambda_2 t}\]

<|ref|>text<|/ref|><|det|>[[28, 607, 533, 633]]<|/det|>
2) \(x(0) = 0\) und \(\dot{x}(0) = v_0\), \(t_0 = 0\) 

<|ref|>equation<|/ref|><|det|>[[92, 645, 536, 670]]<|/det|>
\[x(0) = C_1 + C_2 = 0 \iff C_2 = -C_1\]

<|ref|>equation<|/ref|><|det|>[[92, 685, 404, 710]]<|/det|>
\[\dot{x}(0) = \lambda_1 C_1 + \lambdabar_2 C_2 = v_0\]

<|ref|>text<|/ref|><|det|>[[92, 744, 365, 769]]<|/det|>
Einsetzen von \(C_2 = -C_1\): 

<|ref|>equation<|/ref|><|det|>[[107, 781, 375, 807]]<|/det|>
\[\lambda_1 C_1 + \lambda_2 \cdot (-C_1) = v_0\]

<|ref|>equation<|/ref|><|det|>[[107, 820, 320, 845]]<|/det|>
\[C_1 (\lambda_1 - \lambda_2) = v_0\]

<|ref|>equation<|/ref|><|det|>[[107, 854, 563, 888]]<|/det|>
\[C_1 = \frac{v_0}{\lambda_1 - \lambda_2} \quad C_2 = \frac{v_0}{\lambda_2 - \lambda_1} = -\frac{v_0}{\lambda_1 - \lambda_2}\]

<|ref|>equation<|/ref|><|det|>[[107, 890, 400, 920]]<|/det|>
\[x(t) = \frac{v_0}{\lambda_2 - \lambda_1} (e^{\lambda_1 t} - e^{\lambda_2 t})\]

<|ref|>text<|/ref|><|det|>[[639, 303, 960, 344]]<|/det|>
Starke Dämpfung (Kriechfall)
D > 0 

<|ref|>image<|/ref|><|det|>[[630, 384, 920, 536]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[640, 750, 841, 771]]<|/det|>
x(0)=0, dx/dt=v0 

<|ref|>image<|/ref|><|det|>[[630, 775, 940, 920]]<|/det|>