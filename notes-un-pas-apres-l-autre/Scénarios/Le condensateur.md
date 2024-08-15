# Description

# Références

Voltmètre

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
> > Aujourd'hui, on s'intéresse aux condensateurs.
> 
> > [!theo]+
> > Oui, et on a du pain sur la planche ! du coup, je te propose de tout de suite regarder ce que ça donne en spintronics.

> [!close-up]+ 2 / name
> 
> Un condensateur en spintronics, c'est la même pièce que le voltmètre.
> 
> Si on le branche à notre pile
> Et qu'on démarre le tout
> 
> Ça fini par s'arrêter

> [!scene]- 3 / name
> 
> > [!xav]+
> > On dirait que c'est une résistance variable dans le temps.
> 
> > [!theo]+
> > Alors, c'est pas faux, mais comment on la ferait varier dans l'autre sens ?
> 
> > [!xav]+
> > Je sais pas, en la débranchant ?
> 
> > [!theo]+
> > Essaie pour voir
> 

> [!close-up]+ 4 / name
> 
> Wow !
> 

> [!scene]- 5 / name
> 
> > [!theo]+
> > Voilà ! c'est ça la vrai utilité d'un condensateur !
> 
> > [!xav]+
> > Euh, c'est à dire ?
> 
> > [!theo]+
> > Ça stock de l’énergie. Méchanique en spintronics et éléctrique en éléctronique.
> 
> > [!xav]+
> > Ok, pourquoi pas, mais je vois toujours pas le cas d'usage.
> 
> > [!theo]+
> > Y'en a plein, mais l'un des plus évident et que ça permet de compenser les petites coupures d'alimentation. Je te montre avec un circuit spintronics.
> 

> [!close-up]+ 6 / name
> 
> Là , j'ai un circuit simple, composé d'une pile, d'une résistance et d'un interrupteur pour couper l'alimentation.
> J'ai aussi mis un condensateur en parallèle de la résistance.
> 
> Si je démarre le circuit, tout se déroule comme d'habitude.
> Mais si je l'arrête
> Ça continue de tourner
> 
> Alors là ça c'est arrêté parce que la coupure a été longue. Mais si on recommence avec des coupures courtes.
> 
> La résistance ne s'est jamais arrêté de tourner !

> [!scene]- 7 / name
> 
> > [!xav]+
> > Ok, sympa. Et comment on en fabrique un en éléctronique ?
> 
> > [!theo]+
> > Avec 2 feuilles d'alu et une feuille de papier
> 
> > [!xav]+
> > Euh… il va falloir m'en dire plus là !
> 
> > [!theo]+
> > ok mais on va avoir besoin de regarder un peut se qu'il se passe à l'échelle de l'électron. Pour ça on va se faire quelques simulations. Alors, je te préviens tout de suite, les simulations vont s'appuyer sur un modèle simplifié et on va prendre quelques raccourcis, mais au vu de ce qu'on cherche à comprendre et de nos connaissances actuelles, ça sera largement suffisant.
> 

