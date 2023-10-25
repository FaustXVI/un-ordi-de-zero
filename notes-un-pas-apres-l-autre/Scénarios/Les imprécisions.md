# Description

# Références

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
> > Bon, la dernière fois, j'ai fait des calculs pour prédire une intensité et quand j'ai mesuré, j'ai trouvé une valeur différente.
> 
> > [!theo]+
> > Oui, et moi je te disait que c'était normal.
> 
> > [!xav]+
> > Mais je vois pas pourquoi ! En théorie, la théorie et la pratique, c'est la même chose !
> 
> > [!theo]+
> > Oui, mais en pratique, c'est différent !
> 
> > [!xav]+
> > Bon, déjà, je me souviens que tu m'a dit que quand on réfléchissait théoriquement, on utilisait des fil idéaux. Je présume qu'en pratique, c'est pas le cas ? 
> 
> > [!theo]+
> > Tout à fait, et c'est le même problème avec tous les composants du circuit. Je te propose qu'on les regarde un par un et qu'on parle des imprécisions à chaque fois.
>  
> > [!xav]+
> > Et on met à jour le schéma théorique à chaque fois pour représenter ce qu'il se passe en vrai ?

> [!manim]- 2 / les résistances supplémentaires
> 
> Bonne idée, commençons par reprendre notre circuit théorique.
> ![[2-resistances-parallel-amp.excalidraw]]
> 
> Maintenant intéressons nous aux fils, qu'on représente par des simple traits dans nos schémas.
> ![[fil.excalidraw]]
> 
> La différence entre un fil en théorie et un fil en pratique, c'est qu'en vrai, les fils ont une résistance.
> Un fil pratique est donc en fait une résistance de faible valeur.
> ![[résistance.excalidraw]]
> 
> Mettons à jour notre schema avec cette information en changeant chaque fil pour y ajouter une résistance, en bleu pour les reconnaître.
> ![[2-resistances-parallel-amp-r-fil.excalidraw]]
> 
> Sans oublier qu'en pratique on a des fils qui vont de la pile à la breadboard et d'autres de l'ampèremètre à la breadboard  .
> ![[2-resistances-parallel-amp-r-all-fil.excalidraw]]
> 
> En plus, on utilise une breadboard, qui est aussi une forme de fil aussi. On ajoute donc des résistances en rose correspondantes à chaque fois qu'on passe dans la breadboard.
> ![[2-resistances-parallel-amp-r-breaboard.excalidraw]]
> 
> Et d'ailleurs, pour passer d'un fil à autre chose, on a des contacts à chaque fois, qui ont leur propre résistance qu'on peut représenter en orange.
> ![[2-resistances-parallel-amp-r-contact.excalidraw]]
> 
> Et enfin, il ne faut pas oublier que la pile a une résistance interne ainsi que les ampèremètres. Qu'on peut représenter en vert. 
>  ![[2-resistances-parallel-amp-r-all.excalidraw]]

> [!scene]- 3 / Sérieux
> 
> > [!xav]+
> > ....
> 
> > [!theo]+
> > ....
> 
> > [!xav]+
> > ....
> 
> > [!theo]+
> > ....
> 
> > [!xav]+
> > Et tu disais qu'on avait "quelques" imprecision ?
> 
> > [!theo]+
> > Oui, et ça, c'est que pour les fils.
> 
> > [!xav]+
> > Ok, mais, ça a vraiment un impact ?
> 
> > [!theo]+
> > Et bha, pour répondre à cette question, faisons une expérience.
> 

> [!close-up]- 4 / expérience des fils
> 
> Je reprends notre circuit et ne garde qu'une seule branche. Je remplace la résistances et la pile par des simples fils.
> 
> Maintenant, je mesure la résistance du circuit.
> 
> On obtient $XXX\Omega$. Et comparé à nos résistances de $1000\Omega$ c'est tout de même $XX.X\%$
>

> [!scene]- 5 / ouch
> 
> > [!xav]+
> > A oui quand même !
> 
> > [!theo]+
> > Oui, est c'est pas nos seuls imprécisions !
> 
> > [!xav]+
> > Je t'écoute.
> 
> > [!theo]+
> > Les résistances qu'on manipule ne sont pas exactement à la valeur indiquée. Il y'a a une tolérance, en occurrence, celles qu'on a utilisée une une valeur de $1000\Omega \pm 2\%$.
> 
> > [!xav]+
> > Ce qui nous ajoutes encore quelques $\Omega$ d'imprécision.
> 
> > [!theo]+
> > Et il y a la même choses pour les piles. Une pile neuve ne donne pas forcément exactement $1.5 V$, c'est d'ailleurs fréquent qu'elles délivres un peu plus.
> 
> > [!xav]+
> > Et puis, y'a le niveau d'usure de la pile aussi. Si j'utilise des vielles piles, j'aurais probablement moins que $1.5 V$.
> 
> > [!theo]+
> > Exact. Et enfin, on en arrive à la prise de mesure elle même.
> 
> > [!xav]+
> > Oui, tu me disait que j'utilisait mal l'ampèremètre ?
> 
> > [!theo]+
> > Oui, tu utilisais une résolution trop faible pour la mesure que tu faisais, et l'exactitude de la mesure peut alors te jouer des tours.
> 
> > [!xav]+
> > J'ai rien compris.
> 
> > [!theo]+
> > Je te fait un dessin, ça sera plus simple.
> 

