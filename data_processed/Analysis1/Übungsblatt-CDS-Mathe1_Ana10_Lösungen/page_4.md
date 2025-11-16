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