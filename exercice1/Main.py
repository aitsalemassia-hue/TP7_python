from Mixins import Document
if __name__ == "__main__":

    # Création du document
    doc = Document("Rapport", "Contenu important")

    #  Tester l'horodatage
    print("\n Horodatage ")
    doc.horodatage()

    #  Tester la validation
    print("\n Validation ")
    doc.valider()

    #  Tester la sérialisation JSON
    print("\n Conversion JSON ")
    print(doc.to_json())

    # Tester l'historique
    print("\n Historique ")
    doc.ajouter_action("Création du document")
    doc.ajouter_action("Modification du document")
    doc.ajouter_action("Sauvegarde du document")
    doc.afficher_historique()

    #  Tester la sauvegarde
    print("\n Sauvegarde ")
    doc.sauvegarder()