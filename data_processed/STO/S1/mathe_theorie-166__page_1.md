<|ref|>sub_title<|/ref|><|det|>[[16, 12, 580, 120]]<|/det|>
Zusammenfassung:
Sätze der Wahrscheinlichkeit 

<|ref|>sub_title<|/ref|><|det|>[[21, 145, 275, 175]]<|/det|>
Additionssatz : 

<|ref|>equation<|/ref|><|det|>[[44, 186, 730, 294]]<|/det|>
\[
\begin{align*}
P(A \cup B) &= P(A) + P(B) - P(A \cap B) \\
\text{wenn } A \text{ und } B \text{ disjunkt sind, } d.h. } A \cap B = \emptyset, \\
\text{dann gilt: } P(A \cup B) = P(A) + P(B)
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[21, 321, 320, 351]]<|/det|>
Multiplikationssatz : 

<|ref|>equation<|/ref|><|det|>[[44, 362, 696, 555]]<|/det|>
\[
\begin{align*}
P(A \cap B) &= P(A) \cdot P(B|A) \\
&= P(B) \cdot P(A|B) \\
\text{für unabhängige Ereignisse } A \text{ und } B, \text{ d.h.} \\
P(A|B) &= P(A) \quad \text{und} \quad P(B|A) = P(B) \\
P(A \cap B) &= P(A) \cdot P(B)
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[21, 575, 415, 604]]<|/det|>
Totale Wahrscheinlichkeit : 

<|ref|>equation<|/ref|><|det|>[[44, 614, 812, 688]]<|/det|>
\[
\begin{align*}
P(B) &= \sum_i P(A_i) \cdot P(B|A_i) \\
\Omega &= A_1 \cup A_2 \cup \ldots \cup A_n, \quad A_i : \text{paarweise disjunkt}
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[21, 714, 270, 743]]<|/det|>
Satz von Beyes : 

<|ref|>equation<|/ref|><|det|>[[44, 753, 336, 794]]<|/det|>
\[
P(A_i|B) = \frac{P(A_i) \cdot P(B|A_i)}{P(B)}
\]