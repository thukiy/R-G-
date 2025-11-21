# --- PAGE page_1 ---

# Übungsblatt Ana 6 

## 1. Funktionsgraphen verschieben

Wir modifizieren jeweils den Funktionsterm, so dass der Graph die verlangte Verschiebung erfährt.
a) Wir verschieben $f(x)=x^{2}$ um $\Delta y=3$ nach oben. Der modifizierte Funktionsterm lautet

$$
\underline{g(x)}=f(x)+\Delta y=f(x)+3=x^{2}+3
$$

b) Wir verschieben $f(x)=1 / x$ um $\Delta x=2$ nach rechts. Der modifizierte Funktionsterm lautet

$$
\underline{g(x)}=f(x-\Delta x)=f(x-2)=\underline{\underline{x-2}}
$$

c) Wir verschieben $f(x)=2^{x}$ um $\Delta x=3$ nach links. Der modifizierte Funktionsterm lautet

$$
\underline{g(x)}=f(x+\Delta x)=f(x+3)=\underline{\underline{2^{x+3}}}
$$

d) Wir verschieben $f(x)=\sqrt{x-2}$ um $\Delta y=2$ nach unten. Der modifizierte Funktionsterm lautet

$$
\underline{g(x)}=f(x)-\Delta y=\underline{\sqrt{x-2}-2}
$$

e) Wir verschieben $f(x)=x^{2} \cdot \sin (x-3)$ um $\Delta x=4$ nach links. Der modifizierte Funktionsterm lautet

$$
\underline{g(x)}=f(x+\Delta x)=f(x+4)=(x+4)^{2} \cdot \sin (x+4-3)=\underline{(x+4)^{2} \cdot \sin (x+1)}
$$

f) Wir verschieben $f(x)=3^{x+2} \cdot \cosh (2 x)$ um $\Delta x=1$ nach rechts. Der modifizierte Funktionsterm lautet

$$
\underline{g(x)}=f(x-\Delta x)=f(x-1)=3^{x-1+2} \cdot \cosh (2 \cdot(x-1))=\underline{3^{x+1} \cdot \cosh (2 x-2)}
$$

# --- PAGE page_2 ---

# 2. Parität von Funktionen 

Wir bestimmen jeweils die Parität des angegebenen Funktionsterms.
a) Wir betrachten $f(x)=x^{2}$. Es gilt

$$
\underline{f(-x)}=(-x)^{2}=(-1)^{2} \cdot x^{2}=1 \cdot x^{2}=x^{2}=\underline{f(x)}
$$

Die Funktion hat demnach positive Parität.
b) Wir betrachten $f(x)=1 / x$. Es gilt

$$
\underline{f(-x)}=\underline{1}=-\underline{1}=\underline{-f(x)}
$$

Die Funktion hat demnach negative Parität.
c) Wir betrachten $f(x)=-2^{|x|}$. Es gilt

$$
\underline{f(-x)}=-2^{|-x|}=-2^{|x|}=\underline{f(x)}
$$

Die Funktion hat demnach positive Parität.
d) Wir betrachten $f(x)=\sin (3 x)$. Es gilt

$$
\underline{f(-x)}=\sin (3 \cdot(-x))=\sin (-3 x)=-\sin (3 x)=\underline{-f(x)}
$$

Die Funktion hat demnach negative Parität.
e) Wir betrachten $f(x)=x \cdot \cos (5 x)$. Es gilt

$$
\underline{f(-x)}=(-x) \cdot \cos (5 \cdot(-x))=-x \cdot \cos (-5 x)=-x \cdot \cos (5 x)=\underline{-f(x)}
$$

Die Funktion hat demnach negative Parität.
f) Wir betrachten $f(x)=\cosh (x) \cdot \sinh \left(x^{2}\right)$. Es gilt

$$
\underline{f(-x)}=\cosh (-x) \cdot \sinh \left((-x)^{2}\right)=\cosh (x) \cdot \sinh \left(x^{2}\right)=\underline{f(x)}
$$

Die Funktion hat demnach positive Parität.

