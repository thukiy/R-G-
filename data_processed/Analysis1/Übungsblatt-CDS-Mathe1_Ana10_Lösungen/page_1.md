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