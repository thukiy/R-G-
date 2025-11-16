# 4. Funktionsdefinitionen 

Wir untersuchen, welche der folgenden Definitionen eine Funktion beschreiben und welche nicht.
a) Die Definition $f: \mathbb{Q} \rightarrow \mathbb{Q}, x \mapsto f(x):=x^{2}$ stellt eine Funktion dar, denn für jedes $x=\frac{p}{q} \in \mathbb{Q}$ mit $p, q \in \mathbb{Z}$ und $q \neq 0$ gilt

$$
\underline{\underline{f(x)}}=x^{2}=\left(\frac{p}{q}\right)^{2}=\frac{p^{2}}{\frac{q^{2}}{}}\in \mathbb{Q}
$$

weil $p^{2} \in \mathbb{Z}$ und $q^{2} \in \mathbb{Z} \backslash\{0\}$.
b) Die Definition $f: \mathbb{Q} \rightarrow \mathbb{Q}, x \mapsto f(x):=\sqrt{x}$ stellt keine Funktion dar, denn es gilt zum Beispiel

$$
\underline{\underline{f(2)}}=\sqrt{2} \notin \mathbb{Q}
$$

c) Die Definition $f: \mathbb{N} \rightarrow \mathbb{N}^{+}, x \mapsto f(x):=2^{x}$ stellt eine Funktion dar, denn es gilt

$$
\underline{\underline{f(0)}}=2^{0}=\underline{\underline{1} \in \mathbb{N}^{+}}
$$

sowie für alle $n \in \mathbb{N}^{+}$dass

$$
\underline{\underline{f(n)}}=2^{n}=\underbrace{2 \cdot \ldots \cdot 2}_{n \text { Faktoren }} \in \mathbb{N}^{+}
$$

d) Die Definition $f: \mathbb{N}^{+} \rightarrow \mathbb{Q}, x \mapsto f(x):=\frac{1}{x}$ stellt eine Funktion dar, denn für alle $n \in \mathbb{N}^{+}$ gilt

$$
\underline{\underline{f(n)}}=\frac{1}{n} \in \mathbb{Q}
$$

e) Die Definition $\left.\left.f:\right] 0,1] \rightarrow\right] 0,1], x \mapsto f(x):=\frac{1}{x}$ stellt keine Funktion dar, denn es gilt zum Beispiel

$$
\underline{\underline{f\left(\frac{1}{2}\right)}}=\frac{1}{\frac{1}{2}}=\underline{\underline{2} \notin] 0,1]}
$$

f) Die Definition $f: \mathbb{Q} \backslash\{1\} \rightarrow \mathbb{Q}, x \mapsto f(x):=\frac{1}{x-1}$ stellt eine Funktion dar, denn für jedes $x=\frac{p}{q} \in \mathbb{Q} \backslash\{1\}$ mit $p, q \in \mathbb{Z}$ und $q \neq 0$ gilt

$$
p \neq q
$$

und damit

$$
\underline{\underline{f(x)}}=\frac{1}{x-1}=\frac{1}{\frac{p}{q}-1}=\frac{1}{\frac{p}{q}-\frac{q}{q}}=\frac{1}{\frac{p-q}{q}}=\frac{q}{\underline{\underline{p-q}}} \in \mathbb{Q}
$$

weil $q \in \mathbb{Z}$ und $p-q \in \mathbb{Z} \backslash\{0\}$.