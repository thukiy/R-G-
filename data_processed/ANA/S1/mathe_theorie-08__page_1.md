<|ref|>sub_title<|/ref|><|det|>[[370, 11, 628, 70]]<|/det|>
# Grundlagen Logik 

<|ref|>text<|/ref|><|det|>[[23, 156, 373, 188]]<|/det|>
## Satz 1.1 Seien A, B und C Aussagen. Dann gelten die 

<|ref|>text<|/ref|><|det|>[[31, 220, 160, 247]]<|/det|>
1. Assoziativgesetze: 

<|ref|>equation<|/ref|><|det|>[[149, 270, 360, 344]]<|/det|>
\[ (A \lor (B \lor C)) \Leftrightarrow ((A \lor B) \lor C), \]
\[ (A \land (B \land C)) \Leftrightarrow ((A \land B) \land C). \]

<|ref|>text<|/ref|><|det|>[[31, 384, 163, 411]]<|/det|>
2. Distributivgesetze: 

<|ref|>equation<|/ref|><|det|>[[134, 434, 380, 510]]<|/det|>
\[ (A \land (B \lor C)) \Leftrightarrow ((A \land B) \lor (A \land C)), \]
\[ (A \lor (B \land C)) \Leftrightarrow ((A \lor B) \land (A \lor C)). \]

<|ref|>text<|/ref|><|det|>[[31, 550, 175, 577]]<|/det|>
3. Kommutativgesetze: 

<|ref|>equation<|/ref|><|det|>[[189, 601, 325, 677]]<|/det|>
\[ (A \land B) \Leftrightarrow (B \land A), \]
\[ (A \lor B) \Leftrightarrow (B \lor A). \]

<|ref|>text<|/ref|><|det|>[[31, 716, 216, 744]]<|/det|>
4. DE MORGANschen Regeln: 

<|ref|>equation<|/ref|><|det|>[[157, 767, 355, 841]]<|/det|>
\[ \begin{aligned} ( \neg (A \lor B) ) & \Leftrightarrow ( ( \neg A ) \land ( \neg B ) ), \\ ( \neg (A \land B) ) & \Leftrightarrow ( ( \neg A ) \lor ( \neg B ) ). \end{aligned} \]

<|ref|>text<|/ref|><|det|>[[483, 506, 949, 538]]<|/det|>
Beweis. Stellvertretend überprüfen wir die Regeln von DE MORGAN¹. 

<|ref|>table<|/ref|><|det|>[[521, 567, 950, 821]]<|/det|>
<table><tr><td>A</td><td>B</td><td>\(\neg(A \land B)\)</td><td>\((\neg A) \lor (\neg B)\)</td><td>\(((\neg A \land B)) \Leftrightarrow ((\neg A) \lor (\neg B))\)</td></tr><tr><td>W</td><td>W</td><td>F</td><td>F</td><td>W</td></tr><tr><td>W</td><td>F</td><td>W</td><td>W</td><td>W</td></tr><tr><td>F</td><td>W</td><td>W</td><td>W</td><td>W</td></tr><tr><td>F</td><td>F</td><td>W</td><td>W</td><td>W</td></tr></table>