> [!manim]+ 8 / simulation
> 
> Comme tu le sais, la matière est composé d'atomes. 
> Nous allons représenter chaque atome éléctriquement neutres par un point jaune.
> 
> Un atome qui a un surplus d'éléctron sera représenté par un point bleu avec un signe moins dedans, signifiant que l'atome a une change négative supplémentaire.
> 
> Un atome qui a un déficite d'éléctron sera représenté par un point rouge avec un signe plus dedans, signifiant que l'atome a une change négative manquante qu'on peut voir comme une charge positive.
> 
> Prenons un cas très simple : un carré de matière avec une seul charge négative.
> 
> L'éléctron peut se déplacer librement, on parle d'ailleurs d'éléctron libre. Pour simuler ça, les charges (négatives ou positivent) peuvent soit se déplacent de manière aléatoires sur un atome voisin ou soit rester sur place.
> 
> Pour savoir ce qu'il se passe quand on a deux charges, il faut s’intéresser à la loi de Coulomb.
> 
> Elle nous nous dit que les signes opposés s'attirent et que les signes identiques se repoussent.
> 
> L'intensité de cette force est donnée par la formule :
> $k_0 \frac{|q_1 \times q_2|}{r^2}$
> 
> où k0 est une constante
> q1 et q2 sont les charges concernées
> r est la distance entre les deux charges
> 
> Donc pour deux même charges, plus la distance est grandes moins la force est importante.
> 
> Reprenons notre carré de matière, mais avec deux charges négatives cette fois si.
> 
> Les charges de même signe se repoussent. Pour simuler ça, au moment du choix de la prochaine position de la charge, on favorise le choix des positions les plus éloignés des autres charges de même signe. On vois donc bien que les deux charges se rapprochent presque jamais.
> 
> Si on recommence avec une charge négative et une charge positive.
> 
> Les charges de signe contraires s'attirent. Pour simuler ça, au moment du choix de la prochaine position de la charge, on favorise le choix des positions les plus proches des autres charges de signe opposés. On vois donc bien que les deux charges se rapprochent très vites et restent collées. En réalité, quand elles se rencontres, les deux charges s'annuleraient et notre carré finirait électriquement neutre.
> 
> Maintenant que les bases sont posés. Prenons le coté négatif d'une pile. On peut le représenté comme étant une masse d'atomes négativement chargés.
> 
> Prenons un fil électriquement neutre que nous mettons en contact avec le côté négatif de la pile.
> 
> On vois que les charges se répartissent rapidement dans la matière et que le fil contient maintenant des charges négatives. Les charges vont se répartir de manière égales dans la matière. On dit alors que le fil est à équipotentiel de la batterie. Si on enlève soudainement la pile et qu'on met sur pause.
> 
> On vois qu'il reste des charges négatives dans le fil (X dans notre simulation).
> Et ça, c'est très intéressant pour nous car c'est une forme de stockage ! Le but maintenant, et d'augmenter le nombres de charges contenus dans notre dispositif quand on enlève la pile.
> 
> Pour commencer, il faut qu'on face la même chose de l'autre côté de la pile. Sinon on n'arrivera pas  à brancher notre condensateur à un circuit.
> 
> Ensuite, la première avancées qu'on peut faire, c'est de se rendre compte que plus on a de matière, plus on a de place pour les charges. On peut donc mettre deux grandes plaques de chaque côté.
> 
> Si on lance notre simulation et qu'on la laisse tourner un petit moment … et qu'on enlève la pile d'un coup.
> 
> On obtient N charges négatives, ce qui est mieux que les X d'avant. On a aussi P charges positives.
> 
> Si on se rappelle la loi de Coulomb, les opposés s'attirent mais l'intensité de cette force diminue avec le carrée de la distance.
> 
> Si on rapproche les deux plaques, les charges opposés seront plus proches et ça pourrait nous aider.
> 
> Aller, on se fait le même circuit en rapprochant les plaques.
> 
> On laisse de nouveau tourner notre simulation pendant un petit moment … et on enlève la pile d'un coup.
> 
> On obtient NN charges négatives et PP charges positives. C'est beaucoup mieux. On voit d'ailleurs que les charges se concentrent à la surface des plaques.
> 
> Enfin, si je diminue le voltage de la pile en mettant moins de charges dedans.
> 
> Qu'on fait tourner de nouveau notre simulation un peu … et qu'on enlève la pile.
> 
> On voit qu'on a que ZZ charges négatives et YY charges positives.
> 
> On viens donc de comprendre que :
> 
> Q, le nombre de charges contenus dans notre condensateur
> 
> augmente avec A, la surface de nos plaques.
> diminue avec d, la distance entre nos plaques.
> augmente avec V, le voltage de notre pile.
> 
> Et en effet, la formule du nombre de charges dans un condensateur est :
> $Q = \epsilon_{0} \times \frac{A}{d} \times V$
> 
> $\epsilon_{0}$ étant une constante dépendante de la matière isolante contenue entre les deux plaques.
> 
> Pour un même voltage $V$ ce qui distingue une capacité d'une autre c'est donc $\epsilon_{0} \times \frac{A}{d}$.
> 
> Cette valeur est donc caractéristique d'un condensateur et est noté C. On l’appelle la capacitance et elle se mesure en Farad noté F.
> 
> 1 Farad = 1 Coulomb par Volt
> 
> Enfin, le symbole utilisé dans les schémas électroniques représentent exactement ce qu'on viens de simuler, à savoir deux plaques séparées par un gap.

