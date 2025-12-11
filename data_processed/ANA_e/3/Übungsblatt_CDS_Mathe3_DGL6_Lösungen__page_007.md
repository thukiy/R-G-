<|ref|>text<|/ref|><|det|>[[114, 81, 850, 144]]<|/det|>
Diese Gleichung differenzieren wir nach der Zeit und nutzen die Beziehung \(I = \frac{dq}{dt}\).
Dies ergibt dann die DGL einer freien ungedämpften elektromagnetischen
Schwingung: 

<|ref|>equation<|/ref|><|det|>[[114, 140, 261, 170]]<|/det|>
\[ \frac{d^2I}{dt^2} + \frac{1}{LC} \cdot \frac{dq}{dt} = 0. \]

<|ref|>equation<|/ref|><|det|>[[114, 166, 370, 195]]<|/det|>
\[ \text{Mit } \omega^2 = \frac{1}{LC} \cdot \frac{d^2I}{dt^2} + \omega^2 \cdot I = 0. \]

<|ref|>text<|/ref|><|det|>[[114, 193, 485, 211]]<|/det|>
Diese DGL besitzt die allgemeine Lösung 

<|ref|>equation<|/ref|><|det|>[[114, 209, 415, 228]]<|/det|>
\[ I(t) = K_1 \cdot \sin(\omega t) + K_2 \cdot \cos(\omega t). \]

<|ref|>text<|/ref|><|det|>[[114, 226, 750, 245]]<|/det|>
Mit Hilfe der Anfangsbedingungen können \(K_1\) und \(K_2\) bestimmt werden: 

<|ref|>text<|/ref|><|det|>[[144, 243, 844, 263]]<|/det|>
1. Der Strom ist zu Beginn der Schwingung, also bei \(t = 0\), gleich 0: \(I(0) = 0\). 

<|ref|>text<|/ref|><|det|>[[144, 260, 723, 280]]<|/det|>
2. Die Spannung am Kondensator ist zu Beginn \(U_0\): \(U_C(0) = U_0\). 

<|ref|>text<|/ref|><|det|>[[114, 277, 678, 296]]<|/det|>
Verwenden dieser Anfangsbedingungen für die Maschenregel: 

<|ref|>equation<|/ref|><|det|>[[114, 293, 446, 349]]<|/det|>
\[ U_L(0) + U_C(0) = L \cdot \left( \frac{dI}{dt} \right)_{t=0} + U_0 = 0. \]

<|ref|>equation<|/ref|><|det|>[[114, 323, 320, 352]]<|/det|>
\[ \Rightarrow \left( \frac{dI}{dt} \right)_{t=0} = -\frac{U_0}{L} \]

<|ref|>text<|/ref|><|det|>[[114, 348, 501, 367]]<|/det|>
Für die Integrationskonstanten ergibt sich: 

<|ref|>equation<|/ref|><|det|>[[114, 365, 513, 384]]<|/det|>
\[ I(0) = 0 \Rightarrow K_1 \cdot \sin(0) + K_2 \cdot \cos(0) = K_2 = 0 \]

<|ref|>equation<|/ref|><|det|>[[114, 389, 707, 430]]<|/det|>
\[ \frac{dI}{dt} = \frac{d}{dt} [K_1 \cdot \sin(\omega t) + K_2 \cdot \cos(\dot{\omega} t)] = \omega K_1 \cdot \cos(\omega t) - \omega K_2 \cdot \sin(\omega t) \\ = \omega [K_1 \cdot \cos(\omega t) - K_2 \cdot \sin(\dot{\omega} t)] \]

<|ref|>equation<|/ref|><|det|>[[114, 435, 635, 472]]<|/det|>
\[ \left( \frac{dI}{dt} \right)_{t=0} = -\left( \frac{U_0}{L} \right) \Rightarrow \omega [K_1 \cdot \cos(0) - K_2 \cdot \sin(0)] = \omega K_1 = -\frac{U_0}{L} \]

<|ref|>equation<|/ref|><|det|>[[114, 467, 420, 504]]<|/det|>
\[ \Rightarrow K_1 = -\frac{U_0}{\omega L} = -\frac{U_0\sqrt{LC}}{L} = -U_0\sqrt{\frac{C}{L}} \]

<|ref|>text<|/ref|><|det|>[[114, 501, 666, 520]]<|/det|>
Im Schwingkreis fliesst somit der sinusförmige Wechselstrom 

<|ref|>equation<|/ref|><|det|>[[114, 518, 671, 590]]<|/det|>
\[ \begin{aligned} I(t) &= -U_0\sqrt{\frac{C}{L}} \cdot \sin(\omega t) = -I_0 \cdot \sin(\omega t) = I_0 \cdot \sin(\omega t + \pi), \quad t \ge 0 \\ \text{mit } I_0 &= U_0\sqrt{\frac{C}{L}} \text{ und } \omega = \frac{1}{\sqrt{LC}}. \end{aligned} \]

<|ref|>text<|/ref|><|det|>[[114, 588, 671, 607]]<|/det|>
Wenn wir die gegebenen Zahlenwerte einsetzen, erhalten wir: 

<|ref|>equation<|/ref|><|det|>[[114, 605, 380, 624]]<|/det|>
\[ I(t) = 0,1A \cdot \sin(1000/s + \pi). \]

<|ref|>text<|/ref|><|det|>[[114, 622, 580, 641]]<|/det|>
Der zeitliche Verlauf ist im I-t-Diagramm dargestellt. 

<|ref|>image<|/ref|><|det|>[[234, 659, 760, 880]]<|/det|>