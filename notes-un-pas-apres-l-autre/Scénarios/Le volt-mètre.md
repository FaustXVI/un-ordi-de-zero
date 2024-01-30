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
> J'obtiens environ 6 spin-volts, ce qui est bien le voltage de la pile spintronics.
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
> > Aller, on passe à la pratique !
> 

> [!close-up]+ 4 / création du voltmètre
> 
> 


Résistance connue plus ampère-mètre => voltmètre
Objectif : impact minimal (les composants sont prévu pour fonctionner à un certain ampérage, on veut pas cramer le circuit en faisant une mesure, plus conso alim) => R au max et ampère-mètre sensible et mesure en parallèle

next vidéo => Porte ou