## 3. Aussagen über lineare Funktionen

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) Der Graph einer linearen Funktion ist in jedem Fall eine Gerade. | $\bullet$ | $\bigcirc$ |
| b) Jede lineare Funktion ist injektiv. | $\bigcirc$ | $\bullet$ |
| c) Eine lineare Funktion ist genau dann bijektiv, wenn ihre Steigung nicht <br> verschwindet. | $\bullet$ | $\bigcirc$ |
| d) Der Graph jeder linearen Funktion schneidet die $y$-Achse. | $\bullet$ | $\bigcirc$ |

# --- PAGE page_3 ---

# 4. Umkehrfunktion einer linearen Funktion 

Wir betrachten $m \in \mathbb{R} \backslash\{0\}, q \in \mathbb{R}$ und die lineare Funktion

$$
\begin{aligned}
f: \mathbb{R} & \rightarrow \mathbb{R} \\
x & \mapsto f(x):=m \cdot x+q
\end{aligned}
$$

a) Um die Umkehrfunktion von $f$ zu berechnen, bestimmen wir die Lösung der Gleichung

$$
\begin{array}{rlrl}
y & =f(x)=m \cdot x+q & & -q \\
\Leftrightarrow & y-q & =m \cdot x & & : m \\
\Leftrightarrow & \frac{y-q}{m} & =x
\end{array}
$$

Daraus erhalten wir

$$
f^{-1}(y)=\frac{y-q}{m}=\frac{1}{m} \cdot y-\frac{q}{m}
$$

b) Wir zeigen mehrere Varianten, um zu begründen, warum die Umkehrfunktion von $f$ nur für $m \neq 0$ existiert.
Variante 1: Für $m=0$ würde gelten

$$
f(x)=m \cdot x+q=0 \cdot x+q=0+q=q \equiv \text { konst. }
$$

Das bedeutet, für jedes $x \in \mathbb{R}$ hätte der Funktionswert $f(x)$ den gleichen Wert $q$. Die Funktion $f$ wäre demnach nicht injektiv, somit nicht bijektiv und folglich nicht umkehrbar.
Variante 2: Für $m=0$ wäre der Graph von $f$ eine horizontale Gerade im $x$ - $y$-Diagramm. Somit wäre $f$ offensichtlich nicht bijektiv und folglich nicht umkehrbar.
Variante 3: Um die Umkehrfunktion von $f$ zu berechnen, haben wir in (15) durch $m$ dividiert. Diese Division wäre für $m=0$ nicht möglich, was die Existenz der Umkehrfunktion in diesem Fall ausschliesst.
c) Für den $x$-Achsabschnitt $p$ von $f$ gilt
$f(p)=0$.
Daraus und durch Einsetzen von (17) folgt
$\underline{p}=f^{-1}(0)=\frac{0-q}{m}=\frac{-q}{m}=\underline{\underline{-m}}$.
d) Wir betrachten die lineare Funktion
$f(x)=3 \cdot x+5$
mit den Grund-Form-Parametern $m=3$ und $q=5$. Gemäss (17) und (20) sind die Umkehrfunktion und der $x$-Achsabschnitt

$$
\begin{aligned}
\underline{f^{-1}(y)} & =\frac{y-q}{m}=\underline{\underline{y-5}}=\frac{1}{3} \cdot y-\frac{5}{3} \\
\underline{p} & =-\frac{q}{m}=\underline{\underline{-\frac{5}{3}}}
\end{aligned}
$$

# --- PAGE page_4 ---

# 5. Arbeiten mit linearen Funktionen 

Wir bestimmen jeweils das gesuchte Objekt.
a) Gesucht ist eine lineare Funktion mit Steigung $m=-2$, deren Graph durch den Punkt $\left(x_{0} ; y_{0}\right) \backslash(1 ;-14$ v\&rläuft. Wir erhalten
wir
$\underline{\underline{f(x)}}=m \cdot\left(x-x_{0}\right)+y_{0}=-2 \cdot(x-1)+(-14)=-2 \cdot x+2-14=\underline{\underline{-2 \cdot x-12}}$
b) Gesucht ist eine lineare Funktion, deren Bildmenge nicht ganz $\mathbb{R}$ umfasst und deren Graph durch den Punkt $(-3 ; 5)$ verläuft. Eine lineare Funktion ist genau dann nicht surjektiv, wenn ihre Steigung verschwindet, d.h. wenn $m=0$. Eine solche Funktion ist konstant. Wir erhalten
$\underline{\underline{f(x)}}=f(-3)=\underline{\underline{5}}$
c) Wir suchen den Schnittpunkt $\left(x_{\mathrm{T}} ; y_{\mathrm{T}}\right)$ der Geraden durch die Punkte $\left(x_{1} ; y_{1}\right)=(0 ;-10)$ und $\left(x_{2} ; y_{2}\right)=(-1 ;-14)$ mit der Geraden durch die Punkte $\left(x_{3} ; y_{3}\right)=(-8 ; 13)$ und $\left(x_{4} ; y_{4}\right)=(7 ;-2)$. Mit Hilfe der Zwei-Punkt-Form für lineare Funktionen können wir die beiden Geraden beschreiben als Graphen der linearen Funktionen

