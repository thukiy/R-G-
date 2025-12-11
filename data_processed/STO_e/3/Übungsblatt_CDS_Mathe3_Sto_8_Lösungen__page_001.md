<|ref|>title<|/ref|><|det|>[[115, 165, 465, 201]]<|/det|>
# Übungsblatt Sto 8 

<|ref|>text<|/ref|><|det|>[[575, 179, 880, 216]]<|/det|>
Computational and Data Science
BSc HS2024 

<|ref|>text<|/ref|><|det|>[[115, 232, 272, 261]]<|/det|>
## Lösungen 

<|ref|>text<|/ref|><|det|>[[528, 240, 880, 259]]<|/det|>
Differentialgleichungen und Stochastik 

<|ref|>text<|/ref|><|det|>[[115, 287, 210, 305]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 303, 880, 387]]<|/det|>
- Sie kennen die Begriffe Grundgesamtheit, Merkmal, Merkmalsträger, Merkmalsausprägung, Nominal-, Ordinal-, metrische Skala, kumulierte Häufigkeit, empirische Verteilungsfunktion, Modus, Median, arithmetisches Mittel, Quantil, mittlere absolute Abweichung, Spannweite, empirische Varianz und können diese auf konkrete Datensätze anwenden. 

<|ref|>text<|/ref|><|det|>[[115, 386, 856, 437]]<|/det|>
- Sie kennen verschiedene Methoden, um einen Datensatz grafisch darzustellen: Stabdiagramm, Rechteckdiagramm, Kreisdiagramm, Histogramm, Polygonzug, Box-Plot und können diese auch für konkrete Datensätze anwenden. 

<|ref|>sub_title<|/ref|><|det|>[[115, 467, 323, 485]]<|/det|>
### 1. Baumbestand in D 

<|ref|>text<|/ref|><|det|>[[115, 484, 875, 535]]<|/det|>
Für das Jahr 1997 wurden in den deutschen Bundesländern (ausser Berlin) folgende Zahlen für den Anteil (in %) von Bäumen mit deutlichen Umweltschäden ausgewiesen: 

<|ref|>table<|/ref|><|det|>[[115, 540, 880, 579]]<|/det|>
<table><tr><td>Bundesland</td><td>HE</td><td>NS</td><td>NRW</td><td>SH</td><td>BB</td><td>MV</td><td>S</td></tr><tr><td>Anteil</td><td>16</td><td>15</td><td>20</td><td>20</td><td>10</td><td>10</td><td>19</td></tr></table>

<|ref|>table<|/ref|><|det|>[[115, 591, 880, 630]]<|/det|>
<table><tr><td>Bundesland</td><td>SA</td><td>TH</td><td>BW</td><td>B</td><td>HH</td><td>RP</td><td>SL</td></tr><tr><td>Anteil</td><td>14</td><td>38</td><td>19</td><td>19</td><td>33</td><td>24</td><td>19</td></tr></table>

<|ref|>text<|/ref|><|det|>[[115, 644, 848, 695]]<|/det|>
Erläutern Sie die Begriffe Grundgesamtheit, Untersuchungseinheit, Merkmal und Ausprägung anhand dieses Beispiels. Zeichnen Sie für die obigen Angaben einen Boxplot. Vergleichen Sie arithmetisches Mittel und Median der Angaben. 

<|ref|>text<|/ref|><|det|>[[115, 710, 857, 744]]<|/det|>
Grundgesamtheit: Bäume in den deutschen Bundesländern (ausser Berlin) im Jahr 1997. 

<|ref|>text<|/ref|><|det|>[[115, 743, 383, 761]]<|/det|>
Untersuchungseinheit: Baum. 

<|ref|>text<|/ref|><|det|>[[115, 760, 490, 778]]<|/det|>
Untersuchungsmerkmal: Umweltschaden. 

<|ref|>text<|/ref|><|det|>[[115, 776, 463, 795]]<|/det|>
Ausprägung: Umweltschaden Ja/Nein. 

<|ref|>text<|/ref|><|det|>[[115, 809, 363, 827]]<|/det|>
Die geordneten Daten sind 

<|ref|>table<|/ref|><|det|>[[120, 829, 732, 874]]<|/det|>
<table><tr><td>i</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td></tr><tr><td></td><td>10</td><td>10</td><td>14</td><td>15</td><td>16</td><td>19</td><td>19</td><td>19</td><td>19</td><td>20</td><td>20</td><td>24</td><td>33</td><td>38</td></tr></table>