# --- PAGE page_1 ---

# -`sleq`j_rr ?1_10 Computational and Data Science BSc HS 2023 

## Lösungen

Mathematik 1

## 1. Aussagen über Ableitungen von trigonometrischen Funktionen

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) Die Ableitungen der trigonometrischen Funktionen sind nur bezüglich des <br> Gradmass definiert. | 0 | $\bullet$ |
| b) Die Ableitungen der trigonometrischen Funktionen sind nur bezüglich des <br> Bogenmass definiert. | $\bullet$ | 0 |
| c) Die Ableitungen $\sin ^{\prime}(x)$ und $\cos ^{\prime}(x)$ sind für alle $x \in \mathbb{R}$ definiert. | $\bullet$ | 0 |
| d) Die Ableitungen $\tan ^{\prime}(x)$ und $\cot ^{\prime}(x)$ sind für alle $x \in \mathbb{R}$ definiert. | 0 | $\bullet$ |
| e) Die Ableitungen $\tan ^{\prime}(x)$ und $\cot ^{\prime}(x)$ sind genau für alle jene $x \in \mathbb{R}$ defi- <br> niert, an welchen auch $\tan (x)$ bzw. $\cot (x)$ definiert sind. | $\bullet$ | 0 |

## 2. Ableitung von trigonometrischen Funktionen

Wir verwenden die Beziehungen zwischen den trigonometrischen Funktionen und geeignete Ableitungsregeln, um aus der Sinus-Ableitung

$$
\sin ^{\prime}(\varphi)=\cos (\varphi)
$$

jeweils die Ableitung der folgenden Funktionen zu bestimmen.
a) Für alle $\varphi \in \mathbb{R}$ gilt

$$
\cos (\varphi)=\sin (\pi / 2-\varphi)
$$

Mit Hilfe der Ketten-Regel und (1) erhalten wir

$$
\underline{\cos ^{\prime}(\varphi)}=\sin ^{\prime}(\pi / 2-\varphi) \cdot(\pi / 2-\varphi)^{\prime}=\cos (\pi / 2-\varphi) \cdot(-1)=-\underline{\sin (\varphi)}
$$

b) Für alle $\varphi \in \mathbb{R} \backslash(\pi / 2+\pi \mathbb{Z})$ gilt

$$
\tan (\varphi)=\frac{\sin (\varphi)}{\cos (\varphi)}
$$

Wir zeigen mehrere Varianten, wie die Ableitung von $\tan (\varphi)$ berechnet und dargestellt werden kann.

# --- PAGE page_2 ---

Variante 1: Mit Hilfe der Quotienten-Regel, (1) und (3) erhalten wir

