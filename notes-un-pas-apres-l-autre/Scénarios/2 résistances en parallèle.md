# Description

Aujourd'hui, on essaie de comprendre ce qui se passe dans le dernier circuit qu'on a fait avec deux résistances en parallèle.

# Références
[[Lois de Kirchhoff]] : https://www.youtube.com/watch?v=Hs1gesB3Lv4 (2 résistances en parallèle)
La [[résistance]] : https://www.youtube.com/watch?v=gGyxI5CayDM
# Textes

> [!scene]- 1 / Intro
> 
> > [!xav]+
> > Bonjour !
> 
> > [!theo]+
> > Salut !
> 
> > [!xav]+
> > La dernière fois, on a fait un circuit avec deux résistances sur deux branches différentes.
> 
> > [!theo]+
> > Oui, c'est ce qu'on appelle mettre les résistances en parallèle.
> 
> > [!xav]+
> > Et on en était arrivé au point où on voyait bien que ça fonctionne, mais sans vraiment comprendre comment.
> 
> > [!theo]+
> > Tout à fait.
>
> > [!xav]+
> > Mais ça c'est facile en fait. On a la [[loi d'ohm]], U=RI, or on connait R puisse qu'on la choisie et on connaît U, la tension de notre pile qu'on choisit aussi.
> 
> > [!theo]+
> > Stop !
> 
> > [!xav]+
> > Quoi ?
> 
> > [!theo]+
> > Je pense que tu pré-suppose beaucoup de chose. Par exemple, comment tu sais que les tensions aux bornes des résistances sont le même et qu'en plus elles sont égale à la tension de la pile ?
> 
> > [!xav]+
> > Euh, bah, c'est évident non ?
> 
> > [!theo]+
> > Mauvaise réponse ! Aller, on se fait une petite révision de la [[Lois de Kirchhoff#Loi des mailles|loi des mailles]]
> 

> [!manim]- 2 / [[Lois de Kirchhoff#Loi des mailles|loi des mailles]]
> 
> La loi des mailles dit que $$\sum_{n}{U_n} = 0$$
> 
> Si on prend le schéma de notre circuit. On y vois une grande boucle, dit autrement une maille.
> ![[2-resistances-parallel-amp.excalidraw]]
> 
> On peut y placer 4 points, $a$, $b$, $c$ et $d$.
> 
> D'après la loi des mailles, on a donc $U_{ab} + U_{bc} + U_{cd} + U_{da} = 0$
> 
> $U_da$ est la tension de notre pile, si on la met de l'autre côté on obtient $$U_{ab} + U_{bc} + U_{cd} = - U_{da}$$ soit $$U_{ab} + U_{bc} + U_{cd} = U_{ad}$$
> 
> On est donc loin de ce qui tu disais. Pourtant tu as vu juste car $U_{ab}$ et $U_{cd}$ sont sur le même fil sans rien au milieu. Quand on réfléchis théoriquement, on manipule des fils dits idéaux. Cela veut dire qu'ils ont la même tension du début à la fin.
> 
> Donc $U_{ab}$ et $U_cd$ sont tous deux égaux à zéro.
> 
> $$0 + U_{bc} + 0 = U_{ad}$$
> $$U_{bc} = U_{ad}$$
> 
> On a donc bien $U_{bc}$, la tension aux bornes des branches, qui est égal à $U_{ad}$ la tension de notre pile.
> 

> [!scene]- 3 / ok mais j'ai raison
> 
> > [!xav]+
> > Ok, et dans la vrai vie, avec des fils qui ne sont pas idéaux, il se passe quoi ?
> 
> > [!theo]+
> > Souviens toi, on en a déjà parlé quand on a parlé des résistances. Les fils ont leur propre résistance qui dépend de leur composition, de leur longueur et de leur diamètre.
> > Mais dans ce que nous on fait, l'impact est tellement faible qu'on peut le négliger et faire comme si on avait des fils idéaux.
> 
> > [!xav]+
> > Ok, donc j'ai eu un coup de bol mais j'avais raison.
> 
> > [!theo]+
> > Oui
> 
> > [!xav]+
> > Donc si j'ai bien tout compris, je peux te faire les calculs regarde.
> 
> [!manim]+ N / name
> 
> 

> [!manim]- 4 / calcul de i
> 
> Pour chaque branche, la [[loi d'ohm]] nous dit :
> $$U = R \times I$$
> 
> Or on viens de dire que $U$ est égal à la tension de notre pile. Et comme on la choisie, on peut la fixer à la valeur que l'on veut, par exemple, $1.5\ V$
> $$1.5 = R \times I$$
> 
> Ensuite, dans la même logique, on choisie $R$ donc on peut y mettre valeur que l'on veut, par exemple $10\ \Omega$
> $$1.5 = 10 \times I$$
> 
> Donc $I$ est égal à 1.5 sur 10
> $$\frac{1.5}{10} = I$$
> 
> soit 0.15 Ampères
> $$0.15 = I$$
> 
> donc 150 milli-ampères


Changement : U=RI => intensité dans les branche
=> quid après ?
=> loi des nœuds
=> un moyen plus rapide ?
=> loi des mailles et calcul du R général

> [!manim]- X / [[Lois de Kirchhoff#Loi des nœuds|loi des nœuds]]
> 
> Un nœud, c'est un point de notre circuit où il y a une ou plusieurs intensités en entrée et une ou plusieurs intensités en sorties.
> ![[nœud.excalidraw]]
> 
> Prenons un exemple avec deux intensités entrantes $i_1$ et $i_2$ et deux intensités sortantes $i_3$ et $i_4$
> 
> La loi des nœuds dit que tout ce qui entre dans un nœud doit sortir.
> 
> Dit autrement, que la somme des intensités entrantes est égale à l'opposé de la somme des intensités sortantes.
> $$i_1 + i_2 = i_3 + i_4$$
> 
> Cependant, une intensité peut être mesurée dans les deux sens, on peut donc tout mesurer comme si on avait que des intensités en entrée. On a juste à inverser $i_3$ et $i_4$
> $$i_1 + i_2 = (-i_3) + (-i_4)$$
> 
> Si on passe $i_3$ et $i_4$ de l'autre côté, on obtient $$i_1 + i_2 + i_3 + i_4 = 0$$
> 
> Si on généralise, on retrouve la vrai formulation de la loi des nœuds : la sommes des intensités en un point, toutes mesurées dans le même sens par rapport au nœud, est égal à zéro
> $$\sum_{n}{i_n} = 0$$
> 
 