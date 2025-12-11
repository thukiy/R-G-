<|ref|>equation<|/ref|><|det|>[[120, 80, 400, 144]]<|/det|>
\[
\mathbf{P} = \begin{bmatrix} 0 \\ 0 \\ h \end{bmatrix} \quad \text{und} \quad s_0 = \begin{bmatrix} 0 \\ -a \\ 0 \end{bmatrix}.
\]

<|ref|>text<|/ref|><|det|>[[115, 146, 876, 199]]<|/det|>
Wir bestimmen nun den Vektor \(\mathbf{v}\) in Flugrichtung des Flugzeugs, wobei wir diesen
Vektor aus seinem horizontalen \(\mathbf{v}_\parallel\) und vertikalen \(\mathbf{v}_\perp\) Anteil zusammensetzen. Da das
Flugzeug in nordwestliche Richtung fliegt können wir wählen 

<|ref|>equation<|/ref|><|det|>[[120, 199, 220, 260]]<|/det|>
\[
\mathbf{v}_\parallel := \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}
\]

<|ref|>equation<|/ref|><|det|>[[120, 264, 513, 285]]<|/det|>
\[
\Delta l := |\mathbf{v}_\parallel| = \sqrt{1^2 + 1^2 + 0^2} = \sqrt{1 + 1 + 0} = \sqrt{2}.
\]

<|ref|>equation<|/ref|><|det|>[[120, 287, 480, 360]]<|/det|>
\[
\mathbf{v}_\perp = \begin{bmatrix} 0 \\ 0 \\ \Delta h \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ S \cdot \Delta l \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ S \cdot \sqrt{2} \end{bmatrix}
\]

<|ref|>equation<|/ref|><|det|>[[115, 360, 525, 409]]<|/det|>
\[
\mathbf{v} = \mathbf{v}_\parallel + \mathbf{v}_\perp = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix} + \begin{bmatrix} 0 \\ 0 \\ S \cdot \sqrt{2} \right) = \begin{bmatrix} 1 \\ 1 \\ \sqrt{2} \cdot S \end{bmatrix}
\]

<|ref|>text<|/ref|><|det|>[[115, 410, 500, 429]]<|/det|>
Die Flugbahn des Flugzeugs ergibt sich zu 

<|ref|>equation<|/ref|><|det|>[[115, 428, 481, 488]]<|/det|>
\[
\mathbf{s}(\tau) = \mathbf{s}_0 + \tau \cdot \mathbf{v} = \begin{bmatrix} 0 \\ -a \\ 0 \end{bmatrix} + \tau \cdot \begin{bmatrix} 1 \\ 1 \\ \sqrt{2} \cdot S \right).
\]

<|ref|>text<|/ref|><|det|>[[115, 490, 864, 525]]<|/det|>
Für die Berechnung des Abstands der Spitze des Sendemasts zu der Flugbahn des
Flugzeugs (Abstand eines Punktes von einer Geraden in 3D) 

<|ref|>equation<|/ref|><|det|>[[115, 523, 752, 585]]<|/det|>
\[
\mathbf{u} = (\mathbf{P} - \mathbf{s}_0) \times \mathbf{v} = \begin{bmatrix} 0 \\ 0 \\ h \end{bmatrix} - \begin{bmatrix} 0 \\ -a \\ 0 \end{bmatrix} \times \begin{bmatrix} 1 \\ 1 \\ \sqrt{2} \cdot S \cdot h \end{bmatrix} = \begin{bmatrix} 0 \\ a \\ h \end{bmatrix} \times \begin{bmatrix} 1 \\ 1 \\ \sqrt{3} \cdot S \end{bmatrix}
\]

<|ref|>equation<|/ref|><|det|>[[120, 588, 505, 655]]<|/det|>
\[
= \begin{bmatrix} a \cdot \sqrt{2} \cdot S - h \cdot 1 \\ h \cdot 1 - 0 \cdot \sqrt{2} \cdot S \\ 0 \cdot 1 - a \cdot 1 \end{bmatrix} = \begin{bmatrix} \sqrt{2} \cdot S \cdot a - h \\ h \\ -a \end{bmatrix}.
\]

<|ref|>equation<|/ref|><|det|>[[115, 656, 475, 710]]<|/det|>
\[
\underline{d} = \frac{|\mathbf{u}|}{|\mathbf{v}|} = \frac{\sqrt{(\sqrt{2} \cdot S \cdot a - h)^2 + h^2 + (-a)^2}}{\sqrt{1^2 + 1^2 + (\sqrt{2} \cdot S)^2}}
\]

<|ref|>equation<|/ref|><|det|>[[120, 713, 330, 732]]<|/det|>
\[
\approx 2.65 \cdot 10^3 \text{ m} = 2.65 \text{ km}.
\]

<|ref|>sub_title<|/ref|><|det|>[[115, 749, 404, 767]]<|/det|>
3. Abstand Punkt von Gerade 

<|ref|>text<|/ref|><|det|>[[115, 768, 861, 829]]<|/det|>
Von einer Geraden ist der Punkt (4;2;3) und der Richtungsvektor \(\vec{a} = \begin{pmatrix} 2 \\ 1 \\ 3 \end{pmatrix}\) gegeben.
Berechnen Sie den Abstand des Punktes (4;1;1) von dieser Geraden.