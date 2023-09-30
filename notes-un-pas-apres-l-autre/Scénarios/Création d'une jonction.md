# Titre
Faire une jonction avec un trombone
# Description
Aujourd'hui, on fait des jonctions pour faire passer le courant dans deux branches en même temps.
# Références
La schématique fin sc5
# Textes

> [!scene]- 1 / intro
> 
> > [!xav]+
> > Bonjour !
> 
> > [!theo]+
> > Salut !
> 
> > [!xav]+
> > Aujourd'hui on s'intéresse aux [[jonction]]s.
> 
> > [!theo]+
> > Alors, une jonction, en fait c'est tout simple hein. C'est ce qui permet de passer de 1 seul fil à deux ou plusieurs fils.
> 
> > [!xav]+ Xav, dessin en live
> > Ok, ça, c'est facile à dessiner. On dessine notre fil de départ et on fait une fourche pour le séparer en deux. Ça le fait non ?
> > ![[jonction.excalidraw]]
> 
> > [!theo]+
> > Tout à fait, c'est totalement comme ça qu'on la représente dans un schéma. Aller, je te montre ce que ça donne en spintronics !
> 

> [!close-up]- 2 / spintronics
> 
> Pour rappel, en spintronics, les fils sont représentés par des chaines. La jonction, permet donc de passer d'une seule chaîne à deux chaînes. On peut par exemple faire tourner deux résistances sur deux chaînes différentes.
> 

> [!scene]- 3 / un trombone
> 
> > [!xav]+
> > Ok, et en éléctronique, comment on peut faire ça ?
> 
> > [!theo]+
> > De plein de manière différentes. Dès qu'on passe d'un seul fil à deux, on a une jonction. Donc par exemple, si on coupe un fil dans la longueur, on a une jonction.
> 
> > [!xav]+
> > Euh,  j'ai pas très envie de couper mes fils.
> 
> > [!theo]+
> > Pas besoin, regarde, nous on utilise des fils qui ont des pinces crocodile au bout. Du coup, une simple tige métallique nous permettant de mettre 3 fils fera l'affaire. Un trombone déplié par exemple.
> 
> > [!xav]+
> > Ok, partons sur le trombone. Pour valider que ça marche, il faut qu'on voie passer le courant dans les deux branches en même temps. J'ai une idée de circuit, je te montre
> 

> [!manim]- 4 / schéma
> 
> On va bien entendu avoir une [[pile]], puis notre [[jonction]].
> 
> On va faire deux branches identiques avec :
>   - une [[résistance]] pour éviter les courts circuits
>   - un [[ampère-mètre]] pour voir le courant passer
>    
>    ![[sc-Jonction 2023-09-23 16.20.43.excalidraw]]
> 
> Si notre [[jonction]] fonctionne correctement, on verra une valeur sur les deux [[ampère-mètre]]s en même temps.

> [!scene]- 5 / go éléctronique
> 
> > [!theo]+
> > Super ! Et puis ça correspond bien à ce qu'on a fait en spintronics !
> 
> > [!xav]+
> > Par contre, c'est marrant, sur mon schéma, j'ai deux jonctions en fait. Une qui sépare un fil en deux et l'autre qui prends deux fils pour n'en donner qu'un
> 
> > [!theo]+
> > Oui, c'est normal, il faut bien que les deux branches qui tu créer finissent sur l'anode de la [pile] !
> 
> > [!xav]+
> > Ok, mais du coup, il va me falloir deux trombones pour le faire en électronique.
> 
> > [!theo]+
> > Tout à fait ! Ce rendre compte de ce genre de choses, c'est tout l’intérêt des schémas ! On passe à la pratique ?
> 

> [!close-up]- 6 / utilisation des trombones
> 
> Aller ! J'ai donc une pile et deux branches qui contiennent toutes les deux une [[résistance]] et un [[ampère-mètre]]. Quand je branche… je vois bien les deux [[ampère-mètre]] bouger !
> 

> [!scene]- 7 / Breadboard
> 
> > [!theo]+
> > Excellent ! Et regarde ce que ça te permet d'utiliser !
> 
> > [!xav]+
> > C'est quoi ce machin ?
> 
> > [!theo]+
> > Ça s'appelle une breadboard. En fait c'est simple, c'est plein de jonctions en colonnes ou en lignes. Ça te permettre de relier tes composants sans avoir trop de fils super long qui traînent partout !
> 
> > [!xav]+
> > Ah ! bha c'est le bien venu parce que ça commençait à prendre de la place !
> 
> > [!theo]+
> > Bon, par contre, on est loin d'avoir tout vu hein ! Par exemple, on a vu nos ampères-mètres bouger, mais pour l'instant on sais pas prédire la valeur qu'ils vont afficher !  Ni ce qu'afficherai un ampère-mètre après que les deux branches se rejoignent.
> 
> > [!xav]+
> > Oulà ! Je te vois venir ! Tu vas me donner plein de formules et faire des calculs compliqués ! On se fait ça une prochaine fois ?
> 
> > [!theo]+
> > Ok ok, un pas…
> 
> > [!xav]+
> > Après l'autre
> 
