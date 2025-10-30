# Gestionnaire de tache TODO

## Description
Ce Programme est un gestionnaire de tâches en Python.  
Il nous permet d'ajouter, de supprimer, de lister, de marquer comme fait des taches ainsi que de quitter le programme.
J'ai mit un systeme de logs aussi.

## Installation/Exécution
Avoir python3 d'installer
Il faut télécharger main.py
Il faut lancer le programme dans le terminal:
python3 main.py
Votre programme marche avec les logs afficher

## Fonctionnalité du programme
Le menu du programme nous montre 5 choix:
1 Ajouter une tache
2 Lister les taches
3 Marquer les taches comme faite
4 Supprimer une tache
5 quitter le programme

Pour ne pas faire d'erreur dans le programme:
-Mettre les bon chiffre qui correspond au tache pour supprimer ou marquer une tache
-Le nom de la tache doit avoir obligatoirement un nom
-Si il y a une erreur un message vous le dit

## Choix technique
J'ai utiliser le module logging (todo.log) avec des niveaux de logs:
Info=C'est des actions normal ajouter,supprimer,lister,marquer une tache
Warning=C'est quand on va faire le mauvais choix ou que l'action ne marche pas
Error=Ca va être quand l'utilisateur va entrer un mot ou un texte au lieu d'un nombre
Critical=Pour les erreurs grave qui va empecher le programme de continuer normalement
J'utilise try/except pour controler les erreurs et eviter que le programme crash


