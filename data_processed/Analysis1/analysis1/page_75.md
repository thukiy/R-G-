# Kurvendiskussion 

Man sammelt Informationen über den Verlauf einer Funktion, um sie skizzieren zu können.

- Ableitung enthält Informationen, in welchen Bereichen die Funktion steigt bzw. fällt, wo Extremwerte wie Maxima und Minima vorliegen.
- Ableitung beschreibt das Krümmungsverhalten der Funktion, wo eventuelle Wendepunkte vorliegen.

Typischerweise werden folgende Schritte bei der Kurvendiskussion durchgeführt:

- Nullstellen bestimmen
- Ordinatenabschnitt (y-Achsenabschnitt) bestimmen
- Extremwerte bestimmen
- Krümmungsverhalten und Wendepunkte
- Verhalten der Funktion an den Rändern des Definitionsbereichs, um festzustellen, an welchen Stellen globale Maxima bzw. Minima vorliegen
- Skizze
nützlich: eventuelle Symmetrie der Funktion bestimmen, indem $f(-x)$ gebildet wird

Bsp: $\quad f(x)=\left(x^{2}-x\right) \cdot e^{-x}, \quad f: R \rightarrow R$
Exkemsstellen und Wendestellen bestimmen

$$
\begin{aligned}
f^{\prime}(x) & =(2 x-1) \cdot e^{-x}+\left(x^{2}-x\right) \cdot\left(-e^{-x}\right) \\
& =e^{-x}\left(2 x-1-x^{2}+x\right) \\
& =e^{-x}\left(-x^{2}+3 x-1\right) \\
f^{\prime \prime}(x) & =-e^{-x}\left(-x^{2}+3 x-1\right)+e^{-x}(-2 x+3) \\
& =e^{-x}\left(x^{2}-3 x+1-2 x+3\right) \\
& =e^{-x}\left(x^{2}-5 x+4\right) \\
f^{\prime \prime \prime}(x) & =-e^{-x}\left(x^{2}-5 x+4\right)+e^{-x}(2 x-5) \\
& =e^{-x}\left(-x^{2}+5 x-4+2 x-5\right) \\
& =e^{-x}\left(-x^{2}+7 x-9\right)
\end{aligned}
$$