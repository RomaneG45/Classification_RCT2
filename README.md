Ce dossier recense toutes les méthodes testées sur les données RCT2 :
- AC > 0
- AC > 2
- AC > 0 avec fenetre glissante non chevauchante de 2s
- AC > 2 avec fenetre glissante non chevauchante de 2s
- Seuil adaptatif de Coley
- Puissance > 1
- Puissance > 1 avec fenêtre glissante non chevauchante de 2s
- Puissance > 1 avec fenêtre glissante non chevauchante de 10s
- Random Forest entrainé sur les Activity Counts

Les méthodes suivent le même framework : 
1. Récupération des annotations et synchronisation avec les données d'accélération converties en AC
2. Pour les méthodes utilisant les données gyroscopiques (seuil adaptatif de Coley et puissances) : Récupération des données gyroscopiques
3. Codage du seuil avec les éventuelles fenêtres glissante non chevauchante
4. Nettoyage des AC et de leurs annotations
5. Calcul de l'accuracy et des F1 scores mouvement et non mouvement
6. Enregistrement dans les fichiers excel


Les données des capteurs aux poignets et au thorax sont synchronisés ensemble en se référant aux annotations "Start_LW"/"Start_RW"/"Start_thorax". Les codes sont utilisables sur toutes les données RCT2, sauf sur les 2 fichiers suivants : 04.06.02_MS_02 (ne contient aucun annotation "Start_Thorax") et 04.09.01_MS_02 (le fichier du thorax dure 3 sec).

Actuellement (31/12/2025), seulement les données des capteurs des poignets sont utilisés afin de detecter les mouvements des membres supérieurs. Dans une optique de détection de la marche, les capteurs du thorax pourront être utilisés (ils sont déjà synchronisés avec les capteurs des poignets).
