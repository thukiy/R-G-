<|ref|>text<|/ref|><|det|>[[90, 65, 895, 102]]<|/det|>
f) Mit Hilfe der Summen-Regel, der Faktor-Regel, der Ketten-Regel und der Exponential-Regel erhalten wir 

<|ref|>equation<|/ref|><|det|>[[117, 110, 764, 200]]<|/det|>
\[
\begin{align*}
\frac{f'(l)}{l} &= \left( 3 \cdot 2^{-\frac{l}{9}} + 4 \right)' = 3 \cdot \left( 2^{-\frac{1}{9} \cdot l} \right)' + (4)' = 3 \cdot \left( -\frac{1}{9} \cdot l \right)' \cdot \ln(2) \cdot 2^{-\frac{1}{9} \cdot l} + 0 \\
&= 3 \cdot \left( -\frac{1}{9} \right) \cdot \ln(2) \cdot 2^{-\frac{l}{9}} = -\frac{\ln(2)}{3} \cdot 2^{-\frac{l}{9}}.
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[76, 226, 384, 244]]<|/det|>
3. Ausbreitung des Corona-Virus 

<|ref|>text<|/ref|><|det|>[[76, 243, 890, 314]]<|/det|>
Wir betrachten einen Tag im Frühling 2020, an welchem in der Schweiz insgesamt \(N_r = 3'245\) bestätigte Ansteckungen mit dem Corona-Virus registriert sind und \(A_r = 227/\text{d}\) Neuansteckungen gemeldet werden. Wenn man von einem *exponentiellen Wachstum* ausgeht, dann folgt die Gesamtzahl bestätige Ansteckungen einer *verallgemeinerten Exponentialfunktion* der Form 

<|ref|>equation<|/ref|><|det|>[[76, 321, 240, 349]]<|/det|>
\[
N(t) = N_0 \cdot a^{\frac{t-t_0}{\Sigma}}.
\]

<|ref|>text<|/ref|><|det|>[[76, 360, 521, 379]]<|/det|>
Die Anzahl Neuansteckungen ist die Zuwachs-Rate 

<|ref|>equation<|/ref|><|det|>[[76, 389, 320, 425]]<|/det|>
\[
A(t) = \dot{N}(t) = \frac{\ln(a)}{\Sigma} \cdot N(t).
\]

<|ref|>text<|/ref|><|det|>[[76, 433, 671, 453]]<|/det|>
Für die Werte am betrachteten Tag gilt demanch in guter Näherung 

<|ref|>equation<|/ref|><|det|>[[282, 461, 686, 500]]<|/det|>
\[
A_r \approx \frac{\ln(a)}{\Sigma} \cdot N_r \qquad \left| \cdot \frac{\Sigma}{A_r} \right|.
\]

<|ref|>text<|/ref|><|det|>[[76, 510, 890, 548]]<|/det|>
Daraus und durch Einsetzen der Basis \(a = 2\) können wir die *Zeitspanne* \(\Sigma\) berechnen, in welcher eine Verdopplung der Ansteckungen zu erwarten ist. Wir erhalten 

<|ref|>equation<|/ref|><|det|>[[76, 558, 408, 599]]<|/det|>
\[
\Sigma \approx \ln(a) \cdot \frac{N_r}{A_r} \approx \ln(2) \cdot \frac{3'245}{227 \frac{1}{\text{d}}} \approx \frac{10 \text{d}}{\text{d}}.
\]

<|ref|>sub_title<|/ref|><|det|>[[76, 622, 567, 641]]<|/det|>
4. Aussagen über die natürliche Logarithmusfunktion 

<|ref|>table<|/ref|><|det|>[[76, 649, 890, 837]]<|/det|>
<table><tr><td>Welche der folgenden Aussagen sind wahr und welche falsch?</td><td>wahr</td><td>falsch</td></tr><tr><td>a) Es gilt \(\ln(e) = 1\).</td><td>●</td><td>○</td></tr><tr><td>b) Es gilt \(\ln(8)/\ln(2) = 3\).</td><td>●</td><td>○</td></tr><tr><td>c) Für alle \(x \in \mathbb{R}^+\) gilt \(\exp(\ln(x)) = x\).</td><td>●</td><td>○</td></tr><tr><td>d) Ist \(f(x) = \ln(|x|)\), dann gilt \(f'(-2) = -0.5\).</td><td>●</td><td>○</td></tr><tr><td>e) Die Funktion \(\ln : \mathbb{R}^+ \to \mathbb{R}\) ist *bijektiv*.</td><td>●</td><td>○</td></tr><tr><td>f) Es gilt \(\ln(\exp(\sqrt{3})) \in \mathbb{Q}\).</td><td>○</td><td>●</td></tr></table>