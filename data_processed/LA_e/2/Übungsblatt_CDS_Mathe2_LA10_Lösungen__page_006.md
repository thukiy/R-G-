<|ref|>text<|/ref|><|det|>[[119, 83, 330, 105]]<|/det|>
Damit gilt \(\dim \mathbb{L}_{1,2} = 1\). 

<|ref|>text<|/ref|><|det|>[[119, 105, 214, 122]]<|/det|>
Weiter ist 

<|ref|>equation<|/ref|><|det|>[[357, 134, 636, 196]]<|/det|>
\[ (A_1 - \lambda_3 E) = \begin{pmatrix} -3 & 5 & 7 \\ 0 & 0 & 3 \\ 0 & 0 & -3 \end{pmatrix} \]

<|ref|>text<|/ref|><|det|>[[119, 210, 395, 230]]<|/det|>
zu lösen. Hier liegt die Lösung 

<|ref|>equation<|/ref|><|det|>[[400, 244, 590, 306]]<|/det|>
\[ \mathbb{L}_3 = \operatorname{Span} \left\{ \begin{pmatrix} 5 \\ 3 \\ 0 \end{pmatrix} \right\} \]

<|ref|>text<|/ref|><|det|>[[119, 320, 872, 360]]<|/det|>
vor, also stimmt die algebraische Vielfachheit mit der geometrischen überein. Es gilt \(\dim \mathbb{L}_3 = 1\). 

<|ref|>text<|/ref|><|det|>[[119, 357, 500, 376]]<|/det|>
Das charakteristische Polynom zu \(A_2\) lautet 

<|ref|>equation<|/ref|><|det|>[[191, 388, 792, 450]]<|/det|>
\[ \det(A_2 - \lambda E) = \begin{vmatrix} 1 - \lambda & 0 & -1 \\ 1 & 2 - \lambda & 1 \\ 2 & 2 & 3 - \lambda \end{vmatrix} = (1 - \lambda)(2 - \lambda)(3 - \lambda) \stackrel{!}{=} 0. \]

<|ref|>text<|/ref|><|det|>[[119, 465, 606, 484]]<|/det|>
Die einfachen Eigenwerte sind \(\lambda_1 = 1\), \(\lambda_2 = 2\) und \(\lambda_3 = 3\). 

<|ref|>text<|/ref|><|det|>[[119, 485, 866, 525]]<|/det|>
Die Koeffizientenmatrizen der zugehörigen homogenen Gleichungssysteme \((A_2 - \lambda_i E)x = 0\), \(i = 1, 2, 3\), liefern folgende Eigenräume: 

<|ref|>equation<|/ref|><|det|>[[273, 538, 710, 600]]<|/det|>
\[ \begin{pmatrix} 0 & 0 & -1 \\ 1 & 1 & 1 \\ 2 & 2 & 2 \end{pmatrix} \implies \mathbb{L}_1 = \operatorname{Span} \left\{ \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix} \right\}, \]

<|ref|>equation<|/ref|><|det|>[[273, 630, 707, 692]]<|/det|>
\[ \begin{pmatrix} -1 & 0 & -1 \\ 1 & 0 & 1 \\ 2 & 2 & 1 \end{pmatrix} \implies \mathbb{L}_2 = \operatorname{Span} \left\{ \begin{pmatrix} 2 \\ -1 \\ -2 \end{pmatrix} \right\}, \]

<|ref|>equation<|/ref|><|det|>[[273, 722, 704, 785]]<|/det|>
\[ \begin{pmatrix} -2 & 0 & -1 \\ 1 & -1 & 1 \\ 2 & 2 & 0 \end{pmatrix} \implies \mathbb{L}_3 = \operatorname{Span} \left\{ \begin{pmatrix} 1 \\ -1 \\ -2 \end{pmatrix} \right\}. \]

<|ref|>text<|/ref|><|det|>[[119, 785, 864, 824]]<|/det|>
Damit stimmen algebraische und geometrische Vielfachheiten überein, und es gilt \(\mathbb{L}_i = 1\) für \(i = 1, 2, 3\). 

<|ref|>text<|/ref|><|det|>[[119, 825, 500, 845]]<|/det|>
Das charakteristische Polynom zu \(A_3\) lautet 

<|ref|>equation<|/ref|><|det|>[[187, 860, 792, 922]]<|/det|>
\[ \begin{vmatrix} 2 - \lambda & 1 & 1 \\ 1 & 2 - \lambda & 1 \\ 0 & 0 & 1 - \lambda \end{vmatrix} = (1 - \lambda) \left[ (2 - \lambda)^2 - 1 \right] = (1 - \lambda)^2 (3 - \lambda) \stackrel{!}{=} 0. \]