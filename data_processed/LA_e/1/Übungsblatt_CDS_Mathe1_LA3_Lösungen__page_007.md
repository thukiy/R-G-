<|ref|>text<|/ref|><|det|>[[120, 82, 637, 100]]<|/det|>
Variante 2: Wir wenden das GAUSS-JORDAN-Verfahren an. Es gilt 

<|ref|>equation<|/ref|><|det|>[[144, 107, 630, 164]]<|/det|>
\[ \begin{bmatrix} 2 & -3 & 1 & 3 \\ -1 & 3 & -2 & 0 \\ 3 & -1 & 5 & 1 \end{bmatrix} \Leftrightarrow \begin{bmatrix} -1 & 3 & -2 & 0 \\ 2 & -3 & 1 & 3 \\ 3 & -1 & 5 & 1 \end{bmatrix} \Leftrightarrow 2 \begin{bmatrix} 1 & -3 & 2 & 0 \\ 2 & -3 & 1 & 3 \\ 3 \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[144, 172, 682, 230]]<|/det|>
\[ \begin{bmatrix} 1 & -3 & 2 & 0 \\ 0 & 3 & -3 & 3 \\ 0 & 8 & -1 & 1 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & -3 & 2 & 0 \\ 0 & [1] & -1 & 1 \\ 8 & 0 & 8 & -1 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & -3 & 3 & 0 \\ 0 & [1] & -1 & 1 \\ 0 & 0 & 7 & -7 \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[144, 239, 744, 299]]<|/det|>
\[ \begin{bmatrix} 2 & [1] & -3 & 2 & 0 \\ -1 & 0 & [1] & -1 & 1 \\ 0 & 0 & [1] & -1 & 1 \end{bmatrix} \Leftrightarrow \begin{bmatrix} -3 & [1] & -3 & 0 & 2 \\ 0 & [1] & 0 & 0 & 0 \\ 0 & 0 & [1] & -1 & 1 \end{bmatrix}\Leftrightarrow \begin{bmatrix} 1 & 0 & 0 & 2 \\ 0 & [1] & 0 & 0 \\ 0 & 0 & [1] & -1 \end{bmatrix}. \]

<|ref|>text<|/ref|><|det|>[[124, 308, 460, 324]]<|/det|>
Die Lösungsmenge des LGLS ist demnach 

<|ref|>equation<|/ref|><|det|>[[397, 336, 551, 358]]<|/det|>
\[ \mathbb{L} = \{(2; 0; -1)\}. \]

<|ref|>text<|/ref|><|det|>[[114, 365, 144, 381]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[120, 380, 539, 395]]<|/det|>
Variante 1: Wir wenden das GAUSS-Verfahren an. Es gilt 

<|ref|>equation<|/ref|><|det|>[[144, 404, 688, 520]]<|/det|>
\[ \begin{bmatrix} 2 & -6 & 1 & 0 \\ 3 & 6 & 3 & -2 \\ 1 & 2 & 3 & -3 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 2 & -6 & 1 & 0 \\ 0 & [21] & -5 & 2 \\ \frac{3}{7} & 0 & 9 & -4 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 2 & -6 & 1 \\ 0 & [21] & -5 \\ 0 & 0 & -\frac{13}{7} \end{bmatrix} \]

<|ref|>text<|/ref|><|det|>[[140, 530, 410, 546]]<|/det|>
Durch Rückwärtseinsetzen finden wir 

<|ref|>equation<|/ref|><|det|>[[238, 555, 660, 632]]<|/det|>
\[ \begin{align*} z &= 1 \\ 21y - 5z &= 2 \Rightarrow y &= \frac{2+5z}{21} = \frac{2+5\cdot1}{21} = \frac{7}{21} = \frac{1}{3} \\ 2x - 6y + z &= 0 \Rightarrow x &= \frac{6y - z}{2} = \frac{6\cdot\frac{1}{3} - 1}{2} = \frac{2-1}{2} = \frac{1}{2}. \end{align*} \]

<|ref|>text<|/ref|><|det|>[[120, 635, 640, 651]]<|/det|>
Variante 2: Wir wenden das GAUSS-JORDAN-Verfahrenan. Es gilt 

<|ref|>equation<|/ref|><|det|>[[144, 661, 744, 728]]<|/det|>
\[ \begin{bmatrix} 2 & -6 & 1 & 0 & 0 \\ 3 & 6 & 3 & -2 & 2 \\ 1 & 2 & 3 & -3 & -1 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 2 & -6 & 1 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 2 & -6 & 0 & -1 \\ 0 & [21] & 0 & 7 \\ 0 & 0 & [1] & 1 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 2 & -6 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 2 & -6 & 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 2 & -6 & 0 \\ 0 & [3] & 0 & 1 \\ 0 & 0 & [1] & 1 \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[144, 735, 744, 792]]<|/det|>
\[ \begin{bmatrix} 1 & [2] & -6 & 1 & 0 \\ -5 & 0 & [21] & -5 & 2 \\ 0 & 0 & [1] & 1 \end{bmatrix} \Leftarrow \begin{bmatrix} 2 & -6 & 0 & -1 \\ 0 & 0 & [21] & 0 & 7 \\ 0 & 0 & 0 & [1] & 1 \end{bmatrix} \Leftarrow -2 \begin{bmatrix} 2 & -6 & 0 & -1 \\ 0 & \begin{bmatrix} 3 \end{bmatrix} & 0 & 1 \\ 0 & 0 & [1] & 1 \\ \end{bmatrix} \]

<|ref|>equation<|/ref|><|det|>[[144, 800, 476, 856]]<|/det|>
\[ \begin{bmatrix} 2 & 0 & 0 & 1 \\ 0 & [3] & 0 & 1 \\ 0 & 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & 0 & 0 & \frac{1}{2} \\ 0 & [1] & 0 & \frac{1}{3} \\ 0 & 0 & [1] & 1 \end{bmatrix}. \]

<|ref|>text<|/ref|><|det|>[[120, 871, 445, 887]]<|/det|>
Die Lösungsmenge des LGLS ist demnach 

<|ref|>equation<|/ref|><|det|>((1, 897, 528, 925]]<|/det|>
\[ \mathbb{L} = \{(\frac{1}{2}; \frac{1}{3}; 1)\}. \]