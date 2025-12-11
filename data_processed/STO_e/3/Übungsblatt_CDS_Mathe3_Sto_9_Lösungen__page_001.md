<|ref|>sub_title<|/ref|><|det|>[[115, 166, 465, 202]]<|/det|>
# Übungsblatt Sto 9 

<|ref|>text<|/ref|><|det|>[[576, 179, 879, 216]]<|/det|>
Computational and Data Science
BSc HS2024 

<|ref|>text<|/ref|><|det|>[[115, 232, 270, 261]]<|/det|>
## Lösungen 

<|ref|>text<|/ref|><|det|>[[752, 240, 880, 258]]<|/det|>
Mathematik 3 

<|ref|>text<|/ref|><|det|>[[115, 287, 210, 304]]<|/det|>
Lernziele: 

<|ref|>text<|/ref|><|det|>[[115, 303, 781, 339]]<|/det|>
- Sie kennen die Begriffe Punktwolke, Kovarianz, Korrelationskoeffizient, Bestimmtheitsmass und ihre wichtigsten Eigenschaften. 

<|ref|>text<|/ref|><|det|>[[115, 337, 810, 389]]<|/det|>
- Sie können die Kovarianz und Korrelationskoeffizienten für eine gegebene Stichprobe bestimmen und können die Korrelation von Daten mittels einer Punktwolke qualitativ beurteilen. 

<|ref|>sub_title<|/ref|><|det|>[[115, 418, 508, 436]]<|/det|>
### 1. Kovarianz und Korrelationskoeffizient 

<|ref|>text<|/ref|><|det|>[[115, 435, 812, 470]]<|/det|>
Berechnen Sie die Kovarianz und den Korrelationskoeffizienten der folgenden Stichproben und skizzieren Sie die jeweilige Punktwolke: 

<|ref|>text<|/ref|><|det|>[[115, 469, 144, 486]]<|/det|>
a) 

<|ref|>table<|/ref|><|det|>[[139, 483, 499, 540]]<|/det|>
<table><tr><td>i</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>xi</td><td>2</td><td>2</td><td>4</td><td>1</td><td>5</td><td>4</td></tr><tr><td>yi</td><td>3</td><td>2</td><td>4</td><td>2</td><td>4</td><td>2</td></tr></table>

<|ref|>text<|/ref|><|det|>[[115, 538, 144, 555]]<|/det|>
b) 

<|ref|>table<|/ref|><|det|>[[139, 552, 444, 609]]<|/det|>
<table><tr><td>i</td><td>1</td><td>2</td><td>3</td><td></td><td>4</td><td>5</td></tr><tr><td>xi</td><td>2</td><td>4</td><td>6</td><td></td><td>8</td><td>10</td></tr><tr><td>yi</td><td>20</td><td>17</td><td>13</td><td></td><td>10</td><td>6</td></tr></table>

<|ref|>table<|/ref|><|det|>[[139, 626, 785, 812]]<|/det|>
<table><tr><td>i</td><td>xi</td><td>yi</td><td>xi - x̄</td><td>(xi - x̄)²</td><td>yi - ȳ</td><td>(yi - ȳ)²</td><td>(xi - x̄)(yi - ȳ)</td></tr><tr><td>1</td><td>2</td><td>3</td><td>-1</td><td>1</td><td>1/6</td><td>1/36</td><td>-1/6</td></tr><tr><td>2</td><td>2</td><td>2</td><td>-1</td><td>1</td><td>-5/6</td><td>25/36</td><td>5/6</td></tr><tr><td>3</td><td>4</td><td>4</td><td>1</td><td>1</td><td>7/6</td><td>49/36</td><td>7/6</td></tr><tr><td>4</td><td>1</td><td>2</td><td>-2</td><td>4</td><td>-5/6</td><td>25/36</td><td>10/6</td></tr><tr><td>5</td><td>5</td><td>4</td><td>2</td><td>4</td><td>7/6</td><td>49/36</td><td>14/6</td></tr><tr><td>6</td><td>4</td><td>2</td><td>1</td><td>1</td><td>-5/6</td><td>25/36</td><td>-5/6</td></tr><tr><td>Σ</td><td>18</td><td>17</td><td>0</td><td>12</td><td>0</td><td>174/36</td><td>5</td></tr></table>