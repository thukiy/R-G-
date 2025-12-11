<|ref|>title<|/ref|><|det|>[[115, 165, 485, 201]]<|/det|>
# Übungsblatt DGL 7 

<|ref|>text<|/ref|><|det|>[[575, 179, 880, 216]]<|/det|>
Computational and Data Science
BSc HS2024 

<|ref|>text<|/ref|><|det|>[[115, 232, 270, 261]]<|/det|>
## Lösungen 

<|ref|>text<|/ref|><|det|>[[752, 240, 880, 258]]<|/det|>
Mathematik 3 

<|ref|>text<|/ref|><|det|>[[115, 287, 210, 305]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 303, 880, 354]]<|/det|>
- Sie kennen die Begriffe freie gedämpfte harmonische Schwingung, Dämpfungskonstante, schwache/kritische/starke Dämpfung sowie ihre wichtigsten Eigenschaften. 

<|ref|>text<|/ref|><|det|>[[115, 352, 816, 387]]<|/det|>
- Sie können den qualitativen Verlauf einer freien gedämpften harmonischen Schwingung anhand der Parameter in der DGL beurteilen. 

<|ref|>text<|/ref|><|det|>[[115, 385, 875, 420]]<|/det|>
- Sie können das AWP der freien gedämpften harmonischen Schwingung für einen RLC Schaltkreis aufstellen und qualitativ beurteilen. 

<|ref|>sub_title<|/ref|><|det|>[[115, 434, 725, 453]]<|/det|>
### 1. Aussagen über freie gedämpfte harmonische Schwingungen 

<|ref|>text<|/ref|><|det|>[[115, 451, 666, 469]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table<|/ref|><|det|>[[115, 466, 880, 654]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td>a) Bei freien gedämpften harmonischen Schwingungen wird die innere Dämpfung berücksichtigt.</td><td>X</td><td></td></tr><tr><td>b) Bei freien gedämpften harmonischen Schwingungen wird die innere Dämpfung vernachlässigt.</td><td></td><td>X</td></tr><tr><td>c) Bei freien gedämpften harmonischen Schwingungen werden äussere Anregungen berücksichtigt.</td><td></td><td>X</td></tr><tr><td>d) Bei freien gedämpften harmonischen Schwingungen werden äussere Anregungen vernachlässigt.</td><td>X</td><td></td></tr><tr><td>e) Die Frequenz einer freien gedämpften harmonischen Schwingung lässt sich direkt aus der DGL ablesen.</td><td>X</td><td></td></tr></table>

<|ref|>sub_title<|/ref|><|det|>[[115, 668, 723, 687]]<|/det|>
### 2. Aussagen über freie gedämpfte harmonische Schwingungen 

<|ref|>text<|/ref|><|det|> [[115, 685, 875, 720]]<|/det|>
Sei \(\omega_0, \delta > 0\) und \(t_0, x_0, v_0 \in \mathbb{R}\). Gegeben sei das folgende AWP der freien gedämpften harmonischen Schwingung: 

<|ref|>equation<|/ref|><|det|>[[115, 718, 350, 737]]<|/det|>
\[
\text{DGL: } \ddot{x} + 2\delta \dot{x} + \omega_0^2 x = 0
\]

<|ref|>equation<|/ref|><|det|>[[115, 735, 250, 754]]<|/det|>
\[
\text{AB: } x(t_0) = x_0
\]

<|ref|>equation<|/ref|><|det|>[[152, 753, 255, 772]]<|/det|>
\[
\dot{x}(t_0) = v_0.
\]

<|ref|>text<|/ref|><|det|>[[115, 769, 680, 788]]<|/det|>
Welche der folgenden Aussagen sind wahr und welche falsch? 

<|ref|>table_caption<|/ref|><|det|>[[115, 787, 880, 805]]<|/det|>
 

<|ref|>table<|/ref|><|det|>[[115, 792, 880, 925]]<|/det|>
<table><tr><td></td><td>wahr</td><td>falsch</td></tr><tr><td rowspan="2">a) Ist \(x_1\) eine Lösung der DGL, dann auch die Funktion \(x_2 = 7x_1\).</td><td>X</td><td></td></tr><tr><td></td><td>X</td></tr><tr><td>b) Sind \(x_1\) und \(x_2\) Lösungen des AWP, dann auch die Funktion \(x_3 = x_2 + x_1\).</td><td></td><td>X</td></tr><tr><td>c) Gilt \(\delta > \omega_0\), dann oszilliert die Lösung \(x(t)\) mit der Kreisfrequenz \(\omega_d < \omega_0\).</td><td></td><td>X</td></tr><tr><td>d) Gilt \(\delta < \omega_0\), dann oszilliert die Lösung \(x(t)\) mit der Kreisfrequenz \(\omega_0\).</td><td></td><td>X</td></tr></table>