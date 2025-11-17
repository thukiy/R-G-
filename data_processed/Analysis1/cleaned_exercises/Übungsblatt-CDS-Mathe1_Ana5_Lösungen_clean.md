# --- PAGE page_1 ---

# Übungsblatt Ana 5 

## 1. Aussagen über Betrag und Vorzeichen

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :--: | :--: |
| a) Für alle positiven reellen Zahlen $x>0$ gilt $|x|=x$. | $\bullet$ | $\bigcirc$ |
| b) Für jedes $x \in \mathbb{R}$ gilt $||x||=|x|$. | $\bullet$ | $\bigcirc$ |
| c) Für jedes $x \in \mathbb{R}$ gilt $\operatorname{sgn}(\operatorname{sgn}(x))=\operatorname{sgn}(x)$. | $\bullet$ | $\bigcirc$ |
| d) Die Gleichung $\operatorname{sgn}(x)=|x|$ hat nur die Lösung $x=0$. | $\bigcirc$ | $\bullet$ |
| e) Für jedes $x \in \mathbb{R}$ gilt $0 \leq|\operatorname{sgn}(x)| \leq 1$. | $\bullet$ | $\bigcirc$ |
| f) Für jedes $x \in \mathbb{R}$ gilt $\operatorname{sgn}(|x|)=1$. | $\bigcirc$ | $\bullet$ |

## 2. Aussagen über Potenz-Funktionen

Wir betrachten $A \subseteq \mathbb{R}, p \in \mathbb{R}$ und die allgemeine Potenz-Funktion

$$
\begin{aligned}
f: & A \rightarrow \mathbb{R} \\
& x \mapsto f(x):=x^{p}
\end{aligned}
$$

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :--: | :--: |
| a) Für $p=0.5$ darf man $A=\mathbb{R}$ wählen. | $\bigcirc$ | $\bullet$ |
| b) Für $p \leq 0$ muss in jedem Fall gelten $0 \notin A$. | $\bullet$ | $\bigcirc$ |
| c) In jedem Fall gilt $f(0)=0$. | $\bigcirc$ | $\bullet$ |
| d) Falls $1 \in A$, dann gilt $f(1)=1$. | $\bullet$ | $\bigcirc$ |

# --- PAGE page_2 ---

# 3. Aussagen über eigentliche Exponentialfunktionen 

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :--: | :--: |
| a) Eigentliche Exponentialfunktionen beschreiben jeweils die Beziehung zwi- <br> schen zwei Grössen in vielen Anwendungen aus Alltag, Naturwissenschaft, <br> Technik und Wirtschaft. | 0 |  |
| b) Eigentliche Exponentialfunktionen sind immer injektiv. |  |  |
| c) Eigentliche Exponentialfunktionen sind immer strikt monoton steigend. | 0 |  |
| d) Jede eigentliche Exponentialfunktion hat eine Umkehrfunktion, sofern man <br> die Zielmenge geschickt wählt. |  |  |
| e) Es gibt keine eigentliche Exponentialfunktion, deren Graph durch den <br> Punkt $(0 ; 0)$ verläuft. |  |  |
| f) Der Graph jeder eigentlichen Exponentialfunktion verläuft durch den <br> Punkt $(0 ; 1)$. |  |  |

## 4. Einfache, eigentliche Exponentialfunktionen

Wir betrachten die eigentlichen Exponentialfunktionen mit Basen $a \in\{2,3,1 / 2,1 / 3\}$, d.h.

$$
f(x):=2^{x}, \quad g(x):=3^{x}, \quad h(x):=\left(\frac{1}{2}\right)^{x} \quad \text { und } \quad i(x):=\left(\frac{1}{3}\right)^{x}
$$

a) Wir berechnen für die Funktionen $f, g, h$ und $i$ aus (2) die Funktionswerte jeweils an den Stellen $x \in\{-3,-2,-1,0,1,2,3\}$ und stellen die Ergebnisse in einer Tabelle zusammen:

