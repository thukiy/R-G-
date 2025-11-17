# --- PAGE page_1 ---

# -`sleq`j_rr ?1_9 Computational and Data Science BSc HS 2023 

## Lösungen

Mathematik 1

## 1. Aussagen über die natürliche Exponentialfunktion

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :--: | :--: |
| a) Es gilt $\exp (1)=2.718^{\prime} 3$. | $\bigcirc$ | $\bullet$ |
| b) Es gilt $\exp ^{\prime}(x)=\mathrm{e}^{x}$. | $\bullet$ | $\bigcirc$ |
| c) Es gilt $\exp \left(10^{\prime} 000\right)=\exp ^{10}(10)$. | $\bigcirc$ | $\bullet$ |
| d) Für alle $x, y \in \mathbb{R}$ gilt $\exp (x-y)=\exp (x) / \exp (y)$. | $\bullet$ | $\bigcirc$ |

## 2. Ableitung von Exponentialfunktionen

Wir berechnen jeweils die Ableitung der angegebenen Funktion.
a) Mit Hilfe der Exponential-Regel erhalten wir

$$
\underline{\underline{f^{\prime}(x)}}=\left(2^{x}\right)^{\prime}=\underline{\underline{\ln (2) \cdot 2^{x}}}
$$

b) Mit Hilfe der Summen-Regel und der Exponential-Regel erhalten wir

$$
\underline{\underline{f^{\prime}(x)}}=\left(3^{x}-\mathrm{e}^{x}\right)^{\prime}=\left(3^{x}\right)^{\prime}-\left(\mathrm{e}^{x}\right)^{\prime}=\underline{\underline{\ln (3) \cdot 3^{x}-\mathrm{e}^{x}}}
$$

c) Mit Hilfe der Faktor-Regel und der Exponential-Regel erhalten wir

$$
\underline{\underline{f(t)}}=\left(3 \cdot 5^{t}\right)^{\prime}=3 \cdot\left(5^{t}\right)^{\prime}=\underline{\underline{3 \cdot \ln (5) \cdot 5^{t}}}
$$

d) Mit Hilfe der Summen-Regel sowie der Exponential-Regel und Monom-Regel erhalten wir

$$
\underline{\underline{f^{\prime}(z)}}=\left(w^{z}+z^{w}\right)^{\prime}=\left(w^{z}\right)^{\prime}+\left(z^{w}\right)^{\prime}=\underline{\underline{\ln (w) \cdot w^{z}+w \cdot z^{w-1}}}
$$

e) Mit Hilfe der Ketten-Regel und der Exponential-Regel erhalten wir

$$
\underline{\underline{f^{\prime}(q)}}=\left(u^{2 q}\right)^{\prime}=(2 q)^{\prime} \cdot \ln (u) \cdot u^{2 q}=\underline{\underline{2 \ln (u) u^{2 q}}}
$$

# --- PAGE page_2 ---

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

# --- PAGE page_3 ---

# 5. Ableitung von Logarithmusfunktionen 

Wir berechnen jeweils die Ableitung der angegebenen Funktion.
a) Mit Hilfe der Faktor-Regel und der Logarithmus-Regel erhalten wir

$$
\underline{\underline{f^{\prime}(x)}=(2 \ln (x))^{\prime}=2 \cdot \ln ^{\prime}(x)=2 \cdot \frac{1}{x}=\frac{2}{\underline{x}}}
$$

b) Mit Hilfe der Faktor-Regel und der Logarithmus-Regel erhalten wir

$$
\underline{\underline{f^{\prime}(x)}=\left(6 \log _{7}(x)+1\right)^{\prime}=6 \cdot \frac{1}{x \cdot \ln (7)}+0=\frac{6}{\underline{x \cdot \ln (7)}}}
$$

c) Mit Hilfe der Ketten-Regel und der Logarithmus-Regel erhalten wir

$$
\begin{aligned}
\underline{\underline{f^{\prime}(x)}} & =\left(\log _{2}(2 x+1)\right)^{\prime}=(2 x+1)^{\prime} \cdot \log _{2}^{\prime}(2 x+1)=(2+0) \cdot \frac{1}{(2 x+1) \cdot \ln (2)} \\
& =\underline{\underline{(2 x+1) \cdot \ln (2)}}
\end{aligned}
$$

