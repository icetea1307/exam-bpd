import logging

logging.basicConfig(
    filename="todo.log", 
    level=logging.DEBUG,  
    format="%(asctime)s - [%(levelname)s] - %(message)s"  
)

logging.info("Démarrage du gestionnaire de tâches")

taches = []

def afficher_menu():
    """Affiche le menu principal du programme"""
    print("\n--- Gestionnaire de Todo ---")
    print("1. Ajouter une tâche")
    print("2. Lister les tâches")
    print("3. Marquer une tâche comme faite")
    print("4. Supprimer une tâche")
    print("5. Quitter")

"""Boucle principale du programme"""
while True:
    afficher_menu()
    choix = input("Choix : ")

    """Vérification du choix saisi"""
    if choix not in ["1", "2", "3", "4", "5"]:
        print("Choix invalide.")
        logging.warning(f"Choix invalide saisi : {choix}")
        continue

    """Ajout d'une tâche"""
    if choix == "1":
        nom = input("Nouvelle tâche : ").strip()
        if not nom:
            print("Le nom de la tâche ne peut pas être vide.")
            logging.warning("Tentative d'ajout d'une tache vide.")
        else:
            taches.append({"nom": nom, "faite": False})
            print("Tâche ajoutée.")
            logging.info(f"Tache ajoutee : {nom}")

        """Affichage de la liste des tâches"""
    elif choix == "2":
        if not taches:
            print("Aucune tâche.")
            logging.info("Affichage des taches : aucune tache disponible.")
        else:
            for i, t in enumerate(taches, 1):
                statut = "✅" if t["faite"] else "❌"
                print(f"{i}. {statut} {t['nom']}")
            logging.info("Affichage de la liste des taches.")

        """Marquer une tâche comme faite"""
    elif choix == "3":
        if not taches:
            print("Aucune tâche à marquer.")
            logging.warning("Tentative de marquer une tache alors qu'il n'y en a aucune.")
            continue
        try:
            i = int(input("Numéro de la tâche : ")) - 1
            if 0 <= i < len(taches):
                taches[i]["faite"] = True
                print("Tâche marquée comme faite.")
                logging.info(f"Tache marquee comme faite : {taches[i]['nom']}")
            else:
                print("Numéro de tâche invalide.")
                logging.warning(f"Numero invalide lors du marquage : {i + 1}")
        except ValueError:
            print("Entrée non valide.")
            logging.error("Entree non numérique lors du marquage d'une tache.")
        except Exception as e:
            print("Erreur inattendue.")
            logging.critical(f"Erreur critique lors du marquage : {e}")

        """Suppression d'une tâche"""
    elif choix == "4":
        if not taches:
            print("Aucune tâche à supprimer.")
            logging.warning("Tentative de suppression sans taches disponibles.")
            continue
        try:
            i = int(input("Numéro à supprimer : ")) - 1
            if 0 <= i < len(taches):
                supprimee = taches.pop(i)
                print(f"Tâche supprimée : {supprimee['nom']}")
                logging.info(f"Tache supprimee : {supprimee['nom']}")
            else:
                print("Numéro de tâche invalide.")
                logging.warning(f"Numero invalide lors de la suppression : {i + 1}")
        except ValueError:
            print("Entree non valide.")
            logging.error("Entree non numérique lors de la suppression d'une tache.")
        except Exception as e:
            print("Erreur critique pendant la suppression.")
            logging.critical(f"Erreur critique lors de la suppression : {e}")

        """Quitter le programme"""
    elif choix == "5":
        print("Au revoir !")
        logging.info("Fermeture du programme.")
        break


def testfonction():
    """cette fonction est une fonction de test"""
    return "test"