$$
\begin{aligned}
\underline{\tan ^{\prime}(\varphi)} & =\frac{\sin ^{\prime}(\varphi) \cdot \cos (\varphi)-\sin (\varphi) \cdot \cos ^{\prime}(\varphi)}{\cos ^{2}(\varphi)}=\frac{\cos (\varphi) \cdot \cos (\varphi)-\sin (\varphi) \cdot(-\sin (\varphi))}{\cos ^{2}(\varphi} \\
& =\frac{\cos ^{2}(\varphi)+\sin ^{2}(\varphi)}{\cos ^{2}(\varphi)}=\frac{\cos ^{2}(\varphi)}{\cos ^{2}(\varphi)}+\frac{\sin ^{2}(\varphi)}{\cos ^{2}(\varphi)}=\underline{1+\tan ^{2}(\varphi)}
\end{aligned}
$$

Variante 2: Mit Hilfe der Quotienten-Regel, (1) und (3) erhalten wir

$$
\begin{aligned}
\underline{\tan ^{\prime}(\varphi)} & =\frac{\sin ^{\prime}(\varphi) \cdot \cos (\varphi)-\sin (\varphi) \cdot \cos ^{\prime}(\varphi)}{\cos ^{2}(\varphi)}=\frac{\cos (\varphi) \cdot \cos (\varphi)-\sin (\varphi) \cdot(-\sin (\varphi))}{\cos ^{2}(\varphi} \\
& =\frac{\cos ^{2}(\varphi)+\sin ^{2}(\varphi)}{\cos ^{2}(\varphi)}=\underline{\frac{1}{\cos ^{2}(\varphi)}}
\end{aligned}
$$

c) Für alle $\varphi \in \mathbb{R} \backslash \pi \mathbb{Z}$ gilt

$$
\cot (\varphi)=\frac{\cos (\varphi)}{\sin (\varphi)}
$$

Wir zeigen mehrere Varianten, wie die Ableitung von $\cot (\varphi)$ berechnet und dargestellt werden kann.
Variante 1: Mit Hilfe der Quotienten-Regel, (1) und (3) erhalten wir

$$
\begin{aligned}
\underline{\cot ^{\prime}(\varphi)} & =\frac{\cos ^{\prime}(\varphi) \cdot \sin (\varphi)-\cos (\varphi) \cdot \sin ^{\prime}(\varphi)}{\sin ^{2}(\varphi)}=\frac{-\sin (\varphi) \cdot \sin (\varphi)-\cos (\varphi) \cdot \cos (\varphi)}{\sin ^{2}(\varphi} \\
& =\frac{-\sin ^{2}(\varphi)-\cos ^{2}(\varphi)}{\sin ^{2}(\varphi)}=-\frac{\sin ^{2}(\varphi)}{\sin ^{2}(\varphi)}-\frac{\cos ^{2}(\varphi)}{\sin ^{2}(\varphi)}=\underline{-1-\cot ^{2}(\varphi)}
\end{aligned}
$$

Variante 2: Mit Hilfe der Quotienten-Regel, (1) und (3) erhalten wir

$$
\begin{aligned}
\underline{\cot ^{\prime}(\varphi)} & =\frac{\cos ^{\prime}(\varphi) \cdot \sin (\varphi)-\cos (\varphi) \cdot \sin ^{\prime}(\varphi)}{\sin ^{2}(\varphi)}=\frac{-\sin (\varphi) \cdot \sin (\varphi)-\cos (\varphi) \cdot \cos (\varphi)}{\sin ^{2}(\varphi} \\
& =\frac{-\sin ^{2}(\varphi)-\cos ^{2}(\varphi)}{\sin ^{2}(\varphi)}=\frac{-1}{\sin ^{2}(\varphi)}=\underline{-\frac{1}{\sin ^{2}(\varphi)}}
\end{aligned}
$$

# 3. Aussagen über Ableitungen von trigonometrischen Funktionen 

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :--: |
| a) Es gilt $\cos ^{\prime}(0)=1$. | $\bigcirc$ | $\bigcirc$ |
| b) Die Gerade $y=x$ ist eine Tangente an die Graphen von $\sin (x)$ und $\tan (x)$. | $\bigcirc$ | $\bigcirc$ |
| c) Für alle $x \in \mathbb{R}$ gilt $\sin ^{\prime \prime}(x)=-\sin (x)$ und $\cos ^{\prime \prime}(x)=-\cos (x)$. | $\bigcirc$ | $\bigcirc$ |
| d) Die Cotangens-Ableitung kann aus der Sinus-Ableitung berechnet werden. | $\bigcirc$ | $\bigcirc$ |
| e) Für alle $x \in]-\pi / 2, \pi / 2\left[\right.$ gilt $\left.\tan ^{\prime}(x) \geq 1\right.$. | $\bigcirc$ | $\bigcirc$ |
| f) Für alle $x \in]-\pi / 2, \pi / 2\left[\right.$ gilt $\left.\tan ^{\prime}(x)=\sin ^{\prime}(x) / \cos ^{\prime}(x)\right.$. | $\bigcirc$ | $\bigcirc$ |

# --- PAGE page_3 ---

# 4. Ableitungen mit trigonometrischen Funktionen 

Wir berechnen jeweils die Ableitung der angegebenen Funktion.
a) Wir betrachten die Funktion

$$
f(x)=\sin (4 x+3)
$$

Mit Hilfe der Ketten-Regel erhalten wir

$$
\underline{\underline{f^{\prime}(x)}}=\sin ^{\prime}(4 x+3) \cdot(4 x+3)^{\prime}=\cos (4 x+3) \cdot(4+0)=\underline{\underline{4 \cos (4 x+3)}}
$$

b) Wir betrachten die Funktion

$$
f(x)=\cos (2-x)
$$

Mit Hilfe der Ketten-Regel erhalten wir

$$
\underline{\underline{f^{\prime}(x)}}=\cos ^{\prime}(2-x) \cdot(2-x)^{\prime}=-\sin (2-x) \cdot(0-1)=\underline{\underline{\sin (2-x)}}
$$

c) Wir betrachten die Funktion

$$
f(x)=\cos \left(x^{2}-1\right)
$$

Mit Hilfe der Ketten-Regel erhalten wir

$$
\underline{\underline{f^{\prime}(x)}}=\cos ^{\prime}\left(x^{2}-1\right) \cdot\left(x^{2}-1\right)^{\prime}=-\sin \left(x^{2}-1\right) \cdot(2 x-0)=\underline{\underline{-2 x \sin \left(x^{2}-1\right)}}
$$

d) Wir betrachten die Funktion

$$
f(x)=2 \cot \left(x^{3}\right)
$$

Mit Hilfe der Ketten-Regel erhalten wir

$$
\underline{\underline{f^{\prime}(x)}}=2 \cdot \cot ^{\prime}\left(x^{3}\right) \cdot\left(x^{3}\right)^{\prime}=2 \cdot\left(-1-\cot ^{2}\left(x^{3}\right)\right) \cdot 3 x^{2}=\underline{\underline{-6 x^{2} \cdot\left(1+\cot ^{2}\left(x^{3}\right)\right)}}
$$