$$
\begin{aligned}
f(x) & =m \cdot\left(x-x_{1}\right)+y_{1}=\frac{y_{2}-y_{1}}{x_{2}-x_{1}} \cdot\left(x-x_{1}\right)+y_{1}=\frac{-14-(-10)}{-1-0} \cdot(x-0)+(-10) \\
& =\frac{-14+10}{-1} \cdot x-10=4 \cdot x-10 \\
\tilde{f}(x) & =\tilde{m} \cdot\left(x-x_{0}\right)+y_{3}=\frac{y_{4}-y_{3}}{x_{4}-x_{3}} \cdot\left(x-x_{3}\right)+y_{3}=\frac{-2-13}{7-(-8)} \cdot(x-(-8))+13 \\
& =\frac{-15}{15} \cdot(x+8)+13=-x-8+13=-x+5
\end{aligned}
$$

Es muss gelten

$$
\begin{aligned}
& f\left(x_{\mathrm{T}}\right)=\tilde{f}\left(x_{\mathrm{T}}\right) \\
& \Leftrightarrow \quad 4 \cdot x_{\mathrm{T}}-10=-x_{\mathrm{T}}+5 \quad \mid+x_{\mathrm{T}}+10 \\
& \Leftrightarrow \quad 5 \cdot x_{\mathrm{T}}=15 \quad \mid: 5 . \\
& \Leftrightarrow \quad x_{\mathrm{T}}=\frac{15}{5}=3
\end{aligned}
$$

und
$y_{\mathrm{T}}=f\left(x_{\mathrm{T}}\right)=f(3)=4 \cdot 3-10=12-10=2$.
Der Schnittpunkt der Geraden ist demnach

$$
\left(x_{\mathrm{T}} ; y_{\mathrm{T}}\right)=(3 ; 2)
$$

d) Gesucht ist eine lineare Funktion mit Steigungswinkel $\alpha=60^{\circ}$, deren Graph die $x$-Achse bei $x_{0}=1 / \sqrt{3}$ schneidet. Der Graph dieser Funktion hat demnach die Steigung
$m=\tan (\alpha)=\tan \left(60^{\circ}\right)=\sqrt{3}$

# --- PAGE page_5 ---

und verläuft durch den Punkt $\left(x_{0} ; y_{0}\right)=(1 / \sqrt{ } 3 ; 0)$. Wir erhalten

$$
\underline{\underline{f(x)}}=m \cdot\left(x-x_{0}\right)+y_{0}=\sqrt{3} \cdot\left(x-\frac{1}{\sqrt{3}}\right)+0=\underline{\sqrt{3} \cdot x-1}
$$

# 6. Aussagen über eine Funktion 

Wir betrachten die Funktion

$$
\begin{aligned}
f: \mathbb{R} & \rightarrow \mathbb{R} \\
z & \mapsto f(z):=2 \cdot(2-z)
\end{aligned}
$$

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :--: |
| a) Die Funktion $f$ ist eine lineare Funktion. | $\bullet$ | $\bigcirc$ |
| b) Der Graph von $f$ ist eine Gerade mit Steigung 2. | $\bigcirc$ | $\bullet$ |
| c) Es gilt $f(0)=2$. | $\bigcirc$ | $\bullet$ |
| d) Der Graph von $f$ verläuft durch den Punkt $(-2 ; 8)$. | $\bullet$ | $\bigcirc$ |
| e) Die Bildmenge von $f$ ist ganz $\mathbb{R}$. | $\bullet$ | $\bigcirc$ |
| f) Die Gleichung $f(z)=z$ hat keine Lösung. | $\bigcirc$ | $\bullet$ |

## 7. Preise eines Taxis