d) Mit Hilfe der Summen-Regel und der Logarithmus-Regel erhalten wir

$$
\underline{\underline{f^{\prime}(x)}}=\left(\log _{5}(x)+\log _{x}(5)\right)^{\prime}=\left(\log _{5}(x)\right)^{\prime}+\left(\log _{x}(5)\right)^{\prime}=\underline{\underline{x \ln (5)}-\frac{\log _{x}(5)}{x \ln (x)}}
$$

e) Mit Hilfe der Ketten-Regel und der Logarithmus-Regel erhalten wir

$$
\begin{aligned}
\underline{\underline{f^{\prime}(x)}} & =\left(\log _{a}(b x+c)\right)^{\prime}=(b x+c)^{\prime} \cdot \log _{a}^{\prime}(b x+c)=(b+0) \cdot \frac{1}{(b x+c) \cdot \ln (a)} \\
& =\underline{\underline{b \over(b x+c) \cdot \ln (a)}}
\end{aligned}
$$

f) Mit Hilfe der Ketten-Regel der Logarithmus-Regel und der Betrags-Regel erhalten wir

$$
\underline{\underline{f^{\prime}(x)}=(\ln (|x|))^{\prime}=|x|^{\prime} \cdot \ln ^{\prime}(|x|)=\operatorname{sgn}(x) \cdot \frac{1}{|x|}=\frac{1}{\operatorname{sgn}(x) \cdot|x|}=\frac{1}{\underline{x}}}
$$

## 6. Diverse Ableitungen

Wir berechnen jeweils die Ableitung der angegebenen Funktion.
a) Wir betrachten die Funktion

$$
f(x)=\mathrm{e}^{-x}
$$

Mit Hilfe der Ketten-Regel erhalten wir

$$
\underline{\underline{f^{\prime}(x)}}=\mathrm{e}^{-x} \cdot(-x)^{\prime}=\mathrm{e}^{-x} \cdot(-1)=\underline{-\mathrm{e}^{-x}}
$$

# --- PAGE page_4 ---

b) Wir betrachten die Funktion

$$
f(x)=x \cdot \mathrm{e}^{x}
$$

Mit Hilfe der Produkt-Regel erhalten wir

$$
\underline{f^{\prime}(x)}=x^{\prime} \cdot \mathrm{e}^{x}+x \cdot\left(\mathrm{e}^{x}\right)^{\prime}=1 \cdot \mathrm{e}^{x}+x \cdot \mathrm{e}^{x}=\underline{(1+x) \cdot \mathrm{e}^{x}}
$$

c) Wir betrachten die Funktion

$$
f(x)=(x+2) \cdot \mathrm{e}^{x}
$$

Mit Hilfe der Produkt-Regel erhalten wir

$$
\begin{aligned}
\underline{f^{\prime}(x)} & =(x+2)^{\prime} \cdot \mathrm{e}^{x}+(x+2) \cdot\left(\mathrm{e}^{x}\right)^{\prime}=(1+0) \cdot \mathrm{e}^{x}+(x+2) \cdot \mathrm{e}^{x}=(1+(x+2)) \cdot \mathrm{e}^{x} \\
& =\underline{(x+3) \cdot \mathrm{e}^{x}}
\end{aligned}
$$

d) Wir betrachten die Funktion

$$
f(x)=\mathrm{e}^{-x^{2}}
$$

Mit Hilfe der Ketten-Regel erhalten wir

$$
\underline{f^{\prime}(x)}=\mathrm{e}^{-x^{2}} \cdot\left(-x^{2}\right)^{\prime}=\mathrm{e}^{-x^{2}} \cdot\left(-2 \cdot x^{2-1}\right)=\underline{-2 \cdot x \cdot \mathrm{e}^{-x^{2}}}
$$

e) Wir betrachten die Funktion

$$
f(x)=(x+1) \cdot 2^{x}
$$

Mit Hilfe der Produkt-Regel erhalten wir

