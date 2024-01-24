=> idée du voltmètre => prochaine vidéo
# Description

Maintenant que l'on connait la loi des nœuds et la loi des mailles, on peut gagner du temps en calculant la résistance équivalente de notre circuit.

# Références
- loi d'ohm
- loi des nœuds
- loi des mailles
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
> $U = R \times I$
> 
> La loi des mailles nous dit que $U_1 = U_2 = U$
> 
> On peut donc remplacer les tensions des équations précédentes :
> - $U = R_1 \times I_1$
> - $U = R_2 \times I_2$
>   
> La loi des nœuds nous dit que $I_1 + I_2 = I$
> 
> En utilisant les équations précédentes on trouve :
> - $I_1 = \frac{U}{R_1}$
> - $I_2 = \frac{U}{R_2}$
>   
> On obtiens alors :
>  $$I = \frac{U}{R_1} + \frac{U}{R_2}$$
> 
> Et en utilisant cela dans notre équation de la loi d'ohm pour notre circuit, on obtient :
>  
> $$U = R \times ( \frac{U}{R_1} + \frac{U}{R_2})$$
> 
> Et en passant $U$ et $R$ de l'autre côté, on obtient :
> 
> $$\frac{1}{R} = \frac{1}{U} \times ( \frac{U}{R_1} + \frac{U}{R_2})$$
> 
> On peut simplifier à droite en suppriment les $U$ :
> 
>  $$\frac{1}{R} = \frac{1}{R_1} + \frac{1}{R_2}$$
>  
>  Si on généralise pour $N$ résistances en parallèles, on trouve que l'inverse de la résistance équivalente est égale à la somme des résistances mises en parallèles.
>  
>  $$\frac{1}{R} = \sum\limits_{n}{\frac{1}{R_n}}$$
>  
>  ou encore que la résistance équivalente est égale à l'inverse de la somme des inverses des résistances mises en parallèles.
>  
>  $$R = \frac{1}{ \sum\limits_{n} {\frac{1}{R_n}} }$$
>  

> [!scene]- 3 / usage
> 
> > [!xav]+
> > Ok, d'accord… Je m'attendais à quelque-chose de plus simple !
> 
> > [!theo]+
> > Au final, la formule est assez simple à utiliser, et encore plus dans notre cas avec deux résistances égales ! Je te montre
> 

> [!manim]+ 4 / quick math
> 
> $$R = \frac{1}{\sum\limits_{n}{\frac{1}{R_n}}}$$
> 
> Comme les deux résistances sont égales, on peut les factoriser de la somme :
> 
> $$R = \frac{1}{\frac{1}{R_{branche}}\sum\limits_{n}{1}}$$
> 
> La somme est alors égale aux nombre de branches, soit deux.
> 
> $$R = \frac{1}{\frac{1}{R_{branche}}\times 2}$$
> 
> Et comme l'inverse de l'inverse d'une valeur est égale à la valeur elle-même, on obtient :
> 
> $$R = \frac{1}{2} R_{branche}$$
> 

> [!scene]- 5 / résultat
> 
> > [!xav]+
> > Donc nous, avec nos deux résistances de $100K\Omega$, la résistance équivalente est de $50K\Omega$
> 
> > [!theo]+
> > Exactement, et pour le confirmer, je te propose de mesurer la résistance du circuit avec un ohm-mètre
> 

> [!close-up]+ 6 / mesure
> 
> Donc là j'ai repris notre circuit avec nos deux branches, et si je place l'ohm-mètre sur tout le circuit, j'obtiens $50.XK\Omega$
> 

> [!scene]- 7 / conclusion
> 
> > [!theo]+
> > Ce qui est parfaitement dans notre marge d'erreur !
> 
> > [!xav]+
> > Ok, super ! Avec tout ce qu'on viens de voir, je crois que j'ai compris comment faire un volt-mètre !
> 
> > [!theo]+
> > Ça serait top ! Tu me montres ça la prochaine fois ?
> 
> > [!xav]+
> > Yes, faisons un pas 
> 
> > [!theo]+
> > Après l'autre
> 
