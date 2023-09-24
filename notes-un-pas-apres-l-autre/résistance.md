# Schéma
![[résistance.excalidraw]]
# Création 
https://www.youtube.com/watch?v=gGyxI5CayDM

# [[Unités]]
le ohm noté $\Omega$
# Deux résistances
La [[loi d'ohm]]  dit  :  $$ U =  R \times I $$
On a deux résistances donc :
$$U_1 =  R_1 \times I_{R_1}$$
$$U_2 =  R_2 \times I_{R_2}$$
## En série
https://www.youtube.com/watch?v=Hs1gesB3Lv4

La [[Lois de Kirchhoff#Loi des mailles|Loi des mailles]] dit :
$$ U = U_{R_1} + U_{R_2}$$
donc $$U = R_1  \times I_{R_1} + R_2 \times I_{R_2}$$
La [[Lois de Kirchhoff#Loi des nœuds|Loi des nœuds]] dit : $$  I = I_{R_1} = I_{R_2} $$
Ce qui  donne  : $$
U = R_1 \times I + R_2 \times I = (R_1 + R2) \times I
$$
Donc $$ R  = R_1 + R_2 $$

## En parallèle

$U$  est le même pour toutes les branches donc $$  U_1  = U_2 = U $$
Donc : $$U =  R_1 \times I_{R_1}$$
$$U =  R_2 \times I_{R_2}$$

La [[Lois de Kirchhoff#Loi des nœuds|loi  des nœuds]] dit  :  $$I = I_{R_1} + I_{R_2}$$
soit : $$I = \frac{U}{R_1} + \frac{U}{R_2} $$
$$I = U \times  (\frac{1}{R_1} + \frac{1}{R_2}) $$
$$U = I \times  \frac{1}{\frac{1}{R_1} + \frac{1}{R_2}} $$
$$U = I \times  \frac{1}{\frac{R_2}{R_1 \times R_2} + \frac{R_1}{R_1 \times R_2}}$$
$$U = I \times  \frac{R_1 \times R_2}{R_1 + R_2}$$
donc : 
$$R = \frac{R_1 \times R_2}{R_1 + R_2}$$
