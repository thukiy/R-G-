f) Mit Hilfe der Summen-Regel, der Faktor-Regel, der Ketten-Regel und der Exponential-Regel erhalten wir

$$
\begin{aligned}
\underline{\underline{f^{\prime}(l)}} & =\left(3 \cdot 2^{-\frac{l}{9}}+4\right)^{\prime}=3 \cdot\left(2^{-\frac{1}{9} \cdot l}\right)^{\prime}+(4)^{\prime}=3 \cdot\left(-\frac{1}{9} \cdot l\right)^{\prime} \cdot \ln (2) \cdot 2^{-\frac{1}{9} \cdot l}+0 \\
& =3 \cdot\left(-\frac{1}{9}\right) \cdot \ln (2) \cdot 2^{-\frac{l}{9}}=\underline{\underline{-\frac{\ln (2)}{3} \cdot 2^{-\frac{l}{9}}}}
\end{aligned}
$$

# 3. Ausbreitung des Corona-Virus 

Wir betrachten einen Tag im Frühling 2020, an welchem in der Schweiz insgesamt $N_{\mathrm{r}}=3^{\prime} 245$ bestätigte Ansteckungen mit dem Corona-Virus registriert sind und $A_{\mathrm{r}}=227 / \mathrm{d}$ Neuansteckungen gemeldet werden. Wenn man von einem exponentiellen Wachstum ausgeht, dann folgt die Gesamtzahl bestätige Ansteckungen einer verallgemeinerten Exponentialfunktion der Form
$N(t)=N_{0} \cdot a^{\frac{t-t_{0}}{\Sigma}}$.
Die Anzahl Neuansteckungen ist die Zuwachs-Rate
$A(t)=\dot{N}(t)=\frac{\ln (a)}{\Sigma} \cdot N(t)$.
Für die Werte am betrachteten Tag gilt demanch in guter Näherung

$$
A_{\mathrm{r}} \approx \frac{\ln (a)}{\Sigma} \cdot N_{\mathrm{r}} \quad \cdot \frac{\Sigma}{A_{\mathrm{r}}}
$$

Daraus und durch Einsetzen der Basis $a=2$ können wir die Zeitspanne $\Sigma$ berechnen, in welcher eine Verdopplung der Ansteckungen zu erwarten ist. Wir erhalten
$\Sigma \approx \ln (a) \cdot \frac{N_{\mathrm{r}}}{A_{\mathrm{r}}} \approx \ln (2) \cdot \frac{3^{\prime} 245}{227 \frac{1}{d}} \approx \underline{\underline{10 \mathrm{~d}}}$.

## 4. Aussagen über die natürliche Logarithmusfunktion

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) Es gilt $\ln (\mathrm{e})=1$. | $\bullet$ | $\bigcirc$ |
| b) Es gilt $\ln (8) / \ln (2)=3$. | $\bullet$ | $\bigcirc$ |
| c) Für alle $x \in \mathbb{R}^{+}$gilt $\exp (\ln (x))=x$. | $\bullet$ | $\bigcirc$ |
| d) Ist $f(x)=\ln (|x|)$, dann gilt $f^{\prime}(-2)=-0.5$. | $\bullet$ | $\bigcirc$ |
| e) Die Funktion $\ln : \mathbb{R}^{+} \rightarrow \mathbb{R}$ ist bijektiv. | $\bullet$ | $\bigcirc$ |
| f) Es gilt $\ln (\exp (\sqrt{3})) \in \mathbb{Q}$. | $\bigcirc$ | $\bullet$ |