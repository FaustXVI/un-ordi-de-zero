# Description

Aujourd'hui, on essaie de comprendre ce qui se passe dans le dernier circuit qu'on a fait avec deux résistances en parallèle.

# Références
[[Lois de Kirchhoff]] : https://www.youtube.com/watch?v=Hs1gesB3Lv4 (2 résistances en parallèle)
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
> > Oui, et pour ça, on va avoir besoin de réviser les [[Lois de Kirchhoff]] et de les exprimer de manière mathématiques.
> 
> > [!xav]+
> > Si je me souviens bien, il y a deux lois :
> >  - la [[Lois de Kirchhoff#Loi des nœuds|loi des nœuds]]
> >  - la [[Lois de Kirchhoff#Loi des mailles|loi des mailles]]
> 
> > [!theo]+
> > Oui tout à fait. Commençons par la [[Lois de Kirchhoff#Loi des nœuds|loi des nœuds]

> [!manim]- 2 / [[Lois de Kirchhoff#Loi des nœuds|loi des nœuds]]
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
 
> [!scene]- 3 / avec deux branches
> 
> > [!xav]+
> > Ok donc dans notre circuit à deux branches, la somme des intensités dans les branches est égale à l'intensité en entrée de la jonction. C'est ça ?
> 
> > [!theo]+
> > Exactement.
> 