$$
\begin{aligned}
\underline{f^{\prime}(x)} & =(x+1)^{\prime} \cdot 2^{x}+(x+1) \cdot\left(2^{x}\right)^{\prime}=(1+0) \cdot 2^{x}+(x+1) \cdot \ln (2) \cdot 2^{x} \\
& =\underline{(1+\ln (2) \cdot(x+1)) \cdot 2^{x}}
\end{aligned}
$$

f) Wir betrachten die Funktion

$$
f(x)=(x+1) \cdot 3^{-x^{2}}
$$

Mit Hilfe der Produkt-Regel und der Ketten-Regel erhalten wir

$$
\begin{aligned}
\underline{f^{\prime}(x)} & =(x+1)^{\prime} \cdot 3^{-x^{2}}+(x+1) \cdot\left(3^{-x^{2}}\right)^{\prime}=(1+0) \cdot 3^{-x^{2}}+(x+1) \cdot \ln (3) \cdot 3^{-x^{2}} \cdot\left(-x^{2}\right)^{\prime} \\
& =3^{-x^{2}}+(x+1) \cdot \ln (3) \cdot 3^{-x^{2}} \cdot\left(-2 \cdot x^{2-1}\right)=(1+(x+1) \cdot \ln (3) \cdot(-2 x)) \cdot 3^{-x^{2}} \\
& =\underline{(1-2 \cdot \ln (3) \cdot x \cdot(x+1)) \cdot 3^{-x^{2}}}
\end{aligned}
$$

# --- PAGE page_5 ---

# 7. Diverse Ableitungen berechnen mit Python/Sympy 

Wir berechnen die Ableitungen aus Aufgabe 6 mit Python/Sympy. Dazu implementieren wir den folgenden Code, den wir für jede Teilaufgabe modifizieren.

```
# Python initialisieren:
import IPython.display as dp;
import sympy as sp;
# Python konfigurieren:
sp.init_printing();
x=sp.symbols('x');
# Parameter:
f=...;
# Berechnungen:
fs=sp.simplify(sp.diff(f,x));
# Ausgabe:
dp.display(f);
dp.display(fs);
```

a) Wir modifizieren den Code.

```
# Parameter:
f=sp.exp(-x);
```

Gemäss Ausgabe erhalten wir die Ableitung

$$
f^{\prime}(x)=-\mathrm{e}^{-x}
$$

b) Wir modifizieren den Code.

```
# Parameter:
f=x*sp.exp(x);
```

Gemäss Ausgabe erhalten wir die Ableitung

$$
\underline{f^{\prime}(x)}=(x+1) \cdot \mathrm{e}^{x}
$$

c) Wir modifizieren den Code.

```
# Parameter:
f=(x+2)*sp.exp(x);
```

Gemäss Ausgabe erhalten wir die Ableitung

$$
\underline{f^{\prime}(x)}=(x+3) \cdot \mathrm{e}^{x}
$$

d) Wir modifizieren den Code.

```
# Parameter:
f=sp.exp(-x**2);
```

Gemäss Ausgabe erhalten wir die Ableitung

$$
\underline{\dot{f}(t)}=-2 \cdot x \cdot \mathrm{e}^{-x^{2}}
$$

e) Wir modifizieren den Code.

# --- PAGE page_6 ---

\# Parameter:
$f=(x+1) * 2 * * x ;$
Gemäss Ausgabe erhalten wir die Ableitung
$\underline{f^{\prime}(s)=2^{x} \cdot((x+1) \cdot \ln (2)+1)}$.
f) Wir modifizieren den Code.
\# Parameter:
$f=(x+1) * 3 * *(-x * * 2)$;
Gemäss Ausgabe erhalten wir die Ableitung
$\underline{f^{\prime}(x)=3^{-x^{2}} \cdot(-x \cdot(x+1) \cdot \ln (9)+1)}$.

# 8. Diverse Ableitungen 

