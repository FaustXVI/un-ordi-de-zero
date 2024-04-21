# Description

# Références
- Porte ET
- Interrupteurs
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
> > La dernière fois, on en était à se poser la question de ce que donnerait deux interrupteurs en parallèles. 
> 
> > [!theo]+
> > Aller, on saute dans le bain tout de suite et on regarde ce que ça donne en spintronics
> 

> [!close-up]+ 2 / spintronics
> 
> On a donc, notre pile, une résistance pour éviter les cours circuits, et deux interrupteurs en parallèle qui sont actuellement ouverts et on voit que rien ne tourne.
> 
> Si je ferme le premier, ça tourne.
> 
> Si je réouvre le premier et ferme le second, ça tourne aussi.
> 
> Enfin, si je ferme les deux en même temps, ça tourne toujours.
> 

> [!scene]- 3 / observation
> 
> > [!xav]+
> > C'est marrant on dirait que ça se comporte à l'inverse d'une porte ET.
> 
> > [!theo]+
> > Oui, c'est parce que c'est une porte OU ! C'est flagrant si on regarde leurs tables de vérité !
> 
> > [!xav]+
> > Leur quoi ?
> 
> > [!theo]+
> > Ouais, ça mérite un dessin !
> 

> [!manim]+ 4 / table de vérité
> 
> Tout ce qui va suivre tourne autour de l'affirmation suivante : `Du courant passe.`
> 
> Ainsi, si on prends un circuit simple contenant juste une pile et un interrupteur. 
> 
> Quand l'interrupteur est ouvert, l'affirmation est `Fausse`, car aucun courant ne passe. 
> 
> Quand l'interrupteur est fermé, l'affirmation est `Vrai`, car du courant passe.
> 
> Tout ce joue donc sur l'état de l'interrupteur.
> Quand il est ouvert, on est dans l'état `Faux` : le courant ne passe pas
> Quand il est fermé, on est dans l'état `Vrai` : le courant passe
> 
> On peut maintenant regarder ce qu'il se passe quand on met deux interrupteurs dans le circuit en faisant un tableau avec les états du premier interrupteur en colonnes et les états du second en ligne.
> 
> En logique, on appelle ces tableaux des tables de vérités. Et chaque opération logique, comme le `ET` ou le `OU`, on leur propre table de vérité.
> 
> Par exemple, pour l'opération `ET` on obtient
> 
> `FAUX` et `FAUX` donne `FAUX`
> 
> `VRAI` et `FAUX` donne `FAUX`
> 
> `FAUX` et `VRAI` donne `FAUX`
> 
> `VRAI` et `VRAI` donne `VRAI`
> 
> Ce qui correspond bien à ce qu'on avait observé lors de la création de notre porte `ET`.
> 
> Si maintenant on regarde l'opération `OU` on obtient
> 
> `FAUX` et `FAUX` donne `FAUX`
> 
> `VRAI` et `FAUX` donne `VRAI`
> 
> `FAUX` et `VRAI` donne `VRAI`
> 
> `VRAI` et `VRAI` donne `VRAI`
> 
> Ce qui correspond bien à notre circuit actuel.
> 

> [!scene]- 5 / go pratique
> 
> > [!xav]+
> > Ok, c'est clair ! Aller on passe à la version électronique !
> 

> [!close-up]+ 6 / electronique
> 
> J'ai donc, notre circuit avec une pile et une résistance pour éviter les court circuit, nos deux interrupteurs en parallèle et un ampère-mètre pour voir le courant passer.
> 
> Quand les deux interrupteurs sont ouvert, rien ne passe, on a bien 0.
> 
> Quand j'appuie sur le premier, du courant passe.
> 
> Quand j'appuie sur le second, du courant passe.
> 
> Et enfin, quand j'appuie sur les deux, du courant passe.

> [!scene]- 7 / conclusion
> 
> > [!theo]+
> > Et bha super ! On a maintenant deux portes logiques à notre disposition !
> 
> > [!xav]+
> > Ok, et ensuite on regarde ce que ça donne quand on met deux piles en parallèles ?
> 
> > [!theo]+
> > Alors là, pour être honnête, on est pas prêts pour en parler.
> 
> > [!xav]+
> > Ok, on repousse au jour où on en aura besoin alors. Mais du coup, on fait quoi après ?
> 
> > [!theo]+
> > Bha on commence à avoir fait le tour de ce qu'on peut faire avec les composant qu'on a pour l'instant. 
> 
> > [!xav]+
> > On passe au composant suivant alors ! C'est quoi ?
> 
> > [!theo]+
> > Le condensateur ! Ça me semble parfait pour faire un pas
> 
> > [!xav]+
> > Après l'autre !
> 

