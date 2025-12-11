<|ref|>sub_title<|/ref|><|det|>[[30, 15, 350, 45]]<|/det|>
Inhomogene Gleichung 

<|ref|>text<|/ref|><|det|>[[60, 55, 870, 84]]<|/det|>
generell : AWP wird in homogenes und inhomogenes AWP aufgeteilt 

<|ref|>text<|/ref|><|det|>[[60, 110, 500, 179]]<|/det|>
homogenes AWP : \(y' n = m(x) \cdot y_n\)
\(y_n(x_0) = y_0\) 

<|ref|>text<|/ref|><|det|>[[60, 205, 607, 264]]<|/det|>
inhomogenes AWP : \(y' p = m(x) \cdot y_p + q(x)\)
partikulares
\(y_p(x_0) = 0\) 

<|ref|>text<|/ref|><|det|>[[60, 302, 911, 371]]<|/det|>
seien \(y_n\) und \(y_p\) dösungen einer homogenen bzw. inhomogenen DGL mit AB, dann ist die allg. dösung gegeben durch \(y(x) = y_n(x) + y_p(x)\) 

<|ref|>text<|/ref|><|det|>[[60, 400, 715, 429]]<|/det|>
→ \(y_n\) erhalten wir mit Methode Trennung der Variablen 

<|ref|>text<|/ref|><|det|>[[130, 437, 700, 465]]<|/det|>
↔ wenn \(y_n\) lag die DGL ist, dann auch \(C \cdot y_n\) 

<|ref|>text<|/ref|><|det|>[[60, 474, 936, 504]]<|/det|>
→ für partikuläre dösung werden wir "Variation der Konstanten" an : 

<|ref|>text<|/ref|><|det|>[[100, 513, 664, 540]]<|/det|>
C sei nun von x abhängige Funktion → C(x) 

<|ref|>sub_title<|/ref|><|det|>[[30, 570, 530, 599]]<|/det|>
Bestimmung der partikulären dösung : 

<|ref|>text<|/ref|><|det|>[[60, 604, 404, 636]]<|/det|>
Ansalta : \(y(x) = C(x) \cdot e^{M(x)}\) 

<|ref|>text<|/ref|><|det|>[[60, 666, 430, 692]]<|/det|>
in inhomogene DGL einsetzen : 

<|ref|>equation<|/ref|><|det|>[[90, 696, 790, 844]]<|/det|>
\[
\begin{align*}
C'(x) \cdot e^{M(x)} + C(x) \cdot e^{M(x)} &= m(x) \cdot C(x) \cdot e^{M(x)} + q(x) \\
C'(x) \cdot e^{M(x)} &= q(x) \\
C'(x) &= q(x) \cdot e^{-M(x)} \\
C(x) &= \int (q(x) \cdot e^{-M(x)}) \, dx
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[80, 875, 640, 902]]<|/det|>
→ allgemeine dösung der inhomogenen DGL : 

<|ref|>equation<|/ref|><|det|>[[130, 905, 800, 941]]<|/det|>
\[
y_{\text{allg}} = y_n + y_p = C \cdot e^{M(x)} + C(x) \cdot e^{M(x)} = (C + C(x)) e^{M(x)}
\]