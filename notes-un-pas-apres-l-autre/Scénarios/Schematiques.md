# Description
Aujourd'hui, on représente nos circuits sur le papier grâce à des schémas !
# Références
[[Faire bouger une boussole avec une patate]]
[[Faire une résistance avec une mine de criterium]]
[[Les unités en électronique]]
[[L'interrupteur]]
[[La porte ET]]

# Textes

> [!scene]- 1/ Intro
> 
> > [!xav]+
> > Bonjour
> 
> > [!theo]+
> > Salut !
> 
> > [!xav]+
> > Aujourd'hui, on pose nos idées sur le papier !
> 
> > [!theo]+
> > Oui ! on va faire de la schématique !
> 
> > [!xav]+
> > Le but, c'est de pouvoir faire un dessin qui représent notre circuit pour pouvoir réflechir dessus sans avoir besoin de tout monter.
> 
> > [!theo]+
> >  Et on veut aussi que ce soit super facile à dessiner hein ! Parce que clairement, j'ai pas fait les beaux arts !
> 
> > [!xav]+
> > Bon, on va pas tout voir tout de suite, mais on peut déjà regarder comment représenter les composants qu'on a débloqué non ?
> 

> [!manim]- 2 / Schemas
> 
> Oui, commençons par le plus simple de tous : le fil.
> 
> On peut le représenter avec un simple trait
> 
> ![[fil.excalidraw]]
> 
> ---------------
> 
> Ensuite, on a la [[pile]], qu'on représente avec deux barres verticales.
> La bare la plus longue représente l'anode, qu'on marque souvent avec un $+$ sur les piles.
> Et le côté le plus court représente la cathode.
> 
> ![[plie.excalidraw]]
> 
> -----------------
> 
> On peut représenter l'[[ampère-mètre]] avec un cercle et un $A$ dedans.
> 
> ![[ampère-mètre.excalidraw]]
> 
> -----------------
> 
> La [[résistance]] se dessine comme un fil en zigzag
> 
> ![[résistance.excalidraw]]
> 
> -----------------
> 
> Le [[ohm-mètre]] se dessine comme l'ampère-mètre mais avec un $\Omega$ à la place du $A$
> 
> ![[ohm-mètre.excalidraw]]
> 
> -----------------
> 
> Et enfin, l'[[interrupteur]] se représente comme un clapet.
> Ainsi, on peut le dessiner ouvert
> 
> ![[interrupteur.excalidraw]]
> 
> ---------------
> 
> Ou fermé
> 
> ![[interrupteur-fermé.excalidraw]]

> [!scene]- 3 / dialogue dessin
> 
> > [!xav]+
> > Et ce qui est top, c'est que ça marche aussi bien pour spintronics que pour l'électronique
> 
> > [!theo]+
> >Oui ! et d'ailleurs, je te propose de regarder quelques exemples
> 
> > [!xav]+
> > Ok, commençons par l'un de nos premier circuits, une pile avec une résistance.
>

> [!manim]- 4 / Pile + résistance
> 
> Pour représenter ce circuit, on dessine notre symbol de pile, celui de la résistance et celui de l'ampère-mètre. Enfin on relie le tout par des fils.
> 
> ![[Pile+résistance.excalidraw]]
> 
> --------------
> 
> Physiquement, en spintronics, ça donne ça.
> 
> ![[sprintronics-pile-resistance.png]]
> 
> --------------
> 
> Et en électronique, ça donne ça.
> 
> ![[electronics-pile-resistance.png]]
> 

> [!scene]- 5 / challenge
> 
> > [!xav]+
> > Et si on veut représenter le circuit qu'on a utilisé pour notre porte `ET` ?
> 

> [!manim]- 6 / [[Porte ET]]
> 
> Alors, on avait, une pile relié à une résistance, puis nos deux interrupteurs et l'amprè-mètre pour voir le signal passer.
> 
> ![[Port ET.excalidraw]]
> 
> ---------
> 
> C'est exactement ce qu'on avait en spintronics
> 
> ![[sprintronics-porte-et.png]]
> 
> ----------
> 
> Et en électronique, on avait remplacé notre combo pile / résistance / ampère-mètre par un ohm-mètre ce qui donne ce schema
> 
> ![[Porte-ET-ohm-metre.excalidraw]]
> 
> -------------
> 
> Et ce qui avait physiquement donné ça
> 
> ![[electronics-porte-et.png]]
> 
> -------------

> [!scene]- 7 / next step
> 
> > [!xav]+
> > C'est top ! Ça va nous simplifier la vie ! On passe au composant suivant ?
> 
> > [!theo]+
> > Oui, la jonction ! Et on aura plein de choses à dire dessus ! Ça va nous faire quelques vidéos !
> 
> > [!xav]+
> > Ok, on y va doucement alors, un pas…
> 
> > [!theo]+
> >… après l'autre !