Wir berechnen jeweils die Ableitung der angegebenen Funktion.
a) Wir betrachten die Funktion
$f(x)=5^{x^{3}-\sqrt{x}+7}$.
Mit Hilfe der Ketten-Regel erhalten wir
$\underline{f^{\prime}(x)}=\left(x^{3}-\sqrt{x}+7\right)^{\prime} \cdot \ln (5) \cdot 5^{x^{3}-\sqrt{x}+7}=\underbrace{\left(3 x^{2}-\frac{1}{2 \sqrt{x}}\right) \cdot \ln (5) \cdot 5^{x^{3}-\sqrt{x}+7}}_{\text {. }}$
b) Wir betrachten die Funktion
$f(x)=\log _{2}\left(9 x^{2}-4\right)$.
Mit Hilfe der Ketten-Regel erhalten wir

$$
\begin{aligned}
\underline{f^{\prime}(x)} & =\left(9 x^{2}-4\right)^{\prime} \cdot \log _{2}^{\prime}\left(9 x^{2}-4\right)=\left(9 \cdot 2 x^{2-1}-0\right) \cdot \frac{1}{\ln (2) \cdot\left(9 x^{2}-4\right)} \\
& =\underline{\frac{18 x}{\ln (2) \cdot\left(9 x^{2}-4\right)}}
\end{aligned}
$$

c) Wir betrachten die Funktion

$$
\begin{aligned}
f(x) & =\sqrt[4]{\ln \left(x^{256}\right)}=\sqrt[4]{\ln \left(|x|^{256}\right)}=\sqrt[4]{256 \cdot \ln (|x|)}=\sqrt[4]{256} \cdot \sqrt[4]{\ln (|x|)}=4 \cdot \sqrt[4]{\ln (|x|)} \\
& =4 \cdot(\ln (|x|))^{\frac{1}{4}}
\end{aligned}
$$

Mit Hilfe der Ketten-Regel erhalten wir
$\underline{f^{\prime}(x)}=4 \cdot \frac{1}{4} \cdot(\ln (|x|))^{\frac{1}{4}-1} \cdot(\ln (|x|))^{\prime}=(\ln (|x|))^{-\frac{3}{4}} \cdot \frac{1}{x}=\frac{1}{x \cdot \sqrt[4]{\ln ^{3}(|x|)}}$.

# --- PAGE page_7 ---

d) Wir betrachten die Funktion

$$
f(x)=\frac{1}{1+\mathrm{e}^{-x}}
$$

Mit Hilfe der Reziproken-Regel erhalten wir

$$
\begin{aligned}
& \xrightarrow{f^{\prime}(x)}=-\frac{\left(1+\mathrm{e}^{-x}\right)^{\prime}}{\left(1+\mathrm{e}^{-x}\right)^{2}}=-\frac{0-\mathrm{e}^{-x}}{\left(1+\mathrm{e}^{-x}\right)^{2}}=\frac{\mathrm{e}^{-x}}{\left(1+\mathrm{e}^{-x}\right)^{2}}=\frac{\mathrm{e}^{2 x} \cdot \mathrm{e}^{-x}}{\mathrm{e}^{2 x} \cdot\left(1+\mathrm{e}^{-x}\right)^{2}} \\
& =\frac{\mathrm{e}^{2 x-x}}{\left(\mathrm{e}^{x}\right)^{2} \cdot\left(1+\mathrm{e}^{-x}\right)^{2}}=\frac{\mathrm{e}^{x}}{\left(\mathrm{e}^{x} \cdot\left(1+\mathrm{e}^{-x}\right)\right)^{2}}=\frac{\mathrm{e}^{x}}{\left(\mathrm{e}^{x}+1\right)^{2}} .
\end{aligned}
$$

e) Wir betrachten die Funktion

$$
f(x)=\ln ^{\ln (x)}(x)=(\ln (x))^{\ln (x)}
$$

Mit Hilfe der Exponential-Regel erhalten wir

$$
\begin{aligned}
& \xrightarrow{f^{\prime}(x)}=\left(\ln ^{\prime}(x) \cdot \ln (\ln (x))+\ln ^{\prime}(x) \cdot \frac{\ln (x)}{\ln (x)}\right) \cdot \ln ^{\ln (x)}(x) \\
& =\left(\frac{1}{x} \cdot \ln (\ln (x))+\frac{1}{x} \cdot 1\right) \cdot \ln ^{\ln (x)}(x)=\frac{1}{x} \cdot(\ln (\ln (x))+1) \cdot \ln ^{\ln (x)}(x) .
\end{aligned}
$$