Wir betrachten ein Taxi, dessen Taxometer so eingestellt ist, dass jede Fahrt mindestens $P_{0}=$ 8.00 CHF kostet und pro gefahrenen Kilometer noch $\Delta K=2.50 \mathrm{CHF}$ hinzukommen.
a) Wir beschreiben den Fahrpreis $P$ in Abhängigkeit der Fahrstrecke $s$ durch eine lineare Funktion mit Funktionsterm der Form
$P(s)=m \cdot s+q$.
Offensichtlich soll gelten
$P_{0}=P(0)=m \cdot 0+q=0+q=q$.
Für die Steigung muss gelten
$m=\frac{\Delta P}{\Delta s}=\frac{2.50 \mathrm{CHF}}{1 \mathrm{~km}}=2.50 \frac{\mathrm{CHF}}{\mathrm{km}} \cdot(39)$ Daraus erhalten wir
$\underline{\underline{P(s)}}=m \cdot s+q=\underline{\underline{2.50 \frac{\mathrm{CHF}}{\mathrm{~km}} \cdot s+8.00 \mathrm{CHF}} .}$
b) Die Fahrt über eine Strecke von $s_{\mathrm{b}} \approx 14.0 \mathrm{~km}$ von Chur nach Landquart kostet

$$
\begin{aligned}
\underline{\underline{P_{\mathrm{b}}}} & =P\left(s_{\mathrm{b}}\right) \approx P(14.0 \mathrm{~km})=2.50 \frac{\mathrm{CHF}}{\mathrm{~km}} \cdot 14.0 \mathrm{~km}+8.00 \mathrm{CHF}=35.0 \mathrm{CHF}+8.00 \mathrm{CHF} \\
& =\underline{\underline{43.00 \mathrm{CHF}}}
\end{aligned}
$$

# --- PAGE page_6 ---

c) Wenn dafür ein Budget von $B \approx 68.00 \mathrm{CHF}$ zur Verfügung steht, dann kann mit dem Taxi eine Strecke gefahren werden von

$$
\underline{\underline{s_{\mathrm{c}}}}=K^{-1}(B)=\frac{B-q}{m} \approx \frac{68.00 \mathrm{CHF}-8.00 \mathrm{CHF}}{2.50 \frac{\mathrm{CHF}}{\mathrm{~km}}}=\underline{\underline{24.0 \mathrm{~km}}}
$$

# 8. Aussagen über eine lineare Funktion 

Wir betrachten die lineare Funktion

$$
\begin{aligned}
h: \mathbb{R} & \rightarrow \mathbb{R} \\
t & \mapsto h(t):=3 \cdot(t-5)+9
\end{aligned}
$$

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) Der Graph von $h$ ist eine Gerade mit Steigung 3. | $\bullet$ | $\bigcirc$ |
| b) Es gilt $h(2)=0$. | $\bullet$ | $\bigcirc$ |
| c) Der Graph von $h$ verläuft durch den Punkt $(-5 ; 9)$. | $\bigcirc$ | $\bullet$ |
| d) Der Graph von $h$ schneidet die $y$-Achse bei $q=-6$. | $\bullet$ | $\bigcirc$ |
| e) Die Funktion $h$ ist bijektiv. | $\bullet$ | $\bigcirc$ |

## 9. Notenskala einer Prüfung

Wir betrachten eine Mathematik-Prüfung, für welche eine lineare Notenskala festgelegt werden soll, so dass $p_{1}=0$ Punkte mit der Note $N_{1}=1$ und $p_{2}=60$ Punkte mit der Note $N_{2}=6$ bewertet werden.
a) Wir beschreiben die Notenskala durch eine lineare Funktion. Deren Steigung ist

$$
m=\frac{\Delta N}{\Delta p}=\frac{N_{2}-N_{1}}{p_{2}-p_{1}}=\frac{6-1}{60-0}=\frac{5}{60}=\frac{1}{12}
$$

Mit Hilfe der Zwei-Punkt-Form für linare Funktionen erhalten wir

$$
\underline{\underline{N(p)}}=m \cdot\left(p-p_{1}\right)+N_{1}=\frac{1}{12} \cdot(p-0)+1=\underline{\underline{\frac{1}{12}} \cdot p+1}
$$

b) Eine Punktzahl von $p_{\mathrm{b}}=43$ wird bewertet mit der Note

