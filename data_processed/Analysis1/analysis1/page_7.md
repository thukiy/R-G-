# Grundlagen Logik

Satz 1.1 Seien $A, B$ und $C$ Aussagen. Dann gelten die

1. Assoziativgesetze:

$$ \begin{gathered} (A \vee(B \vee C)) \Leftrightarrow((A \vee B) \vee C) \ L \end{gathered} $$

$A \wedge(B \wedge C)) \Leftrightarrow((A \wedge B) \wedge C)$.
2. Distributivgesetze:

$$ \begin{gathered} (A \wedge(B \vee C)) \Leftrightarrow((A \wedge B) \vee(A \wedge C)) \ L \end{gathered} $$

$A \vee(B \wedge C)) \Leftrightarrow((A \vee B) \wedge(A \vee C))$.
3. Kommutativgesetze:

$$ \begin{gathered} (A \wedge B) \Leftrightarrow(B \wedge A) \ L \end{gathered} $$

$A \vee B) \Leftrightarrow(B \vee A)$.
4. De Morganschen Regeln:

$$ \begin{gathered} (\neg(A \vee B)) \Leftrightarrow((\neg A) \wedge(\neg B)) \ L \end{gathered} $$

Beweis. Stellvertretend überprüfen wir die Regeln von DE MORGAN ${ }^{1}$.

|  $A$ | $B$ | $\neg(A \wedge B)$ | $(\neg A) \vee(\neg B)$ | $(\neg(A \wedge B)) \Leftrightarrow((\neg A) \vee(\neg B))$  |
| --- | --- | --- | --- | --- |
|  W | W | F | F | W  |
|  W | F | W | W | W  |
|  F | W | W | W | W  |
|  F | F | W | W | W  |