| $x$ | $f(x)$ | $g(x)$ | $h(x)$ | $i(x)$ |
| :--: | :--: | :--: | :--: | :--: |
| -3 | $1 / 8$ | $1 / 27$ | 8 | 27 |
| -2 | $1 / 4$ | $1 / 9$ | 4 | 9 |
| -1 | $1 / 2$ | $1 / 3$ | 2 | 3 |
| 0 | 1 | 1 | 1 | 1 |
| 1 | 2 | 3 | $1 / 2$ | $1 / 3$. |
| 2 | 4 | 9 | $1 / 4$ | $1 / 9$ |
| 3 | 8 | 27 | $1 / 8$ | $1 / 27$ |

# --- PAGE page_3 ---

b) Wir skizzieren die Graphen der Funktionen $f, g, h$ und $i$ aus (2) in einem einzigen $x$ - $y$ Diagramm.

c) Gemäss Skizze aus Teilaufgabe b) sind die Funktionen $f$ und $g$ monoton steigend, während $h$ und $i$ monoton fallend sind. Allgemein gilt

$$
\begin{aligned}
& \underline{0<a<1} \Leftrightarrow a^{x} \text { monoton fallend } \\
& \underline{a>1} \Leftrightarrow a^{x} \text { monoton steigend. }
\end{aligned}
$$

d) Wir betrachten die Funktionen $f, g, h$ und $i$ aus (2) als Funktionen des Typs $\mathbb{R} \rightarrow \mathbb{R}$.

Surjektivität: Gemäss Skizze aus Teilaufgabe b) gilt

$$
f(\mathbb{R})=g(\mathbb{R})=h(\mathbb{R})=i(\mathbb{R})=\mathbb{R}^{+} \subset \mathbb{R}
$$

Weil die Bildmenge von $f, g, h$ und $i$ nur $\mathbb{R}^{+}$ist, stimmt sie nicht mit der Zielmenge $\mathbb{R}$ überein. Die Funktionen sind demnach nicht surjektiv.
Injektivität: Weil gemäss Skizze aus Teilaufgabe b) jedes $y \in \mathbb{R}^{+}$Funktionswert der Funktionen $f, g, h$ und $i$ zu jeweils genau einem Argument $x \in \mathbb{R}$ ist, sind diese Funktionen injektiv.
Bijektivität: Weil $f, g, h$ und $i$ nicht surjektiv sind, können sie auch nicht bijektiv sein.
e) Der Umstand, dass die Funktionen $f, g, h$ und $i$ als Funktionen des Typs $\mathbb{R} \rightarrow \mathbb{R}$ zwar injektiv aber nicht surjektiv sind, kann durch eine Verkleinerung der Zielmenge $\mathbb{R}$ auf die Bildmenge $\mathbb{R}^{+}$behoben werden. Als Funktionen des Typs $\underline{\mathbb{R} \rightarrow \mathbb{R}^{+}}$sind $f, g, h$ und $i$ in der Tat surjektiv und damit auch bijektiv.

# --- PAGE page_4 ---

f) Wir betrachten die Funktionen $f, g, h$ und $i$ gemäss Teilaufgabe e) als Funktionen des Typs $\mathbb{R} \rightarrow \mathbb{R}^{+}$und berechnen ihre Umkehrfunktionen. Dazu müssen wir die Funktionsterme aus 2) nach $x$ auflösen. Es seien also $x \in \mathbb{R}$ und $y \in \mathbb{R}^{+}$, dann gilt

$$
\begin{aligned}
y & =a^{x} \\
\Leftrightarrow \quad \log _{a}(y) & =x
\end{aligned} \quad \left\lvert\, \log _{a}(\ldots)\right.
$$

Die Umkehrfunktionen von $f$ und $g$ sind demnach

$$
\begin{aligned}
& f^{-1}: \mathbb{R}^{+} \rightarrow \mathbb{R} \\
& x \mapsto f^{-1}(x):=\log _{2}(x)
\end{aligned} \quad \text { und } \quad \begin{aligned}
g^{-1}: \mathbb{R}^{+} & \rightarrow \mathbb{R} \\
x & \mapsto g^{-1}(x):=\log _{3}(x)
\end{aligned}
$$

Ebenso erhalten wir für $h$ und $i$ die Umkehrfunktionen

