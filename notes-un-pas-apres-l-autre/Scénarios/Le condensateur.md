# Description

# Références

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
> >
> 
> > [!theo]+
> >

> [!manim]+ N / simulation
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
