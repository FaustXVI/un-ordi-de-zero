# Description
Aujourd'hui on créer un voltmètre !
# Références
- Résistance équivalente
- Les unités
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
> > Aller ! Je te montre comment je pense faire un volt-mètre ?
> 
> > [!theo]+
> > Vas-y, je t'écoute.
> 
> > [!xav]+
> > Je vais commencer par te montrer ce que ça donne en spintronics.
> 

> [!close-up]+ 2 / spintronics
> 
> Un voltmètre en spintronics, ça resemble à ça.
> 
> Si je prends un circuit simple, composé d'une pile et d'une résistance et que je veux mesurer le voltage aux bornes de ma résistance, je peux mettre mon voltmètre en parallèle.
> 
> Et si je fais tourner mon circuit
> 
> J'obtiens environ 7 spin-volts, ce qui est bien le voltage de la pile spintronics.
> 

> [!scene]- 3 / impact
> 
> > [!xav]+
> > La première chose à noter, c'est que le voltmètre est en parallèle du morceau de circuit qu'on veut mesurer.
> 
> > [!theo]+
> > Ce qui est normal puisque tu veux mesurer une différence de potentiel entre deux points.
> 
> > [!xav]+
> > Certes, mais pour la gestion de l'impact sur le circuit, ça change tout !
> 
> > [!theo]+
> > C'est à dire ?
> 
> > [!xav]+
> > Comme on l'a dit la dernière fois, ne pas avoir d'impact sur le circuit, ça veut dire avoir un résistance équivalente égale à la résistance du circuit sans notre instrument de mesure.
> 
> > [!theo]+
> > Exact.
> 
> > [!xav]+
> > Ce qui veut dire qui pour l'ampère-mètre et l'ohm-mètre qui se mettent en série, il faut avoir une résistance la plus proche de zéro.
> 
> > [!theo]+
> > Oui, jusque là, rien de surprenant.
> 
> > [!xav]+
> > Mais pour notre voltmètre qui est en parallèle, la résistance équivalente évolue en fonction de l'inverse de la résistance que l'on ajoute !
> 
> > [!theo]+
> > Oui, c'est le résumé de ce qu'on a dit la dernière fois.
> 
> > [!xav]+
> > Cela veut donc dire qu'on a besoin d'un voltmètre avec la résistance la plus grande possible !
> 
> > [!theo]+
> > Bien vu ! Et comment tu comptes faire ça ?
> 
> > [!xav]+
> > Pour faire un volt-mètre, je vais utiliser la loi d'ohm.
> 
> > [!theo]+
> > U = R I, pour rappel.
> 
> > [!xav]+
> > Si je mesure I dans ma branche grâce à un ampère-mètre, vu que j'aurais choisi R, je peux calculer U.
> 
> > [!theo]+
> > Parfait ! Et pour maximiser R il faudra que tu tienne compte de la sensibilité de ton ampère-mètre et de son exactitude !
> 
> > [!xav]+
> > J'y ai déjà réfléchi, je te montre.
> 

> [!manim]+ 4 / choix de R
> 
> Notre ampère-mètre peut mesurer des micro ampère avec un chiffre après la virgule soit une résolution à $10^{-7}$.
> 
> La résistance la plus grosse que j'ai à disposition est de $1M\Omega$ soit $10^6$.
> 
> Si je mesure une tension de $1.5V$ avec cette résistance, je devrait lire $1.5\mu A$ sur mon ampère mètre.
> 
> Cependant, si je tiens compte de la résolution de mon ampère mètre et de son exactitude de $\pm$ 1%, je me rends compte que ma mesure affichera quelque chose entre $1.4\mu A$ et $1.6\mu A$ ce qui se traduit par une imprécision de $\pm$ 10% ce que je trouve trop important.
> 
> Si j'utilise une résistance de $100K\Omega$ soit $10^5$, je devrait lire $15.0\mu A$ et en prenant en compte de nouveau la résolution et une exactitude de $\pm$ 1%, il devrait s'afficher quelque chose entre $14.8\mu A$ et $15.2 \mu A$ ce qui fait une imprécision de $\pm$ 2% qui est bien plus acceptable.
> 

> [!scene]- 5 / ok go
> 
> > [!theo]+
> > Ok, super, tu peux passer à la pratique !
> 

> [!close-up]+ 6 / création du voltmètre
> 
> J'ai fait un circuit contenant notre pile neuve et une résistance de $10\Omega$ qui est la plus petite que j'ai.
> 
> Je met maintenant en parallèle notre résistance de $100K\Omega$ et notre ampère-mètre.
> 
> Et on obtient $15.X \mu A$, multiplié par les $10^5$ de notre résistance, on obtient $1.5X V$
> 

> [!scene]- 7 / conclusion et porte ou
> 
> > [!theo]+
> > Ce qui est bien proche des $1.6V$ qu'on trouve souvent sur une pile neuve ! Bien joué, tu peux maintenant utiliser ton voltmètre comme tu veux !
> 
> > [!xav]+
> > Aller ! On passe à la suite ?
> 
> > [!theo]+
> > Oui, pour la prochaine fois, je te propose de regarder ce  qu'il se passe si on met deux interrupteurs en parallèle.
> 
> > [!xav]+
> > Ça semble parfait pour faire un pas
> 
> > [!theo]+
> > après l'autre.
> 
