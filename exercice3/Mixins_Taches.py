from datetime import datetime
class ValidationMixin:

     def valider_titre(self):
          if not self.titre or not self.titre.strip():
               raise ValueError("Le titre est obligatoire")


class HistoriqueMixin:

     def __init__(self):
          self.historique = []

     def enregistrer_version(self):
          self.historique.append(self.description)

     def afficher_historique(self):
          for i, version in enumerate(self.historique, 1):
               print(f"Version {i} : {version}")



class JournalisationMixin:

     def journaliser(self, message):
          print(f"[Journal] {datetime.now()} : {message}")



class Tache(ValidationMixin, HistoriqueMixin, JournalisationMixin):

     def __init__(self, titre, description):
          HistoriqueMixin.__init__(self)

          self.titre = titre
          self.description = description
          self.date_creation = datetime.now()

          self.valider_titre()
          self.journaliser("Création de la tâche")

     def mettre_a_jour(self, description):
          self.valider_titre()

          self.enregistrer_version()
          self.description = description

          self.journaliser("Modification de la tâche")