$$
\underline{\underline{N_{\mathrm{b}}}}=N\left(p_{\mathrm{b}}\right)=N(43)=\frac{1}{12} \cdot 43+1 \approx \underline{\underline{4.58}}
$$

c) Für eine genügende Note $N_{\mathrm{c}}=4$ muss mindestens eine Punktzahl erzielt werden von

$$
\begin{aligned}
\underline{\underline{p_{\mathrm{c}}}} & =N^{-1}\left(N_{\mathrm{c}}\right)=\frac{1}{m} \cdot N_{\mathrm{c}}-\frac{q}{m}=\frac{1}{\frac{1}{12}} \cdot 4-\frac{1}{\frac{1}{12}}=12 \cdot 4-12=12 \cdot(4-1)=12 \cdot 3 \\
& =\underline{\underline{36}}
\end{aligned}
$$

# --- PAGE page_7 ---

# 10. Aussagen über verallgemeinerte Exponentialfunktionen 

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :-- | :-- |
| a) Verallgemeinerte Exponentialfunktionen beschreiben jeweils die Bezie- <br> hung zwischen zwei Grössen in vielen Anwendungen aus Alltag, Natur- <br> wissenschaft, Technik und Wirtschaft. | $\bullet$ | $\bigcirc$ |
| b) Verallgemeinerte Exponentialfunktionen sind immer injektiv. | $\bullet$ | $\bigcirc$ |
| c) Verallgemeinerte Exponentialfunktionen sind immer strikt monoton. | $\bullet$ | $\bigcirc$ |
| d) Jede verallgemeinerte Exponentialfunktion hat eine Umkehrfunktion, so- <br> fern man die Zielmenge geschickt wählt. | $\bullet$ | $\bigcirc$ |
| e) Jede eigentliche Exponentialfunktion ist auch eine verallgemeinerte Expo- <br> nentialfunktion. | $\bullet$ | $\bigcirc$ |

## 11. Eigenschaften von verallgemeinerten Exponentialfunktionen

Seien $a \in \mathbb{R}^{+} \backslash\{1\}, \Sigma \in \mathbb{R} \backslash\{0\}, x_{0} \in \mathbb{R}, y_{0} \in \mathbb{R} \backslash\{0\}$ und $f$ die verallgemeinerte Exponentialfunktion

$$
\begin{aligned}
f: \mathbb{R} & \rightarrow \mathbb{R} \\
x & \mapsto f(x):=y_{0} \cdot a^{\frac{x-x_{0}}{\Sigma}}
\end{aligned}
$$

Wir beweisen die folgenden Eigenschaften von $f$ für alle $x, \Delta x \in \mathbb{R}$.
a) Es gilt

$$
\underline{\underline{f\left(x_{0}\right)}}=y_{0} \cdot a^{\frac{x_{0}-x_{0}}{\Sigma}}=y_{0} \cdot a^{\frac{0}{\Sigma}}=y_{0} \cdot a^{0}=y_{0} \cdot 1=\underline{\underline{y_{0}}}
$$

b) Für alle $x \in \mathbb{R}$ gilt

$$
\begin{aligned}
\underline{\underline{f(x+\Sigma)}} & =y_{0} \cdot a^{\frac{x+\Sigma-x_{0}}{\Sigma}}=y_{0} \cdot a^{\frac{\Sigma}{\Sigma}+\frac{x-x_{0}}{\Sigma}}=y_{0} \cdot a^{\frac{\Sigma}{\Sigma}} \cdot a^{\frac{x-x_{0}}{\Sigma}}=y_{0} \cdot a^{1} \cdot a^{\frac{x-x_{0}}{\Sigma}}=a \cdot y_{0} \cdot a^{\frac{x-x_{0}}{\Sigma}} \\
& =\underline{\underline{a \cdot f(x)}}
\end{aligned}
$$

c) Für alle $x \in \mathbb{R}$ gilt

$$
\begin{aligned}
\underline{\underline{f(x-\Sigma)}} & =y_{0} \cdot a^{\frac{x-\Sigma-x_{0}}{\Sigma}}=y_{0} \cdot a^{\frac{-\Sigma}{\Sigma}+\frac{x-x_{0}}{\Sigma}}=y_{0} \cdot a^{-\frac{\Sigma}{\Sigma}} \cdot a^{\frac{x-x_{0}}{\Sigma}}=y_{0} \cdot a^{-1} \cdot a^{\frac{x-x_{0}}{\Sigma}} \\
& =\frac{1}{a} \cdot y_{0} \cdot a^{\frac{x-x_{0}}{\Sigma}}=\frac{f(x)}{\underline{\underline{a}}}
\end{aligned}
$$

