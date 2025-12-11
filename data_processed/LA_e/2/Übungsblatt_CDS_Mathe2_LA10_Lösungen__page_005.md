<|ref|>text<|/ref|><|det|>[[115, 83, 144, 100]]<|/det|>
c) 

<|ref|>text<|/ref|><|det|>[[115, 97, 707, 117]]<|/det|>
Wir erhalten mit einem entsprechenden Ansatz die Umformungen 

<|ref|>equation<|/ref|><|det|>[[254, 133, 736, 157]]<|/det|>
\[ \lambda(\mathbf{v}, \mathbf{v}) = \langle \lambda \mathbf{v}, \mathbf{v} \rangle = \langle A \mathbf{v}, \mathbf{v} \rangle = \langle B^T B \mathbf{v}, \mathbf{v} \rangle = \langle B \mathbf{v}, B \mathbf{v} \rangle \geq 0. \]

<|ref|>text<|/ref|><|det|>[[118, 177, 330, 196]]<|/det|>
Daraus resultiert \(\lambda \geq 0\). 

<|ref|>text<|/ref|><|det|>[[118, 196, 465, 216]]<|/det|>
Als konkretes Zahlenbeispiel haben wir 

<|ref|>equation<|/ref|><|det|>[[286, 232, 728, 292]]<|/det|>
\[ A = B^T B = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix} = \begin{pmatrix} 6 & 4 \\ 4 & 5 \end{pmatrix}. \]

<|ref|>text<|/ref|><|det|>[[118, 308, 503, 327]]<|/det|>
Das charakteristische Polynom von \(A\) lautet 

<|ref|>equation<|/ref|><|det|>[[412, 342, 600, 363]]<|/det|>
\[ P(\lambda) = \lambda^2 - 11\lambda + 14. \]

<|ref|>text<|/ref|><|det|>[[118, 380, 627, 400]]<|/det|>
Daraus ergeben sich wie erwartet die positiven Eigenwerte 

<|ref|>equation<|/ref|><|det|>[[399, 412, 614, 450]]<|/det|>
\[ \lambda_{1,2} = \frac{1}{2} \left( 11 \pm \sqrt{65} \right) > 0. \]

<|ref|>sub_title<|/ref|><|det|>[[115, 465, 315, 483]]<|/det|>
## 5. Diagonalmatrizen 

<|ref|>text<|/ref|><|det|>[[115, 481, 475, 499]]<|/det|>
Gegeben seien die folgenden Matrizen: 

<|ref|>equation<|/ref|><|det|>[[115, 496, 603, 545]]<|/det|>
\[ A_1 = \begin{pmatrix} 1 & 5 & 7 \\ 0 & 4 & 3 \\ 0 & 0 & 1 \end{pmatrix}, A_2 = \begin{pmatrix} 1 & 0 & -1 \\ 1 & 2 & 1 \\ 2 & 2 & 3 \end{pmatrix}, A_3 = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 0 & 0 & 1 \end{pmatrix}. \]

<|ref|>text<|/ref|><|det|>[[115, 543, 869, 562]]<|/det|>
a) Bestimmen Sie die Eigenvektoren und zugehörigen Eigenräume obiger Matrizen. 

<|ref|>text<|/ref|><|det|>[[115, 560, 680, 579]]<|/det|>
b) Welche der Matrizen sind ähnlich zu einer Diagonalmatrix? 

<|ref|>text<|/ref|><|det|>[[115, 595, 144, 611]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[115, 610, 865, 650]]<|/det|>
Die Matrix \(A_1\) ist eine Dreiecksmatrix, damit stehen die Eigenwerte auf der Hauptdiagonalen. Wir haben den doppelten Eigenwert \(\lambda_{1,2} = 1\) und \(\lambda_3 = 4\). 

<|ref|>text<|/ref|><|det|>[[115, 650, 864, 690]]<|/det|>
Der zu \(\lambda_{1,2} = 1\) gehörige Eigenraum ist \(\text{Kern } (A_1 - \lambda_{1,2}E)\). Es gilt also wieder das homogene Gleichungssystem mit der Koeffizientenmatrix 

<|ref|>equation<|/ref|><|det|>[[362, 707, 625, 767]]<|/det|>
\[ (A_1 - \lambda_{1,2}E) = \begin{pmatrix} 0 & 5 & 7 \\ 0 & 3 & 3 \\ 0 & 0 & 0 \end{pmatrix} \]

<|ref|>text<|/ref|><|det|>[[118, 768, 870, 809]]<|/det|>
zu lösen. Gauss-Schritte sind nicht nötig. Die 1. Variable ist frei wählbar, also lautet der Lösungs- bzw. der Eigenraum von \(\lambda_{1,2} = 1\) 

<|ref|>equation<|/ref|><|det|>[[392, 824, 600, 883]]<|/det|>
\[ \mathbb{L}_{1,2} = \text{Span} \left\{ \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \right\}. \]