$$
\begin{aligned}
& h^{-1}: \mathbb{R}^{+} \rightarrow \mathbb{R} \\
& x \mapsto h^{-1}(x):=\log _{1 / 2}(x)
\end{aligned} \quad \text { und } \quad \begin{aligned}
i^{-1}: \mathbb{R}^{+} & \rightarrow \mathbb{R} \\
x & \mapsto i^{-1}(x):=\log _{1 / 3}(x)
\end{aligned}
$$

Alternativ könnten wir die Funktionsterme von $h^{-1}$ und $i^{-1}$ auch schreiben als

$$
\begin{aligned}
& \underline{\underline{i^{-1}(x)}}=\log _{1 / 2}(x)=\frac{\log _{2}(x)}{\log _{2}(1 / 2)}=\frac{\log _{2}(x)}{-1}=\underline{-\log _{2}(x)} \\
& \underline{\underline{i^{-1}(x)}}=\log _{1 / 3}(x)=\frac{\log _{3}(x)}{\log _{3}(1 / 3)}=\frac{\log _{3}(x)}{-1}=\frac{-\log _{3}(x) .
\end{aligned}
$$

# 5. Aussagen über eine Funktion 

Wir betrachten die Funktion

$$
\begin{aligned}
f: \mathbb{R} & \rightarrow \mathbb{R} \\
x & \mapsto f(x):=(\sqrt{3})^{x}-1
\end{aligned}
$$

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) Die Funktion $f$ ist eine eigentliche Exponentialfunktion. | $\bigcirc$ | $\bullet$ |
| b) Es gilt $f(0)=0$. | $\bullet$ | $\bigcirc$ |
| c) Es gilt $f\left(1^{\prime} 001\right) \in \mathbb{Q}$. | $\bigcirc$ | $\bullet$ |
| d) Die Funktion $g: \mathbb{R} \rightarrow \mathbb{R}$ mit $g(x):=(f(x)+1)^{2}$ ist eine eigentliche <br> Exponentialfunktion. | $\bullet$ | $\bigcirc$ |
| e) Der Graph von $f$ schneidet die Graphen aller eigentlichen Exponential- <br> funktionen. | $\bigcirc$ | $\bullet$ |

# --- PAGE page_5 ---

# 6. Eigenschaften von eigentlichen Exponentialfunktionen 

Seien $a \in \mathbb{R}^{+} \backslash\{1\}, x, y \in \mathbb{R}, z \in \mathbb{R} \backslash\{0\}$ und $f$ die eigentliche Exponentialfunktion

$$
\begin{aligned}
f: \mathbb{R} & \rightarrow \mathbb{R} \\
x & \mapsto f(x):=a^{x}
\end{aligned}
$$

Wir beweisen die folgenden Eigenschaften von $f$ und prüfen diese jeweils an einem selbstgewählten Zahlenbeispiel nach.
a) Allgemein gilt

$$
\underline{\underline{f(0)}}=a^{0}=\underline{1}
$$

Als Beispiel wählen wir $a=2$. Wir erhalten

$$
\underline{\underline{f(0)}}=2^{0}=\underline{1}
$$

b) Allgemein gilt

$$
\underline{\underline{f(-x)}}=a^{-x}=\frac{1}{a^{x}}=\frac{1}{\underline{\underline{f(x)}}}
$$

Als Beispiel wählen wir $a=2$ und $x=3$. Wir erhalten

$$
\begin{aligned}
f(3) & =2^{3}=8 \\
\underline{\underline{f(-3)}} & =2^{-3}=\frac{1}{2^{3}}=\frac{1}{8}=\frac{1}{\underline{\underline{f(3)}}
\end{aligned}
$$

c) Allgemein gilt

$$
\underline{\underline{f(1)}}=a^{1}=\underline{\underline{a}}
$$

Als Beispiel wählen wir $a=3$. Wir erhalten

$$
\underline{\underline{f(1)}}=3^{1}=3=\underline{\underline{a}}
$$

d) Allgemein gilt

$$
\underline{\underline{f(-1)}}=a^{-1}=\frac{1}{\underline{\underline{a}}}
$$

Als Beispiel wählen wir $a=3$. Wir erhalten

$$
\underline{\underline{f(-1)}}=3^{-1}=\frac{1}{3}=\frac{1}{\underline{\underline{a}}}
$$

e) Allgemein gilt

