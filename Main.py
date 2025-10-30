import logging

# --- Configuration du système de logs ---
logging.basicConfig(
    filename="todo.log",  # nom du fichier où seront écrits les logs
    level=logging.DEBUG,  # niveau de détail des messages (DEBUG = tout)
    format="%(asctime)s - [%(levelname)s] - %(message)s"  # format du message
)

logging.info("Démarrage du gestionnaire de tâches")

taches = []

"""Afficher le menu """
def afficher_menu():
    """Affiche le menu avec les options disponibles pour l'utilisateur"""
    print("\n--- Gestionnaire de Todo ---")
    print("1. Ajouter une tâche")
    print("2. Lister les tâches")
    print("3. Marquer une tâche comme faite")
    print("4. Supprimer une tâche")
    print("5. Quitter")

    """Boucle principale du programme"""
while True:
    """Affiche le menu pour chaque tour de boucle"""
    afficher_menu()
    
    """choix de l'utilisateur"""
    choix = input("Choix : ")

    """Vérifie si le choix est valide"""
    if choix not in ["1", "2", "3", "4", "5"]:
        """Si le choix n'est pas dans le menu affiche un message et continue"""
        print("Choix invalide.")
        continue

    """Ajouter une tâche"""
    if choix == "1":
        """Demande le nom de la tâche et enleve les espaces inutiles"""
        nom = input("Nouvelle tâche : ").strip()
        
        """Si il n'y a rien affiche un message"""
        if not nom:
            print("Le nom de la tâche ne peut pas être vide.")
        else:
            """Ajoute la tâche à la liste avec l'état 'faite' à False"""
            taches.append({"nom": nom, "faite": False})
            print("Tâche ajoutée.")

        """Lister les tâches"""
    elif choix == "2":
        """S'il n'y a rien affiche un message"""
        if not taches:
            print("Aucune tâche.")
        else:
            """Sinon regarde chaque tâche et affiche son numéro avec son état et son nom"""
            for i, t in enumerate(taches, 1):
                statut = "✅" if t["faite"] else "❌"
                print(f"{i}. {statut} {t['nom']}")
   
        """Marquer une tache comme fait"""
    elif choix == "3":
        """Si il n'y a rien affiche un message"""
        if not taches:
            print("Aucune tâche à marquer.")
            continue
        try:
            """Demande le numéro de la tâche et le convertit en index"""
            i = int(input("Numéro de la tâche : ")) - 1
            if 0 <= i < len(taches):
                """Change l'état de la tâche à True"""
                taches[i]["faite"] = True
                print("Tâche marquée comme faite.")
            else:
                print("Numéro de tâche invalide.")
        except ValueError:
            """Si l'entrée n'est pas un nombre affiche un message"""
            print("Entrée non valide.")

        """Supprimer une tâche"""
    elif choix == "4":
        if not taches:
            print("Aucune tâche à supprimer.")
            continue
        try:
            i = int(input("Numéro à supprimer : ")) - 1
            if 0 <= i < len(taches):
                """Supprime la tâche choisie et affiche son nom"""
                supprimee = taches.pop(i)
                print(f"Tâche supprimée : {supprimee['nom']}")
            else:
                print("Numéro de tâche invalide.")
        except ValueError:
            print("Entrée non valide.")

        """Quitter le programme"""
    elif choix == "5":
        """Affiche un message et sort de la boucle"""
        print("Au revoir !")
        break
    
def testfonction():
    """cette fonction est une fonction de test"""
    return "test"
