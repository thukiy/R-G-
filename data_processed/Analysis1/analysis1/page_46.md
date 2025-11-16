# Stetigkeit einer Funktion 

Def: Eine in $x_{0}$ und einer gewissen Umgebung von $x_{0}$ definierte Funktion $y=f(x)$ heisst stetig an der Stelle $x_{0}$, wenn der Grenzwert von $f(x)$ an $x_{0}$ vorhanden ist und mit dem Funktionswert übereinstimmt :
$\lim _{x \rightarrow x_{0}} f(x)=f\left(x_{0}\right)$
Bsp: $\quad$ f $(x)=x^{2} \quad$ f: $R \rightarrow R$
$f(1)=1 \quad \lim _{x \rightarrow 1} f(x)=1=f(1)$
$\Rightarrow$ ist auf ganz $R$ stetig

- $f(x)=\frac{1}{1-x} \quad f: R \backslash \mathbb{E} 13 \rightarrow R$
$\Rightarrow f(x)$ ist an $x=1$ nicht stetig, da nicht definiert an dieser Stelle (Definitionslücke)
- $f(x)=\left\{\begin{array}{ll}1 & x \geqslant 0 \\ 0 & <0\end{array}\right.$
$\Rightarrow f(x)$ ist an $x=0$ nicht stetig
Unstetigkeitsstellen : - Lücken im Definitionsbereich
- endliche sprünge
- Polstellen

Bsp: $\quad f(x)=\frac{x^{2}-1}{x+1} \quad$ bei $x_{0}=-1$ Definitionslücke
$\lim _{x \rightarrow-1} \frac{x^{2}-1}{x+1}=\lim _{x \rightarrow-1} \frac{(x+1)(x-1)}{x+1}=\lim _{x \rightarrow-1}(x-1)=-2$
Beheben der Lücke : Funktionswert = Grenzwert

$$
g(x)=\left\{\begin{array}{ll}
\frac{x^{2}-1}{x+1} & x \neq-1 \\
-2 & x=-1
\end{array}\right\}=x-1 \Rightarrow g(x) \text { ist stetig }
$$