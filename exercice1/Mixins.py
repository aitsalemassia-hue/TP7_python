from datetime import datetime
import json
from abc import ABC, abstractmethod
class Horodatable:
     def horodatage(self):
          print(f"[LOG] Action à {datetime.now()}")

class Validable:
     def valider(self):
          if not getattr(self, "titre", None):
               raise ValueError("Titre manquant")
          print("Validation OK")

class Serializable:
     def to_json(self):
          return json.dumps(self.__dict__, ensure_ascii=False)


class Historisable:

     def __init__(self):
          self.historique = []

     def ajouter_action(self, action):
          self.historique.append(action)

     def afficher_historique(self):
          print(self.historique)




class Document(Horodatable, Validable, Serializable, Historisable):
     def __init__(self, titre, contenu):
          self.titre = titre
          self.contenu = contenu
          self.historique = []
     def sauvegarder(self):
          self.horodatage()
          self.valider()
          self.ajouter_action("Sauvegarde du document")
          print(f"Document '{self.titre}' sauvegardé.")

