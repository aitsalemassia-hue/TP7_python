
from Mixins_Taches import Tache


if __name__ == "__main__":

    # Création
    t = Tache("Projet Python", "Version initiale")

    # Première modification
    t.mettre_a_jour("Travail commencé")

    # Deuxième modification
    t.mettre_a_jour("Travail terminé")

    # Afficher les informations
    print("\n Informations ")
    print("Titre :", t.titre)
    print("Description :", t.description)
    print("Date :", t.date_creation)

    # Afficher l'historique
    print("\n Historique ")
    t.afficher_historique()