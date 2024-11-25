from .outil import Outil

class Tournevis(Outil):
    def __init__(self, sous_type, taille, etat="Dispo", emprunt="no", date_emprunt="", usage=0):
        super().__init__("Tournevis", sous_type, taille, etat, emprunt, date_emprunt, usage)
    
    def visser(self):
        self.increment_usage()
        print("Visser !")
    
    def devisser(self):
        self.increment_usage()
        print("Dévisser !")
