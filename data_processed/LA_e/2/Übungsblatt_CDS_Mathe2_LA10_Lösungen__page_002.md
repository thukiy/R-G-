<|ref|>text<|/ref|><|det|>[[117, 83, 415, 102]]<|/det|>
Demnach ist A regulär und es gilt 

<|ref|>equation<|/ref|><|det|>[[344, 112, 650, 138]]<|/det|>
\[ \ker(A) = \{0\} \quad \text{und} \quad \operatorname{img}(A) = \mathbb{R}^2. \]

<|ref|>text<|/ref|><|det|>[[114, 139, 145, 157]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[114, 155, 877, 191]]<|/det|>
Wir erzeugen mit dem Gauß-Jordan-Verfahren reduzierte Stufenform (aus A ergeben sich die Vektoren im Kern, aus Aᵀ das Bild von A): 

<|ref|>equation<|/ref|><|det|>[[117, 188, 519, 277]]<|/det|>
\[ A: \begin{bmatrix} 2 & 3 \\ 4 & 6 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 2 & 3 \\ 1 & 2 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 2 & 3 \\ 0 & 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & 2 \\ 0 & 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 \\ 1 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 0 & 0 \end{bmatrix} \\ A^T: \begin{bmatrix} 2 & 4 \\ 3 & 6 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & 2 \\ 1 & 2 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & 2 \\ 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & 2 \\ \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 0 \end{bmatrix} \Leftrightarrow 1 \cdot x + \frac{3}{2} \cdot y = 0 \Rightarrow x = -\frac{3}{2} \cdot y \]

<|ref|>equation<|/ref|><|det|>[[117, 280, 697, 320]]<|/det|>
\[ \ker(A) = \left\{ \begin{bmatrix} -\frac{3}{2} y \\ y \end{bmatrix} \in \mathbb{R}^2 \right\} = \operatorname{span} \left\{ \begin{bmatrix} -\frac{3}{2} \\ 1 \end{bmatrix} \right\} = \operatorname{span} \left\{ \begin{bmatrix} 3 \\ -2 \end{bmatrix} \right\} \]

<|ref|>text<|/ref|><|det|>[[114, 386, 385, 405]]<|/det|>
Für das Bild von A ergibt sich 

<|ref|>equation<|/ref|><|det|>[[117, 406, 339, 450]]<|/det|>
\[ \operatorname{img}(A) = \operatorname{span} \left\{ \begin{bmatrix} 1 \\ 2 \end{bmatrix} \right\} \]

<|ref|>text<|/ref|><|det|>[[114, 455, 145, 472]]<|/det|>
c) 

<|ref|>equation<|/ref|><|det|>[[114, 472, 856, 580]]<|/det|>
\[ A: \begin{bmatrix} 0 & -3 & 2 \\ 3 & 0 & -1 \\ -2 & 1 & 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & -\frac{1}{2} & 0 \\ 0 & 3 & -2 \\ 3 & 0 & -1 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & -\frac{1}{3} & 0 \\ 0 & 3 & -2 \\ 0 & \frac{3}{2} & -1 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & -\frac {1}{2} & 0 \\ 0 & 1 & -\frac{2}{3} \\ 3 & 0 & 3 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & -\frac{1}{6} & 0 \\ 0 & 1 & -\frac{2}{3} \\ \frac{3}{2} & -1 & 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 & -\left(\frac{1}{6}\right) & 0 \\ 0 & 1 & -\frac{2}{3} \\ \left(\frac{3}{2}\right) & -1 & 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 \\ 0 \\ \frac{1}{3} \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 \\ 0 \\ 0 \\ 0 \end{bmatrix} \Leftrightarrow \begin{bmatrix} 1 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} \Leftrightarrow 1 \cdot x + 0 \cdot y = 0 \Rightarrow x = 0 \Rightarrow y = 0 \]

<|ref|>text<|/ref|><|det|>[[114, 621, 435, 640]]<|/det|>
Für die Vektoren im Kern von A gilt 

<|ref|>equation<|/ref|><|det|>[[117, 642, 450, 682]]<|/det|>
\[ 0 \cdot x + 1 \cdot y - \frac{2}{3} \cdot z = 0 \Rightarrow y = \frac{2}{3} \cdot z \]

<|ref|>equation<|/ref|><|det|>[[117, 682, 450, 722]]<|/det|>
\[ 1 \cdot x + 0 \cdot y - \frac{1}{3} \cdot z = 0 \Rightarrow x = \frac{1}{3} \cdot z \]

<|ref|>equation<|/ref|><|det|>[[114, 716, 675, 780]]<|/det|>
\[ \ker(A) = \left\{ \begin{bmatrix} \frac{1}{3} z \\ \frac{2}{3} z \\ z \end{bmatrix} \in \mathbb{R}^3 \right\} = \operatorname{span} \left\{ \begin{bmatrix} \frac{1}{3} \\ \frac{2}{3} \\ 1 \end{bmatrix} \right\} = \operatorname{span} \left[ \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} \right] \]

<|ref|>text<|/ref|><|det|>[[114, 783, 385, 801]]<|/det|>
Für das Bild von A ergibt sich 

<|ref|>equation<|/ref|><|det|>[[114, 800, 695, 865]]<|/det|>
\[ \operatorname{img}(A) = \operatorname{span} \left\{
\begin{bmatrix} 1 \\ 0 \\ -\frac{1}{3} \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \\ -\frac{2}{3} \end{bmatrix}
\right\} = \operatorname{span} \left\{
\begin{bmatrix} 3 \\ 0 \\ -1 \end{bmatrix}, \begin{bmatrix} 0 \\ 3 \\ -2 \end{bmatrix}
\right\} \]