<|ref|>equation<|/ref|><|det|>[[118, 84, 800, 255]]<|/det|>
\[
\begin{align*}
R_{\beta} \cdot R_{\alpha} &= \begin{bmatrix} \cos(\beta) & -\sin(\beta) \\ \sin(\beta) & \cos(\beta) \end{bmatrix} \cdot \begin{bmatrix} \cos(\alpha) & -\sin(\alpha) \\ \sin(\alpha) & \cos(\alpha) \end{bmatrix} \\
&= \begin{bmatrix} \cos(\beta) \cos(\alpha) + (-\sin(\beta)) \sin(\alpha) & \cos(\beta)(-\sin(\alpha)) + (-\sin(\beta)) \cos(\alpha) \\ \sin(\beta) \cos(\alpha) + \cos(\beta) \sin(\alpha) & \sin(\beta)(-\sin(\alpha)) + \cos(\beta) \cos(\alpha) \end{bmatrix} \\
&= \begin{bmatrix} \cos(\beta)\cos(\alpha) - \sin(\beta)\sin(\alpha) & -\cos(\beta)\sin(\alpha) - \sin(\beta)\cos(\alpha) \\ \sin(\beta)\cos(\alpha) + \cos(\beta)\sin(\alpha) & \cos(\beta)\cos(\alpha) - \sin(\beta)\sin(\alpha) \end{bmatrix} \\
&= \begin{bmatrix} \cos(\beta + \alpha) & -\sin(\beta + \alpha) \\ \sin(\beta + \alpha) & \cos(\beta + \alpha) \end{bmatrix} = R_{\beta + \alpha} = R_{\alpha + \beta} = R_{\alpha} \cdot R_{\beta}.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 258, 144, 274]]<|/det|>
e) 

<|ref|>equation<|/ref|><|det|>[[118, 275, 470, 312]]<|/det|>
\[
R_0 = \begin{bmatrix} \cos(0) & -\sin(0) \\ \sin(0) & \cos(0) \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \underline{\underline{1}}.
\]

<|ref|>equation<|/ref|><|det|>[[118, 315, 794, 400]]<|/det|>
\[
\begin{align*}
R_{\pm\pi/6} &= \begin{bmatrix} \cos(\pm\pi/6) & -\sin(\pm\pi/6) \\ \sin(\pm\pi/6) & \cos(\pm\pi/6) \end{bmatrix} = \begin{bmatrix} \cos(\pi/6) & \mp\sin(\pi/6) \\ \pm\sin(\pi/6) & \cos(\pi/6) \end{bmatrix} = \begin{bmatrix} \frac{\sqrt{3}}{2} & \mp\frac{1}{2} \\ \pm\frac{1}{2} & \frac{\sqrt{3}}{2} \end{bmatrix} \\
&= \frac{1}{2} \cdot \begin{bmatrix} \sqrt{3} & \mp 1 \\ \pm 1 & \sqrt{3} \end{bmatrix}.
\end{align*}
\]

<|ref|>equation<|/ref|><|det|>[[115, 408, 816, 491]]<|/det|>
\[
R_{\pm\pi/4} = \begin{bmatrix} \cos(\pm\pi/4) & -\sin(\pm\pi/4) \\ \sin(\pm\pi/4) & \cos(\pm\pi/4) \end{bmatrix} = \begin{bmatrix} \cos(\pi/4) & \mp\sin(\pi/4) \\ \pm\sin(\pi/4) & \cos(\pi/4) \end{bmatrix} = \begin{bmatrix} \frac{1}{\sqrt{2}} & \mp\frac{1}{\sqrt{2}} \\ \pm\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{bmatrix} \\
&= \frac{1}{\sqrt{2}} \cdot \begin{bmatrix} 1 & \mp 1 \\ \pm 1 & 1 \end{bmatrix}.
\]

<|ref|>equation<|/ref|><|det|>[[115, 504, 816, 587]]<|/det|>
\[
R_{\pm\pi/3} = \begin{bmatrix} \cos(\pm\pi/3) & -\sin(\pm\pi/3) \\ \sin(\pm\pi/3) & \cos(\pm\pi/3) \end{bmatrix} = \begin{bmatrix} \cos(\pi/3) & \mp\sin(\pi/3) \\ \pm\sin(\pi/3) & \cos(\pi/3) \end{bmatrix} = \begin{bmatrix} \frac{1}{2} & \mp\frac{\sqrt{3}}{2} \\ \pm\frac{\sqrt{3}}{2} & \frac{1}{2} \end{bmatrix} \\
&= \frac{1}{2} \cdot \begin{smallmatrix} 1 & \mp\sqrt{3} \\ \pm\sqrt{3} & 1 \end{smallmatrix}.
\]

<|ref|>equation<|/ref|><|det|>[[115, 600, 784, 684]]<|/det|>
\[
R_{\pm\pi/2} = \begin{bmatrix} \cos(\pm\pi/2) & -\sin(\pm\pi/2) \\ \sin(\pm\pi/2) & \cos(\pm\pi/2) \end{bmatrix} = \begin{bmatrix} \cos(\pi/2) & \mp\sin(\pi/2) \\ \pm\sin(\pi/2) & \cos(\pi/2) \end{bmatrix} = \begin{bmatrix} 0 & \mp 1 \\ \pm 1 & 0 \end{bmatrix} \\
&= \pm \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} = \pm\underline{\underline{1}}.
\]

<|ref|>equation<|/ref|><|det|>[[115, 690, 820, 755]]<|/det|>
\[
R_{\pm\pi} = \begin{bmatrix} \cos(\pm\pi) & -\sin(\pm\pi) \\ \sin(\pm\pi) & \cos(\pm\pi) \end{bmatrix} = \begin{bmatrix} \cos(\pi) & \mp\sin(\pi) \\ \pm\sin(\pi) & \cos(\pi) \end{bmatrix} = \begin{bmatrix} -1 & \mp 0 \\ \pm 0 & -1 \end{bmatrix} = \begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix} \\
&= -\underline{1} = P.
\]