e) Wir betrachten die Funktion

$$
f(x)=x \tan ^{2}(x)
$$

Mit Hilfe der Produkt-Regel und der Quadrat-Regel erhalten wir

$$
\begin{aligned}
\underline{\underline{f^{\prime}(x)}} & =x^{\prime} \cdot \tan ^{2}(x)+x \cdot\left(\tan ^{2}(x)\right)^{\prime}=1 \cdot \tan ^{2}(x)+x \cdot 2 \cdot \tan (x) \cdot \tan ^{\prime}(x) \\
& =\underline{\tan ^{2}(x)+2 x \tan (x) \cdot\left(1+\tan ^{2}(x)\right)}
\end{aligned}
$$

f) Wir betrachten die Funktion

$$
f(x)=\frac{1}{\tan (5-3 x)}=\cot (5-3 x)
$$

Mit Hilfe der Ketten-Regel erhalten wir

$$
\begin{aligned}
\underline{\underline{f^{\prime}(x)}} & =\cot ^{\prime}(5-3 x) \cdot(5-3 x)^{\prime}=\left(-1-\cot ^{2}(5-3 x)\right) \cdot(0-3) \\
& =\underline{\underline{3 \cdot\left(1+\cot ^{2}(5-3 x)\right)}}
\end{aligned}
$$

# --- PAGE page_4 ---

# 5. Aussagen über Ableitungen von Arcus-Funktionen 

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :--: | :--: |
| a) Die Ableitungen der Arcus-Funktionen sind nur bezüglich des Bogenmass <br> definiert. | $\bullet$ | $\bigcirc$ |
| b) Die Ableitungen $\arcsin ^{\prime}(x)$ und $\arccos ^{\prime}(x)$ sind für alle $x \in \mathbb{R}$ definiert. | $\bigcirc$ | $\bullet$ |
| c) Die Ableitungen $\arcsin ^{\prime}(x)$ und $\arccos ^{\prime}(x)$ sind genau für alle jene $x \in \mathbb{R}$ <br> definiert, an welchen auch $\arcsin (x)$ bzw. $\arccos (x)$ definiert sind. | $\bigcirc$ | $\bullet$ |
| d) Die Ableitungen $\arctan ^{\prime}(x)$ und $\operatorname{arccot}^{\prime}(x)$ sind für alle $x \in \mathbb{R}$ definiert. | $\bullet$ | $\bigcirc$ |
| e) Die Ableitungen $\arctan ^{\prime}(x)$ und $\operatorname{arccot}^{\prime}(x)$ sind genau für alle jene $x \in \mathbb{R}$ <br> definiert, an welchen auch $\arctan (x)$ bzw. $\operatorname{arccot}(x)$ definiert sind. | $\bullet$ | $\bigcirc$ |

## 6. Ableitung von Arcus-Funktionen

