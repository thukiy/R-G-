<|ref|>text<|/ref|><|det|>[[118, 86, 690, 144]]<|/det|>
Daraus folgt \(\overline{F} = \frac{72037}{10} = 7203.7\), \(\overline{B} = 382.5\), \(\text{var}(F) = 18934000.6\), \(\text{var}(B) = 14\,333.7\) und \(\text{cov}(F, B) = -79\,965.5\). Dann ist 

<|ref|>equation<|/ref|><|det|>[[183, 156, 625, 250]]<|/det|>
\[r(F, B) = \frac{\text{cov}(F, B)}{\sqrt{\text{var}(F) \cdot \text{var}(B)}} = \frac{-79\,965.5}{\sqrt{18934000.6 \cdot 14\,333.7}} = -0.154\]

<|ref|>text<|/ref|><|det|>[[118, 263, 690, 300]]<|/det|>
Für die weiteren Schritte geben wir die Kovarianzmatrix an, wie oben ganzzahlig gerundet: 

<|ref|>table<|/ref|><|det|>[[118, 300, 688, 440]]<|/det|>
<table><tr><td>cov</td><td>F</td><td>B</td><td>S</td><td>\(S_F\)</td><td>\(B_F\)</td><td>\(S_W\)</td></tr><tr><td>F</td><td>18 934 001</td><td>-79 965</td><td>-10 461</td><td>-6849</td><td>-23 694</td><td>51 507</td></tr><tr><td>B</td><td>-79 965</td><td>14 334</td><td>-294</td><td>62</td><td>488</td><td>-964</td></tr><tr><td>S</td><td>-10 461</td><td>-294</td><td>2298</td><td>24</td><td>-11</td><td>1423</td></tr><tr><td>\(S_F\)</td><td>-6849</td><td>62</td><td>24</td><td>3</td><td>11</td><td>-10</td></tr><tr><td>\(B_F\)</td><td>-23 694</td><td>488</td><td>-11</td><td>11</td><td>47</td><td>-106</td></tr><tr><td>\(S_W\)</td><td>51 507</td><td>-964</td><td>1423</td><td>-10</td><td>-106</td><td>1135</td></tr></table>

<|ref|>text<|/ref|><|det|>[[118, 448, 875, 484]]<|/det|>
Auf den Diagonalen dieser Matrix stehen die Merkmale. Wie bei der Berechnung von r(F,B) bestimmt man nun die paarweisen Korrelationen. 

<|ref|>table<|/ref|><|det|>[[118, 485, 688, 623]]<|/det|>
<table><tr><td>r</td><td>F</td><td>B</td><td>S</td><td>\(S_F\)</td><td>\(B_{F}\)</td><td>\(S_W\)</td></tr><tr><td>F</td><td>1</td><td>-0.15</td><td>-0.05</td><td>-0.85</td><td>-0.79</td><td>0.35</td></tr><tr><td>B</td><td>-0.15</td><td>1</td><td>-0.05</td><td>0.28</td><td>0.59</td><td>-0.24</td></tr><tr><td>S</td><td>-0.05</td><td>-0.05</td><td>1</td><td>0.28</td><td>-0.03</td><td>0.88</td></tr><tr><td>\(S_F\)</td><td>-0.85</td><td>0.28</td><td>0.28</td><td>1</td><td>0.87</td><td>-0.17</td></tr><tr><td>\(B_F\)</td><td>-0.79</td><td>0.59</td><td>-0.03</td><td>0.87</td><td>1</td><td>-0.46</td></tr><tr><td>\(S_W\)</td><td>0.35</td><td>-0.24</td><td>0.88</td><td>-0.17</td><td>-0.46</td><td>1</td></tr></table>

<|ref|>text<|/ref|><|det|>[[118, 641, 685, 680]]<|/det|>
\(B\), \(S\) und \(F\) sind praktisch unkorreliert: \(r(F, B) = -0.15\), \(r(F, S) = -0.05\) und \(r(B, S) = -0.05\). 

<|ref|>text<|/ref|><|det|>[[118, 686, 688, 816]]<|/det|>
Trotzdem sind die Baby- und die Storchquoten hochgradig miteinander korreliert \(r(B_F, S_F) = 0.87\)! Ein arg naiver Betrachter könnte aus der erfreulichen Zunahme der Störche auch auf ein Ansteigen der Geburtenziffer hoffen. Berücksichtigt man dagegen die Wasserfläche, so sind auf einmal Baby- und Storchquoten negativ korreliert: \(r(B_F, S_W) = -0.46\)! Also je weniger Störche, umso mehr Kinder! Oder?? 

<|ref|>text<|/ref|><|det|>[[118, 823, 688, 896]]<|/det|>
Was lässt sich aus diesem Beispiel lernen? Eine kausale Verknüpfung zwischen \(F, B\) und \(S\) ist nirgends ersichtlich. Berechnet man jedoch Quoten oder andere Gliederungszahlen, so können sich die Korrelationen unvorhersehbar ändern.