=> calcul du R général
=> démo avec un ohm mètre
=> idée du voltmètre => prochaine vidéo
# Description

Maintenant que l'on connait la loi des nœuds et la loi des mailles, on peut gagner du temps en calculant la résistance équivalente de notre circuit.

# Références
- loi d'ohm
- loi des nœuds
- loi des mailles
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
> > La dernière fois, tu me disais qu'on pouvais calculer la résistance équivalente de notre circuit. Mais, c'est quoi une résistance équivalente ?
> 
> > [!theo]+
> > Un résistance équivalente, c'est la valeur de la résistance que je devrais utiliser, si je voulais remplacer une partie du circuit par une seule résistance sans que cela n'ai le moindre impact pour le reste du circuit.
> 
> > [!xav]+
> > OK, et donc dans notre cas tu voudrais remplacer nos deux résistance par une seule, c'est ça ?
> 
> > [!theo]+
> > Oui, et maintenant qu'on a compris la loi des nœuds et la loi des mailles, on est capable de la calculer ! Regardes, je te montre
> 

> [!manim]+ 2 / Démonstration
> 
> Pour rappel, notre circuit est composé 
> - d'une pile délivrant une tension $U$
> - et de deux résistances, $R_1$ et $R_2$
>
> On peut noter l'intensité des deux branches $I_1$ et $I_2$
> 
> La loi d'ohm nous dit alors que: 
> - $U_1 = R_1 \times I_1$
> - $U_2 = R_2 \times I_2$
>
>
>
> On veut remplacer nos deux résistances par une seule résistance $R$, on devra donc avoir à la fin 
> $U = R \time I$
> 
> soit
> 
> $R = \frac{U}{I}$
> 
> La loi des mailles nous dit que $U_1 = U_2 = U$
> La loi des nœuds nous dit que $I_1 + I_2 = I$
> 
> 
> 