Wir verwenden die Ketten-Regel, um jeweils die Ableitung der folgenden Funktionen aus der Ableitung der Umkehrfunktion zu bestimmen.
a) Für alle $\varphi \in]-\pi / 2, \pi / 2[$ gilt

$$
\arcsin (\sin (\varphi))=\varphi
$$

und

$$
\cos (\varphi)>0 \Rightarrow \cos (\varphi)=\sqrt{1-\sin ^{2}(\varphi)}
$$

Durch beidseitiges Ableiten von (24) mit Hilfe der Ketten-Regel erhalten wir

$$
\begin{aligned}
& \arcsin ^{\prime}(\sin (\varphi)) \cdot \sin ^{\prime}(\varphi)=\varphi^{\prime} \\
& \Rightarrow \quad \arcsin ^{\prime}(\sin (\varphi)) \cdot \cos (\varphi)=1 \quad \mid: \cos (\varphi) \\
& \Rightarrow \quad \arcsin ^{\prime}(\sin (\varphi))=\frac{1}{\cos (\varphi)}=\frac{1}{\sqrt{1-\sin ^{2}(\varphi)}}
\end{aligned}
$$

Durch die Substitution $x:=\sin (\varphi)$ erhalten wir für alle $x \in]-1,1[$ die ArcussinusAbleitung

$$
\underline{\arcsin ^{\prime}(x)=\frac{1}{\sqrt{1-x^{2}}}}
$$

b) Für alle $\varphi \in] 0, \pi[$ gilt

$$
\arccos (\cos (\varphi))=\varphi
$$

und

$$
\sin (\varphi)>0 \Rightarrow \sin (\varphi)=\sqrt{1-\cos ^{2}(\varphi)}
$$

# --- PAGE page_5 ---

Durch beidseitiges Ableiten von (30) mit Hilfe der Ketten-Regel erhalten wir

$$
\begin{aligned}
& \arccos ^{\prime}(\cos (\varphi)) \cdot \cos ^{\prime}(\varphi)=\varphi^{\prime} \\
& \Rightarrow \quad \arccos ^{\prime}(\cos (\varphi)) \cdot(-\sin (\varphi))=1 \quad \mid:(-\sin (\varphi)) \\
& \Rightarrow \quad \arccos ^{\prime}(\cos (\varphi))=-\frac{1}{\sin (\varphi)}=-\frac{1}{\sqrt{1-\cos ^{2}(\varphi)}}
\end{aligned}
$$

Durch die Substitution $x:=\cos (\varphi)$ erhalten wir für alle $x \in]-1,1[$ die ArcuscosinusAbleitung

$$
\underline{\arccos ^{\prime}(x)=-\frac{1}{\sqrt{1-x^{2}}}}
$$

c) Für alle $\varphi \in]-\pi / 2, \pi / 2[$ gilt

$$
\arctan (\tan (\varphi))=\varphi
$$

Durch beidseitiges Ableiten von (36) mit Hilfe der Ketten-Regel erhalten wir

$$
\begin{aligned}
& \arctan ^{\prime}(\tan (\varphi)) \cdot \tan ^{\prime}(\varphi)=\varphi^{\prime} \\
& \Rightarrow \quad \arctan ^{\prime}(\tan (\varphi)) \cdot\left(1+\tan ^{2}(\varphi)\right)=1 \quad \mid:\left(1+\tan ^{2}(\varphi)\right) \\
& \Rightarrow \quad \arctan ^{\prime}(\tan (\varphi))=\frac{1}{1+\tan ^{2}(\varphi)} .
\end{aligned}
$$

Durch die Substitution $x:=\tan (\varphi)$ erhalten wir für alle $x \in \mathbb{R}$ die Arcustangens-Ableitung

$$
\underline{\arctan ^{\prime}(x)=\frac{1}{1+x^{2}}}
$$

d) Für alle $\varphi \in] 0, \pi[$ gilt

$$
\operatorname{arccot}(\cot (\varphi))=\varphi
$$

Durch beidseitiges Ableiten von (41) mit Hilfe der Ketten-Regel erhalten wir

$$
\begin{aligned}
& \operatorname{arccot}^{\prime}(\cot (\varphi)) \cdot \cot ^{\prime}(\varphi)=\varphi^{\prime} \\
& \Rightarrow \quad \operatorname{arccot}^{\prime}(\cot (\varphi)) \cdot\left(-1-\cot ^{2}(\varphi)\right)=1 \quad \mid:\left(-1-\cot ^{2}(\varphi)\right) \\
& \Rightarrow \quad \operatorname{arccot}^{\prime}(\cot (\varphi))=-\frac{1}{1+\cot ^{2}(\varphi)} .
\end{aligned}
$$

Durch die Substitution $x:=\cot (\varphi)$ erhalten wir für alle $x \in \mathbb{R}$ die ArcuscotangensAbleitung

$$
\underline{\operatorname{arccot}^{\prime}(x)=-\frac{1}{1+x^{2}}}
$$

# --- PAGE page_6 ---

# 7. Aussagen über zwei Funktionsgraphen 

Wir betrachten die Graphen der Funktionen $f$ (grün) und $g$ (orange).


| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) Es gilt $\dot{f}(0)<0$. | $\bigcirc$ | $\bullet$ |
| b) Es gilt $\dot{g}(-4)=0$. | $\bullet$ | $\bigcirc$ |
| c) Es gilt $\dot{f}(2)<\dot{g}(2)$. | $\bullet$ | $\bigcirc$ |
| d) Es gibt eine Stelle $t$, an der gilt $\dot{f}(t)=\dot{g}(t)$. | $\bullet$ | $\bigcirc$ |
| e) Gemäss Graphen wäre es denkbar, dass $\dot{f}(t)=g(t)$. | $\bullet$ | $\bigcirc$ |
| f) Gemäss Graphen wäre es denkbar, dass $\dot{g}(t)=f(t)$. | $\bigcirc$ | $\bullet$ |

## 8. Ableitung von hyperbolischen Funktionen

Wir verwenden die Definitionen sowie geeignete Ableitungsregeln, um die Ableitungen der hy-perbolischen Funktionen zu berechnen.
a) Wir betrachten die Funktion

$$
\sinh (x)=\frac{\mathrm{e}^{x}-\mathrm{e}^{-x}}{2}
$$

Aus der Ableitung der natürlichen Exponentialfunktion und mit Hilfe der Ketten-Regel finden wir