> [!scene]- 9 / name
> 
> > [!xav]+
> > Donc si je comprends bien, ton idée est d'utiliser deux feuilles d'alu pour faire les plaques et une feuille de papier pour faire un isolant le plus fin possible.
> 
> > [!theo]+
> > Exactement ! Et si tu écrase le tout avec un poids pour éviter d'avoir de l'air entre les deux plaque, ça nous donnera le meilleur condensateur qu'on puisse faire avec du matériel de tous les jours.
> 
> > [!xav]+
> > Ok, et pour tester on regarde l'intensité. Sans condensateur, on passera tout de suite à zéro alors qu'avec un condensateur, ça prendra plus de temps. C'est ça ?
> 
> > [!theo]+
> > C'est l'idée oui.
> 

> [!close-up]+ 10 / à vide
> 
> Donc là, je fais le test sans condensateur.
> Pour l'instant j'ai une intensité XX (saturée ?)
> Et si je coupe,
> Je tombe à zéro, mais ça prend un peu de temps

> [!scene]- 11 / name
> 
> > [!xav]+
> > Comment ça se fait ça ?
> 
> > [!theo]+
> > Parce que notre multimètre contient des condensateurs. Et qu'ils sont d'ailleurs de bien meilleure qualité que ce qu'on va arriver à produire. Et ça, ça va nous causer de problèmes
> 
> > [!xav]+
> > Et avec ça ? c'est que de la mécanique
> 
> > [!theo]+
> > Vu la qualité du condensateur qu'on va produire, rien que l'inertie de l'aiguille va nous fausser la mesure.
> 
> > [!xav]+
> > On fait comment alors ?
> 
> > [!theo]+
> > On peut ajouter des interrupteurs pour que le courant ne passe pas par notre ampère-mètre pendant la charge de notre condensateur. Un autre interrupteur nous permettra de vider le condensateur via l'ampère-mètre
>  

> [!close-up]+ 12 / name
> 
> OK, bonne idée. Regarde, je viens de faire le circuit.
> 
> Donc quand j'appuie sur le premier bouton, je charge notre condensateur et l'ampère-mètre reste à zéro.
> 
> Et maintenant je vais arrêter la charge et basculer rapidement sur l'ampère mètre.
> 
> Et y'a absolument rien qui se passe…
> 

> [!scene]- 13 / name
> 
> > [!theo]+
> > Oui, c'est pas étonnant.
> 
> > [!xav]+
> > Pourquoi ?
> 
> > [!theo]+
> > Parce que toutes les charges partent trop vite. L'ampère mètre n'a pas le temps de les détecter.
> 
> > [!xav]+
> > Et on fait comment alors ?
> 
> > [!theo]+
> > Là tu es en court circuit, donc le courant va passer aussi vite que possible. Si tu ajoute une résistance, tu devrais voir quelque chose.
> 

> [!close-up]+ 14 / name
> 
> Ok, j'ai le même circuit avec une résistance en plus.
> 
> Je charge le condensateur…
> 
> Et je bascule vers l'ampère mètre.
> 
> Et effectivement, ça bouge.

> [!scene]- 15 / name
> 
> > [!xav]+
> > Par contre, ça bouge pas beaucoup et pendant pas longtemps !
> 
> > [!theo]+
> > Oui, c'est pas un très gros compensateur qu'on viens de faire et on est pas loin des limites de notre matériel.
>  
> > [!xav]+
> > J'aimerais bien voir quelque chose de mieux quand même.
> 
> > [!theo]+
> > Si tu regardes notre circuit, en fait, on viens de faire un voltmètre
> 
> > [!xav]+
> > Ah oui !
> 
> > [!theo]+
> > Le voltmètre de notre multimètre est très probablement de meilleur qualité que ce qu'on viens de faire. Si tu l'utilise, tu verras probablement quelque chose pendant plus longtemps.
> 

> [!close-up]+ 16 / name
> 
> Aller, on essaie. J'ai retiré notre résistance et utilise notre ampère-mètre en tant que voltmètre.
> 
> Je charge le condensateur…
> 
> Et je bascule vers le voltmètre.
> 
> Ah ! Là on vois quelque chose !

> [!scene]- 17 / name
> 
> > [!theo]+
> > Pfiou ! Et bha maintenant on peut utiliser des condensateurs modernes !
> 
> > [!xav]+
> > Et qu'est-ce qu'il se passe quand on en met deux dans un circuit ?
> 
> > [!theo]+
> > Je te propose de garder ça pour la prochaine fois, on a déjà vu beaucoup de choses pour aujourd'hui !
> 
> > [!xav]+
> > Oui, tu as raison, un pas…
> 
> > [!theo]+
> > après l'autre !
> 
