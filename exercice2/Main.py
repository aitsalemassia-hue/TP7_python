
from Mixins_entreprise import Contrat


if __name__ == "__main__":

     # 1. Création du contrat
     print("\n Création ")
     contrat1 = Contrat(1, "Initial")
     print("Contrat créé :", contrat1.description)

     # 2. Journalisation
     print("\n Journalisation")
     contrat1.journaliser("Création du contrat")

     # 3. Modification
     print("\n Modification ")
     contrat1.modifier("Révisé")

     # 4. Afficher le contrat
     print("\n État actuel ")
     print(contrat1.description)

     # 5. Afficher l'historique
     print("\n Historique ")
     for date, etat in contrat1.historique:
          print("Date :", date)
          print("Ancienne description :", etat["description"])

     # 6. Conversion JSON
     print("\n Conversion JSON ")
     json_data = contrat1.to_json()
     print(json_data)

     # 7. Reconstruction depuis JSON
     print("\n Reconstruction JSON ")
     nouveau_contrat = Contrat.from_json(
          '{"id": 2, "description": "Nouveau contrat"}'
     )
     print(nouveau_contrat.id)
     print(nouveau_contrat.description)