$$
\underline{\underline{\sinh ^{\prime}(x)}}=\left(\frac{\mathrm{e}^{x}-\mathrm{e}^{-x}}{2}\right)^{\prime}=\frac{\left(\mathrm{e}^{x}\right)^{\prime}-\left(\mathrm{e}^{-x}\right)^{\prime}}{2}=\frac{\mathrm{e}^{x}-(-1) \cdot \mathrm{e}^{-x}}{2}=\frac{\mathrm{e}^{x}+\mathrm{e}^{-x}}{2}=\underline{\underline{\cosh (x)}}
$$

b) Wir betrachten die Funktion

$$
\cosh (x)=\frac{\mathrm{e}^{x}+\mathrm{e}^{-x}}{2}
$$

# --- PAGE page_7 ---

Aus der Ableitung der natürlichen Exponentialfunktion und mit Hilfe der Ketten-Regel finden wir

$$
\underline{\operatorname{cosh}^{\prime}(x)}=\left(\frac{\mathrm{e}^{x}+\mathrm{e}^{-x}}{2}\right)^{\prime}=\frac{\left(\mathrm{e}^{x}\right)^{\prime}+\left(\mathrm{e}^{-x}\right)^{\prime}}{2}=\frac{\mathrm{e}^{x}+(-1) \cdot \mathrm{e}^{-x}}{2}=\frac{\mathrm{e}^{x}-\mathrm{e}^{-x}}{2}=\underline{\operatorname{sinh}(x)}
$$

c) Wir betrachten die Funktion

$$
\tanh (x)=\frac{\sinh (x)}{\cosh (x)}
$$

Wir zeigen mehrere Varianten, wie die Ableitung von $\tanh (x)$ berechnet und dargestellt werden kann.
Variante 1: Aus den Ergebnissen der Teilaufgaben a) und b) und mit Hilfe der QuotientenRegel finden wir

$$
\begin{aligned}
\underline{\tanh ^{\prime}(x)} & =\frac{\sinh ^{\prime}(x) \cdot \cosh (x)-\sinh (x) \cdot \cosh ^{\prime}(x)}{\cosh ^{2}(x)}=\frac{\cosh (x) \cdot \cosh (x)-\sinh (x) \cdot \sinh (x)}{\cosh ^{2}(x)} \\
& =\frac{\cosh ^{2}(x)-\sinh ^{2}(x)}{\cosh ^{2}(x)}=\frac{\cosh ^{2}(x)}{\cosh ^{2}(x)}-\frac{\sinh ^{2}(x)}{\cosh ^{2}(x)}=\underline{1-\tanh ^{2}(x)}
\end{aligned}
$$

Variante 2: Aus den Ergebnissen der Teilaufgaben a) und b) und mit Hilfe der QuotientenRegel finden wir

$$
\begin{aligned}
\underline{\tanh ^{\prime}(x)} & =\frac{\sinh ^{\prime}(x) \cdot \cosh (x)-\sinh (x) \cdot \cosh ^{\prime}(x)}{\cosh ^{2}(x)}=\frac{\cosh (x) \cdot \cosh (x)-\sinh (x) \cdot \sinh (x)}{\cosh ^{2}(x)} \\
& =\frac{\cosh ^{2}(x)-\sinh ^{2}(x)}{\cosh ^{2}(x)}=\underline{\frac{1}{\cosh ^{2}(x)}}
\end{aligned}
$$

d) Wir betrachten die Funktion

$$
\operatorname{coth}(x)=\frac{\cosh (x)}{\sinh (x)}
$$

Wir zeigen mehrere Varianten, wie die Ableitung von $\operatorname{coth}(x)$ berechnet und dargestellt werden kann.
Variante 1: Aus den Ergebnissen der Teilaufgaben a) und b) und mit Hilfe der QuotientenRegel finden wir

$$
\begin{aligned}
\underline{\operatorname{coth}^{\prime}(x)} & =\frac{\cosh ^{\prime}(x) \cdot \sinh (x)-\cosh (x) \cdot \sinh ^{\prime}(x)}{\sinh ^{2}(x)}=\frac{\sinh (x) \cdot \sinh (x)-\cosh (x) \cdot \cosh (x)}{\sinh ^{2}(x)} \\
& =\frac{\sinh ^{2}(x)-\cosh ^{2}(x)}{\sinh ^{2}(x)}=\frac{\sinh ^{2}(x)}{\sinh ^{2}(x)}-\frac{\cosh ^{2}(x)}{\sinh ^{2}(x)}=\underline{1-\operatorname{coth}^{2}(x)}
\end{aligned}
$$

Variante 2: Aus den Ergebnissen der Teilaufgaben a) und b) und mit Hilfe der QuotientenRegel finden wir

