<|ref|>text<|/ref|><|det|>[[115, 81, 755, 118]]<|/det|>
Es liegt eine hypergeometrische Verteilung vor: N = 40, M = Anzahl der unvollständigen Packungen = 4 

<|ref|>text<|/ref|><|det|>[[115, 117, 144, 135]]<|/det|>
a) 

<|ref|>equation<|/ref|><|det|>[[115, 135, 630, 210]]<|/det|>
\[
\begin{align*}
N &= 40, \quad M = 4, \quad n = 1; \quad P(X = x) = f(x) = \frac{\binom{4}{x} \binom{36}{1-x}}{\binom{40}{1}} \\
X &= 0 \quad (\text{nur vollständige Packungen: } P(X = 0) = f(0) = 0,9)
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 210, 140, 228]]<|/det|>
b) 

<|ref|>equation<|/ref|><|det|>[[115, 228, 650, 315]]<|/det|>
\[
\begin{align*}
N &= 40, \quad M = 4 \quad n = 10; \quad P(X = x) = f(x) = \frac{\binom{4} {x} \binom{36}{10-x}}{\binom{40}{10}} \\
P(X = 2) = f(2) = 0,2142
\end{align*}
\]

<|ref|>sub_title<|/ref|><|det|>[[115, 331, 260, 348]]<|/det|>
4. Kernreaktor 

<|ref|>text<|/ref|><|det|>[[115, 347, 880, 433]]<|/det|>
Bei einem Kernreaktor werden an die Brennelemente extrem hohe
Qualitätsanforderungen gestellt. Die Wahrscheinlichkeit dafür, dass ein
Brennelement diesen hohen Anforderungen nicht genügt, betrage p = 10⁻⁴. Wie gross
ist die Wahrscheinlichkeit, dass alle 1500 Brennelemente eines Reaktors die
vorgeschriebenen Qualitätsbedingungen erfüllen? 

<|ref|>text<|/ref|><|det|>[[115, 446, 839, 483]]<|/det|>
Es liegt eine Binomialverteilung vor mit n = 1500 und p = 10⁻⁴. Es darf durch eine
Poisson-Verteilung angenähert werden, da n*p = 0,15 = μ < 5 und p ≤ 0,01. 

<|ref|>equation<|/ref|><|det|>[[115, 481, 650, 516]]<|/det|>
\[
P(X = x) = f(x) = \frac{0,15^x}{x!} \cdot e^{-0,15} \Rightarrow P(X = 0) = f(0) = 0,8607
\]

<|ref|>equation<|/ref|><|det|>[[115, 516, 770, 533]]<|/det|>
Exakte Verteilung (Binomialverteilung mit n = 1500, p = 0,0001 und q = 1 - p = 0,9999):

<|ref|>equation<|/ref|><|det|>[[115, 533, 728, 572]]<|/det|>
\[
P(X = x) = f(x) = \binom{1500}{x} \cdot 0,0001^x \cdot 0,9999^{1500-x} \quad (x = 0,1,2, \dots, 1500)
\]

<|ref|>equation<|/ref|><|det|>[[115, 572, 642, 590]]<|/det|>
\[
P(X = 0) = f(0) = 0,8607 \quad (\text{in Übereinstimmung mit der Näherung})
\]

<|ref|>sub_title<|/ref|><|det|>[[115, 605, 252, 622]]<|/det|>
5. Kulturreise 

<|ref|>text<|/ref|><|det|>[[115, 621, 880, 723]]<|/det|>
Ein Touristikunternehmer bietet in jedem Herbst eine exklusive Kulturreise zu den
Schlössern der Loire an. Die Reise erfolgt mit einem Kleinbus, in dem neun Touristen
Platz haben. Aus langjähriger Erfahrung weiss der Unternehmer, dass eine jede
Buchung in den letzten beiden Tagen mit einer Wahrscheinlichkeit von 5% kurzfristig
storniert wird. Der Unternehmer hat wegen der kurzfristigen Stornierungen statt neun
Buchungen zehn Buchungen entgegengenommen. 

<|ref|>text<|/ref|><|det|>[[115, 721, 663, 739]]<|/det|>
a) Welches Überbelegungsrisiko geht der Unternehmer ein? 

<|ref|>text<|/ref|><|det|>[[115, 737, 870, 772]]<|/det|>
b) Um in der Gewinnzone zu bleiben, müssen mindestens acht Personen mitfahren.
Wie wahrscheinlich ist es, dass der Unternehmer noch kurzfristig für 

<|ref|>text<|/ref|><|det|>[[115, 770, 770, 805]]<|/det|>
Ersatzreisende sorgen muss, um nicht in die Verlustzone zu geraten?
c) Mit wie vielen Stornierungen hat er durchschnittlich zu rechnen?