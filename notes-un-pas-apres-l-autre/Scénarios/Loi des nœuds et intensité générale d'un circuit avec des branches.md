# Description

Cette fois si, on place l'ampère-mètre après les branches et on regarde l'intensité qu'on y trouve. La loi des nœuds va nous aider à comprendre ce qu'il se passe.

# Références
- les imprécisions
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
> > La dernière fois, on se demandait ce que ça donnerai si on mettais un ampèremètre après les deux branches.
> 
> > [!theo]+
> > Yes ! Et pour se donner une idée de la réponse, regardons ce que ça donne en spintronics !
> 

> [!close-up]+ 2 / Ampèremètre après
> 
> J'ai refait notre circuit avec deux résistances.
> J'ai mis un crochet bleu par chaîne pour qu'on puisse comparer la vitesse de rotation des chaines.
> Si je fait tourner le circuit, on voit que la chaîne lié à la pile tourne plus vite que celle des branches.

> [!scene]- 3 / Intiution
> 
> > [!xav]+
> > Et du coup, de manière intuitive, j'ai l'impression que la chaîne lié à la pile tourne deux fois plus vite que celle des branches, donc je dirait que les intensités s'additionnent.
> 
> > [!theo]+
> > Bien joué ! Tu viens d'intuiter la loi des nœuds ! Je te fait un dessin pour t'en parler plus en détail.
> 

> [!manim]- 4 / [[Lois de Kirchhoff#Loi des nœuds|loi des nœuds]]
> 
> Un nœud, c'est un point de notre circuit où il y a une ou plusieurs intensités en entrée et une ou plusieurs intensités en sorties.
> ![[nœud.excalidraw]]
> 
> Prenons un exemple avec deux intensités entrantes $i_1$ et $i_2$ et deux intensités sortantes $i_3$ et $i_4$
> 
> La loi des nœuds dit que tout ce qui entre dans un nœud doit sortir.
> 
> C'est ce que l'on appelle la conservation des charges électriques et c'est quelque chose qui était sous entendu et nécessaire dans mon explication de la loi des mailles.
> 
> Ça veut dire que la somme des intensités entrantes est égale à l'opposé de la somme des intensités sortantes.
> $$i_1 + i_2 = i_3 + i_4$$
> 
> Cependant, une intensité peut être mesurée dans les deux sens, on peut donc tout mesurer comme si on avait que des intensités entrantes. On a juste à inverser $i_3$ et $i_4$
> $$i_1 + i_2 = (-i_3) + (-i_4)$$
> 
> Si on passe $i_3$ et $i_4$ de l'autre côté, on obtient $$i_1 + i_2 + i_3 + i_4 = 0$$
> 
> Si on généralise, on retrouve la vrai formulation de la loi des nœuds : la sommes des intensités en un point, toutes mesurées dans le même sens par rapport au nœud, est égal à zéro
> $$\sum_{n}{i_n} = 0$$
> 

> [!scene]- 5 / Calcul
> 
> > [!xav]+
> > Ok, donc en utilisant des résistance de 100K$\Omega$ avec 1% de tolérance et la même pile neuve que la dernière fois qui semble délivrer 1.57V, et mon ampèremètre qui a une exactitude à 1% on devrait avoir une mesure de 31.4$\mu$A plus ou moins 2%.
> 
> > [!theo]+
> > Exactement ! Ce qui nous fait une mesure entre 30.8$\mu A$ et 32$\mu A$ Aller, on passe à la pratique !
> 

> [!close-up]+ 6 / Mesure 
> 
> J'ai repris notre circuit avec nos deux branches et une pile neuve. Maintenant, si je mesure l'intensité après les branches, j'obtiens 31.X$\mu$A

> [!scene]- 7 / Conclusion
> 
> > [!xav]+
> > Et bha parfait ! Par contre, on a dû faire 3 vidéo pour en arriver là, y'a pas un moyen plus rapide ?
> 
> > [!theo]+
> > Si ! On aurait pu calculer la résistance équivalente de notre circuit.
> 
> > [!xav]+
> > HA ! C'est intéressant ça ! Tu me l'explique la prochaine fois ?
> 
> > [!theo]+
> > Avec plaisir ! Faisons un pas
> 
> > [!xav]+
> > après l'autre
> 
