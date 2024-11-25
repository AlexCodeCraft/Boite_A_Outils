from .outil import Outil

class ClePlate(Outil):
    def __init__(self, taille, etat="Dispo", emprunt="no", date_emprunt="", usage=0):
        super().__init__("Clé Plate", "", taille, etat, emprunt, date_emprunt, usage)
    
    def utiliser(self):
        self.increment_usage()
        print(f"Utiliser la clé plate de taille {self.taille} !")
