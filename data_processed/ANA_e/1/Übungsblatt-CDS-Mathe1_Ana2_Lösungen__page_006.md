<|ref|>sub_title<|/ref|><|det|>[[77, 67, 310, 84]]<|/det|>
## 4. Funktionsdefinitionen 

<|ref|>text<|/ref|><|det|>[[77, 83, 895, 102]]<|/det|>
Wir untersuchen, welche der folgenden Definitionen eine Funktion beschreiben und welche nicht. 

<|ref|>text<|/ref|><|det|>[[90, 106, 790, 125]]<|/det|>
a) Die Definition \(f: \mathbb{Q} \to \mathbb{Q}\), \(x \mapsto f(x) := x^2\) stellt eine Funktion dar, denn für jedes 

<|ref|>equation<|/ref|><|det|>[[117, 124, 450, 147]]<|/det|>
\[
x = \frac{p}{q} \in \mathbb{Q} \text{ mit } p, q \in \mathbb{Z} \text{ und } q \neq 0 \text{ gilt}
\]

<|ref|>equation<|/ref|><|det|>[[375, 156, 633, 202]]<|/det|>
\[
\frac{f(x)}{x} = x^2 = \left(\frac{p}{q}\right)^2 = \frac{p^2}{q^2} \in \mathbb{Q},
\]

<|ref|>text<|/ref|><|det|>[[117, 217, 377, 237]]<|/det|>
weil \(p^2 \in \mathbb{Z}\) und \(q^2 \in \mathbb{Z} \setminus \{0\}\). 

<|ref|>text<|/ref|><|det|>[[90, 243, 890, 280]]<|/det|>
b) Die Definition \(f: \mathbb{Q} \to \mathbb{Q}\), \(x \to f(x) := \sqrt{x}\) stellt keine Funktion dar, denn es gilt zum Beispiel 

<|ref|>equation<|/ref|><|det|>[[432, 293, 888, 315]]<|/det|>
\[
f(2) = \sqrt{2} \notin \mathbb{Q}. \quad (13)
\]

<|ref|>text<|/ref|><|det|>[[90, 336, 816, 355]]<|/det|>
c) Die Definition \(f: \mathbb{N} \to \mathbb{N}^+\), \(x \mapsto f(x) := 2^x\) stellt eine Funktion dar, denn es gilt 

<|ref|>equation<|/ref|><|det|>[[413, 367, 888, 389]]<|/det|>
\[
\frac{f(0)}{2} = 2^0 = \frac{1}{2} \in \mathbb{N}^+ \quad (14)
\]

<|ref|>text<|/ref|><|det|>[[117, 407, 352, 425]]<|/det|>
sowie für alle \(n \in \mathbb{N}^+\) dass 

<|ref|>equation<|/ref|><|det|>[[375, 437, 888, 477]]<|/det|>
\[
\frac{f(n)}{n} = 2^n = \underbrace{2 \cdot \ldots \cdot 2}_{n \text{ Faktoren}} \in \mathbb{N}^+. \quad (15)
\]

<|ref|>text<|/ref|><|det|>[[90, 496, 888, 533]]<|/det|>
d) Die Definition \(f: \mathbb{N}^+ \to \mathbb{Q}\), \(x \mapsto f(x) := \frac{1}{x}\) stellt eine Funktion dar, denn für alle \(n \in \mathbb{N}^+\) gilt 

<|ref|>equation<|/ref|><|det|>[[437, 546, 888, 583]]<|/det|>
\[
f(n) = \frac{1}{n} \in \mathbb{Q}. \quad (16)
\]

<|ref|>text<|/ref|><|det|>[[90, 600, 890, 637]]<|/det|>
e) Die Definition \(f: \lfloor 0,1 \rfloor \to \lfloor 0,1 \rfloor\), \(x \mapsto f(x) := \frac{1}{x}\) stellt keine Funktion dar, denn es gilt zum Beispiel 

<|ref|>equation<|/ref|><|det|>[[392, 648, 888, 692]]<|/det|>
\[
f\left(\frac{1}{2}\right) = \frac{1}{\frac{1}{2}} = 2 \notin \lfloor 0,1 \rfloor. \quad (17)
\]

<|ref|>text<|/ref|><|det|>[[90, 710, 890, 749]]<|/det|>
f) Die Definition \(f: \mathbb{Q} \setminus \{1\} \to \mathbb{Q}\), \(x \mapsto f(x) := \frac{1}{1-x}\) stellt eine Funktion dar, denn für jedes \(x = \frac{p}{q} \in \mathbb{Q} \setminus \{1\}\) mit \(p, q \in \mathbb{Z}\) und \(q \neq 0\) gilt 

<|ref|>equation<|/ref|><|det|>[[475, 764, 888, 783]]<|/det|>
\[
p \neq q \quad (18)
\]

<|ref|>text<|/ref|><|det|>[[117, 796, 216, 813]]<|/det|>
und damit 

<|ref|>equation<|/ref|><|det|>[[276, 822, 888, 863]]<|/det|>
\[
\frac{f(x)}{x} = \frac{1}{x-1} = \frac{1}{\frac{p}{q}-1} = \frac{1}{\frac{p}{q} - \frac{q}{q}} = \frac{1}{\frac{p-q}{q}} = \frac{q}{p-q} \in \mathbb{Q}, \quad (19)
\]

<|ref|>text<|/ref|><|det|>[[117, 878, 393, 897]]<|/det|>
weil \(q \in \mathbb{Z}\) und \(p - q \in \mathbb{Z} \setminus \{0\}\).