f) Wir betrachten die Funktion

$$
f(x)=\frac{2^{-\sqrt{|x|}}}{\ln (2)}
$$

Mit Hilfe der Ketten-Regel erhalten wir

$$
\begin{aligned}
& \xrightarrow{f^{\prime}(x)}=\frac{1}{\ln (2)} \cdot(-\sqrt{|x|})^{\prime} \cdot \ln (2) \cdot 2^{-\sqrt{|x|}}=-\frac{1}{2 \cdot \sqrt{|x|}} \cdot|x|^{\prime} \cdot 2^{-\sqrt{|x|}}=-\frac{\operatorname{sgn}(x)}{2 \cdot \sqrt{|x|}} \cdot 2^{-\sqrt{|x|}} \\
& =\underbrace{-\frac{\operatorname{sgn}(x)}{\sqrt{|x|}} \cdot 2^{-\sqrt{|x|}-1}}
\end{aligned}
$$

# 9. Diverse Ableitungen berechnen mit Python/Sympy 

Wir berechnen die Ableitungen aus Aufgabe 8 mit Python/Sympy. Dazu implementieren wir den folgenden Code, den wir für jede Teilaufgabe modifizieren.

```
# Python initialisieren:
import IPython.display as dp;
import sympy as sp;
# Python konfigurieren:
sp.init_printing();
x=sp.symbols('x',real=True);
# Parameter:
f=...;
# Berechnungen:
fs=sp.simplify(sp.diff(f,x));
# Ausgabe:
dp.display(f);
dp.display(fs);
```

# --- PAGE page_8 ---

a) Wir modifizieren den Code.
\# Parameter:
$f=5 * *(x * * 3-s p . s q r t(x)+7)$;
Gemäss Ausgabe erhalten wir die Ableitung
$f^{\prime}(x)=\frac{5^{-\sqrt{x}+x^{3}+7} \cdot\left(6 \cdot x^{\frac{5}{2}}-1\right) \cdot \ln (5)}{2 \cdot \sqrt{x}}$.
b) Wir modifizieren den Code.
\# Parameter:
$f=\operatorname{sp} \cdot \log (9 * x * * 2-4,2)$;
Gemäss Ausgabe erhalten wir die Ableitung
$f^{\prime}(x)=\frac{18 \cdot x}{\left(9 \cdot x^{2}-4\right) \cdot \ln (2)}$.
c) Wir modifizieren den Code.
\# Parameter:
$f=($ sp. $\log (x * * 256)) * *(1 / 4)$;
Gemäss Ausgabe erhalten wir die Ableitung
$f^{\prime}(x)=\frac{64.0}{x \cdot \ln ^{0.75}\left(x^{256}\right)}$.
d) Wir modifizieren den Code.
\# Parameter:
$f=1 /(1+\operatorname{sp} \cdot \exp (-x))$;
Gemäss Ausgabe erhalten wir die Ableitung
$f^{\prime}(x)=\frac{1}{4 \cdot \cosh ^{2}\left(\frac{x}{2}\right)}$.
e) Wir modifizieren den Code.
\# Parameter:
$f=($ sp. $\log (x)) * * \operatorname{sp} \cdot \log (x)$;
Gemäss Ausgabe erhalten wir die Ableitung
$f^{\prime}(x)=\frac{(\ln (\ln (x))+1) \cdot \ln ^{\ln (x)}(x)}{x}$.
f) Wir modifizieren den Code.
\# Parameter:
$f=2 * *(-\operatorname{sp.sqrt}(\operatorname{sp} \cdot \operatorname{Abs}(x))) / \operatorname{sp} \cdot \log (2)$;
$f^{\prime}(x)=\left\{\left.\begin{array}{c|c} 

$$
\begin{array}{c}
0 \\
-\frac{2^{-\sqrt{|x|}-1} \cdot x}{\left|x^{\frac{3}{2}}\right|} \\
\hline
\end{array} \right\rvert\, \begin{array}{l}
\text { sonst. }
\end{array}\right.$