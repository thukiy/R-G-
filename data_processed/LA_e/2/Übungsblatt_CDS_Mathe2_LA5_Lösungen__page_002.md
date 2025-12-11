<|ref|>text<|/ref|><|det|>[[115, 83, 144, 100]]<|/det|>
c) 

<|ref|>equation<|/ref|><|det|>[[115, 96, 413, 167]]<|/det|>
\[C^{-1} = \begin{pmatrix} \frac{2}{3} & \frac{1}{3} & \frac{1}{3} \\ -\frac{1}{3} & \frac{4}{3} & -\frac{2}{3} \\ -\frac{1}{3} & \frac{2}{3} & -\frac{1}{3} \end{pmatrix}\]

<|ref|>text<|/ref|><|det|>[[115, 170, 144, 188]]<|/det|>
d) 

<|ref|>equation<|/ref|><|det|>[[115, 186, 494, 288]]<|/det|>
\[D^{-1} = \begin{pmatrix} \frac{2}{3} & -\frac{1}{6} & -\frac{1}{3} & -\frac{1}{2} \\ -\frac{13}{3} & \frac{11}{6} & \frac{2}{3} & -\frac{1}{2} \\ 15 & -\frac{11}{2} & -2 & -\frac{5}{2} \\ 7 & -\frac{5}{2} & -1 & -\frac{3}{2} \end{pmatrix}\]

<|ref|>text<|/ref|><|det|>[[115, 290, 144, 307]]<|/det|>
e) 

<|ref|>text<|/ref|><|det|>[[115, 306, 418, 322]]<|/det|>
Wir benutzen zuerst Zeilenoperationen: 

<|ref|>equation<|/ref|><|det|>[[125, 330, 825, 655]]<|/det|>
\[
\begin{align*}
A \quad & E \\
\left( \begin{array}{cc} \cos(\phi) & -\sin(\phi) \\ \sin(\phi) & \cos(\phi) \end{array} \right) \quad & \left( \begin{array}{cc} 1 & 0 \\ 0 & 1 \end{array} \right) \\
\left( \begin{array}{cc} (\cos(\phi))^2 & -\sin(\phi) \cos(\phi) \\ \sin(\phi) & \cos(\phi) \end{array}  \right) \quad & \left( \begin{array}{cc} \cos(\phi) & 0 \\ 0 & 1 \end{array} \right) \\
\left( (\cos(\phi))^2 + \sin(\phi))^2 & -\sin(\phi) \cos(\phi) + \sin(\phi) \cos(\phi) \\ \sin(\phi) & \cos(\ph) \end{array} \right) \quad & \left( \begin{array}{cc}\cos(\phi) & \sin(\phi) \\ 0 & 1 \end{array} \right) \\
\left( \begin{array} {cc} 1 & 0 \\ \sin(\phi) & \cos(\phi) \end{array} \right) & \left( \begin{array}{cc} \cos(\phi) & \sin(\phi) \\ 0 & 1 \end{array}\right) \\
\left( \begin{array}{cc} 1 & 0 \\ 0 & \cos(\phi) \end{array} \right) & \left( \begin{cc} \cos(\phi) & \sin(\phi) \\ -\cos(\phi) \sin(\phi) & 1 - (\sin(\phi))^2 \end{array} \right) \\
\left( \begin{array} {cc} 1& 0 \\ 0 & \cos(\phi) \end{array} \right) & \\
\left( \begin{array} {cc} 1 & 0 \\ 0 & \cos(\phi) \end{array}\right) & \left( \begin{array}{cc} \cos(\phi) & \cos(\phi) \\ -\cos(\phi) \sin(\phi) & (\cos(\phi))^2 \end{array} \right) \\
\left( \begin{array}  {cc} 1 & 0 \\ 0 & 1 \end{array} \right)
\end{align*}
\]

<|ref|>text<|/ref|><|det|>[[115, 653, 300, 670]]<|/det|>
Also lautet die Inverse: 

<|ref|>equation<|/ref|><|det|>[[350, 664, 592, 701]]<|/det|>
\[A^{-1} = \begin{pmatrix} \cos(\phi) & \sin(\phi) \\ -\sin(\phi) & \cos(\phi) \end{pmatrix}.\]

<|ref|>sub_title<|/ref|><|det|>[[115, 718, 330, 736]]<|/det|>
## 2. Erinnerung an LGS 

<|ref|>text<|/ref|><|det|>[[115, 735, 850, 884]]<|/det|>
Ein Gerätehersteller hat noch Kapazitäten frei. In der Produktion werden Teile zusammengebaut, danach werden die fertigen Geräte geprüft und in das Lager gebracht. Für Gerät A ist im Lager je ein Stellplatz, für die Geräte B und C je zwei Plätze erforderlich. Die Montage dauert 20 Minuten bei Gerät A, 10 Minuten bei B und 20 Minuten bei C. Die Prüfung benötigt 4 Minuten für Gerät A, 2 Minuten für B und 6 Minuten für C. Es stehen insgesamt noch 45 Stunden für die Montage, 240 Lagerplätze und 10 Stunden Prüfzeit zur Verfügung. Welche Teile sind in welchen Mengen noch zu produzieren, um das Lager und die verfügbare Zeit voll auszulasten?