$$
\begin{aligned}
\underline{\operatorname{coth}^{\prime}(x)} & =\frac{\cosh ^{\prime}(x) \cdot \sinh (x)-\cosh (x) \cdot \sinh ^{\prime}(x)}{\sinh ^{2}(x)}=\frac{\sinh (x) \cdot \sinh (x)-\cosh (x) \cdot \cosh (x)}{\sinh ^{2}(x)} \\
& =\frac{\sinh ^{2}(x)-\cosh ^{2}(x)}{\sinh ^{2}(x)}=\frac{-1}{\sinh ^{2}(x)}=\underline{-\frac{1}{\sinh ^{2}(x)}}
\end{aligned}
$$

# --- PAGE page_8 ---

# 9. Ableitungen mit hyperbolischen Funktionen 

Wir berechnen jeweils die Ableitung der angegebenen Funktion.
a) Wir betrachten die Funktion

$$
f(x)=\sinh (4 x+3)
$$

Mit Hilfe der Ketten-Regel erhalten wir

$$
\underline{\underline{f^{\prime}(x)}}=\sinh ^{\prime}(4 x+3) \cdot(4 x+3)^{\prime}=\cosh (4 x+3) \cdot(4+0)=\underline{\underline{4 \cosh (4 x+3)}}
$$

b) Wir betrachten die Funktion

$$
f(x)=\cosh (2-x)
$$

Mit Hilfe der Ketten-Regel erhalten wir

$$
\underline{\underline{f^{\prime}(x)}}=\cosh ^{\prime}(2-x) \cdot(2-x)^{\prime}=\sinh (2-x) \cdot(0-1)=\underline{\underline{-\sinh (2-x)}}
$$

c) Wir betrachten die Funktion

$$
f(x)=\cosh \left(x^{2}-1\right)
$$

Mit Hilfe der Ketten-Regel erhalten wir

$$
\underline{\underline{f^{\prime}(x)}}=\cosh ^{\prime}\left(x^{2}-1\right) \cdot\left(x^{2}-1\right)^{\prime}=\sinh \left(x^{2}-1\right) \cdot(2 x-0)=\underline{\underline{2 x \sinh \left(x^{2}-1\right)}}
$$

d) Wir betrachten die Funktion

$$
f(x)=2 \operatorname{coth}\left(x^{3}\right)
$$

Mit Hilfe der Ketten-Regel erhalten wir

$$
\underline{\underline{f^{\prime}(x)}}=2 \cdot \operatorname{coth}^{\prime}\left(x^{3}\right) \cdot\left(x^{3}\right)^{\prime}=2 \cdot\left(1-\operatorname{coth}^{2}\left(x^{3}\right)\right) \cdot 3 x^{2}=\underline{\underline{6 x^{2} \cdot\left(1-\operatorname{coth}^{2}\left(x^{3}\right)\right)}}
$$

e) Wir betrachten die Funktion

$$
f(x)=x \tanh ^{2}(x)
$$

Mit Hilfe der Produkt-Regel und der Quadrat-Regel erhalten wir

$$
\begin{aligned}
\underline{\underline{f^{\prime}(x)}} & =x^{\prime} \cdot \tanh ^{2}(x)+x \cdot\left(\tanh ^{2}(x)\right)^{\prime}=1 \cdot \tanh ^{2}(x)+x \cdot 2 \cdot \tanh (x) \cdot \tanh ^{\prime}(x) \\
& =\underline{\underline{\tanh ^{2}(x)+2 x \tanh (x) \cdot\left(1-\tanh ^{2}(x)\right)}}
\end{aligned}
$$

f) Wir betrachten die Funktion

$$
f(x)=\frac{1}{\tanh (5-3 x)}=\operatorname{coth}(5-3 x)
$$

Mit Hilfe der Ketten-Regel erhalten wir

$$
\begin{aligned}
\underline{\underline{f^{\prime}(x)}} & =\operatorname{coth}^{\prime}(5-3 x) \cdot(5-3 x)^{\prime}=\left(1-\operatorname{coth}^{2}(5-3 x)\right) \cdot(0-3) \\
& =\underline{\underline{3 \cdot\left(\operatorname{coth}^{2}(5-3 x)-1\right)}}
\end{aligned}
$$

# --- PAGE page_9 ---

# 10. Ableitung von Area-Funktionen 

Wir verwenden die Ketten-Regel, um jeweils die Ableitung der folgenden Funktionen aus der Ableitung der Umkehrfunktion zu bestimmen.
a) Für alle $z \in \mathbb{R}$ gilt

$$
\operatorname{arsinh}(\sinh (z))=z
$$

und

$$
\cosh (z)=\sqrt{1+\sinh ^{2}(z)}
$$

Durch beidseitiges Ableiten von (70) mit Hilfe der Ketten-Regel erhalten wir

