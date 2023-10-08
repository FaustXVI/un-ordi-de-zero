=> un ampère mètre après les branches ?
=> loi des nœuds
=> démo
=> un moyen plus rapide ? (autre vidéo ?)
=> calcul du R général
=> avant et après, c'est la même chose
=> démo avec un ohm mêtre
# Description

# Références

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
> >
> 
> > [!theo]+
> >
> 

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
 