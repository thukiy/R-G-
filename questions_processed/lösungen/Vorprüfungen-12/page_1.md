<|ref|>sub_title<|/ref|><|det|>[[20, 8, 620, 44]]<|/det|>
4) Hotel : 135 Betten, 75 Zimmer 

<|ref|>equation<|/ref|><|det|>[[77, 49, 500, 117]]<|/det|>
\[
\begin{align*}
x & \dots \text{ Anzahl } \text{Cinzelzimmer} \\
y & \dots \text{ Doppel-} \\
z & \dots \text{ Dreier-}
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[75, 144, 950, 216]]<|/det|>
\[
\begin{align*}
x + y + z &= 75 \quad \begin{cases} 1 & 1 & 1 \\ 1 & 2 & 3 \end{cases} \quad \begin{cases} 75 \cdot (-1) & 1 & 1 & 1 & 75 \\ 0 & 1 & 2 & 60 \end{cases} \\
x + 2y + 3z &= 135 \quad \begin{cases} 1 & 2 & 3 \end{cases} \quad \begin{cases} 135 & 2 \end{cases} \\
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[75, 240, 785, 270]]<|/det|>
\[
\rightarrow 2. zelle : y + 2z = 60 \Leftrightarrow y = 60 - 2z
\]

<|ref|>equation<|/ref|><|det|>[[125, 280, 810, 310]]<|/det|>
\[
1. zelle : x + y + z = 75 \Leftrightarrow x = 75 - y - z
\]

<|ref|>equation<|/ref|><|det|>[[595, 319, 920, 350]]<|/det|>
\[
x = 75 - (60 - 2z) - z
\]

<|ref|>equation<|/ref|><|det|>[[595, 360, 768, 388]]<|/det|>
\[
x = 15 + z
\]

<|ref|>equation<|/ref|><|det|>[[87, 417, 603, 450]]<|/det|>
\[
z \geq 0 ; y \geq 0 ; 0 \leq z \leq 30
\]

<|ref|>equation<|/ref|><|det|>[[87, 473, 884, 510]]<|/det|>
\[
L = \{(15 + z ; 60 - 2z ; z) \mid z \in \mathbb{N}_0, 0 \leq z \leq 30\}
\]

<|ref|>equation<|/ref|><|det|>[[100, 536, 320, 571]]<|/det|>
\[
\begin{array}{c|c|c}
x & y & z \\
\hline
15 & 60 & 0 \\
16 & 58 & 1 \\
\vdots & \vdots & \vdots \\
45 & 0 & 30 \\
\end{array}
\]