$$
\begin{aligned}
& \operatorname{arsinh}^{\prime}(\sinh (z)) \cdot \sinh ^{\prime}(z)=z^{\prime} \\
& \Rightarrow \quad \operatorname{arsinh}^{\prime}(\sinh (z)) \cdot \cosh (z)=1 \quad \mid: \cosh (z) \\
& \Rightarrow \quad \operatorname{arsinh}^{\prime}(\sinh (z))=\frac{1}{\cosh (z)}=\frac{1}{\sqrt{1+\sinh ^{2}(z)}}
\end{aligned}
$$

Durch die Substitution $x:=\sinh (z)$ erhalten wir für alle $x \in \mathbb{R}$ die Areasinus-HyperbolicusAbleitung

$$
\underline{\operatorname{arsinh}^{\prime}(x)=\frac{1}{\sqrt{1+x^{2}}}}
$$

b) Für alle $z \in \mathbb{R}_{0}^{+}$gilt

$$
\operatorname{arcosh}(\cosh (z))=z
$$

und

$$
\sinh (z)>0 \Rightarrow \sinh (z)=\sqrt{\cosh ^{2}(z)-1}
$$

Durch beidseitiges Ableiten von (76) mit Hilfe der Ketten-Regel erhalten wir

$$
\begin{aligned}
& \operatorname{arcosh}^{\prime}(\cosh (z)) \cdot \cosh ^{\prime}(z)=z^{\prime} \\
& \Rightarrow \quad \operatorname{arcosh}^{\prime}(\cosh (z)) \cdot \sinh (z)=1 \quad \mid: \sinh (z) \\
& \Rightarrow \quad \operatorname{arcosh}^{\prime}(\cosh (z))=\frac{1}{\sinh (z)}=\frac{1}{\sqrt{\cosh ^{2}(z)-1}}
\end{aligned}
$$

Durch die Substitution $x:=\cosh (z)$ erhalten wir für alle $x \in[1, \infty[$ die AreacosinusHyperbolicus-Ableitung

$$
\underline{\operatorname{arcosh}^{\prime}(x)=\frac{1}{\sqrt{x^{2}-1}}}
$$

# --- PAGE page_10 ---

c) Für alle $z \in \mathbb{R}$ gilt

$$
\operatorname{artanh}(\tanh (z))=z
$$

Durch beidseitiges Ableiten von (82) mit Hilfe der Ketten-Regel erhalten wir

$$
\begin{aligned}
& \operatorname{artanh}^{\prime}(\tanh (z)) \cdot \tanh ^{\prime}(z)=z^{\prime} \\
& \Rightarrow \quad \operatorname{artanh}^{\prime}(\tanh (z)) \cdot\left(1-\tanh ^{2}(z)\right)=1 \quad \mid:\left(1-\tanh ^{2}(z)\right) \\
& \Rightarrow \quad \operatorname{artanh}^{\prime}(\tanh (z))=\frac{1}{1-\tanh ^{2}(z)} .
\end{aligned}
$$

Durch die Substitution $x:=\tanh (z)$ erhalten wir für alle $x \in]-1,1[$ die Areatangens-Hyperbolicus-Ableitung

$$
\underline{\operatorname{artanh}^{\prime}(x)=\frac{1}{1-x^{2}}}
$$

d) Für alle $z \in \mathbb{R} \backslash\{0\}$ gilt

$$
\operatorname{arcoth}(\operatorname{coth}(z))=z
$$

Durch beidseitiges Ableiten von (87) mit Hilfe der Ketten-Regel erhalten wir

$$
\begin{aligned}
& \operatorname{arcoth}^{\prime}(\operatorname{coth}(z)) \cdot \operatorname{coth}^{\prime}(z)=z^{\prime} \\
& \Rightarrow \quad \operatorname{arcoth}^{\prime}(\operatorname{coth}(z)) \cdot\left(1-\operatorname{coth}^{2}(z)\right)=1 \quad \mid:\left(1-\operatorname{coth}^{2}(z)\right) \\
& \Rightarrow \quad \operatorname{arcoth}^{\prime}(\operatorname{coth}(z))=\frac{1}{1-\operatorname{coth}^{2}(z)} .
\end{aligned}
$$

Durch die Substitution $x:=\operatorname{coth}(z)$ erhalten wir für alle $x \in \mathbb{R} \backslash]-1,1[$ die Areacotangens-Hyperbolicus-Ableitung

$$
\underline{\operatorname{arcoth}^{\prime}(x)=\frac{1}{1-x^{2}}}
$$

# 11. Diverse Ableitungen berechnen 

Wir berechnen jeweils die Ableitung der angegebenen Funktion.
a) Wir betrachten die Funktion

$$
f(x)=\frac{x^{6}}{3}-\frac{x^{15}}{5}-\mathrm{e}^{14}
$$

Mit Hilfe der Summen-Regel, der Faktor-Regel und der Monom-Ableitung erhalten wir

$$
\underline{f^{\prime}(x)}=\frac{1}{3} \cdot 6 x^{6-1}-\frac{1}{5} \cdot 15 x^{15-1}-0=2 x^{5}-3 x^{14}=\underline{x^{5} \cdot\left(2-3 x^{9}\right)}
$$