$$
\underline{\underline{f(x+1)}}=a^{x+1}=a^{x} \cdot a^{1}=a^{x} \cdot a=\underline{\underline{a} \cdot f(x)}
$$

Als Beispiel wählen wir $a=5$ und $x=2$. Wir erhalten

$$
\begin{aligned}
f(2) & =5^{2}=25 \\
\underline{\underline{f(2+1)}} & =f(3)=5^{3}=125=5 \cdot 25=\underline{\underline{5 \cdot f(2)}}
\end{aligned}
$$

# --- PAGE page_6 ---

f) Allgemein gilt

$$
\underline{\underline{f(x-1)}}=a^{x-1}=\frac{a^{x}}{a^{1}}=\underline{\frac{f(x)}{a}}
$$

Als Beispiel wählen wir $a=5$ und $x=3$. Wir erhalten

$$
\begin{aligned}
f(3) & =5^{3}=125 \\
\underline{\underline{f(3-1)}} & =f(2)=5^{2}=25=\frac{125}{5}=\underline{\underline{\frac{f(3)}{5}}}
\end{aligned}
$$

g) Allgemein gilt

$$
\underline{\underline{f(x+y)}}=a^{x+y}=a^{x} \cdot a^{y}=\underline{\underline{f(x) \cdot f(y)}}
$$

Als Beispiel wählen wir $a=2, x=3$ und $y=5$. Wir erhalten

$$
\begin{aligned}
f(3) & =2^{3}=8 \\
f(5) & =2^{5}=32 \\
\underline{\underline{f(3+5)}} & =f(8)=2^{8}=256=8 \cdot 32=\underline{\underline{f(3) \cdot f(5)}}
\end{aligned}
$$

h) Allgemein gilt

$$
\underline{\underline{f(x-y)}}=a^{x-y}=\frac{a^{x}}{a^{y}}=\frac{f(x)}{\underline{\underline{f(y)}}}
$$

Als Beispiel wählen wir $a=2, x=3$ und $y=5$. Wir erhalten

$$
\begin{aligned}
f(3) & =2^{3}=8 \\
f(5) & =2^{5}=32 \\
\underline{\underline{f(3-5)}} & =f(-2)=2^{-2}=\frac{1}{4}=\frac{8}{32}=\underline{\underline{f(3)}} \\
\underline{\underline{(5)}}
\end{aligned}
$$

i) Allgemein gilt

$$
\underline{\underline{f(x \cdot y)}}=a^{x \cdot y}=\left(a^{x}\right)^{y}=\underline{\underline{(f(x))^{y}=(f(y))^{x}}}
$$

Als Beispiel wählen wir $a=2, x=3$ und $y=5$. Wir erhalten

$$
\begin{aligned}
f(3) & =2^{3}=8 \\
f(5) & =2^{5}=32 \\
\underline{\underline{f(3 \cdot 5)}}=f(15) & =2^{15}=32^{\prime} 768=8^{5}=\underline{\underline{(f(3))^{5}}} \\
\underline{\underline{f(3 \cdot 5)}}=f(15) & =2^{15}=32^{\prime} 768=32^{3}=\underline{\underline{(f(5))^{3}}}
\end{aligned}
$$

# --- PAGE page_7 ---

j) Allgemein gilt

$$
f\left(\frac{x}{z}\right)=a^{\frac{x}{z}}=\sqrt[4]{a^{x}}=\sqrt[4]{f(x)}
$$

Als Beispiel wählen wir $a=2, x=10$ und $z=5$. Wir erhalten

$$
\begin{aligned}
f(10) & =2^{10}=1^{\prime} 024 \\
f\left(\frac{10}{5}\right) & =f(2)=2^{2}=4=\sqrt[5]{1^{\prime} 024}=\sqrt[5]{f(10)}
\end{aligned}
$$

k) Allgemein gilt

$$
\underline{f\left(\log _{a}(x)\right)}=a^{\log _{a}(x)}=\underline{x}
$$

Als Beispiel wählen wir $a=3$ und $x=81$. Wir erhalten

$$
\underline{f\left(\log _{3}(81)\right)}=f(4)=3^{4}=\underline{81}
$$

I) Allgemein gilt