> [!manim]- 6 / Exactitude, résolution et précision
> Mesurer quelque chose, ça veut dire place la valeur de la propriété qui nous intéresse sur un axe.
> Commençons donc par dessiner un axe sur lequel positionner nos valeurs.
> Pour notre exemple, imaginons qu'on veuille mesurer une valeur d'exactement $1.5mA$, représenté par ce point vert.
> 
> ![[axe.excalidraw]]
> 
> Notre premier problème, c'est que cette axe est de longueur infinie et qu'en pratique, on manipule des instruments de taille finie.
> Nous devons donc commencer par définir sur quelle partie de cette axe nous allons travailler.
> Une solution simple à se problème est de deviner une valeur maximal de ce que l'on veut mesurer. 
> 
> Par exemple, on sait que ce que l'on veut mesurer est entre $100\mu A$ et $10mA$.
> 
> ![[axe-segment.excalidraw]]
> 
> C'est exactement ce que tu fais quand tu configure ton ampèremètre ou quand tu choisi d'utiliser un double décimètre plutôt qu'un mètre.
> 
> Notre instrument de mesure peut alors déjà nous donner une information : est-ce que la valeur correspond à l'ordre de grandeur que nous avons estimé ou non.
> 
> Afin d'avoir plus d'information, on va alors découper notre axe en segments de longueur identique. Plus la longueur des segments sera petite, plus la résolution de notre mesure, c'est à dire le nombre de chiffres que nous pourrons lire, sera grande.
> 
> Si on divise notre morceau d'axe en 10 segments, chaque segment va représenter $1mA$.
> Si on le divise en 100 segments, chaque segment représentera $100 \mu A$.
> On peut mesurer faire des segments aussi petits que l'on veut, cela ne veut pas dire que notre mesure sera exact.
> ![[axe-scale.excalidraw]]
> 
> Quand on choisi notre fenêtre de mesure, notre ampèremètre choisis automatiquement la résolution maximal qu'il peut afficher.
>  
> L'exactitude de la mesure représente la proximité de notre mesure avec la valeur réelle.
> Dans notre exemple, une exactitude de $\pm 1\%$ veut dire que la mesure de $1.5 mA$ sera comprise entre $1.4 mA$ et $1.6 mA$.
> ![[axe-accuracy.excalidraw]]
> 
> D'après son manuel utilisateur, l'ampèremètre qu'on utilise a une précision de $\pm 1\%$.
> 
> Enfin, la précision nous indique à quelle point la mesure est reproductible.
> Dans notre exemple, si notre mesure est précise, et que nous avons lu $1.4 mA$ la première fois, si nous refaisons la mesure, nous lirons de nouveau $1.4 mA$.
> A l'inverse, si notre mesure est imprécise, nous pourrions lire $1.6 mA$ ce que reste dans notre fenêtre d'exactitude. 
> ![[axe-precision.excalidraw]]
> 

> [!scene]- 7 / Contre-mesure
> 
> > [!xav]+
> > Ok, compris. Donc j'aurais du mesurer en utilisant une configuration plus petite c'est ça ?
> 
> > [!theo]+
> >  Exactement.
> 
> > [!xav]+
> > Ok, et est-ce qu'on a moyen de minimiser l'impact de ces imprécisions ?
> 
> > [!theo]+
> > Déjà, on peut essayer de faire un montage physique le plus proche possible du montage théorique en utilisant le minimum de fils et de contacts possibles.
> 
> > [!xav]+
> > Ok, logique. Mais on aura toujours des fils et des contacts.
> 
> > [!theo]+
> > Oui, l'astuce est alors d'utiliser des résistances assez grandes pour que l'impact devienne négligeable. Si l'impact des imprécisions est en dessous d'un pourcent, ça sera très bien.
> 
> > [!xav]+
> > Ok, donc on utilise les plus gosses résistances possible ! J'en ai de $1M\Omega$, et on mesurera en $\mu A$
> 
> > [!theo]+
> > C'est une bonne idée, sauf qu'il faut aussi tenir compte de la précision et de la résolution de ton ampèremètre ! Dans sa configuration minimal de $200\mu A$  il mesurera au dixième de $\mu A$ près.
>
> > [!xav]+
> > Ah! Et du coup on va avoir le même problème de résolution qu'avant. 
> 
> > [!theo]+
> > Exactement.
>  
> > [!xav]+
> > Ok, donc on prends un cran en dessus : $100K\Omega$ et on mesure en toujours en $\mu A$ !
> 
> > [!theo]+
> > Parfait ! Y'a plus qu'à !
> 

> [!close-up]- 8 / Mesure V2
> 
> OK, donc là, j'ai utilisé le moins de fils possibles, des résistances de $100K\Omega$ et une pile neuve.
> Si je mesure l’ampérage de la première branche, j'obtiens $15.X \mu A$.
> Et si je mesure sur la seconde branche j'obtiens $15.Y \mu A$
> Maintenant, je change la pile neuve pour une pile usagée.
> Si je mesure l’ampérage de la première branche, j'obtiens $15.Z \mu A$.
> Et si je mesure sur la seconde branche j'obtiens $15.Z \mu A$

> [!scene]- 9 / ok next
> 
> > [!xav]+
> > Du coup je comprends bien mes mesures qui correspondent bien aux valeurs auxquelles je m'attendais. 
> 
> > [!theo]+
> > Super, on passe à la suite alors. A ton avis, si on met l'ampèremètre après les branches, quelle valeur  on va mesurer .
> 
> > [!xav]+
> > C'est une bonne question, mais la j'ai besoin de digèrer tout ce qu'on viens de voir. On regarde ça la prochaine fois ?
> 
> > [!theo]+
> > Ok, un pas...
> 
> > [!xav]+
> > ... après l'autre
> 
