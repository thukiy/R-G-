<|ref|>equation<|/ref|><|det|>[[15, 20, 660, 75]]<|/det|>
\[ \text{Bsp:} \quad (5) = \frac{5!}{3!(5-3)!} = \frac{5!}{3!2!} = \frac{5! \cdot 4 \cdot 5}{3! \cdot 2 \cdot 1} = 10 \]

<|ref|>sub_title<|/ref|><|det|>[[15, 87, 365, 116]]<|/det|>
## Pascal'sches Dreieck : 

<|ref|>table<|/ref|><|det|>[[0, 120, 567, 312]]<|/det|>
<table><tr><td></td><td>1</td><td>1. Zeile</td></tr><tr><td></td><td>1 1</td><td>2. Zeile</td></tr><tr><td></td><td>1 2 1</td><td>3. Zeile</td></tr><tr><td></td><td>1 3 3 1</td><td>4. Zeile</td></tr><tr><td></td><td>1 4 6 4 1</td><td>5. Zeile</td></tr><tr><td></td><td>1 5 10 10 5 1</td><td>6. Zeile</td></tr></table>

<|ref|>text<|/ref|><|det|>[[44, 319, 678, 352]]<|/det|>
(k) steht in \((n+1)\). Zeile und an \((k+1)\). Stelle 

<|ref|>sub_title<|/ref|><|det|>[[15, 380, 905, 413]]<|/det|>
## Veranschaulichung Kombination \(k\)-ter Ordnung ohne Zurücklegen 

<|ref|>image<|/ref|><|det|>[[260, 420, 595, 540]]<|/det|>
 

<|ref|>text<|/ref|><|det|>[[50, 555, 716, 585]]<|/det|>
→ Formel für Permutationen verwenden (Teil b) 

<|ref|>equation<|/ref|><|det|>[[138, 585, 590, 632]]<|/det|>
\[ P(n; k, n-k) = \frac{n!}{k!(n-k)!} = \binom{n}{k} \]

<|ref|>sub_title<|/ref|><|det|>[[15, 655, 909, 688]]<|/det|>
## Veranschaulichung Kombination \(n\)-te Ordnung mit Zurücklegen 

<|ref|>table<|/ref|><|det|>[[0, 690, 630, 800]]<|/det|>
<table><tr><td>k =</td><td>1</td><td>2</td><td>3</td><td>...</td><td>k</td></tr><tr><td>kugeln</td><td>n</td><td>n-1</td><td>n-1</td><td></td><td>n-1</td></tr><tr><td></td><td></td><td>+1</td><td>+1</td><td></td><td></td></tr></table>

<|ref|>text<|/ref|><|det|>[[88, 807, 900, 884]]<|/det|>
→ insgesamt: \(n+k-1\) Kugeln, wenn auf den Teil
d.h. im Binomialkoeffizient wird \(n\) durch
\((n+k-1)\) ersetzt → \(\binom{n+k-1}{k} = \frac{(n+k-1)!}{k!(n+k-1-k)!} = \frac{(n+k-1)!}{k!(n-1)!} = \binom{n+k-1}{n-1}\)