d) Für alle $x, \Delta x \in \mathbb{R}$ gilt

$$
\underline{\underline{f(x+\Delta x)}}=y_{0} \cdot a^{\frac{x+\Delta x-x_{0}}{\Sigma}}=y_{0} \cdot a^{\frac{\Delta x}{\Sigma}+\frac{x-x_{0}}{\Sigma}}=y_{0} \cdot a^{\frac{\Delta x}{\Sigma}} \cdot a^{\frac{x-x_{0}}{\Sigma}}=\underline{\underline{a^{\frac{\Delta x}{\Sigma}} \cdot f(x)}}
$$

# --- PAGE page_8 ---

# 12. Falten eines Papiers 

Wir betrachten ein rechteckiges Blatt Papier mit Dicke und Fläche gemäss

$$
\begin{aligned}
d_{0} & \approx 0.100 \mathrm{~mm}=1.00 \cdot 10^{-1} \cdot 10^{-3} \mathrm{~m}=1.00 \cdot 10^{-1-3} \mathrm{~m}=1.00 \cdot 10^{-4} \mathrm{~m} \\
A_{0} & \approx 1.00 \mathrm{~m}^{2}
\end{aligned}
$$

a) Das Papier werde in der Mitte gefaltet. Dabei werden die beiden Falt-Teile aufeinander gelegt und das Ganze als neues Blatt betrachtet. Dicke und Fläche des Papiers ändern beim Falten um die Faktoren

$$
\underline{a=2} \quad \text { bzw. } \quad \underline{b=\frac{1}{2}}
$$

b) Wir beschreiben die Entwicklungen der Dicke und der Fläche des Papiers bei wiederholtem Falten durch je eine verallgemeinerte Exponentialfunktion. Als unabhängige Variable verwenden wir dazu

$$
n: \equiv \text { Anzahl durchgeführte Faltungen. }
$$

Gemäss Situationsangaben legen wir sinnvollerweise die folgenden Parameter fest.

| Funktion: | RS: | RW: | BA: | SW: |
| :--: | :--: | :--: | :--: | :--: |
| Dicke: | $n_{0}=0$ | $d_{0} \approx 1.00 \cdot 10^{-4} \mathrm{~m}$ | $a=2$ | $\Sigma=1$ |
| Fläche: | $n_{0}=0$ | $A_{0} \approx 1.00 \mathrm{~m}^{2}$ | $b=1 / 2$ | $\Sigma=1$ |

Daraus erhalten wir die verallgemeinerten Exponentialfunktionen
Dicke: $\quad \underline{d(n)}=d_{0} \cdot a^{\frac{n-n_{0}}{\Sigma}}=d_{0} \cdot 2^{\frac{n-0}{1}}=d_{0} \cdot 2^{n} \approx \underline{1.00 \cdot 10^{-4} \mathrm{~m} \cdot 2^{n}}$
Fläche: $\quad \underline{A(n)}=A_{0} \cdot b^{\frac{n-n_{0}}{\Sigma}}=A_{0} \cdot\left(\frac{1}{2}\right)^{\frac{n-0}{1}}=A_{0} \cdot\left(\frac{1}{2}\right)^{n} \approx \underline{1.00 \mathrm{~m}^{2} \cdot \frac{1}{2^{n}}}$.
c) Es sei $n_{\mathrm{E}}$ die Anzahl durchzuführende Faltungen, bis die Dicke des Papiers die mittlere Distanz zwischen Erde und Mond von
$d_{\mathrm{E}} \approx 400 \cdot 10^{3} \mathrm{~km}=4.00 \cdot 10^{2} \cdot 10^{3} \cdot 10^{3} \mathrm{~m}=4.00 \cdot 10^{2+3+3} \mathrm{~m}=4.00 \cdot 10^{8} \mathrm{~m}$
übersteigt. Gemäss (58) gilt

