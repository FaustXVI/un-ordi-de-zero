# Description

Aujourd'hui, on essaie de comprendre ce qui se passe dans le dernier circuit qu'on a fait avec deux résistances en parallèle.

# Références
[[Lois de Kirchhoff]] : https://www.youtube.com/watch?v=Hs1gesB3Lv4 (2 résistances en parallèle)
La [[résistance]] : https://www.youtube.com/watch?v=gGyxI5CayDM
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
> > Tout à fait.
>
> > [!xav]+
> > Mais ça c'est facile en fait. On a la [[loi d'ohm]], U=RI, or on connait R puisse qu'on choisie nos résistances et on connaît U, la tension de notre pile qu'on choisit aussi.
> 
> > [!theo]+
> > Stop !
> 
> > [!xav]+
> > Quoi ?
> 
> > [!theo]+
> > Je pense que tu pré-suppose beaucoup de chose. Par exemple, comment tu sais que les tensions aux bornes des résistances sont les même et qu'en plus elles sont égale à la tension de la pile ?
> 
> > [!xav]+
> > Euh, bah, c'est évident non ?
> 
> > [!theo]+
> > Mauvaise réponse ! Aller, on se fait une petite révision de la [[Lois de Kirchhoff#Loi des mailles|loi des mailles]]
> 

> [!manim]- 2 / [[Lois de Kirchhoff#Loi des mailles|loi des mailles]]
> 
> Pour rappel, la loi des mailles s'intéresse aux tensions, et les tensions c'est une histoire d'énergie. Il faut donc respecter la loi de conservation de l'énergie, c'est à dire que la somme des énergies consommées doit être égale à la somme des énergie produites.
> $$\sum_{n}{E\ consommée_n} = \sum_{n}{E\ produite_n}$$
> 
> Comme nous on parle d'électricité, on parle d'énergie par Coulomb, dit autrement, de tensions. On obtient donc :
> $$\sum_{n}{U\ consommée_n} = \sum_{n}{U\ produite_n}$$
> 
> Prenons un circuit très simple, composé d'une pile et d'une résistance.
> ![[Pile+résistance.excalidraw]]
> 
> La tension consommée par la résistance doit être égale à celle générée par la pile.
> 
> On constate que les flèches des tensions vont dans des sens différents par rapport au circuit, qu'on appel aussi maille.
> 
> Or, il est facile d'inverser le sens d'une flèche, il suffit de prendre la mesure dans l'autre sens.Cela reviens à mesurer une tension produite comme si c'était une tension consommée.
> 
> On aura juste une valeur négative dans le cas où il s'agit d'un tension produite mesurée à l'envers.
> 
> De plus, maintenant que toutes les flèches sont dans le même sens, on obtient ce que l'on appelle une maille orientée.
> 
> Si on reviens à notre équation, nous n'avons plus de tension produite, donc leur somme vaut zéro.
> $$\sum_{n}{U\ consommée_n} = 0$$
> 
> On retrouve alors la loi des mailles telle qu'elle est habituellement exprimée : 
> La somme des tensions dans une maille orientée est égale à zéro.
> $$\sum_{n}{U_n} = 0$$
> 
> Maintenant que nous avons correctement défini la loi des mailles, regardons ce que cela donne sur notre circuit.
> ![[2-resistances-parallel-amp.excalidraw]]
> On y vois une grande boucle composée de notre circuit ainsi qu'une petite boucle intérieure.
> 
> Les ampères mètres n'étant là que pour nous permettre de mesurer, on peut les supprimer le temps de notre réflexion.
> ![[2-resistances-parallel.excalidraw]]
> 
> On peut y placer 4 points, $a$ sur l'anode de notre plie, $b$ à la création des branches, $c$ à la fin des branches et $d$ sur la cathode de notre pile,
> 
> Dans notre boucle intérieure, la loi des mailles nous dit que $U_{bc} + U_{cb} = 0$ ce qui est plutôt logique puisqu'on mesure la même tension dans deux sens différents.
> 
> Notre boucle extérieure est plus intérésante.
> D'après la loi des mailles, on a $U_{ab} + U_{bc} + U_{cd} + U_{da} = 0$
> 
> $U_{da}$ est la tension consommée de notre pile, si on la met de l'autre côté on obtient $$U_{ab} + U_{bc} + U_{cd} = - U_{da}$$ soit $$U_{ab} + U_{bc} + U_{cd} = U_{ad}$$
> 
> Tu disais que la tension produite par la pile ,ici $U_{ad}$ était égale à la tension aux consommée par les résistances, ici $U_{bc}$. Et clairement, pour l'instant, ce n'est pas ça.
> Pourtant tu as vu juste car $U_{ab}$ et $U_{cd}$ sont sur le même fil sans rien au milieu. Quand on réfléchis théoriquement, on manipule des fils dits idéaux. Cela veut dire qu'ils ont la même tension du début à la fin.
> 
> Donc $U_{ab}$ et $U_{cd}$ sont tous deux égaux à zéro.
> 
> $$0 + U_{bc} + 0 = U_{ad}$$
> $$U_{bc} = U_{ad}$$
> 
> On a donc bien $U_{bc}$, la tension aux bornes des branches, qui est égal à $U_{ad}$ la tension de notre pile.
> 

> [!scene]- 3 / ok mais j'ai raison
> 
> > [!xav]+
> > Ok…
> > Bref! J'ai eu un coup de bol mais j'avais raison !
> 
> > [!theo]+
> > Oui
> 
> > [!xav]+
> > Donc si j'ai bien tout compris, je peux te faire les calculs regarde.
> 

> [!manim]- 4 / calcul de i
> 
> Pour chaque branche, la [[loi d'ohm]] nous dit :
> $$U = R \times I$$
> 
> Or on viens de dire que $U$ est égal à la tension de notre pile. Et comme on la choisie, on peut la fixer à la valeur que l'on veut, par exemple, $1.5\ V$
> $$1.5 = R \times I$$
> 
> Ensuite, dans la même logique, on choisie $R$ donc on peut y mettre valeur que l'on veut, par exemple $1000\ \Omega$
> $$1.5 = 1000 \times I$$
> 
> Donc $I$ est égal à 1.5 sur 1000
> $$\frac{1.5}{1000} = I$$
> 
> soit 0.0015 Ampères
> $$0.0015 = I$$
> 
> donc 1.5 milli-ampères

> [!scene]- 5 / Ok, check
> 
> > [!xav]+
> > C'était plutôt facile en fait !
> 
> > [!theo]+
> > On monte le circuit et on vérifie ça ?
> 

> [!close-up]- 6 / intensité dans les branches
> 
> Aller, j'ai refait le circuit sur une breadboard. On retrouve bien, notre pile, connecté à deux branches, une verte, une jaune qui contiennent toute les deux une résistance de 1000$\Omega$ et retournent à la pile.
> ![[2_résistances_parallèles_bb.png]]
> 
> Si je place l'ampère mètre sur la branche jaune, j'obtiens 1.5 mA
> ![[2_résistances_parallèles_branche_jaune_bb.png]]
> 
> Et si je me place sur la branche verte, j'obtiens 1.5 mA
> ![[2_résistances_parallèles_branche_verte_bb.png]]
> 

> [!scene]- 7 / et après ?
> 
> > [!theo]+
> > Super, c'est très proche de ce qu'on avait prédit !
> 
> > [!xav]+
> > Oui, enfin… 1.4 c'est pas 1.5 !
> 
> > [!theo]+
> > Oui, mais ça c'est normal.
> 
> > [!xav]+
> > Comment ça ?
> 
> > [!theo]+
> > Bha déjà, quand on passe en pratique, on a plein d’imprécisions héritant du matériel qu'on utilise. Et puis, en plus, tu n'utilises pas ton ampère mètre très bien :/
> 
> > [!xav]+
> > Comment ça j'utilise mal mon ampère mètre ?
> 
> > [!theo]+
> > Je t'explique tout ça la prochaine fois ok? Un pas…
> 
> > [!xav]+
> > après l'autre.
> 
