<|ref|>sub_title<|/ref|><|det|>[[114, 81, 252, 99]]<|/det|>
## 7. Produktion 

<|ref|>text<|/ref|><|det|>[[114, 98, 870, 167]]<|/det|>
Bei einem schwer beherrschbaren Produktionsprozess beträgt das Risiko, dass ein erzeugter Artikel den Qualitätserfordernissen nicht genügt, 2,6 %. Wie gross ist die Wahrscheinlichkeit, dass aus 300 erzeugten Artikeln eine Lieferung von 290 Artikeln zusammengestellt werden kann, die den Qualitätserfordernissen genügt? 

<|ref|>text<|/ref|><|det|>[[114, 179, 874, 216]]<|/det|>
Zufallsvariable X = Anzahl der Artikel, die den Qualitätsanforderungen nicht genügen X ist binomialverteilt mit n = 300 und p = 0,026 

<|ref|>equation<|/ref|><|det|>[[114, 214, 565, 255]]<|/det|>
\[F_B(10|300; 0,026) = \sum_{a=0}^{10} \binom{300}{a} \cdot 0,026^a \cdot 0,974^{300-a}\]

<|ref|>text<|/ref|><|det|>[[114, 255, 816, 275]]<|/det|>
Mit 83,8 % genügt die zusammengestellte Lieferung den Qualitätsansprüchen. 

<|ref|>sub_title<|/ref|><|det|>[[114, 288, 360, 307]]<|/det|>
## 8. Vorzeitiger Ruhestand 

<|ref|>text<|/ref|><|det|>[[114, 305, 872, 423]]<|/det|>
In der Berliner Morgenpost vom 19. Dezember 2002 wird berichtet, dass im Jahr 2001 im Durchschnitt jeder 71. verbeamtete Berliner Lehrer vorzeitig pensioniert wurde. Im Bekanntenkreis Ihrer Eltern befinden sich fünf verbeamtete Lehrer, die unabhängig voneinander an unterschiedlichen Berliner Schulen in unterschiedlichen Fächern unterrichten und zu unterschiedlichen Altersgruppen gehören. Wie gross ist die Wahrscheinlichkeit dafür, dass mindestens zwei dieser Bekannten im Jahre 2001 vorzeitig in den Ruhestand versetzt wurden? 

<|ref|>text<|/ref|><|det|>[[120, 436, 875, 563]]<|/det|>
diskrete Zufallsgröße X: *Anzahl vorzeitig pensionierter Lehrer unter 5 zufällig ausgewählten verbeamteten Lehren*, Verteilungsmodell: Binomialverteilung mit n = 5 und p = 1 / 71 = 0,0141, wenn folgende Annahme gilt: die Auswahl der 5 verbeamteten Lehrer im Bekanntenkreis der Eltern kann als ein fünfmaliges unabhängig voneinander durchgeführtes BERNOULLI Experiment mit konstanter Erfolgswahrscheinlichkeit für das Ereignis „zufällig ausgewählter verbeamteter Lehrer wird vorzeitig pensioniert“ gedeutet werden, zu ermittelnde Wahrscheinlichkeit: \(P(X \ge 2) = 1 - P(X \le 1) = 1 - (P(X = 0) + P(X = 1)) = 1 - (0,9315 + 0,0666) = 0,0019\) 

<|ref|>sub_title<|/ref|><|det|>[[114, 575, 195, 592]]<|/det|>
## 9. Skat 

<|ref|>text<|/ref|><|det|>[[114, 591, 821, 627]]<|/det|>
Beim Skat (3 Spieler, 32 Karten) erhält jeder Spieler 10 Karten, die restlichen 2 Karten bleiben verdeckt. Mit welcher Wahrscheinlichkeit erhält ein Spieler 

<|ref|>text<|/ref|><|det|>[[114, 626, 256, 644]]<|/det|>
a) alle 4 Asse, 

<|ref|>text<|/ref|><|det|>[[114, 642, 245, 660]]<|/det|>
b) kein Ass? 

<|ref|>text<|/ref|><|det|>[[120, 674, 480, 690]]<|/det|>
**Zufallsvariable:** X = Anzahl der „Asse“ eines Spielers 

<|ref|>text<|/ref|><|det|>[[120, 693, 872, 735]]<|/det|>
X ist *hypergeometrisch* verteilt mit den folgenden Parametern: N = 32 (Anzahl der Karten); M = 4 (Anzahl der „Asse“); n = 10 (Anzahl der Karten eines Spielers). Die *Wahrscheinlichkeitsfunktion* der diskreten Zufallsvariablen X lautet damit wie folgt: 

<|ref|>equation<|/ref|><|det|>[[161, 733, 755, 801]]<|/det|>
\[f(x) = P(X = x) = \frac{\binom{M}{x} \cdot \binom{N - M}{n - x}}{\binom{N}{n}} = \frac{\binom{4}{x} \cdot \binom{32 - 4}{10 - x}}{\binom{32}{10}} \quad (x = 0, 1, 2, 3, 4)\]