$$
\begin{aligned}
d_{\mathrm{E}}=d\left(n_{\mathrm{E}}\right) & =d_{0} \cdot 2^{n_{\mathrm{E}}} & \mid: d_{0} \\
\Leftrightarrow & \frac{d_{\mathrm{E}}}{d_{0}} & =2^{n_{\mathrm{E}}} & \left\lvert\, \log _{2}(\ldots)\right.
\end{aligned}
$$

Daraus und durch Aufrunden auf die nächst grössere natürliche Zahl erhalten wir

$$
\begin{aligned}
\underline{n_{\mathrm{E}}} & =\left\lceil\log _{2}\left(\frac{d_{\mathrm{E}}}{d_{0}}\right)\right\rceil \approx\left\lceil\log _{2}\left(\frac{4.00 \cdot 10^{8} \mathrm{~m}}{1.00 \cdot 10^{-4} \mathrm{~m}}\right)\right\rceil=\left\lceil\log _{2}\left(4.00 \cdot 10^{12}\right)\right\rceil \\
& =\left\lceil\log _{2}(4.00)+12 \cdot \log _{2}(10)\right\rceil \approx\lceil 41.9\rceil=\underline{42}
\end{aligned}
$$

# --- PAGE page_9 ---

d) Es sei $n_{\mathrm{E}}$ die Anzahl durchzuführende Faltungen, bis die Fläche des Papiers den von Auge gerade noch sichtbaren Wert von
$A_{\mathrm{E}} \approx 0.100 \mathrm{~mm}^{2}=1.00 \cdot 10^{-1} \cdot\left(10^{-3} \mathrm{~m}\right)^{2}=1.00 \cdot 10^{-1-2.3} \mathrm{~m}^{2}=1.00 \cdot 10^{-7} \mathrm{~m}^{2}$
unterschreitet. Gemäss (58) gilt

$$
\begin{aligned}
& A_{\mathrm{E}}=A\left(n_{\mathrm{E}}\right)=A_{0} \cdot \frac{1}{2^{n_{\mathrm{E}}}} \\
& \Leftrightarrow \\
& 2^{n_{\mathrm{E}}} \cdot A_{\mathrm{E}}=A_{0} \\
& 2^{n_{\mathrm{E}}}=\frac{A_{0}}{A_{\mathrm{E}}} \\
& \|\cdot 2^{n_{\mathrm{E}}} \\
& \Leftrightarrow \\
& 2^{n_{\mathrm{E}}}=\frac{A_{0}}{A_{\mathrm{E}}}
\end{aligned}
$$

Daraus und durch Aufrunden auf die nächst grössere natürliche Zahl erhalten wir

$$
\begin{aligned}
\underline{n_{\mathrm{E}}} & =\left\lceil\log _{2}\left(\frac{A_{0}}{A_{\mathrm{E}}}\right)\right\rceil \approx\left\lceil\log _{2}\left(\frac{1.00 \mathrm{~m}^{2}}{1.00 \cdot 10^{-7} \mathrm{~m}^{2}}\right)\right\rceil=\left\lceil\log _{2}\left(1.00 \cdot 10^{7}\right)\right\rceil \\
& =\left\lceil\log _{2}(1.00)+7 \cdot \log _{2}(10)\right\rceil \approx\lceil 23.3\rceil=\underline{24}
\end{aligned}
$$

# 15. Aussagen über eine verallgemeinerte Exponentialfunktion 

Wir betrachten die verallgemeinerte Exponentialfunktion

$$
R(z)=12 \mathrm{~J} \cdot\left(\frac{1}{3}\right)^{\frac{z-2 m}{3 m}}
$$

| Welche der folgenden Aussagen sind wahr und welche falsch? | wahr | falsch |
| :-- | :--: | :--: |
| a) Es gibt ein $z$, so dass gilt $R(z)=13 \mathrm{~J}$. | $\bullet$ | $\bigcirc$ |
| b) Alle Funktionswerte von $R$ sind positiv. | $\bullet$ | $\bigcirc$ |
| c) Die Funktion $R$ lässt sich auch mit Hilfe der Basis $1 / 2$ ausdrücken. | $\bullet$ | $\bigcirc$ |
| d) Die Funktion $R$ ist monoton steigend. | $\bigcirc$ | $\bullet$ |
| e) Der Graph der Funktion $R$ verläuft durch den Punkt $(5 ; 4)$. | $\bigcirc$ | $\bullet$ |