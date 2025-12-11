<|ref|>text<|/ref|><|det|>[[115, 81, 305, 100]]<|/det|>
Richtungsvektorfeld: 

<|ref|>image<|/ref|><|det|>[[117, 100, 870, 418]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[115, 422, 777, 460]]<|/det|>
Die ermittelte statische Lösung ist folglich ein globaler Attraktor und stabil.
c) 

<|ref|>text<|/ref|><|det|>[[115, 457, 633, 492]]<|/det|>
Die statische Lösung haben wir schon ermittelt: U = 12 V.
Nicht statische Lösungen mittels Trennung der Variablen: 

<|ref|>equation<|/ref|><|det|>[[130, 503, 370, 536]]<|/det|>
\[ \frac{dU_c}{dt} = -\frac{\lambda}{RC} \cdot (U_c - U) \]

<|ref|>equation<|/ref|><|det|>[[130, 540, 426, 615]]<|/det|>
\[ \frac{\lambda}{U_c - U} \cdot \frac{dU_c}{dt} = -\frac{\lambda}{RC} \cdot \frac{t}{U_c - U} \]

<|ref|>equation<|/ref|><|det|>[[130, 618, 405, 655]]<|/det|>
\[ \ln\left(\frac{U_c - U}{-U}\right) = -\frac{\lambda}{RC} \cdot (t - t_0) \]

<|ref|>equation<|/ref|><|det|>[[130, 655, 375, 691]]<|/det|>
\[ \frac{U_c - U}{-U} = e^{-\frac{\lambda}{RC} \cdot (t - t_0)} \]

<|ref|>equation<|/ref|><|det|>[[130, 689, 405, 725]]<|/det|>
\[ U_c - U = -U \cdot e^{-\frac{\lambda}{RC} \cdot (t - t_0)} \]

equation<|/ref|><|det|>[[130, 725, 621, 761]]<|/det|>
\[ U_c(t) = U(1 - e^{-\frac{\lambda}{RC} \cdot (t - t_0)}) \quad \text{Störung des AWP} \]

<|ref|>text<|/ref|><|det|>[[137, 770, 446, 792]]<|/det|>
Für den Strom I(t) ergibt sich: 

<|ref|>equation<|/ref|><|det|>[[137, 795, 565, 830]]<|/det|>
\[ I(t) = C \cdot \frac{dU_c}{dt} = C \cdot U \cdot \frac{\lambda}{RC} \cdot e^{-\frac{\lambda}{RC} \cdot (t - t_0)} = \frac{U}{R} \cdot e^{-\frac{\lambda}{RC} \cdot (t - t_0)}\]

<|ref|>equation<|/ref|><|det|>[[192, 841, 395, 877]]<|/det|>
\[ = \frac{U}{R} \cdot e^{-\frac{\lambda}{RC} \cdot(t - t_0)} \]