# --- PAGE page_11 ---

b) Wir betrachten die Funktion

$$
f(x)=\cos ^{3}(x)
$$

Mit Hilfe der Ketten-Regel, der Monom-Ableitung und der Cosinus-Ableitung erhalten wir

$$
\underline{\underline{f^{\prime}(x)}}=\cos ^{\prime}(x) \cdot 3 \cdot \cos ^{3-1}(x)=\underline{\underline{-3 \sin (x) \cos ^{2}(x)}}
$$

c) Wir betrachten die Funktion

$$
f(x)=\sin \left(1+x^{5}\right)
$$

Mit Hilfe der Ketten-Regel, der Sinus-Ableitung und der Monom-Ableitung erhalten wir

$$
\underline{\underline{f^{\prime}(x)}}=\left(1+x^{5}\right)^{\prime} \cdot \sin ^{\prime}\left(1+x^{5}\right)=\left(0+5 x^{5-1}\right) \cdot \cos \left(1+x^{5}\right)=\underline{\underline{5 x^{4} \cos \left(1+x^{5}\right)}}
$$

d) Wir betrachten die Funktion

$$
f(t)=3^{z} \sin (z)
$$

Der Funktionsterm hängt nicht von der Argumentvariable $t$ ab. Unter der Annahme, dass auch $z$ von $t$ unabhängig ist, muss gelten

$$
\underline{\hat{f}(t)}=0
$$

Des weiteren betrachten wir die Funktion

$$
\tilde{f}(z)=3^{z} \sin (z)
$$

Mit Hilfe der Produkt-Regel, der Exponential-Ableitung und der Sinus-Ableitung erhalten wir

$$
\begin{aligned}
\tilde{f}^{\prime}(z) & =\left(3^{z}\right)^{\prime} \cdot \sin (z)+3^{z} \cdot \sin ^{\prime}(z)=\ln (3) \cdot 3^{z} \cdot \sin (z)+3^{z} \cdot \cos (z) \\
& =3^{z} \cdot(\ln (3) \cdot \sin (z)+\cos (z))
\end{aligned}
$$

e) Wir betrachten die Funktion

$$
f(s)=\frac{1}{1+s^{2}+\mathrm{e}^{s}}
$$

Mit Hilfe der Reziproken-Regel, der Monom-Ableitung und der Exponential-Ableitung erhalten wir

$$
\underline{\underline{f^{\prime}(s)}}=-\frac{\left(1+s^{2}+\mathrm{e}^{s}\right)^{\prime}}{\left(1+s^{2}+\mathrm{e}^{s}\right)^{2}}=-\frac{0+2 s^{2-1}+\mathrm{e}^{s}}{\left(1+s^{2}+\mathrm{e}^{s}\right)^{2}}=\underline{\underline{-\frac{2 s+\mathrm{e}^{s}}{\left(1+s^{2}+\mathrm{e}^{s}\right)^{2}}}}
$$

f) Wir betrachten die Funktion

$$
f(x)=\frac{\sin (x)}{\mathrm{e}^{x}}
$$

Wir zeigen mehrere Varianten, um die Ableitung von $f$ zu berechnen.

# --- PAGE page_12 ---

Variante 1: Mit Hilfe der Quotienten-Regel, der Sinus-Ableitung und der ExponentialAbleitung erhalten wir

$$
\underline{\underline{f^{\prime}(x)}}=\frac{\sin ^{\prime}(x) \cdot \mathrm{e}^{x}-\sin (x) \cdot\left(\mathrm{e}^{x}\right)^{\prime}}{\left(\mathrm{e}^{x}\right)^{2}}=\frac{\cos (x) \cdot \mathrm{e}^{x}-\sin (x) \cdot \mathrm{e}^{x}}{\left(\mathrm{e}^{x}\right)^{2}}=\underline{\underline{\cos (x)-\sin (x)} \mathrm{e}^{x}}
$$

Variante 2: Mit Hilfe der Produkt-Regel, der Sinus-Ableitung und der Exponential-Ableitung (mit Minuszeichen) erhalten wir

$$
\begin{aligned}
\underline{\underline{f^{\prime}(x)}} & =\sin ^{\prime}(x) \cdot \mathrm{e}^{-x}+\sin (x) \cdot\left(\mathrm{e}^{-x}\right)^{\prime}=\cos (x) \cdot \mathrm{e}^{-x}+\sin (x) \cdot\left(-\mathrm{e}^{-x}\right) \\
& =\cos (x) \cdot \mathrm{e}^{-x}-\sin (x) \cdot \mathrm{e}^{-x}=\underline{(\cos (x)-\sin (x)) \mathrm{e}^{-x}}
\end{aligned}
$$