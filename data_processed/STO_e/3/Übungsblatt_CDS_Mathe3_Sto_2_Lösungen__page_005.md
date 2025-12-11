<|ref|>table<|/ref|><|det|>[[240, 99, 750, 225]]<|/det|>
<table><tr><td>Ereignis</td><td colspan="2">Wahrscheinlichkeit</td></tr><tr><td>Opa zu Hause</td><td>\(P(H)\)</td><td>0.15</td></tr><tr><td>Opa flirtet</td><td>\(P(M)\)</td><td>0.80</td></tr><tr><td>Opa sammelt Pilze</td><td>\(P(W)\)</td><td>0.05</td></tr><tr><td>Opa wird gefunden</td><td>\(P(G)\)</td><td>?</td></tr><tr><td>Anja findet Opa, falls er flirtet</td><td>\(P(G | M)\)</td><td>0.9</td></tr><tr><td>Dirk findet Opa, falls er Pilze sammelt</td><td>\(P(G | W)\)</td><td>0.5</td></tr></table>

<|ref|>text<|/ref|><|det|>[[115, 230, 144, 247]]<|/det|>
a) 

<|ref|>text<|/ref|><|det|>[[115, 247, 504, 263]]<|/det|>
Die Wahrscheinlichkeit, dass Anja den Opa findet, ist 

<|ref|>equation<|/ref|><|det|>[[223, 275, 470, 312]]<|/det|>
\[
\begin{align*}
P(G \cap M) &= P(G | M) \cdot P(M) \\
&= 0.9 \cdot 0.8 = 0.72
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 314, 144, 331]]<|/det|>
b) 

<|ref|>text<|/ref|><|det|>[[115, 333, 541, 349]]<|/det|>
Die Wahrscheinlichkeit, dass Dirk findet den Opa findet ist 

<|ref|>equation<|/ref|><|det|>[[223, 361, 470, 397]]<|/det|>
\[
\begin{align*}
P(G \cap W) &= P(G | W) \cdot P(W) \\
&= 0.5 \cdot 0.05 = 0.025
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 410, 572, 441]]<|/det|>
Die Wahrscheinlichkeit, dass eines der Kinder den Opa finden
wird, ist 

<|ref|>equation<|/ref|><|det|>[[215, 453, 475, 490]]<|/det|>
\[
\begin{align*}
P(G) &= P(G \cap M) + P(G \cap W) \\
&= 0.72 + 0.025 = 0.745.
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 490, 144, 507]]<|/det|>
c) 

<|ref|>text<|/ref|><|det|>[[115, 507, 572, 538]]<|/det|>
Die Wahrscheinlichkeit dafür, den Opa bei Rückkehr zuhause in
seinem Sessel sitzend anzutreffen, ist 

<|ref|>equation<|/ref|><|det|>[[152, 549, 540, 660]]<|/det|>
\[
\begin{align*}
P(H | G^C) &= \frac{P(H \cap G^C)}{P(G^C)} = \frac{P(G^C | H) \cdot P(H)}{P(G^C)} \\
&= \frac{1 \cdot P(H)}{P(G^C)} = \frac{P(H)}{1 - P(G)} \\
&= \frac{0.15}{0.255} = 0.588 \ 235
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[115, 675, 272, 692]]<|/det|>
8. Pünktlichkeit 

<|ref|>text<|/ref|><|det|>[[115, 692, 880, 841]]<|/det|>
Die Freunde Peter und Paul führen gemeinsam einen kleinen Laden. Die Ladentür ist
mit zwei unterschiedlichen Schlössern gesichert. Peter verfügt über den Schlüssel für
das eine Schloss, Paul verfügt über den Schlüssel für das andere Schloss. Der
Laden kann folglich nur dann pünktlich geöffnet werden, wenn beide Freunde
pünktlich zur Arbeit erscheinen. Die Wahrscheinlichkeit, dass Peter rechtzeitig
erscheint, beträgt 85 Prozent. Für Paul beträgt diese Wahrscheinlichkeit sogar nur 82
Prozent. Mit einer Wahrscheinlichkeit von 90 Prozent ist mindestens einer der
Freunde rechtzeitig vor der Ladenöffnung da. Mit welcher Wahrscheinlichkeit wird der
Laden pünktlich geöffnet?