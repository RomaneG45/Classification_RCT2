# Classification_RCT2

## Ce repositorie contient les codes de plusieurs méthodes de détection du mouvement, le but du projet étant trouver la méthode optimale en comparant les prédictions obtenues avec chaque seuil, aux annotations vidéos recueillies dans l'essai RCT2.

## Les différentes méthodes testées
- Seuil AC>0
- Seuil AC>0 avec fenetres glissantes non chevauchantes de 2s
- Seuil AC>2
- Seuil AC>2 avec fenetres glissantes non chevauchantes de 2s
- Seuil adaptatif de Coley, basé sur la vitesse angulaire (voir rapport mindmaze)
- Puissance > 1 (avec puissance = accX*gyrX + accY*gyrY + accZ*gyrZ (acc = données d'accélération à chaque seconde, et gyr = données de rotation à chaque seconde)
- Puissance > 1 avec fenetre glissantes non chevauchantes de 2s
- Puissance > 1 avec fenetre glissantes non chevauchantes de 10s
- RandomForest sur les Activity Counts (Imbalanced Random Forest avec validation croisée en LeaveOneOut)

## Résultats et conclusions
Les méthodes AC>0, AC>0 avec fenetre de 2s, AC>2, AC>2 avec fenetre de 2s, puissance>1, puissance>1 avec fenetre de 2s et le seuil adaptatif de Coley montrent des résultats généraux bons, mais une prédiction de la sédentarité très mauvaise (résultats retrouvés dans la littérature).
En revanche, Random Forest présente des taux d'accuracy moyens, bien inférieurs aux autres méthodes.
Les fenetres glissantes de 10 secondes ne paraissent pas non plus adaptée au public : elles prédisent trop de mouvement, inhibant les secondes de sédentarité qui sont souvent bien plus courtes que 10s. Les scores généraux sont satisfaisants, mais les scores de prédictions de la sédentarité sont bien inférieurs aux autres méthodes.

## Structures des codes
La même méthode est appliquée pour tester les différents seuils :
1. Récupération des données actimétriques, transformation en Activty Counts et synchronisation avec les annotations vidéos et entre les différents capteurs. Les annotations étant définies aux millièmes de seconde près, un vote à la majorité est effectué pour réduire à une annotation par seconde. Par exemple, si l'annotation "mouvement" est présente jusque la seconde 10,786 : la seconde 10 est définie comme "mouvement", car le temps dépasse la moitié d'une seconde. L'affichage graphique permet ensuite de vérifier la bonne synchronisation des données.
2. Facultatif suivant la méthode : récupération et nettoyage des données gyroscopiques.
3. Création et prédiction du seuil
4. Nettoyage des données et des annotations: suppression des secondes sans information sur le mouvement (annotations "non noté" et secondes représantant le décalage entre 2 annotations ou en extrémité d'enregistrement).
5. Calcul des métriques : Accuracy et F1 scores (F1 mouvement, F1 non mouvement)
6. Enregistrement dans des fichiers Excel de sortie.