$$
\underline{\log _{a}(f(x))}=\log _{a}\left(a^{x}\right)=\underline{x}
$$

Als Beispiel wählen wir $a=3$ und $x=4$. Wir erhalten

$$
\underline{\log _{3}(f(4))}=\log _{3}\left(3^{4}\right)=\underline{4}
$$

# 7. Aussagen über hyperbolische Funktionen 

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) Die hyperbolischen Funktionen werden mit Hilfe der natürlichen Exponen- <br> tialfunktion definiert. | $\bullet$ | $\bigcirc$ |
| b) Die hyperbolische Funktion cosh ist auf ganz $\mathbb{R}$ definiert. | $\bullet$ | $\bigcirc$ |
| c) Die hyperbolische Funktion sinh ist auf ganz $\mathbb{R}$ definiert. | $\bullet$ | $\bigcirc$ |
| d) Die hyperbolische Funktion tanh ist auf ganz $\mathbb{R}$ definiert. | $\bullet$ | $\bigcirc$ |
| e) Die hyperbolische Funktion coth ist auf ganz $\mathbb{R}$ definiert. | $\bigcirc$ | $\bullet$ |

# --- PAGE page_8 ---

# 8. Aussagen über hyperbolische Funktionen 

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :--: | :--: |
| a) Es gilt $\cosh (0) \in \mathbb{N}$. | $\bullet$ | $\bigcirc$ |
| b) Es gilt $\cosh (3)-\sinh (3)=1$. | $\bigcirc$ | $\bullet$ |
| c) Die Funktion $\sinh : \mathbb{R} \rightarrow \mathbb{R}$ ist injektiv. | $\bullet$ | $\bigcirc$ |
| d) Die Funktion $\cosh : \mathbb{R} \rightarrow[1, \infty[$ ist bijektiv. | $\bigcirc$ | $\bullet$ |

## 9. Pythagoras-Satz für hyperbolische Funktionen

Wir betrachten den Pythagoras-Satz für hyperbolische Funktionen gemäss

$$
\cosh ^{2}(x)-\sinh ^{2}(x)=1
$$

a) Für $x=0$ gilt

$$
\begin{aligned}
\underline{\cosh ^{2}(0)-\sinh ^{2}(0)} & =\left(\frac{\mathrm{e}^{0}+\mathrm{e}^{-0}}{2}\right)^{2}-\left(\frac{\mathrm{e}^{0}-\mathrm{e}^{-0}}{2}\right)^{2}=\left(\frac{1+1}{2}\right)^{2}-\left(\frac{1-1}{2}\right)^{2} \\
& =\left(\frac{2}{2}\right)^{2}-\left(\frac{0}{2}\right)^{2}=1^{2}-0^{2}=\underline{1}
\end{aligned}
$$

b) Für alle $x \in \mathbb{R}$ gilt

$$
\begin{aligned}
\underline{\cosh ^{2}(x)-\sinh ^{2}(x)} & =\left(\frac{\mathrm{e}^{x}+\mathrm{e}^{-x}}{2}\right)^{2}-\left(\frac{\mathrm{e}^{x}-\mathrm{e}^{-x}}{2}\right)^{2}=\frac{\left(\mathrm{e}^{x}+\mathrm{e}^{-x}\right)^{2}}{2^{2}}-\frac{\left(\mathrm{e}^{x}-\mathrm{e}^{-x}\right)^{2}}{2^{2}} \\
& =\frac{\left(\mathrm{e}^{x}\right)^{2}+2 \cdot \mathrm{e}^{x} \cdot \mathrm{e}^{-x}+\left(\mathrm{e}^{-x}\right)^{2}}{4}-\frac{\left(\mathrm{e}^{x}\right)^{2}-2 \cdot \mathrm{e}^{x} \cdot \mathrm{e}^{-x}+\left(\mathrm{e}^{-x}\right)^{2}}{4} \\
& =\frac{\mathrm{e}^{2 x}+2 \cdot 1+\mathrm{e}^{-2 x}-\mathrm{e}^{2 x}+2 \cdot 1-\mathrm{e}^{-2 x}}{4}=\frac{2+2}{4}=\frac{4}{4}=\underline{1}
\end{aligned}
$$