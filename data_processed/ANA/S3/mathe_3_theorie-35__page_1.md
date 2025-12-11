<|ref|>text<|/ref|><|det|>[[30, 55, 716, 82]]<|/det|>
wenn DGL autonom ist: autonome Verschiebung möglich 

<|ref|>text<|/ref|><|det|>[[30, 92, 490, 121]]<|/det|>
alleg. dag.: \(y(x) = C_1^* y_1(x) + C_2^* y_2(x)\) 

<|ref|>text<|/ref|><|det|>[[30, 130, 480, 159]]<|/det|>
neu: \(y(x) = C_1 y_1(x-x_0) + C_2 y_2(x-x_0)\) 

<|ref|>text<|/ref|><|det|>[[30, 189, 230, 214]]<|/det|>
1. Falle: \(D > 0\) 

<|ref|>equation<|/ref|><|det|>[[163, 216, 550, 250]]<|/det|>
\[y(x) = C_1 e^{\lambda_1(x-x_0)} + C_2 e^{\lambda_2(x-x_0)}\]

<|ref|>equation<|/ref|><|det|>[[163, 255, 595, 288]]<|/det|>
\[y'(x) = C_1 \lambda_1 e^{\lambda_1(x-x_0)} + C_2 \lambda_2 e^{\lambda_2(x-x_0)}\]

<|ref|>text<|/ref|><|det|>[[163, 302, 540, 328]]<|/det|>
Eingeben der AB: \(y(x_0) = y_0\) 

<|ref|>equation<|/ref|><|det|>[[421, 343, 545, 366]]<|/det|>
\[y'(x_0) = y_0\]

<|ref|>equation<|/ref|><|det|>[[163, 378, 343, 404]]<|/det|>
\[y(x_0) = C_1 + C_2\]

<|ref|>equation<|/ref|><|det|>[[421, 390, 616, 430]]<|/det|>
\[\begin{cases} \text{LGS für } C_1 \& C_2 \end{cases}\]

<|ref|>equation<|/ref|><|det|>[[163, 416, 410, 441]]<|/det|>
\[y'(x_0) = C_1 \lambda_1 + C_2 \lambda_2\]

<|ref|>equation<|/ref|><|det|>[[163, 470, 400, 530]]<|/det|>
\[\begin{array}{c|c|c|c}
1 & 1 & y_0 & 1 \cdot (-\lambda_1) \\
\hline
\lambda_1 & \lambda_2 & y_0 & 0 \\
\end{array}\]

<|ref|>equation<|/ref|><|det|>[[421, 470, 470, 530]]<|/det|>
\[\begin{array}{c|c|c|c}
1 & 1 \\
\hline
\lambda_1 & \lambda_2 & y_0 & 0
\end{array}\]

<|ref|>equation<|/ref|><|det|>[[163, 540, 325, 570]]<|/det|>
\[\rightarrow C_2 = \frac{y_0 - \lambda_1 y_0}{\lambda_2 - \lambda_1}\]

<|ref|>equation<|/ref|><|det|>[[421, 540, 470, 570]]<|/det|>
\[\begin{array}{c|c|c|c}
1 & 1 \\
\hline \lambda_1 & \lambda_2 & y_0 & 0
\end{array}\]

<|ref|>text<|/ref|><|det|>[[163, 580, 325, 610]]<|/det|>
\[\rightarrow C_1 = y_0 - C_2 = \frac{y_0 (\lambda_2 - \lambda_1) - y_0 + \lambda_1 y_0}{\lambda_2 - \lambda_1} = \frac{\lambda_2 y_0 - y_0}{\lambda_2 - \lambda_1}\]

<|ref|>text<|/ref|><|det|>[[30, 644, 230, 670]]<|/det|>
2. Falle: \(D = 0\) 

<|ref|>equation<|/ref|><|det|>[[163, 675, 511, 708]]<|/det|>
\[y(x) = [C_1 + C_2(x-x_0)] \cdot e^{\lambda(x-x_0)}\]

<|ref|>equation<|/ref|><|det|>[[163, 711, 730, 747]]<|/det|>
\[y'(x) = C_2 \cdot e^{\lambda(x-x_0)} + [C_1 + C_2(x-x_0)] \cdot \lambda \cdot e^{\lambda(x-x_0)}\]

<|ref|>equation<|/ref|><|det|>[[163, 760, 365, 789]]<|/det|>
\[y(x_0) = C_1 = y_0\]

<|ref|>equation<|/ref|><|det|>[[163, 796, 475, 826]]<|/det|>
\[y'(x_0) = C_2 + C_1 \cdot \lambda = y_0\]

<|ref|>equation<|/ref|><|det|>[[271, 833, 603, 863]]<|/det|>
\[C_2 = y_0 - C_1 \cdot \lambda = y_0 - y_0 \cdot \lambda\]