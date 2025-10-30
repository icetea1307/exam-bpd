taches = []

def afficher_menu():
    print("\n--- Gestionnaire de Todo ---")
    print("1. Ajouter une tâche")
    print("2. Lister les tâches")
    print("3. Marquer une tâche comme faite")
    print("4. Supprimer une tâche")
    print("5. Quitter")

while True:
    afficher_menu()
    choix = input("Choix : ")

    if choix not in ["1", "2", "3", "4", "5"]:
        print("Choix invalide.")
        continue

    if choix == "1":
        nom = input("Nouvelle tâche : ").strip()
        if not nom:
            print("Le nom de la tâche ne peut pas être vide.")
        else:
            taches.append({"nom": nom, "faite": False})
            print("Tâche ajoutée.")

    elif choix == "2":
        if not taches:
            print("Aucune tâche.")
        else:
            for i, t in enumerate(taches, 1):
                statut = "✅" if t["faite"] else "❌"
                print(f"{i}. {statut} {t['nom']}")

    elif choix == "3":
        if not taches:
            print("Aucune tâche à marquer.")
            continue
        try:
            i = int(input("Numéro de la tâche : ")) - 1
            if 0 <= i < len(taches):
                taches[i]["faite"] = True
                print("Tâche marquée comme faite.")
            else:
                print("Numéro de tâche invalide.")
        except ValueError:
            print("Entrée non valide.")

    elif choix == "4":
        if not taches:
            print("Aucune tâche à supprimer.")
            continue
        try:
            i = int(input("Numéro à supprimer : ")) - 1
            if 0 <= i < len(taches):
                supprimee = taches.pop(i)
                print(f"Tâche supprimée : {supprimee['nom']}")
            else:
                print("Numéro de tâche invalide.")
        except ValueError:
            print("Entrée non valide.")

    elif choix == "5":
        print("Au revoir !")
        break
